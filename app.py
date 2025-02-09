import pandas as pd
from flask import Flask, request, render_template, jsonify
import joblib

app = Flask(__name__)

pipeline = joblib.load('artifacts/preprocessing_pipeline.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.form.to_dict(flat=True)
    df = pd.DataFrame([data])
    price = int(pipeline.predict(df)[0])

    return jsonify({'Price': price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
