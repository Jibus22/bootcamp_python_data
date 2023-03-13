import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()

print(f"\nCROP {70 * '-'}")
arr1 = np.arange(0,25).reshape(5,5)
print(f"arr1: {arr1}", end="\n-\n")
print(spb.crop(arr1, (3,1),(1,0)))
# Output :
# array([[ 5],
#        [10],
#        [15]])

print(f"\nTHIN {70 * '-'}")
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(f"arr2: {arr2}", end="\n-\n")
print(spb.thin(arr2,3,0))
#Output :
# array([[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
#        [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
#        [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
#        [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
#        [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
#        [’A’, ’B’, ’D’, ’E’, ’G’, ’H’]], dtype=’<U1’)
print(spb.thin(arr2,3,1))

print(f"\nJUXTAPOSE {70 * '-'}")
arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(f"arr3: {arr3}", end="\n-\n")
print(spb.juxtapose(arr3, 3, 1))
#Output :
# array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
#        [1, 2, 3, 1, 2, 3, 1, 2, 3],
#        [1, 2, 3, 1, 2, 3, 1, 2, 3]])
print(spb.juxtapose(arr3, 2, 0))

print(f"\nMOSAIC {70 * '-'}")
print(spb.mosaic(arr3, (2, 5)))
print(spb.mosaic(arr3, (6, 1)))



print(f"\nMISC {70 * '-'}")

from ImageProcessor import ImageProcessor

imgproc = ImageProcessor()
img = imgproc.load("42AI.png")

mosaic_img = spb.mosaic(img, (3, 5))
juxtapose_img = spb.juxtapose(img, 3, 1)
thin_img = spb.thin(img, 2, 1)
crop_img = spb.crop(img, (140,140),(30,50))

imgproc.display(mosaic_img)
imgproc.display(juxtapose_img)
imgproc.display(thin_img)
imgproc.display(crop_img)
