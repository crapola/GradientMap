from PIL import Image
import config

def dither(x:int, y:int, i:float, v:float, base:int) -> int:
	""" v=number of values from base"""
	k=((1,3),(4,2))
	return base+(i*v)+ ( 1 if ((v*(i%(1./v))) +k[x%2][y%2]/4.)>=1 else 0 ) 

def main():
	image=Image.open("test.png")
	width=image.width
	height=image.height

	pixels=tuple(image.getdata())

	# Create list of values from red (since it's a greyscale image).
	intensities=[x[0] for x in pixels]
	#print(intensities)
	
	result_colors=[]

	for i,x in enumerate(intensities):
		g=x/255.0
		red=0#dither(i%width,int(i/width),g,config.size[0],config.base[0])
		green=dither(i%width,int(i/width),g,config.size[1],config.base[1])
		blue=dither(i%width,int(i/width),g,config.size[2],config.base[2])
		color=(int(red),int(green),int(blue))
		result_colors.append(color)

	#print(result_colors)
	# Destination image.
	result=Image.new('RGB',(width,height))
	result.putdata(result_colors)
	result.show()

if __name__=="__main__":
	main()