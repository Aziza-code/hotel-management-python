
def espace_reservation():
    import tkinter as tk
    from tkinter import ttk,messagebox
    import db_hotel  # ton module de base de données

    # Fenêtre principale de l espace reservation
    root1 = tk.Tk()
    root1.title("Gestion des reservations")
    tk.Label(root1, text="la chambre :").grid(row=0, column=0, padx=5, pady=5)

    combo_rooms=ttk.Combobox(root1)
    combo_rooms.grid(row=0, column=1, padx=5, pady=5)
    def load_free_rooms(event=None):
        rooms = db_hotel.get_free_rooms()
        # On met dans la Combobox le numéro de chambre (tu peux ajouter le prix si tu veux)
        combo_rooms['values'] = [f"Chambre {r[1]}  DH" for r in rooms]

    # Bind sur le clic pour afficher la liste automatiquement
    combo_rooms.bind("<Button-1>", load_free_rooms)
    #ajoute de client label et l'entry
    tk.Label(root1, text="CNE de client :").grid(row=1, column=0, padx=5, pady=5)
    entry_client=tk.Entry(root1)
    entry_client.grid(row=1, column=1, padx=5, pady=5)
    #la date d entree label et l'entry
    tk.Label(root1, text="la date d'entrer:").grid(row=2, column=0, padx=5, pady=5)
    entry_date_ent=tk.Entry(root1)
    entry_date_ent.grid(row=2, column=1, padx=5, pady=5)
    #date de sortie label et entry
    tk.Label(root1, text="la date de sortie:").grid(row=3, column=0, padx=5, pady=5)
    entry_date_sort=tk.Entry(root1)
    entry_date_sort.grid(row=3, column=1, padx=5, pady=5)
    #ajouter la reservation
    def ajout_reservation():
        cne=entry_client.get()
        entrer=entry_date_ent.get()
        sortie=entry_date_sort.get()
        num_room=combo_rooms.get()
        if cne.strip() == "" or entrer.strip()=="" or sortie.strip()=="" or num_room=="":
            messagebox.showerror("Erreur", "tout les champs sont obligatoires !")
            return
        else:
            db_hotel.add_booking(num_room,cne, entrer,sortie)
            messagebox.showinfo("Succès", "reservation ajouté avec succès !")


    btn=tk.Button(root1,text="ajouter la reservation",command=ajout_reservation)
    btn.grid(row=4, column=1, padx=5, pady=5)

    root1.mainloop()
