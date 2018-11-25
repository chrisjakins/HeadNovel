from flask_wtf import FlaskForm
import wtforms
import datetime

class PostForm(FlaskForm):
    # TODO 
    # need a unique post ID
    post_text = wtforms.TextAreaField('Post',
        [wtforms.validators.DataRequired('Post field can not be empty.'),
         wtforms.validators.Length(max = 400)])

    username = wtforms.TextField('Username',
        [wtforms.validators.DataRequired('Username field can not be empty.')])

    current_time = datetime.datetime.now()

    submit = wtforms.SubmitField('Submit')
