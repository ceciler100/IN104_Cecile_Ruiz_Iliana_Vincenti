Pour lancer le code : 

Taper dans le terminal: (modifier si besoin les paramètres dans le fichier params.py)

$python3 main.py

To install gym : 

```commandline
$ pip install --user gym
```


 ->main.py: ce qui doit être lancé pour voir l'apprentissage renforcé
 
 ->main_parametres_optimaux.py: sert à déterminer quels sont les coefficients gamma et alpha optimaux dans la formule du Q-learning (pour le tester, le lancer directement depuis le terminal)
 
 ->main_exploration_optimale.py: sert à déterminer quel est le coefficient d'exploration optimal (quand celui-ci ne varie pas au cours de l'exécution de l'algorithme) (pour le tester, le lancer directement depuis le terminal)
 
 ->params.py: contient le nom des différents agents et environnements à appeler et aussi les paramètres de la grille et de l'agent. Ce fichier doit être modifié si on souhaite utiliser un agent ou un environnement différent. On peut aussi y modifier les paramètres de l'expérience: 
 
 ->Dossier "agents": contient tous les codes définissant les agents dans les grilles
 
 ->Dossier "environments": contient les différentes grilles que les agents doivent explorer
