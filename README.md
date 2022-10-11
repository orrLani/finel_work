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
cd ~/catkin_ws/ </br>
catkin_init_workspace </br>
ls -l </br>

## Clone or download project repository into the src directory of the catkin workspace
cd ~/catkin_ws/src </br>
git clone  https://github.com/andreasBihlmaier/gazebo2rviz.git </br>
git clone https://github.com/andreasBihlmaier/pysdf.git  </br>
git clone https://github.com/JenniferBuehler/general-message-pkgs.git </br>
git clone https://github.com/JenniferBuehler/gazebo-pkgs.git </br>
git clone https://github.com/pal-robotics/gazebo_ros_link_attacher.git </br>
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git </br>
git clone https://github.com/orrLani/finel_work.git </br>


## Build the project
cd ~/catkin_ws </br>
catkin_make </br>

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






