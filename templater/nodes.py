import html

class Node(object):
    def eval(self, context):
        raise NotImplementedError()

class GroupNode(Node):
    def __init__(self):
        self._children = []

    def eval(self, context):
        result = ''

        for child in self._children:
            child_html = child.eval(context)
            result += child_html

        return result

    def add_child(self, node):
        self._children.append(node)

class TextNode(Node):
    def __init__(self, content=''):
        self.content = content

    def eval(self, context):
        return self.content

class PythonNode(Node):
    def __init__(self, expr=''):
        self.expr = expr

    def eval(self, context):
        return html.escape(str(eval(self.expr, {}, context)))

class IfNode(Node):
    def __init__(self, predicate=''):
        self.predicate = predicate
        self._true_child = None
        self._false_child = None

    def eval(self, context):
        predicate_result = eval(self.predicate, {}, context)
        if predicate_result:
            return self._true_child.eval(context)
        elif self._false_child is not None:
            return self._false_child.eval(context)
        else:
            return ''

    def set_true_child(self, node):
        self._true_child = node

    def set_false_child(self, node):
        self._false_child = node

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
