from PIL import Image
from pylab import *
import numpy as np

# read image to array
im = array(Image.open('img/square0.jpg'))
# plot the image
imshow(im)
show()
n=5
#q=[[qx,qy]]
q=np.array([ [0.0, 0.0, 1.0],[10.0, 0.0, 1.0], [10.0,10.0,1.0], [0.0, 10.0,1.0], [5.0,5.0,1.0]])
gin_rc=ginput(n)

print gin_rc

#M = 0 0 0 pwqx pwqy pw pvqx pvqy pv
#    pwqx pwqy pw 0 0 0 puqx puqy pu
M=[]
          
for i in range(4):
    qx=q[i,0]
    qy=q[i,1]
    pv=gin_rc[i][1]
    pu=gin_rc[i][0]
    
    M.append([0, 0, 0, qx, qy, 1, pv*qx, pv*qy, pv, qx, qy, 1, 0, 0, 0, pu*qx, pu*qy, pu])
    print(0, 0, 0, qx, qy, 1, pv*qx, pv*qy, pv)
    print(qx, qy, 1, 0, 0, 0, pu*qx, pu*qy, pu)

A=np.array(M).reshape(-1,9)
U,s,V=np.linalg.svd(A)

#H=H11 H12 H13 H21 H22 H23 H31 H32 H33
H=np.reshape(V[:,-1],(3,3))
p_new=np.dot(H,q.T)
p_new=p_new/p_new[2,:]
plot(p_new[0,:],p_new[1,:],'*b')