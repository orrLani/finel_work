# finel_work

In the proposed project, heterogeneous teams of autonomous robots will be utilized to achieve a common goal. The robots we used were two kinds: a robotic arm and a turtlebot3. </br>
We use PDDL to plan a set of steps the robots can take to get from their initial state to their goal state, in fewer actions. 


# report

## Installation

### Install the workspace via the installation (step 2 - Environment Setup) in this github:
https://github.com/orrLani/Multi_Agent_System_Based_Help </br>

### install our package in the workspace:
cd ~/catkin_ws/src </br>
git clone https://github.com/orrLani/finel_work </br>


### build the project
cd ~/catkin_ws </br>
catkin_make </br>

### change permissions of py_cogntive_robots.py by set chmod +x at this file.

### run in 4 terminals the folowoing code:
1. roscore
2. roslaunch new_moveit_config multi_gazebo_update.launch 
3. roslaunch new_moveit_config bringup_update.launch
4. rosrun py_moveit py_cogntive_robots.py


## Videos for demonstration:

https://www.youtube.com/watch?v=e8SRlvpJeT0 </br>

https://www.youtube.com/watch?v=OgC8j_9-6Oo </br>

