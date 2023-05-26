# Hint: You can use any path-finding or union-search algorithm for this mission.

# https://py.checkio.org/mission/find-friends/solve/
# tu znajdziesz rysunki do testow

import collections


def bfs(graph, start, goal):
    if start == goal:
        return True
    visited, queue = set(), collections.deque([(start, [])])
    while queue:
        current, path = queue.popleft()
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == goal:
                print(path + [current, neighbor])
                return True
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)
    return False


def check_connection(network, first, second):
    # prepare graph representation
    graph = dict()
    for n in network:
        n1, n2 = n.split("-")
        try:
            graph[n1].add(n2)
        except KeyError:
            graph[n1] = set()
            graph[n1].add(n2)
        try:
            graph[n2].add(n1)
        except KeyError:
            graph[n2] = set()
            graph[n2].add(n1)
    return bfs(graph, first, second)


if __name__ == "__main__":
    assert (
        check_connection(
            (
                "dr101-mr99",
                "mr99-out00",
                "dr101-out00",
                "scout1-scout2",
                "scout3-scout1",
                "scout1-scout4",
                "scout4-sscout",
                "sscout-super",
            ),
            "scout2",
            "scout3",
        )
        is True
    ), "Scout Brotherhood"
    assert (
        check_connection(
            (
                "mr99-cat",
                "mega-mr99",
            ),
            "cat",
            "mr99",
        )
        is True
    )
    assert (
        check_connection(
            (
                "cat-super",
                "cat-nikola",
                "nikola-super",
            ),
            "nikola",
            "super",
        )
        is True
    )
    check_connection(
        (
            "dr101-mr99",
            "mr99-out00",
            "dr101-out00",
            "scout1-scout2",
            "scout3-scout1",
            "scout1-scout4",
            "scout4-sscout",
            "sscout-super",
        ),
        "scout2",
        "scout3",
    ) is True
    assert (
        check_connection(
            (
                "dr101-mr99",
                "mr99-out00",
                "dr101-out00",
                "scout1-scout2",
                "scout3-scout1",
                "scout1-scout4",
                "scout4-sscout",
                "sscout-super",
            ),
            "super",
            "scout2",
        )
        is True
    )
    assert (
        check_connection(
            (
                "dr101-mr99",
                "mr99-out00",
                "dr101-out00",
                "scout1-scout2",
                "scout3-scout1",
                "scout1-scout4",
                "scout4-sscout",
                "sscout-super",
            ),
            "dr101",
            "sscout",
        )
        is False
    )


"""
Sophia's drones are not soulless and stupid drones; they can make and have friends. 
In fact, they already are working for the their own social network just for drones! 
Sophia has received the data about the connections between drones and she wants to know more about relations between them.

We have an array of straight connections between drones. 
Each connection is represented as a string with two names of friends separated by hyphen. 
For example: "dr101-mr99" means what the dr101 and mr99 are friends. 
Your should write a function that allow determine more complex connection between drones. 
You are given two names also. Try to determine if they are related through common bonds by any depth. 
For example: if two drones have a common friends or friends who have common friends and so on.

network
Let's look at examples:
scout2 and scout3 have the common friend scout1 so they are related. 
super and scout2 are related through sscout, scout4 and scout1. 
But dr101 and sscout are not related.

Input: Three arguments: Information about friends as a tuple of strings; first name as a string; second name as a string.

Output: Are these drones related or not as a boolean.

Example:

check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3") == True
check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False

How it is used: This concept will help you find not too obvious connections with the building of bond networks. And how to work social networks.

Precondition: len(network) ≤ 45
if "name1-name2" in network, then "name2-name1" not in network
3 ≤ len(drone_name) ≤ 6
first_name and second_name in network.
"""


def check_connection(network, first, second):
    network_first = [first]
    i = 0
    while True:
        name_current = network_first[i]
        for conn in network:
            name1, name2 = conn.split("-")
            if name1 == name_current and name2 not in network_first:
                network_first.append(name2)
            if name2 == name_current and name1 not in network_first:
                network_first.append(name1)
        i += 1
        if i == len(network_first):
            break
    return True if second in network_first else False


def check_connection(network, first, second):
    nodes = {n: set() for net in network for n in net.split("-")}

    for n in network:
        k, v = n.split("-")
        nodes[k].add(v)
        nodes[v].add(k)

    def find_path(nodes, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in nodes:
            return None
        for node in nodes[start]:
            if node not in path:
                newpath = find_path(nodes, node, end, path)
                if newpath:
                    return newpath
        return None

    return False if not find_path(nodes, first, second) else True
