import xml.etree.ElementTree as ET
from PIL import Image
Image.MAX_IMAGE_PIXELS = None


images =[]
tree = ET.parse('C:\\Users\\bluee\\Desktop\\CodingProjects\\testProjects\\XML animate\\a.xml')
root = tree.getroot()


for j,i in enumerate(root):
    print(i.attrib["x"],i.attrib["y"],i.attrib["width"],i.attrib["height"])
    im = Image.open("C:\\Users\\bluee\\Desktop\\CodingProjects\\testProjects\\XML animate\\zoe.png")
    crop_area=(int(i.attrib["x"]),int(i.attrib["y"]),int(i.attrib["width"])+int(i.attrib["x"]), int(i.attrib["height"])+int(i.attrib["y"]))
    print(crop_area)
    im1 = im.crop(crop_area)
    images.append(im1)
    im.close()

print(images)
images[0].save('XML animate\\out.gif', save_all=True, append_images=images[1:],duration=60,loop=1)