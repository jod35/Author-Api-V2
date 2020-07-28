from main import app,db
from flask import request,jsonify
from main.models import Author

@app.route('/')
def index():
    return jsonify({'message':"Hello Welcome to my API"})


@app.errorhandler(404)
def not_found(error):
    return jsonify({"message":"Not Found"})

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"message":"Server has got an internal error."})

@app.shell_context_processor
def make_shell_context():
    return {
        'db':db,
        'app':app,
        'Author':Author
    }