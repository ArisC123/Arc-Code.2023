import math
from algo import *
from in_out import *


def main(filename):
    print("Starting main function")
    waypoints = readWaypointFile(filename)


    # Determine path
    path = determinePath(waypointDict)

    if order is not None:
        # Export path
        for i in path:
            print("Latitude: ", float(waypointDict['latitude'][i]), " Longitude: ", float(waypointDict['longitude'][i]))
            print(order)
    else:
        print("No order/path found.")


if __name__ == '__main__':
    main('waypoint_1.txt')
