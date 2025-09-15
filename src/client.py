import requests
import zlib
import base64
import uuid
import os
PLANTUML_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def make_request(uml):
    encoded = encode_uml(uml)
    res = requests.request(method="GET",data=uml, url=f'http://www.plantuml.com/plantuml/png/{encoded}')
    return save_to_path(res)

def encode_uml(uml):
    data = uml.encode('utf-8')
    compressed = zlib.compress(data)[2:-4]
    base64_encoded = base64.b64encode(compressed).decode('utf-8')
    translation_table = str.maketrans(BASE64_ALPHABET, PLANTUML_ALPHABET)
    plantuml_encoded = base64_encoded.translate(translation_table)
    return plantuml_encoded

def save_to_path(res):
    fname = uuid.uuid4().__str__() + ".png"
    file_path = f"../erd/{fname}"
    if not os.path.exists("../erd"):
        os.mkdir("../erd")
    with open(file_path,"wb") as f:
        f.write(res.content)
    return f"** Saved ERD at {file_path}"