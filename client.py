from flask import Flask, render_template, request, flash, session, escape, redirect, url_for
from forms import *
from database import Database
import datetime


debug = True
app = Flask(__name__)
app.secret_key = 'dev key'
db = Database()


###############################################################

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

###############################################################

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

###############################################################

@app.route('/logout')
def logout():
    # removes username is someone is logged in
    session.pop('username', None)
    return redirect(url_for('index'))

###############################################################

@app.route('/comment', methods = ['GET', 'POST'])
def add_comment():
    form = CommentForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('Check required fields.')
            return render_template('comment.html', form = form)
        else:
            db.insert_item('comment', request.form)
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('comment.html', form = form)

###############################################################

@app.route('/post', methods = ['GET', 'POST'])
def add_post():
    form = PostForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('Check required fields.')
            return render_template('post.html', form = form)

        else:
            attr = 'post_id,time_stamp,text,poster_id,likes_list'

            values = '150,\'' + curr_time() + '\','
            values += parse_dict(request.form)
            values += ',NULL'

            db.insert_item('post', attr, values)
            return render_template('success.html')

    elif request.method == 'GET':
        return render_template('post.html', form = form)

###############################################################

@app.route('/message', methods = ['GET', 'POST'])
def add_message():
    form = MessageForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('Check required fields.')
            return render_template('message.html', form = form)
        else:
            db.insert_item('message', request.form)
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('message.html', form = form)

###############################################################

@app.route('/profile', methods = ['GET', 'POST'])
def add_profile():
    form = ProfileForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('Check required fields.')
            return render_template('profile.html', form = form)
        else:
            db.insert_item('profile', request.form)
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('profile.html', form = form)

###############################################################

@app.route('/page', methods = ['GET', 'POST'])
def add_page():
    form = PageForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('Check required fields.')
            return render_template('page.html', form = form)
        else:
            db.insert_item('page', request.form)
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('page.html', form = form)

###############################################################

# HELPERS

def parse_dict(items):
    values = ''
    for item in request.form:
        if item != 'csrf_token' and item != 'submit':
            values += '\'' + request.form[item] + '\','
        elif item == 'username':
            values += str(db.get_user_id(request.form[item])) + ','

    return values[:-1]


def curr_time():
    time = datetime.datetime.now()
    return str(time.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    app.run(debug = debug)
