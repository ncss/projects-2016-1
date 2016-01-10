from templater import parser
from templater import tokenizer

def render(path, context):
    text = open(path).read()
    #TODO Run parser
