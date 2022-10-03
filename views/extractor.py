import cv2 as cv
import pytesseract
from flask_restful import Resource, reqparse
import werkzeug
import numpy as np


class Extract(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("image", type=werkzeug.datastructures.FileStorage, required=True, help="Image must be provided", location="files")

    def post(self):
        args = self.reqparse.parse_args()
        image_file = args["image"]
        file_bytes = np.fromfile(image_file, np.uint8)        
        img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
        text = pytesseract.image_to_string(img).replace("\n", " ")
        return {"extracted_text": text}, 200