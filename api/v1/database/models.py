from mongoengine import Document, StringField


class Project(Document):
    title = StringField(required=True, max_length=200)
    description = StringField(required=True)
