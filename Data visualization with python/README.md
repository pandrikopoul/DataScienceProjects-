# Data Visualization Project

## Introduction
This repository contains code and datasets for a project focused on visualizing relational and high-dimensional data.

## Folder Structure
- `code/`: Contains all project code, divided into parts.
  - `part1`: Code for Step 1.
  - `part2`: Code for Step 2.
  - ...
- `data/`: Holds all datasets used in the project.

## Implementation Steps

## Step 1: Read and draw a graph

* Take a given file in edge list format, e.g. Les Misérables network, Jazz network ✅
* Load the file into your program (build data structures for that) ✅
* Create and draw a layout (node-link diagram) for the loaded graph. Feel free to imagine any kind of layout you want, e.g. some user-defined functions for the x and y coordinates. ✅
* Explain what's the computational complexity of your layout algorithm ✅
* Comment on the pros/cons of your resulting layout ✅
* (bonus) Give yourself 10 minutes to think of a simple algorithm for graph drawing that theoretically should produce results better than your previous attempt. Implement this algorithm, show your results, compare to the drawings produced by the previous algorithm, and analyze the algorithm’s running time. ✅

## Step 2: Extract and visualize trees

* Take a graph and compute a BFS and a DFS tree of it ✅
* Implement your favorite tree layout algorithm (layered, radial, bubble) ✅ (Radial)
* Analyze the time complexity of your implementation ✅
* Apply your implementation to (at least) Les Misérables network and Jazz network ✅
* Comment on the quality of your visualizations; ✅
* Compare the quality of the visualizations for the BFS and DFS, what do you observe? ✅
* Applying DFS, construct several spanning trees, using several vertices as roots, and comment how the quality of the overall visualization depends on the choice of the root. ✅
* Add the non-tree edges to the drawings and discuss the obtained pictures. ✅
* Which (other) quality metrics except for those optimized by the method implicitly or explicitly could be optimized to improve your results? (refer to bonus tasks)

## Step 3: Compute a force-directed layout

* Implement a force-directed layout; ✅
* Explain your choice of forces/parameters ✅
* Draw the result (Les Misérables network and Jazz network) ✅
* Comment on the quality of the resulting drawing; which (other) quality metrics could be optimized to improve your results?  ✅

## Step 4: Compute a layered layout

* Consider you have a directed graph ✅
* Construct a DAG (directed acyclic graph) by reversing edges - use either the trivial heuristic or the one with guarantees (Eades at al. 93) ✅
* Perform layer assignment (using height minimization) ✅
* Perform iterative crossing minimization using both median and barycenter heuristics ✅
* Assign coordinates to the vertices in any way you like and draw the edges ✅
* Reverse back the edges that have been changed in the first step ✅
* Use a Small Directed Network, Pro League Network at this step to experiment with your algorithm. ✅
* Discuss your results and explain your choices of the heuristics carefully. Feel free to use other heuristics for each step but do not forget to explain your choices. ✅

NB: you may also try to visualize the Argumentation Network, but be aware that it may be quite large for your implementation

## Step 5: Multilayer/clustered graphs and edge bundling

* Take the input graph (you can work with Argumentation Network and Political Blogosphere Network) ✅
* Consider two subgraphs of it that are typically formed by clusters (there are two big clusters in the Argumentation Network: "Youngest Devonian Strata" and "Gap in the Sequence of Devonshi") ✅
* Lay out each of the respective subgraphs using force-directed layout ✅
* Draw the resulting layouts surrounded by bounding boxes ✅
* Implement the force-directed bundling and apply it to the edges connecting nodes of the two clusters (inter-cluster edges) ✅

## Step 6: Projections for graphs

* Take the input graph (for instance Les Misérables network) ✅
* Compute similarity matrix using graph-theoretic distance ✅
* Project it using at least two different projections (MDS, t-SNE, ISOMAP) ✅ ( MDS, t-SNE)
* Draw the resulting layouts ✅
* Compare/discuss the obtained layouts and parameter choices ✅

## Step 7: Quality measurement of graph projections

* Take the input graph (Les Misérables network, Jazz network, League network) ✅
* Take the layouts computed by force-directed, layered, projection ✅
* Draw these layouts side by side ✅
* Compute the quality metrics (graph-related (crossing number, crossing resolution, stress of layout), projection-related (continuity, trustworthiness, stress, Shepard)) ✅
* Compare and discuss the results (and argue about which of the layouts YOU prefer) ✅
  
## Additional bonus tasks on all steps

You can choose to implement any number of the following tasks.

* Consider the three algorithms you implemented (Steps 2-4). Apply your implementations to graphs of various sizes. Pick three sizes that make sense for each implementation, explain your choices. Discuss how your implementations and parametrizations scale. See the reference on the Datasets page for more graph instances. Note that this step may require you to be able to read other graph formats beyond simple edge lists.
* Return to the tree layout. Which quality metric can be additionally optimized to improve the layouts your have constructed? Implement a suggested improvement and evaluate the results.
* Return to the force-directed algorithm. Implement the speed-up of computing repulsive forces using quad-tree. Measure the time that the layout algorithm takes for N iterations with and without speed up. Discuss your results.
* Return to the layered layout. Implement the step of node positioning using quadratic programming. Get creative: propose your own method for node positioning. Compare the results.
* Return to the layered layout. Implement drawing of the edges using curves (e.g. splines or any other choice of yours) to improve the quality of the result. You can check yEd on how the final drawings may look like.✅
* Return to the multilayer/clustered graphs visualization. Expand your method to work for more than two clusters. For this, you need to find a way to arrange an arbitrary number of boxes (containing layouts of the layers) next to each other. We do not recommend just to stack them vertically or horizontally. ✅
* Return to your edge-bundling implementation. Implement the Gaussian smoothing to make your bundles look better.

## Project Report
- `Data_Visualization_Final_Hochman_Psara_Andrikopoulos.pdf`: The project report contains detailed descriptions of all the steps outlined in the implementation section, including objectives, methodology, results, and conclusions.
