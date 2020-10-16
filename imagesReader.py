def readBigInt(file):
    return int.from_bytes(file.read(4), byteorder='big')
def readInt(file):
    return int.from_bytes(file.read(1), byteorder='big')

def getLabels(labelFile):
    magicNumber = readBigInt(labelFile)
    itemsAmount = readBigInt(labelFile)
    labels = []
    for i in range(itemsAmount):
        labels.append(readInt(labelFile))
    return labels

def getImages(imageFile):
    magicNumber = readBigInt(imageFile)
    itemsAmount = readBigInt(imageFile)
    rows = readBigInt(imageFile)
    columns = readBigInt(imageFile)
    images = []
    for i in range(itemsAmount):
        images.append(imageFile.read(rows*columns))
    return images

def getImagesWithLabels(labelFile, imageFile):
    labels = getLabels(labelFile)
    images = getImages(imageFile)
    imagesWithLabels = []
    for i in range(len(labels)):
        label = labels[i]
        image = images[i]
        imagesWithLabels.append(ImageWithLabel(image, label))
    return imagesWithLabels

class ImageWithLabel:
    def __init__(self, image, label):
        self.image = image
        self.label = label