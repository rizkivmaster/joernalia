from common.storage import images_storage, thumbnails_storage
from common.database.ModelBase import ModelBase
from common.database.PostgreBase import PostgreBase
from sqlalchemy import String, Column, Integer


class ImageData(ModelBase):
	__tablename__ = "ImageData"
	_id = Column()



def start():
    images_storage.start()
    thumbnails_storage.start()

def stop():
    images_storage.stop()
    thumbnails_storage.stop()

def save_image(image):
	"""
	rtype: :str
	"""
	
	pass

def get_image_url(image_id):
	pass

def get_thumbnails_url(image_id):
	pass

def delete_image(image_id):
	pass

def exists(image_id):
	pass