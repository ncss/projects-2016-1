from nodes import GroupNode, TextNode, PythonNode

class Parser(object):
    def __init__(self, context, tokenzier=None):
        self._context = context
        self._tokenizer = tokenzier
        self._head = None

    def set_tokenzier(self, tokenzier):
        self._tokenizer = tokenzier

    def _parse_literal(self, token):
        return TextNode(token)

    def _parse_tag_stmt(self, token):
        raise NotImplementedError()

    def _parse_for(self):
        group = GroupNode()

        for token, token_type in self._tokenizer:
            if token_type == 'literal':
                node = self._parse_literal(token)
            elif token_type == 'tag_stmt':
                # Check if we are looking at an {% end for %} tag
                op, args = self._remove_tag(token).split(maxsplit=1)
                if op == 'end' and args[0] == 'for':
                    break
                else:
                    node = self._parse_tag_stmt(token)
            elif token_type == 'tag_repr':
                node = self._parse_tag_repr(token)

            group.add_child(node)

        return group

    def _parse_tag_repr(self, token):
        node = PythonNode()

        token = self._remove_tag(token)
        token = token.strip()

        return PythonNode(token)

    def parse(self):
        group = GroupNode()

        for token, token_type in self._tokenizer:
            if token_type == 'literal':
                node = self._parse_literal(token)
            elif token_type == 'tag_stmt':
                node = self._parse_tag_stmt(token)
            elif token_type == 'tag_repr':
                node = self._parse_tag_repr(token)

            group.add_child(node)

        return group

    def _remove_tag(self, token):
        return token[2:] + token[:-2]
