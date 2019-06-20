from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from settings import DB_URI

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.url_map.strict_slashes = False
CORS(app)

db = SQLAlchemy(app)
from resources import ContactListResource, ContactResource

api.add_resource(ContactListResource, '/api/contacts')
api.add_resource(ContactResource, '/api/contacts/<contact_id>')


if __name__ == '__main__':
    app.run(port=8000, debug=True)