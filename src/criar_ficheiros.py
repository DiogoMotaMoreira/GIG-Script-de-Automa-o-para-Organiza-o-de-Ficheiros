import os
import random
from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas


# O que precisas:
#   Instalar as bibliotecas:
#       pip install pillow reportlab


def create_test_files(folder_path, num_files=100):
    os.makedirs(folder_path, exist_ok=True)

    def create_image(file_path):
        img = Image.new("RGB", (100, 100), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        draw = ImageDraw.Draw(img)
        draw.text((20, 40), "Img", fill="white")
        img.save(file_path)

    def create_pdf(file_path):
        c = canvas.Canvas(file_path)
        c.drawString(50, 500, "PDF Teste")
        c.showPage()
        c.save()

    def create_txt(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Ficheiro de texto para testes.\n" * 5)

    types = ['img', 'pdf', 'txt', 'vid', 'aud']

    for i in range(1, num_files + 1):
        t = random.choice(types)
        if t == 'img':
            create_image(os.path.join(folder_path, f"imagem_teste_{i}.png"))
        elif t == 'pdf':
            create_pdf(os.path.join(folder_path, f"documento_teste_{i}.pdf"))
        elif t == 'txt':
            create_txt(os.path.join(folder_path, f"nota_teste_{i}.txt"))
        elif t == 'vid':
            # ficheiro fictício vídeo (20 KB)
            with open(os.path.join(folder_path, f"video_teste_{i}.mp4"), "wb") as f:
                f.write(os.urandom(1024 * 20))
        elif t == 'aud':
            # ficheiro fictício áudio (10 KB)
            with open(os.path.join(folder_path, f"audio_teste_{i}.mp3"), "wb") as f:
                f.write(os.urandom(1024 * 10))

if __name__ == "__main__":
    folder = "ficheiros"
    create_test_files(folder, num_files=100)
    print(f"Criados 100 ficheiros na pasta '{folder}'.")
