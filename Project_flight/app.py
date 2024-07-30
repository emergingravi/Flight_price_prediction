from flask import Flask, request, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("Project_flight\Flight_price_model.pkl")

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get form data
   
    date = int(request.form['date'].split('-')[2])
    month = int(request.form['date'].split('-')[1])
    year = int(request.form['date'].split('-')[0])
    dep_hours = int(request.form['dep_hours'])
    dep_min = int(request.form['dep_min'])
    arrival_hours = int(request.form['arrival_hours'])
    arrival_min = int(request.form['arrival_min'])
    duration_hours = int(request.form['duration_hours'])
    duration_min = int(request.form['duration_min'])
    total_stops = int(request.form['total_stops'])
    airline = request.form['airline']
    source = request.form['source']
    destination = request.form['destination']

   # Prepare data for prediction
    input_data = np.array([[date, month, year, dep_hours, dep_min, arrival_hours, arrival_min, duration_hours, duration_min, total_stops, airline, source, destination]])

    # Make prediction
    prediction = model.predict(pd.DataFrame(input_data, columns=['Date', 'Month', 'Year', 'Dep_hours', 'Dep_min', 'Arrival_hours', 'Arrival_min', 'Duration_hours', 'Duration_min', 'Total_Stops', 'Airline', 'Source', 'Destination']))

    predicted_price =prediction[0]
    return f"The predicted price for the flight is Rs. {predicted_price:.2f}."

if __name__ == '__main__':
    app.run(debug=True)
