# python-speed-test-iterations
Hi! I was solving one task and I did it using list iteration for i in range(len(list)) <br />
I chose this way because I didn't know that I can iter list using for i in list <br />
when i got it I found out this I decided to change my code (looks better) <br />
but this tiny change made my code slower <br />
and now I want to test this snake and find out what should i use to make my code faster <br />

```Python
100 tests
ITERATION WITHOUT INDICES
max: 0.07628965377807617 #-0.015570640563964844
min: 0.047356367111206055 #-0.008429527282714844
mean: 0.052383697032928465 #-0.008178174495697021

ITERATION WITH INDICES
max: 0.09186029434204102 #+0.015570640563964844 +20%
min: 0.0557858943939209 #+0.008429527282714844 +17%
mean: 0.06056187152862549 #+0.008178174495697021 +15%
time for tests: 11.354320049285889

500 tests
ITERATION WITHOUT INDICES
max: 0.13207268714904785 #-0.0769045352935791
min: 0.04680657386779785 #-0.008004903793334961
mean: 0.05613903093338013 #-0.013916979312896732

ITERATION WITH INDICES
max: 0.20897722244262695 #+0.0769045352935791 +58%
min: 0.05481147766113281 #+0.008004903793334961 +17%
mean: 0.07005601024627686 #+0.013916979312896732 +24%
time for tests: 63.13935875892639

1000 tests
ITERATION WITHOUT INDICES
max: 0.2128446102142334 #-0,04320788383
min: 0.04684329032897949 #-0.0069713592529296875
mean: 0.05748220133781433 #-0.010205175876617428

ITERATION WITH INDICES
max: 0.25605249404907227 #+0,04320788383 +20%
min: 0.05381464958190918 #+0.0069713592529296875 +14%
mean: 0.06768737721443176 #+0.010205175876617428 +17%
time for tests: 125.20248126983643
```
so indices not the best way to write a code? 
it is my 1600 tests and results can be different
if you wanna test please share with me <br />
