#!/usr/local/bin/python3

class HuffmanNode(object):
    def __init__(self, left = None, right = None, root = None):
        self.left = left
        self.right = right
        self.root = root

def create_tree(node, quan, codes, level, subnodes_count):
    if (len(codes) == 0):
        return
    else:
        if (node.left == None):
            if (subnodes_count < quan[level + 1]):
                node.left = codes[0]
                print(codes[0])
                create_tree(node, quan, codes[1::], level, subnodes_count + 1)
            else:
                node.right = HuffmanNode(root = node)
                create_tree(node.right, quan, codes, level + 1, 0)
        elif (node.right == None):
            if (subnodes_count < quan[level + 1]):
                node.right = codes[0]
                print(codes[0])
                create_tree(node, quan, codes[1::], level, subnodes_count + 1)
            else:
                node.right = HuffmanNode(root = node)
                create_tree(node.right, quan, codes, level + 1, 0)
        else:
            print('root node')
            create_tree(node.root, quan, codes, level - 1, quan[level])
