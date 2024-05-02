import re

def main():
    input_string = """
    position = initial + rate * 60
    """
    tokens = [
        (r'"Hello World!!!"', "<Literal String>"),
        (r'if', "<IF>"),
        (r'then', "<THEN>"),
        (r'else', "<ELSE>"),
        (r'[A-Za-z][A-Za-z0-9]*', "<ID>"),
        (r'[0-9]+', "<INT>"),
        (r'[0-9]+\.[0-9]+', "<FLOAT>"),
        (r'<', "<LT>"),
        (r'<=', "<LE>"),
        (r'==', "<EQ>"),
        (r'!=', "<NE>"),
        (r'>', "<GT>"),
        (r'>=', "<GE>"),
        (r'\+', "<ADD>"),
        (r'-', "<SUB>"),
        (r'\*', "<MUL>"),
        (r'/', "<DIV>"),
        (r'\^', "<POW>"),
        (r'=', "<ASSIGNMENT>")
    ]

    input_lines = input_string.split('\n')
    for line in input_lines:
        line = line.strip()
        if not line:
            continue
        for token_pattern, token_name in tokens:
            match = re.search(token_pattern, line)
            if match:
                print(token_name, end=' ')
                # line = line[match.end():] # Remove the matched part
        print()

if __name__ == "__main__":
    main()
