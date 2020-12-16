from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/<name>')
def home(name):
    return render_template('cover.html')


@app.route('/<name>')
def user(name):
    return f'Hello {name}!'


@app.route('/admin')
def admin():
    return redirect(url_for('user', name='admin!'))


if __name__ == "__main__":
    app.run()
