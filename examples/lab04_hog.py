#lab04_hog.py
from scipy.ndimage import filters
from PIL import Image
from pylab import *

def getHog(img, pos):
    '''to compute histogram of gradient at pos. 
    Note that this fucntion may access out of bound pixel'''
    sigma=1
    posx=int(pos[0][0])
    posy=int(pos[0][1])
    img8=img[posx-8:posx+8,posy-8:posy+8]
    imgx = zeros(img8.shape)
    filters.gaussian_filter(img8, (sigma,sigma), (0,1), imgx)
    imgy = zeros(img8.shape)
    filters.gaussian_filter(img8, (sigma,sigma), (1,0), imgy)
    theta=arctan2(imgy,imgx)
    t=4*(theta.flatten()/pi+1)
    t=t.astype(int)
    
    desc = zeros(8)
    desc=bincount(t,None,8)
    return desc



img = array(Image.open('img/graffiti.jpg').convert('L'))
set_cmap('gray')
imshow(img)
title('original image')
pos=ginput(1)

print getHog(img,pos)
