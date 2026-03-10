# Installing packages (start here)
To create a new virtual environment use the following command
python -m venv .venv/

Activate it using the following command
source .venv/bin/activate.csh

To install the packages necessary for running the code below, run the following command in a fresh virtual environent:
pip install -r requirements.txt

# Dynamic programming
To test how well the Dynamic Programming worked the following scenarios were tested:

Q value iteration at iterations 0, 8 (halfway) and 16 (at convergence) with
goal_location = [7,3]
gamma         = 0.99
threshold     = 70.

Seeing what happens with a new goal location. The parameters used are:
goal_location = [6,2]
gamma         = 0.99
threshold     = 1.0

Seeing what happens with a lower discount factor. The parameters used are:
goal_location = [7,3]
gamma         = 0.5
threshold     = 70.

Seeing what happens with a higher threshold. The parameters used are:
goal_location = [7,3]
gamma         = 0.99
threshold     = 78.

These experiments are all run consecutively using
python DynamicProgramming.py

The plots will also be added to the DynamicProgramming_plots directory that will be generated

The optimal_episode_return is determined using gamma = 0.99 and threshold = 70.

# Exploration
The epsilon-greedy policy is tested for the following parameters:
epsilon            = 0.03, 0.1, 0.3
learning_rate      = 0.1
n_timesteps        = 50001
eval_interval      = 1000
max_episode_length = 100
gamma              = 1.0

The Boltzmann or softmax policy is tested for the following parameters:
temperature        = 0.01, 0.1, 1.0
learning_rate      = 0.1
n_timesteps        = 50001
eval_interval      = 1000
max_episode_length = 100
gamma              = 1.0

Running the exploration part of the assignment and returning the plot used in the
report is achieved with the following command:
python -c "from Experiment import Experiment_class ; run = Experiment_class() ; run.exploration()"

# Back-up: on-policy versus off-policy
The following parameters are used when comparing Q-learning and SARSA
policy         = 'egreedy'
epsilon        = 0.1
learning_rates = [0.03,0.1,0.3]

Running this part of the assignment and returning the plot used in the 
report is achieved with the following command:
python -c "from Experiment import Experiment_class ; run = Experiment_class() ; run.on_off_policy()"

# Back-up: Depth of target

Running this part of the assignment and returning the plot used in the 
report is achieved with the following command:
python -c "from Experiment import Experiment_class ; run = Experiment_class() ; run.back_up_depth()"