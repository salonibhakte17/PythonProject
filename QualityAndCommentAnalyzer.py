import re

def analyze_python_file(filename):
    total_lines = 0
    total_comments = 0
    total_functions = 0
    snake_case_functions = 0
    non_snake_case_functions = 0
    function_pattern = r'^\s*def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
    snake_case_pattern = r'^[a-z]+(_[a-z]+)*$'
    with open(filename, 'r') as file:
        for line in file:
            total_lines += 1
            stripped_line = line.strip()
            if stripped_line.startswith("#"):
                total_comments += 1
            match = re.match(function_pattern, line)
            if match:
                total_functions += 1
                function_name = match.group(1)
                if re.match(snake_case_pattern, function_name):
                    snake_case_functions += 1
                else:
                    non_snake_case_functions += 1
    print("\n----- Code Quality Report -----")
    print("Total Lines of Code:", total_lines)
    print("Total Comments:", total_comments)
    print("Total Functions:", total_functions)
    print("Functions Following snake_case:", snake_case_functions)
    print("Functions Violating snake_case:", non_snake_case_functions)
    if non_snake_case_functions == 0:
        print("Overall Code Quality: Excellent")
    elif non_snake_case_functions <= 2:
        print("Overall Code Quality: Good")
    else:
        print("Overall Code Quality: Needs Improvement")
file_name = input("Enter Python file name (example: sample.py): ")
analyze_python_file(file_name)