from flask import Flask, render_template
from forms import PostForm

debug = True
app = Flask(__name__)
app.secret_key = 'dev key'

@app.route('/post', methods = ['GET', 'POST'])
def post():
    form = PostForm()
    return render_template('post.html', form = form)

if __name__ == '__main__':
    app.run(debug = debug)
