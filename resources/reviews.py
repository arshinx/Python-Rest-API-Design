# Courses
from flask import jsonify, Blueprint
from flask.ext.restful import Resource, Api, reqparse, inputs
import models
import requests

# ReviewList - returns all reviews
class ReviewList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument(
        'course',
        required = True,
        help = 'No course provided',
        location = ['form', 'json']
        type = inputs.positive
        )

        self.reqparse.add_argument(
        'rating',
        required = True,
        help = 'No rating provided',
        location = ['form', 'json'],
        type = inputs.int_range(1, 5)
        )

        self.reqparse.add_argument(
        'comment',
        required = False,
        nullable = True,
        location = ['form', 'json'],
        default = ''
        )

        super(ReviewList, self).__init__()

    def get(self):
        return jsonify({'reviews': [{'course': 1, 'rating': 5}] })

# Review - returns a select review
class Review(Resource):
    def get(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def put(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def delete(self, id):
        return jsonify({'course': 1, 'rating': 5})

# Construct Api
reviews_api = Blueprint('resources.reviews', __name__)
api = Api(reviews_api)
api.add_resource(ReviewList, '/reviews', endpoint='/reviews')
api.add_resource(Review, '/reviews/<int:id>', endpoint='/review')
