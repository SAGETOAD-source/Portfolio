import streamlit as st
from common import GLOBAL_CSS
from data import CERTIFICATIONS

st.set_page_config(page_title="Certifications | Krishnendu Das", page_icon="🎓", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

certifications = CERTIFICATIONS

st.markdown("# Certifications")

if not certifications:
    st.warning("No certifications found.")
else:
    for c in certifications:
        with st.container(border=True):
            st.markdown(f"**{c['name']}**")
            st.caption(f"{c['org']} — {c['year']}")