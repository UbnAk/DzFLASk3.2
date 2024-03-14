# Создать форму для регистрации пользователей на сайте. Форма должна 
# содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку 
# "Зарегистрироваться". При отправке формы данные должны сохраняться 
# в базе данных, а пароль должен быть зашифрован.




from flask import Flask, render_template, redirect, request
from flask_wtf.csrf import CSRFProtect
from model import db, User
from form import RegistrationForm
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'mysecretskey'
db.init_app(app)
csrf = CSRFProtect(app)

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Database created.')

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        
        user = User(name=name, surname=surname, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        return redirect('/')
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)