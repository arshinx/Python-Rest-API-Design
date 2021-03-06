# Courses
from flask import jsonify, Blueprint
from flask.ext.restful import (Resource, Api, reqparse, inputs, fields, marshal, marshal_with, url_for, abort)
import models

# Fields
course_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'url': fields.String,
    'reviews': fields.List(fields.String)
}

# Add Reviews (Empty List when no reviews present)
def add_reviews(course):
    course.reviews = [url_for('resources.reviews.review', id = review.id) for review in course.review_set]
    return course

# Course or 404?
def course_or_404(course_id):
    try:
        course = models.Course.get(models.Course.id == course_id)
    except models.Course.DoesNotExist:
        abort(404, message="Course {} does not exist".format(course_id))
    else:
        return course


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
        courses = [marshal(add_reviews(course), course_fields) for course in models.Course.select()]
        return {'courses': courses}

    @marshal_with(course_fields)
    def post(self):
        args = self.reqparse.parse_args()
        course = models.Course.create(**args)
        print(args["title"])
        print(args['url'])
        return (add_reviews(course), 201, {
                'Location': url_for('resources.courses.course', id=course.id)}
               )

# Course - returns a single course
class Course(Resource):
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
        super(Course, self).__init__()

    @marshal_with(course_fields)
    def get(self, id):
        return add_reviews(course_or_404(id))
        # or remove decorator '@' and add:
        # return marshall_with(add_reviews(course_or_404(id)), course_fields)

    def put(self, id):
        return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})

# Construct API
courses_api = Blueprint('resources.courses', __name__)
api = Api(courses_api)
api.add_resource(CourseList, '/api/v1/courses', endpoint='courses')
api.add_resource(Course, '/api/v1/courses/<int:id>', endpoint='course')
