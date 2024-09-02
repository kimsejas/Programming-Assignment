import xml.etree.ElementTree as ET
import re
import os
from PIL import Image, ImageDraw

def main():
    filenames = getInputs()
    for filename in filenames:
        leafNodeBounds = getLeafNodeBounds(filename)
        if leafNodeBounds:
            drawNewPng(filename, leafNodeBounds)


def getInputs():
    entries = os.listdir('Programming-Assignment-Data/')
    filenames = set()
    for entry in entries:
        if not entry.startswith('.'):
            filenames.add(entry[:-4])
    return filenames

def getLeafNodeBounds(filename):
    try:
        tree = ET.parse("Programming-Assignment-Data/" + filename + ".xml")
        root = tree.getroot()
        leafNodeBounds = []
        for node in root.iter():
            if len(node) == 0:
                bounds = re.split(r'\D+', node.attrib["bounds"])[1:-1]
                topLeft = (int(bounds[0]), int(bounds[1]))
                bottomRight = (int(bounds[2]), int(bounds[3]))
                leafNodeBounds.append([topLeft,bottomRight])
        return leafNodeBounds
    except ET.ParseError as error:
        print("Error parsing", filename, "XML: ", error)

def drawNewPng(filename, leafNodeBounds):
    with Image.open("Programming-Assignment-Data/" + filename + ".png") as image:
        draw = ImageDraw.Draw(image)
        for coords in leafNodeBounds:
            draw.rectangle(coords, fill=None, outline=(255,237,41,255), width=10)
        image.save(fp = "Programming-Assignment-New-PNG/" + filename + ".png")

if __name__ == "__main__":
    main()




