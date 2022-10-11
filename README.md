# finel_work

# How to run the code

## install ros melodic -
  http://wiki.ros.org/melodic/Installation/Ubuntu
 
##  install TurtleBot3 Simulation
sudo apt-get install ros-melodic-turtlebot3-*

## install MoveIt:
 sudo apt install ros-melodic-catkin python-catkin-tools
 sudo apt install ros-melodic-moveit
 
## run the folowing code in 4 terminals:

catkin_make

At the first terminal run:
cd ~/catkin_ws
source devel/setup.bash
export TURTLEBOT3_MODEL=burger 
roscore 

At the secound terminal run:
cd ~/catkin_ws
source devel/setup.bash
export TURTLEBOT3_MODEL=burger 
roslaunch new_moveit_config multi_gazebo_update.launch 

At the third terminal run:
cd ~/catkin_ws
source devel/setup.bash
export TURTLEBOT3_MODEL=burger 
roslaunch new_moveit_config bringup_update.launch

At the last terminal run:
cd ~/catkin_ws
source devel/setup.bash
cd src/Multi_Agent_System_Base_Help_py_moovit_scripts/code
chmod +x python_sim.py
rosrun py_moveit py_cogntive_robots






