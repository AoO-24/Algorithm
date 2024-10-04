'''
# 问题描述
有一堆数字，除了一个数字，其它的数字都是成对出现。班上的每个同学拿一个数字，正好将这些数字全部拿完，问如何快速找到拿了单独数字的同学？

## 输入格式
- 空格分隔输入所有的数字

## 输出格式
- 单独的那个数字

## 输入样例(1)
```
1 1 2 2 3 3 4 5 5
```
## 输出样例(1)
4

## 输入样例(2)
```
0 1 0 1 2
```
## 输出样例(2)
2
'''

def solution(inp):
    # Edit your code here
    # 使用异或运算的特性来找出只出现一次的数字
    result = 0
    for num in inp:
        result ^= num
    return result


if __name__ == "__main__":
    # Add your test cases here

    print(solution([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 4)
    print(solution([0, 1, 0, 1, 2]) == 2)
