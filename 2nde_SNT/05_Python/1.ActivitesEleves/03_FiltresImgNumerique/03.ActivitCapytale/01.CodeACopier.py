from PIL import Image

image_en_cours = Image.open('LFC.jpg')
pixels = image_en_cours.load()

for i in range(image_en_cours.width):
    for j in range(image_en_cours.height):
        r, v, b = pixels[i, j]
    
        gris = int((r + v + b) / 3)
        pixels[i, j] = (gris,gris,gris)

image_en_cours.show()
