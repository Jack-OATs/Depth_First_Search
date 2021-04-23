# README - Find Path in Map #

This is the framework for writing a DFS to search a 2 dimensional array of 1's and 0's (with 1 being a wall) to find a path from one point to another.  The depth first search should begin going down, then to the right, then up, and finally to the left when doing a search.  Since it is depth first it should go in the order of those directions until it hits a wall.  All paths on any map must be found and returned in under 5 seconds.

## Files Contained ##

### Map_Builder.py ###
Used to create a new series of maps and save them to the Maps directory.  

### map_path.py ###
Template file used for completing the homework assignment.  The method *find_path_DFS(map, current, goal, explored, path, depth=0)* will be the one to complete and the signature must remain functional in this form.  You may add more methods if needed.

### map_display.py ###
A file that will allow you to display a map in 2D array on the screen.
