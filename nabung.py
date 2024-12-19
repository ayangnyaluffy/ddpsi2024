import streamlit as st

st.title("Ini Halaman nabung!")

with st.form("Nabung"):
    nama = st.text_input("Masukkan nama")
    nomimal = st.number_input("Masukkan nominal nabung")
    SubmitButton = st.form_submit_button("Simpan")

    if SubmitButton :
        st.write(nama)
        st.session_state['Nabung'].append({
            "Nama" : nama,
            "Nominal" : nomimal,
        })
        st.success("Berhasil menabung!")