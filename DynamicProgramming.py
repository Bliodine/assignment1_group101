#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practical for course 'Reinforcement Learning',
Leiden University, The Netherlands
By Thomas Moerland
"""

import numpy as np
from Environment import StochasticWindyGridworld
from Helper import argmax

class QValueIterationAgent:
    ''' Class to store the Q-value iteration solution, perform updates, and select the greedy action '''

    def __init__(self, n_states, n_actions, gamma, threshold=0.01):
        self.n_states  = n_states
        self.n_actions = n_actions
        self.gamma     = gamma
        self.Q_sa      = np.zeros((n_states,n_actions))
        
    def select_action(self,s):
        ''' Returns the greedy best action in state s ''' 

        "Use the provided argmax function to select the action corresponding to the maximum of Q(s,a)"
        return argmax(self.Q_sa[s])
        
        
    def update(self,s,a,p_sas,r_sas):
        ''' Function updates Q(s,a) using p_sas and r_sas '''
        # TO DO: Add own code
        """
        We can retrieve p_sas and r_sas from the model() method in StochasticWindyGridworld
        For this we need to do something like env = StochasticWindyGridworld(initialize_model=True)
        Only then are p_sas and r_sas accessible through

        p_sas, r_sas = env.model(s,a)

        This function takes p_sas and r_sas as inputs however. Perhaps it can be called in Q_value_iteration
        Then we just define the update to Qsa here and worry about p_sas and r_sas later

        Equation 1 is a sum over all next states, therefore we need and array of states, array of p_sas and an array of r_sas

        If that's the case then
        self.Q_sa[s,a] = np.sum(p_sas * (r_sas + self.gamma * self.select_action(s)))
        I think
        """
        # self.Q_sa[s,a] += np.sum(p_sas * (r_sas + self.gamma * max(self.Q_sa[s]))) #this will set all values to -6...
        "Find the maximum Q-value for each state and store this in an array"
        # max_Q = np.array([])
        # s_next = argmax(p_sas) #find the next state we'll end up in
        # print()
        # for s_i in range(self.n_states):
        #     max_Q = np.append(max_Q,max(self.Q_sa[s_i]))
        # self.Q_sa[s,a] = np.dot(p_sas, (p_sas + self.gamma * max_Q))
        # print("At this update the following information is used:")
        # print(f"p_sas \t= {p_sas}")
        # print(f"r_sas \t= {r_sas}")
        # print(f"s \t= {s}")
        # print(f"a \t= {a}")
        # self.Q_sa[s,a] += 1

        # self.Q_sa[s,a] = np.dot(p_sas, (p_sas + self.gamma * max(self.Q_sa[s_next])))
        # print(f"Q[s,a] \t= {self.Q_sa[s,a]}")
        # "Print the maximum absolute error?"

        self.Q_sa[s,a] = np.sum(p_sas * (r_sas + self.gamma * np.max(self.Q_sa,axis=1))) #?

        # pass
    
    
def Q_value_iteration(env, gamma=1.0, threshold=0.001):
    ''' Runs Q-value iteration. Returns a converged QValueIterationAgent object '''
    
    QIagent = QValueIterationAgent(env.n_states, env.n_actions, gamma)
    

    # QIagent.Q_sa[4,0] = 10
     # TO DO: IMPLEMENT Q-VALUE ITERATION HERE
        
    # Plot current Q-value estimates & print max error
    # env.render(Q_sa=QIagent.Q_sa,plot_optimal_policy=True,step_pause=0.2)
    # print("Q-value iteration, iteration {}, max error {}".format(i,max_error))
    
    counter = 1
    "As long as the error is above the threshold, keep repeating"
    while counter < 100:
        "Reset the error to zero"
        error   = 0 
        
        "For all states"
        for s in range(env.n_states):
            "For all actions"
            for a in range(env.n_actions):
                "Store current estimate"
                x = QIagent.Q_sa[s,a]

                "Get p_sas and r_sas"
                p_sas, r_sas = env.model(s,a)
    
                "Update the Q-table"
                QIagent.update(s,a,p_sas,r_sas)

                "Update the error"
                error = np.max([error,np.abs(x - QIagent.Q_sa[s,a])])

        print(f"At iteration {counter} the error is {error}")

        "Update the "
        counter += 1

        "Stop the algorithm if the convergence criterion has been reached"
        if error < threshold:
            print(f"Algorithm finished after {counter} iterations by convergence")
            break


    return QIagent

def experiment():
    gamma     = 0.99 # Considers all future rewards equally if set to 1.0
    threshold = 0.001
    env       = StochasticWindyGridworld(initialize_model=True)
    env.render()
    QIagent   = Q_value_iteration(env,gamma,threshold)
    
    "view optimal policy"
    done = False
    s    = env.reset()
    while not done:
        "Select action to take"
        a               = QIagent.select_action(s)

        "Take this action and recieve the next state, the reward and whether the terminal state is reached"
        s_next, r, done = env.step(a)

        "Plot the process and include an arrow in the plot that indicates the greedy action in a state"
        env.render(Q_sa=QIagent.Q_sa,plot_optimal_policy=True,step_pause=1.5)

        "Update the current state"
        s               = s_next

    # TO DO: Compute mean reward per timestep under the optimal policy
    # print("Mean reward per timestep under optimal policy: {}".format(mean_reward_per_timestep))
    
if __name__ == '__main__':
    experiment()
    # env       = StochasticWindyGridworld(initialize_model=True)
    # env.render()
    # print(env._state_to_location(5))
    # print(env._location_to_state([2,2]))
    # p_sas, r_sas = env.model(env._location_to_state([0,0]),0)
    # print(p_sas.shape,r_sas.shape)
    # print(p_sas,"\n",r_sas,"\n",p_sas*r_sas)
    # print(env.p_sas[0][2])
    # print(env.r_sas[0][2])


