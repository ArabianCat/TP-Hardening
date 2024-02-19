# Fonction pour extraire les adresses IP de robots louches à partir des logs
def extract_suspicious_ips_from_logs(log_file):
    suspicious_ips = set()  # Utilisation d'un ensemble pour éviter les doublons

    with open(log_file, 'r') as file:
        # Parcourir chaque ligne du fichier de log
        for line in file:
            # Vérifier si la ligne contient à la fois "GoogleBot" et "Uptimerobot"
            if "Googlebot" in line or "uptimerobot.com" in line or "robots.txt" in line or "googlebot.com" in line or "bingbot" in line:
                continue  # Passer à la ligne suivante si la ligne contient les deux
            # Séparation des champs du log en utilisant le caractère '|'
            log_parts = line.strip().split('|')
            # Extraction de l'adresse IP et de l'agent utilisateur
            ip = log_parts[0]
            user_agent = log_parts[9]

            # Vérifier si l'agent utilisateur semble être un robot
            if "bot" in user_agent.lower():
                suspicious_ips.add(ip)
                print(line)

    return suspicious_ips

# Fonction pour exporter les adresses IP de robots louches dans un fichier texte
def export_ips_to_txt(ips, output_file):
    with open(output_file, 'w') as file:
        for ip in ips:
            file.write(ip + '\n')

if __name__ == "__main__":
    # Fichier de log d'entrée
    log_file = "C:\\Users\\arthu\\OneDrive\\Documents\\ESGI\\Python\\IP Flag\\access.log"
    # Fichier de sortie pour les adresses IP de robots louches
    output_file = "C:\\Users\\arthu\\OneDrive\\Documents\\ESGI\\Python\\IP Flag\\suspicious_ips.txt"

    # Extraction des adresses IP de robots louches
    suspicious_ips = extract_suspicious_ips_from_logs(log_file)

    # Export des adresses IP de robots louches dans un fichier texte
    export_ips_to_txt(suspicious_ips, output_file)

    print("Extraction des adresses IP de robots louches terminée. Consultez le fichier", output_file)
