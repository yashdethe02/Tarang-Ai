from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

feature_names = ['STATE', 'Temp', 'D.O. (mg/l)', 'PH', 'CONDUCTIVITY (µmhos/cm)', 'B.O.D. (mg/l)', 'NITRATENAN N+ NITRITENANN (mg/l)', 'FECAL COLIFORM (MPN/100ml)']

@app.route('/')
def hello_world():
    return render_template("aipred.html")

@app.route('/home', endpoint='home_page')
def home():
    return render_template('home.html')

@app.route('/insights', endpoint='insights_page')
def insights():
    return render_template('insights.html')

@app.route('/flag', endpoint='flag_page')
def insights():
    return render_template('flag.html')

@app.route('/tips', endpoint='tips_page')
def insights():
    return render_template('tips.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        form_values = {
            'state': 'STATE',
            'temp': 'Temp',
            'do': 'D.O. (mg/l)',
            'ph': 'PH',
            'conductivity': 'CONDUCTIVITY (µmhos/cm)',
            'bod': 'B.O.D. (mg/l)',
            'nitrate': 'NITRATENAN N+ NITRITENANN (mg/l)',
            'fecalColiform': 'FECAL COLIFORM (MPN/100ml)'
        }
        
        input_values = []
        for form_field in form_values.keys():
            value = float(request.form.get(form_field, 0))
            input_values.append(value)
        
        final_input = pd.DataFrame([input_values], columns=feature_names)
        
        prediction = model.predict_proba(final_input)
        
        prob_safe = prediction[0][1] * 100
        prob_unsafe = prediction[0][0] * 100

        output1 = "SAFE: {:.2f}%".format(prob_safe)
        output2 = "UNSAFE: {:.2f}%".format(prob_unsafe)

        safe_prob_formatted = "{:.2f}".format(prob_safe)
        unsafe_prob_formatted = "{:.2f}".format(prob_unsafe)

        if prob_safe > prob_unsafe:
            result = 'Water is SAFE.'
        else:
            result = 'Water is UNSAFE.'

        return render_template('aipred.html', 
                              pred=result,
                              safe_prob=safe_prob_formatted,
                              unsafe_prob=unsafe_prob_formatted,
                              show_result=True)
        
    except Exception as e:
        return render_template('aipred.html', pred=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)