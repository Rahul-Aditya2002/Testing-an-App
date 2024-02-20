import streamlit as st
x=st.radio('Are you a student',options=['Yes','No'])
if x=='Yes':
    st.write('Yes I am a student')
else:
    st.write('No I am not a student')