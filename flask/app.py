import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [int(x) for x in request.form.values()]
    for i in x_test:
     if x_test[i].dtype == 'object':
        if len(list(x_test[i].unique())) >= 1:
            l.fit(x_test[i])
            x_test[i] = l.transform(x_test[i])

    '''x_test=oh.transform(x_test).toarray()'''
    prediction=model.predict(x_test)
    output=prediction[0]
    
    if(output==0):
        return render_template('index.html', prediction_text='Attrition = No')
    else:
        return render_template('index.html', prediction_text='Attrition = Yes')        
if __name__ == "__main__":
    app.run(debug=True)