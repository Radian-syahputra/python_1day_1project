# Penggunaan Library baru Pandas :
# pandas adalah library untuk mengolah data berbentuk tabel, seperti Excel di dalam Python. Ada dua istilah yang perlu kamu hafal:
# Istilah	Artinya	                                Analogi
# DataFrame	seluruh tabel (baris dan kolom) 	satu sheet Excel
# Series	satu kolom dari tabel	            satu kolom di Excel
import pandas as pd


#  Membuat File csv menjadi data frame 
def muat_dataset(path : str) -> pd.DataFrame :
    df : pd.DataFrame = pd.read_csv(path)
    return df


# Lihat Sekilas Isi tabel
def lihat_sekilas(df : pd.DataFrame) -> None :
    print(df.head())
    print(df.tail())
    print(df.shape)
    print(df.columns)

def cek_struktur(df : pd.DataFrame) -> None :
    print(df.info())
    print(df.dtypes)
    print(df.describe())

def cek_kualitas(df : pd.DataFrame) -> None :
    jumlh_kosong : pd.Series = df.isnull().sum()
    jumlh_duplikat : int = df.duplicated().sum()

    print(jumlh_kosong)
    print(jumlh_duplikat)

def take_columns(df : pd.DataFrame) -> None :
    umur = df["Age"]
    gula_dan_bmi = df["Glucose", "BMI"]
    print(umur)
    print(gula_dan_bmi)
    
def filter_passien(df : pd.DataFrame)-> None :
    gula_tinggi  =  df[df["Glucose"] > 140]
    lansia_diabetes = df[df["Age"] > 50] & df[df["Outcome"]]

    print(len(gula_tinggi))
    print(len(lansia_diabetes))