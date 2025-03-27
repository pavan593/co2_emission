from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("co2_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict', methods=['POST'])
def predict():
    # Get input values
    feature1 = float(request.form['feature1'])
    feature2 = float(request.form['feature2'])
    
    # Predict using model
    prediction = model.predict([[feature1, feature2]])
    
    return render_template("result.html", prediction=prediction[0])

    except Exception as e:
        return render_template('result.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
