from flask import Flask, render_template, request, flash, session, escape, redirect, url_for
from forms import *

debug = True
app = Flask(__name__)
app.secret_key = 'dev key'
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
            # add to database
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
            # add results to database here
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
            # add results to database here
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
            # add results to database here
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
            # add results to database here
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('page.html', form = form)

###############################################################

if __name__ == '__main__':
    app.run(debug = debug)
