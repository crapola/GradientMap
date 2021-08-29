from PIL import Image
import numpy as np
import config

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
	# Pixels and indices as numpy arrays.
	v=np.array(values)/255.0
	i=np.arange(len(v))
	# Dithering.
	k=np.array((0,2,3,1))
	thresholds=np.take(k,i%2+2*((i//width)%2))/4.0-0.5
	# Create colors.
	params=np.array((config.base,config.size)).reshape(2,3,1)
	rgb=(params[0]+params[1]*v+thresholds).astype(int)
	rgb=np.stack(rgb,1)
	result_colors=[tuple(x) for x in rgb.tolist()]
	# Save destination image.
	result=Image.new('RGB',image.size)
	result.putdata(result_colors)
	result.show()
	result.save("result.png")
	print_value_range(result)

if __name__=="__main__":
	main()