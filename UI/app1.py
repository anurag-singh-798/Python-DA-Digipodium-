import streamlit as st
from random import choice

st.title("Name generator")

fnames = ['Alex','Bob','Charlie','David','Eve','Frank','George']

lnames = ['Anderson','Baker','Clark','Davis','Evans','Foster','Harris']

btn = st.button("Generate name")
if btn:
    fn = choice(fnames)
    ln = choice(lnames)
    fullname = f"{fn} {ln}"
    st.success(fullname)

# streamlit run UI/app1.py