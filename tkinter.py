from tkinter import *

def calculate_total():
    total = (int(Burger_sb.get()) * 2 +
             int(Steak_sb.get()) * 4 +
             int(Crab_sb.get()) * 5 +
             int(Coketail_sb.get()) * 5 +
             int(Tea_sb.get()) * 3 +
             int(Juice_sb.get()) * 5)
    total_label.config(text=f"Total: ${total}")

window = Tk()
window.title("Snack de HAJAR et IHSSANE")
window.minsize(width=500, height=700)
window.configure(bg="pink")

resto_name = Label(text="Welcome to Hajar Restaurant", font=("Times New Roman", 20, "bold"), bg="pink")
resto_name.grid(column=1, row=0)

quote = Label(text="Petit snack peut créer votre jour", font=("Times New Roman", 18, "italic"), bg="pink")
quote.grid(column=1, row=2)

Burger = PhotoImage(file="burgeri.png")
Burger_Label = Label(image=Burger, borderwidth=0)
Burger_Label.place(x=50, y=130)
Burger_info = Label(text="Burger, Tomato =$2", font=("Times New Roman", 10, "normal"), bg="pink")
Burger_info.place(x=40, y=230)
Burger_sb = Spinbox(from_=0, to=10, width=5)
Burger_sb.place(x=80, y=270)

Steak = PhotoImage(file="steako.png")
Steak_Label = Label(image=Steak, borderwidth=0)
Steak_Label.place(x=200, y=130)
Steak_info = Label(text="Steak, Viande, sauce =$4", font=("Times New Roman", 10, "normal"), bg="pink")
Steak_info.place(x=210, y=230)
Steak_sb = Spinbox(from_=0, to=10, width=5)
Steak_sb.place(x=225, y=270)

Crab = PhotoImage(file="crabo.png")
Crab_Label = Label(image=Crab, borderwidth=0)
Crab_Label.place(x=350, y=130)
Crab_info = Label(text="Crab, Tomato, épices =$5", font=("Times New Roman", 10, "normal"), bg="pink")
Crab_info.place(x=350, y=230)
Crab_sb = Spinbox(from_=0, to=10, width=5)
Crab_sb.place(x=380, y=270)

Coketail = PhotoImage(file="coketaili.png")
Coketail_Label = Label(image=Coketail, borderwidth=0)
Coketail_Label.place(x=50, y=380)
Coketail_info = Label(text="Blue lagoon =$5", font=("Times New Roman", 10, "normal"), bg="pink")
Coketail_info.place(x=40, y=480)
Coketail_sb = Spinbox(from_=0, to=10, width=5)
Coketail_sb.place(x=80, y=520)

Tea = PhotoImage(file="teai.png")
Tea_Label = Label(image=Tea, borderwidth=0)
Tea_Label.place(x=200, y=380)
Tea_info = Label(text="Iced Tea =$3", font=("Times New Roman", 10, "normal"), bg="pink")
Tea_info.place(x=225, y=480)
Tea_sb = Spinbox(from_=0, to=10, width=5)
Tea_sb.place(x=230, y=520)

Juice = PhotoImage(file="juicei.png")
Juice_Label = Label(image=Juice, borderwidth=0)
Juice_Label.place(x=350, y=380)
Juice_info = Label(text="Mango =$5", font=("Times New Roman", 10, "normal"), bg="pink")
Juice_info.place(x=360, y=480)
Juice_sb = Spinbox(from_=0, to=10, width=5)
Juice_sb.place(x=375, y=520)

total_label = Label(text="Total: $0", font=("Times New Roman", 15, "bold"), bg="pink")
total_label.place(x=200, y=600)

calculate_button = Button(text="Calculate Total", command=calculate_total)
calculate_button.place(x=220, y=640)

window.mainloop()