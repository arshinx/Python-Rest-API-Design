# Data Model
import datetime
from peewee import *

DATABASE = Sqlitedatabase('courses.sqlite')

class Course(Model):
    title = CharField()
    url   = CharField(unique=True)
    created_at = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = DATABASE
