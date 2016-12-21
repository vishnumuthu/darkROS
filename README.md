# darkROS
Title - 3D localization and classification of trash object for mobile cleaning robots

## Introduction:
The main objective of the project is to separate the trash from a road side environment or an after party site. The process is designed that the robot is programmed to navigate and search the area for path and detecting object. Later, after detecting trash they are classified into three sections like paper cup, can or thin and the organic like leaf.

# DarkROS Project Instruction:
Please install all the Packages and tools for the program to execute correctly.
## Simulation section:
Used to simulate the packages of ROS and DarkROS using Gazebo,

Pre-install:
```
sudo apt-get install ros-indigo-gazebo-ros-pkgs ros-indigo-gazebo-ros-control
sudo apt-get install ros-indigo-turtlebot-simulator
```

Weblink:

http://gazebosim.org/tutorials?tut=ros_installing

http://wiki.ros.org/turtlebot_simulator

## Real turtlebot section:
### Turtlebot:
Used to kick start all the sensor connection for the turtlebot robot.

Pre-install:
```
sudo apt-get install ros-indigo-turtlebot-bringup ros-indigo-turtlebot-navigation ros-indigo-rtabmap-ros
```

### Rtabmap_ros (3D reconstruction of area):
Design the 3D environment of the arena using kinect.

Pre-install:
```
sudo apt-get install ros-indigo-rtabmap-ros
```

Weblink:

http://wiki.ros.org/rtabmap_ros/Tutorials/MappingAndNavigationOnTurtlebot


### Frontier_explorer(Autonomous navigation):
Explore the unseen area inside the boundary.

Pre-install (Note:The modified code is placed inside the DarkROS):
```
git clone https://github.com/paulbovbel/frontier_exploration.git
```

Weblink:

http://wiki.ros.org/frontier_exploration

### Installing Object Recognition Packages:
Used to recognize the 3D object in the environment

Pre-install:
```
sudo apt-get install ros-indigo-ecto-*
sudo apt-get install ros-indigo-moveit-full
sudo apt-get install libosmesa6-dev
sudo apt-get install couchdb
```

Packages:
```
git clone http://github.com/wg-perception/object_recognition_core
git clone http://github.com/wg-perception/capture
git clone http://github.com/wg-perception/reconstruction
git clone http://github.com/wg-perception/linemod
git clone http://github.com/wg-perception/ork_renderer
git clone http://github.com/wg-perception/tabletop
git clone http://github.com/wg-perception/tod
git clone http://github.com/wg-perception/transparent_objects
```

Additional:
```
git clone http://github.com/wg-perception/object_recognition_msgs
git clone http://github.com/wg-perception/object_recognition_ros
git clone http://github.com/wg-perception/object_recognition_ros_visualization
git clone https://github.com/wg-perception/ork_tutorials
```
weblink:

http://wg-perception.github.io/object_recognition_core/install.html#install

http://wg-perception.github.io/object_recognition_core/infrastructure/couch.html#object-recognition-core-db

https://wg-perception.github.io/ork_tutorials/tutorial01/tutorial.html

https://wg-perception.github.io/ork_tutorials/tutorial02/tutorial.html

http://wg-perception.github.io/capture/index.html#ork-capture

### AR tag tracker:

Pre-install (Note:The modified code is placed inside the DarkROS):
```
Git clone https://github.com/sniekum/ar_track_alvar.git
```
Weblink:

http://wiki.ros.org/ar_track_alvar

### Speech:

Pre-install:
```
sudo apt-get install ros-indigo-audio-common
sudo apt-get install libasound2
sudo apt-get install festvox-don 
```

Weblink:

http://wiki.ros.org/sound_play

# Working:
## Simulation:
```
Roslaunch fake_turtle fake_turtle.launch
```
Use the command for the Gazebo to start up.

## Real Time:
### Adding the Database:
```
rosrun object_recognition_core object_add.py -n "<name>" -d "<details>" --commit
rosrun object_recognition_core mesh_add.py <add the ID code of DB> <path to stl file> --commit (or)
rosrun object_recognition_capture upload -i <bag file> -n '<name>' -d <detail> --commit
```

### Training the Database:
```
rosrun object_recognition_core training -c `rospack find object_recognition_linemod`/conf/training.ork
```

## TurtleBot:
```
Roslaunch real_turtle real_turtlebot.launch (or)
Roslaunch real_turtle real_turtlebot1.launch (or)
Roslaunch real_turtle real_turtlebot_final.launch 
```
## Workstation:
```
Roslaunch real_turtle real_turtlebot_station.launch
```
