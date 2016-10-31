# Data Model
import datetime
from peewee import *

DATABASE = SqliteDatabase('courses.sqlite')

# Course Model
class Course(Model):
    title = CharField()
    url   = CharField(unique=True)
    created_at = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = DATABASE

# Review Model
class Review(Model):
    course = ForeignKeyField(Course, related_name = 'review_set')
    rating = IntegerField()
    comment = TextField(default='')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

# Initializer
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Course, Review], safe=True)
