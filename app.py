import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Actors, Movies
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    CORS(app, resources={r"/": {"origins": "*"}})

    @app.route('/')
    def get_greeting():
        if 'EXCITED' not in os.environ:
          os.environ['EXCITED'] = "true"
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad! Yeppppieeee!"



    # Get all actors
    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = Actors.query.all()

        if len(actors) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        })
    
    # Create new actor 
    @app.route('/actors', methods=['POST'])
    def create_actor():
        body = request.get_json()

        if (('name' not in body) or ('age' not in body) or ('gender' not in body)):

           abort(422)

        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        actor = Actors(name, age, gender)
        actor.insert()

        return jsonify({
            'success': True #,
            # 'actors': [actor.format() for actor in actors]
        })
    

    return app

app = create_app()

if __name__ == '__main__':
    app.run()