#Using redis concept to store the immage array and display
import redis
from PIL import Image
from numpy import array
img=Image.open("/home/aatmaj/Desktop/asa.png")
arr=array(img)
r =  redis.StrictRedis(host="localhost",port=6379,db=0)
r.set("build1",arr)
#the image is converted to matrix and it is stored 
#------------------------------------
#a=r.get("build1") -> a gets the array in list form 
#import numpy as np
#m=np.asarray(a) ->converted the list into array
#type(m)
#<class 'numpy.ndarray'> ->
#from scipy.misc import toimage 
#toimage(m).show()

