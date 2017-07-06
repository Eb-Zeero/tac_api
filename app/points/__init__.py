from flask import Blueprint

auth = Blueprint('tac_api', __name__)

from . import user