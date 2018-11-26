import numpy as np
from PIL import Image

list_images = ['./Full_Size_Images/TUPAC-TE-319.svs_01_01.png', './Full_Size_Images/TUPAC-TE-319.svs_01_02.png']

images = [Image.open(i) for i in list_images] #Store a list of open images
# use pillow to achieve this...

# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in images])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in images ) )

# save that beautiful picture
imgs_comb = Image.fromarray( imgs_comb)
imgs_comb.save( 'Combined.png' )

