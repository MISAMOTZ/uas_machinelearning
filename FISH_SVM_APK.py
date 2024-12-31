import pickle
import streamlit as st
import numpy as np


st.title("Support Vector Machine (SVM)")
st.write("Ini adalah halaman untuk SVM.")

# Membaca model SVM dan scaler
svm = pickle.load(open('svm_model_fish_data.sav', 'rb'))
scaler = pickle.load(open('scaler_svm_fish.sav', 'rb'))

# Judul web
st.title('Prediksi Spesies Ikan dengan SVM')

# Inputan untuk fitur panjang, berat, dan rasio lebar
col1, col2 = st.columns(2)

with col1:
    length = st.number_input("Panjang (length)", min_value=0.0)

with col2:
    weight = st.number_input("Berat (weight)", min_value=0.0)

with col1:
    w_l_ratio = st.number_input("Rasio Lebar (w_l_ratio)", min_value=0.0)

# Inisialisasi variabel untuk prediksi
species_prediction = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Spesies Ikan'):
    # Scaling data input
    scaled_input = scaler.transform([[length, weight, w_l_ratio]])

    # Menggunakan model SVM untuk memprediksi spesies
    species_pred = svm.predict(scaled_input)
    species_prediction = species_pred[0]  # Ambil hasil prediksi pertama

    # Tampilkan hasil prediksi
    st.success(f"Spesies yang Diprediksi: {species_prediction}")
