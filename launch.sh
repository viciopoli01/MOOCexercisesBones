#!/bin/bash

set -e

#roslaunch vehicle_detection vehicle_detection_node.launch veh:=![vehicle]
#roslaunch vehicle_detection vehicle_filter_node.launch veh:=cristina
roslaunch mooc mooc.launch veh:=$VEHICLE_NAME