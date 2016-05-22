from agent import LearningAgent
from environment import Environment
from simulator import Simulator
from enum import Enum 
import time
import random
from collections import defaultdict
import pickle
import numpy as np

class OprationType(Enum):
    TRAIN = 1
    TEST = 2

class LearningAgent_Basic_Qtable(LearningAgent):
    def __init__(self, env):
        LearningAgent.__init__(self, env)
        self.qtable = defaultdict(int)
        self.updateQTable_1_done = False
        return
    def dumpQTable(self, filename):
        with open(filename, "w") as clf_outfile:
            pickle.dump(self.qtable, clf_outfile)
        print "Q table: " + str(self.qtable)
        return
    def loadQTable(self,filename):
        with open(filename, "r") as clf_infile:
            self.qtable = pickle.load(clf_infile)
        return
    def setOperationType(self, operationType):
        self.operationType = operationType
        return
    def selectAction(self, state):
        if self.operationType == OprationType.TRAIN:
            listOfActions=[None, 'forward', 'left', 'right']
            return random.choice(listOfActions)
        # we are testing Q table here
        if self.operationType != OprationType.TEST:
            raise Exception("invalid operation is being set" + self.operationType)
        return self.getQAction(state)
    
    def getQAction(self, state):
        tempList = []
        listOfActions=[None, 'forward', 'left', 'right']
        for action in listOfActions:
            tempList.append(self.qtable[(state, action)])
        
        m = max(tempList)
        maxindexes =  [i for i, j in enumerate(tempList) if j == m]
            
        return listOfActions[np.random.choice(maxindexes)]
    
    def getQMax(self, next_state):
        tempList = []
        listOfActions=[None, 'forward', 'left', 'right']
        for action in listOfActions:
            tempList.append(self.qtable[(next_state, action)])
        return max(tempList)
    def updateQTable_2(self, next_state):
        if self.operationType != OprationType.TRAIN:
            return
        
        if not self.updateQTable_1_done:
            return
        #At this point, we know the next_state,and can proceed to update Q Table
        alpha = 0.1
        gamma = 0.5
        
        q_old = self.qtable[(self.current_state, self.current_action)]
        q_max = self.getQMax(next_state)
        q_new = (1- alpha)*q_old + alpha*(self.current_reward + gamma * q_max)
        self.qtable[(self.current_state, self.current_action)] = q_new
#         print "Q table: " + str(self.qtable)
        return
    def updateQTable_1(self, reward):
        if self.operationType != OprationType.TRAIN:
            return
        # At this point, we will not know the next state(since the traffice ight would change, and the other dummy agents would move)
        self.updateQTable_1_done = True
        self.current_state = self.state
        self.current_action = self.action
        self.current_reward = reward
        return
    def beforeSimlatorRun(self, sim):
        LearningAgent.beforeSimlatorRun(self, sim)
        if self.operationType == OprationType.TEST:
            self.loadQTable('qtable.pkl')
        return
    def afterSimulatorRun(self):
        LearningAgent.afterSimulatorRun(self)
        if self.operationType == OprationType.TRAIN:
            self.dumpQTable('qtable.pkl')
            return 
        return
    def beforeAct(self, next_state):
        self.updateQTable_2(next_state)
        return 
    def afterAct(self, reward):
        self.updateQTable_1(reward)
        return
    



def run():
    """Run the agent for a finite number of trials."""
    # Specify the operaton type for Q Table: TRAIN or TEST
    ot = OprationType.TEST
    
    
    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent_Basic_Qtable)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=0.01, display=False)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False
    a.setOperationType(ot)
    
    sim.run(n_trials=100)  # run for a specified number of trials
 
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()
