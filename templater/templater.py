from . import parser
from . import tokenizer

def render(filename: str, **kwargs) -> str:
    with open(filename) as f:
        file_content = f.read()
        template_parser = parser.Parser(tokenizer.Tokenizer(file_content))

    group_node = template_parser.parse()

    return group_node.eval(kwargs)
