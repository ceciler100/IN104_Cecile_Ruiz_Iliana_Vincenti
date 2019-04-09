__author__ = "Florence Carton"

import sys
from environments.EnvironmentGrid1D import EnvironmentGrid1D
from environments.EnvironnementGrille2D import EnvironnementGrille2D



def make_env(env_name, params):

	list_environments = {
	'EnvironmentGrid1D':EnvironmentGrid1D(params),
	'EnvironnementGrille2D':EnvironnementGrille2D(params)
	}

	try:
		env = list_environments[env_name]
	except:
		print('env_name not found')
		sys.exit()

	return env

