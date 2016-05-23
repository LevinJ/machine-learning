import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
import time
import pandas as pd

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here
        self.testResults = []
        self.totalPenaty = 0# This indicates the invalid the learning agent made during a trial
        self.totalReward = 0

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required
    def trail_start(self):
        self.totalReward = 0
        self.totalPenaty = 0
        return
    def trail_end(self):
        state = self.env.agent_states[self]
        completed = state['location'] == state['destination']
#         metrics = 0 if completed else -15
        metrics = self.totalReward
#         metrics = metrics + self.totalReward
        self.testResults.append((metrics, completed, self.totalReward,  self.totalPenaty,state['deadline']))
        return
    def beforeSimlatorRun(self, sim):
        self.simulator = sim 
        return
    def outputRunningResult(self):
        df = pd.DataFrame(self.testResults, columns=['metrics', 'completed', 'totalreward', 'penalty','deadline'])
        print df
        print "####Penalty incurred: \n" + str(df[df['penalty'] < 0])
        print "####Not completed: \n" + str(df[df['completed'] == False])
        self.final_completerate = df['completed'].sum()/float(df['completed'].count())
        self.final_test_result = df['metrics'].mean()
        # For those do incur penalty, what's the average
        self.final_penalties = df['penalty'][df['penalty']<0].mean()
        self.final_deadline = df['deadline'].mean()
        print "Test result: Average Discounted Reward,{} Completion Rate,{} Average Penalty,{} Average Deadline,{}".format(str(self.final_test_result), 
                                                                                                    self.final_completerate, self.final_penalties,self.final_deadline)
        return
    def afterSimulatorRun(self):
        self.outputRunningResult()
        return
    def selectAction(self, state):
        listOfActions=[None, 'forward', 'left', 'right']
        return self.next_waypoint
#         return random.choice(listOfActions)
    def beforeAct(self, next_state):
        pass
    def afterAct(self, reward):
        pass
    def getCurrentState(self):
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)
        state = (self.next_waypoint, inputs['light'], inputs['oncoming'], inputs['right'], inputs['left'])
        return state,inputs,deadline
    def update(self, t):
        #allow time for us to see the reward that the agent get due to its last action
        if self.simulator.display:
            time.sleep(2)
            
        # TODO: Update state
        self.state,inputs,deadline = self.getCurrentState()
        # TODO: Select action according to your policy
        self.action = self.selectAction(self.state)
        
        self.env.status_text = "state: {}\naction: {}".format(self.get_state(), self.action)

        print "LearningAgent.update(): deadline = {}, inputs = {}, next_waypoint={},action = {}".format(deadline, inputs, self.next_waypoint,self.action)
        if self.simulator.display:
            self.simulator.render()
            #allow time for us to see the action that the learning agent is about to take
            time.sleep(3)

        # Execute action and get reward
        self.beforeAct(self.state)
        reward = self.env.act(self, self.action)
        self.afterAct(reward)
        self.totalReward = self.totalReward + reward
        if reward < 0:
            self.totalPenaty = self.totalPenaty + reward
        #this action has been used and need to be invalidated
        self.action = "Outdated"

        # TODO: Learn policy based on state, action, reward
        print "LearningAgent.update():reward = {}".format(reward)  # [debug]


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=0.01, display=False)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    sim.run(n_trials=100)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()
