####################################################################
#############DATABASE MODELS########################################
####################################################################
from main import db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


######################
######Author##########
######################

class Author(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),nullable=False)
    specialization=db.Column(db.String(80),nullable=False)

    def __init__(self,name,specialization):
        self.name=name
        self.specialization=specialization

    def __str__(self):
        return f'Author {self.name}'
    
    #find out the specialization
    def is_specialized_in(self):
        return self.specialization

    #create a new author 
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self



######################
##Output Schema#######
######################
class AuthorOuputSchema(ModelSchema):
     #dictates how our SQLAlchemy instances will be returned as JSON
    class Meta(ModelSchema.Meta):
        model=Author
        sqla_session=db.session

    id=fields.Number(dump_only=True)
    name=fields.String(required=True)
    specialization=fields.String(required=True)