import streamlit as st
import runpy

# Tambahkan menu
selected_menu = st.sidebar.radio("Pilih Menu:", ["Home", "Random Forest", "SVM"])

if selected_menu == "Home":
    st.title("Halaman Home")
    st.write("Ini adalah halaman utama.")
elif selected_menu == "Random Forest":
    # Gunakan runpy untuk mengeksekusi file .py
    runpy.run_path('FISH_RF_APK.py')
elif selected_menu == "SVM":
    # Gunakan runpy untuk mengeksekusi file .py
    runpy.run_path('FISH_SVM_APK.py')
