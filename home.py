import streamlit as st

st.title("Home")
st.write("Selamat datang di aplikasi Multi-Page untuk Machine Learning!")
st.write("Gunakan menu di sidebar untuk berpindah antar halaman.")

# Tambahkan deskripsi atau informasi di sidebar
st.sidebar.title("Navigasi Aplikasi")
st.sidebar.info("Gunakan menu di bawah untuk berpindah antar halaman.")

# Tambahkan menu
selected_menu = st.sidebar.radio("Pilih Menu:", ["Home", "Random Forest", "SVM"])

if selected_menu == "Home":
    st.title("Halaman Home")
    st.write("Ini adalah halaman utama.")
elif selected_menu == "Random Forest":
    st.title("Halaman Random Forest")
    st.write("Ini adalah halaman untuk Random Forest.")
    import FISH_RF_APK 
elif selected_menu == "SVM":
    st.title("Halaman SVM")
    st.write("Ini adalah halaman untuk SVM.")
