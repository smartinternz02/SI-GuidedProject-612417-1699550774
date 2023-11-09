from flask import Flask,render_template,request
import pickle
#import pandas as pd
#import numpy as np

# loading my mlr model
model=pickle.load(open('Travel.pkl','rb'))

# Flask is used for creating your application
# render template is use for rendering the html page

app= Flask(__name__)  # your application


@app.route('/')  # default route 
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST']) # prediction route
def predict():
    Age = request.form['Age']
    EmploymentType = request.form['EmploymentType']
    if EmploymentType == 'Private Sector/Self Employed':
        EmploymentType = 1
    if EmploymentType == 'Government Sector':
        EmploymentType = 0
        
    AnnualIncome = request.form['AnnualIncome']
    
    FamilyMembers = request.form['FamilyMembers']
    ChronicDiseases = request.form['ChronicDiseases']
    if ChronicDiseases == 'Yes':
        ChronicDiseases = 1
    if ChronicDiseases == 'No':
        ChronicDiseases = 0
    FrequentFlyer = request.form['FrequentFlyer']
    if FrequentFlyer == 'Yes':
        FrequentFlyer = 1
    if FrequentFlyer == 'No':
        FrequentFlyer = 0
        
    EverTravelledAbroad = request.form['EverTravelledAbroad']
    if EverTravelledAbroad == 'Yes':
        EverTravelledAbroad = 1
    if EverTravelledAbroad == 'No':
        EverTravelledAbroad = 0
        
    total = [[int(Age), int(EmploymentType), float(AnnualIncome), FamilyMembers , int(ChronicDiseases), int(FrequentFlyer) , int(EverTravelledAbroad),0,0]]
    prediction = model.predict(total)
    if prediction == 1:
        prediction = 'Yes'
    if prediction == 0:
        prediction = 'No' 
    
    return render_template("index.html", result = "Would the Travel insurance be favourable to the customer? " + str(prediction))

    
    
    
# running your application
if __name__ == "__main__":
    app.run(port = 8000)

#http://localhost:5000/ or localhost:5000