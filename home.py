import streamlit as st
import runpy

# Tambahkan menu
selected_menu = st.sidebar.radio("Pilih Menu:", ["Home", "Random Forest Ikan", "SVM Ikan", "Random Forest Fruit", "SVM Fruit", "Random Forest Pumpkin", "SVM Pumpkin"])

if selected_menu == "Home":
    st.title("Halaman Home")
    st.write("Ini adalah halaman utama.")
elif selected_menu == "Random Forest Ikan":
    # Gunakan runpy untuk mengeksekusi file .py
    runpy.run_path('FISH_RF_APK.py')
elif selected_menu == "SVM Ikan":
    # Gunakan runpy untuk mengeksekusi file .py
    runpy.run_path('FISH_SVM_APK.py')
elif selected_menu == "Random Forest Fruit":
    # Gunakan runpy untuk mengeksekusi file .py
    runpy.run_path('FRUIT_RF_APK.py')
elif selected_menu == "SVM Fruit":
    # Gunakan runpy untuk mengeksekusi file .py
    runpy.run_path('FRUIT_SVM_APK.py')
elif selected_menu == "Random Forest Pumpkin":
    # Gunakan runpy untuk mengeksekusi file .py
    runpy.run_path('PUMPKIN_RF_APK.py')
elif selected_menu == "SVM Pumpkin":
    # Gunakan runpy untuk mengeksekusi file .py
    runpy.run_path('PUMPKIN_SVM_APK.py')
