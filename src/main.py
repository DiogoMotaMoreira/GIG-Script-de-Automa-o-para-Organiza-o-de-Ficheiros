import os
import shutil

def ver_pastas(caminho):
    for nome_arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, nome_arquivo)
        if os.path.isdir(caminho_completo):
            pastas.append(nome_arquivo)

def ver_ficheiros(caminho):
    for nome_arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, nome_arquivo)
        if os.path.isfile(caminho_completo):
            _, extensao = os.path.splitext(nome_arquivo)
            if extensao in pastas:
                destino = os.path.join(caminho, extensao)
                shutil.move(caminho_completo, os.path.join(destino, nome_arquivo))
            else:
                os.mkdir(os.path.join(caminho, extensao))
                pastas.append(extensao)
                destino = os.path.join(caminho, extensao)
                shutil.move(caminho_completo, os.path.join(destino, nome_arquivo))

if __name__ == "__main__":
    caminho = input("Insira o caminho da pasta: ")
    pastas = []
    ver_pastas(caminho)
    ver_ficheiros(caminho)

