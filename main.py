import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
from apyori import apriori
from tkinter.messagebox import showinfo

# Operasi file membaca dataset
data = pd.read_csv('store_data.csv', header=None)

root = tk.Tk()
root.geometry("600x500")
root.title('Apriori GUI using Apriori algorithm - Mohammad Fadhil Fadholi')
root.resizable(False, False)

def event():
    # mengubah dataset menjadi elemen list-list
    records = []
    for i in range(0, 7501):
        records.append([str(data.values[i, j]) for j in range(0, 20)])

    a = float(entry.get())
    b = float(entry2.get())

    rules = apriori(records, min_support=a, min_confidence=b,
                    min_lift=3, min_length=2)
    result = list(rules)
    panjang = str(len(result))

    label3 = tk.Label(
        root, text="\nBanyaknya Strong Aassociation Rules: "+panjang)
    label3.pack()

    label4 = tk.Label(
        root, text="Jika ingin menggunakannya lagi,\njalankan ulang programnya ya:)")
    label4.pack()

    frm = Frame(root)
    frm.pack(side=tk.LEFT, padx=20)

    tv = ttk.Treeview(frm, columns=(1, 2, 3), show="headings")
    tv.pack()

    tv.heading(1, text="Rule")
    tv.heading(2, text="Support")
    tv.heading(3, text="Confidence")

    for item in result:
        pair = item[0]
        items = [x for x in pair]

        tv.insert('', tk.END, values=(
            items[0]+" -> "+items[1], item[1], item[2][0][2]))

    tv.grid(row=0, column=0, sticky='nsew')

    # add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tv.yview)
    tv.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

label = tk.Label(root, text="masukkan minimum support yang anda inginkan")
entry = tk.Entry()
label2 = tk.Label(root, text="masukkan minimum confidence yang anda inginkan")
entry2 = tk.Entry()
tombol = tk.Button(root, text="Hasil", command=event)

label.pack()
entry.pack()
label2.pack()
entry2.pack()
tombol.pack()

root.mainloop()
