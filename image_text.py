import pytesseract 
import cv2
import tempfile
from PIL import Image
import re


def set_image_dpi(file_path):
    im = Image.open(file_path)
    length_x, width_y = im.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False,   suffix='.png')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(300, 300))
    
    return temp_filename

class extraction:
    def extract_time_hhmmss(self, read_string):
        hhmmss = re.search("(([0]?[1-9]|1[0-2])(:)([0-5][0-9])(:)([0-5][0-9]))", read_string)
        if(hhmmss):
            return hhmmss.group()

    def extract_time_mmss(self, read_string):
        mmss = re.search("(([0-5][0-9])(:)([0-5][0-9]))", read_string)
        if(mmss):
            return mmss.group()

    def extract_time_hm(self, read_string):
        hm = re.search("(\d{1,2}h\s\d{1,2}m(\s)?\d{1,2}s)|(\d{1,2}[dm](\s)?\d{1,2}s)|(\d{1,2}h(\s)?\d{1,2}[ms])|(\d{1,2}[hms]){5,}", read_string)
        if(hm):
            return hm.group()

    def extract_dist(self, read_string):
        dist = re.search("\d+\.\d{0,2}", read_string)
        if(dist):
            return dist.group()

class category:
    def strava(self, img):
        #print(pytesseract.image_to_string(img))

        #just making sure top of screenshot is cutout
        img = img[500:20000, 0:1000]
        e = extraction()
        #if time is in hhmmss format
        if(e.extract_time_hhmmss(pytesseract.image_to_string(img))):
            print("\npossible time taken in hhmmss : ", e.extract_time_hhmmss(pytesseract.image_to_string(img)))
        
        #if time is in 00h00m00s format
        else:
            print("\npossible time taken in hm : ", e.extract_time_hm(pytesseract.image_to_string(img)))

        #distance in decimal format
        print("\n\npossible distance covered : ", e.extract_dist(pytesseract.image_to_string(img)))




scaledImage = set_image_dpi("/home/abhilashak2k/Townscript/ImageText/strava5.jpg")
img = cv2.imread(scaledImage)
cat = category()
#img = image[500:20000, 0:1000]
# cv2.imshow("img", img)
# cv2.waitKey(5000)


#if strava
cat.strava(img)

#if nike







