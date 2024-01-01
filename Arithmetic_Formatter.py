def getSpace(number):
   if number == 0:
       return ''
   s = ' '
   r = ''
   for x in range(number):
       r = r + s
   return r

def getSeparator(number):
   if number == 0:
       return ''
   s = '-'
   r = ''
   for x in range(number):
       r = r + s
   return r

def arithmetic_arranger(problems, show_result=False):

 line1 = line2 = line4 = operation = ''
 str_line1 = str_line2 = str_line3 = str_line4 = ''
 operation_res = ''
 res = 0

 if len(problems) > 5:
     return 'Error: Too many problems.'

 for problem in problems:
   
   if " - " in problem:         
       a  = problem.split(" - ")
       operation = "-"
   elif " + " in problem:         
       a  = problem.split(" + ")
       operation = "+"
   else:
       return "Error: Operator must be '+' or '-'"
   
   op1 =  a[0]
   op2 =  a[1]
   
   if not op1.isdigit() or not op2.isdigit():
       return 'Error: Numbers must only contain digits.'
   
   if len(op1) > 4 or len(op2) > 4:
       return 'Error: Numbers cannot be more than four digits.'

   res = eval(problem);
   if operation == "+" or  res >= 0:
       operation_res = ' '
   else:
       operation_res = '-'



   diff = len(op1) - len(op2)

   space = getSpace(abs(diff))

   if diff > 0:   
       line1 = str(op1)
       line2 = space + str(op2)
   elif diff < 0:             
       line1 = space + str(op1)
       line2 = str(op2)
   else:
       line1 = str(op1)
       line2 = space + str(op2)
   
   dash =  getSeparator(len( operation + ' ' + line2))
   diff1 = len(str(max(int(op1), int(op2)))) - len(str(abs(res)))


   if diff1 < 0:
       line4 = '  ' + operation_res  + ' ' + getSpace(abs(diff1)) + str(abs(res))
   else:
       line4 = '    ' + operation_res  + ' ' + getSpace(abs(diff1)) + str(abs(res))    
    
   str_line1 = str_line1 + '      ' + line1
   str_line2 = str_line2 + '    ' + operation + ' ' + line2
   str_line3 = str_line3 + '    ' + dash

   if show_result == True:
       str_line4 = str_line4 + line4

 arranged_problems = str_line1 + '\n' + str_line2 + '\n' + str_line3 + '\n' + str_line4
 return arranged_problems

output = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "100 - 500", "1000 - 50"], False)
print(output)

#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40    - 3800     19998      474
