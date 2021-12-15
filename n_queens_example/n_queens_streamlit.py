import streamlit as st
from n_queens_cp_model import streamlit_call_n_queens

st.title("N Queens Example")
st.sidebar.button("Run!")
# raw_data = st.sidebar.file_uploader("Upload MTM Delta File", type = ['xlsx']) #Input Data1 File