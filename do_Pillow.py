from PIL import Image,ImageFilter

im = Image.open("D:\\GIT_other\\test.png")
w,h=im.size
print("Original image size  : %sx%s" % (w , h))

im.thumbnail((w//2,h//2))
print("Resize image to: %sx%s" % (w//2,h//2))

im.save("D:\\GIT_other\\thumbnail.jpg" , "jpeg")

im2 = Image.open("D:\\GIT_other\\test.png")
im3=im2.filter(ImageFilter.BLUR)
im3.save('D:\\GIT_other\\blur.jpg', 'jpeg')