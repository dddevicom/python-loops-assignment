import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
from datetime import datetime, date
import csv

# User accounts storage
users = {}

stations = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad", "Kolkata"]

# Train data with base availability
trains = {
    101: {"name": "Mumbai - Delhi Express", "available": 8},
    102: {"name": "Chennai - Bangalore Shatabdi", "available": 5},
    103: {"name": "Kolkata - Hyderabad Duronto", "available": 3},
}

berth_options = ['Lower', 'Middle', 'Upper', 'Side Lower', 'Side Upper']

# Tickets storage: PNR -> ticket info for each passenger
booked_tickets = {}

# Availability per train per journey date
availability = {}
for tid in trains:
    availability[tid] = {}

today_str = date.today().strftime("%d-%m-%Y")
for tid in trains:
    availability[tid][today_str] = trains[tid]["available"]

def generate_unique_pnr():
    while True:
        pnr = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if pnr not in booked_tickets:
            return pnr

def save_ticket_to_csv(pnr, ticket_info):
    # Append passenger ticket info to CSV file
    header = ['PNR', 'Username', 'TrainID', 'TrainName', 'Date', 'From', 'To',
              'PassengerName', 'Age', 'Gender', 'Berth', 'Status']
    file_exists = False
    try:
        with open('railway_bookings.csv', 'r', newline='') as f:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open('railway_bookings.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)
        p = ticket_info['passenger']
        writer.writerow([pnr, ticket_info['username'], ticket_info['train_id'], ticket_info['train_name'],
                         ticket_info['date'], ticket_info['from'], ticket_info['to'],
                         p['name'], p['age'], p['sex'], p['berth'], ticket_info['status']])

def clear_win():
    for widget in win.winfo_children():
        widget.destroy()

def show_login():
    clear_win()
    tk.Label(win, text="Login", font=("Arial",14)).pack(pady=10)
    user_e = tk.Entry(win)
    user_e.pack(pady=5)
    user_e.insert(0,"Username")
    pass_e = tk.Entry(win,show="*")
    pass_e.pack(pady=5)
    pass_e.insert(0,"Password")
    def try_login():
        u,p = user_e.get(),pass_e.get()
        if users.get(u) == p:
            messagebox.showinfo("Login","Login successful!")
            show_main(u)
        else:
            messagebox.showerror("Login","Invalid username or password.")
    tk.Button(win,text="Login",command=try_login).pack(pady=5)
    tk.Button(win,text="Create Account",command=show_signup).pack(pady=5)

def show_signup():
    clear_win()
    tk.Label(win, text="Create Account", font=("Arial",14)).pack(pady=10)
    user_e = tk.Entry(win)
    user_e.pack(pady=5)
    pass_e = tk.Entry(win, show="*")
    pass_e.pack(pady=5)
    def create():
        u, p = user_e.get(), pass_e.get()
        if u in users:
            messagebox.showerror("Signup","Username already exists.")
            return
        if not u or not p:
            messagebox.showerror("Signup","Username and password cannot be empty.")
            return
        users[u] = p
        messagebox.showinfo("Signup","Account created successfully! Please login.")
        show_login()
    tk.Button(win, text="Sign Up", command=create).pack(pady=5)
    tk.Button(win, text="Back to Login", command=show_login).pack(pady=5)

def show_main(username):
    clear_win()
    tk.Label(win, text=f"Welcome, {username}!", font=("Arial",16)).pack(pady=15)
    tk.Button(win, text="Book Tickets", command=lambda: show_book(username), width=20).pack(pady=10)
    tk.Button(win, text="Check PNR Status", command=show_pnr, width=20).pack(pady=10)
    tk.Button(win, text="Logout", command=show_login, width=20).pack(pady=10)

def validate_date(ddmmyyyy):
    try:
        dt = datetime.strptime(ddmmyyyy, "%d-%m-%Y")
        return dt.date()
    except ValueError:
        return None

def show_book(username):
    clear_win()
    tk.Label(win, text="Journey Details", font=("Arial",14)).pack(pady=10)

    tk.Label(win, text="From Station").pack()
    from_station = ttk.Combobox(win, values=stations)
    from_station.current(0)
    from_station.pack(pady=5)

    tk.Label(win, text="To Station").pack()
    to_station = ttk.Combobox(win, values=stations)
    to_station.current(1)
    to_station.pack(pady=5)

    tk.Label(win, text="Journey Date (DD-MM-YYYY)").pack()
    date_e = tk.Entry(win)
    date_e.insert(0, today_str)
    date_e.pack(pady=5)

    tk.Label(win, text="Select Train").pack()
    train_c = ttk.Combobox(win, values=[f"{tid}: {tinfo['name']}" for tid, tinfo in trains.items()])
    train_c.current(0)
    train_c.pack(pady=5)

    available_label = tk.Label(win, text="Available Tickets: ")
    available_label.pack(pady=5)

    def update_availability(*args):
        selected_train = train_c.get().split(":")[0]
        selected_date_str = date_e.get()
        dt = validate_date(selected_date_str)
        if dt and selected_train.isdigit():
            train_id = int(selected_train)
            date_str = dt.strftime("%d-%m-%Y")
            av = availability.get(train_id, {}).get(date_str, trains[train_id]["available"])
            available_label.config(text=f"Available Tickets for {date_str}: {av}")
        else:
            available_label.config(text="Available Tickets: Please enter valid date & select train")

    train_c.bind("<<ComboboxSelected>>", update_availability)
    date_e.bind("<FocusOut>", lambda e: update_availability())
    date_e.bind("<Return>", lambda e: update_availability())

    tk.Label(win, text="Number of Tickets (max 6):").pack()
    num_tix = tk.Entry(win)
    num_tix.pack(pady=5)

    def go_next():
        qty_str = num_tix.get()
        journey_str = date_e.get()
        dt = validate_date(journey_str)
        if not dt:
            messagebox.showerror("Date Error", "Please enter journey date in DD-MM-YYYY format.")
            return
        try:
            qty = int(qty_str)
            if qty < 1 or qty > 6:
                raise ValueError()
        except:
            messagebox.showerror("Quantity Error", "Number of tickets must be between 1 and 6.")
            return
        f_station = from_station.get()
        t_station = to_station.get()
        if f_station == t_station:
            messagebox.showerror("Station Error", "From and To stations cannot be the same.")
            return
        train_id = int(train_c.get().split(":")[0])
        date_str = dt.strftime("%d-%m-%Y")
        avail = availability.get(train_id, {}).get(date_str, trains[train_id]["available"])
        show_passenger_fields(username, dt, f_station, t_station, train_id,
                              trains[train_id]["name"], qty, avail, date_str)

    tk.Button(win, text="Next", command=go_next, width=20).pack(pady=10)

    update_availability()

def show_passenger_fields(username, journey, from_s, to_s, train_id, train_name, qty, avail, date_str):
    clear_win()
    tk.Label(win, text=f"Passenger Details for {train_name}", font=("Arial",14)).pack(pady=10)
    tk.Label(win, text=f"Journey Date: {date_str}").pack()
    tk.Label(win, text=f"Available Tickets: {avail}").pack(pady=5)

    entries = []
    for i in range(qty):
        frame = tk.Frame(win)
        frame.pack(pady=3)
        tk.Label(frame, text=f"Passenger {i+1}").grid(row=0, columnspan=2, pady=2)
        name = tk.Entry(frame, width=20)
        age = tk.Entry(frame, width=10)
        sex = ttk.Combobox(frame, values=['M', 'F'], width=5)
        berth = ttk.Combobox(frame, values=berth_options, width=10)

        tk.Label(frame, text="Name").grid(row=1, column=0)
        tk.Label(frame, text="Age").grid(row=1, column=1)
        tk.Label(frame, text="Gender").grid(row=3, column=0)
        tk.Label(frame, text="Berth").grid(row=3, column=1)

        name.grid(row=2, column=0, padx=4)
        age.grid(row=2, column=1, padx=4)
        sex.grid(row=4, column=0, padx=4)
        berth.grid(row=4, column=1, padx=4)

        sex.set('M')
        berth.set('Lower')

        entries.append((name, age, sex, berth))

    def book_tix():
        passengers = []
        pnrs = []
        for e in entries:
            n, a, s, b = e[0].get().strip(), e[1].get().strip(), e[2].get().strip(), e[3].get().strip()
            if n == "" or a == "" or s == "" or b == "":
                messagebox.showerror("Input Error", "Please fill all passenger details.")
                return
            try:
                age_val = int(a)
                if age_val < 0:
                    raise ValueError()
            except:
                messagebox.showerror("Input Error", "Please enter valid ages.")
                return
            passengers.append({'name': n, 'age': age_val, 'sex': s, 'berth': b})

        num_confirm = min(qty, avail)
        num_wait = max(0, qty - avail)
        ticket_status = ['Confirmed'] * num_confirm + ['Waiting List'] * num_wait

        for i in range(qty):
            pnr = generate_unique_pnr()
            ticket_info = {
                'username': username,
                'train_id': train_id,
                'train_name': train_name,
                'date': date_str,
                'from': from_s,
                'to': to_s,
                'passenger': passengers[i],
                'status': ticket_status[i]
            }
            booked_tickets[pnr] = ticket_info
            save_ticket_to_csv(pnr, ticket_info)
            pnrs.append(pnr)

        # Decrement availability only by confirmed tickets count
        if date_str in availability[train_id]:
            availability[train_id][date_str] -= num_confirm
        else:
            availability[train_id][date_str] = trains[train_id]["available"] - num_confirm

        messagebox.showinfo("Booking Confirmed",
                            f"Bookings done!\nPNRs:\n" + "\n".join(pnrs) +
                            f"\nTicket Statuses: {', '.join(ticket_status)}")
        show_main(username)

    tk.Button(win, text="Book Now", command=book_tix, width=20).pack(pady=15)

def show_pnr():
    clear_win()
    tk.Label(win, text="Check PNR Status", font=("Arial",14)).pack(pady=15)
    pnr_e = tk.Entry(win, width=20)
    pnr_e.pack(pady=10)

    def check():
        val = pnr_e.get().strip().upper()
        t = booked_tickets.get(val)
        if t:
            p = t['passenger']
            msg = (f"PNR: {val}\nTrain: {t['train_name']}\nJourney Date: {t['date']}\nRoute: {t['from']} → {t['to']}\n\n"
                   f"Passenger: {p['name']}, Age: {p['age']}, Gender: {p['sex']}, Berth: {p['berth']}\n"
                   f"Ticket Status: {t['status']}")
            messagebox.showinfo("PNR Details", msg)
        else:
            messagebox.showerror("PNR Error", "No booking found with this PNR.")

    tk.Button(win, text="Check Status", command=check, width=20).pack(pady=10)
    tk.Button(win, text="Back to Menu", command=show_login, width=20).pack(pady=5)

# Initialize and start the app
win = tk.Tk()
win.title("Railway Ticket Reservation System")
win.geometry("450x700")
show_login()
win.mainloop()
