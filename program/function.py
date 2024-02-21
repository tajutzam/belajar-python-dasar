def displayContact(list_kontak):
    print('Daftar Kontak')
    print('--------------')
    index = 0;
    for item in list_kontak:
        index += 1;
        name = item.get('name')
        number = item.get('number')
        print(f'{index}.Name : {name} => {number}')
        print('--------------')
    
def addContact(list_kontak , **argument):
    list_kontak.append(argument)
    print('success add contact')

def deleteContact(list_kontak , name):
    for item in list_kontak.copy():
        if(item.get('name') == name):
            list_kontak.remove(item)
            print('success hapus kontak')
        else:
            print('kontak tidak ditemukan')

def searchContact(list_kontak , name):
    itemKontak = '';
    isFound = False;
    for item in list_kontak.copy():
        if(item.get('name') == name):
           isFound = True;
           itemKontak = item
        else:
            isFound = False;
    return {'isFound' : isFound , 'item': itemKontak}