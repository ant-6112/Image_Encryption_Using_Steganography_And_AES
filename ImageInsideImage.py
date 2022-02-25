from PIL import Image
import click

class Steganography:

    def __int_to_bin(rgb):
        r, g, b = rgb
        return (f'{r:08b}',
                f'{g:08b}',
                f'{b:08b}')


    def __bin_to_int(rgb):
        r, g, b = rgb
        return (int(r, 2),
                int(g, 2),
                int(b, 2))

    def __merge_rgb(rgb1, rgb2):
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2
        rgb = (r1[:4] + r2[:4],
               g1[:4] + g2[:4],
               b1[:4] + b2[:4])
        return rgb

    def merge(img1, img2):
        if img2.size[0] > img1.size[0] or img2.size[1] > img1.size[1]:
            raise ValueError('Image 2 should not be larger than Image 1!')

        pixel_map1 = img1.load()
        pixel_map2 = img2.load()

        new_image = Image.new(img1.mode, img1.size)
        pixels_new = new_image.load()

        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                rgb1 = Steganography.__int_to_bin(pixel_map1[i, j])

                rgb2 = Steganography.__int_to_bin((0, 0, 0))

                if i < img2.size[0] and j < img2.size[1]:
                    rgb2 = Steganography.__int_to_bin(pixel_map2[i, j])

                rgb = Steganography.__merge_rgb(rgb1, rgb2)

                pixels_new[i, j] = Steganography.__bin_to_int(rgb)

        return new_image

    def unmerge(img):
        pixel_map = img.load()

        new_image = Image.new(img.mode, img.size)
        pixels_new = new_image.load()

        original_size = img.size

        for i in range(img.size[0]):
            for j in range(img.size[1]):

                r, g, b = Steganography.__int_to_bin(pixel_map[i, j])

                rgb = (r[4:] + '0000',
                       g[4:] + '0000',
                       b[4:] + '0000')

                rgb3 = ('1111' + r[4:], 
                       '1111' + g[4:], 
                       '1111' + b[4:])

                rgb2 = ('1111' + r[:4], 
                       '1111' + g[:4], 
                       '1111' + b[:4])

                pixels_new[i, j] = Steganography.__bin_to_int(rgb)

                if pixels_new[i, j] != (0, 0, 0):
                    original_size = (i + 1, j + 1)

        new_image = new_image.crop((0, 0, original_size[0], original_size[1]))

        return new_image

    

