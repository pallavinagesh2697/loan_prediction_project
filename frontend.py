import pandas as pd
import streamlit as st
import pickle
st.set_page_config(page_title='Loan_Predictor')
st.header('Welcome to loan predictor application!!!')
st.header('Please enter your details to continue......')
df=pd.read_csv('cleaned.csv')
with open('model.pkl','rb') as file:
    model=pickle.load(file)
objects={}
for i in df.columns:
    if df[i].dtype==object:
        objects[i]=list(df[i].unique())
        objects[i].sort()
with st.container(border=True):
    age=st.number_input('person_age:',min_value=18,max_value=90)
    gender=st.selectbox('person_gender:',options=objects['person_gender'])
    education=st.selectbox('person_education:',options=objects['person_education'])
    income=st.number_input('person_income:')
    experience=st.number_input('person_emp_exp:')
    ownership=st.selectbox('person_house_ownership:',options=objects['person_home_ownership'])
    loan_amount=st.number_input('loan_amount:')
    loan_intent=st.selectbox('loan_intent:',options=objects['loan_intent'])
    loan_int_rate=st.number_input('loan_int_rate')
    loan_percent_income=st.number_input('loan_percent_income:')
    cb_person_cred_hist_length=st.number_input('credit_history:')
    credit_score=st.number_input('credit_score')
    previous_loan_defaults_on_file=st.selectbox('is there any previous loan default on file:',options=objects['previous_loan_defaults_on_file'])
    input_vals=[[age,objects['person_gender'].index(gender),objects['person_education'].index(education),income,experience,objects['person_home_ownership'].index(ownership),loan_amount,objects['loan_intent'].index(loan_intent),loan_int_rate,loan_percent_income,cb_person_cred_hist_length,credit_score,objects['previous_loan_defaults_on_file'].index(previous_loan_defaults_on_file)]]
    c1,c2,c3=st.columns([1.9,1.8,1])
    if c2.button('submit'):
        out=model.predict(input_vals)
        if out[0]==1:
            st.subheader('Loan can be sanctioned')
        else:
            st.subheader('Loan can not be sanctioned')
