## TRAINING_PYTHON

### Créer le projet puis installer son env virtuel avec le python du pc :
python -m venv .venv 

### Choisir l'interpréteur Python 3.11.6 ('.venv: venv') dans VsCode

### Lancer Training_Python/.venv/Scripts/Activate.ps1

### Si un message d'erreur survient lors du lancement de Training_Python/.venv/Scripts/Activate.ps1 :
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
nom_du_projet/.venv/Scripts/Activate.ps1
Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope Process

### installer les dépendances
-m pip install -r requirements.txt

### Utiliser le python interne au projet pour run le projet : 
.\.venv\Scripts\python.exe test.py


