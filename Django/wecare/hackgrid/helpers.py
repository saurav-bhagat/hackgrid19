import networkx as nx
import pickle
import plotly.plotly as py
import plotly
import random
from plotly.graph_objs import *
import math
from plotly.offline import init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import plotly.io as pio


map_40_dict = {
    0:{'pos':(62,-36), 'connections': [1]},
1:{'pos':(54,-61), 'connections': [0,2]},
2:{'pos':(106,-67), 'connections': [1,3,25]},
3:{'pos':(247,-77), 'connections': [2,4]},
4:{'pos':(308,-58), 'connections': [3,5,22]},
5:{'pos':(408,-40), 'connections': [4,6]},
6:{'pos':(445,-95), 'connections': [5,8,22]},
7:{'pos':(544,-137), 'connections': [10,8,18,9]},
8:{'pos':(474,-121), 'connections': [6,7,20]},
9:{'pos':(629,-159), 'connections': [7,11,16,17]},
10:{'pos':(559,-76), 'connections': [11,7]},
11:{'pos':(652,-99), 'connections': [9,10,12,15]},
12:{'pos':(679,-55), 'connections': [11,13,15]},
13:{'pos':(743,-20), 'connections': [12,14]},
14:{'pos':(783,-84), 'connections': [13,15]},
15:{'pos':(718,-121), 'connections': [11,12,14,16]},
16:{'pos':(689,-180), 'connections': [15,9,19]},
17:{'pos':(588,-275), 'connections': [19,18,9]},
18:{'pos':(513,-257), 'connections': [7,17,20,31]},
19:{'pos':(639,-291), 'connections': [16,17,32]},
20:{'pos':(449,-238), 'connections': [21,8,18]},
21:{'pos':(367,-253), 'connections': [20,22,24,29]},
22:{'pos':(336,-159), 'connections': [4,21,23]},
23:{'pos':(311,-166), 'connections': [22]},
24:{'pos':(197,-250), 'connections': [21,25]},
25:{'pos':(84,-228), 'connections': [2,24,26,35]},
26:{'pos':(153,-338), 'connections': [25,27,34]},
27:{'pos':(221,-421), 'connections': [28,26]},
28:{'pos':(349,-449), 'connections': [27,29]},
29:{'pos':(446,-445), 'connections': [21,28,30,33]},
30:{'pos':(483,-377), 'connections': [29,31,32]},
31:{'pos':(499,-322), 'connections': [18,30]},
32:{'pos':(584,-408), 'connections': [19,30]},
33:{'pos':(509,-524), 'connections': [29,32]},
34:{'pos':(82,-377), 'connections': [35,26]},
35:{'pos':(84,-293), 'connections': [34,25]}  
}





class Map:
	def __init__(self, G):
		self._graph = G
		self.intersections = nx.get_node_attributes(G, "pos")
		self.roads = [list(G[node]) for node in G.nodes()]

	def save(self, filename):
		with open(filename, 'wb') as f:
			pickle.dump(self._graph, f)

def load_map_graph(map_dict):
	G = nx.Graph()
	for node in map_dict.keys():
		G.add_node(node, pos=map_dict[node]['pos'])
	for node in map_dict.keys():
		for con_node in map_dict[node]['connections']:
			G.add_edge(node, con_node)
	return G

def load_map_10():
	G = load_map_graph(map_10_dict)
	return Map(G)

def load_map_40():
	G = load_map_graph(map_40_dict)
	return Map(G)

def show_map(M, start=None, goal=None, path=None):
    
    
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
    
    cord_mapper = {
        "Eye Foundation and Research Center":0,
        "Apollo Gleneagles Hospitals":23,
        "AMRI Hospitals":31,
        "Tangra" : 34,
        "Kankurgachi" : 2,
        "Beleghata" :26,
        "Nicco Park": 19,
        "Sister Nivedita Statue": 10,
        "Newtown" : 14,
        "Salt Lake stadium": 20,
        "Kali Mandir" : 28,
        "LA Block" : 33
    }
    
    locmapper = {
        0:"Eye Foundation and Research Center",
        23:"Apollo Gleneagles Hospitals",
        31:"AMRI Hospitals",
        34:"Tangra",
        2: "Kankurgachi",
        26: "Beleghata" ,
        19: "Nicco Park",
        10: "Sister Nivedita Statue",
        14: "Newtown" ,
        20: "Salt Lake stadium",
        28: "Kali Mandir" ,
        33: "LA Block" 
        
    }
    
    
    G = M._graph
    pos = nx.get_node_attributes(G, 'pos')
    abx = []
    aby = []

    for edge in G.edges():
        x0, y0 = G.node[edge[0]]['pos']
        x1, y1 = G.node[edge[1]]['pos']
        abx += [x0, x1, None]
        aby += [y0, y1, None]
    
    
    edge_trace = Scatter(
    x=abx,
    y=aby,
    line=Line(width=1,color='#888'),
    hoverinfo='none',
    mode='lines')
    
    #result lines
    abx = []
    aby = []
    res = [start]+path+[goal]
    for i in range(len(res)-1):
        x0, y0 = G.node[res[i]]['pos']
        x1, y1 = G.node[res[i+1]]['pos']
        abx += [x0, x1, None]
        aby += [y0, y1, None]
        
    edge_trace1 = Scatter(
    x=abx,
    y=aby,
    line=Line(width=4,color='blue'),
    hoverinfo='none',
    mode='lines')
    

    aax = []
    aay = []
    az = []
    
    for node in hospital:
        x, y = G.node[hospital[node]]['pos']
        aax.append(x)
        aay.append(y)
        node_info = node
        az.append(node_info)
        

    #hospital
    node_trace = Scatter(
        x=aax,
        y=aay,
        text=az,
        mode='markers+text',
        textposition='top right',
        hoverinfo='text',
        marker=Marker(
            showscale=False,
            colorscale='Hot',
            reversescale=True,
            color='red',
            symbol=3,
            size=15,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=2)))
    
    aax =[]
    aay =[]
    az =[]
    for node in locations:
        x, y = G.node[locations[node]]['pos']
        aax.append(x)
        aay.append(y)
        az.append(node)
        
   



    #location
    node_trace1 = Scatter(
        x=aax,
        y=aay,
        text=az,
        mode='markers+text',
        textposition='top center',
        hoverinfo='text',
        marker=Marker(
            showscale=False,
            colorscale='Hot',
            reversescale=True,
            #color='blue',
            symbol=114,
            size=15,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=2)))


    fig = Figure(data=Data([edge_trace,node_trace,node_trace1,edge_trace1]),
                 layout=Layout(
                    title='<br>Ambulance path',
                    titlefont=dict(size=16),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                   
                    xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))
    #pio.write_image(fig, 'images/fig1.svg')
    return(plotly.offline.plot(fig,output_type = "div", include_plotlyjs=False))
    