__author__ = "Florence Carton"


def default_params():
	""" Default parameters function

	Return : 
		params_dict : dictionnary of parameters
	"""

	params_dict = {

	## Agent parameters
	#'agent': 'Agent001',

	#'agent': 'Agent002',
	
	#'agent': 'Agent003',
	
	#'agent': 'Agent004',
	
	'agent':'Agent005',
	
	## Environment parameters"
	# 'env':'EnvironmentGrid1D',
	'num_cells_grid1D': 100, 
	
	#'env': 'EnvironnementGrille2D',
	#'env': 'EnvironnementGrille2DObs',
	'env': 'Labyrinthe',
	'colonne': 20,
	'ligne': 20,


	## Training parameters
	'num_training_episodes':1000,
	'max_action_per_episode':200

	}
	return params_dict


### unit test to check if param function is ok

if __name__ == '__main__':

    params = default_params()
    print('default_params = ',params)
    print('num_training_episodes = ', params['num_training_episodes'])

    params['new_param']='my_new_param' ## adding a new parameter
    print('params with new parameter',params)
