from pydantic import BaseModel
from mongoengine import Document, StringField


# class maxx_upload_images(Document):
#     Artist_name = StringField()
#     Type = StringField()




class User(BaseModel):
    name: str
    email: str
    password: str