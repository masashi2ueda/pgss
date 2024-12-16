import streamlit as st
from pgss import PageSessionState

pss = PageSessionState(__file__)
pss.set_if_not_exist({"count": 1})

if st.button("Increment"):
    pss["count"] += 1

st.write("This is page1.py")
st.write(f"cout: {pss['count']}")
