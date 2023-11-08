import tkinter as tk
window = tk.Tk()
window.title("Car parking calculator")


parkingzone_label = tk.Label(window,
                             text="1. Select your parking zone:",
                             font=("Arial", 10))

parkingzone_label.grid(row=0,column=0,
                       pady=10,padx=5,sticky="w")

parkingzone_listbox = tk.Listbox(window,height=4)
parkingzone_listbox.insert(0,'A')
parkingzone_listbox.insert(1,'B')
parkingzone_listbox.insert(2,'C')
parkingzone_listbox.insert(3,'D')

parkingzone_listbox.grid(row=1,column=0,
                         pady=10,columnspan=5)

paymentmode_label = tk.Label(window,
                             text="2. Select your payment mode:",
                             font=("Arial", 10))
paymentmode_label.grid(row=2,column=0,
                       padx=5,pady=10,sticky="w")

paymentmode_radio_frame=tk.Frame(window)
paymentmode_radio_frame.grid(row=3,column=0,
                             pady=10,padx=15,sticky="w")

paymentmode_var = tk.StringVar()

debit_radio = tk.Radiobutton(paymentmode_radio_frame,
                             text="Debit",
                             variable=paymentmode_var,
                             value="Debit")

debit_radio.grid(row=0,column=0,
                 pady=10,padx=15,sticky="w")


cash_radio = tk.Radiobutton(paymentmode_radio_frame,
                             text="Cash",
                             variable=paymentmode_var,
                             value="Cash")
cash_radio.grid(row=0,column=1,
                 pady=10,padx=15,sticky="w")


registration_label = tk.Label(window,
                             text="3. Enter your vehicle registration:",
                             font=("Arial", 10))
registration_label.grid(row=4,column=0,
                       padx=5,pady=10,sticky="w")

vehicle_registration_entry = tk.Entry(window,font=("Arial", 15))
vehicle_registration_entry.grid(row=5,column=0,
                                padx=30,pady=10,
                                columnspan=5)



entrytime_label = tk.Label(window,
                         text="4. Type in your entry time in the textbox below:",
                         font=("Arial", 10))

entrytime_label.grid(row=6,column=0,
                   padx=5,pady=10,sticky="w")


ent_time_entry = tk.Entry(window,
                          font=("Arial", 15))

ent_time_entry.grid(row=7,column=0,
                     padx=30,pady=10,
                     columnspan=5)


vehicletype_label = tk.Label(window,
                             text="5. Select your vehicle type:",
                             font=("Arial", 10))

vehicletype_label.grid(row=8,column=0,
                       padx=5,pady=10,sticky="w")

vehicles_radio_frame=tk.Frame(window)

vehicles_radio_frame.grid(row=9,column=0,
                 pady=10,padx=15,sticky="w")

vehicletype_var = tk.StringVar()

toyota_radio = tk.Radiobutton(vehicles_radio_frame,
                             text="Toyota",
                             variable=vehicletype_var,
                             value="Toyota")

toyota_radio.grid(row=0,column=0,
                 pady=10,padx=15,sticky="w")


isuzu_radio = tk.Radiobutton(vehicles_radio_frame,
                             text="Isuzu",
                             variable=vehicletype_var,
                             value="Isuzu")
isuzu_radio.grid(row=0,column=1,
                 pady=10,padx=15,sticky="w")

subaru_radio = tk.Radiobutton(vehicles_radio_frame,
                             text="Subaru",
                             variable=vehicletype_var,
                             value="Subaru")
subaru_radio.grid(row=0,column=2,
                 pady=10,padx=15,sticky="w")

nissan_radio = tk.Radiobutton(vehicles_radio_frame,
                             text="Nissan",
                             variable=vehicletype_var,
                             value="Nissan")
nissan_radio.grid(row=0,column=3,
                 pady=10,padx=15,sticky="w")

others_radio = tk.Radiobutton(vehicles_radio_frame,
                             text="Others",
                             variable=vehicletype_var,
                             value="Others")
others_radio.grid(row=0,column=4,
                 pady=10,padx=15,sticky="w")


def determine_exit_time():
    from datetime import datetime
    now = datetime.now()

    exit_time = now.strftime("%H:%M")
    return exit_time


def generate_receipt():
    new_window = tk.Tk()
    new_window.title("Receipt")

#getting the selected item from the listbox
    for i in parkingzone_listbox.curselection():
        parking_zone = parkingzone_listbox.get(i)

        
#pushing the selected parking zone to the receipt
        parkingzone_receipt_label = tk.Label(new_window,
                                 text="Parking zone: " + parking_zone,
                                 font=("Arial", 10),
                                 fg="black")

        parkingzone_receipt_label.grid(row=0,column=0,
                           padx=30,
                           sticky="w")

#getting the selected payment mode from the radio buttons and pushing it to the receipt
    payment_mode = paymentmode_var.get()
    paymentmode_receipt_label = tk.Label(new_window,
                                         text="Payment mode: " + payment_mode,
                                         font=("Arial", 10),
                                         fg="black")

    paymentmode_receipt_label.grid(row=1,column=0,
                                   padx=30,pady=0,
                                   sticky="w")

#getting the vehicle reg from entry and pushing it
    vehicle_registration = vehicle_registration_entry.get()

    registration_receipt_label = tk.Label(new_window,
                                          text="Vehicle registration: " + vehicle_registration,
                                         font=("Arial", 10),
                                         fg="black")

    registration_receipt_label.grid(row=2,column=0,
                                    padx=30,pady=0,
                                    sticky="w")

#getting entry time
    entry_time = ent_time_entry.get() 

    entrytime_receipt_label = tk.Label(new_window,
                                       text="Entry time: " + entry_time,
                                       font=("Arial", 10),
                                       fg="black")

    entrytime_receipt_label.grid(row=3,column=0,
                                    padx=30,pady=0,
                                    sticky="w")

#getting vehicle type
    vehicle_type = vehicletype_var.get()

    vehicletype_receipt_label = tk.Label(new_window,
                                       text="Vehicle type: " + vehicle_type,
                                       font=("Arial", 10),
                                       fg="black")

    vehicletype_receipt_label.grid(row=4,column=0,
                                    padx=30,pady=0,
                                    sticky="w")

#pushing the exit time gotten from the function determine_exit_time() 
    exittime_receipt_label = tk.Label(new_window,
                                       text="Exit time: " + determine_exit_time(),
                                       font=("Arial", 10),
                                       fg="black")

    exittime_receipt_label.grid(row=5,column=0,
                                padx=30,pady=0,
                                sticky="w")

#determining the duration and pushing it to the receipt
    from datetime import datetime
    t1=datetime.strptime(entry_time, "%H:%M")
    t2=datetime.strptime(determine_exit_time(), "%H:%M")
    duration = t2 - t1
    duration_in_hours = duration.total_seconds() / (60 * 60)
    duration_in_hours_rounded=round(duration_in_hours,2)
    duration_in_hours_string=str(duration_in_hours_rounded)
    

    duration_receipt_label = tk.Label(new_window,
                                       text="Duration in hours: " + duration_in_hours_string,
                                       font=("Arial", 10),
                                       fg="black")

    duration_receipt_label.grid(row=6,column=0,
                                padx=30,pady=0,
                                sticky="w")

#determing the total hourly charge for different parameters
    if parking_zone == "A":
        if vehicle_type == "Toyota":
            hourly_rate = 200
        elif vehicle_type == "Isuzu":
            hourly_rate = 330
        elif vehicle_type == "Subaru":
            hourly_rate = 125
        elif vehicle_type == "Nissan":
            hourly_rate = 140
        else:
            hourly_rate = 500
    elif parking_zone == "B":
        if vehicle_type == "Toyota":
            hourly_rate = ((10/100) * 200) + 200
        elif vehicle_type == "Isuzu":
            hourly_rate = ((10/100) * 330) + 330
        elif vehicle_type == "Subaru":
            hourly_rate = ((10/100) * 125) + 125
        elif vehicle_type == "Nissan":
            hourly_rate = ((10/100) * 140) + 140
        else:
            hourly_rate = ((10/100) * 500) + 500
    elif parking_zone == "C":
        if vehicle_type == "Toyota":
            hourly_rate = ((15/100) * 200) + 200
        elif vehicle_type == "Isuzu":
            hourly_rate = ((15/100) * 330) + 330
        elif vehicle_type == "Subaru":
            hourly_rate = ((15/100) * 125) + 125
        elif vehicle_type == "Nissan":
            hourly_rate = ((15/100) * 140) + 140
        else:
            hourly_rate = ((10/100) * 500) + 500
    elif parking_zone == "D":
        if vehicle_type == "Toyota":
            hourly_rate = ((20/100) * 200) + 200
        elif vehicle_type == "Isuzu":
            hourly_rate = ((20/100) * 330) + 330
        elif vehicle_type == "Subaru":
            hourly_rate = ((20/100) * 125) + 125
        elif vehicle_type == "Nissan":
            hourly_rate = ((20/100) * 140) + 140
        else:
            hourly_rate = ((20/100) * 500) + 500

    total_hourly_charge = float(hourly_rate)* float(duration_in_hours) 


#determining the time discount
    if duration_in_hours_rounded > 5:
        time_discount = (20/100) * total_hourly_charge
    else:
        time_discount = 0


#determining the payment mode discount
    if payment_mode == "Debit":
        payment_mode_discount = (5/100) * total_hourly_charge
    else:
        payment_mode_discount = 0

#vat equation
    VAT = (16/100) * total_hourly_charge


#final charge rounded and in string format
    final_amount = total_hourly_charge + VAT - time_discount - payment_mode_discount
    final_amount_rounded = round(final_amount, 2)
    final_amount_string = str(final_amount_rounded)


#pushing the final charge to the receipt
    charge_receipt_label = tk.Label(new_window,
                                       text="Total charge: Ksh" + final_amount_string,
                                       font=("Arial", 10),
                                       fg="black")

    charge_receipt_label.grid(row=7,column=0,
                                padx=30,pady=0,
                                sticky="w")

    

                                     

process_label = tk.Label(window,
                         text="6. Click the following button to process your total bill:",
                         font=("Arial", 10))

process_label.grid(row=10,column=0,
                   padx=5,pady=10,sticky="w")



process_charges_button = tk.Button(window,
                                   text="Process charges",
                                   bg="black",
                                   fg="White",
                                   font=("Arial", 15),
                                   command= lambda:[generate_receipt(), determine_exit_time()])
process_charges_button.grid(row=11,column=0,
                            padx=30,pady=10,
                           columnspan=5,)


 


window.mainloop()
