import os

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from scripts.tmforum import get_product, create_order

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=['GET', 'POST'])
def order():
    id = request.form.get('id', 101)
    params = {'id': id}
    if request.method == 'GET':
        product = get_product(params)
        return render_template('order.html')
    # POST form submission
    tmforum_response = create_order(params)
    return redirect(url_for('shipment'))


@app.route('/customize')
def customize():
    return render_template('customize.html')


@app.route('/shipment', methods=['GET', 'POST'])
def shipment():
    print 'request.method', request.method
    if request.method == 'GET':
        return render_template('shipment.html')
    else:
        return redirect(url_for('thanks'))


@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 0))
    if port:
        app.debug = False
        app.run(host='0.0.0.0', port=port)
    else:
        app.debug = True
        app.run()
