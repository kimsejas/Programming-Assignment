# CSCI-435-Programming-Assignment

# How to Run 
1. Clone this repo and open it an IDE of your choice
2. Run the command below to install the necessary libraries 
  
  ```
   pip install -r requirements.txt
  ```
3.  Run the highlightLeafNode.py file using the command below. The script will process the files and save new images with highlighted leaf nodes in the Programming-Assignment-New-PNG directory.

   ```
python highlightLeafNode.py
```
# Design Approach
My soluton was to parse the XML file using a library and find nodes that do not have any children. Parsing an XML was wrapped in a try-except so that if an error occured, the program can continue and an error message will print. Also, a library was used for efficiency. When a leaf node is found, the coordinates of its bounds are stored and used to draw rectangles on the png file. This was repeated for each file in the Programming-Assignment-Data folder.


# Libraries Used 
The following libraries were imported:
- xml.etree.ElementTree: For parsing the XML
- re: For creating regular expression
- os: For getting file XML and PNG pairs
- PIL (Pillow): For opening, drawing, and saving PNG images

 
