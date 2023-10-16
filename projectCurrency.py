import requests
import _tkinter 

import tkinter as tk 
from tkinter import *
import tkinter.messagebox 
#GUI-------------------------------------------------------------------------------------------------------
root = tk.Tk()

root.title("Taha Polat Döviz Kuru Çeviricisi")

Tops = Frame(root, bg = '#ff0028', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Taha Polat Döviz Kuru Çeviricisi ',
					bg='#ff0028', fg='white')
headlabel.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("Para Birimi")
variable2.set("Para Birimi")

#Gerçek Zamanlı Kur Hesaplayıcı Program Fonksiyonu----------------------------------------------------------

def RealTimeCurrencyConversion():
	from forex_python.converter import CurrencyRates
	c = CurrencyRates()

	from_currency = variable1.get()
	to_currency = variable2.get()

	if (Amount1_field.get() == ""):
		tkinter.messagebox.showinfo("HATA !!", "Miktar Girilmedi.\n Lütfen Uygun Bir Miktar Giriniz!")

	elif (from_currency == "Para Birimi" or to_currency == "Para Birimi"):
		tkinter.messagebox.showinfo("Hata !!",
									"Para Birimi Seçilmedi .\n Lütfen Menüden Uygun Bir Para Birimi Seçiniz!.")

	else:
		new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
		new_amount = float("{:.4f}".format(new_amt))
		Amount2_field.insert(0, str(new_amount))

#clearing all the data entered by the user
def clear_all():
	Amount1_field.delete(0, tk.END)
	Amount2_field.delete(0, tk.END)


CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "TRY"]

root.configure(background='#e6e5e5')
root.geometry("700x400")

Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Miktar : ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Neyden : ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Neye : ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Sonuç : ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)

FromCurrency_option.grid(row=3, column=0, ipadx=0, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=0, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=10, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=0, sticky=E)

Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Dönüştür ", padx=2, pady=2, bg="#ff2800", fg="white",
				command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Hepsini Temizle ", padx=2, pady=2, bg="#ff2800", fg="white",
				command=clear_all)
Label_9.grid(row=10, column=0)


root.mainloop()

