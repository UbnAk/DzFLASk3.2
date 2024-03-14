# Создать форму для регистрации пользователей на сайте. Форма должна 
# содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку 
# "Зарегистрироваться". При отправке формы данные должны сохраняться 
# в базе данных, а пароль должен быть зашифрован.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')