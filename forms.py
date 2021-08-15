from flask_wtf import FlaskForm

from wtforms import StringField, HiddenField, SubmitField
from wtforms.validators import InputRequired


class RegisterForm(FlaskForm):
    """From to register new client."""
    email = StringField(
        "Электронная почта", 
        [InputRequired("Пожалуйста, введите адрес вашей электронной почты")]
    )
    password = StringField(
        "Пароль", 
        [InputRequired("Пожалуйста, придумайте ваш пароль")]
    )
    submit = SubmitField("Зарегистрироваться")


class LoginForm(FlaskForm):
    """Login form for authentication."""
    email = StringField(
        "Электронная почта", 
        [InputRequired("Пожалуйста, введите адрес вашей электронной почты")]
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
        [InputRequired("Пожалуйста, введите адрес вашей электронной почты")]
    )
    phone = StringField(
        "Телефон", 
        [InputRequired("Пожалуйста, введите номер вашего телефона")]
    )
    order = HiddenField()
    submit = SubmitField()