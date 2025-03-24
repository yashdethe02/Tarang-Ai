from flask import Flask, render_template, redirect, url_for, g, session, request
from flask_cors import CORS  # Add this import
import os  # Add this import

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.before_request
def before_request():
    g.current_user = None
    if 'user_id' in session:
        pass

@app.context_processor
def inject_user():
    return dict(current_user=g.current_user)

@app.route('/')
def index():
    return redirect(url_for('home_page'))

@app.route('/home', endpoint='home_page')
def home():
    return render_template('home.html')

@app.route('/insights', endpoint='insights_page')
def insights():
    return render_template('insights.html')

@app.route('/flag', endpoint='flag_page')
def flag():
    return render_template('flag.html')

@app.route('/tips', endpoint='tips_page')
def tips():
    return render_template('tips.html')

@app.route('/ai_prediction', endpoint='ai_prediction_page')
def ai_prediction():
    return render_template('aipred.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    state = request.form.get('STATE')
    temp = request.form.get('temp')
    do = request.form.get('do')
    ph = request.form.get('ph')
    conductivity = request.form.get('conductivity')
    bod = request.form.get('bod')
    nitrate = request.form.get('nitrate')
    fecal_coliform = request.form.get('fecalColiform')

    # Perform prediction logic here
    # For demonstration, we'll use dummy values
    pred = "Safe"
    safe_prob = 85.0
    unsafe_prob = 15.0

    return render_template('aipred.html', show_result=True, pred=pred, safe_prob=safe_prob, unsafe_prob=unsafe_prob)

if __name__ == "__main__":
    app.run(debug=True, port=5002)