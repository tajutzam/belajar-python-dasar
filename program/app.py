


import function

# membuat program daftar kontak
# lsit of dictionary
list_kontak = [
  {"name" : "mohammad tajut zamzami" , 'number' : "085607185972"}
]

# menu program

while True:
    print('#Menu')
    print('1.Daftar Kontak')
    print('2.Tambah Kontak')
    print('3.Hapus Kontak')
    print('4.Cari Kontak')
    print('0.Keluar program')
    menu = input('Silahkan pilih menu : ')
    if menu == '0':
        break;
    
    if menu == '1':
      function.displayContact(list_kontak)
    elif menu == '2':
      print("Tambah kontak") 
      nameContact = input('masukan nama : ')
      numberContact = input('masukan nomer : ')
      function.addContact(list_kontak , name = nameContact, number = numberContact )
      function.displayContact(list_kontak);
    elif menu == '3':
      print("Hapus kontak")
      name = input('Masukan Nama kontak : ')
      function.deleteContact(list_kontak , name)
    elif menu == '4':
      print("Cari Kontak")
      name = input('Masukan Nama kontak : ')
      kontak = function.searchContact(list_kontak , name)
      if kontak.get('isFound') :
        print(kontak.get('item'))
      else:
        print('kontak not found')
        
      
      
      