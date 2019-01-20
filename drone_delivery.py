from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
from geopy.distance import distance
import time


def create_distance_callback(dist_matrix):
  
    def distance_callback(from_node, to_node):
        d = distance(dist_matrix[from_node]['latlon'], dist_matrix[to_node]['latlon']).m
        return d 
    
    return distance_callback


def get_delivery_order(list_of_points):
    '''
    list_of_points: list containing dictionaries of points, with a name and lat and lon coordinates.
    returns dict with keys:
        result:bool 
        time_to_compute_in_seconds:float
        total_distance_in_meters:int
        delivery_order:list[dict]
    '''
    tsp_size = len(list_of_points)
    num_routes = 1
    origin = 0

    # Response payload
    result = False
    time_to_compute_in_seconds = -1
    total_distance_in_meters = -1
    delivery_order = []

    routing = pywrapcp.RoutingModel(tsp_size, num_routes, origin)
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
    dist_callback = create_distance_callback(list_of_points)
    routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)

    start_time = time.time()
    assignment = routing.SolveWithParameters(search_parameters)
    time_to_compute_in_seconds = time.time() - start_time

    if assignment:
        result = True
        print("success")
        total_distance_in_meters = assignment.ObjectiveValue()
        route_number = 0
        index = routing.Start(route_number) 
        
        while not routing.IsEnd(index):
            delivery_order.append(list_of_points[routing.IndexToNode(index)])
            index = assignment.Value(routing.NextVar(index))
        delivery_order.append(list_of_points[routing.IndexToNode(index)])

    return {"result": result, 
        "time_to_compute_in_seconds": time_to_compute_in_seconds, 
        "total_distance_in_meters": total_distance_in_meters, 
        "delivery_order": delivery_order}


def main():
    # Testing
    p0 = {'name': 'p0', 'latlon': (-33.891413, 151.268683)}
    p1 = {'name': 'p1', 'latlon': (-33.891338, 151.274032)}
    p2 = {'name': 'p2', 'latlon': (-33.889167, 151.270709)}
    p3 = {'name': 'p3', 'latlon': (-33.891867, 151.272004)}
    p4 = {'name': 'p4', 'latlon': (-33.894699, 151.268533)}
    p5 = {'name': 'p5', 'latlon': (-32.894699, 151.238533)}
    p6 = {'name': 'p6', 'latlon': (-31.894699, 151.268433)}
    p7 = {'name': 'p7', 'latlon': (-33.895699, 151.258533)}
    p8 = {'name': 'p8', 'latlon': (-33.893699, 151.298533)}
    p9 = {'name': 'p9', 'latlon': (-32.894699, 151.268533)}
    p10 = {'name': 'p10', 'latlon': (-30.894699, 150.268533)}

    points = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
        
    tsp_size = len(points)
    num_routes = 1
    depot = 0

    # Create routing model
    routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
    
    # Create the distance callback.
    dist_callback = create_distance_callback(points)
    routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
    
    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
        # Solution distance.
        print ("Total distance: " + str(assignment.ObjectiveValue()) + " meters\n")
        # Display the solution.
        # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
        route_number = 0
        index = routing.Start(route_number) # Index of the variable for the starting node.
        route = ''
        while not routing.IsEnd(index):
            # Convert variable indices to node indices in the displayed route.
            route += points[routing.IndexToNode(index)]['name'] + ' -> '
            index = assignment.Value(routing.NextVar(index))
        
        route += points[routing.IndexToNode(index)]['name']
        print ("Route:\n\n" + route)
    else:
        print ('No solution found.')

if __name__ == '__main__':
  main()