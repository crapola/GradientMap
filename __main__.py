from PIL import Image
import config

def dither(x,y,i,v,base):
	"""
	Dither a color component.
	Parameters
	----------
	x,y : int
		Pixel position.
	i : float
		Pixel value in range [0,1].
	v
		Number of values from base.
	base : int
		Base value for this component.
	Returns
	-------
	int
		Component value in range [0,255].
	"""
	k=((1,3),(4,2))
	if v==0:
		return base+(i*v)
	return base+(i*v)+ ( 1 if ((v*(i%(1./v))) +k[x%2][y%2]/4.)>=1 else 0 ) 

def print_value_range(image):
	values=tuple(image.getdata())
	print(f"Value range: {(min(values),max(values))}.")

def main():
	image=Image.open("source.png").convert("L")
	print_value_range(image)
	# Convert.
	result_colors=[]
	values=tuple(image.getdata())
	width=image.width
	height=image.height
	for i,x in enumerate(values):
		v=x/255.0
		red=dither(i%width,int(i/width),v,config.size[0],config.base[0])
		green=dither(i%width,int(i/width),v,config.size[1],config.base[1])
		blue=dither(i%width,int(i/width),v,config.size[2],config.base[2])
		color=(int(red),int(green),int(blue))
		result_colors.append(color)
	# Save destination image.
	result=Image.new('RGB',image.size)
	result.putdata(result_colors)
	result.show()
	result.save("result.png")
	print_value_range(result)

if __name__=="__main__":
	main()