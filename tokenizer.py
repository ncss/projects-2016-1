def tokenize(filename):
    text = open(filename).read()
    tokens = []
    in_special_token = False
    literal_token = []
    symbol_start = -1
    for i in range(len(text)-1):
        symbol = text[i:i+2]         
        if (symbol == "{%" or symbol == "{{"):
            if len(literal_token) > 0:
                tokens.append("".join(literal_token[1:]))
                literal_token = []
            symbol_start = i
            in_special_token = True
        elif (symbol == "%}" or symbol == "}}"):
            tokens.append(text[symbol_start:i+2])
            in_special_token = False
        elif in_special_token == False:
            literal_token.append(text[i])
    return tokens

print(tokenize("test_tokenizer.txt"))

        
        
        
        
