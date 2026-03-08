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

        """
<<<<<<< HEAD
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
=======
        The Q table with elements Q[s,a] has states along the rows and actions along the columns.
        The term gamma * max_a' Q(s',a') represents the maximum value of Q by considering the different actions available
        In order to code this we check the maximum of self.Q_sa along axis 1 (checking along a row). For example
        if we have the following matrix
        [1  2   3]
        [9  1   2]
        [10 12  8]
        and use np.max() along axis 1 we get the following array: [3, 9, 12]. Along axis 0 we would get the following array
        [10, 12, 8] (checking along the columns)
        """
        self.Q_sa[s,a] = np.sum(p_sas * (r_sas + self.gamma * np.max(self.Q_sa,axis=1))) #?

    
def Q_value_iteration(env, gamma=1.0, threshold=0.001, stop="end"):
    """
    Runs Q-value iteration. Returns a converged QValueIterationAgent object

    env         : environment
    gamma       : float. Discount factor
    threshold   : float. 
    stop        : str. When to stop the value iteration. Should be either ['begin','halfway','end']
    """

    "Initialise the QValueIterationAgent class"
    QIagent = QValueIterationAgent(env.n_states, env.n_actions, gamma)
    
>>>>>>> origin/Judith
     # TO DO: IMPLEMENT Q-VALUE ITERATION HERE
        
    # Plot current Q-value estimates & print max error
    # env.render(Q_sa=QIagent.Q_sa,plot_optimal_policy=True,step_pause=0.2)
    # print("Q-value iteration, iteration {}, max error {}".format(i,max_error))
<<<<<<< HEAD
    
    counter = 1
    "As long as the error is above the threshold, keep repeating"
=======

    counter = 1
    "As long as the maximum number of iterations is not reached, keep repeating"
>>>>>>> origin/Judith
    while counter < 100:
        "Reset the error to zero"
        error   = 0 
        
<<<<<<< HEAD
=======
        "If we want to stop the Q-value iteration algorithm, this handles that"
        match stop:
            case "begin":
                if counter == 1:
                    break
            case "halfway":
                if counter == 8: # While testing it takes about 17 iterations to converge with a threshold of 0.001
                    break
            case "end":
                "Let the algorithm converge naturally"
                pass

>>>>>>> origin/Judith
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

<<<<<<< HEAD
        print(f"At iteration {counter} the error is {error}")

        "Update the "
        counter += 1
=======
        print("Q-value iteration, iteration {}, max error {}".format(counter,error))
>>>>>>> origin/Judith

        "Stop the algorithm if the convergence criterion has been reached"
        if error < threshold:
            print(f"Algorithm finished after {counter} iterations by convergence")
            break

<<<<<<< HEAD
=======
        "Increase the iteration counter"
        counter += 1

>>>>>>> origin/Judith

    return QIagent

def experiment():
    gamma     = 0.99 # Considers all future rewards equally if set to 1.0
    threshold = 0.001
    env       = StochasticWindyGridworld(initialize_model=True)
    env.render()
    # stop      = "end"
    stop      = None
    QIagent   = Q_value_iteration(env,gamma,threshold,stop=stop)
    
    "view optimal policy"
<<<<<<< HEAD
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
=======
    done      = False
    s         = env.reset()
>>>>>>> origin/Judith

    "Store the rewards and states in arrays"
    states    = np.array([])
    rewards   = np.array([])

    "Save the figure at the beginning"
    step = 1
    while not done:
        "Select action to take"
        a               = QIagent.select_action(s)

        "Take this action and recieve the next state, the reward and whether the terminal state is reached"
        s_next, r, done = env.step(a)

        "Store the state"
        states          = np.append(states,s)

        "Store the reward"
        rewards         = np.append(rewards,r)

        "Plot the process and include an arrow in the plot that indicates the greedy action in a state"
        env.render(Q_sa=QIagent.Q_sa,plot_optimal_policy=True,step_pause=0.1)

        "Save a figure"
        if step == 1:
            match stop:
                case "begin":
                    env.fig.savefig("step1_VI_at_begining.pdf")
                case "halfway":
                    env.fig.savefig("step1_VI_halfway.pdf")
                case "end":
                    env.fig.savefig("step1_VI_at_end.pdf")
        "Increase the step counter so we only store the figure once"
        step += 1           
        
        "Update the current state"
        s               = s_next
    
    "We can calculate V(s) using the rewards array"
    def value_function(s,gamma=gamma):
        """
        Returns the cumulative reward from a given state s
        assuming that the optimal policy is being followed
        """

        "This function only works for the states that are visited and not for others"
        assert s in states , f"Select a state from one of these:\n{states}"

        "Find the index of the given state"
        index = np.where(states == s)[0][0]

        "Let the user know what this state corresponds to"
        print(f"State {s} corresponds to the location {env._state_to_location(s)}")

        """
        Suppose that after state s follows a number of states until the terminal
        state T is reached. In that case the value function can be determined using
        V(s) = sum_(t = 0)^(T-1) gamma^T r_T)
        """
        
        "Apply this equation"
        return np.sum(rewards[index:]* gamma**np.arange(len(rewards[index:])))
    
    "The number of steps is equal to the number of rewards received"
    number_of_steps          = len(rewards)

    """
    Calculate the mean reward received per timestep. Here gamma is set to one
    to take future rewards into account equally. If gamma is set to <1 then
    determining the mean_reward_per_timestep using the value function would
    not be accurate. In that case, this could instead be determined as follows:
    
    mean_reward_per_timestep = (100 + (number_of_steps - 1) * -1) / number_of_steps

    This is the  case because the agent will definitely find a reward of 100. It will
    get that reward in its final step. All other steps incur a reward of negative 1.
    Sum those two quantities and divide them by two to get the mean reward per timestep.
    This requires knowledge of the rewards gained in the environment and assumes all
    steps other than the one to the terminal state incur the same reward.
    """
    mean_reward_per_timestep = value_function(3,gamma=1) / number_of_steps
    
    print("Number of steps is",number_of_steps)
    print("Mean reward per timestep under optimal policy: {:.5g}".format(mean_reward_per_timestep))
    
if __name__ == '__main__':
    experiment()
<<<<<<< HEAD
    # env       = StochasticWindyGridworld(initialize_model=True)
    # env.render()
    # print(env._state_to_location(5))
    # print(env._location_to_state([2,2]))
    # p_sas, r_sas = env.model(env._location_to_state([0,0]),0)
    # print(p_sas.shape,r_sas.shape)
    # print(p_sas,"\n",r_sas,"\n",p_sas*r_sas)
    # print(env.p_sas[0][2])
    # print(env.r_sas[0][2])
=======
>>>>>>> origin/Judith


