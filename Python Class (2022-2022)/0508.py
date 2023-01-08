# x = list(map(int, input().split()))
# print(sum(x))

# import time

# start = time.time()

# s = 0
# for i in range(1, 1):
#     s+=i

# print(time.time() - start)
import random
import time

class Quiz:
    def __init__(self, start, end):
        self.n1 = random.randrange(start, end)
        self.n2 = random.randrange(start, end)
        self.operators = ["+", "-", "*", "/", "%"]
        self.op = random.choice(self.operators)

    def quiz(self):
        answer = input(f"{self.n1} {self.op} {self.n2} = ")
        while answer.insumeric() and self.calculate() != int(answer):
            answer = input(f"{self.n1} {self.op} {self.n2} = ")

    def calculate(self):
        if self.op == "+":
            return self.plus()
        elif self.op == "-":
            return self.minus()
        elif self.op == "*":
            return self.multiple()
        elif self.op == "/":
            return self.divide()
        elif self.op == "%":
            return self.remainder()
    def plus(self):
        return self.n1 + self.n2
    
    def minus(self):
        return self.n1 - self.n2

    def multiple(self):
        return self.n1 * self.n2

    def divide(self):
        return self.n1 // self.n2
    
    def remainder(self):
        return self.n1 % self.n2


start_time = time.time()

for i in range(5):
    Quiz(1, 11).quiz()

end_time = time.time() - start_time
print(f"Correct Answer!! Elapsed : {end_time}")