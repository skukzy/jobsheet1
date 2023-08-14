class OperasiFile:
  def __init__(self):
    self.nama_file = ''
    self.isi_file = ''

  def buat(self):
    try:
      f = open(self.nama_file, 'w')
      f.close()
      status = True
    except:
      status = False
    return status

  def sisipkan(self):
    try:
      f = open(self.nama_file, 'w')
      f.write(self.isi_file)
      f.close()
      status = True
    except:
      status = False
    return status

  def baca(self):
    try:
      f = open(self.nama_file, 'r')
      print(f.read())
      f.close()
      status = True
    except:
      status = False
    return status


f = OperasiFile()

mulai = True
while mulai:
  print("1. Buat File")
  print("2. Isi File")
  print("3. Baca File")
  print("4. Selesai")
  pilih = input('Pilih nomor (1/2/3/4): ')

  if pilih == '1':
    f.nama_file = input('nama file: ')
    if f.buat():
      print("File berhasil dibuat.")
    else:
      print("Error tidak bisa buat file.")
  elif pilih == '2':
    f.nama_file = input('nama file: ')
    f.isi_file = input('isi file: ')
    if f.sisipkan():
      print("File berhasil diisi.")
    else:
      print("Error tidak bisa menulis kedalam file.")
  elif pilih == '3':
    f.nama_file = input('nama file: ')
    if f.baca():
      pass
    else:
      print("Error tidak bisa menulis kedalam file.")
  else:
    mulai = False
    print("Selesai.")


