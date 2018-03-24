from PIL import Image

def loadImg(path):
    try:
        return Image.open(path)
    except Exception as exc:
        return exc
