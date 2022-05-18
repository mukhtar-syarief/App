import sqlite3

dbmahasiswa = sqlite3.connect("./db/mahasiswa.db")
mahasiswa = dbmahasiswa.cursor()

# mahasiswa.execute('''CREATE TABLE mahasiswa (nim integer, nama_mahasiswa text, jurusan text, tahun_masuk integer)''')
# mahasiswa.execute("INSERT INTO mahasiswa VALUES (1344201001, 'Babe Cabita', 'Akuntansi', 2013)")
# mahasiswa.execute("INSERT INTO mahasiswa VALUES (1244201001, 'Budi Gunawan', 'Ilmu Komunikasi', 2012)")
# mahasiswa.execute("INSERT INTO mahasiswa VALUES (1444201001, 'Dahlan Iskan', 'Teknik Informatika', 2014)")
# mahasiswa.execute("INSERT INTO mahasiswa VALUES (1544201001, 'Budi Sadikin', 'Matematika', 2015)")


for row in mahasiswa.execute("SELECT * FROM mahasiswa"):
    print(row)


dbmahasiswa.commit()
dbmahasiswa.close()