from flask_wtf import FlaskForm
import wtforms
import datetime

class PostForm(FlaskForm):
    post_text = wtforms.TextAreaField('Post')
    username = wtforms.TextField('Username')
    current_time = datetime.datetime.now()
    print(current_time)

    submit = wtforms.SubmitField('Submit')
