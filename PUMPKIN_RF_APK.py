import pickle
import streamlit as st
import numpy as np

# Membaca model SVM dan scaler
rf = pickle.load(open('rf_model_pumpkin.sav', 'rb'))
scaler = pickle.load(open('scaler_rf_pumpkin.sav', 'rb'))

# Judul web
st.title('Prediksi Class Pumpkin dengan Random Forest')

# Inputan untuk fitur Area, Perimeter, Major_Axis_Length, Minor_Axis_Length, dll
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area", min_value=0.0)
    
with col2:
    perimeter = st.number_input("Perimeter", min_value=0.0)

with col1:
    major_axis_length = st.number_input("Major Axis Length", min_value=0.0)

with col2:
    minor_axis_length = st.number_input("Minor Axis Length", min_value=0.0)

with col1:
    convex_area = st.number_input("Convex Area", min_value=0.0)

with col2:
    equiv_diameter = st.number_input("Equivalent Diameter", min_value=0.0)

with col1:
    eccentricity = st.number_input("Eccentricity", min_value=0.0)

with col2:
    solidity = st.number_input("Solidity", min_value=0.0)

with col1:
    extent = st.number_input("Extent", min_value=0.0)

with col2:
    roundness = st.number_input("Roundness", min_value=0.0)

with col1:
    aspect_ratio = st.number_input("Aspect Ratio", min_value=0.0)

with col2:
    compactness = st.number_input("Compactness", min_value=0.0)

# Inisialisasi variabel untuk prediksi
species_prediction = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Spesies Ikan'):
    # Scaling data input
    scaled_input = scaler.transform([[area, perimeter, major_axis_length, minor_axis_length, convex_area,
                                      equiv_diameter, eccentricity, solidity, extent, roundness,
                                      aspect_ratio, compactness]])

    # Menggunakan model SVM untuk memprediksi spesies
    species_pred = rf.predict(scaled_input)
    species_prediction = species_pred[0]  # Ambil hasil prediksi pertama

    # Tampilkan hasil prediksi
    st.success(f"Spesies yang Diprediksi: {species_prediction}")
