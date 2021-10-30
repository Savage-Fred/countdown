import random

TEST = True

class conundrum:
  operators = ["+","-","/","*"]
  bigs = [25, 50, 75, 100]
  target_min = 100
  total_inputs = 6
  inputs = []
  the_usual = 2

  def __init__(self):
    self.target = abs(int(random.gauss(500,250)))%1000
    self.target_min_check()
    self.update_numbers(2)
  
  def update_target(self):
    self.target = abs(int(random.gauss(500,250)))%1000
    self.target_min_check()
  
  def update_numbers(self,in_bigs):
    self.inputs = []
    in_bigs = int(in_bigs)
    bigs_copy = self.bigs.copy()
    for x in range(self.total_inputs - in_bigs):
      self.inputs.append(random.randint(1,10))
    for x in range(in_bigs-1):
      print(len(self.bigs))
      print(self.bigs)
      self.inputs.append(bigs_copy.pop(random.randint(0,len(self.bigs)-1)))
  
  def target_min_check(self):
    if self.target < self.target_min:
      self.target += 100
  
  def play(self):
    if not TEST: 
      self.update_numbers(int(input("Number of bigs: ")))
    else: 
      self.update_numbers(self.the_usual)
    self.update_target()
    print("The numbers are", end=": ")
    print(self.inputs)
    print("And the target is", end=": ")
    print(self.target)
    expression = input("expression: ")
    self.eval_expression(expression)

  def eval_expression(self,expression):
    #if not self.check_expression(expression):
    #  return False
    #else:
      open_parens = 0
      operators = []
      operands = []
      regA = 0  #Register A
      regB = 0  #Register B
      regR = 0  #Register Result 
      for char in expression:
        if char == "(":
          open_parens +=1
        
        elif char == ")":
          if open_parens <= 0:
            return False
          else: 
            open_parens -= 1
            regA = operands.pop()
            regB = operands.pop()
            op = operators.pop()
            regR = self.arithmetic(regA,regB,op)
            operands.append(regR)

        elif char in str(self.inputs):
          print(char)
          operands.append(int(char))

        elif char in self.operators:
          print(char)
          operators.append(char)

      while len(operators) > 0 and len(operands) > 0:
        regA = operands.pop()
        regB = operands.pop()
        op = operators.pop()
        regR = self.arithmetic(regA, regB, op)
        print(regA,end=" " )
        print(op,end=" ")
        print(regB, end=" = ")
        print(regR)
        operands.append(self.arithmetic(regA,regB,op))
      
        print 


  def arithmetic(self, op1, op2, operator):
    if operator not in self.operators:
      return -99
    elif operator == "+":
      return op1+op2
    elif operator == "-":
      return op1 - op2
    elif operator == "*":
      return op1 * op2
    elif operator == "/":
      if op1%op2 != 0:
        raise Exception("non integer division")
      else: 
        return op1/op2
      

  def check_expression(self,expression):
    for char in expression:
      if char not in self.operators: 
        if char not in ("(",")"):
          if char not in self.inputs:
            print(char,end=": ")
            print("bad expression")
            return False
    return True


  

if __name__ == "__main__":
  c = conundrum()
  #print(c.inputs)
  while True:
    c.play()


