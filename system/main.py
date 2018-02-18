import os
from sys import argv
import ImageProcessing
from PIL import ImageEnhance

if __name__ == '__main__':

    files = argv[1:]

    qntt_files = len(files)

    for i in range(qntt_files):

        img = ImageProcessing.Image.open(files[i])

        # Transform Image in Black and White 
        img = ImageProcessing.verify_bw(img)
        img_origin = img.copy()
        # Isolate the scoliosis column
        img = ImageProcessing.isolate_vertebral_column(img)
        # Cut the image
        img = ImageProcessing.crop_image(img)
        # Equalize the image
        img = ImageProcessing.histogram_equalize(img)
        # Isolate just or next the vertebral column
        img = ImageProcessing.isolate_scoliosis(img)
        img = ImageProcessing.median_filter(img, 2)
        img = ImageProcessing.histogram_equalize(img)
        img = ImageProcessing.median_filter(img, 4)
        img = ImageProcessing.sobel_filter(img)
        img = ImageProcessing.median_filter(img, 8)
        img = ImageProcessing.isolate_scoliosis(img)
        img = ImageProcessing.binary(img)
        img = ImageProcessing.trace_line(img)
        img = ImageProcessing.merge_images(img_origin, img)
        img.save("../results/{0}".format(files[i].split("/")[-1]))
        img.show()
