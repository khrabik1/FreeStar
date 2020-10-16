#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:12:24 2020

@author: katherynhrabik
"""
import sys

class Neighboring_Nodes:
    
    def __init__(self, size, debug):
        
        self.size = self.initialize_size(size)
        
        #No default set for debug mode at this time
        self.debug = debug
        
        #Blank array to initialize grid
        self.grid = []
        
           
    def initialize_size(self, size):
        #This method ensures that the user passed an appropriate size for the grid.
        #If 0 is passed, a message is pressed and the system exits completely.
        #If a negative is passed, the number is inverted.
        
        if size > 0:
            return round(size)
        elif size == 0:
            print("Cannot initialize grid with value 0. Try running again.")
            sys.exit(0)
        else:
            print("A negative number was passed in. Inverting.")
            return -size
        
        
    def construct_grid(self):
        #Creates a blank grid, then creates a single node for each location in it
        #This fulfills problem #1 and allows debug mode to run when requested
        
        self.grid = [[0 for column in range(self.size)]
                        for row in range(self.size)]
        
        #Create coordinates for entire grid
        coords = [(i,j) for i, n in enumerate(self.grid) for j, n2 in enumerate(n)]
        
        #Initialize index
        index = 1
        
        #Indexing left to right instead of up and down
        #NOTE: Index starts at 1 rather than 0
        coords.sort(key=lambda x: x[1])
        
        #Assigning each node to its place in the grid
        for val in coords:
            self.grid[val[0]][val[1]] = Node(val, index)
            index += 1
            
        #Prints once when grid is drawn, assuming debug mode = True
        if self.debug == True:
            print("DEBUG MODE: Printing (x,y,i) data for all Nodes")
            #Note, This will print in COORDINATE order, not necessarily index order.
            for row in self.grid:
                for node in row:
                    print("Coordinates: " + str(node.coords) + ", Index: " + str(node.index))
        
        
    #This method handles any number of arguments passed BY NAME
    def find_neighbors(self, neighborhood_type, *args, **kwargs):
        
        coords = kwargs.get('coords', None)
        index = kwargs.get('index', None)
        #If M is not passed, m defaults to 1
        m = kwargs.get('m', 1)
        
        #If M is outside the desired range (aka 0 < m <= self.size/2)
        #M will, again, be defaulted to 1
        if m < 0 or m > self.size//2:
            print("Given 'm' value is outside of range. Defaulting to 1. Please review")
            m = 1
            
        #All drawing methods are based on coordinates
        #If only an index is passed, the coordinates corresponding to the index
        #are passed back
        
        coordinates = self.select_mode(coords, index)
        
        #Basic switch based on neighborhood type
        if(neighborhood_type == 'Square'):
            alls = set(self.square_method(coordinates,m))
        elif(neighborhood_type == 'Diamond'):
            alls = set(self.diamond_method(coordinates,m))
        elif(neighborhood_type == 'Cross'):
            alls = set(self.cross_method(coordinates,m))
        
        #Creates a visual representation of the pattern
        self.visual_representation(alls, coords)
        
        
    def select_mode(self, coords, index):
        #This method allows us to use the passed values we desire, without
        #stopping the find_neighbors method from accepting all of them
        #If neither are passed, the system prints a message and exits
        #If a. both are passed, or b. just index is passed, the default is 
        #to pass back the coordinates associated with the given index.
        
        if coords is None and index is None:
            print("Need to pass either coordinates or index. Run function again.")
            sys.exit(0)
        
        elif index is None:
            return coords
            
        else:
            for row in self.grid:
                for item in row:
                    if item.index == index:
                        return item.coords
        
    
    def visual_representation(self, alls, coords):
       #This automatically prints the pattern requested
       #Was not a requirement, but I thought might be helpful for testing
       drawing_grid = [[0 for column in range(self.size)] 
                        for row in range(self.size)]
       
       for u in range(self.size):
           for v in range(self.size):

               if (u,v) in alls:
                   drawing_grid[v][u] = 1
      
       for row in drawing_grid:
           print(row)
           
           
     #THE DESIGN METHODS: Cross, Square, Diamond
     #All based on positional locations
     #ASSUMPTION 1: I fill in the origin coordinate as well as the rest of
     #the pattern
     #ASSUMPTION 2: to handle coordinates "falling off" the edges, I allow
     #the original origin to be used, and anything outside the grid will not be
     #saved. Due to this, if you choose an origin near the edge of the grid,
     #you will get part of the total design (i.e. half a diamond) without
     #any errors and without any negative coordinates saving.

    def cross_method(self, coords, m):
        
        alls = []
        
        alls.append(coords)
        
        for i in range (1,m+1):
            if (coords[0]-i >= 0):
                alls.append((coords[0]-i, coords[1]))

            if coords[0] + i <= self.size-1:
                alls.append((coords[0]+i, coords[1]))
                
            if  (coords[1] + i <= self.size-1):
                alls.append((coords[0], coords[1]+i))

            if  (coords[1] -1 >= 0):
                alls.append((coords[0], coords[1]-i))
                
                
         
        return alls
    
    def square_method(self, coords, m):
        
        alls = []
        
        alls.append(coords)
        
        for i in range (1, m+1):
            if (coords[0] -i >= 0):
                alls.append((coords[0]-i, coords[1]))
                for j in range(1, m+1):
                    if (coords[1] - j >= 0) & (coords[1]-i <= self.size-1):
                        alls.append((coords[0] - i, coords[1] - i))
                        alls.append((coords[0] - i, coords[1] - j))

            if (coords[0] + i <= self.size-1):
                alls.append((coords[0]+i, coords[1]))
                for j in range(1, m+1):
                    if (coords[1] + j <= self.size-1):
                        alls.append((coords[0] + i, coords[1] + j))    
                    
            if  (coords[1] + i <= self.size-1):
                alls.append((coords[0], coords[1]+i))
                for j in range(1, m+1):
                    if (coords[0] -j >= 0):
                        alls.append((coords[0] - j, coords[1] + i))
            
            if  (coords[1] -1 >= 0):
                alls.append((coords[0], coords[1]-i))
                for j in range(1, m + 1):
                    if (coords[0] + j <= self.size):
                        alls.append((coords[0] + j, coords[1] - i))
                    
                
        
        return alls
    
    def diamond_method(self,coords,m):
        
        alls = []
        
        alls.append(coords)
        
        for i in range (1,m+1):
            if (coords[0]-i >= 0):
                alls.append((coords[0]-i, coords[1]))

            if coords[0] + i <= self.size-1:
                alls.append((coords[0]+i, coords[1]))
                
            if  (coords[1] + i <= self.size-1):
                alls.append((coords[0], coords[1]+i))

            if  (coords[1] -1 >= 0):
                alls.append((coords[0], coords[1]-i))
        
        for i in range(self.size-1):
            for j in range(1, self.size-1):
                if (abs((i - coords[0])) + abs((j-coords[1])) <= m):
                    alls.append((abs((coords[0]+i)) - coords[0], abs((coords[1]+j)) - coords[1]))
                    
        
        return alls


# (Extremely basic) node class
class Node:
    
    def __init__(self, coords, index):
        self.coords = coords
        self.index = index


##########################Sample Driver Code###################################

#Create the grid (problem #1)        
testgrid = Neighboring_Nodes(8, False)
testgrid.construct_grid()

#You can pass any arguments you want - the only required is the neighborhood type
#('Diamond', 'Cross', 'Square')
#PLEASE NOTE: if you omit both coordinates and index, the system will exit.
#Also, if you omit m, it defaults to 1.
#Also helpful: indexes go left to right and start at 1, so the end of the first row is
#index 8.
testgrid.find_neighbors('Diamond', coords=(4,4), index=37, m=2)


###############################################################################









