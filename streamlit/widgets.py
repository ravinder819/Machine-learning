import streamlit as st
import  pandas as pd
st.title('streamlit text input')
name=st.text_input('enter your name:')

age=st.slider('select your age :',0,100,25)
st.write(f"your age is {age}")

options =['pyhton','html','c++','java']
choice=st.selectbox('chose your favorite language:',options)
st.write(f'you selected {choice}')

if name:
    st.write(f'hello {name}')

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df=pd.DataFrame(data)
df.to_csv('sampledata.csv1')
st.write(df)

uploaded_file=st.file_uploader('choose a csv file',type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
