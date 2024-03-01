from PIL import Image
import random

def CreeImg(nb):
    # Créer une nouvelle image en mode RGB
    image = Image.new('RGB', (nb, nb))

    # Obtenir les données de l'image sous forme d'une liste
    pixels = image.load()

    # Définir une couleur aléatoire pour chaque pixel
    for i in range(image.width):
        for j in range(image.height):
            pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Sauvegarder l'image
    nm = "image_" + str(nb) + "x" + str(nb) + ".png"
    image.save(nm)

    # Afficher l'image
    image.show()

def AfficheNB(img):
    # Charger l'image
    image_en_cours = Image.open(img)
    pixels = image_en_cours.load()

    # Parcourir chaque pixel
    grossis(image_en_cours)
    input("Suite....")
    for i in range(image_en_cours.width):
        for j in range(image_en_cours.height):
            r, v, b = pixels[i, j]
            # Calculer la teinte de gris
            gris = int((r + v + b) / 3)
            pixels[i, j] = (gris,gris,gris)
            grossis(image_en_cours)
            input("Suite....")

def grossis(img_in, square_size=1000):
    # Charger l'image originale
    original_image = img_in
    original_pixels = original_image.load()

    # Créer une nouvelle image avec les dimensions étendues
    new_width = original_image.width * square_size
    new_height = original_image.height * square_size
    new_image = Image.new('RGB', (new_width, new_height))

    # Parcourir chaque pixel de l'image originale
    for i in range(original_image.width):
        for j in range(original_image.height):
            # Obtenir la couleur du pixel original
            pixel_color = original_pixels[i, j]

            # Dessiner un carré de 1000x1000 pixels avec cette couleur dans la nouvelle image
            for x in range(square_size):
                for y in range(square_size):
                    new_image.putpixel((i * square_size + x, j * square_size + y), pixel_color)

    # Afficher la nouvelle image
    new_image.show()

CreeImg(2)
AfficheNB('image_2x2.png')




def Tout(img):
    # Charger l'image
    image_en_cours = Image.open(img)
    pixels = image_en_cours.load()

    # GRIS
    # Parcourir chaque pixel
    for i in range(image_en_cours.width):
        for j in range(image_en_cours.height):
            r, v, b = pixels[i, j]

            # Calculer la teinte de gris
            gris = int((r + v + b) / 3)
            pixels[i, j] = (gris, gris, gris)

    image_en_cours.save('./LFCPix/LFC_Gris.jpg')

    # Charger l'image
    image_en_cours = Image.open(img)
    pixels = image_en_cours.load()

    # NEGATIF
    # Parcourir chaque pixel
    for i in range(image_en_cours.width):
        for j in range(image_en_cours.height):
            r, v, b = pixels[i, j]

            # Calculer la teinte de gris
            pixels[i, j] = (255 - r, 255 - v, 255 - b)

    image_en_cours.save('./LFCPix/LFC_Neg.jpg')

    # Charger l'image
    image_en_cours = Image.open(img)
    pixels = image_en_cours.load()

    # N&B
    # Parcourir chaque pixel
    for i in range(image_en_cours.width):
        for j in range(image_en_cours.height):
            r, v, b = pixels[i, j]

            # Calculer la teinte de gris
            gris = int((r + v + b) / 3)
            # test si plus près de noir que de blanc
            if gris > 255 // 2:
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0, 0, 0)

    image_en_cours.save('./LFCPix/LFC_NB.jpg')

    # Charger l'image
    image_en_cours = Image.open(img)
    pixels = image_en_cours.load()

    # Rouge Bourrin
    # Parcourir chaque pixel
    for i in range(image_en_cours.width):
        for j in range(image_en_cours.height):
            r, v, b = pixels[i, j]
            # Appliquer le filtre
            pixels[i, j] = (255, v, b)

    image_en_cours.save('./LFCPix/LFC_Rouge.jpg')

    # Charger l'image
    image_en_cours = Image.open(img)
    pixels = image_en_cours.load()

    # Vert majoritaire
    # Parcourir chaque pixel
    for i in range(image_en_cours.width):
        for j in range(image_en_cours.height):
            r, v, b = pixels[i, j]

            # Calculer la teinte de gris
            gris = int((r + v + b) / 3)
            if v == max(r, v, b):
                pixels[i, j] = (0, 255, 0)
            else:
                pixels[i, j] = (gris, gris, gris)

    image_en_cours.save('./LFCPix/LFC_Vert.jpg')
#Tout('./LFCPix/0.LFC.jpg')



def Tout2(img):
    # Charger l'image
    image_en_cours = Image.open(img)
    pixels = image_en_cours.load()

    # GRIS
    # Parcourir chaque pixel
    for i in range(image_en_cours.width):
        for j in range(image_en_cours.height):
            r, v, b = pixels[i, j]

            # Calculer la teinte de gris
            gris = int(r + v + b)
            pixels[i, j] = (gris, gris, gris)

    image_en_cours.save('./LFCPix/LFC_Gris2.jpg')

    # Charger l'image
    image_en_cours = Image.open(img)
    pixels = image_en_cours.load()

    # NEGATIF
    # Parcourir chaque pixel
    for i in range(image_en_cours.width):
        for j in range(image_en_cours.height):
            r, v, b = pixels[i, j]

            # Calculer la teinte de gris
            pixels[i, j] = (255 - r, v, b)

    image_en_cours.save('./LFCPix/LFC_NegPart.jpg')

    # Charger l'image
    image_en_cours = Image.open(img)
    pixels = image_en_cours.load()

    # N&B
    # Parcourir chaque pixel
    for i in range(image_en_cours.width):
        for j in range(image_en_cours.height):
            r, v, b = pixels[i, j]

            # Calculer la teinte de gris
            gris = int((r + v + b) / 3)
            # test si plus près de noir que de blanc
            if gris > 255 // 2:
                pixels[i, j] = (255, 0, 0)
            else:
                pixels[i, j] = (0, 0, 0)

    image_en_cours.save('./LFCPix/LFC_RB.jpg')

    # Charger l'image
    image_en_cours = Image.open(img)
    pixels = image_en_cours.load()

    # Rouge Bourrin
    # Parcourir chaque pixel
    for i in range(image_en_cours.width):
        for j in range(image_en_cours.height):
            r, v, b = pixels[i, j]

            # Calculer la teinte de gris
            gris = int((r + v + b) / 3)
            # test si plus près de noir que de blanc
            if gris > 255 // 2:
                pixels[i, j] = (255, 0, 255)
            else:
                pixels[i, j] = (0, 0, 0)

    image_en_cours.save('./LFCPix/LFC_RBl.jpg')

#Tout2('./LFCPix/0.LFC.jpg')