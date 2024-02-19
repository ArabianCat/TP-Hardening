# Fonction pour extraire les adresses IP à partir des logs
def extract_ips_from_logs(log_file):
    ips = set()  # Utilisation d'un ensemble pour éviter les doublons
    with open(log_file, 'r') as file:
        for line in file:
            # Séparation des champs du log en utilisant le caractère '|'
            log_parts = line.strip().split('|')
            # Vérification si la requête est POST et URI est /login
            if log_parts[2] == 'POST' and log_parts[4] == '/login':
                ips.add(log_parts[0])  # Ajout de l'adresse IP
    return ips

# Fonction pour exporter les adresses IP dans un fichier texte
def export_ips_to_txt(ips, output_file):
    with open(output_file, 'w') as file:
        for ip in ips:
            file.write(ip + '\n')

if __name__ == "__main__":
    # Fichier de log d'entrée
    log_file = "C:\\Users\\arthu\\OneDrive\\Documents\\ESGI\\Python\\IP Flag\\access.log"
    # Fichier de sortie pour les adresses IP
    output_file = "C:\\Users\\arthu\\OneDrive\\Documents\\ESGI\\Python\\IP Flag\\ips_login_requests.txt"

    # Extraction des adresses IP
    ips = extract_ips_from_logs(log_file)

    # Export des adresses IP dans un fichier texte
    export_ips_to_txt(ips, output_file)

    print("Extraction des adresses IP terminée. Consultez le fichier", output_file)
