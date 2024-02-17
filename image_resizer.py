from PIL import Image

def resize_image(name,width,height,save_as):
    image=Image.open(name)
    print(f"before size: {image.size}")
    resize=image.resize((width,height))
    print(f"after size: {resize.size}")
    resize.save(save_as)

name=input("enter the name of the iamge file: ")
width=int(input("enter the width of image: "))
height=int(input("enter the height of image: "))
save_as=input("enter the name the image have to be saved: ")
resize_image(name,width,height,save_as)
