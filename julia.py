import cmath
from PIL import Image


PHI_D = 145
MAG = 30
JULIA = cmath.rect(MAG/100,(PHI_D/180)*cmath.pi)
JULIA = -0.7 + 0.27015j
screen = (1000,1000)
terry = Image.open("cropped3.jpg")
terrys = [0,0,0,0]
terrys[0] =((screen[0]/2-(terry.size[0]-1)/2)-100)/(screen[0]/2)-1 
terrys[1] = ((screen[0]/2+(terry.size[0]-1)/2)-100)/(screen[0]/2)-1
terrys[2] = ((screen[1]/2-(terry.size[1]-1)/2)-100)/(screen[1]/2)-1
terrys[3] = ((screen[1]/2+(terry.size[1]-1)/2)-100)/(screen[1]/2)-1
MAX_ITER = 100

canvas = Image.new('RGB',screen)
count = 0
perc = 0
for x in range(0,screen[0]):
    for y in range(0,screen[1]):
        num = (x/(screen[0]/2)-1,y/(screen[1]/2)-1)
        z = complex(num[0],num[1])
        color = (0,0,0)
        hit = False
        for i in range(0,MAX_ITER):
            count = i
            z = pow(z,2) + JULIA
            if z.real >terrys[0] and z.real <terrys[1] and hit == False:
                if z.imag > terrys[2] and z.imag<terrys[3]:
                    x2 = int((z.real+1)*(screen[0]/2)-(screen[0]/2-terry.size[0]/2)+100)
                    y2 = int((z.imag+1)*(screen[1]/2)-(screen[1]/2-terry.size[1]/2)+100)
                    color = terry.getpixel((x2,y2))
                    hit = True
            if abs(z) > 2:
                color = (0,0,0)
                break
        if abs(z) > 2:
            canvas.putpixel((x,y),color)
            #canvas.putpixel((x,y),(int(255*(count/MAX_ITER)),int(255*(count/MAX_ITER)),int(255*(count/MAX_ITER))))
        else:
            canvas.putpixel((x,y),color)
    perc +=1
    if perc == 10:
        print(x/screen[0]*100)
        perc = 0
canvas.show()
        
        
