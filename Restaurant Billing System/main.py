import tkinter
import random
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#0A7CFF")
        self.root.title("Resturent Billing System - created by manthan")
        tkinter.Label(self.root, text="Resturent Billing System", bd=12, relief=tkinter.RIDGE,
                      font=("Arial Black", 20), bg="#A569BD", fg="white").pack(fill=tkinter.X)
        # ===================================variables=======================================================================================
        self.samosa = tkinter.IntVar()
        self.paneer_tikka = tkinter.IntVar()
        self.chicken_tikka = tkinter.IntVar()
        self.vegetable_pakora = tkinter.IntVar()
        self.papdi_chaat = tkinter.IntVar()
        self.tomato_soup = tkinter.IntVar()
        self.masala_papad = tkinter.IntVar()
        self.butter_chicken = tkinter.IntVar()
        self.tikka_masala = tkinter.IntVar()
        self.basmathi_rice = tkinter.IntVar()
        self.paneer_masala = tkinter.IntVar()
        self.palak_paneer = tkinter.IntVar()
        self.dal = tkinter.IntVar()
        self.chole_bhuture = tkinter.IntVar()
        self.Noodles = tkinter.IntVar()
        self.aloo_chaat = tkinter.IntVar()
        self.pasta = tkinter.IntVar()
        self.pav_bhaji = tkinter.IntVar()
        self.bhel_puri = tkinter.IntVar()
        self.paani_puri = tkinter.IntVar()
        self.pakora = tkinter.IntVar()
        self.total_sna = tkinter.StringVar()
        self.total_gro = tkinter.StringVar()
        self.total_hyg = tkinter.StringVar()
        self.a = tkinter.StringVar()
        self.b = tkinter.StringVar()
        self.c = tkinter.StringVar()
        self.c_name = tkinter.StringVar()
        self.bill_no = tkinter.StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.phone = tkinter.StringVar()
        # ==========================================customer details label frame=================================================
        details = tkinter.LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#A569BD",
                                     fg="white", relief=tkinter.GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        tkinter.Label(details, text="Customer Name", font=("Arial Black", 14), bg="#A569BD",
                                  fg="white").grid(row=0, column=0, padx=15)

        tkinter.Entry(details, borderwidth=4, width=30, textvariable=self.c_name).grid(row=0, column=1,
                                                                                                    padx=8)

        tkinter.Label(details, text="Contact No.", font=("Arial Black", 14), bg="#A569BD",
                                     fg="white").grid(row=0, column=2, padx=10)

        tkinter.Entry(details, borderwidth=4, width=30, textvariable=self.phone).grid(row=0, column=3,
                                                                                      padx=8)

        tkinter.Label(details, text="Bill.No.", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(
            row=0, column=4, padx=10)

        tkinter.Entry(details, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5,
                                                                                        padx=8)
        # =======================================Resturant Menu=================================================================
        snacks = tkinter.LabelFrame(self.root, text="Starter", font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483",
                                    relief=tkinter.GROOVE, bd=10)
        snacks.place(x=5, y=180, height=380, width=325)

        tkinter.Label(snacks, text="Samosa", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=0,
                                                                                                        column=0,
                                                                                                        pady=11)
        tkinter.Entry(snacks, borderwidth=2, width=15, textvariable=self.samosa).grid(row=0, column=1,
                                                                                      padx=10)

        tkinter.Label(snacks, text="Paneer Tikka", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=1, column=0, pady=11)
        tkinter.Entry(snacks, borderwidth=2, width=15, textvariable=self.paneer_tikka).grid(row=1,
                                                                                            column=1,
                                                                                            padx=10)

        tkinter.Label(snacks, text="Chicken Tikka", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=2, column=0, pady=11)
        tkinter.Entry(snacks, borderwidth=2, width=15, textvariable=self.chicken_tikka).grid(row=2,
                                                                                             column=1,
                                                                                             padx=10)

        tkinter.Label(snacks, text="Vegetable Pakora", font=("Arial Black", 11), bg="#E5B4F3",
                      fg="#6C3483").grid(row=3, column=0, pady=11)
        tkinter.Entry(snacks, borderwidth=2, width=15, textvariable=self.vegetable_pakora).grid(row=3,
                                                                                                column=1,
                                                                                                padx=10)

        tkinter.Label(snacks, text="Papdi Chaat", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=4, column=0, pady=11)
        tkinter.Entry(snacks, borderwidth=2, width=15, textvariable=self.papdi_chaat).grid(row=4,
                                                                                           column=1,
                                                                                           padx=10)

        tkinter.Label(snacks, text="Tomato Soup", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=5, column=0, pady=11)
        tkinter.Entry(snacks, borderwidth=2, width=15, textvariable=self.tomato_soup).grid(row=5,
                                                                                           column=1,
                                                                                           padx=10)

        tkinter.Label(snacks, text="Masala Papad", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=6, column=0, pady=11)
        tkinter.Entry(snacks, borderwidth=2, width=15, textvariable=self.masala_papad).grid(row=6,
                                                                                            column=1,
                                                                                            padx=10)
        # =================================== Main Course =====================================================================================
        grocery = tkinter.LabelFrame(self.root, text="Main Course", font=("Arial Black", 12), relief=tkinter.GROOVE,
                                     bd=10, bg="#E5B4F3", fg="#6C3483")
        grocery.place(x=340, y=180, height=380, width=325)

        tkinter.Label(grocery, text="Butter Chicken", font=("Arial Black", 11), bg="#E5B4F3",
                      fg="#6C3483").grid(row=0, column=0, pady=11)
        tkinter.Entry(grocery, borderwidth=2, width=15, textvariable=self.butter_chicken).grid(row=0,
                                                                                               column=1,
                                                                                               padx=10)

        tkinter.Label(grocery, text="Chicken Tikka Masala", font=("Arial Black", 11), bg="#E5B4F3",
                      fg="#6C3483").grid(row=1, column=0, pady=11)
        tkinter.Entry(grocery, borderwidth=2, width=15, textvariable=self.tikka_masala).grid(row=1,
                                                                                             column=1,
                                                                                             padx=10)

        tkinter.Label(grocery, text="Basmathi Rice", font=("Arial Black", 11), bg="#E5B4F3",
                      fg="#6C3483").grid(row=2, column=0, pady=11)
        tkinter.Entry(grocery, borderwidth=2, width=15, textvariable=self.basmathi_rice).grid(row=2,
                                                                                              column=1,
                                                                                              padx=10)

        tkinter.Label(grocery, text="Paneer Masala", font=("Arial Black", 11), bg="#E5B4F3",
                      fg="#6C3483").grid(row=3, column=0, pady=11)
        tkinter.Entry(grocery, borderwidth=2, width=15, textvariable=self.paneer_masala).grid(row=3,
                                                                                              column=1,
                                                                                              padx=10)

        tkinter.Label(grocery, text="Palak Paneer", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=4, column=0, pady=11)
        tkinter.Entry(grocery, borderwidth=2, width=15, textvariable=self.palak_paneer).grid(row=4,
                                                                                             column=1,
                                                                                             padx=10)

        tkinter.Label(grocery, text="Daal Tadka", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=5, column=0, pady=11)
        tkinter.Entry(grocery, borderwidth=2, width=15, textvariable=self.dal).grid(row=5, column=1,
                                                                                    padx=10)

        tkinter.Label(grocery, text="Chole Bhuture", font=("Arial Black", 11), bg="#E5B4F3",
                      fg="#6C3483").grid(row=6, column=0, pady=11)
        tkinter.Entry(grocery, borderwidth=2, width=15, textvariable=self.chole_bhuture).grid(row=6,
                                                                                              column=1,
                                                                                              padx=10)
        # ========================================Snacks===============================================================================
        hygine = tkinter.LabelFrame(self.root, text="Snacks", font=("Arial Black", 12), relief=tkinter.GROOVE, bd=10,
                                    bg="#E5B4F3", fg="#6C3483")
        hygine.place(x=677, y=180, height=380, width=325)

        tkinter.Label(hygine, text="Noodles", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=0,
                                                                                                         column=0,
                                                                                                         pady=11)
        tkinter.Entry(hygine, borderwidth=2, width=15, textvariable=self.Noodles).grid(row=0, column=1,
                                                                                       padx=10)

        tkinter.Label(hygine, text="Aloo Tikki Chaat", font=("Arial Black", 11), bg="#E5B4F3",
                      fg="#6C3483").grid(row=1, column=0, pady=11)
        tkinter.Entry(hygine, borderwidth=2, width=15, textvariable=self.aloo_chaat).grid(row=1,
                                                                                          column=1,
                                                                                          padx=10)

        tkinter.Label(hygine, text="Pasta", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=2,
                                                                                                       column=0,
                                                                                                       pady=11)
        tkinter.Entry(hygine, borderwidth=2, width=15, textvariable=self.pasta).grid(row=2, column=1,
                                                                                     padx=10)

        tkinter.Label(hygine, text="Pav Bhaji", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=3, column=0, pady=11)
        tkinter.Entry(hygine, borderwidth=2, width=15, textvariable=self.pav_bhaji).grid(row=3, column=1,
                                                                                         padx=10)

        tkinter.Label(hygine, text="Bhel Puri", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=4, column=0, pady=11)
        tkinter.Entry(hygine, borderwidth=2, width=15, textvariable=self.bhel_puri).grid(row=4, column=1,
                                                                                         padx=10)

        tkinter.Label(hygine, text="Paani Puri", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=5, column=0, pady=11)
        tkinter.Entry(hygine, borderwidth=2, width=15, textvariable=self.paani_puri).grid(row=5,
                                                                                          column=1,
                                                                                          padx=10)

        tkinter.Label(hygine, text="Pokara", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=6,
                                                                                                        column=0,
                                                                                                        pady=11)
        tkinter.Entry(hygine, borderwidth=2, width=15, textvariable=self.pakora).grid(row=6, column=1,
                                                                                      padx=10)
        # =====================================================billarea==============================================================================
        billarea = tkinter.Frame(self.root, bd=10, relief=tkinter.GROOVE, bg="#E5B4F3")
        billarea.place(x=1010, y=188, width=330, height=372)

        tkinter.Label(billarea, text="Bill Area", font=("Arial Black", 17), bd=7, relief=tkinter.GROOVE,
                      bg="#E5B4F3", fg="#6C3483").pack(fill=tkinter.X)

        scrol_y = tkinter.Scrollbar(billarea, orient=tkinter.VERTICAL)
        self.txtarea = tkinter.Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=tkinter.BOTH, expand=1)
        # =================================================billing menu=========================================================================================
        billing_menu = tkinter.LabelFrame(self.root, text="Billing Summery", font=("Arial Black", 12),
                                          relief=tkinter.GROOVE, bd=10, bg="#A569BD", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        tkinter.Label(billing_menu, text="Total Starters Price", font=("Arial Black", 11), bg="#A569BD",
                                     fg="white").grid(row=0, column=0)
        tkinter.Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_sna).grid(
            row=0, column=1, padx=10, pady=7)

        tkinter.Label(billing_menu, text="Total Main Course Price", font=("Arial Black", 11),
                      bg="#A569BD", fg="white").grid(row=1, column=0)
        tkinter.Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_gro).grid(
            row=1, column=1, padx=10, pady=7)

        tkinter.Label(billing_menu, text="Total Snacks Price", font=("Arial Black", 11), bg="#A569BD",
                      fg="white").grid(row=2, column=0)
        tkinter.Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_hyg).grid(
            row=2, column=1, padx=10, pady=7)

        tkinter.Label(billing_menu, text="Starter Tax", font=("Arial Black", 11), bg="#A569BD",
                      fg="white").grid(row=0, column=2)
        tkinter.Entry(billing_menu, width=30, borderwidth=2, textvariable=self.a).grid(row=0,
                                                                                       column=3,
                                                                                       padx=10,
                                                                                       pady=7)

        tkinter.Label(billing_menu, text="Main Course Tax", font=("Arial Black", 11), bg="#A569BD",
                      fg="white").grid(row=1, column=2)
        tkinter.Entry(billing_menu, width=30, borderwidth=2, textvariable=self.b).grid(row=1,
                                                                                       column=3,
                                                                                       padx=10,
                                                                                       pady=7)

        tkinter.Label(billing_menu, text="Snacks Tax", font=("Arial Black", 11), bg="#A569BD",
                      fg="white").grid(row=2, column=2)
        tkinter.Entry(billing_menu, width=30, borderwidth=2, textvariable=self.c).grid(row=2,
                                                                                       column=3,
                                                                                       padx=10,
                                                                                       pady=7)

        button_frame = tkinter.Frame(billing_menu, bd=7, relief=tkinter.GROOVE, bg="#6C3483")
        button_frame.place(x=830, width=500, height=95)

        tkinter.Button(button_frame, text="Total Bill", font=("Arial Black", 15), pady=10, bg="#E5B4F3",
                       fg="#6C3483", command=lambda: total(self)).grid(row=0, column=0, padx=12)
        tkinter.Button(button_frame, text="Clear Field", font=("Arial Black", 15), pady=10, bg="#E5B4F3",
                       fg="#6C3483", command=lambda: clear(self)).grid(row=0, column=1, padx=10, pady=6)
        tkinter.Button(button_frame, text="Exit", font=("Arial Black", 15), pady=10, bg="#E5B4F3",
                       fg="#6C3483", width=8, command=lambda: exit1(self)).grid(row=0, column=2, padx=10,
                                                                                pady=6)
        intro(self)


def total(self):
    if self.c_name.get == "" or self.phone.get() == "":
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.nu = self.samosa.get() * 50
    self.no = self.paneer_tikka.get() * 240
    self.la = self.chicken_tikka.get() * 280
    self.ore = self.vegetable_pakora.get() * 180
    self.mu = self.papdi_chaat.get() * 80
    self.si = self.masala_papad.get() * 40
    self.na = self.tomato_soup.get() * 150
    total_snacks_price = (
            self.nu +
            self.no +
            self.la +
            self.ore +
            self.mu +
            self.si +
            self.na)
    self.total_sna.set(str(total_snacks_price) + " Rs")
    self.a.set(str(round(total_snacks_price * 0.09, 3)) + " Rs")

    self.at = self.butter_chicken.get() * 300
    self.pa = self.tikka_masala.get() * 320
    self.oi = self.basmathi_rice.get() * 130
    self.ri = self.paneer_masala.get() * 260
    self.su = self.palak_paneer.get() * 250
    self.te = self.chole_bhuture.get() * 220
    self.da = self.dal.get() * 180
    total_grocery_price = (
            self.at +
            self.pa +
            self.oi +
            self.ri +
            self.su +
            self.te +
            self.da)

    self.total_gro.set(str(total_grocery_price) + " Rs")
    self.b.set(str(round(total_grocery_price * 0.09, 3)) + " Rs")

    self.so = self.Noodles.get() * 180
    self.sh = self.pasta.get() * 180
    self.cr = self.aloo_chaat.get() * 100
    self.lo = self.pav_bhaji.get() * 150
    self.fo = self.bhel_puri.get() * 50
    self.ma = self.paani_puri.get() * 50
    self.sa = self.pakora.get() * 80

    total_hygine_price = (
            self.so +
            self.sh +
            self.cr +
            self.lo +
            self.fo +
            self.ma +
            self.sa)

    self.total_hyg.set(str(total_hygine_price) + " Rs")
    self.c.set(str(round(total_hygine_price * 0.10, 3)) + " Rs")
    self.total_all_bill = (total_snacks_price +
                           total_grocery_price +
                           total_hygine_price +
                           (round(total_grocery_price * 0.01, 3)) +
                           (round(total_hygine_price * 0.10, 3)) +
                           (round(total_snacks_price * 0.05, 3)))
    self.total_all_bil = str(self.total_all_bill) + " Rs"
    billarea(self)


def intro(self):
    self.txtarea.delete(1.0, tkinter.END)
    self.txtarea.insert(tkinter.END, "\tWELCOME TO Restaurant\n\tPhone-No.9823968917")
    self.txtarea.insert(tkinter.END, f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(tkinter.END, f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(tkinter.END, f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(tkinter.END, "\n====================================\n")
    self.txtarea.insert(tkinter.END, "\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(tkinter.END, "\n====================================\n")


def billarea(self):
    intro(self)
    if self.samosa.get() != 0:
        self.txtarea.insert(tkinter.END, f"Samosa\t\t {self.samosa.get()}\t{self.nu}\n")
    if self.paneer_tikka.get() != 0:
        self.txtarea.insert(tkinter.END, f"Paneer Tikka\t\t {self.paneer_tikka.get()}\t{self.no}\n")
    if self.chicken_tikka.get() != 0:
        self.txtarea.insert(tkinter.END, f"Chicken Tikka\t\t {self.chicken_tikka.get()}\t{self.la}\n")
    if self.vegetable_pakora.get() != 0:
        self.txtarea.insert(tkinter.END, f"Vegetable Pakoda\t\t {self.vegetable_pakora.get()}\t{self.ore}\n")
    if self.papdi_chaat.get() != 0:
        self.txtarea.insert(tkinter.END, f"Masala Papdi Chaat\t\t {self.papdi_chaat.get()}\t{self.mu}\n")
    if self.tomato_soup.get() != 0:
        self.txtarea.insert(tkinter.END, f"Tomato Soup\t\t {self.tomato_soup.get()}\t{self.na}\n")
    if self.masala_papad.get() != 0:
        self.txtarea.insert(tkinter.END, f"Masala Papad\t\t {self.masala_papad.get()}\t{self.si}\n")
    if self.butter_chicken.get() != 0:
        self.txtarea.insert(tkinter.END, f"Butter Chicken\t\t {self.butter_chicken.get()}\t{self.at}\n")
    if self.tikka_masala.get() != 0:
        self.txtarea.insert(tkinter.END, f"Paneer Tikka Masala\t\t {self.tikka_masala.get()}\t{self.pa}\n")
    if self.basmathi_rice.get() != 0:
        self.txtarea.insert(tkinter.END, f"Jira Rice\t\t {self.basmathi_rice.get()}\t{self.ri}\n")
    if self.paneer_masala.get() != 0:
        self.txtarea.insert(tkinter.END, f"Paneer Masala\t\t {self.paneer_masala.get()}\t{self.oi}\n")
    if self.palak_paneer.get() != 0:
        self.txtarea.insert(tkinter.END, f"Palak Paneer\t\t {self.palak_paneer.get()}\t{self.su}\n")
    if self.dal.get() != 0:
        self.txtarea.insert(tkinter.END, f"Daal Tadka\t\t {self.dal.get()}\t{self.da}\n")
    if self.chole_bhuture.get() != 0:
        self.txtarea.insert(tkinter.END, f"Chole Bhuture\t\t {self.chole_bhuture.get()}\t{self.te}\n")
    if self.Noodles.get() != 0:
        self.txtarea.insert(tkinter.END, f"Noodles\t\t {self.Noodles.get()}\t{self.so}\n")
    if self.aloo_chaat.get() != 0:
        self.txtarea.insert(tkinter.END, f"Aloo Chaat\t\t {self.aloo_chaat.get()}\t{self.lo}\n")
    if self.pasta.get() != 0:
        self.txtarea.insert(tkinter.END, f"Pasta\t\t {self.pasta.get()}\t{self.sh}\n")
    if self.pav_bhaji.get() != 0:
        self.txtarea.insert(tkinter.END, f"Pav Bhaji\t\t {self.pav_bhaji.get()}\t{self.cr}\n")
    if self.bhel_puri.get() != 0:
        self.txtarea.insert(tkinter.END, f"Bhel Puri\t\t {self.bhel_puri.get()}\t{self.fo}\n")
    if self.paani_puri.get() != 0:
        self.txtarea.insert(tkinter.END, f"Paani Puri\t\t {self.paani_puri.get()}\t{self.ma}\n")
    if self.pakora.get() != 0:
        self.txtarea.insert(tkinter.END, f"Pakode\t\t {self.pakora.get()}\t{self.sa}\n")

    self.txtarea.insert(tkinter.END, f"------------------------------------\n")
    if self.a.get() != "0.0 Rs":
        self.txtarea.insert(tkinter.END, f"Total Starter Tax : {self.a.get()}\n")
    if self.b.get() != "0.0 Rs":
        self.txtarea.insert(tkinter.END, f"Total Main Course Tax : {self.b.get()}\n")
    if self.c.get() != "0.0 Rs":
        self.txtarea.insert(tkinter.END, f"Total Snacks Tax : {self.c.get()}\n")
    self.txtarea.insert(tkinter.END, f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(tkinter.END, f"------------------------------------\n")


def clear(self):
    self.txtarea.delete(1.0, tkinter.END)
    self.samosa.set(0)
    self.paneer_tikka.set(0)
    self.chicken_tikka.set(0)
    self.vegetable_pakora.set(0)
    self.papdi_chaat.set(0)
    self.tomato_soup.set(0)
    self.masala_papad.set(0)
    self.butter_chicken.set(0)
    self.tikka_masala.set(0)
    self.basmathi_rice.set(0)
    self.paneer_masala.set(0)
    self.palak_paneer.set(0)
    self.dal.set(0)
    self.chole_bhuture.set(0)
    self.Noodles.set(0)
    self.aloo_chaat.set(0)
    self.pasta.set(0)
    self.pav_bhaji.set(0)
    self.bhel_puri.set(0)
    self.paani_puri.set(0)
    self.pakora.set(0)
    self.total_sna.set(0)
    self.total_gro.set(0)
    self.total_hyg.set(0)
    self.a.set(0)
    self.b.set(0)
    self.c.set(0)
    self.c_name.set(0)
    self.bill_no.set(0)
    self.bill_no.set(0)
    self.phone.set(0)


def exit1(self):
    self.root.destroy()


root = tkinter.Tk()
obj = Bill_App(root)
root.mainloop()
