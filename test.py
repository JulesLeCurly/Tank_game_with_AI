from PIL import Image
import colorsys

def to_grayscale_hsv(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]

            if a == 0:
                continue

            # RGB → HSV
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

            # Pour du noir et gris :
            # - saturation = 0
            # - luminosité (v) reste identique
            s = 0.0 

            # HSV → RGB
            r2, g2, b2 = colorsys.hsv_to_rgb(h, s, v)

            pixels[x, y] = (int(r2*255), int(g2*255), int(b2*255), a)

    img.save(output_path)
    print(f"[OK] {output_path} créé.")


to_grayscale_hsv("lifeheart_red.png", "lifeheart_gray.png")

