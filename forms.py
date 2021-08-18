from flask_wtf import FlaskForm

from wtforms import StringField, HiddenField, SubmitField, ValidationError
from wtforms.validators import InputRequired, Email, Length

from models import db, User


class RegisterForm(FlaskForm):
    """From to register new client."""
    email = StringField(
        "Электронная почта", 
        [
            InputRequired("Пожалуйста, введите адрес вашей электронной почты"), 
            Email("Пожалуйста, укажите валидный адрес электронной почты. Например example@email.com")
        ]
    )
    password = StringField(
        "Пароль", 
        [
            InputRequired("Пожалуйста, придумайте ваш пароль"), 
            Length(min=5,max=100)
        ]
    )
    submit = SubmitField("Зарегистрироваться")

    def validate_email(self, email):
        user = db.session.query(User).filter_by(email=email.data).first()
        if user:
            raise ValidationError('Пользователь с такой электронной почтой уже зарегистрирован. Пожалуйста, укажите другую почту.')


class LoginForm(FlaskForm):
    """Login form for authentication."""
    
    email = StringField(
        "Электронная почта", 
        [
            InputRequired("Пожалуйста, введите адрес вашей электронной почты"),
            Email("Пожалуйста, укажите валидный адрес электронной почты. Например example@email.com")
        ]
    )
    password = StringField(
        "Пароль", 
        [InputRequired("Пожалуйста, введите ваш пароль")]
    )
    submit = SubmitField()


class CartForm(FlaskForm):
    """Clien's cart form."""
    name = StringField(
        "Ваше имя", 
        [InputRequired("Пожалуйста, введите ваше имя")]
    )
    address = StringField(
        "Адрес", 
        [InputRequired("Пожалуйста, введите адрес доставки")]
    )
    email = StringField(
        "Электронная почта", 
        [
            InputRequired("Пожалуйста, введите адрес вашей электронной почты"),
            Email("Пожалуйста, укажите валидный адрес электронной почты.")
        ]
    )
    phone = StringField(
        "Телефон", 
        [InputRequired("Пожалуйста, введите номер вашего телефона")]
    )
    order = HiddenField()
    submit = SubmitField("Оформить заказ")
    
    def validate_email(self, email):
        user = db.session.query(User).filter_by(email=email.data).first()
        if user:
            raise ValidationError('Пользователь с такой электронной почтой уже зарегистрирован. Пожалуйста, укажите другую почту.')
