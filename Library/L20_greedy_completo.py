import heapq
from functools import total_ordering

@total_ordering
class HuffmanNode:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self._build_repr()) 

    def _build_repr(self):  
        if self.symbol is not None:
            return {self.symbol: ""}
        else:
            left_encoding = self.left._build_repr()
            right_encoding = self.right._build_repr()
            return {
                **{key: "0" + value for key, value in left_encoding.items()},
                **{key: "1" + value for key, value in right_encoding.items()},
            }

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency


def recursive_activity_selection(start, finish, n):
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    selected_activities = []

    def select_activities(k, n):
        m = k + 1
        while m < n and activities[m][0] < activities[k][1]:
            m += 1
        if m < n:
            selected_activities.append(activities[m])
            select_activities(m, n)

    if n > 0:
        selected_activities.append(activities[0])
        select_activities(0, n)
    return selected_activities


def greedy_activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    n = len(activities)
    selected = [activities[0]]
    last_finish = activities[0][1]

    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]
    return selected


def recursive_fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)

    def knapsack_helper(i, capacity):
        if i >= len(items) or capacity <= 0:
            return 0, []
        weight, value = items[i]
        if weight <= capacity:
            val, chosen = knapsack_helper(i + 1, capacity - weight)
            return val + value, [(weight, value)] + chosen
        else:
            fraction = capacity / weight
            return value * fraction, [(weight, value * fraction)]

    return knapsack_helper(0, capacity)


def greedy_fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0.0
    selected_items = []

    for weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
            selected_items.append((weight, value))
        else:
            fraction = capacity / weight
            total_value += value * fraction
            selected_items.append((weight, value * fraction))
            break
    return total_value, selected_items


def recursive_huffman_coding(symbols, frequencies):
    nodes = [HuffmanNode(s, f) for s, f in zip(symbols, frequencies)]

    def build(nodes):
        if len(nodes) == 1:
            return nodes[0]
        nodes.sort()
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged = HuffmanNode(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        nodes.append(merged)
        return build(nodes)

    return build(nodes)._build_repr()


def iterative_huffman_coding(symbols, frequencies):
    heap = [HuffmanNode(s, f) for s, f in zip(symbols, frequencies)]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]._build_repr()


if __name__ == "__main__":
    # Activity Selection Problem
    start_times = [1, 3, 0, 5, 8, 5]
    finish_times = [2, 4, 6, 7, 9, 9]
    n = len(start_times)

    result = recursive_activity_selection(start_times, finish_times, n)
    print("Activity Selection (Recursive):", result)

    result = greedy_activity_selection(start_times, finish_times)
    print("Activity Selection (Greedy):", result)

    # Fractional Knapsack
    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50

    result, selected_items = recursive_fractional_knapsack(items, capacity)
    print("Fractional Knapsack (Recursive): Max value:", result, "Selected items:", selected_items)

    result, selected_items = greedy_fractional_knapsack(items, capacity)
    print("Fractional Knapsack (Greedy): Max value:", result, "Selected items:", selected_items)

    # Huffman Codes
    symbols = ["A", "B", "C", "D", "E"]
    frequencies = [45, 13, 12, 16, 9]

    root_recursive = recursive_huffman_coding(symbols, frequencies)
    print("Huffman Coding (Recursive):", root_recursive)

    root_iterative = iterative_huffman_coding(symbols, frequencies)
    print("Huffman Coding (Iterative):", root_iterative)
