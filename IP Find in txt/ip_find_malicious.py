import re
import folium
import pygeoip
from collections import Counter

def extract_malicious_ips_from_log_file(log_file):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    malicious_ips = []

    try:
        with open(log_file, 'r') as file:
            for line in file:
                log_parts = line.split('|')
                # Vérifie si le statut HTTP est non réussi (statut commençant par 4 ou 5)
                if log_parts[6].startswith(('4', '5')):
                    ip_matches = re.findall(ip_pattern, log_parts[0])
                    malicious_ips.extend(ip_matches)
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

    return malicious_ips

def create_map_with_malicious_ips(malicious_ips, top_n=10):
    gi = pygeoip.GeoIP('C:\\Users\\arthu\\OneDrive\\Documents\\ESGI\\Python\\IP Find in txt\\GeoLiteCity.dat')
    m = folium.Map(location=[0, 0], zoom_start=2)

    # Compter le nombre d'occurrences de chaque adresse IP malveillante
    ip_counter = Counter(malicious_ips)
    # Sélectionner les adresses IP malveillantes les plus fréquentes
    top_malicious_ips = ip_counter.most_common(top_n)

    # Placer les marqueurs sur la carte pour les adresses IP malveillantes les plus fréquentes
    for ip, count in top_malicious_ips:
        try:
            record = gi.record_by_addr(ip)
            if record:
                latitude = record['latitude']
                longitude = record['longitude']
                popup_text = f"{ip} (Attempts: {count})"
                folium.Marker(location=[latitude, longitude], popup=popup_text, icon=folium.Icon(color='red')).add_to(m)
        except Exception as e:
            print(f"Erreur lors de la recherche des informations de localisation pour l'adresse IP {ip}: {str(e)}")

    m.save('C:\\Users\\arthu\\OneDrive\\Documents\\ESGI\\Python\\IP Find in txt\\map_with_top_malicious_ips.html')


if __name__ == "__main__":
    log_file = input("Entrez le chemin du fichier de log : ")
    malicious_ips = extract_malicious_ips_from_log_file(log_file)

    if malicious_ips:
        print("Adresses IP malveillantes extraites du fichier de log :")
        for ip in malicious_ips:
            print(ip)

        create_map_with_malicious_ips(malicious_ips)
        print("La carte avec les adresses IP malveillantes les plus fréquentes a été créée avec succès.")
    else:
        print("Aucune adresse IP malveillante n'a été trouvée dans le fichier de log.")
