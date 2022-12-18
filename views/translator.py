import cv2 as cv
import pytesseract
from deep_translator import GoogleTranslator
from flask_restful import Resource, reqparse
import werkzeug
import numpy as np
import config 


class Translate(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("image", type=werkzeug.datastructures.FileStorage, required=True, help="Image must be provided", location="files")
        self.reqparse.add_argument("translation_language", type=str, required=True, help="Translation language must be provided", location="form")

    def post(self):
        args = self.reqparse.parse_args()
        image_file = args["image"]
        file_bytes = np.fromfile(image_file, np.uint8)
        trans_language = args["translation_language"]
        
        img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
        text = pytesseract.image_to_string(img).replace("\n", " ")
        translated = GoogleTranslator(source='auto', target=trans_language).translate(text).replace("\n", " ")
        return {"extracted_text":text, "translated_text": translated}, config.SUCCESS_CODE