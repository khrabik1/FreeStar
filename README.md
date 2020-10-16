# FreeStar

Neighboring_Nodes:

- General Notes
  - Driver Code included at bottom of file
  - Written in Python
  - Designed to print a visualization for ease of testing
  - Very heavily commented to make logic clear for design choices
  
- ASSUMPTIONS AND DESIGN CHOICES:
  - No default is set for debug mode. True or False must be passed in.
  - Regarding print of coordinates: they print in COORDINATE order rather than INDEX order. Indices are assigned left to right, top to bottom, (as we read) to facilitate easy counting
  - Any number can be passed for "size", but this is checked before the grid is initialized. If the number passed is 0, the system will print a message and exit. If the number is negative, it will automatically invert (-3 will become 3). Also, the user can pass in a float as a size (like 7.8) - it will round to the nearest whole integer.
  - The "find neighbors" method can take any number of arguments. Only the neighborhood type is explicitly required. If you don't pass coordinates or an index, the system will alert you to try again and exit. If you pass both, it will default to index. If you don't pass m (neighborhood size), m defaults to 1.
  - If an improper m value is sent (i.e not 0 < m <= size/2), m will default to 1 and the user will be alerted
  - SPECIAL CASES: If an origin coordinate that does not exist is passed, you will be sent a blank canvas. If an index that does not exist is passed, origin defaults to (0,0)
  - In the case that the origin is too close to the edge for a full diagram (i.e. with part of it "falling off" the edges), I do not move to a different origin point. Rather, I allow the image to fall off. This does NOT save out-of-boundary coordinates, nor does it bomb out. It is simply an error handling design choice.
  - For example, a "Diamond" with an origin point near an edge will return something like this (below)
  
  [0 0 0 0 0 0]
  [1 0 0 0 0 0]
  [1 1 0 0 0 0]
  [1 0 0 0 0 0]
  [0 0 0 0 0 0]
  
  - The origin and the rest of the design (cross, diamond, square) are marked with '1' for visualizations. the rest of the grid is marked with '0'
  
  SQL Challenge:
  
  - I wanted to stay away from any "flavor" specific language as much as possible, so this is written in "straight sql" and will most likely run in any sql server, but for reference (if there's an issue) I'm using MySQL.
  
