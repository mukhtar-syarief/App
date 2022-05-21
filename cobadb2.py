import sqlite3

dbkaryawan = sqlite3.connect('db/data_karyawan.db')
data_karyawan = dbkaryawan.cursor()

# absen_karyawan = []
# with open("data/absen_karyawan.txt") as absensi:
#     absen = absensi.read().split('\n')
#     for absen in absen:
#         absen = absen.split(',')
#         absen = {
#             'nama': absen[0],
#             'waktu': absen[1],
#             'kehadiran':absen[2]
#         }
#         absen_karyawan.append(absen)

# print(absen_karyawan)



# data_karyawan.execute("CREATE TABLE absensi_karyawan (nama text, waktu text, kehadiran text)")

# for absen in absen_karyawan:
#     data_karyawan.execute("INSERT INTO absensi_karyawan VALUES(?, ?, ?)", (absen['nama'], absen['waktu'], absen['kehadiran']))

for x in data_karyawan.execute("SELECT * FROM absensi_karyawan"):
    print(x)

# data_order = []
# with open("data/data_order.txt") as order:
#     order = order.read().split("\n")
#     for order in order:
#         order = order.split(",")
#         order = {
#             'nama': order[0],
#             'waktu': order[1],
#             'nama_produk': order[2],
#             'quantity': int(order[3])
#         }
#         data_order.append(order)

# print(data_order)

# data_karyawan.execute("CREATE TABLE data_order (nama text, waktu text, nama_produk text, quantity integer)")

# for order in data_order:
#     data_karyawan.execute("INSERT INTO data_order VALUES(?,?,?,?)",(order['nama'], order['waktu'], order['nama_produk'], order['quantity']))

for y in data_karyawan.execute("SELECT * FROM data_order"):
    print(y)



# ORDER BY









dbkaryawan.commit()
dbkaryawan.close()