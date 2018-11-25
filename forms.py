from flask_wtf import Form
import wtforms

class PostForm(Form):
    post_text = wtforms.TextAreaField('Post')
    username = wtforms.TextField('Username')

    submit = wtforms.SubmitField('Submit')
