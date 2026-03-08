# gui_main.py
import tkinter as tk
from tkinter import simpledialog, messagebox
from graph import Graph
from dijkstra import dijkstra, shortest_path

# Create graph
g = Graph()

# Tkinter root window
root = tk.Tk()
root.withdraw()  # hide main window

# Get edges from user
while True:
    entry = simpledialog.askstring("Input", "Enter edge (start end weight) or type 'done':")
    if entry is None or entry.lower() == 'done':
        break
    try:
        start, end, weight = entry.split()
        weight = int(weight)
        g.add_edge(start, end, weight)
    except:
        messagebox.showerror("Error", "Invalid input! Format: start end weight")

# Get starting node
start_node = simpledialog.askstring("Input", "Enter starting node:")

# Compute shortest distances and paths
distances, previous_nodes = dijkstra(g, start_node)

# Display distances
dist_text = "Shortest distances from {}\n".format(start_node)
for node, dist in distances.items():
    dist_text += "{}: {}\n".format(node, dist)

# Display paths
dist_text += "\nShortest paths from {}\n".format(start_node)
for node in g.nodes:
    if node == start_node:
        continue
    path = shortest_path(previous_nodes, node)
    dist_text += "{} -> {}: {}\n".format(start_node, node, " -> ".join(path))

# Show output in messagebox
messagebox.showinfo("Results", dist_text)

root.mainloop()