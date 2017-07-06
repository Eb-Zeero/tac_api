from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

from points.proposals.proposals_per_partner import partner_proposal
import datetime
from points.user import User, token_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:men1zeero00@localhost:3306/tac'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


languages = [{'name': 'JavaScripts'},
             {'name': 'Python'},
             {'name': 'Ruby'}]


@app.route('/', methods=['GET'])
def test():
    return jsonify({"message": "it is working"})


@app.route('/lang', methods=['GET'])
def return_all():
    return jsonify({'languages': languages})


@app.route('/lang/<string:name>', methods=['GET'])
def return_one(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})


@app.route('/lang', methods=['POST'])
def add_one():
    json_dict = request.get_json()
    language = {'name': json_dict['name']}
    languages.append(language)
    return jsonify({'languages': languages})


@app.route('/lang/<string:name>', methods=['PUT'])
def edit_one(name):
    langs = [language for language in languages if language['name'] == name]
    json_dict = request.get_json()
    langs[0]['name'] = json_dict['name']
    return jsonify({'language': langs[0]})


@app.route('/lang/<string:name>', methods=['DELETE'])
def remove_one(name):
    langs = [language for language in languages if language['name'] == name]
    languages.remove(langs[0])
    return jsonify({'language': languages})


@app.route('/proposal/<string:partner>', methods=['GET'])
def proposals_per_partner(partner):
    proposals = partner_proposal('nhlavu')
    print(proposals.keys)
    return jsonify({'proposals': proposals})


@app.route('/statistics', methods=['GET'])
@token_required
def statistics_page(current_user):
    # todos = Todo.query.filter_by(user_id=current_user.id).all()
    return ''


@app.route('/login')
def login():
    auth = request.authorization

    if not auth.username or not auth.password:
        return make_response('Could not verify user! ', 401, {'WWW-Authenticate': 'Basic realm="Login required'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify user! ', 401, {'WWW-Authenticate': 'Basic realm="Login required'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
                           app.config['SECRET_KEY'])

        return jsonify({"token": token.decode("UTF-8")})
    return make_response('Could not verify user! ', 401, {'WWW-Authenticate': 'Basic realm="Login required'})

if __name__ == '__main__':
    app.run(debug=True)
