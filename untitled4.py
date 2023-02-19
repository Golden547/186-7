# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 12:55:17 2023

@author: JSS-SHN
"""

from tkinter import *
from tkinter import messagebox
import base64

root = Tk()
root.title("Unique Encryption")
root.geometry("400x400")
root.config(bg="#99d4c4")

def startEncryption():
    encryption_screen = Toplevel(root)
    encryption_screen.title("Encrypt Data")
    encryption_screen.geometry("400x400")
    encryption_screen.config(bg="#99d4c4")

    Label(encryption_screen, text="Enter File Name", font=("Calibri", 12), bg="#99d4c4").grid(row=0, column=0, padx=10, pady=10)

   
    global file_name_entry
    file_name_entry = Entry(encryption_screen, font=("Calibri", 12), bd=2)
    file_name_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(encryption_screen, text="Enter Text to be Encrypted", font=("Calibri", 12), bg="#99d4c4").grid(row=1, column=0, padx=10, pady=10)

    global encryption_text_data
    encryption_text_data = Text(encryption_screen, font=("Calibri", 12), bd=2)
    encryption_text_data.grid(row=1, column=1, padx=10, pady=10)

    Button(encryption_screen, text="Create", font=("Calibri", 12), bg="#e0f2f1", command=saveData).grid(row=2, column=0, columnspan=2, padx=10, pady=10)


def saveData():
    global file_name_entry, encryption_text_data

    # Get the file name from the entry field
    file_name = file_name_entry.get()

    try:
        file = open(f"{file_name}.txt", "w")
        data = encryption_text_data.get("1.0", END)
        ciphercode = base64.b64encode(data.encode("utf-8"))
        hexciphercode = ciphercode.hex()
        file.write(hexciphercode)
        file.close()
        messagebox.showinfo("Success", "File saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Error Occured: {e}")


#
def startDecryption():
    decryption_screen = Toplevel(root)
    decryption_screen.title("Decrypt Data")
    decryption_screen.geometry("400x400")
    decryption_screen.config(bg="#99d4c4")

    Label(decryption_screen, text="Enter File Name", font=("Calibri", 12), bg="#99d4c4").grid(row=0, column=0, padx=10, pady=10)

  
    global file_name_entry1
    file_name_entry1 = Entry(decryption_screen, font=("Calibri", 12), bd=2)
    file_name_entry1.grid(row=0, column=1, padx=10, pady=10)

    Button(decryption_screen, text="Decrypt", font=("Calibri", 12), bg="#e0f2f1", command=decryptData).grid(row=1, column=0, columnspan=2, padx=10, pady=10)



def decryptData():
    global file_name_entry1

   
