__author__ = "Florence Carton"

import sys
from environments.EnvironmentGrid1D import EnvironmentGrid1D
from environments.EnvironnementGrille2D import EnvironnementGrille2D
from environments.EnvironnementGrille2DObs import EnvironnementGrille2DObs
from environments.Labyrinthe import Labyrinthe



def make_env(env_name, params):

	list_environments = {
	'EnvironmentGrid1D':EnvironmentGrid1D(params),
	'EnvironnementGrille2D':EnvironnementGrille2D(params),
	'EnvironnementGrille2DObs':EnvironnementGrille2DObs(params),
	'Labyrinthe':Labyrinthe(params)
	}

	try:
		env = list_environments[env_name]
	except:
		print('env_name not found')
		sys.exit()

	return env

