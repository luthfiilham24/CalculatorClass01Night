import streamlit as st

st.title("Kalkulator Sederhana")

# Input angka
num1 = st.number_input("Masukkan Angka Pertama", value=0.0)
num2 = st.number_input("Masukkan Angka Kedua", value=0.0)

# Pilih operasi
operation = st.selectbox(
    "Pilih Operasi",
    ["Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)"]
)

# Tombol hitung
if st.button("Hitung"):
    if operation == "Tambah (+)":
        result = num1 + num2
    elif operation == "Kurang (-)":
        result = num1 - num2
    elif operation == "Kali (×)":
        result = num1 * num2
    elif operation == "Bagi (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Tidak bisa membagi dengan nol"

    st.subheader("Hasil:")
    st.success(result)