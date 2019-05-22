__author__ = "Florence Carton"

import sys
from agents.AgentRandom import AgentRandom
from agents.Agent001 import Agent001
from agents.Agent002 import Agent002
from agents.Agent003 import Agent003
from agents.Agent004 import Agent004
from agents.Agent005 import Agent005
from agents.Agent007 import Agent007



def make_agent(agent_name, params):

	list_agent = {
	'AgentRandom':AgentRandom(params),
	'Agent001':Agent001(params),
	'Agent002':Agent002(params),
	'Agent003':Agent003(params),
	'Agent004':Agent004(params),
	'Agent005':Agent005(params),
	'Agent007':Agent007(params)
	}

	try:
		agent = list_agent[agent_name]
	except:
		print('agent_name not found')
		sys.exit()

	return agent

