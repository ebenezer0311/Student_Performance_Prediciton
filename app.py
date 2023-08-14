from flask import Flask, render_template , request
import pickle
import numpy as np
app=Flask(__name__)

model=pickle.load(open('performance.pickle','rb'))



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['post'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    if prediction<0:
        prediction=0
    return render_template("index.html",prediction_text='Final Grade Marks are likely to be : {}'.format(int(prediction)))

if __name__=="__main__":
    app.run(debug=True)

    