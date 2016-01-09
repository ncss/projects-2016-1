def tokenize(filename):
    text = open(filename).read()
    tokens = []
    in_token = False
    symbol_start = -1
    for i in range(len(text)-1):
        symbol = text[i:i+2]         
        if (symbol == "{%" or symbol == "{{"):
            symbol_start = i
            in_token = True
        elif (symbol == "%}" or symbol == "}}"):
            tokens.append(text[symbol_start:i+2])
            in_token = False
    return tokens

#print(tokenize("test_tokenizer.txt"))

        
        
        
        
