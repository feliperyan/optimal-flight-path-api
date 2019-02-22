# Optimal Flight Path API server

This is a simple API server which receives a json with a list of coordinates and calculates the optimal path to travel between all points and an origin point. It's used in conjunction with this repo: https://github.com/feliperyan/lwc-drone-delivery

Look at the example_inbound and example_outbound for what the API endpoint expects and outputs.


<img src="./GoogleAI_logo_small.png" alt="Google OR Tools" width="100"/>

This repo uses the Google OR Tools library. Google OR Tools is an open source software suite for optimization, tuned for tackling the world's toughest problems in vehicle routing, flows, integer and linear programming, and constraint programming.
More information https://developers.google.com/optimization/routing/tsp