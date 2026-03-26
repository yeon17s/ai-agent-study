#Runnable 객체의 주요 메서드

# 1. invoke() - 동기 방식

from langchain_core.runnables import RunnableLambda

# def append_ten(target: int) -> int:
#     return target + 10
append_ten = lambda x: x + 10
# multiply_two = lambda x: x * 2

result = append_ten(10)
print(f'result = {result}') 

run_append = RunnableLambda(append_ten) #Runnable
run_multiply = RunnableLambda(lambda x: x * 2) #Runnable

append_result = run_append.invoke(5)
print(f'append_result = {append_result}')