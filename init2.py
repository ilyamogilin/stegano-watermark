from factory import ImageFactory

path = 'images/Tulips.bmp'

message = 'abd'
factory = ImageFactory()
img = factory.createImage(path)
key = img.encrypt(message)
# print(key)
img.write()

factory = ImageFactory()
img2 = factory.createImage('images/new_Tulips.bmp')
message2 = img.decrypt(key)
print(message)

print(message2)
