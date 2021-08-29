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
	v=np.array(values)/255.0
	i=np.arange(len(v))
	# Dithering.
	k=np.array((0,2,3,1))
	thresholds=np.take(k,i%2+2*((i//width)%2))/4.0-0.5
	# Channels.
	rs=(config.base[0]+config.size[0]*v+thresholds).astype(int)
	gs=(config.base[1]+config.size[1]*v+thresholds).astype(int)
	bs=(config.base[2]+config.size[2]*v+thresholds).astype(int)
	reds=rs.tolist()
	greens=gs.tolist()
	blues=bs.tolist()
	result_colors=tuple(zip(reds,greens,blues))
	# Save destination image.
	result=Image.new('RGB',image.size)
	result.putdata(result_colors)
	result.show()
	result.save("result.png")
	print_value_range(result)

if __name__=="__main__":
	main()