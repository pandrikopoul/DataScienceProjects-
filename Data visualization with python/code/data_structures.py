import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pydot # conda install pydot
import time
from matplotlib.colors import Normalize
import matplotlib.colors as mcolors
import math
import matplotlib.collections as collections

################## classes part 1 #####################


class Vertex:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.neighbors = []
    def add_neighbor(self,neighbor):
        self.neighbors.append(neighbor)
class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, vertex):
        self.vertices[vertex.id] = vertex

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_vertex(self, id):
        if id not in self.vertices:
            return None
        return self.vertices[id]

    def visualize_graph(self,custom_figsize,radius): # O(V + V + E) = O(2V + E) = O(V + E)
        self.place_vertices_in_circle(radius) # O(V)
        fig, ax = plt.subplots(figsize=(custom_figsize, custom_figsize))  # Adjust width and height as needed
        # Plot Vertices
        scaling_factor = 1 / len(self.vertices)
        for vertex in self.vertices.values(): # O(V)
            ax.scatter(vertex.x, vertex.y, color='blue', zorder=2, s= scaling_factor* 40000*(custom_figsize/15), edgecolors='black')
            ax.text(vertex.x, vertex.y, str(vertex.id), fontsize= (scaling_factor* 40000*(custom_figsize/15))/100, ha='center', va='center', zorder=len(self.vertices) * scaling_factor * 2, color='white')
        # Plot edges
        for edge in self.edges: #O(E)
            start = self.vertices[edge.start.id]
            end = self.vertices[edge.end.id]
            ax.plot([start.x, end.x], [start.y, end.y], color='gray', zorder=1, linewidth=0.5)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Graph Visualization')
        ax.grid(True)
        plt.show()
    def visualize_graph_Bonus(self,custom_figsize,radius): # O(V + V + E) = O(2V + E) = O(V + E)
        avg_nghb=0
        #compute average neighbors
        for vertex in self.vertices.values():
          avg_nghb+= len(vertex.neighbors)
        avg_nghb= avg_nghb/len(self.vertices)
        print("avg neighbors",avg_nghb)
        #---
        self.place_vertices_in_circle_Bonus(radius,avg_nghb) # O(V)
        fig, ax = plt.subplots(figsize=(custom_figsize, custom_figsize))  # Adjust width and height as needed
        # Plot Vertices
   # Plot Vertices
        scaling_factor = 1 / len(self.vertices)
        for vertex in self.vertices.values(): # O(V)

            ax.scatter(vertex.x, vertex.y, color='blue', zorder=2, s= scaling_factor* 40000*(custom_figsize/15), edgecolors='black')
            ax.text(vertex.x, vertex.y, str(vertex.id), fontsize= (scaling_factor* 40000*(custom_figsize/15))/100, ha='center', va='center', zorder=len(self.vertices) * scaling_factor * 2, color='white')
        # Plot edges
        for edge in self.edges: #O(E)
            start = self.vertices[edge.start.id]
            end = self.vertices[edge.end.id]
            ax.plot([start.x, end.x], [start.y, end.y], color='gray', zorder=1, linewidth=0.5)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Graph Visualization')
        ax.grid(True)
       # ax.set_aspect('equal', adjustable='box')
        plt.show()

    def place_vertices_in_circle(self,radius): # O(V)
        num_vertices = len(self.vertices)
        radius = radius  # Radius of the circle
        center_x = 0
        center_y = 0
        angle_increment = 2 * np.pi / num_vertices

        # Place vertices in a bit of randomized circle
        for i, vertex in enumerate(self.vertices.values()): # O(V)
            angle = i * angle_increment
            vertex.x = center_x + radius * np.cos(angle)
            vertex.y = center_y + radius * np.sin(angle)
    def place_vertices_in_circle_Bonus(self,radius,avg_nghb): # O(V)

        num_vertices = len(self.vertices)
        radius = radius  # Radius of the circle
        given_radius = radius
        center_x = 0
        center_y = 0
        angle_increment = 2 * np.pi / num_vertices

        # Place vertices in a bit of randomized circle
        for i, vertex in enumerate(self.vertices.values()): # O(V)
            radius = given_radius
            if len(vertex.neighbors) > avg_nghb/3 and  len(vertex.neighbors) <= avg_nghb :
                radius=radius-0.2*radius
            if len(vertex.neighbors) > avg_nghb :
                radius=radius-0.4*radius
            angle = i * angle_increment
            vertex.x = center_x + radius * np.cos(angle)
            vertex.y = center_y + radius * np.sin(angle)


def create_custom_graph(G): # O(V) + O(E) + O(V) + O(E) = O(2V + 2E) = O(V + E)
    # Parsing the vertices and edges from the generated graph into lists
    vertices = [n.get_name() for n in G.get_node_list()] # O(V)
    edges = [(edge.get_source(),edge.get_destination(),edge.get_weight()) for edge in G.get_edge_list()] # O(E)
    graph = Graph()
    for vertex in vertices: # O(V)
        vertex = Vertex(vertex, 0, 0)  # Initialize the vertex with ID and default coordinates
        graph.add_vertex(vertex)
    for edge in edges: # O(E)
        source_vertex = graph.get_vertex(edge[0])
        neighbor_vertex = graph.get_vertex(edge[1])
        if source_vertex is None:
            source_vertex = Vertex(edge[0], 0, 0)
        if neighbor_vertex is None:
            neighbor_vertex = Vertex(edge[1], 0, 0)
        source_vertex.add_neighbor(neighbor_vertex)
        graph.add_edge(Edge(source_vertex, neighbor_vertex))
    return graph

################## classes part 2 #####################

class vertex_for_BFS:
    def __init__(self, id):
        self.id = id
        self.color = 0 # 0 = white(not visited) | 1 = gray (visited & inside the queue) | 2 = black (visited & outside the queue)
        self.distance = float('inf')
        self.parent = None

class vertex_for_DFS:
    def __init__(self,id):
        self.id = id
        self.b = 0
        self.f = 0
        self.color = 0
        self.parent = None
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def top(self):
        return self.items[-1]

class TreeVertex:
    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.parent = parent
        self.point = None

class RadialPoint:
    def __init__(self, vertex, point, parent_point):
        self.vertex = vertex
        self.point = point
        self.parent_point = parent_point

################## classes part 3 #####################

class Forced_vertex:
    def __init__(self, id):
        self.id = id
        self.position = np.array([np.random.uniform(0, 10), np.random.uniform(0, 10)])  # Random initial position
        self.force = np.zeros(2)  # Initial force vector
################## classes parts 4 & 6  #####################
class FVertex(Vertex):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.parents = []
        self.children = []
    def add_neighbor(self,neighbor):
        self.neighbors.append(neighbor)
    def add_parents(self,parent):
        self.parents.append(parent)
    def add_children(self,child):
        self.children.append(child)

################## classes parts 4  #####################

class Graph_part_four:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_vertex(self, id):
        for vertex in self.vertices:
            if vertex.id == id:
                return vertex

    def remove_edge(self, start, end):
        for edge in self.edges:
            if edge.start == start and edge.end == end:
                self.edges.remove(edge)

    def remove_vertex(self, id):
        for vertex in self.vertices:
            if vertex.id == id:
                self.vertices.remove(vertex)

    def update_x_y(self,id,x,y):
      for vertex in self.vertices:
            if vertex.id == id:
              vertex.x = x
              vertex.y = y


    def visualize_graph(self, custom_figsize, radius):  # O(V + V + E) = O(2V + E) = O(V + E)

      self.place_vertices_in_circle(radius)  # O(V)

      fig, ax = plt.subplots(figsize=(custom_figsize, custom_figsize))  # Adjust width and height as needed
      # Plot Vertices
      scaling_factor = 1 / len(self.vertices)
      for vertex in self.vertices:  # O(V)
          ax.scatter(vertex.x, vertex.y, color='blue', zorder=2, s=scaling_factor * 40000 * (custom_figsize / 15),
                    edgecolors='black')
          ax.text(vertex.x, vertex.y, str(vertex.id), fontsize=(scaling_factor * 40000 * (custom_figsize / 15)) / 100,
                  ha='center', va='center', zorder=len(self.vertices) * scaling_factor * 2, color='white')
      # Plot edges with direction
      for edge in self.edges:  # O(E)
          start = edge.start
          end = edge.end
          dx = end.x - start.x
          dy = end.y - start.y
          ax.annotate("", xy=(end.x, end.y), xytext=(start.x, start.y),
                      arrowprops=dict(arrowstyle="->", linewidth=2.0, color='gray'))

      ax.set_xlabel('X')
      ax.set_ylabel('Y')
      ax.set_title('Graph Visualization with Edge Direction')
      ax.grid(True)


    def place_vertices_in_circle(self,radius): # O(V)
        num_vertices = len(self.vertices)
        radius = radius  # Radius of the circle
        center_x = 0
        center_y = 0
        angle_increment = 2 * np.pi / num_vertices

        # Place vertices in a bit of randomized circle
        for i, vertex in enumerate(self.vertices): # O(V)
            angle = i * angle_increment
            vertex.x = center_x + radius * np.cos(angle)
            vertex.y = center_y + radius * np.sin(angle)
################## classes parts 6 & 7  #####################

class FSGraph(Graph):
    def remove_edge(self, start, end):
        for edge in self.edges:
            if edge.start == start and edge.end == end:
                self.edges.remove(edge)

    def remove_vertex(self, id):
        if id in self.vertices:
            self.vertices.pop(id)

    def update_x_y(self,id,x,y):
        self.vertices[id].x = x
        self.vertices[id].y = y
    def visualize_graph(self, custom_figsize, radius):  # O(V + V + E) = O(2V + E) = O(V + E)

      self.place_vertices_in_circle(radius)  # O(V)

      fig, ax = plt.subplots(figsize=(custom_figsize, custom_figsize))  # Adjust width and height as needed
      # Plot Vertices
      scaling_factor = 1 / len(self.vertices)
      for vertex in self.vertices.values():  # O(V)
          ax.scatter(vertex.x, vertex.y, color='blue', zorder=2, s=scaling_factor * 40000 * (custom_figsize / 15),
                    edgecolors='black')
          ax.text(vertex.x, vertex.y, str(vertex.id), fontsize=(scaling_factor * 40000 * (custom_figsize / 15)) / 100,
                  ha='center', va='center', zorder=len(self.vertices) * scaling_factor * 2, color='white')
      # Plot edges with direction
      for edge in self.edges:  # O(E)
          start = self.vertices[edge.start.id]
          end = self.vertices[edge.end.id]
          dx = end.x - start.x
          dy = end.y - start.y
          ax.annotate("", xy=(end.x, end.y), xytext=(start.x, start.y),
                      arrowprops=dict(arrowstyle="->", linewidth=2.0, color='gray'))

      ax.set_xlabel('X')
      ax.set_ylabel('Y')
      ax.set_title('Graph Visualization with Edge Direction')
      ax.grid(True)
      #plt.show()
     # plt.close(fig)

################## classes parts 6 & 7  #####################

class SEdge(Edge):
    def __init__(self, start, end, weight=0):
        super().__init__(start, end) 
        self.weight = weight

################## classes part 7  #####################

class SForced_vertex(Forced_vertex):
    def __init__(self, id):
        super().__init__(id) 
        self.x = self.position[0]
        self.y = self.position[1]
