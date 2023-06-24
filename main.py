import requests
from bs4 import BeautifulSoup
import time
import os

# Array für alle URLs der einzelnen Seiten
urls = [
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-1-5000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-5001-10000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-10001-15000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-15001-20000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-20001-25000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-25001-30000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-30001-35000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-35001-40000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-40001-45000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-45001-50000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-50001-55000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-55001-60000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-60001-65000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-65001-70000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-70001-75000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-75001-80000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-80001-85000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-85001-90000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-90001-95000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-95001-100000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-100001-105000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-105001-110000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-110001-115000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-115001-120000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-120001-125000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-125001-130000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-130001-135000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-135001-140000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-140001-145000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-145001-150000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-150001-155000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-155001-160000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-160001-165000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-165001-170000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-170001-175000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-175001-180000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-180001-185000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-185001-190000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-190001-195000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-195001-200000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-200001-205000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-205001-210000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-210001-215000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-215001-220000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-220001-225000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-225001-230000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-230001-235000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-235001-240000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-240001-245000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-245001-250000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-250001-255000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-255001-260000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-260001-265000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-265001-270000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-270001-275000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-275001-280000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-280001-285000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-285001-290000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-290001-295000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-295001-300000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-300001-305000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-305001-310000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-310001-315000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-315001-320000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-320001-325000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-325001-330000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-330001-335000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-335001-340000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-340001-345000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-345001-350000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-350001-355000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-355001-360000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-360001-365000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-365001-370000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-370001-375000',
    'https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/German_frequency_list-375001-380000'
]

# Lösche die Datei, falls sie existiert
if os.path.exists('frequency_dictionary.txt'):
    os.remove('frequency_dictionary.txt')

# Öffne die Datei
with open('frequency_dictionary.txt', 'w') as f:
    # Iteriere über jede URL
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Finde den richtigen Teil der Seite, der die Wortliste enthält
        word_list_section = soup.find('div', {'class': 'mw-parser-output'})

        # Teile den Text in Zeilen auf
        lines = word_list_section.text.split('\n')

        # Filtere Zeilen aus, die keine Wörter repräsentieren (z.B. leere Zeilen)
        lines = [line for line in lines if line]

        # Schreibe jede Zeile in die Datei im gewünschten Format
        for line in lines:
            # Überprüfe, ob die Zeile einen Slash enthält
            if '/' in line:
                # Überspringe die Zeile, wenn sie einen Slash enthält
                continue

            # Teile die Zeile am ersten Leerzeichen auf
            parts = line.split(' ', 1)

            # Überprüfe, ob die Zeile mindestens zwei Teile hat
            if len(parts) >= 2:
                number, word = parts
                # Schreibe das Wort und die Zahl im gewünschten Format
                f.write(f'{word} {number}\n')
            else:
                # Überspringe die Zeile, wenn sie nicht dem erwarteten Format entspricht
                continue

        # Warte kurz, bevor die nächste Anfrage gesendet wird, um den Server nicht zu überlasten
        time.sleep(0.3)