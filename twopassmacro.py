class Macroprocessor:
    def __init__(self):
        self.macro_table = {}
        self.pass1_output = []
        self.pass2_output = []

    def pass1(self, source_code):
        lines = source_code.split('\n')
        for line in lines:
            if line.strip().startswith("MACRO"):
                parts = line.split()
                if len(parts) >= 2:  # Check if there are enough elements in the parts
                    macro_name = parts[1]
                    parameter_list = parts[2:]
                    self.macro_table[macro_name] = parameter_list
                else:
                    print("Invalid MACRO definition:", line)
            else:
                self.pass1_output.append(line)

    def pass2(self):
        for line in self.pass1_output:
            parts = line.split()
            expanded_line = []
            for part in parts:
                if part in self.macro_table:
                    macro_name = part
                    arguments = parts[parts.index(part) + 1].split(',')
                    macro_definition = self.macro_table[macro_name]
                    for macro_part in macro_definition:
                        if macro_part in arguments:
                            expanded_line.append(arguments[macro_definition.index(macro_part)])
                        else:
                            expanded_line.append(macro_part)
                else:
                    expanded_line.append(part)
            self.pass2_output.append(' '.join(expanded_line))

    def get_pass1_output(self):
        return '\n'.join(self.pass1_output)

    def get_pass2_output(self):
        return '\n'.join(self.pass2_output)

# Example usage
if __name__ == "__main__":
    source_code = """
    PRG START 0
    ..
    MACRO
    INCR
    A, 1, DATA
    A, 2, DATA
    A, 3, DATA
    ..MEND
    ..INCR
    ..INCR
    END
    """
    macro_processor = Macroprocessor()
    macro_processor.pass1(source_code)
    macro_processor.pass2()
    print("Pass 1 Output:")
    print(macro_processor.get_pass1_output())
    print("\nPass 2 Output:")
    print(macro_processor.get_pass2_output())
