from stack import Stack

def balanser(unbalansed_str):
    balans = Stack()
    left_balans = "({["
    right_balans = ")}]"
    for item in unbalansed_str:
        if item in left_balans or balans.isEmpty() == True:
            balans.push(item)
        elif item in right_balans: 
            if right_balans.find(item) == left_balans.find(balans.peek()):
                balans.pop()
            else:
                balans.push(item)
    if balans.size() != 0:
        return "Несбалансированно"
    return "Cбалансированно"
