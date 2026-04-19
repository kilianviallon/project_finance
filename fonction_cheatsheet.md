# fichier .md

*fichiers permettant de mettre en forme du texte facilement*

---

## Setup initial
```bash
git init                        # initialiser un repo local / crée un dossier caché .git/ qui va contenir tout l'historique de ton projet.
git clone <url>                 # copier un repo existant depuis GitHub
git remote add origin <url>     # relier ton repo local à GitHub
```

---

## Workflow quotidien
```bash
git status                      # voir l'état de tes fichiers, prend une "photo" de l'état actuel de ton dépôt et te montre :
- les fichiers modifiés mais pas encore stagés
- les fichiers stagés (prêts pour le commit)
- les fichiers non trackés (nouveaux fichiers que Git ne connaît pas encore)
git add .                       # stager tous les fichiers modifiés
git add <fichier>               # stager un fichier précis
git commit -m "message clair"   # sauvegarder un snapshot
git push                        # envoyer sur GitHub
git pull                        # récupérer les dernières modifications
```

---

## Branches
```bash
git branch                      # lister les branches
git branch <nom>                # créer une branche
git checkout <nom>              # se déplacer sur une branche
git checkout -b <nom>           # créer + se déplacer en une commande
git merge <nom>                 # fusionner une branche dans la courante
```

---

## Historique & corrections
```bash
git log --oneline               # voir l'historique condensé
git diff                        # voir les modifications non stagées
git restore <fichier>           # annuler les modifs d'un fichier
git reset HEAD~1                # annuler le dernier commit (garde les modifs)
```

---

## Workflow du quotidien (90% des cas)
```bash
git add .  montre quelles modifs (de quels fichiers) tu veux inclure dans ton prochain commit
git commit -m "description de ce que tu as fait"
git push
```

## fonction plus generale :
```bash
touche name : crée un fichier nommé name
rm name : supprime le fichier name
mkdir name : créé un dossier commé name
echo "text" > fichier.txt : crée un fichier avec du texte deja dedans
mv ancien_nom.py nouveau_nom.py : change le nom du fichier
mv fichier.py dossier/        # déplacer un fichier dans un dossier
mv fichier.py dossier/nouveau_nom.py  # déplacer + renommer en même temps
```
## fonction pip:
```bash
pip install  : télécharge et installe des librairies dans ton environnement actif. env doit être activé absolument
pip freeze liste toutes les librairies installées dans ton environnement actif avec leurs versions exactes. permet a qlq qui clone ton repo d'utiliser le mm environnement

```

## utilite et fonction liees au .venv / environnement prive comme anaconda:
```bash
.venv : Le .venv crée un environnement Python isolé pour chaque projet, avec ses propres librairies et versions. Ça évite les conflits entre projets et garantit que tout le monde travaille avec exactement les mêmes dépendances. à placer dans ton  gitignore
# Créer l'environnement (une seule fois par projet)
python -m venv .venv

# L'activer
source .venv/bin/activate       # Mac/Linux

# Installer une lib dedans
pip install numpy

# Sauvegarder les dépendances
pip freeze > requirements.txt : enregistre la liste exacte de toutes les librairies installees dans ton environnement python 
pip install -r requirements.txt : te donne le même environnement que la personne a qui tu as clone le repo github 
# Désactiver
deactivate

#créer l'environnement anaconda (mieux pour les projets solo)

# Créer un environnement pour un projet
conda create --name projet-finance python=3.11

# L'activer
conda activate projet-finance

# Désactiver
conda deactivate

# Voir tous tes environnements
conda env list

# Installer des librairies dedans
pip install numpy pandas matplotlib yfinance

# Sauvegarder les dépendances
pip freeze > requirements.txt

# Supprimer un environnement
conda remove --name projet-finance --all
```
