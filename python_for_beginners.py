
def arithmetic():
    print(8**2)  # 64
    print(5//2)  # 2
    print((8+2)*5)  # 50
    print(10 % 6)  # 4


def stringfunction():
    print('shaheer')  # shaheer
    print('shaheer "laptop"')  # shaheer "laptop"
    print('shaheer\'s laptop')  # shaheer's laptop
    print('shaheer' + 'shaheer')  # shaheershaheer
    print('shaheer' * 5)  # shaheershaheershaheershaheershaheer
    # r for raw string -> c:\Users\i348761\Desktop\new
    print(r'c:\Users\s12345\Desktop\new')


def variables():
    x = 2
    y = 10
    print(x+y)  # 12
    # print(z) # NameError: name 'z' is not defined
    name = 'aydin'
    print(name + ' hamza')  # aydin hamza
    print(name[0])  # a
    print(name[3])  # i
    # print(name[10]) # IndexError: string index out of range
    print(name[-1])  # n
    print(name[0:2])  # ay
    print(name[1:4])  # ydi
    print(name[:3])  # ayd
    # name[3]= 'H' # TypeError: 'str' object does not support item assignment
    print('my name is ' + name[:3])  # my name is ayd
    print(len(name))  # 5
    name = 'shaheer'
    print(name[-4])  # h


def lists():
    nums = [21, 34, 2, 343, 4]
    print(nums)  # [21, 34, 2, 343, 4]
    print(nums[3])  # 343
    print(nums[:3])  # [21, 34, 2]
    print(nums[2:])  # [2, 343, 4]
    names = ['aydin', 'hamza', 'shaheer']
    print(names)  # ['aydin', 'hamza', 'shaheer']
    values = [1.4, 'hamza', 3]
    print(values)  # [1.4,'hamza', 3]
    mil = [nums, names]
    print(mil)  # [[21, 34, 2, 343, 4], ['aydin', 'hamza', 'shaheer']]
    nums.append(33)  # inserts element at the end
    print(nums)  # [21, 34, 2, 343, 4, 33]
    # nums.remove(10) # ValueError: list.remove(x): x not in list
    nums.pop(1)  # 34
    print(nums)  # [21, 2, 343, 4, 33]
    nums.pop()  # removes last element
    print(nums)  # [21, 2, 343, 4]
    del(nums[2:])
    print(nums)  # [21, 2]
    # nums.extend(23,54,2535,56) # TypeError: extend() takes exactly one argument (4 given)
    nums.extend([23, 54, 2535, 56])
    print(nums)  # [21, 2, 23, 54, 2535, 56]
    print(min(nums))  # 2
    print(sum(nums))  # 2691
    print(nums.sort())  # expected result as None. but the list is sorted
    print(nums)  # [2, 21, 23, 54, 56, 2535]


def tuples():
    tup = (324, 34, 45, 21)
    print(tup)  # (324, 34, 45, 21)
    print(tup[1])  # 34
    # tup[1] = 34 # TypeError: 'tuple' object does not support item assignment
    thistuple = ("apple", "banana", "cherry")
    print(len(thistuple))  # 3
    thistuple = ("apple",)  # <class 'tuple'>
    print(type(thistuple))
    # NOT a tuple
    thistuple = ("apple")  # <class 'str'>
    print(type(thistuple))
    thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
    # Return the number of times the value 5 appears in the tuple
    x = thistuple.count(5)
    print(x)  # 2


def sets():
    se = {213, 3, 24, 6, 464, 63}
    print(se)  # {3, 6, 464, 213, 24, 63}
    se = {213, 3, 24, 6, 464, 63, 24}
    print(se)  # {3, 6, 464, 213, 24, 63}
    # se[2] # TypeError: 'set' object is not subscriptable
    # print(se[2]) # TypeError: 'set' object is not subscriptable
    se.add(50)
    print(se)  # {3, 6, 464, 50, 213, 24, 63}
    se.add(5)
    print(se)  # {3, 5, 6, 464, 50, 213, 24, 63}
    se.add(65)
    print(se)  # {65, 3, 5, 6, 464, 50, 213, 24, 63}


def dictionaries():
    dictdata = {1: 'hello', 2: 'world', 3: 'prog'}
    print(dictdata[1])  # hello
    # print(dictdata[5]) # KeyError: 5
    print(dictdata.get(2))  # world
    print(dictdata.get(1, 'Not available'))  # hello
    print(dictdata.get(4, 'Not found'))  # Not found
    keys = ['shaheer', 'aydin', 'hamza']
    values = ['audi', 'bmw', 'vw']
    print(keys, values)  # ['shaheer', 'aydin', 'hamza'] ['audi', 'bmw', 'vw']
    dictdata = dict(zip(keys, values))  # merge 2 lists into dictionary
    print(dictdata)  # {'shaheer': 'audi', 'aydin': 'bmw', 'hamza': 'vw'}
    print(dictdata['aydin'])  # bmw
    dictdata['moon'] = 'night'  # add key value pair to dictionary
    # {'shaheer': 'audi', 'aydin': 'bmw', 'hamza': 'vw', 'moon': 'night'}
    print(dictdata)
    del dictdata['moon']
    print(dictdata)  # {'shaheer': 'audi', 'aydin': 'bmw', 'hamza': 'vw'}
    books = {'Leo Tolstoy': ['Anna Karenina', 'War and Peace'], 'Gustave Flaubert': 'Madame Bovary',
             'Vladimir Nabokov': 'Lolita', 'William Shakespeare': {'Tragedy': 'Hamlet', 'Comedy': 'A Midsummer Night\'s Dream'}}
    # {'Leo Tolstoy': ['Anna Karenina', 'War and Peace'], 'Gustave Flaubert': 'Madame Bovary', 'Vladimir Nabokov': 'Lolita', 'William Shakespeare': {'Tragedy': 'Hamlet', 'Comedy': "A Midsummer Night's Dream"}}
    print(books)
    print(books['Vladimir Nabokov'])  # Lolita
    print(books['Leo Tolstoy'])  # ['Anna Karenina', 'War and Peace']
    print(books['Leo Tolstoy'][1])  # War and Peace
    # {'Tragedy': 'Hamlet', 'Comedy': "A Midsummer Night's Dream"}
    print(books['William Shakespeare'])
    print(books['William Shakespeare']['Comedy'])  # A Midsummer Night's Dream


def morevariables():  # let's check how variables are accessed from the memory
    nums = 2
    print(id(nums))  # 4524026704
    names = 'shaheer'
    print(id(names))  # 4513263280
    x = 10
    y = x  # means the actual values are accessed from same location -> memory efficient
    print(x)  # 10
    print(y)  # 10
    print(id(x))  # 4520836176
    print(id(y))  # 4520836176
    print(id(10))  # 4520836176
    z = 10
    print(id(z))  # 4520836176
    x = 5
    print(id(x))  # 4481657776
    print(id(y))  # 4520836176
    y = x
    print(id(y))  # 4481657776


def datatypes():
    x = 3+5j
    print(type(x))  # <class 'complex'>
    x = 3.4
    y = int(x)
    print(type(x))  # <class 'float'>
    print(type(y))  # <class 'int'>
    z = float(y)
    print(z)  # 3.0
    k = complex(y, z)
    print(k)  # (3+3j)
    print(x < y)  # False -> Boolean
    print(x > y)  # True -> Boolean
    print(int(True))  # 1
    print(int(False))  # 0
    str = "shaheer"
    print(type(str))  # <class 'str'>
    str = 'shaheer'
    print(type(str))  # <class 'str'>
    print(type('abc'))  # <class 'str'>
    print(range(10))  # range(0, 10)
    print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(range(2, 10, 2)))  # [2, 4, 6, 8]
    print(type(range(10)))  # <class 'range'>
    data = {'shaheer': 'audi', 'aydi': 'bmw', 'hamza': 'vw'}
    print(data)  # {'shaheer': 'audi', 'aydi': 'bmw', 'hamza': 'vw'}
    print(data['shaheer'])  # audi
    # bmw , this another way to get data just like above one
    print(data.get('aydi'))


def operators():
    x = 5
    x = x+3
    print(x)  # 8
    x += 5  # assignment operator- shortcut for x=x+5
    print(x)  # 13
    x, y = 10, 14
    print(x, y)  # 10 14
    z = 10
    z = -z  # unary operator
    print(z)  # -10
    # relational operator > < >= <= ! == 
    print(x < y)  # True
    print(x==y) # False
    # logical operator, understand Truth Table
    print(x<11 and y>13) # True since x, y = 10, 14



# arithmetic() # order of execution -> BODMAS - Brackets, Orders, Divide, Multiply, Add, Substract
# stringfunction()
# variables()
# lists() #
# tuples()  # Unchangeable, Allow Duplicates, Ordered
# sets() # {} unsorted, shouldn't repeat- for eg: key
# dictionaries()
# morevariables()
# datatypes()  # int float complex bool
##Numberic, Sequence -> list, tuple,  set, string, range, Dictionary (for mapping) ##
operators()
