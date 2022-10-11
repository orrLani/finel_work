# finel_work

# How to run the code

## install ros melodic -
  http://wiki.ros.org/melodic/Installation/Ubuntu
 
##  install TurtleBot3 Simulation
sudo apt-get install ros-melodic-turtlebot3-*

## install MoveIt:
 sudo apt install ros-melodic-catkin python-catkin-tools
 sudo apt install ros-melodic-moveit
 
## Create a catkin workspace if haven't already
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_init_workspace
ls -l

## Clone or download project repository into the src directory of the catkin workspace
cd ~/catkin_ws/src


git clone https://github.com/andreasBihlmaier/gazebo2rviz.git
git clone https://github.com/andreasBihlmaier/pysdf.git
git clone https://github.com/JenniferBuehler/general-message-pkgs.git
git clone https://github.com/JenniferBuehler/gazebo-pkgs.git
git clone https://github.com/pal-robotics/gazebo_ros_link_attacher.git
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone https://github.com/orrLani/finel_work.git


## Build the project
cd ~/catkin_ws
catkin_make

## run the folowing code in 4 terminals:

### At the first terminal run:
cd ~/catkin_ws
source devel/setup.bash
export TURTLEBOT3_MODEL=burger 
roscore 

### At the secound terminal run:
cd ~/catkin_ws
source devel/setup.bash
export TURTLEBOT3_MODEL=burger 
roslaunch new_moveit_config multi_gazebo_update.launch 

### At the third terminal run:
cd ~/catkin_ws
source devel/setup.bash
export TURTLEBOT3_MODEL=burger 
roslaunch new_moveit_config bringup_update.launch

### At the last terminal run:
cd ~/catkin_ws
source devel/setup.bash
cd src/finel_work/code
chmod +x python_sim.py
rosrun py_moveit py_cogntive_robots






