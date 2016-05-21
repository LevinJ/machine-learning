import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
import time

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required
    def setSimulator(self, sim):
        self.simulator = sim
        return
    def update(self, t):
        time.sleep(2)
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)
        self.state = (self.next_waypoint, inputs['light'], inputs['oncoming'], inputs['right'], inputs['left'])

        # TODO: Update state
        
        # TODO: Select action according to your policy
        listOfActions=[None, 'forward', 'left', 'right']
#         action = random.choice(listOfActions)
        action = self.next_waypoint
        self.action = action
        #render initial status
        
        self.env.status_text = "state: {}\naction: {}".format(self.get_state(), action)

        print "LearningAgent.update(): deadline = {}, inputs = {}, next_waypoint={},action = {}".format(deadline, inputs, self.next_waypoint,action)
        if self.simulator.display:
            self.simulator.render()
        time.sleep(3)#allow time for us to see the action the learning agent is about to take
#         action = self.next_waypoint

        # Execute action and get reward
        reward = self.env.act(self, action)
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
    sim = Simulator(e, update_delay=0.01, display=True)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False
    a.setSimulator(sim)

    sim.run(n_trials=100)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()
