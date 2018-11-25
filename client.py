from flask import Flask, render_template, request, flash
from forms import PostForm

debug = True
app = Flask(__name__)
app.secret_key = 'dev key'

@app.route('/post', methods = ['GET', 'POST'])
def post():
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


if __name__ == '__main__':
    app.run(debug = debug)
