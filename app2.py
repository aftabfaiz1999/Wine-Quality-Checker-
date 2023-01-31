from flask import Flask, render_template, request
import pickle

#load the model
model = pickle.load(open('model', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # get the data from the html form
    fixed_acidity = float(request.form['fixed_acidity'])
    volatile_acidity = float(request.form['volatile_acidity'])
    citric_acid = float(request.form['citric_acid'])
    residual_sugar = float(request.form['residual_sugar'])
    chlorides = float(request.form['chlorides'])
    free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
    total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
    density = float(request.form['density'])
    pH = float(request.form['pH'])
    sulphates = float(request.form['sulphates'])
    alcohol = float(request.form['alcohol'])

    # create a feature array
    data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, 
    free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
    
    # predict the quality using the model
    prediction = model.predict([data])
    quality = prediction[0]

    return render_template('result.html', prediction=quality)

if __name__ == '__main__':
    app.run(debug=True)