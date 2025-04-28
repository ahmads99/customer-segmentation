import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Load model yang sudah disimpan
kproto = pickle.load(open('model/cluster.pkl', 'rb'))

# Fungsi untuk preprocessing data
def data_preprocess(data):  
    kolom_kategorikal = ['Jenis Kelamin', 'Profesi', 'Tipe Residen']
    
    # Encode kategori
    df_encode = data[kolom_kategorikal].copy()
    df_encode['Jenis Kelamin'] = df_encode['Jenis Kelamin'].map({'Pria': 0, 'Wanita': 1})
    df_encode['Profesi'] = df_encode['Profesi'].map({'Ibu Rumah Tangga': 0, 'Mahasiswa': 1, 'Pelajar': 2, 'Professional': 3, 'Wiraswasta': 4})
    df_encode['Tipe Residen'] = df_encode['Tipe Residen'].map({'Cluster': 0, 'Sector': 1})
    
    # Standardisasi data numerik
    kolom_numerik = ['Umur', 'NilaiBelanjaSetahun']
    df_std = data[kolom_numerik].copy()
    df_std['Umur'] = (df_std['Umur'] - 37.5) / 14.7
    df_std['NilaiBelanjaSetahun'] = (df_std['NilaiBelanjaSetahun'] - 7069874.8) / 2590619.0
    
    # Gabungkan data
    df_model = df_encode.merge(df_std, left_index=True, right_index=True, how='left')
    return df_model

# Fungsi untuk memodelkan (prediksi cluster)
def modelling(data):
    # Prediksi cluster menggunakan model yang telah dimuat
    clusters = kproto.predict(data, categorical=[0, 1, 2])  # Menggunakan model kproto yang sudah dimuat
    return clusters

# Fungsi untuk menambahkan segmentasi berdasarkan cluster
def menamakan_segmen(data_asli, clusters):
    final_df = data_asli.copy()
    final_df['cluster'] = clusters
    final_df['segmen'] = final_df['cluster'].map({
        0: 'Diamond Young Member',
        1: 'Diamond Senior Member',
        2: 'Silver Member',
        3: 'Gold Young Member',
        4: 'Gold Senior Member'
    })
    return final_df

# Streamlit UI
st.title("Customer Segmentation and Clustering")

# Upload File Excel
uploaded_file = st.file_uploader("Upload File Excel", type=["xlsx", "xls"])

if uploaded_file:
    # Membaca file Excel
    df = pd.read_excel(uploaded_file)
    st.write("Data yang di-upload:")
    st.dataframe(df)

    # Preprocessing Data
    df_model = data_preprocess(df)

    # Prediksi Cluster
    clusters = modelling(df_model)

    # Menamakan segmen
    final_df = menamakan_segmen(df, clusters)

    # Menampilkan hasil final
    st.write("Data Setelah Clustering dan Segmentation:")
    st.dataframe(final_df)

    # Menyediakan opsi untuk mengunduh hasilnya
    st.download_button(
        label="Download Hasil Segmentation",
        data=final_df.to_csv(index=False),
        file_name="customer_segmentation_result.csv",
        mime="text/csv"
    )
