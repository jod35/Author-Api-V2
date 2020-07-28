from main import app,db
from flask import request,jsonify,request,make_response
from main.models import Author,AuthorOuputSchema

@app.route('/')
def index():
    return jsonify({'message':"Hello Welcome to my API"})

#############################################
###########Getting all the authors###########
#############################################
@app.route('/authors',methods=['GET'])
def get_all_authors():
    #get all authors
    get_authors=Author.query.all()

    # create an instance of the ouput schema
    author_schema=AuthorOuputSchema(many=True)

    #serialize our SQLAlchemy objects basing on the fields we described using the output schema
    authors=author_schema.dump(get_authors)

    return make_response(jsonify(
        {
            "authors":authors
        }
    ))


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