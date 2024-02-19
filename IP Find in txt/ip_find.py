import re
import folium
from folium.plugins import MarkerCluster
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

def create_map_with_ips(ip_addresses):
    gi = pygeoip.GeoIP('C:\\Users\\arthu\\OneDrive\\Documents\\ESGI\\Python\\IP Find in txt\\GeoLiteCity.dat')
    m = folium.Map(location=[0, 0], zoom_start=2)
    marker_cluster = MarkerCluster().add_to(m)

    # Compter le nombre d'occurrences de chaque adresse IP
    ip_counter = Counter(ip_addresses)

    # Sélectionner les 10 adresses IP les plus malveillantes et les 10 adresses IP avec le plus de trafic
    top_malicious_ips = set([ip for ip, _ in ip_counter.most_common(10)])
    top_traffic_ips = set([ip for ip, _ in ip_counter.most_common(10)])

    # Placer les marqueurs sur la carte avec les couleurs appropriées
    for ip, count in ip_counter.items():
        try:
            record = gi.record_by_addr(ip)
            if record:
                latitude = record['latitude']
                longitude = record['longitude']
                popup_text = f"{ip} (Occurrences: {count})"

                # Si l'IP est dans les deux top 10, la marquer en noir
                if ip in top_malicious_ips and ip in top_traffic_ips:
                    color = 'black'
                # Si l'IP est dans le top 10 malveillant, la marquer en rouge
                elif ip in top_malicious_ips:
                    color = 'red'
                # Si l'IP est dans le top 10 de trafic, la marquer en bleu
                elif ip in top_traffic_ips:
                    color = 'blue'
                else:
                    color = 'green'  # Marquer les autres en vert

                folium.Marker(location=[latitude, longitude], popup=popup_text, icon=folium.Icon(color=color)).add_to(marker_cluster)
        except Exception as e:
            print(f"Erreur lors de la recherche des informations de localisation pour l'adresse IP {ip}: {str(e)}")

    m.save('C:\\Users\\arthu\\OneDrive\\Documents\\ESGI\\Python\\IP Find in txt\\map_with_ips.html')

if __name__ == "__main__":
    log_file = input("Entrez le chemin du fichier de log : ")
    ip_addresses = extract_ips_from_log_file(log_file)

    if ip_addresses:
        print("Adresses IP extraites du fichier de log :")
        for ip in ip_addresses:
            print(ip)

        create_map_with_ips(ip_addresses)
        print("La carte avec les adresses IP a été créée avec succès.")
    else:
        print("Aucune adresse IP n'a été trouvée dans le fichier de log.")
