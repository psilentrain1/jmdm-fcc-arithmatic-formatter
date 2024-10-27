def arithmetic_arranger(problems, show_answers=False):
    if check_problems(problems):
        return "Error: Too many problems."
    elif check_operators(problems):
        return "Error: Operator must be '+' or '-'."
    elif check_numbers(problems):
        return "Error: Numbers must only contain digits."
    elif check_length(problems):
        return "Error: Numbers cannot be more than four digits."
    else:
        equation = do_math(problems)
        output = do_format(equation, show_answers)
    return output
        
    
def check_problems(problems):
    if len(problems) > 5:
        return True
    else:
        return False

def check_operators(problems):
    bad_operators = False
    for i in problems:
        problem = i.split(" ")
        for operator in problem:
            if operator == '*' or operator == '/':
                bad_operators = True
    if bad_operators:
        return True
    else:
        return False

def check_numbers(problems):
    bad_operand = False
    for i in problems:
        problem = i.split(" ")
        if (not problem[0].isdigit()) or (not problem[2].isdigit()):
            bad_operand = True
    if bad_operand:
        return True
    else:
        return False

def check_length(problems):
    operand_too_long = False
    for i in problems:
        problem = i.split(" ")
        for operand in problem:
            if len(operand) > 4:
                operand_too_long = True
    if operand_too_long:
        return True
    else:
        return False

def do_math(problems):
    equation = []
    solutions = []
    for i in problems:
        problem = i.split(" ")
        solution = eval(i)
        solutions.append(solution)
        equation.append([problem[0], problem[1], problem[2], str(solution)])
    return equation

def do_format(equation, show_answers):
    long_operand = 0
    long_operand_length = 0
    line_length = 0
    line_one = ""
    line_two = ""
    line_three = ""
    line_four = ""
    s = " "
    h = "-"

    for i in equation:
        if len(i[0]) < len(i[2]):
            long_operand = 2
        else:
            long_operand = 0
        long_operand_length = len(i[long_operand])
        line_length = long_operand_length + 2
        line_one += s*4
        line_two += s*4
        if long_operand == 0:
            e = line_length - len(i[2]) - 2
            line_one += s*2 + i[0]
            line_two += i[1] + s + (s*e) + i[2]
        elif long_operand == 2:
            e = line_length - len(i[0])
            line_one += (s*e) + i[0]
            line_two += i[1] + s + i[2]
        line_three += s*4
        line_three += h*line_length
        line_four += s*4
        f = line_length - len(i[3])
        line_four += s*f + i[3]
        if show_answers:
            output = line_one[4:] + "\n" + line_two[4:] + "\n" + line_three[4:] + "\n" + line_four[4:]
        else:
            output = line_one[4:] + "\n" + line_two[4:] + "\n" + line_three[4:]

    return output




#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 - 1"])}')
#print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"],)}')

#Test1
if arithmetic_arranger(["3801 - 2", "123 + 49"]) == "  3801      123\n-    2    +  49\n------    -----":
    print("Test 1: Pass")
else:
    print("Test 1: Fail")

#Test2
if arithmetic_arranger(["1 + 2", "1 - 9380"]) == "  1         1\n+ 2    - 9380\n---    ------":
    print("Test 2: Pass")
else:
    print("Test 2: Fail")
    print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
    print("  1         1\n+ 2    - 9380\n---    ------")

#Test3
if arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]) == "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----":
    print("Test 3: Pass")
else:
    print("Test 3: Fail")

#Test4
if arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]) == "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------":
    print("Test 4: Pass")
else:
    print("Test 4: Fail")

#Test5
if arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) == 'Error: Too many problems.':
    print("Test 5: Pass")
else:
    print("Test 5: Fail")

#Test6
if arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]) == "Error: Operator must be '+' or '-'.":
    print("Test 6: Pass")
else:
    print("Test 6: Fail")

#Test7
if arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]) == 'Error: Numbers cannot be more than four digits.':
    print("Test 7: Pass")
else:
    print("Test 7: Fail")

#Test8
if arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]) == 'Error: Numbers must only contain digits.':
    print("Test 8: Pass")
else:
    print("Test 8: Fail")

#Test9
if arithmetic_arranger(["3 + 855", "988 + 40"], True) == "    3      988\n+ 855    +  40\n-----    -----\n  858     1028":
    print("Test 9: Pass")
else:
    print("Test 9: Fail")

#Test10
if arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True) == "   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028":
    print("Test 10: Pass")
else:
    print("Test 10: Fail") 