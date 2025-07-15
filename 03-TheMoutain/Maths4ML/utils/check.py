import random
import inspect
import dis
from IPython.display import display, Markdown, Math
import math

def simple_task():
    input("The following adventure shall give you knowledge to rule the world some day.\nBut should you fail one problem, you shall perish because you cannot go back. Are you ready to take the leap?\nIf yes please press enter and answer the following questions.")
    while True:
        sum = input("What is 9+33? Also known as the Answer to the Ultimate Question of Life, the Universe, and Everything:  ")
        try:
            if int(sum)==42:
                print("The door opens, you may proceed. The key to the next problem is: HitchHiker")
                break
            else:
                print("WRONG ANSWER")
        except:
            print("WRONG ANSWER")

def explain_sigma():
    pwd = input("Password from the mean-median-mode exercise?")

    if pwd == "ChamberOfSecrets":
        # ---------- Title ----------
        display(Markdown("""# 🔢  Big-Sigma (Summation) Notation
$$\\sum_{i=0}^{n} f(i)$$
## What it means
Add the value of $f(i)$ for every integer $i$ starting at 0 and ending at $n$ (inclusive). In code-speak, it’s a loop that keeps an **accumulator**.\n
### Parts of the notation
- $\\Sigma$ : summation symbol (Greek capital sigma)\n
- $i = 0$ : start value of the index\n
- $n$ : end value of the index (inclusive)\n
- $f(i)$ : function evaluated at each step\n
### Equivalent Python:
```python
total = 0
for i in range(0, n + 1):
    total += f(i)
```
        
## Example
With $f(i)=i^2$ and $n=3$
$$\\sum_{i=0}^{3} i^2 = 0^2 + 1^2 + 2^2 + 3^2 = 14$$
                         
## Bring it to the next level

                         
*“A squiggle of sigmas, a mean in the fray,*  
*Subtract, then you square — let the outliers play.*  
*Sum it, divide it, then square root the pain,*  
*Deviation’s a dance 'round the average domain.”*  

— *ChatGPT*

Now that you know what the notation means. There is one small function I want you to implement. The formula is the following:
$$\\sigma = \\sqrt{ \\frac{1}{n} \\sum_{i=1}^{n} (x_i - \\mu)^2 }$$
Where we have:
- $\\mu$ : What the speared dragon is to the dragon\n

Copy the following python code in the code block below and fill it in
```python
def complicated_function(arr):
    #TODO
    return 0

utils.check.check_complicated_function(complicated_function)
```"""))
    else:
        print("WRONG PASSWORD!")


def first_room_hints():
    while True:
        pwd = input("What was the password from the last exercise? ")
        try:
            if pwd=="HitchHiker":
                print('''Correct! The hint to the next problem is:
                      dragon = [2, 3, 10]
                      kraken = [0, 4, 2, 0, 5]
                      basilisk = [9, 2, 1, 2, 3, 2, 7, 1, 0]''')
                break
            else:
                print("WRONG ANSWER")
        except:
            print("WRONG ANSWER")

def first_room(spear, capture, flee):

    all_correct = True
    
    forbidden_modules = {'numpy', 'scipy', 'statistics'}
    func_globals = spear.__globals__
    for name, val in func_globals.items():
        try:
            module_name = val.__name__
            if module_name in forbidden_modules:
                print(f"⚠️ Warning: Your function uses forbidden module via alias '{name}' -> {module_name}")
                all_correct = False
        except AttributeError:
            continue

    # Correct implementations
    def spear_correct(arr):
        return sum(arr) / len(arr)

    def capture_correct(arr):
        arr = sorted(arr)
        n = len(arr)
        return (arr[n//2] + arr[(n-1)//2]) / 2

    def flee_correct(arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        max_freq = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_freq]
        return modes[0]
    
    spear_bool = True
    capture_bool = True
    flee_bool = True
    # Test loop
    for _ in range(10):  # 10 random test cases
        arr = [random.randint(0, 10) for _ in range(random.randint(5, 15))]

        if abs(spear(arr) - spear_correct(arr)) > 1e-6:
            if spear_bool:
                print(f"Something's wrong for array {arr}.\nThe spear function you gave returned {spear(arr)} when it should have returned {spear_correct(arr)}")
            spear_bool = False

        if abs(capture(arr) - capture_correct(arr)) > 1e-6:
            if capture_bool:
                print(f"Something's wrong for array {arr}.\nThe capture function you gave returned {capture(arr)} when it should have returned {capture_correct(arr)}")
            capture_bool = False

        # Ensure the returned mode is a valid one
        mode_candidates = [x for x in arr if arr.count(x) == max(map(arr.count, arr))]
        if flee(arr) not in mode_candidates:
            if flee_bool:
                print(f"Something's wrong for array {arr}.\nThe flee function you gave returned the wrong value")
            flee_bool = False

    if spear_bool and capture_bool and flee_bool and all_correct:
        print("Congratulations, you had everything correct. You are now the master of measures of the middle. you may move on to the next room, the key to the next problem is: ChamberOfSecrets")
    
    else:
        print("Nothing happens...The emptiness remains, no whispers in the dark.")

def check_simple_sigma(sigma):
    def uses_only_builtin(func):
        forbidden_modules = {'numpy', 'scipy', 'statistics'}
        func_globals = func.__globals__
        for name, val in func_globals.items():
            try:
                module_name = val.__name__
                if module_name in forbidden_modules:
                    print(f"⚠️ Warning: `{func.__name__}` uses forbidden module via alias '{name}' -> {module_name}")
                    return False
            except AttributeError:
                continue
        return True

    if not uses_only_builtin(sigma):
        print("⚠️ Warning: `sigma` may not comply with vanilla Python restriction.")

    def sigma_correct(arr):
        return sum(arr)

    all_correct = True

    for _ in range(10):
        arr = [random.randint(0, 10) for _ in range(random.randint(5, 15))]

        expected = sigma_correct(arr)
        try:
            result = sigma(arr)
        except Exception as e:
            print(f"❌ sigma({arr}) raised an error: {e}")
            all_correct = False
            continue

        if abs(result - expected) > 1e-6:
            print(f"❌ sigma({arr}) returned {result}, expected {expected}")
            all_correct = False

    if all_correct:
        print("You understand the Sigma, glory to it and to everything. Yes this scary maths symbol is just a for loop ...")
    else:
        print("You don't understand the way of the sigma yet, you must try some more.")

def check_complicated_function(little_sigma):
    all_correct = True
    def uses_only_builtin(func):
        forbidden_modules = {'numpy', 'scipy', 'statistics'}
        func_globals = func.__globals__
        for name, val in func_globals.items():
            try:
                module_name = val.__name__
                if module_name in forbidden_modules:
                    print(f"⚠️ Warning: The function uses forbidden module via alias '{name}' -> {module_name}")
                    return False
            except AttributeError:
                continue
        return True

    if not uses_only_builtin(little_sigma):
        all_correct = False
        print("⚠️ Warning: The function may not comply with vanilla Python restriction.")

    def stddev_correct(arr):
        if len(arr) < 2:
            return 0.0  # Could also raise error depending on definition
        mean = sum(arr) / len(arr)
        variance = sum((x - mean) ** 2 for x in arr) / (len(arr))
        return math.sqrt(variance)

    for _ in range(10):
        arr = [random.randint(0, 100) for _ in range(random.randint(2, 20))]
        expected = stddev_correct(arr)
        try:
            result = little_sigma(arr)
        except Exception as e:
            print(f"❌ little_sigma({arr}) raised an error: {e}")
            all_correct = False
            continue

        if abs(result - expected) > 1e-6:
            print(f"❌ little_sigma({arr}) returned {result}, expected {expected}")
            all_correct = False
    
    if all_correct:
        display(Markdown("""## 🔔The bell curve smiles upon you🔔
The function you have just implemented is what we more commonly refer to as the Standard Deviation, denoted $\\sigma$.
 We call it a measure of *spread*. There are other measures of spread of course, like range, interquartile-range, variance (which is just the square of the standard deviation).
\nChallenging you with the standard deviation was to get your brain working. But now you understand.
 If most values are far away from the mean, the terms in the sum will be large, so the sum will be large
 and the standard deviation will be large. Conversely, if most values are close to the mean, the terms in the sum will be small, so the sum will be small
 so the standard deviation will be small. It's not rocket science :)\n
The journey does not end there. Up we go. The next password will be **PaulAllen**."""))
    else:
        print("You have not yet mastered the task. Reflect, revise, return.")