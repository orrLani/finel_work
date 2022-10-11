# finel_work

# How to run the code

## install the code via the folowning github:
https://github.com/orrLani/Multi_Agent_System_Based_Help </br>

## Create a catkin workspace if haven't already
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/ </br>
catkin_init_workspace </br>
ls -l </br>

## run the folowing code in 4 terminals:

### At the first terminal run:
cd ~/catkin_ws </br>
source devel/setup.bash </br>
export TURTLEBOT3_MODEL=burger  </br>
roscore 

### At the secound terminal run:
cd ~/catkin_ws </br>
source devel/setup.bash </br>
export TURTLEBOT3_MODEL=burger  </br>
roslaunch new_moveit_config multi_gazebo_update.launch 

### At the third terminal run:
cd ~/catkin_ws </br>
source devel/setup.bash </br>
export TURTLEBOT3_MODEL=burger </br>
roslaunch new_moveit_config bringup_update.launch 

### At the last terminal run:
cd ~/catkin_ws </br>
source devel/setup.bash </br>
cd src/finel_work/py_mooveit/scripts/code </br>
chmod +x python_sim.py </br>
rosrun py_moveit py_cogntive_robots






