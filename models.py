
from app import db
from marshmallow import Schema, fields, ValidationError, post_load

##### MODELS #####
class Contact(db.Model):
    __tablename__ = "addressBook_contact"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    phone = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(30))
    address = db.Column(db.Text, nullable=True)

    def __init__(self, id=None, name='', phone='', email='', address=''):
        if id is not None:
            self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


##### SCHEMAS #####
# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError("Value must not be empty.")

class ContactSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True, validate=must_not_be_blank)
    phone = fields.Str()
    email = fields.Email()
    address = fields.Str()

    @post_load
    def make_contact(self, data, **kwargs):
        return Contact(**data)

contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)