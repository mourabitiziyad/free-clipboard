import pyperclip
import time
from PIL import Image

import base64
from io import BytesIO

def listen():
    last = ""
    while True:
        current = pyperclip.paste()
        if current != last:
            if current.startswith("data:image"):
                image_data = current.split(",")[1]
                image = Image.open(BytesIO(base64.b64decode(image_data)))
                image.show()
            print(current)
            last = current
        time.sleep(0.1)

if __name__ == "__main__":
    listen()

    