import os
import sys, sysconfig
import pytesseract
import cv2
import requests
from urllib.parse import unquote
from flask import request
import logging

logging.basicConfig(level=logging.INFO)

IMAGEPATH = "data"

def read_ocr():
    """
    """
    content = request.json
    
    print(f"content: {content}")
    logging.info(content)
    image = content['image']
    lang = content['lang']
    config = content['config']
    logging.info(f"image: {image}, lang: {lang}, config: {config}")
    
    response = requests.get(image)
    image_name = unquote(os.path.basename(image))
    logging.info(f"image_name: {image_name}")
    image_path = os.path.join(image_name)

    with open(image_path, 'wb') as file:
        file.write(response.content)
    img_arr = cv2.imread(image_path)
    text = pytesseract.image_to_string(img_arr, lang=lang, config=config)
    if os.path.isfile(image_path):
        os.unlink(image_path)
    return {"text":text}

def root():
    """
        Root Endpoint
        Returns: Link to the API documentation
    """
    return {"API Documentation":''}
