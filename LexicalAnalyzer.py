def print_token(token, token_type):
    print(f"{token} : {token_type}")

def is_float(s):
    return '.' in s and s.replace('.', '', 1).isdigit()

def is_keyword(s):
    return s in ["if", "for", "while"]

print("Enter code (type 'exit' to quit):")

while True:
    input_line = input()
    if input_line.strip() == "exit":
        break

    current = ""
    i = 0

    while i < len(input_line):
        ch = input_line[i]

        if ch.isalnum() or ch == '_' or ch == '.':
            current += ch
        else:
            if current:
                if current[0].isdigit():
                    if is_float(current):
                        print_token(current, "float_literal")
                    else:
                        print_token(current, "int_literal")
                else:
                    if is_keyword(current):
                        print_token(current, "keyword")
                    else:
                        print_token(current, "identifier")
                current = ""

            if ch.isspace():
                i += 1
                continue

            two_chars = input_line[i:i+2]

            if two_chars == "!=":
                print_token("!=", "not_equal_operator")
                i += 2
                continue
            elif two_chars == "=>":
                print_token("=>", "LE_comparison")
                i += 2
                continue
            elif two_chars == "=<":
                print_token("=<", "GE_comparison")
                i += 2
                continue
            elif two_chars == "==":
                print_token("==", "equal_operator")
                i += 2
                continue
            elif two_chars == "++":
                print_token("++", "increment_operator")
                i += 2
                continue
            elif two_chars == "--":
                print_token("--", "decrement_operator")
                i += 2
                continue
            elif two_chars == "":
                print_token("", "exp_operator")
                i += 2
                continue
            else:
                symbols = {
                    '+': "plus_operator",
                    '-': "sub_operator",
                    '*': "Multiply_operator",
                    '/': "Division_operator",
                    '=': "assignment_operator",
                    '<': "greater_than_operator",
                    '>': "less_than_operator",
                    ',': "Comma",
                    ';': "Semicolon",
                    '(': "LPAREN",
                    ')': "RPAREN",
                    '{': "LBRACE",
                    '}': "RBRACE",
                    '[': "LBracket",
                    ']': "RBracket"
                }

                token_type = symbols.get(ch, "unknown_symbol")
                print_token(ch, token_type)

        i += 1

    if current:
        if current[0].isdigit():
            if is_float(current):
                print_token(current, "float value")
            else:
                print_token(current, "integer value")
        else:
            if is_keyword(current):
                print_token(current, "keyword")
            else:
                print_token(current, "identifier")

    print()

print("Program ended by user.")