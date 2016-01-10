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
        self.current += 1
        return self.tokens[self.current - 1]

    @staticmethod
    def tokenize(text: str) -> [(str, str)]:
        """
        >>> x = Tokenizer.tokenize("{% test %} hello {{ test }}")
        >>> print(list(x))
        [('tag-stmt', '{% test %}'), ('text', ' hello '), ('tag-repr', '{{ test }}')]
        
        Args:
            text:
        """
        tokens = []
        in_stmt_token = False
        in_repr_token = False
        literal_token = []
        symbol_start = -1
        for i in range(len(text)):
            symbol = text[i:i+2]
            if symbol == "{%" or symbol == "{{":
                if in_stmt_token or in_repr_token:
                    raise TemplateSyntaxException("Cannot create a tag inside a tag: '{}'".format(text[symbol_start:i+2]))
                if len(literal_token) > 0:
                    tokens.append(("text", "".join(literal_token[1:])))
                    literal_token = []
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
                        tokens.append(("tag-stmt", text[symbol_start:i+2]))
                        in_stmt_token = False
                elif symbol == "}}":
                    if in_stmt_token:
                       raise TemplateSyntaxException("Cannot close a statement tag with a representation tag: '{}'".format(text[symbol_start:i+2]))
                    else:
                        tokens.append(("tag-repr", text[symbol_start:i+2]))
                        in_repr_token = False
            elif not (in_stmt_token or in_repr_token):
                literal_token.append(text[i])

        if len(literal_token) > 1:
            tokens.append(("text", "".join(literal_token[1:])))

        return tokens
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
