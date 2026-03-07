#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practical for master course 'Reinforcement Learning',
Leiden University, The Netherlands
By Thomas Moerland
"""

import numpy as np
# from Helper import softmax, argmax
from Helper import egreedy
import Environment

# Begin Class BaseAgent ##########################################################################
class BaseAgent:

    def __init__(self, n_states, n_actions, learning_rate, gamma):
        self.n_states       = n_states
        self.n_actions      = n_actions
        self.learning_rate  = learning_rate
        self.gamma          = gamma
        self.Q_sa           = np.zeros((n_states,n_actions))    # per assignment, initialize all Q-values to zero
        
    def select_action(self, s, policy='egreedy' , epsilon=None, temp=None):    # default policy is epsilon-greedy, but one can also select greedy or softmax (Boltzmann) policy
        
        if policy == 'greedy':
            # Modified by me:
            # a = np.random.randint(0,self.n_actions) # Replace this with correct action selection
            a = argmax(self.Q_sa[s]) # Select the best known action to the agent (tie breaking argmax)
        
        elif policy == 'egreedy':
            if epsilon is None:
                raise KeyError("Provide an epsilon")
                
            # Modified by me:
            a = egreedy(self.Q_sa[s], epsilon) # Use the epsilon-greedy policy I implemented in Helper.py
                 
        elif policy == 'softmax':
            if temp is None:
                raise KeyError("Provide a temperature")
                
            # Modified by me:
            a = softmax(self.Q_sa[s], temp) # Selecting softmax        
        else:
            raise KeyError("Unknown policy type")
              
        return a
        
    def update(self):
        raise NotImplementedError('For each agent you need to implement its specific back-up method') # Leave this and overwrite in subclasses in other files


    def evaluate(self,eval_env,n_eval_episodes=30, max_episode_length=100):
        returns  = []  # list to store the reward per episode
        for i in range(n_eval_episodes):
            s    = eval_env.reset()
            R_ep = 0
            for t in range(max_episode_length):
                a = self.select_action(s, 'greedy')
                s_prime, r, done = eval_env.step(a)
                R_ep += r
                if done:
                    break
                else:
                    s = s_prime
            returns.append(R_ep)
        mean_return = np.mean(returns)
        return mean_return
# End Class BaseAgent ##########################################################################

