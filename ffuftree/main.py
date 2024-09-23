import json
import sys
from anytree import Node, RenderTree

def gen_path_tree(json_data, target):
    root = Node(target)
    paths = [item['url'] for item in json_data['results']]

    for path in paths:
        jump_protocol = path.split('://')[0]
        if jump_protocol == 'https':
            path = path.split('://')[1]

        if path.startswith('/'):
            path = path[1:]
            
        parts = path.split('/')
        parts = [p for p in parts if p]  # Remove empty elements

        current_node = root
        for part in parts:
            child = next((c for c in current_node.children if c.name == part), None)
            if not child:
                child = Node(part, parent=current_node)
            current_node = child

    return root

def print_tree(root):
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")

def main():
    # Read JSON from standard input
    json_data = json.load(sys.stdin)

    # Create the tree
    root = gen_path_tree(json_data, sys.argv[1])

    # Print the tree
    print_tree(root)

if __name__ == "__main__":
    main()
