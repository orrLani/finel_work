# Finel_Work

In the proposed project, heterogeneous teams of autonomous robots will be utilized to achieve a common goal. The robots we used were two kinds: a robotic arm and a turtlebot3. </br>
We use PDDL to plan a set of steps the robots can take to get from their initial state to their goal state, in fewer actions. 


# Report
[report.pdf](https://github.com/orrLani/finel_work/files/9792637/report.pdf)


## Installation

### Install the workspace via the installation (step 2 - Environment Setup) in this github:

https://github.com/ItayGrinberg93/Multi_Agent_System_Based_Help </br>

### Install our files in the workspace:

1. git clone https://github.com/orrLani/finel_work </br>
2. remove the files in Multi_Agent_System_Based_Help/py_moveit/scripts/ </br>
3. copy the files from the cloned git to Multi_Agent_System_Based_Help/py_moveit/scripts/

### change permissions of py_cogntive_robots.py by set chmod +x at this file.

### Run in 4 terminals the folowoing code:
```sh
1. roscore
2. roslaunch new_moveit_config multi_gazebo_update.launch 
3. roslaunch new_moveit_config bringup_update.launch
4. rosrun py_moveit py_cogntive_robots.py
```

## Videos for demonstration:

https://www.youtube.com/watch?v=e8SRlvpJeT0 </br>

https://www.youtube.com/watch?v=OgC8j_9-6Oo </br>

