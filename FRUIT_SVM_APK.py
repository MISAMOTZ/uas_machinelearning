import pickle
import streamlit as st 
import numpy as np

# Membaca model SVM
svm = pickle.load(open('svm_model_fruit.sav', 'rb'))


# Judul web
st.title('Prediksi Nama Buah dengan SVM')

# Inputan untuk fitur diameter, berat, warna merah, hijau, dan biru
col1, col2 = st.columns(2)

with col1:
    diameter = st.number_input("Diameter (diameter)", min_value=0.0)
    
with col2:
    weight = st.number_input("Berat (weight)", min_value=0.0)

with col1:
    red = st.number_input("Warna Merah (red)", min_value=0)
    
with col2:
    green = st.number_input("Warna Hijau (green)", min_value=0)
    
with col1:
    blue = st.number_input("Warna Biru (blue)", min_value=0)

# Inisialisasi variabel untuk prediksi
buah_prediction = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Nama Buah'):

    # Scaling data input
    scaled_input = ([[diameter, weight, red, green, blue]])  # Pastikan input dua dimensi
    
    # Menggunakan model untuk memprediksi spesies
    buah_pred = svm.predict(scaled_input)  # Gunakan scaled_input
    buah_prediksi = buah_pred[0]  # Ambil hasil prediksi pertama

    # Tampilkan hasil prediksi
    st.success(f"Nama buah yang Diprediksi: {buah_prediksi}")
