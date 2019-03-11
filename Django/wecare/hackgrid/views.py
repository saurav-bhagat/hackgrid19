from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .helpers import Map, load_map_40, show_map
import math
from .path import *


PathPlanner.create_closedSet = create_closedSet
PathPlanner.create_openSet = create_openSet
PathPlanner.create_cameFrom = create_cameFrom
PathPlanner.create_gScore = create_gScore
PathPlanner.create_fScore = create_fScore
PathPlanner.set_map = set_map
PathPlanner.set_start = set_start
PathPlanner.set_goal = set_goal
PathPlanner.get_current_node = get_current_node
PathPlanner.get_neighbors = get_neighbors
PathPlanner.get_gScore = get_gScore
PathPlanner.get_tenative_gScore = get_tenative_gScore
PathPlanner.is_open_empty = is_open_empty
PathPlanner.distance = distance
PathPlanner.heuristic_cost_estimate = heuristic_cost_estimate
PathPlanner.calculate_fscore = calculate_fscore
PathPlanner.record_best_path_to = record_best_path_to

maps = load_map_40()

hospital = {
        "Eye Foundation and Research Center":0,
        "Apollo Gleneagles Hospitals":23,
        "AMRI Hospitals":31
    }
    
locations = {
    "Tangra" : 34,
    "Kankurgachi" : 2,
    "Beleghata" :26,
    "Nicco Park": 19,
    "Sister Nivedita Statue": 10,
    "Newtown" : 14,
    "Salt lake stadium": 20,
    "Kali Mandir" : 28,
    "LA Block" : 33
}



# Create your views here.


@csrf_exempt
def base_demo(request):
    s = int(request.GET.get('location',''))
    g = int(request.GET.get('hospital',''))
    print(s,g)
    planner = PathPlanner(maps, s, g)
        # path = planner.path
    result = show_map(maps, start=s, goal=g, path=planner.path)
    print(type(result))
    response = render(request, 'hackgrid/graph-display.html', { 'graph': result})
    response['X-Frame-Options'] = "ALLOW-FROM http://b1ddece1.ngrok.io/"
    return response


