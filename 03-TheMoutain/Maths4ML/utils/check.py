import random
import inspect
import dis

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

def check_sigma(sigma):
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

    def sigma_correct(start, end, f):
        return sum(f(n) for n in range(start, end + 1))

    # Labeled test functions
    test_funcs = [
        ("f(n) = n", lambda n: n),
        ("f(n) = n^2", lambda n: n * n),
        ("f(n) = 2^n", lambda n: 2 ** n),
        ("f(n) = (-1)^n", lambda n: (-1) ** n),
        ("f(n) = 3n + 1", lambda n: 3 * n + 1),
    ]

    all_correct = True

    for _ in range(10):
        start = random.randint(0, 10)
        end = random.randint(start, start + 10)
        label, f = random.choice(test_funcs)

        expected = sigma_correct(start, end, f)
        try:
            result = sigma(start, end, f)
        except Exception as e:
            print(f"❌ sigma({start}, {end}, {label}) raised an error: {e}")
            all_correct = False
            continue

        if abs(result - expected) > 1e-6:
            print(f"❌ sigma({start}, {end}, {label}) returned {result}, expected {expected}")
            all_correct = False

    if all_correct:
        print("You understand the Sigma, glory to it and to everything. Yes this scary maths symbol \nis just a for loop less scary when you think about it.")
    else:
        print("You don't understand the way of the sigma yet, you must try some more.")