from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

imgproc = ImageProcessor()
# img = imgproc.load("42AI.png")
img = imgproc.load("elon.png")

cf = ColorFilter()

# print(img)
# print(50 * '-')

blue_img = cf.to_blue(img)
green_img = cf.to_green(img)
red_img = cf.to_red(img)
inverted_img = cf.invert(img)
cel_img = cf.to_celluloid(img)
gsc_img = cf.to_grayscale(img, 'w', weight=[.2, .7, .1])
gsc_img_r = cf.to_grayscale(img, 'w', weight=[1., .0, .0])
gsc_img_g = cf.to_grayscale(img, 'w', weight=[0., 1., .0])
gsc_img_b = cf.to_grayscale(img, 'w', weight=[0., .0, 1.])
gsc_m_img = cf.to_grayscale(img, 'm')

imgproc.display(img)
imgproc.display(blue_img)
imgproc.display(green_img)
imgproc.display(red_img)
imgproc.display(inverted_img)
imgproc.display(cel_img)
imgproc.display(gsc_img)
imgproc.display(gsc_img_r)
imgproc.display(gsc_img_g)
imgproc.display(gsc_img_b)
imgproc.display(gsc_m_img)
