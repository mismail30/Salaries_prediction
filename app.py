import numpy as np
import pandas as pd
import streamlit as st
import joblib

regressor  = joblib.load('finalmodel.pkl')

def welcome():
    return "Welcome All"

def predict_salary(Rating, Status, Roles, Level, Region):
    prediction = regressor.predict(pd.DataFrame({'Rating':[Rating],'Employment Status':[Status], 'Job Roles':[Roles], 'Level':[Level], 'Region':[Region]}
))
    print(prediction)
    return prediction

def main():
    st.title("Predict Salary")
    html_temp = """
    <div style ="background-color:tomato;padding;10px">
    <h2 stylr = "color:white;text-align:center;">Predict Salary ML App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html =True)
    Rating = st.text_input("Rating","Type Here")
    Status = st.selectbox('Please select status ?',    ('Full Time', 'Trainee', 'Intern', 'Contractor'))
    Roles = st.selectbox('Choose Department',    ('SDE', 'Java', 'Frontend', 'Backend', 'Android', 'SDET', 'Testing','IOS', 'Database', 'Web', 'Mobile'))
    Level = st.selectbox('Choose your Level',    ('Junior', 'Senior', 'Middle', 'Principal', 'Specialist', 'Staff','Manager', 'Head', 'Assistant'))
    Region = st.selectbox('Choose your Region',    ('West India', 'South India', 'Western Region', 'Central India','East India', 'North India'))
    result = ""
    
    if st.button("predict"):
        result= predict_salary(Rating,Status,Roles, Level, Region)
    st.success("Your Salary is{}".format(result))
    if st.button ("About"):
        st.text("Data source")
        st.text("https://www.kaggle.com/datasets/iamsouravbanerjee/software-professional-salaries-2022")
        
if __name__=='__main__':
    main()
