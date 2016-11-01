# Courses
from flask import jsonify, Blueprint
from flask.ext.restfull import Resource, Api
import models

class ReviewList(Resource):
    def get(self):
        return jsonify({'reviews': [{'course': 1, 'rating': 5}] })

class Review(Resource):
    def get(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def put(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def delete(self, id):
        return jsonify({'course': 1, 'rating': 5})
