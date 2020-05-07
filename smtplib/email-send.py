import smtplib

pengirimEmail = "pengirimemail@gmail.com"
penerimaEmail = "penerimaemail@gmail.com"
password = input(str("Masukkan Password : "))
pesan = "Halo dunia, pesan ini dikirim menggunakan python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(pengirimEmail, password)
print("Login sukses")
server.sendmail(pengirimEmail, penerimaEmail, pesan)
print("Email telah dikirim ke ", penerimaEmail)


# peringatan: jangan coba kalau akun email anda bermasalah
