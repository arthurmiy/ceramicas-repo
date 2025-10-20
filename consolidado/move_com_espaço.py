import os
import shutil

def mover_arquivos_com_espaco():
    # Caminho da pasta onde o script está
    pasta_base = os.path.dirname(os.path.abspath(__file__))
    pasta_destino = os.path.join(pasta_base, "com_espaco")

    # Cria a pasta de destino se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Contador de arquivos movidos
    movidos = 0

    # Percorre todos os arquivos na pasta base (não inclui subpastas)
    for arquivo in os.listdir(pasta_base):
        caminho_arquivo = os.path.join(pasta_base, arquivo)

        # Verifica se é arquivo e se o nome contém espaço
        if os.path.isfile(caminho_arquivo) and " " in arquivo:
            novo_caminho = os.path.join(pasta_destino, arquivo)

            # Move o arquivo
            shutil.move(caminho_arquivo, novo_caminho)
            print(f"Movido: {arquivo}")
            movidos += 1

    print(f"\n✅ Total de arquivos movidos: {movidos}")
    print(f"📁 Destino: {pasta_destino}")

if __name__ == "__main__":
    mover_arquivos_com_espaco()
