import operator

my_string = input("input what you want to calculate = ")
print(my_string)
def get_operator_fn(op):
 return{
                '+':operator.add,
                '-':operator.sub,
                '*':operator.mul,
                'divided':operator.__truediv__,
            }[op]
def evel_binary(op1,oper,op2):
            op1,op2 = int(op1),int(op2)
            return get_operator_fn(oper)(op1,op2)
            

ans = evel_binary(*(my_string.split()))

print(f"your result is = {ans}")
