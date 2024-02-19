## Partie 1

Nous avons créé un script python (ip_find.py) permettant de créer une map avec html (map_with_ips.html) regroupant les IP avec le plus de traffic et le plus malveillant contenu dans le fichier de log (access.log).
Le code couleur est le suivant :
  - Rouge : Les IPs ditent malveillantes
  - Orange : Les IPs avec le plus de traffic
  - Noir : Les IPs qui sont malveillantes avec le plus de traffic

Deux autres map ont été créer pour mieux différencer les IP qui ont le plus de traffic de ceux qui sont les plus malveillantes (map_with_top_ips_traffic.html & map_with_top_malicious_ips.html)

## Partie 2

Nous avons créé un script python (ip_flag.py) permettant d'exporter dans un ficher (ips_login_requests.txt) toutes les IPs faisant une requête POST sur le /login.
Nous avons également faire un dernier script (ip_flag_robot.py) permettant de voir toutes les IPs utilisant un robot non approprié et exporter cela dans un fichier (suspicious_ips.txt).

## Final

Nous avons aussi fait un fichier TP3.txt regrouppant toutes les informations finals demandés pour le TP.

- Arthur GUILLAUME & Louis JOUHANNET
