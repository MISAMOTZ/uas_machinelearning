import streamlit as st
import runpy

# Menambahkan CSS untuk styling dan animasi
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            color: #0073e6;
            font-size: 36px;
            animation: fadeIn 2s ease-in-out;
        }
        .sidebar .sidebar-content {
            background-color: #f7f7f7;
            padding: 10px;
        }
        .section-header {
            color: #0073e6;
            font-size: 28px;
            margin-top: 20px;
        }
        .highlight {
            color: #ff6f61;
            font-weight: bold;
        }
        .button {
            background-color: #0073e6;
            color: white;
            border-radius: 8px;
            padding: 10px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #005bb5;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
    </style>
    """, unsafe_allow_html=True)

# Tambahkan header utama dengan animasi
st.markdown('<div class="title">Selamat datang di Aplikasi Multi-Page untuk Machine Learning!</div>', unsafe_allow_html=True)

# Tambahkan deskripsi menarik di halaman utama
st.write("Gunakan menu di sidebar untuk berpindah antar halaman. Kami menyediakan berbagai model untuk prediksi ikan, buah, dan labu.")

# Menambahkan sidebar dengan pilihan menu
selected_menu = st.sidebar.radio(
    "Pilih Menu:",
    ["Home", "Random Forest Ikan", "SVM Ikan", "Random Forest Fruit", "SVM Fruit", "Random Forest Pumpkin", "SVM Pumpkin"]
)

# Fungsi untuk membuat tombol dengan animasi hover
def display_button(text, color="primary"):
    button_html = f'''
    <div class="button">{text}</div>
    '''
    st.markdown(button_html, unsafe_allow_html=True)

# Menampilkan konten berdasarkan pilihan menu
if selected_menu == "Home":
    st.title("Halaman Home")
    st.write("Ini adalah halaman utama.")
    st.write("Silakan pilih model untuk memulai.")
elif selected_menu == "Random Forest Ikan":
    st.title("Prediksi dengan Random Forest Ikan")
    display_button("Prediksi Sekarang", color="primary")
    runpy.run_path('FISH_RF_APK.py')
elif selected_menu == "SVM Ikan":
    st.title("Prediksi dengan SVM Ikan")
    display_button("Prediksi Sekarang", color="primary")
    runpy.run_path('FISH_SVM_APK.py')
elif selected_menu == "Random Forest Fruit":
    st.title("Prediksi dengan Random Forest Buah")
    display_button("Prediksi Sekarang", color="primary")
    runpy.run_path('FRUIT_RF_APK.py')
elif selected_menu == "SVM Fruit":
    st.title("Prediksi dengan SVM Buah")
    display_button("Prediksi Sekarang", color="primary")
    runpy.run_path('FRUIT_SVM_APK.py')
elif selected_menu == "Random Forest Pumpkin":
    st.title("Prediksi dengan Random Forest Labu")
    display_button("Prediksi Sekarang", color="primary")
    runpy.run_path('PUMPKIN_RF_APK.py')
elif selected_menu == "SVM Pumpkin":
    st.title("Prediksi dengan SVM Labu")
    display_button("Prediksi Sekarang", color="primary")
    runpy.run_path('PUMPKIN_SVM_APK.py')
