import streamlit as st

from pgss import PageSessionState

pss = PageSessionState("page2.py")
pss.set_if_not_exist({"count": 1, "text": ""})

if st.button("Increment"):
    pss["count"] += 1

st.write("This is page2.py")
st.write(f"count: {pss['count']}")

if text:=st.text_input("Input text", value=pss.text, key=pss("text_key")):
    pss.text = text

st.write(f"pss.text_key: {pss.text_key}")
st.write(f"pss.text: {pss.text}")