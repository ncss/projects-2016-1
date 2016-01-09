class Node(object):
    def __init__(self, context):
        self._children = []
        self._context = context

    def eval(self):
        raise NotImplementedError()

    def add_child(self, node):
        self._children.append(node)

class GroupNode(Node):
    def eval(self):
        result = ''

        for child in self._children:
            child_html = child.eval()
            result += child_html

        return result

class TextNode(Node):
    def __init__(self, content=''):
        self.content = content

    def eval(self):
        return self.content

class PythonNode(Node):
    def __init__(self, expr=''):
        self.expr = expr

    def eval(self):
        return eval(self.expr)

class IfNode(Node):
    def __init__(self, predicate=''):
        self.predicate = predicate

    def eval(self):
        predicate_result = eval(self.predicate)
        if predicate_result:
            return self._children[0].eval()
        else:
            return ''
