# Courses
from flask import jsonify, Blueprint
from flask.ext.restful import Resource, Api, reqparse, inputs
import models

# CourseList - returns list of courses
class CourseList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument(
        'title',
        required = True,
        help = 'No course title provided',
        location = ['form', 'json']
        )

        self.reqparse.add_argument(
        'url',
        required = True,
        help = 'No course URL provided',
        location = ['form', 'json'],
        type = inputs.url
        )
        super(CourseList, self).__init__()

    def get(self):
        return jsonify({'courses': [{'title': 'Python Basics'}] })

    def post(self):
        args = self.reqparse.parse_args()
        return jsonify({'courses': [{'title': 'Python Basics'}] })

# Course - returns a single course
class Course(Resource):
    def get(self, id):
        return jsonify({'title': 'Python Basics'})

    def put(self, id):
        return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})

# Construct API
courses_api = Blueprint('resources.courses', __name__)
api = Api(courses_api)
api.add_resource(CourseList, '/api/v1/courses', endpoint='courses')
api.add_resource(Course, '/api/v1/courses/<int:id>', endpoint='course')
