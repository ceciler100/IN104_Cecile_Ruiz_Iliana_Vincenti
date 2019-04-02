__author__ = "Florence Carton"

import sys
from agents.AgentRandom import AgentRandom
from agents.Agent001 import Agent001



def make_agent(agent_name, params):

	list_agent = {
	'AgentRandom':AgentRandom(params),
	'Agent001':Agent001(params)
	}

	try:
		agent = list_agent[agent_name]
	except:
		print('agent_name not found')
		sys.exit()

	return agent

