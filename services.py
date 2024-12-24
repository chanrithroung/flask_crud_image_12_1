import uuid
from utils import upload_image

def createPost(form, file):
    name = form['name']
    sourcefile = file['thumbnail']
    filename = upload_image(sourcefile=sourcefile)
    des = form['description']



