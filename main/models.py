####################################################################
#############DATABASE MODELS########################################
####################################################################
from main import db

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
        return f'Auhor {self.name}'

    def is_specialized_in(self):
        return self.specialization