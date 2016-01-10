class TemplateException(Exception):
    pass  # TODO: Prevent instantiation


class TemplateSyntaxException(TemplateException):
    pass


class Tokenizer:
    def __init__(self, text):
        self.current = 0
        self.tokens = self.tokenize(text)

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.next()
        if temp is None:
            raise StopIteration
        return temp

    def next(self):
        """
        >>> x = Tokenizer("{% test %} hello {{ test }}")
        >>> next(x)
        ('tag_stmt', '{% test %}')
        >>> _ = next(x)
        >>> _ = next(x)
        >>> print(next(x))
        None
        """
        output = self.tokens[self.current] if not self.end() else None
        self.current += 1 # TODO: Stop incrementing value when end is reached
        return output

    def peek(self):
        """
        >>> x = Tokenizer("{% test %} hello {{ test }}")
        >>> _ = next(x)
        >>> _ = next(x)
        >>> x.peek()
        ('tag_repr', '{{ test }}')
        """
        return self.tokens[self.current] if not self.end() else None

    def end(self):
        """
        >>> x = Tokenizer("{% test %} hello {{ test }}")
        >>> _ = next(x)
        >>> _ = next(x)
        >>> _ = next(x)
        >>> x.end()
        True
        """
        return self.current >= len(self.tokens)

    @staticmethod
    def tokenize(text):
        """
        Args:
            text:

        >>> x = Tokenizer.tokenize("{% test %} hello {{ test }}")
        >>> print(list(x))
        [('tag_stmt', '{% test %}'), ('text', ' hello '), ('tag_repr', '{{ test }}')]
        >>> x = Tokenizer.tokenize(" {{ test }} pp {{ test }} ")
        >>> print(list(x))
        [('text', ' '), ('tag_repr', '{{ test }}'), ('text', ' pp '), ('tag_repr', '{{ test }}'), ('text', ' ')]
        """
        tokens = []
        in_stmt_token = False
        in_repr_token = False
        in_literal_token = False
        literal_token = []
        symbol_start = -1
        i = 0
        while i < len(text):
            # Check current letter and one letter ahead
            symbol = text[i:i+2]
            if symbol == "{%" or symbol == "{{":
                if in_stmt_token or in_repr_token:
                    raise TemplateSyntaxException("Cannot create a tag inside a tag: '{}'".format(text[symbol_start:i+2]))
                if in_literal_token:
                    tokens.append(("text", text[symbol_start:i]))
                    in_literal_token = False
                symbol_start = i
                if symbol == "{%":
                    in_stmt_token = True
                else:
                    in_repr_token = True
            elif symbol == "%}" or symbol == "}}":
                if not (in_stmt_token or in_repr_token):
                    raise TemplateSyntaxException("Cannot close a tag outside a tag. ({})".format("".join(literal_token[1:])))
                if symbol == "%}":
                    if in_repr_token:
                        raise TemplateSyntaxException("Cannot close a representation tag with a statement tag: '{}'".format(text[symbol_start:i+2]))
                    else:
                        tokens.append(("tag_stmt", text[symbol_start:i+2]))
                        in_stmt_token = False
                elif symbol == "}}":
                    if in_stmt_token:
                        raise TemplateSyntaxException("Cannot close a statement tag with a representation tag: '{}'".format(text[symbol_start:i+2]))
                    else:
                        tokens.append(("tag_repr", text[symbol_start:i+2]))
                        in_repr_token = False
                i += 1
            elif not (in_stmt_token or in_repr_token) and not in_literal_token:
                symbol_start = i
                in_literal_token = True
            i += 1

        if in_literal_token:
            tokens.append(("text", text[symbol_start:i]))

        return tokens


if __name__ == "__main__":
    import doctest
    doctest.testmod()
