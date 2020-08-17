from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email


# LawyerInfoForm class - Mike
class LawyerInfoForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

# CaseNotesForm class - Leland
class CaseNotesForm(FlaskForm):
    caseNum = TextAreaField('Case Number', validators=[DataRequired()])
    caseNotes = TextAreaField('Case Notes', validators=[DataRequired()])
    submit = SubmitField()


# LoginForm class - Josh
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()