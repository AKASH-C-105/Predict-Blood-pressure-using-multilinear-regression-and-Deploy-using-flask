from flask import Flask, request, jsonify, render_template
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open('BP2.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get inputs from the form
    age = float(request.form['age'])
    bmi = float(request.form['bmi'])
    exercise_hours = float(request.form['exercise_hours'])

    # Make prediction
    prediction = model.predict([[age, bmi, exercise_hours]])
    result = round(prediction[0], 2)

    # Return result
    return render_template('result.html', prediction_text=f'Predicted Blood Pressure: {result} mmHg')

if __name__ == '__main__':
    app.run(debug=True)
