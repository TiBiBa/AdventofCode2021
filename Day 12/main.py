class Node:

    def __init__(self, name):
        self.neighbours = set()
        self.name = name

    def get_name(self):
        return self.name

    def add_neighbour(self, neighbour):
        self.neighbours.add(neighbour)

    def get_neighbours(self):
        return self.neighbours


def walk_unique(nodes, current_node, route, routes):
    route = route.copy()
    route.append(current_node)
    for neighbour in nodes[current_node].get_neighbours():
        if neighbour == "end":
            route.append("end")
            routes.append(route)
        elif neighbour not in route or not neighbour.islower():
            walk_unique(nodes, neighbour, route, routes)


def create_nodes():
    nodes = {}

    file = open("input.txt", "r")
    edges = file.read().splitlines()
    for edge in edges:
        edge_nodes = edge.split("-")
        for node in edge_nodes:
            if node not in nodes:
                nodes[node] = Node(node)
        nodes[edge_nodes[0]].add_neighbour(edge_nodes[1])
        nodes[edge_nodes[1]].add_neighbour(edge_nodes[0])
    return nodes


def step1():
    nodes = create_nodes()
    start_route = ['start']
    routes = []
    for neighbour in nodes['start'].get_neighbours():
        walk_unique(nodes, neighbour, start_route, routes)
    print(len(routes))


def lower_duplicate_allowed(route):
    for node in route:
        if node.islower() and route.count(node) > 1:
            return False
    return True


def walk_twice(nodes, current_node, route, routes):
    route = route.copy()
    route.append(current_node)
    for neighbour in nodes[current_node].get_neighbours():
        if neighbour == "end":
            routes.append(route + ["end"])
        elif neighbour not in route or neighbour.isupper():
            walk_twice(nodes, neighbour, route, routes)
        elif neighbour != "start" and lower_duplicate_allowed(route):
            walk_twice(nodes, neighbour, route, routes)


def step2():
    nodes = create_nodes()
    start_route = ['start']
    routes = []
    for neighbour in nodes['start'].get_neighbours():
        walk_twice(nodes, neighbour, start_route, routes)
    print(len(routes))

step2()