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
#     def train(self, alpha, gamma, epsilon):
#         self.single_run(OprationType.TRAIN, alpha, gamma, epsilon)
#         return
#     def test(self, alpha=None, gamma=None, epsilon=None):
#         self.single_run(OprationType.TEST, alpha, gamma, epsilon)
#         return
    def single_run(self, operationtype, alpha=None, gamma=None, epsilon=None, n_trials=100):
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
        a.setEpsion(epsilon)
        
        sim.run(n_trials=n_trials) 
        if operationtype == OprationType.TEST:
            self.scores.append((a.final_test_result, a.alpha, a.gamma, a.epsion,a.final_strrepresentation))
        return
    def outputGridSearchResult(self):
        pd.options.display.max_colwidth = 300
        df = pd.DataFrame(self.scores, columns=['score', 'alpha', 'gamma', 'epsilon','finalstringrepresentation'])
        print df
        maxVals = df['score'].max()
        df.to_csv('grid_search_result.csv')
        print "******Best Parameters: *****\n{}".format(df[df['score'] == maxVals])
        return
    def run(self):
        alphas = [0.1,  0.5]
        gammas = [0.5,1]
        epsilons = [None, 0.5,0.8]
        for alpha in alphas:
            for gamma in gammas:
                for epsilon in epsilons:
                    self.single_run(OprationType.TRAIN, alpha, gamma, epsilon,n_trials=100)
                    self.single_run(OprationType.TEST, alpha, gamma, epsilon,n_trials=1200)
        self.outputGridSearchResult()
        return 
    


if __name__ == "__main__":   
    obj= FineTuneQTable()
    obj.run()