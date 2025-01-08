import streamlit as st

from pgss import PageSessionState

pss = PageSessionState("page1.py")

# how to add key 1
if "count" not in pss:
    pss["count"] = 1

# how to add key 2
pss.set_if_not_exist({"count2": 1, "text": ""})

if st.button("Increment"):
    pss["count"] += 1
    pss["count2"] += 2

st.write("This is page1.py")
st.write(f"count: {pss['count']}")
st.write(f"count2: {pss['count2']}")

if text:=st.text_input("Input text", value=pss.text, key=pss("text_key")):
    pss.text = text

st.write(f"pss.text_key: {pss.text_key}")
st.write(f"pss.text: {pss.text}")
