from flask_wtf import FlaskForm
from flask import flash
from misc.helpers.typing_hacks import _l
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

class FlaskFormEx(FlaskForm):
    def validate_and_flash(self) -> bool:
        """
        Validates the form and flashes all validation errors.
        Returns the result of validate_on_submit
        """
        if not self.validate_on_submit():
            for e in self.errors.values():
                flash(e[0], category="error")
            return False
        return True
    
class LoginForm(FlaskFormEx):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    submit = SubmitField(_l('Log in'))

class NewQRForm(FlaskFormEx):
    name = StringField(_l('Name'), validators=[DataRequired()])
    description = StringField(_l('Description'))
    target = StringField(_l('Data'), validators=[DataRequired()])
    ecc_level = SelectField(_l('Error correction level'), choices=[('l', _l('Low')), ('m', _l('Medium')), ('q', _l('Quartile')), ('h', _l('High'))])