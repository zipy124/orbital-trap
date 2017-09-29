import cmath
from PIL import Image


PHI_D = float(input("input angle in terms of pi:"))
MAG = float(input("input magnitude:"))
JULIA = cmath.rect(MAG,PHI_D)
screen = (int(input("x size:")),int(input("y size:")))
trap = Image.open(input("filename:"))
corners = [0,0,0,0]
trap_back = Image.new('RGB',screen)
xp = int(input("x image offset:"))
yp= int(input("y image offset:"))
trap_back.paste(trap,(xp,yp))
corners[0] =xp/(screen[0]/2)-1 
corners[1] = (xp+trap.size[0])/(screen[0]/2)-1
corners[2] = yp/(screen[1]/2)-1
corners[3] = (yp+trap.size[1])/(screen[1]/2)-1
MAX_ITER = int(input("Iterations: "))

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
            if z.real >corners[0] and z.real <corners[1] and hit == False:
                if z.imag > corners[2] and z.imag<corners[3]:
                    x2 = int((z.real+1)*(screen[0]/2))
                    y2 = int((z.imag+1)*(screen[1]/2))
                    color = trap_back.getpixel((x2,y2))
                    hit = True
            if abs(z) > 2:
                color = (0,0,0)
                break
        if abs(z) > 2:
            canvas.putpixel((x,y),color)
        else:
            canvas.putpixel((x,y),color)
    perc +=1
    if perc == 20:
        print(str(x/screen[0]*100)+"%")
        perc = 0
canvas.show()
        
        
