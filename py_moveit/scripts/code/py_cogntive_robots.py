#!/usr/bin/env python
##
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(os.path.join(parent,'parser'))
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import numpy as np
from go_to_module import go_to
import time
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.srv import GetMap
import actionlib
import matplotlib.pyplot as plt
from geometry_msgs.msg import PoseWithCovarianceStamped
from get_blocks import get_block_pos
from geometry_msgs.msg import PoseStamped
from attach import attach
from detach import detach
from PDDL_Planner import PlanToCommamndDict


def reverse():
    print('in reverse')
    pub = rospy.Publisher('tb3_0/cmd_vel', Twist, queue_size=10)
    twist = Twist()
    j = 0
    r = rospy.Rate(10)
    while j < 30:
        twist.linear.x = -0.18
        twist.angular.z = 0
        pub.publish(twist)
        r.sleep()
        j += 1
    j = 0
    r = rospy.Rate(10)
    while j < 30:
        twist.linear.x = 0
        twist.angular.z = 0
        pub.publish(twist)
        r.sleep()
        j += 1
    return


def close_gripper(self, goal=0.02):
    group = moveit_commander.MoveGroupCommander('gripper')
    joint_goal = group.get_current_joint_values()

    joint_goal[0] = goal
    joint_goal[1] = -goal
    group.go(joint_goal, wait=True)
    group.stop()


def open_gripper(self, goal=0):
    group = moveit_commander.MoveGroupCommander('gripper')
    joint_goal = group.get_current_joint_values()

    joint_goal[0] = goal
    joint_goal[1] = goal
    group.go(joint_goal, wait=True)
    group.stop()


def all_close(goal, actual, tolerance):
    all_equal = True
    if type(goal) is list:
        for index in range(len(goal)):

            if abs(actual[index] - goal[index]) > tolerance:
                return False

    elif type(goal) is geometry_msgs.msg.PoseStamped:
        return all_close(goal.pose, actual.pose, tolerance)

    elif type(goal) is geometry_msgs.msg.Pose:
        return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)

    return True


def get_quaternion_from_euler(roll, pitch, yaw):
    """
    Convert an Euler angle to a quaternion.

    Input
      :param roll: The roll (rotation around x-axis) angle in radians.
      :param pitch: The pitch (rotation around y-axis) angle in radians.
      :param yaw: The yaw (rotation around z-axis) angle in radians.

    Output
      :return qx, qy, qz, qw: The orientation in quaternion [x,y,z,w] format
    """
    qx = np.sin(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) - np.cos(roll / 2) * np.sin(pitch / 2) * np.sin(yaw / 2)
    qy = np.cos(roll / 2) * np.sin(pitch / 2) * np.cos(yaw / 2) + np.sin(roll / 2) * np.cos(pitch / 2) * np.sin(yaw / 2)
    qz = np.cos(roll / 2) * np.cos(pitch / 2) * np.sin(yaw / 2) - np.sin(roll / 2) * np.sin(pitch / 2) * np.cos(yaw / 2)
    qw = np.cos(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) + np.sin(roll / 2) * np.sin(pitch / 2) * np.sin(yaw / 2)

    return [qx, qy, qz, qw]
class MoveGroupPythonIntefaceTutorial(object):
    """MoveGroupPythonIntefaceTutorial"""

    def __init__(self):
        super(MoveGroupPythonIntefaceTutorial, self).__init__()

        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('move_group_python_interface_tutorial',
                        anonymous=True)

        robot = moveit_commander.RobotCommander()

        scene = moveit_commander.PlanningSceneInterface()

        group_name = "arm"
        group = moveit_commander.MoveGroupCommander(group_name)

        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                       moveit_msgs.msg.DisplayTrajectory,
                                                       queue_size=20)

        planning_frame = group.get_planning_frame()

        eef_link = group.get_end_effector_link()

        group_names = robot.get_group_names()

        self.box_name = ''
        self.robot = robot
        self.scene = scene
        self.group = group
        self.display_trajectory_publisher = display_trajectory_publisher
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = group_names

    def open_grip(self):
        open_gripper(self)
        rospy.sleep(2)

    def close_grip(self):
        close_gripper(self)
        rospy.sleep(2)

    def go_to_joint_state(self):


        group = self.group
        pose = group.get_current_pose(end_effector_link="plate_link")
        # print(pose)

        joint_goal = group.get_current_joint_values()
        joint_goal[0] = 0
        joint_goal[1] = 0
        joint_goal[2] = 0
        joint_goal[3] = 0
        joint_goal[4] = 0
        joint_goal[5] = 0
        joint_goal[6] = 0

        group.go(joint_goal, wait=True)

        group.stop()

        close_gripper(self)
        rospy.sleep(2)
        open_gripper(self)

        current_joints = self.group.get_current_joint_values()
        return all_close(joint_goal, current_joints, 0.03)

    def go_to_pose_goal(self, pick):

        group = self.group

        x_pos = pick[0]  # -0.182
        y_pos = pick[1]  # 0.0
        z_pos = 0.174  # 0.174

        roll_deg = 0
        pitch_deg = -180
        yaw_deg = 0

        pose_goal = go_to(x_pos, y_pos, z_pos, roll_deg, pitch_deg, yaw_deg)

        pose = group.get_current_pose(end_effector_link="plate_link")

        group.set_goal_position_tolerance(0.02)
        group.set_goal_orientation_tolerance(0.02)

        group.set_pose_target(pose_goal)

        plan = group.go(wait=True)

        group.stop()

        current_pose = self.group.get_current_pose().pose
        return plan

    def plan_cartesian_path(self, dist, scale=1, ):

        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        group = self.group
        waypoints = []
        wpose = group.get_current_pose().pose
        wpose.position.z += scale * dist  # First move up (z)
        waypoints.append(copy.deepcopy(wpose))
        (plan, fraction) = group.compute_cartesian_path(
            waypoints,  # waypoints to follow
            0.01,  # eef_step
            0.0)  # jump_threshold
        return plan, fraction

    def display_trajectory(self, plan):
        robot = self.robot
        display_trajectory_publisher = self.display_trajectory_publisher
        display_trajectory = moveit_msgs.msg.DisplayTrajectory()
        display_trajectory.trajectory_start = robot.get_current_state()
        display_trajectory.trajectory.append(plan)
        # Publish
        display_trajectory_publisher.publish(display_trajectory)

    def execute_plan(self, plan, open):

        group = self.group

        group.execute(plan, wait=True)
        rospy.sleep(1)
        if open:
            open_gripper(self)
        if not open:
            close_gripper(self)
        return

    def pick_n_place(self, pick, place):

        picked = self.go_to_pose_goal(pick)

        if picked:
            rospy.sleep(3)
            cartesian_plan, fraction = self.plan_cartesian_path(dist=-0.08)
            self.display_trajectory(cartesian_plan)
            self.execute_plan(cartesian_plan, open=False)
            print('ready to place')
            rospy.sleep(3)
            self.go_to_pose_goal(place)
            cartesian_plan, fraction = self.plan_cartesian_path(dist=0.08)
            self.display_trajectory(cartesian_plan)
            self.execute_plan(cartesian_plan, open=True)
            return True
        else:
            return False

    def pickup(self, pick):

        picked = self.go_to_pose_goal(pick)

        if picked:
            rospy.sleep(3)
            cartesian_plan, fraction = self.plan_cartesian_path(dist=-0.08)
            self.display_trajectory(cartesian_plan)
            self.execute_plan(cartesian_plan, open=False)
            print('ready to place')
            return True
        else:
            return False

    def drop(self, place):

        placed = self.go_to_pose_goal(place)

        if placed:
            rospy.sleep(3)
            cartesian_plan, fraction = self.plan_cartesian_path(dist=0.08)
            self.display_trajectory(cartesian_plan)
            self.execute_plan(cartesian_plan, open=True)
            print('box placed')
			rospy.sleep(1)
            return True
        else:
            return False

class MapService(object):

    def __init__(self):
        """
        Class constructor
        """
        rospy.wait_for_service('static_map')
        static_map = rospy.ServiceProxy('static_map', GetMap)
        self.map_data = static_map().map
        self.map_org = np.array([self.map_data.info.origin.position.x, self.map_data.info.origin.position.y])
        shape = self.map_data.info.height, self.map_data.info.width
        self.map_arr = np.array(self.map_data.data, dtype='float32').reshape(shape)
        self.resolution = self.map_data.info.resolution

    def show_map(self, point=None):
        plt.imshow(self.map_arr)
        if point is not None:
            plt.scatter([point[0]], [point[1]])
        plt.show()

    def position_to_map(self, pos):
        return (pos - self.map_org) // self.resolution

    def map_to_position(self, indices):
        return indices * self.resolution + self.map_org


class AskOfHelp(object):

    def __init__(self, box_pose, cyton_pose, drop_pose):
        self.goal_pose = box_pose
        self.cyton_pose = cyton_pose
        self.client = actionlib.SimpleActionClient('tb3_0/move_base', MoveBaseAction)
        self.goal = MoveBaseGoal()
        self.x = -1.5
        self.y = 0
        self.boxcounter = 0
        self.drop_pose = drop_pose

    def movebase_client(self, goal_pose):
        self.client.wait_for_server()
        # Creates a new goal with the MoveBaseGoal constructor
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        # Move to position 0.5 on the x axis of the "map" coordinate frame
        goal.target_pose.pose.position.x = goal_pose[0]
        # Move to position 0.5 on the y axis of the "map" coordinate frame
        goal.target_pose.pose.position.y = goal_pose[1]
        # No rotation of the mobile base frame w.r.t. map frame
        # goal.target_pose.pose.orientation.w = goal_pose[3]
        # find the bast angle
        if not goal_pose[6]:
            if np.rad2deg(np.arctan2(goal_pose[1], goal_pose[0])) > 90:
                goal.target_pose.pose.orientation.z = 180 - np.rad2deg(np.arctan2(goal_pose[1], goal_pose[0]))
            elif np.rad2deg(np.arctan2(goal_pose[1], goal_pose[0])) < 0:
                goal.target_pose.pose.orientation.z = 45 + np.rad2deg(np.arctan2(goal_pose[1], goal_pose[0]))
            else:
                goal.target_pose.pose.orientation.z = np.rad2deg(np.arctan2(goal_pose[1], goal_pose[0]))
        else:
            goal.target_pose.pose.orientation.z = np.rad2deg(np.arctan(goal_pose[1] / goal_pose[0]))
        goal.target_pose.pose.orientation.w = np.rad2deg(np.arctan2(goal_pose[1], goal_pose[0]))
        # Sends the goal to the action server.
        self.client.send_goal(goal)
        time.sleep(0.1)
        rospy.loginfo("New goal command received!")
        # Waits for the server to finish performing the action.
        wait = self.client.wait_for_result()
        # If the result doesn't arrive, assume the Server is not available
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            # Result of executing the action
            return self.client.get_result()
        time.sleep(0.1)

    def move_to_point(self, goal_pose):
        try:
            result = self.movebase_client(goal_pose)
        except rospy.ROSInterruptException:
            reverse()


def wapper_action(tutorial, i, tb3, pose, k):
    k = k
    box = i['Box']
    action = i['Action']
    if action == 'move':
        print("action move")
        tb3.move_to_point(pose)
        attach_flag = pose[6]
    elif action == 'reverse':
        print("action reverse")
        reverse()
        if pose[6] == 0 and '3' in box:
            attach_flag = pose[6]
            return [attach_flag, k]
        tb3.move_to_point(pose)
        attach_flag = pose[6]
    elif action == 'attach':
        box = i['Position']
        print("action attach")
        temp = attach(box, "link", "tb3_0", "base_footprint")
        attach_flag = 1
    elif action == 'dettach':
        print("action detach")
        box = i['Box']
        temp = detach(box, "link", "tb3_0", "base_footprint")
        attach_flag = 0
    elif action == 'pickup':
        print("action pickup")
        box_list = get_block_pos()
        pick = box_list[box]
        print(pick)
        moved = tutorial.pickup(pick)
        tutorial.go_to_joint_state()
        tutorial.close_grip()
        attach_flag = pose[6]
    elif action in ['drop']:
        print("action place")
        print(pose)
        pose[2] = 0.065 * k
        moved = tutorial.drop(pose)
        attach_flag = pose[6]
        k = k + 1
        tutorial.go_to_joint_state()
    return [attach_flag, k]

def main():
    start_time = time.time()
    try:
    	domain = sys.argv[1]
    	problem = sys.argv[2]
    except IndexError:
	domain = os.path.join(parent,'pddl','domain_cypton_tb3.pddl')
	problem = os.path.join(parent,'pddl','problem_cypton_tb3.pddl')
	assert os.path.isfile(domain) and os.path.isfile(problem)


    plan = PlanToCommamndDict(domain, problem)
    tutorial = MoveGroupPythonIntefaceTutorial()
    tutorial.go_to_joint_state()
    box_list = get_block_pos()
    tower = [-0.16, 0, 0]
    cyton_pose = [0, 0, 0]
    pickup = [-0.03, 0.24, 0] # [0, 0.17, 0]
    attach_flag = 0
    k = 0
    for i in plan:
        if i['Position'] in ['box_1', 'box_2', 'box_3']:
            box_to_get = box_list[i['Position']]
        elif i['Position'] in ['pickup', 'tower']:
            if i['Position'] == 'pickup':
                box_to_get = pickup
            else:
                if i['Action'] == 'move':
                    box_to_get = [1, 1, 0]
                else:
                    box_to_get = tower
        else:
            box_to_get = tower
            
        try:
            x_pos = box_to_get[0]
            y_pos = box_to_get[1]
            z_pos = box_to_get[2]
            roll_deg = 0
            pitch_deg = 45
            yaw_deg = 0
            pose = [x_pos, y_pos, z_pos, roll_deg, pitch_deg, yaw_deg, attach_flag]
            a = AskOfHelp(pose, cyton_pose, pickup)
            [attach_flag, k] = wapper_action(tutorial, i, a, pose, k)

        except rospy.ROSInterruptException:
            return
        except KeyboardInterrupt:
            return
	tutorial.go_to_joint_state()

if __name__ == '__main__':
    main()
