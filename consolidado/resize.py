from pathlib import Path
from PIL import Image
import shutil

# pasta do próprio script (garante que é "a pasta em que ele está salvo")
BASE_DIR = Path(__file__).resolve().parent
OUT_DIR = BASE_DIR / "saida_640px"
OUT_DIR.mkdir(exist_ok=True)

MAX_DIM = 640  # maior dimensão desejada (lado maior)

def resize_png_keep_alpha(in_path: Path, out_path: Path, max_dim: int = MAX_DIM):
    with Image.open(in_path) as im:
        # Garante que temos canal alpha (transparência) de forma consistente
        if im.mode in ("RGBA", "LA"):
            src = im
        else:
            # Se for paleta (P) com transparência ou RGB, converte para RGBA para preservar alpha
            src = im.convert("RGBA")

        w, h = src.size
        maior = max(w, h)

        if maior <= max_dim:
            # já é menor/igual — copia sem mexer no tamanho
            src.save(out_path, format="PNG")
            return False  # não redimensionou

        escala = max_dim / float(maior)
        new_w = int(round(w * escala))
        new_h = int(round(h * escala))

        # Redimensiona com LANCZOS (alta qualidade), preservando alpha
        redim = src.resize((new_w, new_h), resample=Image.LANCZOS)
        redim.save(out_path, format="PNG")
        return True  # redimensionou

def main():
    pngs = sorted([p for p in BASE_DIR.iterdir() if p.is_file() and p.suffix.lower() == ".png"])
    if not pngs:
        print("Nenhuma imagem .png encontrada na pasta do script.")
        return

    count_resized = 0
    count_total = 0

    for p in pngs:
        count_total += 1
        out = OUT_DIR / p.name
        resized = resize_png_keep_alpha(p, out, MAX_DIM)
        print(f"[{'↓' if resized else '='}] {p.name} -> {out.name}")
        if resized:
            count_resized += 1

    print(f"\nConcluído! {count_resized}/{count_total} arquivo(s) foram redimensionados.")
    print(f"Arquivos salvos em: {OUT_DIR}")

if __name__ == "__main__":
    main()
