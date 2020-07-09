def solve_problem(split_problem):
    num1, operator, num2 = split_problem

    if operator == "+":
        return str(int(num1) + int(num2))

    elif operator == "-":
        return str(int(num1) - int(num2))


def arithmetic_arranger(problems, to_solve=False):
    num_problems = len(problems)

    # Check for too many problems
    if num_problems > 5:
        return "Error: Too many problems."

    split_problems = [problem.split() for problem in problems]

    for problem in split_problems:
        # Check for illegal operators
        if not (problem[1] == "+" or problem[1] == "-"):
            return "Error: Operator must be '+' or '-'."

        # Check for illegal operands
        if not (problem[0].isnumeric() and problem[2].isnumeric()):
            return "Error: Numbers must only contain digits."

        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # format each problem, padding with spaces
    formatted_problems = []

    for problem in split_problems:
        num1, operator, num2 = problem
        difference = len(num1) - len(num2)

        if difference < 0:
            line1 = " " * -difference + num1
            line2 = num2
        else:
            line1 = num1
            line2 = " " * difference + num2

        line1 = "  " + line1
        line2 = operator + " " + line2
        line3 = "-" * len(line1)

        formatted_problems.append([line1, line2, line3])

    # Append solution if required
    if to_solve:
        for i in range(num_problems):
            solution = solve_problem(split_problems[i])
            padding_length = len(formatted_problems[i][0]) - len(solution)
            formatted_problems[i].append(" " * padding_length + solution)

    solution = "\n".join(
        [
            "    ".join([problem[line] for problem in formatted_problems])
            for line in range(len(formatted_problems[0]))
        ]
    )

    return solution

