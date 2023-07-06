import math
 
def parse_expr(expr: str):
    if expr == "":
        return
    expr = expr.replace("^", "**")
    try:
        return eval(expr)
    except:
        return "Error"