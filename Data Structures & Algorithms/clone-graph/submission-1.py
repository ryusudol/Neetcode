class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        head = Node(node.val)
        store = { node.val: head }
        queue = deque([(head, node)])
        while queue:
            new_node, cur_node = queue.popleft()
            for cur_neighbor in cur_node.neighbors:
                cur_val = cur_neighbor.val
                if cur_val not in store:
                    new_neighbor = Node(cur_val)
                    new_neighbor.neighbors.append(new_node)
                    new_node.neighbors.append(new_neighbor)
                    queue.append((new_neighbor, cur_neighbor))
                    store[cur_val] = new_neighbor
                else:
                    if new_node not in store[cur_val].neighbors:
                        store[cur_val].neighbors.append(new_node)
                    if store[cur_val] not in new_node.neighbors:
                        new_node.neighbors.append(store[cur_val])
        return head