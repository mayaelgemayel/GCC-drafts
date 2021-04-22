#convolutions

#test with Gaëtan's code
from PIL import Image

image = Image.open("cat.jpg")       #Charger le fichier
pixelmap = image.load()             #Obtenir la matrice

for i in range(image.size[0]):
    for j in range(image.size[1]):
        (r, g, b) = pixelmap[i, j]     #Obtenir les composantes (r, g, b)
        pixelmap[i, j] = (0, g, b)     #SetPixel

image.save('output.png')               #Save output 