from PIL import Image
import os


def compress_images(image_folder):
    try:
        for file in os.listdir(image_folder):
            file_name, file_extension = os.path.splitext(image_folder + file)
            print('Comprimiendo archivo ' + file_name + file_extension)

            if file_extension == '.jpg':
                file_compress = Image.open(image_folder+file)
                file_compress.save(file_name+'_comprimido.jpg', optimize=True, quality=50)

    except:
        print("no se comprimio")


if __name__ == '__main__':
    compress_images('C:/Users/c_seg/OneDrive/Imágenes/imagenes_a_comprimir/')  # carpetas con imagenes que se desan comprimir
