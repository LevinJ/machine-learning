from agent_basic_qtable import  LearningAgent_Basic_Qtable
from agent_basic_qtable import OprationType

from environment import Environment
from simulator import Simulator
import numpy as np
import pandas as pd

class FineTuneQTable():
    def __init__(self):
        self.scores = []
        return
    def train(self, alpha, gamma):
        self.single_run(OprationType.TRAIN, alpha, gamma)
        return
    def test(self, alpha=None, gamma=None):
        self.single_run(OprationType.TEST, alpha, gamma)
        return
    def single_run(self, operationtype, alpha=None, gamma=None):
#         ot = OprationType.TEST
        # Set up environment and agent
        e = Environment()  # create environment (also adds some dummy traffic)
        a = e.create_agent(LearningAgent_Basic_Qtable)  # create agent
        e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
        # NOTE: You can set enforce_deadline=False while debugging to allow longer trials
    
        # Now simulate it
        sim = Simulator(e, update_delay=0.01, display=False)  # create simulator (uses pygame when display=True, if available)
        # NOTE: To speed up simulation, reduce update_delay and/or set display=False
        a.setOperationType(operationtype)
        if not alpha is None:
            a.setLearingRate(alpha)
        if not gamma is None:
            a.setDicountFactor(gamma)
        
        sim.run(n_trials=100) 
        if operationtype == OprationType.TEST:
            self.scores.append((a.final_test_result, a.alpha, a.gamma, a.final_strrepresentation))
        return
    def outputGridSearchResult(self):
        pd.options.display.max_colwidth = 300
        df = pd.DataFrame(self.scores, columns=['score', 'alpha', 'gamma', 'finalstringrepresentation'])
        print df
        maxVals = df['score'].max()
        df.to_csv('grid_search_result.csv')
        print "******Best Parameters: *****\n{}".format(df[df['score'] == maxVals])
        return
    def run(self):
        alphas = np.arange(0, 1.1, 0.1)
        gammas = np.linspace(0, 2,num=10)
        for alpha in alphas:
            for gamma in gammas:
                self.train(alpha, gamma)
                self.test(alpha, gamma)
        self.outputGridSearchResult()
        return 
    


if __name__ == "__main__":   
    obj= FineTuneQTable()
    obj.run()