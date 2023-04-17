# Graph Isomorphism Python Project

This zip file contains our implementation of algorithms to solve the graph isomorphism and automorphism problems.

## Usage
To use the graph isomorphism algorithm, you can run the main.py script.

You can run the script with the following command:

```python
python main.py [PATH_TO_DIRECTORY]
```

Where `PATH_TO_DIRECTORY` is the path to the directory containing the graphs you want to solve. This argument is optional, and if it is not provided, the script will run on a default `./input/` directory in the same directory as the script.

The main.py script will run output a different output for each file in the directory depending on the name of the file.

- If the file name only contains the word "GI", then the script will only print the equivalence classes of the graphs in the file. 
- If the file name contains the words "GI" and "Aut", then the script will print the equivalence classes and the number of automorphisms for each class.
- If the file name contains only the word "Aut", then the script will only print the number of automorphisms for each graph in the file.
