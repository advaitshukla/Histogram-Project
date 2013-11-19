import Tkinter
import Image, ImageTk, ImageDraw
import math

def histprint(hist):
	histHeight = 120            # Height of the histogram
	histWidth = 256             # Width of the histogram
	multiplerValue = 1.5
	showFstopLines = True
	fStopLines = 5

	# Colours to be used
	backgroundColor = (51,51,51)    # Background color
	lineColor = (102,102,102)       # Line color of fStop Markers 
	red = (255,60,60)               # Color for the red lines
	green = (51,204,51)             # Color for the green lines
	blue = (0,102,255)              # Color for the blue lines
	histMax = max(hist)
	xScale = float(histWidth)/len(hist)                     # xScaling
	yScale = float((histHeight)*multiplerValue)/histMax     # yScaling 


	im = Image.new("RGBA", (histWidth, histHeight), backgroundColor)   
	draw = ImageDraw.Draw(im)


	# Draw Outline is required
	if showFstopLines:    
		xmarker = histWidth/fStopLines
    	x =0
    	for i in range(1,fStopLines+1):
        	draw.line((x, 0, x, histHeight), fill=lineColor)
        	x+=xmarker
    	draw.line((histWidth-1, 0, histWidth-1, 200), fill=lineColor)
    	draw.line((0, 0, 0, histHeight), fill=lineColor)


	# Draw the RGB histogram lines
	x=0; c=0;
	for i in hist:
		if int(i)==0: pass
    	else:
        	color = red
        	if c>255: color = green
        	if c>511: color = blue
        	draw.line((x, histHeight, x, histHeight-(i*yScale)), fill=color)        
    	if x>255: x=0
    	else: x+=1
    	c+=1

	# Now save and show the histogram    
	im.save('histogram.png', 'PNG')
	im.show()


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
	histprint(hist)
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