import tkinter as tk
from client import espace_client
from reservation import espace_reservation
window=tk.Tk()
window.title("l'accueil")
window.geometry("500x500")

frame=tk.Frame(window)
frame.pack(expand=True)
tk.Label(frame, text="Hotel Home :",fg="blue",font=("Arial", 15, "bold")).grid(row=0, column=0, padx=5, pady=5,)
tk.Button(frame, text="Espace Clients", command=espace_client,bg="#5DE2E7").grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Espace Réservations", command=espace_reservation,bg="#5DE2E7").grid(row=1, column=2, padx=5, pady=5)
window.mainloop()
