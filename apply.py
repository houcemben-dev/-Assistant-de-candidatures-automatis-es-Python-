# ==============================
# IMPORTS DES LIBRAIRIES
# ==============================

import pandas as pd                 # Manipulation de données (Excel)
from gmail import ouvrir_gmail      # Fonction perso pour ouvrir Gmail pré-rempli
import webbrowser                   # Ouvrir des liens dans le navigateur
from datetime import datetime       # Gestion des dates
import csv                          # Lecture / écriture de fichiers CSV
import os                           # Interaction avec le système de fichiers


# ==============================
# CHARGEMENT DES ENTREPRISES DÉJÀ TRAITÉES
# ==============================

# Ensemble pour stocker les entreprises déjà traitées (évite les doublons)
deja_traites = set()

# Si un historique existe, on le lit pour ne pas repostuler
if os.path.isfile("history.csv"):
    with open("history.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # On récupère la première colonne (nom de l’entreprise),
            # peu importe son nom exact
            deja_traites.add(row[list(row.keys())[0]])


# ==============================
# LECTURE DU FICHIER EXCEL
# ==============================

# Lecture du fichier contenant les entreprises
df = pd.read_excel("contact.xlsx")

# On filtre uniquement celles à postuler
a_postuler = df[df["Statut"] == "a_postuler"]


# ==============================
# PARAMÈTRES GÉNÉRAUX
# ==============================

objet = "Candidature alternance – Développement Python / IA"


# ==============================
# FONCTION D’HISTORIQUE
# ==============================

def enregistrer_historique(entreprise, type_contact, action):
    """
    Enregistre l'action effectuée dans un fichier history.csv
    Permet de suivre les candidatures et d’éviter les doublons
    """
    fichier = "history.csv"
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    fichier_existe = os.path.isfile(fichier)

    with open(fichier, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # Si le fichier n'existe pas, on écrit l'en-tête
        if not fichier_existe:
            writer.writerow(["entreprise", "date", "type", "action"])

        # Ajout d'une nouvelle ligne d'historique
        writer.writerow([entreprise, date, type_contact, action])


# ==============================
# BOUCLE PRINCIPALE
# ==============================

for index, ligne in a_postuler.iterrows():
    entreprise = ligne["Entreprise"]
    type_contact = str(ligne["Type"]).strip().lower()  # Normalisation des données
    lien = ligne["Lien"]

    # Si l'entreprise a déjà été traitée, on passe à la suivante
    if entreprise in deja_traites:
        print(f"⏭️ {entreprise} déjà traitée, on passe.")
        continue


    # ==============================
    # MESSAGE DE CANDIDATURE
    # ==============================

    message = f"""
Bonjour,

Actuellement en formation Développeur en Intelligence Artificielle, je me spécialise progressivement en Python et data, avec une forte approche pratique (manipulation de données, automatisation, logique applicative).

Je suis aujourd’hui à la recherche d’une alternance afin de consolider mes compétences techniques en environnement professionnel et de contribuer concrètement à des projets réels.

Curieux, motivé et en forte montée en compétences, je serais ravi d’échanger avec {entreprise} pour étudier une éventuelle collaboration.

Cordialement,
Benguermoud Houcem
"""


    print("================================")
    print("Entreprise :", entreprise)
    print("Contact :", lien)


    # ==============================
    # GESTION DES DIFFÉRENTS TYPES DE CONTACT
    # ==============================

    # CAS EMAIL
    if type_contact in ["email", "mail"]:
        print("Action : Envoyer un email")

        if "@" in lien:
            choix = input("Ouvrir Gmail pour cette entreprise ? (o/n) : ")
            if choix.lower() == "o":
                ouvrir_gmail(lien, objet, message)
                enregistrer_historique(entreprise, "email", "preparé")
        else:
            print("⚠️ Adresse email invalide :", lien)


    # CAS FORMULAIRE
    elif type_contact == "formulaire":
        print("Action : Ouvrir le formulaire")
        choix = input("Ouvrir le formulaire ? (o/n) : ")
        if choix.lower() == "o":
            webbrowser.open(lien)
            enregistrer_historique(entreprise, "formulaire", "ouvert")


    # CAS LINKEDIN
    elif type_contact == "linkedin":
        print("Action : Ouvrir LinkedIn")
        choix = input("Ouvrir LinkedIn ? (o/n) : ")
        if choix.lower() == "o":
            webbrowser.open(lien)
            enregistrer_historique(entreprise, "linkedin", "ouvert")


    # CAS INCONNU
    else:
        print("Type de contact inconnu :", type_contact)