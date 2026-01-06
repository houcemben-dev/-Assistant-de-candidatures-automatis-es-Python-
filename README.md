# 📬 Assistant de candidatures automatisées (Python)

Ce projet est un assistant Python permettant de **préparer, centraliser et suivre des candidatures en alternance**, en s’adaptant aux différents canaux de contact (email, formulaire, LinkedIn).

Il a été développé dans un objectif **concret et métier**, afin d’optimiser et structurer une recherche d’alternance.

---

## 🎯 Objectifs du projet

- Automatiser la préparation des candidatures
- Éviter les doublons de postulation
- Centraliser le suivi des actions
- Gagner du temps tout en gardant le contrôle humain

---

## ⚙️ Fonctionnalités

- Lecture d’un fichier Excel contenant les entreprises
- Filtrage des entreprises à postuler
- Gestion de différents types de contact :
  - 📧 Email (ouverture automatique de Gmail pré-rempli)
  - 📝 Formulaire (ouverture du lien)
  - 🔗 LinkedIn (ouverture du profil)
- Confirmation utilisateur avant chaque action
- Suivi des candidatures dans un fichier `history.csv`
- Prévention des doublons (entreprises déjà traitées ignorées)

---

## 🧠 Choix techniques

- **Python** pour la logique applicative
- **Pandas** pour la manipulation de données Excel
- **CSV** pour la persistance légère des actions
- **Webbrowser** pour l’interaction contrôlée avec le navigateur

Certaines actions (pièces jointes, formulaires) ne sont volontairement pas automatisées pour respecter les limites de sécurité et de conformité du web.


👤 Auteur

Benguermoud Houcem
Formation Développeur en Intelligence Artificielle
