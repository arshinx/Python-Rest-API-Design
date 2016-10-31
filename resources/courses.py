# Courses
from flask import jsonify
from flask.ext.restfull import Resource
import models

class CourseList(Resource):
    def get(self):
        return jsonify({'courses': [{'title': 'Python Basics'}] })
