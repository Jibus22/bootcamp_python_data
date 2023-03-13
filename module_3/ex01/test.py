from ImageProcessor import ImageProcessor

imgproc = ImageProcessor()
img = imgproc.load("42AI.png")

print(f"{repr(img)}")

if img is not None:
    imgproc.display(img)
