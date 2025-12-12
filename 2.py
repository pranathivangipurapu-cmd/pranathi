import streamlit as st
st.title ("welcome to streamlit")
num1=st.number_input("enetr number 1")


num2=st.number_input("enter number 2")
sum=num1+num2
st.button("addition")
st.write("sum is:",sum)
num=st.number_input("enter number 1",step=1)
num=st.number_input("enter number 2",step=1)

sum=num1+num2
if st.button("add"):
    st.write("sum is:",sum)


sub=num1-num2
if st.button("sub"):
    st.write("sub is :",sub)

import streamlit as st
st.title("welcome to streamlit")
username=st.text_input("enter username")
password=st.text_input("enter password")
if st.button("login"):
    if username=="admin":
        if password=="1234":
            st.success("valid user")
        else:
            st.error("invalid password")
    else:
        st.error("invalid username")
