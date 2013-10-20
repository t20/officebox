from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order')
def order():
    size = request.args.get('size', 'medium')
    return render_template('order.html')


@app.route('/customize')
def customize():
    return render_template('customize.html')


@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.debug = True
    app.run()