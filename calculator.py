import math
 
def parse_expr(expr: str):
    if expr == "":
        return
    expr = expr.replace("^", "**")
    return eval(expr)