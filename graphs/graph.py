class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self) -> Node | None:
        return self.head_node

    def is_empty(self) -> bool:
        if self.head_node is None:
            return True
        else:
            return False

    def insert_at_head(self, node: Node) -> Node:
        # O(1)
        if not self.is_empty():
            node.next_node = self.head_node
        self.head_node = node
        return self.head_node

    def insert_at_tail(self, node: Node) -> Node:
        # O(n)
        if self.is_empty():
            self.head_node = node
            return
        tmp = self.head_node
        while tmp.next_node is not None:
            tmp = tmp.next_node
        tmp.next_node = node

    def length(self) -> int:
        # O(n)
        len = 0
        current = self.head_node
        while current is not None:
            len += 1
            current = current.next_node
        return len

    def delete_at_head(self):
        if self.is_empty():
            return
        curr = self.head_node
        self.head_node = curr.next_node
        curr.next_node = None

    def delete(self, value) -> bool:
        # find vlaue and re-link node.
        # single case
        # multiple case
        deleted = False
        if self.is_empty():
            return deleted
        current_node = self.get_head()
        previous_node = None
        if current_node.data is value:
            self.delete_at_head()
            deleted = True
            return deleted

        # single node
        while current_node is not None:
            if current_node.data is value:
                previous_node.next_element = current_node.next_node
                current_node.next_node = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next_node
        return deleted

    def search(self, value):
        if self.is_empty():
            return None
        current_node = self.head_node
        while current_node is not None:
            if current_node.data is value:
                return current_node
            current_node = current_node.next_node
        return None


class DirectedGraph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adjacent_vertices = {key: LinkedList() for key in range(num_vertices)}

    def add_edge(self, source: int, destination: int):
        if source < self.num_vertices and destination < self.num_vertices:
            self.adjacent_vertices[source].insert_at_tail(destination)


class UndirectedGraph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adjacent_vertices = {key: LinkedList() for key in range(num_vertices)}

    def add_edge(self, source: int, destination: int):
        if source < self.num_vertices and destination < self.num_vertices:
            self.adjacent_vertices[source].insert_at_tail(destination)
            self.adjacent_vertices[destination].insert_at_tail(source)
