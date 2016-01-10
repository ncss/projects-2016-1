from .nodes import GroupNode, TextNode, PythonNode, ForNode, IfNode
from .tokenizer import Tokenizer

class Parser(object):
    def __init__(self, tokenizer):
        self._tokenizer = tokenizer

    def _parse_text(self, token):
        return TextNode(token)

    def _parse_tag_stmt(self, token):
        op, args = self.read_tag_statement(token)

        node = None

        if op == 'for':
            node = self._parse_for(token)
        elif op == 'if':
            node = self._parse_if(token)
        elif op == 'include':
            node = self._parse_include(token)
        else:
            raise NotImplementedError("op: {}, args: {}".format(op, args))

        return node

    def _parse_include(self, token):
        op, filename = self._remove_tag(token).split(maxsplit=1)

        filename = filename.strip()

        with open(filename) as f:
            t = Tokenizer(f.read())
            p = Parser(t)

        return p.parse()

    def _parse_if(self, token):
        op, args = self._remove_tag(token).split(maxsplit=1)
        predicate = args

        if_node = IfNode(predicate)

        group = GroupNode()

        for token_type, token in self._tokenizer:
            node = None
            if token_type == 'text':
                node = self._parse_text(token)
            elif token_type == 'tag_stmt':
                # Check if we are looking at an {% end if %} tag
                op, args = self._remove_tag(token).split(maxsplit=1)
                args = args.strip()
                if op == 'end' and args == 'if':
                    break
                else:
                    node = self._parse_tag_stmt(token)
            elif token_type == 'tag_repr':
                node = self._parse_tag_repr(token)

            group.add_child(node)

        if_node.set_true_child(group)

        return if_node

    def _parse_for(self, token):
        _, item, _, collection = self._remove_tag(token).split(maxsplit=3)

        for_node = ForNode(item, collection)

        group = GroupNode()

        for token_type, token in self._tokenizer:
            node = None
            if token_type == 'text':
                node = self._parse_text(token)
            elif token_type == 'tag_stmt':
                # Check if we are looking at an {% end for %} tag
                op, args = self._remove_tag(token).split(maxsplit=1)
                args = args.split()
                if op == 'end' and args[0] == 'for':
                    break
                else:
                    node = self._parse_tag_stmt(token)
            elif token_type == 'tag_repr':
                node = self._parse_tag_repr(token)

            group.add_child(node)

        for_node.add_child(group)

        return for_node

    def _parse_tag_repr(self, token):
        node = PythonNode()

        token = self._remove_tag(token)

        return PythonNode(token)

    def parse(self):
        group = GroupNode()

        for token_type, token in self._tokenizer:
            node = None
            if token_type == 'text':
                node = self._parse_text(token)
            elif token_type == 'tag_stmt':
                node = self._parse_tag_stmt(token)
            elif token_type == 'tag_repr':
                node = self._parse_tag_repr(token)

            group.add_child(node)

        return group

    def _remove_tag(self, token):
        return token[2:-2].strip()

    def read_tag_statement(self, token):
        return self._remove_tag(token).split(maxsplit=1)
