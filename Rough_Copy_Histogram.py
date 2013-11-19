import Tkinter
import Image, ImageTk, ImageDraw
import math

def showxy(event):
	data = event.x, event.y
	ca.bind('B1-Motion', lambda event, arg=data: dragging(event, arg))
	ca.bind('<ButtonRelease-1>', lambda mouse, arg=data: endxy(mouse, arg))
    	

def endxy(mouse, arg):
	mousex = mouse.x
	mousey = mouse.y
	img2 = Image.open(image_file)
	width = abs(arg[0] - mouse.x)
	height = abs(arg[1] - mouse.y)
	box = (arg[0], arg[1], width, height)
	cropped = img2.crop(box)
	cropped.show()
	hist = cropped.histogram()
	print ('Red          Blue            Green')
	for y in range(0, 256):
		print hist[y] + 1 , ' : ' , hist[y] , ' | ' , hist[y + 256] , ' | ' , hist[y + 512] 
#	print hist

def dragging(event, arg):
	width = abs(arg[0] - event.x)
	height = abs(arg[1] - event.y)
	transparent_box = (arg[0], arg[1], width, height)
	
	mask=Image.new('L', img.size, color=255)
	draw=ImageDraw.Draw(mask) 
	draw.rectangle(transparent_area, fill='light blue')
	img.putalpha(mask)
	img.paste(draw, mask)

image_file = "coat.png"

w = Tkinter.Tk()

img = Image.open(image_file)
width = img.size[0]
height = img.size[1]
ca = Tkinter.Canvas(w, width=width, height=height)
ca.pack()
photoimg = ImageTk.PhotoImage(img)
ca.create_image(width//2,height//2, image=photoimg)
ca.bind('<Button-1>', showxy)
Tkinter.mainloop()