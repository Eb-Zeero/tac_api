from alchemy.config import db
from flask import request, jsonify
import jwt
from functools import wraps

from alchemy.config import app


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token =request.headers['x-access-token']

        if not token:
            jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is is invalid!.'}), 401

        return f(current_user, *args, **kwargs)
    return decorated


class User(db.Model):

    __tablename__ = "Users2"
    Id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    Name = db.Column(db.String(50))
    Partner_Id = db.Column(db.String(50))
    Password = db.Column(db.String(80))
    Role = db.Column(db.String(80))




    # constructor is not valid for now
    def __init__(self):

        self.user_id = -99
        self.email = 'email'
        self.role = 'GUEST'
        self.error = None
        self.user_valid = False
        self.pages = {'login': {'edit': True, 'view': True}}
        self.login_user("email")

    def __repr__(self):
        return '<Email: {email}\trole: {role}>'.format(email=self.email, role=self.role)

    def is_user_valid(token):
        user = Users.query.filter_by(user_id=token.user_id).first()
        if user is None:
            token.error = "User token has been compromised \n" \
                          "Token no longer exist\n If you were a valid user at least once please login again. \n" \
                          "If this error persist " \
                          "please contact administrator at nhlavutelo@saao.ac.za"
            token.user_valid = False
            token.role = 'GUEST'
            return False
        if user.role == token.role and user.user_id == token.user_id:
            return True

        token.error = "User token has been compromised \n" \
                      "Token no longer exist\n If you were a valid user at least once please login again. \n" \
                      "If this error persist " \
                      "please contact administrator at nhlavutelo@saao.ac.za"
        token.user_valid = False
        token.role = 'GUEST'
        return False

    def login_user(self, credential):
        user = Users.query.filter_by(email=credential['email']).first()

        if user is None:
            self.error = "User not registered"
            self.role = 'GUEST'
            return self

        elif credential['email'] == user.email and user.password == credential['password']:
            self.user_id = user.user_id
            self.emial = user.email
            self.role = user.role
            self.user_valid = True
            self.user_pages()
            self.pages = self.pages
            return self
        else:
            self.error = "Password and email does'nt metch"
            self.user_valid = False
            self.role = 'GUEST'
            return self

    def user_pages(self):
        pages = Pages.query.filter_by(role=self.role).first()
        p_s = []
        dic = {}
        i = 0
        for p in pages.pages.split():
            p1 = p.replace(',', '')
            i += 1
            dic2 = {"edit": False, "view": False}
            page = UserPage(page=p1)
            page.role_page(page=p1, role=self.role)

            dic2["view"] = page.view
            dic2["edit"] = page.edit
            dic[page.name] = dic2

            p_s.append(page)
        self.pages = dic
        return p_s

    def get_user(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'role': self.role,
            'error': self.error,
            'user_valid': self.user_valid
        }


class UserPage(object):
    """
    N.B. method is poorly
    for this object to have correct information about role and the pages role must not be set anywhere but 
    be taken from the database. if new roles are added this method's on this object must be rewritten 
    """
    def __init__(self, page='login'):
        self.name = page
        self.edit = False
        self.view = False
        self.error = None

    def role_page(self, page='login', role='GUEST'):
        if page == "login":
            self.edit = True
            self.view = True
        elif page == 'statistics':
            if role == "GUEST":
                self.view = False
                self.edit = False
            else:
                self.view = True
                self.edit = False

        elif page == 'allocation':
            if role == "GUEST" or role == "INVESTIGATOR":
                self.view = False
                self.edit = False
            elif role == "TAC_MEMBER":
                self.view = True
                self.edit = False
            else:
                self.view = True
                self.edit = True

        elif page == 'documentation':
            if role == "GUEST" or role == "INVESTIGATOR":
                self.view = False
                self.edit = False
            else:
                self.view = True
                self.edit = False

        elif page == 'tech':
            if role == "GUEST" or role == "INVESTIGATOR" or role == "TAC_MEMBER" or role == "TAC_CHAIR":
                self.view = False
                self.edit = False

            else:
                self.view = True
                self.edit = True

        elif page == 'admin':
            if role == "GUEST" \
                    or role == "INVESTIGATOR" \
                    or role == "TAC_MEMBER" \
                    or role == "TAC_CHAIR":
                self.view = False
                self.edit = False

            else:
                self.view = True
                self.edit = True

    def __repr__(self):
        return "<name: {name}\t viawable: {view}\t editable: {edit}>".format(name=self.name, view=self.view, edit=self.edit)
