from flask_restful import Resource, request
from flask import jsonify
from marshmallow import ValidationError
from models import Contact, contact_schema, contacts_schema
from app import db
from pprint import pprint

class ContactListResource(Resource):
    def get(self):
        contacts = Contact.query.all()
        result = contacts_schema.dump(contacts)
        return result.data
    
    def post(self):
        data = request.get_json(force=True)
        contact, errors = contact_schema.load(data)
        if errors:
            return {'detail': errors}, 400
        db.session.add(contact)
        db.session.commit()
        return contact_schema.dump(contact).data

class ContactResource(Resource):
    def get(self, contact_id):
        contact = Contact.query.get(contact_id)
        return contact_schema.dump(contact).data if contact else {'detail':'Not found.'}, 200 if contact else 404

    def put(self, contact_id):
        data = request.get_json(force=True)
        contact, errors = contact_schema.load(data)
        if errors:
            return {'detail': errors}, 400
        contact.id = contact_id
        db.session.merge(contact)
        db.session.commit()
        return contact_schema.dump(contact).data

    def delete(self, contact_id):
        contact = Contact.query.get(contact_id)
        db.session.delete(contact)
        db.session.commit()
        return contact_schema.dump(contact).data