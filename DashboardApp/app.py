import streamlit as st

# Create a multi-page app
st.set_page_config(page_title="Dashboard App", layout="wide")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Executive Overview", "Diagnóstico", "Árbol de KPIs"])

# Global Filter
st.sidebar.markdown("## Filters")
# You can add global filters here, for example:
# filter_value = st.sidebar.slider('Select a value', 0, 100, 50)

# Pages
if page == "Executive Overview":
    st.title("Executive Overview")
    st.markdown("This is the Executive Overview page.")
    # Add content for Executive Overview page here

elif page == "Diagnóstico":
    st.title("Diagnóstico")
    st.markdown("This is the Diagnóstico page.")
    # Add content for Diagnóstico page here

elif page == "Árbol de KPIs":
    st.title("Árbol de KPIs")
    st.markdown("This is the Árbol de KPIs page.")
    # Add content for Árbol de KPIs page here