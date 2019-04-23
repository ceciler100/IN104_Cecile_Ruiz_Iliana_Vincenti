
from params import default_params
from environments.load_env import make_env
from agents.load_agent import make_agent
import matplotlib.pyplot as pyplot
from main import runEpisode

import argparse

#A utiliser avec l'agent004

# This is where the script will start executing
if __name__ == "__main__":

    params = default_params()

    parser = argparse.ArgumentParser()

    parser.add_argument("--render", help="True for display", default=True)

    parser.add_argument("--debug", help="True for display debug info", default=False)

    parser.add_argument("--env", help="get the environment")

    parser.add_argument("--agent", help="get the agent")

    args = parser.parse_args()

    if args.env != None:
        params['env'] = args.env

    if args.agent != None:
        params['agent'] = args.agent

    env_name = params['env']

    agent_name = params['agent']

    environment = make_env(env_name, params)

    params['num_states'] = environment.num_states
    params['num_actions'] = environment.num_actions

    
    render=False
    
    

    # Run episodes
    
    alpha=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    gamma=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    
    for a in alpha:
        for g in gamma:
            for k in range (0,10):
                    agent = make_agent(agent_name, params)
                    listevitesse=[]
                    y_rewards = []
                    nb_episode = []
                    agent.alpha=a
                    agent.gamma=g
                    for episode in range(params['num_training_episodes']):
                        total_reward = runEpisode(environment, agent, 
                                        params['max_action_per_episode'], 
                                        render, args.debug)
                
                        if env_name == 'EnvironmentDiscreteCartpole':
                            agent.update(episode)
                
                        y_rewards.append(total_reward)
                        nb_episode.append(episode)
        
                    #Pour definir les parametres optimaux "a decommenter si on utilise l'agent004
                    #On regarde l'episode a partir duquel la recompense totale est superieure a 60 (on met 60 en argument car la vitesse calculeeavant ne sera pas changee cf codage de fin dans agent004
                    vitesse=agent.fin(60)
                    listevitesse.append(vitesse)
                    environment.close()
                    
            moyenne=0
            for i in listevitesse:
                moyenne+=i
            moyenne=moyenne/len(listevitesse)
            print("Pour alpha=", a, " gamma=", g, " la moyenne de la vitesse est:", moyenne)
            print("___________________________________________________")


#Resultat du programme:
#L'algorihtme semble converger le plus rapidement pour alpha=0.6 et gamma=1 
#





