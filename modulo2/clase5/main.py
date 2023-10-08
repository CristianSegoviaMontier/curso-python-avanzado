from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw



def get_image(image_file):
    try:
        image = Image.open(image_file)
        print(image.size)
        print(image.mode)
        print(image.format)

        # image.show()

        # image_blakwhite = image.convert('L')
        # image_blakwhite.show()
        # image_blakwhite.save('avatar_bn.png')

        # agrego logo:
        font = ImageFont.truetype('fonts/Roboto/Roboto-Bold.ttf',136)
        draw = ImageDraw.Draw(image)
        draw.text(
            (1,1),
            "AVATAR",
            (255,255,255),
            font
        )

        image.show()
        image.save('avatar_con_logo.png')

        # Crear un thumbnail:
        image.thumbnail((250,250))
        image.show()
        image.save('avatar_th.png')



    except:
        print('No hay imagen')


if __name__ == '__main__':
    get_image('Avatar_CFSM_01.png')
