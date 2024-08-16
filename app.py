import streamlit as st
import pickle

def word(password):
  character=[]
  for i in password:
    character.append(i)
  return character
tfidf=pickle.load(open('tfidf.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))
st.title("check your password strenth")
input=st.text_input("enter password",type='password')

button=st.button("Check")

if button:
    data = tfidf.transform([input]).toarray()
    with st.spinner("Processing...."):
      output = model.predict(data)[0]
      st.success(f"## {output}")
      
