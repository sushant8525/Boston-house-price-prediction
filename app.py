from hmac import trans_36
import pickle
from tkinter import Scale
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
from numpy.core.multiarray import array
import pandas as pd
 
app=Flask(__name__)
regmodel=pickle.load(open('regmodel.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict_api',methods=['POST'])
def pridict_api():
    data= request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__=='__main__':
    app.run(debug=True)