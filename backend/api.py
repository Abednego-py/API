from flask import Flask

# from flask import render_template, request, flash, redirect, url_for

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def method_name():
#     firstname = request.args.get('Firstname')
#     return f'{firstname}'

# @app.route('/', methods=['POST'])
# def methodName():
#     firstname = request.form.get('Firstname')
#     return f'''{firstname}'''

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, redirect, render_template, jsonify
import pickle
import numpy as np


app = Flask(__name__)  # intializing the flask app


@app.route('/home', methods=['POST'])
def handle_form_submission():
    firstname = request.form.get('Firstname')
    lastname = request.form.get('Lastname')
    email = request.form.get('Email')
    return jsonify({
        'firstname' : firstname,
        'lastname' : lastname,
        'email' : email
    })
    
@app.route('/search', methods=['GET'])
def handle_search():
    search = request.args.get('search')

    return f'{search}'

@app.route('/predict', methods=['POST', 'GET'])
def price_prediction():
    # if request.method == 'POST':
    volume = request.form.get('volume')
    power = request.form.get('power')
    weight = request.form.get('weight')
    console = request.form.get('console')
    feature = [volume, power, weight, console]

    loaded_model = pickle.load(open("C:/Users/abedn/Downloads/SL workshop/model.pkl", 'rb'))
    result = loaded_model.predict(np.array(feature).reshape(1, 4).astype('int'))
    return render_template('prediction.html', result=result)
    
if __name__ =='__main__':
    app.run(debug=True)
