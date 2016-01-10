class Node(object):
    def __init__(self, context):
        self._children = []

    def eval(self):
        raise NotImplementedError()

    def add_child(self, node):
        self._children.append(node)

class GroupNode(Node):
    def eval(self, context):
        result = ''

        for child in self._children:
            child_html = child.eval(context)
            result += child_html

        return result

class TextNode(Node):
    def __init__(self, content=''):
        self.content = content

    def eval(self, context):
        return self.content

class PythonNode(Node):
    def __init__(self, expr=''):
        self.expr = expr

    def eval(self, context):
        return str(eval(self.expr, {}, context))

class IfNode(Node):
    def __init__(self, predicate=''):
        self.predicate = predicate

    def eval(self, context):
        predicate_result = eval(self.predicate, {}, context)
        if predicate_result:
            return self._children[0].eval(context)
        else:
            # Else evaluate branch
            if len(self._children) == 2:
                return self._children[1].eval(context)
            return ''

class ForNode(Node):
    def __init__(self, item, collection):
        self._item = item
        self._collection = collection
        self._child = None

    def eval(self, context):
        result = ''

        for next_val in eval(self._collection, {}, context):
            child_context = context
            child_context[self._item] = next_val
            next_html = self._child.eval(child_context)
            result += next_html

        return result

    def add_child(self, node):
        self._child = node
