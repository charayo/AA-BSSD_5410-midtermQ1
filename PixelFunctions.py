from PIL import Image, ImageDraw


def compare_pixels(pix1, pix2):
    return pix1[0][0] <= pix2[0][0]  # only comparing red values
# def compare_pixels(pix1, pix2):


def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store pixels in a list
    pixel_array =[]
    for i in range(width):
        for j in range(height):
            # get r and g and b values of pixel at position
            r, g, b = im.getpixel((i, j))  # make an i,j tuple before passing
            pixel_array.append([(r, g, b), (i, j)])  # store pixels in double tuple
        # end for j
    # end for i
    return pixel_array  # send array back to main
# end def storePixels(im):


def pixels_to_image(im, pixels):
    outimg = Image.new("RGB", im.size)
    outimg.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg
# def pixels_to_image(im, pixels):


def pixels_to_point(im, pixels):
    # default background color is black
    for p in pixels:
        im.putpixel(p[1], p[0])
    im.show()
# def pixels_to_point(size, pixels):


def grayscale(im, pixels):
    draw = ImageDraw.Draw(im)
    for index, px in enumerate(pixels):
        if index < 20:
            print(px)
        gray_av = int((px[0][0] + px[0][1] + px[0][2]) / 3)
        draw.point(px[1], (0, 100, 0))
# def grayscale(im, pixels):
