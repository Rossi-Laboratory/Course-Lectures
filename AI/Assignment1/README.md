```python
import heapq

# 節點類別，用於儲存當前狀態
class Node:
    def __init__(self, city, heuristic, parent=None):
        self.city = city  # 當前城市
        self.heuristic = heuristic  # 啟發函數的值（到達 Bucharest 的直線距離）
        self.parent = parent  # 父節點

    def __lt__(self, other):
        return self.heuristic < other.heuristic  # 比較啟發函數值，選擇 h 值最小的節點

# 啟發函數，根據給定城市返回到 Bucharest 的直線距離
heuristics = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

# 城市之間的連接與直線距離
graph = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# 重建從起點到終點的路徑
def reconstruct_path(node):
    path = []
    while node is not None:
        path.append(node.city)
        node = node.parent
    return path[::-1]  # 反轉路徑，從起點到終點

# Greedy Best-First Search 演算法
def greedy_best_first_search(start, goal):
  # TODO: Reconstruct the path using function of reconstruct_path()
    return None  # 沒有找到解決方案

# 從Arad到Bucharest的路徑
path = greedy_best_first_search('Arad', 'Bucharest')
print("Path from Arad to Bucharest:", path)
```

```python
# 從Oradea到Bucharest的路徑
path = greedy_best_first_search('Oradea', 'Bucharest')
print("Path from Oradea to Bucharest:", path)
```

```python
# 從Mehadia到Bucharest的路徑
path = greedy_best_first_search('Mehadia', 'Bucharest')
print("Path from Mehadia to Bucharest:", path)
```