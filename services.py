import uuid
from utils import upload_image
from repository import db_connect as dc

def createPost(form, file) -> None:
    name = form['name']
    sourcefile = file['thumbnail']
    filename = upload_image(sourcefile=sourcefile)
    des = form['description']

    query = f"""
        INSERT INTO `products`(`name`, `thumbnail`, `description`) VALUES
        ( '{name}', '{filename}', '{des}' )
    """
    con = dc()
    cursor = con.cursor()
    cursor.execute(query=query)
    con.commit()


    






