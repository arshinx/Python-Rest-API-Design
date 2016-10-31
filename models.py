# Data Model
import datetime
from peewee import *

DATABASE = Sqlitedatabase('courses.sqlite')

class Course(Model):
    
