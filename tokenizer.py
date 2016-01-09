class TemplateException(Exception):
    pass  # TODO: Prevent instantiation


class TemplateSyntaxException(TemplateException):
    def __str__(self):
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
        [("tag-stmt", "{% test %}"), ("text", " hello "), ("tag-repr", "{{ test }}"]

        Args:
            text:
        """
        tokens = []
        in_special_token = False
        literal_token = []
        symbol_start = -1
        for i in range(len(text)):
            symbol = text[i:i+2]
            if symbol == "{%" or symbol == "{{":
                if len(literal_token) > 0:
                    tokens.append(("text", "".join(literal_token[1:])))
                    literal_token = []
                symbol_start = i
                in_special_token = True
            elif symbol == "%}":
                tokens.append(("tag-stmt", text[symbol_start:i+2]))
                in_special_token = False
            elif symbol == "}}":
                tokens.append(("tag-repr", text[symbol_start:i+2]))
                in_special_token = False
            elif not in_special_token:
                literal_token.append(text[i])

        if len(literal_token) > 0:
            tokens.append(("text", "".join(literal_token[1:])))

        return tokens

if __name__ == "__main__":
    import doctest
    doctest.testmod()
