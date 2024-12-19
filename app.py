import streamlit as st

st.write('Ayo kita nabung!')

dashboard = st.Page("./pages/dashboard.py", title="Dashboard")
nabung = st.Page("./pages/nabung.py", title="Nabung")

pg = st.navigation({
    "Dashboard" : [dashboard],
    "nabung" : [nabung],
})

if "Nabung" not in st.session_state:
    st.session_state['Nabung'] = [] 

pg.run()