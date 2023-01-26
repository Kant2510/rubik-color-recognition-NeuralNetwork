import io
import cv2
import base64
import numpy as np
from PIL import Image


def stringToImage(base64_string):
    imgdata = base64.b64decode(base64_string)
    imgPIL = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(imgPIL), cv2.COLOR_BGR2RGB)
