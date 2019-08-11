from PIL import Image

def dither(x:int, y:int, i:float, v:float, off:int) -> int:
	""" off=base """
	k=((1,3),(4,2))
	return off+(i*v)+ ( 1 if ((v*(i%(1./v))) +k[x%2][y%2]/4.)>=1 else 0 ) 

def main():
	image=Image.open("test.png")
	#image.show()
	pixels=tuple(image.getdata())
	#print(pixels)
	intensities=[x[0] for x in pixels]
	print(intensities)
	
	result=Image.new('RGB',(256,256))
	result.putdata(intensities)
	result.show()

	w=h=4

	for x in range(w):
		for y in range(h):
			for i in [x/10.0 for x in range(10)]:
				#print(i)
				print(dither(0,0,i,20,32),end=' ')
	pass

if __name__=="__main__":
	main()