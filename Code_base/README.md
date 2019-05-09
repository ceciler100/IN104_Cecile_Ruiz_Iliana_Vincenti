Pour lancer le code : 

Taper dans le terminal: (modifier si besoin les paramètres dans le fichier params.py)

```commandline
$python3 main.py
```

To install gym : 

```commandline
$ pip install --user gym
```


 ->main.py: ce qui doit être lancé pour voir l'apprentissage renforcé
 
 ->main_parametres_optimaux.py: sert à déterminer quels sont les coefficients gamma et alpha optimaux dans la formule du Q-learning (pour le tester, le lancer directement depuis le terminal)
 
 ->main_exploration_optimale.py: sert à déterminer quel est le coefficient d'exploration optimal (quand celui-ci ne varie pas au cours de l'exécution de l'algorithme) (pour le tester, le lancer directement depuis le terminal)
 
 ->params.py: contient le nom des différents agents et environnements à appeler et aussi les paramètres de la grille et de l'agent. Ce fichier doit être modifié si on souhaite utiliser un agent ou un environnement différent. On peut aussi y modifier les paramètres de l'expérience: nombre de cases dans la grille1D, nombres de lignes et de colonnes dans les grilles 2D, le nombre total d'épisodes et le nombre d'action par épisode  
 
 ->Dossier "agents": contient tous les codes définissant les agents dans les grilles
   - Agent.py: définition de la classe des agents (ceux qui interagissent avec l'environnement)
   - AgentRandom.py: classe de l'agent se déplaçant aléatoirement dans une grille à une dimension
   - Agent001.py: classe de l'agent se déplaçant suivant la méthode Q-learning dans une grille 1D
   - Agent002.py: classe de l'agent se déplaçant suivant la méthode Q-learning dans une grille 2D
   - Agent003.py: classe de l'agent se déplaçant suivant la méthode Monte Carlo dans une grille 2D: l'algorithme compile mais l'agent ne semble pas apprendre au cours des épisodes
   - Agent004.py: classe de l'agent se déplaçant suivant la méthode Q-learning dans une grille 2D. Il est à utiliser avec les main qui permettent de définir les paramètres optimaux
   - Agent005.py: classe de l'agent se déplaçant suivant la méthode Q-learning dans une grille 2D avec les coefficients alpha et gamma optimaux
   - Agent007.py: classe de l'agent se déplaçant suivant la méthode Q-learning dans une grille 2D avec les coefficients alpha et gamma optimaux ainsi qu'un coefficient d'exploration variable au cours des épisodes
   - load_agent.py: dictionnaire répertoriant les différents agents
   
 
 ->Dossier "environments": contient les différentes grilles que les agents doivent explorer
   - Environment.py: définition de la classe des différents environnements
   - EnvironmentGrid1D.py: classe de la grille à une dimension (définir le nombre de cases dans params.py). A utiliser avec AgentRandom et Agent001
   - EnvironnementGrille2D.py: classe de la grille à deux dimensions (définir le nombre de lignes et de colonnes dans params.py). A utiliser avec les agents 002 à 007
   - EnvironnementGrille2DObs.py: classe de la grille à deux dimensions (définir le nombre de lignes et de colonnes dans params.py) avec peu d'obstacles. A utiliser avec les agents 002 à 007
   - Labyrinthe.py: classe de la grille à deux dimensions avec un labyrinthe prédéfini --> ATTENTION: à utiliser avec une grille de taille 25 * 25. A utiliser avec les agents 002 à 007
   - load_env: dictionnaire répertoriant les différentes grilles
 
 
 
 
 
 
