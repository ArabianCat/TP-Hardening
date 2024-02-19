import re
import folium
import pygeoip
from collections import Counter

def extract_ips_from_log_file(log_file):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ips = []

    try:
        with open(log_file, 'r') as file:
            for line in file:
                log_parts = line.split('|')
                ip_matches = re.findall(ip_pattern, log_parts[0])
                ips.extend(ip_matches)
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

    return ips

def create_map_with_ip_traffic(ip_addresses, top_n=11):
    gi = pygeoip.GeoIP('C:\\Users\\arthu\\OneDrive\\Documents\\ESGI\\Python\\IP Find in txt\\GeoLiteCity.dat')
    m = folium.Map(location=[0, 0], zoom_start=2)

    # Compter le nombre d'occurrences de chaque adresse IP
    ip_counter = Counter(ip_addresses)
    # Sélectionner les adresses IP les plus fréquentes
    top_ips = ip_counter.most_common(top_n)

    # Placer les marqueurs sur la carte pour les adresses IP les plus fréquentes
    for ip, count in top_ips:
        try:
            record = gi.record_by_addr(ip)
            if record:
                latitude = record['latitude']
                longitude = record['longitude']
                popup_text = f"{ip} (Traffic: {count})"
                folium.Marker(location=[latitude, longitude], popup=popup_text, icon=folium.Icon(color='orange')).add_to(m)
        except Exception as e:
            print(f"Erreur lors de la recherche des informations de localisation pour l'adresse IP {ip}: {str(e)}")

    m.save('C:\\Users\\arthu\\OneDrive\\Documents\\ESGI\\Python\\IP Find in txt\\map_with_top_ip_traffic.html')

if __name__ == "__main__":
    log_file = input("Entrez le chemin du fichier de log : ")
    ip_addresses = extract_ips_from_log_file(log_file)

    if ip_addresses:
        print("Adresses IP extraites du fichier de log :")
        for ip in ip_addresses:
            print(ip)

        create_map_with_ip_traffic(ip_addresses)
        print("La carte avec les adresses IP les plus fréquentes a été créée avec succès.")
    else:
        print("Aucune adresse IP n'a été trouvée dans le fichier de log.")
