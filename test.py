from PIL import Image

# -------- CONFIG --------
input_path = "Images/Tank.png"          # Image d'origine
output_path = "Tank_red.png"      # Image transformée en rouge
# ------------------------

# Charger l'image
img = Image.open(input_path).convert("RGBA")
pixels = img.load()

for y in range(img.height):
    for x in range(img.width):
        r, g, b, a = pixels[x, y]

        # Détection d'un pixel vert (inclut les dégradés)
        if g > r * 1.2 and g > b * 1.2 and g > 30:

            # Transformer le vert en rouge en gardant l'intensité du vert
            new_r = g                     # rouge basé sur la luminosité du vert
            new_g = int(g * 0.3)          # réduit pour ne pas garder du vert
            new_b = int(b * 0.3)          # légèrement réduit

            pixels[x, y] = (new_r, new_g, new_b, a)

# Sauvegarde
img.save(output_path)
print("Image générée :", output_path)