import pandas as pd
import numpy as np

csv_file = "marvel.csv"
data = pd.read_csv(csv_file, header=None, names=["source", "target"])

reversed_data = data.rename(columns={"source": "target", "target": "source"})
full_data = pd.concat([data, reversed_data])

nodes = sorted(list(set(full_data['source']).union(set(full_data['target'])))) 
num_nodes = len(nodes)
#print(num_nodes)

node_indices = {node: i for i, node in enumerate(nodes)}

adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

for _, row in full_data.iterrows():
    source_idx = node_indices[row['source']]
    target_idx = node_indices[row['target']]
    adj_matrix[source_idx, target_idx] = 1

adj_matrix_df = pd.DataFrame(adj_matrix, index=nodes, columns=nodes)

row_sums = adj_matrix.sum(axis=1, keepdims=True)
row_sums[row_sums == 0] = 1  # Avoid division by 0
normalized_adj_matrix = adj_matrix / row_sums

normalized_adj_matrix_df = pd.DataFrame(normalized_adj_matrix, index=nodes, columns=nodes)
normalized_adj_matrix_df = normalized_adj_matrix_df.T

pagerank_vector = np.full((num_nodes, 1), 1 / num_nodes)

depreciation = 0.85

for iteration in range(10): 
    pagerank_vector = depreciation * (normalized_adj_matrix_df.values @ pagerank_vector) + (1-depreciation) * (1 / num_nodes)
    
    #print(f"Iteration {iteration + 1}:")
    #intermediate_scores = pd.DataFrame(
        #pagerank_vector, index=nodes, columns=["PageRank Score"]
    #)
    #print(intermediate_scores.sort_values(by="PageRank Score", ascending=False).head(10)) 

pagerank_scores = pd.DataFrame(
    pagerank_vector, index=nodes, columns=["PageRank Score"]
)

pagerank_scores = pagerank_scores.sort_values(by="PageRank Score", ascending=False)

heroes = list(set(data['source'])) 
num = len(heroes)
#print(num)

hero_scores = pagerank_scores.loc[heroes].sort_values(by="PageRank Score", ascending=False)

top_10_scores = hero_scores.head(10)

print("Top 10 PageRank Scores:")
for i, row in top_10_scores.iterrows():
    print(f"{i}, PageRank Score: {row['PageRank Score']:.6f}")    

#adj_matrix_df.to_csv("adjacency_matrix.csv")
#normalized_adj_matrix_df.to_csv("normalized_adjacency_matrix_transposed.csv")

