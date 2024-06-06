import streamlit as st
import streamlit_authenticator as stauth


hashed_password = stauth.Hasher(['securepassword']).generate()
print(hashed_password)