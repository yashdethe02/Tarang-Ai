from flask import Flask, render_template, redirect, url_for, g, session, request
from flask_cors import CORS  # Enable CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Secret key for session management
app.config['SECRET_KEY'] = os.urandom(24)

def get_user_from_db(user_id):
    # This function should return user data from the database.
    # For now, let's just return a dummy user.
    return {"user_id": user_id, "username": "test_user"}

@app.before_request
def before_request():
    """Runs before every request, setting up the current user."""
    g.current_user = None
    if 'user_id' in session:
        g.current_user = get_user_from_db(session['user_id'])  # Example function to fetch user

@app.context_processor
def inject_user():
    """Injects the current user into every template context."""
    return dict(current_user=g.current_user)

@app.route('/')
def index():
    """Redirects to the home page."""
    return redirect(url_for('home'))

@app.route('/home')
def home():
    """Displays the home page."""
    return render_template('home.html')

@app.route('/insights')
def insights():
    """Displays the insights page."""
    return render_template('insights.html')

@app.route('/flag')
def flag():
    """Displays the flag page."""
    return render_template('flag.html')

@app.route('/tips')
def tips():
    """Displays the tips page."""
    return render_template('tips.html')

@app.route('/ai_prediction')
def ai_prediction():
    """Displays the AI prediction page."""
    return render_template('aipred.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the form submission and performs a prediction."""
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
    # For now, let's use dummy values
    pred = "Safe"
    safe_prob = 85.0
    unsafe_prob = 15.0

    # Return the result page with the prediction
    return render_template('aipred.html', show_result=True, pred=pred, safe_prob=safe_prob, unsafe_prob=unsafe_prob)

if __name__ == "__main__":
    app.run(debug=False, port=5002)
