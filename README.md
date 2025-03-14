# Tarang AI: Water Safety Predictor
Trang AI is a dynamic web application tool that uses advanced AI/ML algorithm to predict water safety across various parameters based on real-time inputs from the user. It also offers other features like water safety tips, flagging personal concerns etc.

# Overview
This project predicts water safety based on environmental parameters using a Random Forest Classifier model. It preprocesses water quality data, trains a Random Forest Classifier model, calibrates it, and provides predictions i.e. probability of the water being safe or probability or it being unsafe. The frontend has an easy to use user-friendly interface. Tarang Ai is built using Python, Flask, HTML, Tailwind CSS, JS.

# Key Files
home.html - The main frontend entry point
app.py - Flask backend that handles frontend to backend integration
rfc.py - Python file used to make Random Foreset Classifier model
static/ - CSS, JavaScript, and images
templates/ - HTML templates (including home.html)

# Install dependencies
pip install -r requirements.txt

# Usage
1. Run the Flask application: app.py
2. It will give a local host link, click on it
3. Open your web browser and navigate to the localhost:5000
4. The AI Prediction page or aipred.html interface will be served automatically
5. Fill in the parameters to get water safety AI based prediction.

# Project Structure
TarangAI/

├── rfc.py                  

├── app.py 

├── model.pkl

├── used_sorted_water_data.csv

├── templates/              

│   └── aipred.html 

│   └── home.html

│   └── insights.html

│   └── tips.html

│   └── flag.html

├── static/

│   ├── css/ 

│   │   └── style.css

│   ├── js/  

│   │   └── script.js

│   ├── images/   

│   │   └── [a bunch of .jpg and .png files]

├── requirements.txt 

├── vercel.json 

└── README.md  

# How It Works
The app.py file serves as the backend for this application. It:
1. Hosts the web server
2. Processes prediction requests
3. Serves the aipred.html file dynamically
4. Handles any calls made from the frontend

The aipred.html file provides the user interface where users can:
1. Input data for predictions
2. View prediction results
3. Interact with the AI model

# The Concept
1. Model Training
   - The RFC is trained using a dataset where inputs are mapped to known outputs.  
   - It builds multiple decision trees during training, each learning patterns from different parts of the data.  
   - The final prediction is made by averaging the votes from all trees, making the model robust and less prone to overfitting.  
2. Converting the Model to PKL (Pickle Format) 
   - The model is is saved as a binary file using Pickle to preserve its learned patterns.  
3. Flask Integration 
   - The saved pkl file is loaded into Flask when the server starts.  
   - Users send input data to the Flask which processes the data and passes it to the model.  
   - The model makes a prediction and Flask sends the result back to the user in a structured format.  
4. Flow
   - A user interacts with frontend and sends request to backend (by fill in the parameters forms and clicking predict button) 
   - Flask receives the request, extracts the input, and processes it into the correct format.  
   - The trained RFC model, loaded from the PKL file, analyzes the input and returns a prediction.  
   - The prediction is sent back to the user as a response, enabling real-time decision-making. 
