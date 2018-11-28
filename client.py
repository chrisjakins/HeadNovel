from flask import Flask, render_template, request, flash, session, escape, redirect, url_for
from forms import *
from database import Database
import datetime
import sqlite3


debug = True
app = Flask(__name__)
app.secret_key = 'dev key'
db = Database()


###############################################################

@app.route('/list_users')
def list_users():
   
   db.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from users")

   rows = cur.fetchall();
   return render_template("list_users.html", rows = rows)

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
    # removes username if someone is logged in
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
            attr = 'comment_id,time_stamp,comm_text,commentor_ID,likes_list'

            values = '150,\'' + curr_time() + '\','
            values += parse_dict(request.form)
            values += ',NULL'
            db.insert_item('comment', attr, values)
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
            <<<<<<< HEAD
            attr = 'post_id,text, time_stamp,poster_id,likes_list'
            =======
            attr = 'post_id,time_stamp,text,poster_id,likes_list'
            >>>>>>> 244dc5484f583ab82da0e13071919ac384411798

            post_id = db.get_next_id('post')

            values = str(post_id) + ',\'' + curr_time() + '\','
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
            attr = 'time_stamp,receiver_id,sender_id,message_text,likes_list'

            values = '\'' + curr_time() + '\','
            values += parse_dict(request.form)
            values += ',NULL'

            db.insert_item('message', attr, values)
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
    <<<<<<< HEAD
            attr = 'f_name, l_name, u_name, password, profile_id, created_date, phone_no,email, b_date'
    =======
            attr = 'profile_id,created_date,u_name,password,email,f_name,l_name,phone_no,b_date'
    >>>>>>> 244dc5484f583ab82da0e13071919ac384411798

            values = str(db.get_next_id('profile')) + ',\'' + curr_time() + '\','
            values += parse_dict(request.form)

            db.insert_item('profile', attr, values)
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('profile.html', form = form)

###############################################################

@app.route('/delete_profile', methods = ['GET', 'POST'])
def delete_profile():
    form = Delete_Profile()
    if request.method == 'POST' and form.validate_on_submit():
        request.form['profile_id']
        search = db.delete_profile('profile_id')
        flash('Entry deleted')
        return render_template('delete_profile.html', form = form)
    elif request.method == 'GET':
        return render_template('delete_profile.html')



###############################################################
@app.route('/page', methods = ['GET', 'POST'])
def add_page():
    form = PageForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('Check required fields.')
            return render_template('page.html', form = form)
        else:
            attr = 'page_id,page_name,admin,category,description,num_views'

            values = str(db.get_next_id('page')) + ','
            values += parse_dict(request.form)
            values += ',0'
            db.insert_item('page',attr , values)
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('page.html', form = form)

###############################################################

@app.route('/getpage', methods = ['GET', 'POST'])
def get_page():
    form = GetPageForm()
    if request.method == 'POST':
        results = db.get_item('*', 'page', 'page_id', str(request.form['page_id']))
        columns = ['page_id', 'page_name', 'admin', 'num_views', 'category', 'description']

        return render_template('results.html', columns = columns, items = results)

    elif request.method == 'GET':
        return render_template('getpage.html', form = form)

###############################################################

@app.route('/getpostsbyaccount', methods = ['GET', 'POST'])
def get_posts_by_account():
    form = GetPostsByAccountForm()
    if request.method == 'POST':
        user_id = db.get_item('profile_id', 'profile',
                              'u_name', str(request.form['username']))[0][0]
        page_id = db.get_item('page_id', 'page', 'admin', str(user_id))[0][0]
        results = db.get_item('*', 'post', 'poster_id', str(page_id))

        columns = ['post_id', 'text', 'time_stap', 'poster_id', 'likes_list']
        return render_template('results.html', columns = columns, items = results)

    elif request.method == 'GET':
        return render_template('getpostsbyaccount.html', form = form)

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
