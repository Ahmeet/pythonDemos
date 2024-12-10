def isValid(s:str) -> bool:
    closeToOpen = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    
    for bracket in s:
        print(bracket)
        if bracket in closeToOpen:
            if not stack:
                return False
            top = stack.pop()
            if closeToOpen[bracket] != top:
                return False
        else:
            stack.append(bracket)
            print(stack)
    if stack:
        return False
    else:
        return True
    
print(isValid("([])"))