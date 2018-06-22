#Application for image compamparer
from PIL import Image
import numpy as np

i=Image.open('images/dot1.png')
num1=np.asarray(i)

j=Image.open('images/dot3.png')
num2=np.asarray(j)

first=str(num1)
second=str(num2)

if first == second:
    print ("exists")
else:
    print ("Not exists")

