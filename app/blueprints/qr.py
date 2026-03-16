from flask import Blueprint, render_template, flash, redirect, url_for
from misc.forms import NewQRForm
from flask_login import login_user, logout_user, login_required
from flask_babel import _
from bcrypt import checkpw
from db import User

QRController = Blueprint('QRController', __name__)

@QRController.route('/qr/new')
@login_required
def new_qr():
    form = NewQRForm()
    return render_template('newqr.j2', form=form)