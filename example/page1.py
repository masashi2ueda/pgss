import streamlit as st

from pgss import PageSessionState

pss = PageSessionState(__file__)

# keyがない場合に追加方法1
if "count" not in pss:
    pss["count"] = 1

# keyがない場合に追加する方法2
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
