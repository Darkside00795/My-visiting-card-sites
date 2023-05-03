from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html')


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    print(url_for('contacts'))
    return render_template('contacts.html')


if __name__ == "__main__":
    app.run(debug=True)
