from Node import Knot, Queue, Stack
import copy

root = Knot(1)
root.left = Knot(2)
root.right = Knot(3)
root.left.left = Knot(4)
root.left.right = Knot(5)
root.right.left = Knot(6)
root.right.right = Knot(7)
root.left.left.left = Knot(8)
# root.left.left.right = Knot(9)

root.parent = None
root.left.parent = root
root.right.parent = root
root.left.left.parent = root.left
root.left.right.parent = root.left
root.right.left.parent = root.right
root.right.right.parent = root.right
root.left.left.left.parent = root.left.left


def traverse_queue(top):
    if top is None:
        return

    queue = Queue()
    queue.appending(top)

    while queue.length() != 0:
        node = queue.first_item()
        node.to_show()
        if node.left:
            queue.appending(node.left)
        if node.right:
            queue.appending(node.right)


def traverse_stack(top):
    if top is None:
        return
    stack = Stack()
    stack.insert(top)
    while stack.length() != 0:
        node = stack.pop()
        node.to_show()
        if node.right:
            stack.insert(node.right)
        if node.left:
            stack.insert(node.left)


print(f'Levels:')
traverse_queue(root)
print(f'Preorder:')
traverse_stack(root)

print()


def ancestors(descendant, tree, to_help=Stack()):
    node = tree
    to_help.insert(node)

    while to_help.length() != 0:
        node = to_help.pop()
        if node.data == descendant:
            return node
        if node.right:
            to_help.insert(node.right)
        if node.left:
            to_help.insert(node.left)

    print("This leaf does not belong to this tree!")
    return None


def creating_new_tree(descendant):
    current_node = descendant
    new_tree = Knot(current_node.data)
    new_root = new_tree

    if current_node.right and current_node.left:
        print(f"It is not possible to create a new tree with node = {current_node.data}, choose another one!")
        return

    while True:

        parent = current_node.parent

        if parent.right is current_node:
            new_root.left = Knot(current_node.parent.data)

            if current_node.right:
                new_root.right = copy.deepcopy(current_node.right)

            elif current_node.left:
                new_root.right = copy.deepcopy(current_node.left)

            new_root = new_root.left
            parent.right = None

        elif parent.left is current_node:
            new_root.right = Knot(current_node.parent.data)

            if current_node.right:
                new_root.left = copy.deepcopy(current_node.right)

            elif current_node.left:
                new_root.left = copy.deepcopy(current_node.left)

            new_root = new_root.right
            parent.left = None

        current_node = current_node.parent

        if current_node.left:
            new_root.left = copy.deepcopy(current_node.left)

        elif current_node.right:
            new_root.right = copy.deepcopy(current_node.right)

        if current_node.parent is None:
            return new_tree


wanted_child = ancestors(int(input("Pass leaf's number: ")), root)
if wanted_child is not None:
    new_tree_to_show = creating_new_tree(wanted_child)
    traverse_queue(new_tree_to_show)

