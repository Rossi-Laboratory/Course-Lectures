# HW1 - Greedy Best-First Search

Instructor: YuanFu Yang  
Email: yfyangd@nycu.edu.tw  
Course: IIAI30017 - Artificial Intelligence

---

## Assignment Information
- **Due date:** 10/7  
- **Late penalty:** 1 point deduction per day late.  
- **Maximum extension:** 3 days (submissions later than this will not be accepted).  
- **Submission format:**  
  - Code (`.ipynb`)  
  - Report (answers to 4 questions) in **PDF**  
- **Execution environment:** Google Colab or local PC.  
  - Colab link: [Google Colab](https://colab.research.google.com/?hl=zh-tw)

---

## Assignment Description

### Task
Design a **Greedy Best-First Search** algorithm for the **shortest path problem** on the European railway network.  

- Each **node** represents a station.  
- Each **edge** represents the straight-line distance between stations.  
- The **goal** is to find the optimal path from a starting station to the destination station **Bucharest**.

### Heuristic
The heuristic function is defined as the straight-line distance from each station to the destination (Bucharest).  
Use this heuristic to perform Greedy Best-First Search.

### Provided Data
- A European railway network graph  
- Distances between stations  
- Straight-line distances from each station to Bucharest

---

## Plan-to-Do
- Implement and refine a function:
  ```python
  greedy_best_first_search(start, goal)
  ```
- Perform route planning from:
  - **Arad → Bucharest** (Q1)  
  - **Oradea → Bucharest** (Q2)  
  - **Mehadia → Bucharest** (Q2)  

---

## Questions
1. Provide the route planning from **Arad** to **Bucharest**.  
2. Provide the route planning from **Oradea** and **Mehadia** to **Bucharest**.  
3. Discuss the **pros and cons** of Greedy Best-First Search.  
4. Suggest possible **improvements** to address its disadvantages.  

---

## Notebook Implementation

The following Python code implements the Greedy Best-First Search algorithm and prepares the testing cases.

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

---

## Contact
For questions regarding this assignment:  
**Instructor:** YuanFu Yang  
**Email:** yfyangd@nycu.edu.tw
