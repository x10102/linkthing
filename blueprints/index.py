from flask import Blueprint, current_app, render_template
from auth_helpers import admin_only

IndexController = Blueprint('IndexController', __name__)

@IndexController.route('/')
def app_index():
    return render_template('index.j2')