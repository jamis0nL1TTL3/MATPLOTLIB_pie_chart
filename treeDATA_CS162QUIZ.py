# Build a family tree using your class. The tree should include at least 3 generations and 6 family members total.
# Implement a recursive function to print all names in the tree (preorder traversal).
# Implement a search function that takes a name as input and returns whether that person exists in the tree.
# (Bonus): Add a method to print the tree with indentation to show the structure (e.g., child nodes indented)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child (self, child):
        child.parent = self
        self.children.append(child)

    def get_level (self):
        level = 0
        ancestor = self.parent
        while ancestor:
            level += 1
            ancestor = ancestor.parent
        return level

    def print_tree(self):
        spaces = '  ' * self.get_level() * 3

        print (spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def search_tree(self, target_name):
        if self.data == target_name:
            return True
        for child in self.children:
            if child.search_tree(target_name):
                return True
        return False

def build_family_tree():
    root = TreeNode("Jorgen")

    giuseppe = TreeNode("Giuseppe")
    giuseppe.add_child(TreeNode("Neol"))
    giuseppe.add_child(TreeNode("Paul"))

    chigs = TreeNode("Chigs")
    chigs.add_child(TreeNode("Puck"))
    chigs.add_child(TreeNode("Carlie"))
    chigs.add_child(TreeNode("Boots"))

    root.add_child(giuseppe)
    root.add_child(chigs)

    return root

if __name__ == '__main__':
    root = build_family_tree()
    root.print_tree()
    find_member = input("Please enter a name to search for: ").capitalize()
    if root.search_tree(find_member):
        print (f"{find_member} is in the family tree!")
    else:
        print (f"{find_member} is not in the family tree :(")



