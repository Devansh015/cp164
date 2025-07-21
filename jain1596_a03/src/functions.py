"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""

from Stack_array import Stack

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    
    while not source1.is_empty() or not source2.is_empty():
    
        if not source1.is_empty():
            target.push(source1.pop())
            
        if not source2.is_empty():
            target.push(source2.pop())
            
    return target

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = []
    while not source.is_empty():
        temp.append(source.pop())
    for value in temp:
        source.push(value)
    return

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stack = Stack()
    new_string = ''.join(char.lower() for char in string if char.isalnum())
    for a in new_string:
        stack.push(a)
    right_side = stack._values
    stack.reverse()
    reversed = stack._values
    if right_side == reversed:
        palindrome = True
    else:
        palindrome = False
    return palindrome

# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    values = string.split()

    for operand in values:
        if operand not in OPERATORS:
            stack.push(operand)
        else:
            element1 = float(stack.pop())
            element2 = float(stack.pop())

            if operand == "+":
                result = element2 + element1
            elif operand == "-":
                result = element2 - element1
            elif operand == "*":
                result = element2 * element1
            elif operand == "/":
                result = element2 / element1

            stack.push(result)
    
    answer = stack.pop()

    return answer
    
def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    path = []
    stack = Stack()
    stack.push("Start")

    while not stack.is_empty():
        current_point = stack.pop()

        if current_point == "X":
            path.append("X")
            break

        if current_point not in path:
            if current_point != "Start":
                path.append(current_point)
            stack.push("X")

            routes = maze.get(current_point, [])
            for route in routes:
                stack.push(route)

    return path