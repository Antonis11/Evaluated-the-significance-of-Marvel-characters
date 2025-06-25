# Evaluated-the-significance-of-Marvel-characters

This project analyzes the importance of Marvel heroes using the **PageRank** algorithm.  
Heroes are represented as **nodes** in an undirected graph, where an **edge** exists if two heroes appear in the same comic.

## 🔧 Implementation Details

- Build the **adjacency matrix** from the dataset.
- Create the **normalized adjacency matrix**.
- Use the **transpose** of the normalized matrix to compute PageRank scores.
- Apply a **damping factor (0.85)** to:
  - Simulate random teleportation between nodes,
  - Handle disconnected nodes,
  - Avoid infinite loops,
  - Improve numerical stability.

The PageRank algorithm runs for **10 iterations**, after which the top heroes remain stable.

## 🚀 How to Run

In the terminal:

```bash
python pagerank.py
# or
python3 pagerank.py
```

This will output the top 10 most important Marvel heroes based on their PageRank scores.


