import math
import numpy as np
from in_out import *
from math import radians, sin, cos, sqrt, atan2

waypointDict = {}


def determinePath(waypointDict):
    # Define the distance function

    def distance(lat1, lon1, lat2, lon2):
        R = 6371e3  # Earth's radius in meters
        phi1 = radians(lat1)
        phi2 = radians(lat2)
        delta_phi = radians(lat2 - lat1)
        delta_lambda = radians(lon2 - lon1)

        a = sin(delta_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        d = R * c
        return d

    # Find the starting waypoint with label 'H'
    start_index = None
    for i in range(len(waypointDict['waypointType'])):
        if waypointDict['waypointType'][i] == 'H':
            start_index = i
            break

    if start_index is None:
        raise ValueError("No starting point with label 'H' found in waypoint data.")

    # Initialize the order of waypoints to visit
    order = [start_index]

    # Create copies of the lists
    latitude2 = list(waypointDict['latitude'])
    longitude2 = list(waypointDict['longitude'])
    altitude2 = list(waypointDict['altitude'])
    waypointType2 = list(waypointDict['waypointType'])

    # Iterate through remaining waypoints until all visited
    current = start_index
    while len(latitude2) > 1:
        # Initialize variables for minimum distance
        min_dist = float('inf')
        min_index = None

        # Iterate through remaining waypoints to find closest one
        for i in range(len(latitude2)):
            if i == current:
                continue  # Skip the current waypoint

            lat1 = float(latitude2[current])
            lon1 = float(longitude2[current])
            lat2 = float(latitude2[i])
            lon2 = float(longitude2[i])

            dist = distance(lat1, lon1, lat2, lon2)

            if dist < min_dist:
                min_dist = dist
                min_index = i

        # Add the closest waypoint to order list
        order.append(min_index)

        # Update current waypoint to the closest one
        current = min_index

        # Remove visited waypoint from list
        latitude2.pop(min_index)
        longitude2.pop(min_index)
        altitude2.pop(min_index)
        waypointType2.pop(min_index)
    return order


# PLACEHOLDER, just send out current list


order = [0, 1, 2, 3, 4]
