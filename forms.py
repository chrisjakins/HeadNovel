from flask_wtf import FlaskForm
import wtforms
import datetime

###############################################################################

class PostForm(FlaskForm):
    # TODO 
    # need a unique post ID (can be abstracted to database class)
    post_text = wtforms.TextAreaField('Post',
        [wtforms.validators.DataRequired('Post field can not be empty.'),
         wtforms.validators.Length(max = 400)])

    username = wtforms.TextField('Username',
        [wtforms.validators.DataRequired('Username field can not be empty.')])
    current_time = datetime.datetime.now()

    submit = wtforms.SubmitField('Submit')

###############################################################################

class CommentForm(FlaskForm):
    # TODO
    # unique ID to post commented on
    comment_text = wtforms.TextAreaField('Comment', 
        [wtforms.validators.DataRequired('Comment field can not be empty.'), 
         wtforms.validators.Length(max = 400)])
    username = wtforms.TextField('Username',
        [wtforms.validators.DataRequired('Username field can not be empty.')])

    current_time = datetime.datetime.now()

    submit = wtforms.SubmitField('Submit')

###############################################################################

class MessageForm(FlaskForm):
    # TODO
    # need a unique post ID
    message_text = wtforms.TextAreaField('Message',
        [wtforms.validators.DataRequired('Message field can not be empty.'),
         wtforms.validators.Length(max = 400)])
 
    receiver_username = wtforms.TextField('Receiver Username',
        [wtforms.validators.DataRequired('Receiver Username field can not be empty.')])
 
    current_time = datetime.datetime.now()

    submit = wtforms.SubmitField('Submit')

###############################################################################

class ProfileForm(FlaskForm):                                                     
    # TODO                                                                     
    # need a unique post ID (can be abstracted to database class)              
    password_text = wtforms.TextAreaField('Password',                                  
        [wtforms.validators.DataRequired('Password field can not be empty.')])

    username = wtforms.TextField('Username',                                   
        [wtforms.validators.DataRequired('Username field can not be empty.')])

    email = wtforms.TextField('Email',                                   
        [wtforms.validators.DataRequired('Email field can not be empty.')])
 
    firstName = wtforms.TextField('First Name',                                   
        [wtforms.validators.DataRequired('First Name field can not be empty.')])

    lastName = wtforms.TextField('Last Name',                                   
        [wtforms.validators.DataRequired('Last Name field can not be empty.')])

    phoneNum = wtforms.TextField('Phone Number',                                   
        [wtforms.validators.DataRequired('Phone Number field can not be empty.')])

    current_time = datetime.datetime.now()                                     
 
    submit = wtforms.SubmitField('Submit')
