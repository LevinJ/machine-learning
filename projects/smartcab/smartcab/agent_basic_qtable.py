from agent import LearningAgent
from environment import Environment
from simulator import Simulator
from enum import Enum 
import time
import random
from collections import defaultdict
import pickle
import numpy as np
import pandas as pd


class OprationType(Enum):
    TRAIN = 1
    TEST = 2

class LearningAgent_Basic_Qtable(LearningAgent):
    def __init__(self, env):
        LearningAgent.__init__(self, env)
        self.qtable = defaultdict(int)
        self.updateQTable_1_done = False
        self.alpha = 0.1
        self.gamma = 0.5 
        self.epsion = None
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
    def trail_end(self):
        LearningAgent.trail_end(self)
        #For the last action, updateQTable_1 will be executed, but not updateQTable_2, as a result, the Q value that correspons to last action will not be updated for last action
        # if we do not do it here
        if self.operationType != OprationType.TRAIN:
            return
        state,_,_ = self.getCurrentState()
        self.updateQTable_2(state)
        return
    def selectAction_greedy(self, state):
        res = np.random.choice(['useq', 'random'],p=[1-self.epsion, self.epsion])
        if res == 'random':
            return self.getRandomAction()
        
        return self.getQAction(state)
    def selectAction(self, state):
        if self.operationType == OprationType.TRAIN:
            if self.epsion is None:
                return self.getRandomAction()
            else:
                return self.selectAction_greedy(state)
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
    def setLearingRate(self, alpha):
        self.alpha = alpha
        return
    def setEpsion(self, epsion):
        self.epsion = epsion
        return
    def setDicountFactor(self, gamma):
        self.gamma = gamma
        return
    def updateQTable_2(self, next_state):
        if self.operationType != OprationType.TRAIN:
            return
        
        if not self.updateQTable_1_done:
            return
        #At this point, we know the next_state,and can proceed to update Q Table
        alpha = self.alpha
        gamma = self.gamma
        
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
#         self.saveQTabletoCSV()
        return
    def afterSimulatorRun(self):
        LearningAgent.afterSimulatorRun(self)
        if self.operationType == OprationType.TRAIN:
            self.dumpQTable('qtable.pkl')
            return 
        return
    def saveQTabletoCSV(self):
        qdata = []
        for key, value in self.qtable.iteritems():
            qdata.append((key[0],key[1], value))
        df = pd.DataFrame(qdata, columns=['state', 'action', 'qvalue'])
        grouped  = df.groupby('state')
        grouped.aggregate(np.max)
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
    epsion = 0.5
    
    
    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent_Basic_Qtable)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=0.01, display=False)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False
    a.setOperationType(ot)
    a.setEpsion(epsion)
    
    sim.run(n_trials=100)  # run for a specified number of trials
 
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()
