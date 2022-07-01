import time
from statistics import mean

def test(func, times):
    results = []
    for i in range(times):
        t1 = time.time()
        func()
        results.append(time.time() - t1)
    print(f'max: {max(results)}\nmin: {min(results)}\nmean: {mean(results)}')

def mainOne():
    a = [i for i in range(500000)]
    b = []
    for i in a:
        b.append(i)

def mainTwo():
    a = [i for i in range(500000)]
    b = []
    for i in range(len(a)):
        b.append(a[i])

if __name__ == '__main__':
    t1 = time.time()
    print('ITERATION WITHOUT INDICES')
    test(mainOne, 500)
    print()
    print('ITERATION WITH INDICEC')
    test(mainTwo, 500)
    print(f'time for tests: {time.time()-t1}')
    
