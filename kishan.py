# playing-with-PIL
changing pixel ,changing to grayscale
from PIL import Image
import numpy as np
import cv2
a=Image.open('lenna.png')
width,height=a.size
width
height
#changing size
b=a.resize((int(width/8),int(height/7)))
b.save('kishan.png')
b.size
#flip
b.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal.png')
#upside down
b.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')
#getting RGB values
colors=a.getpixel((240,320))
print(colors)
#converting into greyscale
c=Image.open('kishan.png').convert('LA')
c.save('kishangrey.png')
d=b.resize((int(width/8),int(height/8)))
d.save('reesize.png')
#checking pixels
img=Image.open('lenna.png')
#img=Image.new('RGB',(600,300),color=(73,109,137))
iar=np.asarray(img)
print(iar)
