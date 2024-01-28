import requests
from bs4 import BeautifulSoup
import time
# URL de la page contenant les informations des entreprises
url = "https://www.gifas.fr/member-list"
# Fichier texte dans lequel tu veux enregistrer les liens
fichier_texte = "liens_annuaire.txt"


    #On créé un fichier avec le code html de l'url pour pouvoir faire des verifications
with open("annuaire.html", "r", encoding="utf-8") as file:
    html_content = file.read()
# Analyser le HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Supposons que le montant est dans des balises <div> avec la classe 'page-member__resume__number'
company_truelink = soup.find_all('a', class_='address-list__item result flex items-center')
company_name = soup.find_all('h3', class_="uppon-title uppon-title--medium uppon-title--blue uppercase")




with open(fichier_texte,'w') as fichier:
    i=0
    for balise_a in company_truelink:
        href = balise_a.get('href')
        fichier.write(f"https://www.gifas.fr{href}\n")
        i+=1

# with open(fichier_texte, 'w') as fichier:
#     if len(company_link) > 0:
#         for paragraph in company_link:
#             lien = paragraph.text.strip() 
#             if lien:
#                 fichier.write(lien + '\n')
#                 print(f"Écrit dans le fichier : {lien}")
#     if len(company_name) > 0:
#         for paragraph in company_name:
#             name = paragraph.text.strip()
#             if name:
#                 fichier.write(name + '\n')
#                 print(f"Écrit dans le fichier : {name}")