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

##############################
#####Creating An Author#######
##############################
@app.route('/authors',methods=['POST'])
def create_an_author():
    #get the JSON response
    data=request.get_json()
    author_schema=AuthorOuputSchema()

    #transform JSON data to SQLAlchemy instance
    author=author_schema.load(data)

    #create the instance in the database
    result=author_schema.dump(author.create())

    return make_response(
        jsonify(
            {
                "message":"Author Created",
                "author":result
            }
        ),201
    )


##############################################
###########Get an author by ID################
##############################################
@app.route('/author/<id>',methods=['GET'])
def get_author_by_id(id):
    get_author=Author.query.get_or_404(id)

    author_schema=AuthorOuputSchema()

    author=author_schema.dump(get_author)

    return make_response(jsonify(
        {
            "message":"author",
            "author":author
        }
    ))


##############################################
############Update an author##################
##############################################
@app.route('/author/<id>',methods=['PUT'])
def update_author(id):
    data=request.get_json()

    author_schema=AuthorOuputSchema()
    author_to_update=Author.query.get_or_404(id)

    if data.get('name'):
        author_to_update.name=data.get('name')
    if data.get('specialization'):
        author_to_update.specialization=data.get('specialization')

    db.session.add(author_to_update)
    db.session.commit()

    author=author_schema.dump(author_to_update)

    return make_response(
        jsonify(
            {
                "message":"author info updated to:",
                "author":author
            }
        )
    )

#################################################
##########Delete an author#######################
#################################################
@app.route('/author/<id>',methods=['DELETE'])
def delete_author(id):
    author_to_delete=Author.query.get_or_404(id)

    db.session.delete(author_to_delete)
    db.session.commit()
    
    author=AuthorOuputSchema().dump(author_to_delete)
    return make_response(
        jsonify(
            {"message":"Author deleted successfully",
              "author":author
            }
        )
    )









@app.errorhandler(404)
def not_found(error):
    return jsonify({"message":"Nothing Found"})

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