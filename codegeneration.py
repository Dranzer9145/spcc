class CodeGenerator:
    def __init__(self):
        self.generated_code = []

    def generate_code(self, intermediate_code):
        for token in intermediate_code:
            if token.isdigit():
                self.generated_code.append(f'PUSH {token}')
            elif token in ['+', '-', '*', '/']:
                op2 = self.generated_code.pop()
                op1 = self.generated_code.pop()
                self.generated_code.append(f'{op1} {token} {op2}')
        return self.generated_code

# Example usage:
code_generator = CodeGenerator()
intermediate_code = ["2", "3", "4", "-", "*", "+"]
generated_code = code_generator.generate_code(intermediate_code)
print("Generated Code:", generated_code)
