from lark import Lark, Transformer

grammar = '''
    start: expression
    expression: expression "+" term |
                expression "-" term |
                term
    term: term "*" factor |
          term "/" factor |
          factor
    factor: NUMBER |
            "(" expression ")"
    %import common.NUMBER
    %import common.WS
    %ignore WS
'''

class LRParser:
    def __init__(self):
        self.calculator = Calculator()

    def parse(self, expression):
        parser = Lark(grammar, start='start', parser='lalr')
        try:
            tree = parser.parse(expression)
            print("Successfully parsed the expression:", expression)
        except Exception as e:
            print("Parsing failed:", e)

class Calculator(Transformer):
    def add(self, items):
        return items[0] + items[1]

    def sub(self, items):
        return items[0] - items[1]

    def mul(self, items):
        return items[0] * items[1]

    def div(self, items):
        if items[1] == 0:
            raise ValueError("Division by zero!")
        return items[0] / items[1]

    def NUMBER(self, token):
        return int(token)

if __name__ == "__main__":
    lr_parser = LRParser()
    expression = "2 * (3 + 4)"
    lr_parser.parse(expression)


Output:
For Test Case - 1 ( Successful Parsing ):
Expression : expression = "2 * (3 + 4)"
Result : Successfully parsed the expression: 2 * (3 + 4)
For Test Case - 2 ( Unsuccessful Parsing ):
Expression : expression = "2(3 + 4)"
2.Result : Parsing failed: Unexpected token Token('LPAR', '(') at line 1, column
Expected one of:
* SLASH
* STAR
* MINUS
* $END
* PLUS
Previous tokens: [Token('NUMBER', '2')]
