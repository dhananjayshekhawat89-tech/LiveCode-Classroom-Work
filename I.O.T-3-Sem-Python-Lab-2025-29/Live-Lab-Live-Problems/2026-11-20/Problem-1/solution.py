# LiveCode Classroom - Solution
# Batch: I.O.T 3 Sem Python Lab  2025-29
# Category: Live Lab Problems
# Question: Problem 1 (Create a class name Calculator)
# Score: Submitted (Evaluation Completed)
# Synced: Friday, November 20, 2026 at 9:49 AM

# Write your Python solution below
class calculator:
    def add(self,a,b):
        print(f"The addition of two numbers are:{a}+{b}={a+b}")
    def sub(self,a,b):
        print(f"The addition of two numbers are:{a}-{b}={a-b}")
    def multiply(self,a,b):
        print(f"The multiply of two numbers are:{a}-{b}={a-b}")
    def divide(self,a,b):
        print(f"The addition of two numbers are:{a}/{b}={a/b}")
obj1=calculator()
obj1.add(2,4)
obj1.sub(4,2)
obj1.multiply(4,2)
obj1.divide(4,2)