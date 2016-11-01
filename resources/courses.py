# Courses
from flask import jsonify, Blueprint
from flask.ext.restfull import Resource
import models

class CourseList(Resource):
    def get(self):
        return jsonify({'courses': [{'title': 'Python Basics'}] })

class Course(Resource):
    def get(self, id):
        return jsonify({'title': 'Python Basics'})

    def put(self, id):
        return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})

courses_api = Blueprint('resources_courses', __name__)
api = Api(courses_api)
api.add_resource(CourseList, '/api/v1/courses/<int:id>', endpoint='course')
