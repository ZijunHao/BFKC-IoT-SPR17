from io import BytesIO
from time import sleep
from picamera import PiCamera
from datetime import datetime
import io
import os

# *** Hides personal information for privacy concern
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/pi/iotproject-************.json"

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
vision_client = vision.Client(project='iotproject')

# Pre-stored standard RGBs for rare, medium and well-done
COLOR_LIBRARY = [[156, 82, 75],
                 [190, 113, 97],
                 [158, 120, 88]]


def zero_to_rare(minI):
    return{
        0:'rare',
        1:'medium',
        2:'well done',
        }[minI]


def init_camera():
    camera = PiCamera()

    # Clear the folder before taking pictures to avoid running out of memory
    filelist = [f for f in os.listdir("/home/pi/Desktop/Project/photo_library")]
    if filelist:
        for f in filelist:
            try:
                os.remove("/home/pi/Desktop/Project/photo_library/" + f)
            except Exception as e:
                print e
    return camera


def take_photo(camera):
    # Create an in-memory stream and send to Google Vision client
    try:
        my_stream = BytesIO()
        camera.capture('/home/pi/Desktop/Project/photo_library/{:%Y%m%d%H%M%S}.jpg'.format(datetime.now()))
        camera.capture(my_stream, 'jpeg')
        bytescontent = my_stream.getvalue()
        image = vision_client.image(content=bytescontent)
        my_stream.flush()
        return image
    except Exception as e:
        print e


def what_is_it():
    camera = init_camera()
    label_list = []

    for i in range(3):
        image = take_photo(camera)

        # Performs label detection on the image file
        labels = image.detect_labels()
        i_label = 0
        for label in labels:
            if i_label < 3:     #Get only the first three labels
                label_list.append(label.description)
                i_label = i_label +1
        sleep(1)

    label_set = set(label_list)
    ret = list(label_set)
    return ret    #list type


def well_done():
    camera = init_camera()
    color_list = []

    for i in range(3):
	    image = take_photo(camera)
        props = image.detect_properties()
        tr = 0

        # Find the color that has large R value comparing to G & B component
        for color in props.colors:
            r = color.color.red
            g = color.color.green
            b = color.color.blue
            if tr < ((r-g)**2 + (r-b)**2)**0.5:
                tr = r
                tg = g
                tb = b

        color_list.append(tr)
        color_list.append(tg)
        color_list.append(tb)

    #Get the mean RGB value
    red = (color_list[0]+color_list[3]+color_list[6])/3
    green = (color_list[1]+color_list[4]+color_list[7])/3
    blue = (color_list[2]+color_list[5]+color_list[8])/3

    #Compare with standard RGBs for rare, medium and well-done
    minD = 1000
    minI = 0
    for i in range(3):
        RGB = COLOR_LIBRARY[i]
        # Euclidean norm
        D = ((red-RGB[0])**2+(green-RGB[1])**2+(blue-RGB[2])**2)**0.5
        if D < minD:
            minD = D
            minI = i
    doneness = zero_to_rare(minI)
    return doneness     #str type


if __name__ == "__main__":
    what_is_it()
    sleep(12)
    well_done()
