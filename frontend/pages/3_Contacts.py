import os
import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
from common import GLOBAL_CSS

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

st.set_page_config(page_title="Contact | Krishnendu Das", page_icon="✉️", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

st.markdown("# Get in touch")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        if not (name and email and message):
            st.warning("Please fill in all fields.")
        else:
            if not SUPABASE_URL or not SUPABASE_KEY:
                st.error("Supabase credentials missing from .env")
            else:
                try:
                    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
                    result = supabase.table("messages").insert({"name": name, "email": email, "message": message}).execute()
                    st.success("Message sent successfully! (Check your Supabase dashboard > Table Editor > 'messages' to verify it was saved).")
                except Exception as e:
                    st.error(f"Something went wrong: {e}")