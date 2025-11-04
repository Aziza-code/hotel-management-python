
def espace_client():
    import tkinter as tk
    from tkinter import messagebox
    import db_hotel  # ton module de base de données

    # Fenêtre principale de l espace client
    root = tk.Tk()
    root.title("Gestion des clients")

    # Champs
    tk.Label(root, text="CNE :").grid(row=1, column=0, padx=5, pady=5)
    entry_cne = tk.Entry(root)
    entry_cne.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Nom :").grid(row=0, column=0, padx=5, pady=5)
    entry_nom = tk.Entry(root)
    entry_nom.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Téléphone :").grid(row=2, column=0, padx=5, pady=5)
    entry_tel = tk.Entry(root)
    entry_tel.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="Email :").grid(row=3, column=0, padx=5, pady=5)
    entry_email = tk.Entry(root)
    entry_email.grid(row=3, column=1, padx=5, pady=5)

    """tk.Label(root, text="Chercher un client :").grid(row=0, column=2, padx=5, pady=5)
    entry_chercher = tk.Entry(root)
    entry_chercher.grid(row=0, column=3, padx=5, pady=5)"""
    tk.Label(root, text=" pour afficher tous les clients exictants :").grid(row=2, column=3, padx=5, pady=5)

    def add_client_to_db():
        # 🔹 Récupérer les valeurs ici
        nom = entry_nom.get()
        telephone = entry_tel.get()
        email = entry_email.get()
        cne = entry_cne.get()

        if nom.strip() == "":
            messagebox.showerror("Erreur", "Le nom est obligatoire !")
            return
        else:
            db_hotel.add_client(cne, nom, telephone, email)
            messagebox.showinfo("Succès", "Client ajouté avec succès !")


    def affichage_des_clients():
        resultat = db_hotel.get_clients()
        messagebox.showinfo("Résultat", resultat)


    # Bouton d’ajout
    btn_add = tk.Button(root, text="Ajouter Client", command=add_client_to_db,bg="green")
    btn_add.grid(row=4, column=0, columnspan=2, pady=10)

    # Bouton pour chercher
    btn_cherch = tk.Button(root, text="click here :", command=affichage_des_clients,bg="blue")
    btn_cherch.grid(row=2, column=4, columnspan=2, pady=10)

    root.mainloop()
