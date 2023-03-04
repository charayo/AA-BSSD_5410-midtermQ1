from SortFunctions import selection_sort, quicksort, quickSortIterative
from SearchFunctions import binary_search_sub
from PixelFunctions import storePixels, pixels_to_image, pixels_to_point, compare_pixels, grayscale
from PIL import Image, ImageDraw


def main():
    # getting user's desired threshold value
    # user_threshold = int(input("What threshold do you want to use? (Note: Integers only): "))
    user_threshold = 80
    IMG_NAME = 'comp'

    with Image.open(IMG_NAME + '.jpg') as im:
        with Image.open('editor.jpg') as imR:
            repPix = storePixels(imR)
        pixels = storePixels(im)
        print("stored", len(pixels))
        sorted_pixels = pixels.copy()
        # selection_sort(sorted_pixels, compare_pixels)
        quickSortIterative(sorted_pixels, 0, len(sorted_pixels)-1, compare_pixels)
        # print("sorted", sorted_pixels)
        # sorted_im = pixels_to_image(im, sorted_pixels)
        # sorted_im.save('sorted' + IMG_NAME + '.jpg', 'JPEG')
        threshold = user_threshold  # red to look for. Keep everything greater than this.
        subi = binary_search_sub([r[0][0] for r in sorted_pixels], 0, len(sorted_pixels)-1, threshold)
        print("sublist of reds starts at: ", subi)

        # grayscale(im, pixels)  # original pixels turned gray
        pixels_to_point(imR, sorted_pixels[subi:])
    # end with Image. open (IMG_NAME + ' jpg') as im:

    # save my image data from memory to a file with a different name
    im.save('highlighted' + IMG_NAME + '.jpg', 'JPEG')
# end def main()


if __name__ == "__main__":
    main()
