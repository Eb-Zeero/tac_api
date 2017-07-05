from alchemy.config import db


class Token(db.Model):



    def __init__(self, user):
        self.user_id = user.user_id
        self.role = user.role
        self.error = user.error
        self.user_valid = user.user_valid
        self.links = {}
        self.pages = user.pages
        self.request = None

    def get_token(self):
        """
        give out the token as dictionary
        :return: token's as dictionary
        """
        return {
            'user_id': self.user_id,
            'role': self.role,
            'error': self.error,
            'user_valid': self.user_valid,
            'links': self.links,
            'pages': self.pages


        }

    def __repr__(self):
        return '<User_id: {id}\tRole: {role}> pages: {pages}'\
            .format(id=self.user_id, role=self.role, pages=self.pages)
