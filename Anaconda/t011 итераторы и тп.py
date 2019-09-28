class multifilter:
    '''    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg
    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos > 0
    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0
    '''
    judge_any = lambda pos, neg: pos > 0
    judge_half = lambda pos, neg: pos >= neg
    judge_all = lambda pos, neg: neg == 0     
    
    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.funs = funcs
        self.judge = judge
        self.it = iterable
     
           
    def __iter__(self):
        for i in self.it:
            pos, neg = 0, 0
            for f in self.funs:
                if f(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield i
        
def mul2(x):
    return x % 2 == 0
def mul3(x):
    return x % 3 == 0
def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5))) 
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
'''
class multifilter:
    judge_any  = lambda p,n : p >= 1
    judge_half = lambda p,n : p >= n
    judge_all  = lambda p,n : n == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.it  = iterable
        self.fun = funcs
        self.juf = judge
        
    def __iter__(self):
        for i in self.it:
            res = [f(i) for f in self.fun ]
            if self.juf(res.count(1), res.count(0)):
                yield i  
'''

