# IMPORT LIBBRARY SQLITE3
import sqlite3

# CONNECT KE DATABASE
dbmahasiswa = sqlite3.connect("./db/mahasiswa.db")
mahasiswa = dbmahasiswa.cursor()

# MEMBUAT TABEL BARU DENGAN CREATE
# mahasiswa.execute('''CREATE TABLE mahasiswa (nim integer, nama_mahasiswa text, jurusan text, tahun_masuk integer)''')

# MENGECEK TABEL JIKA SUDAH ADA
mahasiswa.execute("SHOW TABLES")

# # 
# mahasiswa.execute("INSERT INTO mahasiswa VALUES (1344201001, 'Babe Cabita', 'Akuntansi', 2013)")
# mahasiswa.execute("INSERT INTO mahasiswa VALUES (1244201001, 'Budi Gunawan', 'Ilmu Komunikasi', 2012)")
# mahasiswa.execute("INSERT INTO mahasiswa VALUES (1444201001, 'Dahlan Iskan', 'Teknik Informatika', 2014)")
# mahasiswa.execute("INSERT INTO mahasiswa VALUES (1544201001, 'Budi Sadikin', 'Matematika', 2015)")


# for row in mahasiswa.execute("SELECT * FROM mahasiswa"):
#     print(row)

# print(type(row))

# data_mahasiswa = [{
#     "nim" : 1444201005,
#     "nama" : "Satya Dharma",
#     "jurusan" : "Aktuaria",
#     "tahun_masuk" : 2014
#     },{
#     "nim" : 1444201004,
#     "nama" : "Tri Sturina",
#     "jurusan" : "Aktuaria",
#     "tahun_masuk" : 2014
#     },{
#     "nim" : 1444201003,
#     "nama" : "Desi Ratnasari",
#     "jurusan" : "Aktuaria",
#     "tahun_masuk" : 2014
#     },{
#     "nim" : 1444201002,
#     "nama" : "Ratna Wulandari",
#     "jurusan" : "Aktuaria",
#     "tahun_masuk" : 2014
#     },{
#     "nim" : 1444201001,
#     "nama" : "Zoya Fitria",
#     "jurusan" : "Aktuaria",
#     "tahun_masuk" : 2014
#     }]


# for data in data_mahasiswa:
#     print(data["nama"])
#     mahasiswa.execute("INSERT INTO mahasiswa VALUES (?,?,?,?)", (data["nim"], data["nama"], data["jurusan"], data["tahun_masuk"]))
# #     # mahasiswa.execute("INSERT INTO mahasiswa VALUES (data["nim"], data["nama"], data["jurusan"], data["tahun_masuk"])")


# for row in mahasiswa.execute("SELECT * FROM mahasiswa"):
#     print(row)


dbmahasiswa.commit()
dbmahasiswa.close()