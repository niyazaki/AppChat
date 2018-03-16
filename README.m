#Auteurs : KASSABEH Zakariya & JABBOUR Hana

Le fichier ChatClient.py permet la communication peer to peer (UDP) entre deux utilisateurs. Il suffit de lancer le logiciel et
de faire /join <IP du serveur> <port d'écoute du serveur>.

Le serveur quant a lui devait acceuillir les utilisateurs et retenir leur adresse ip ainsi que leur port, mais cette fonctionnalité n'a pas été créée par
manque de compétences. Nous sommes concients que cette partie-ci du projet n'est pas réussie.

Une fois que l'on se connecte au serveur, on peut lui demander la liste des utilisateurs connectés afin de pouvoir les contacter
indépendamment du serveur à l'aide de leur adresse IP et leur port d'écoute via la commande /join <IP client> <port d'écoute client>.
