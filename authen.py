# import kivy
# from kivy.app import App

from guizero import App, Text, TextBox, PushButton, Box

def rot13 (plaintext):
    chipertext = ""
    for pt_chr in plaintext:
        pt_int = ord(pt_chr)

        if (pt_int >= ord('A') and pt_int <= ord('Z')):
            ct_int = pt_int + 13
            if ct_int > ord('Z'):
                ct_int -=26
            chipertext += chr(ct_int)
        elif (pt_int >= ord('a') and pt_int <= ord('z')):
            ct_int = pt_int + 13
            if ct_int > ord('z'):
                ct_int -= 26
            chipertext += chr(ct_int)
        else:
            chipertext += pt_chr
    return chipertext

def encrypt():
    encrypted_text = rot13 (plaintext_text.value)
    chipertext_text.value = encrypted_text
def decrypted():
    decrypted_text = rot13 (chipertext_text.value)
    plaintext_text.value = encrypted_text
def clear_text():
    plaintext_text.value = ""
    chipertext_text.value = ""

app = App(title="ROT13", width=800, height=600)

title = Text(app, text='ROT13 HACKER-ARISE', size=24, height=2)
plaintext_title = Text(app, text="Plaintext: ")
plaintext_text = TextBox(app, width=90, height=10, multiline=True)
button_box = Box(app, height=80, width=220)

encrypt_button = PushButton(button_box, text='Encrypt', align="left", command=encrypt)
decrypt_button = PushButton(button_box, text='Decrypt', align="left", command=encrypt)
clear_button = PushButton(button_box, text='Clear', align="left", command=clear_text)

chipertext_title = Text(app, text="Chipertext: ")
chipertext_text = TextBox(app, width=90, height=10, multiline=True)

app.display()
