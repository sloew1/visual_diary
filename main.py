import os
import subprocess
from file import File
from entry import Entry
from crypto import Crypto
from main_gui import MainGUI
from datetime import date, timedelta, datetime
from entry_list import EntryList


def register():
    pw = MainGUI.register()
    Crypto.set_key(pw)


def login():
    pw = MainGUI.login()
    pw_check_file = open('pw_check.txt', 'rb')
    Crypto.loadKeyFromFile(pw)
    pw_check = Crypto.decrypt(pw_check_file)

    if not pw_check:
        print('Falsches Passwort. Programm wird beendet.')
        quit()


def read():
    date = input('Datum?')
    decrypted_data = 0

    try:
        with open('entries/' + date + '.txt', 'rb') as file:
            decrypted_data = Crypto.decrypt(file)

        print('Entschlüsselte Nachricht: ' + decrypted_data.decode('utf-8'))
    except FileNotFoundError:
        print('Datei nicht gefunden.')
        return Exception

    return decrypted_data


def create():
    text = MainGUI.writeEntry()
    encrypted_data = Crypto.encrypt(text)

    file = File(datetime.utcnow().strftime('%m-%d-%H:%M:%S'))
    file.writeToFile(encrypted_data)


def getDateFromString(str_date):
    # start_date = date(2008, 8, 15)
    # end_date = date(2008, 9, 15)
    year = int(str_date[6:10])
    month = int(str_date[0:2])
    day = int(str_date[3:5])

    return date(year, month, day)


MainGUI.load_gui()
b=0

'''
text = 'Hallo Liebes Tagebuch lol\nneue Zeile lol'
text2 = 'Hallo Liebes Tagebuch lol\nneue Zeile lol2222'
e = Entry()
e2 = Entry()
e.set_text(text)
e2.set_text(text2)
e.set_date(datetime.utcnow())
e2.set_date(datetime.utcnow())
file = File(datetime.now().strftime('%m-%d-%H:%M:%S'))
file.writeToFile(bytes(text, 'utf-8'))
entry_list = Entry.get_entry_list(datetime.now() - timedelta(minutes=600), datetime.now() - timedelta(minutes=200))

#PDF erzeugen Test:
file.create_multipage_pdf(entry_list)
#PDF anzeigen:
#subprocess.call(["xdg-open", 'pdf/' + file.filename + '.pdf'])

#date_start = getDateFromString('02-09-2023')
#date_end = getDateFromString('02-12-2023')
#el = EntryList(date_start, date_end)

# Wenn salt-File existiert, gibt es bereit eine Anmeldung -> login(), falls nicht dann register()

try:
    with open('salt.salt', 'rb') as file:
        file.read()

    login()
except FileNotFoundError:
    register()

# Eintrag schreiben:
create()

#Eintrag lesen, anhand von Datum
read()


pw = input('Passwort wählen: ')
key = Crypto.generate_key(pw)
text = input('Eintrag schreiben: ')
Crypto.encrypt(text, key, 'file1.txt')
Crypto.decrypt('file1.txt', key)

file1 = File('file1.txt')
file1.append('append')
'''




