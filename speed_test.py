import time
from statistics import mean

class Test():
    def __init__(self, times):
        self.times = times
        self.resultsOne = []
        
        self.resultsTwo = []
        
    def test(self):
        t3 = time.time()
        for i in range(self.times):
            t1 = time.time()
            self.mainOne()
            timer1 = time.time() - t1
            self.resultsOne.append(timer1)
            

            t2 = time.time()
            self.mainOne()
            timer2 = time.time() - t2
            self.resultsTwo.append(timer2)

        timer3 = time.time() - t3
        maks = max(self.resultsTwo)-max(self.resultsOne)
        minn = min(self.resultsTwo)-min(self.resultsOne)
        meann = mean(self.resultsTwo)-mean(self.resultsOne)
        
        result = f"""{self.times} times
ITERATION WITHOUT INDICES
max: {max(self.resultsOne)} #{'+'+str(maks*-1) if maks*-1 > 0 else maks*-1} {'+'+str(max(self.resultsOne) / max(self.resultsTwo) * 100 - 100)[:4] if max(self.resultsOne) > max(self.resultsTwo) else ''}
min: {min(self.resultsOne)} #{'+'+str(minn*-1) if minn*-1 > 0 else minn*-1} {'+'+str(min(self.resultsOne) / min(self.resultsTwo) * 100 - 100)[:4] if min(self.resultsOne) > min(self.resultsTwo) else ''}
mean: {mean(self.resultsOne)} #{'+'+str(meann*-1) if meann*-1 > 0 else meann*-1} {'+'+str(mean(self.resultsOne) / mean(self.resultsTwo) * 100 - 100)[:4]+'%' if mean(self.resultsOne) > mean(self.resultsTwo) else ''}

ITERATION WITH INDICEC
max: {max(self.resultsTwo)} #{'+'+str(maks) if maks > 0 else maks} {'+'+str(max(self.resultsTwo) / max(self.resultsOne) * 100 - 100)[:4]+'%' if max(self.resultsTwo) > max(self.resultsOne) else ''}
min: {min(self.resultsTwo)} #{'+'+str(minn) if minn > 0 else minn} {'+'+str(min(self.resultsTwo) / min(self.resultsOne) * 100 - 100)[:4]+'%' if min(self.resultsTwo) > min(self.resultsOne) else ''}
mean: {mean(self.resultsTwo)} #{'+'+str(meann) if meann > 0 else meann} {'+'+str(mean(self.resultsTwo) / mean(self.resultsOne) * 100 - 100)[:4]+'%' if mean(self.resultsTwo) > mean(self.resultsOne) else ''}
time for tests: {timer3}"""
        print(result)
        
    def mainOne(self):
        a = [i for i in range(500000)]
        b = []
        for i in a:
            b.append(i)

    def mainTwo(self):
        a = [i for i in range(500000)]
        b = []
        for i in range(len(a)):
            b.append(a[i])

if __name__ == '__main__':
    test = Test(100)
    test.test()
    
