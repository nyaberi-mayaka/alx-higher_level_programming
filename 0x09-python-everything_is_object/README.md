<h1 align="center">0x09. Python - Everything is object</h1>

***

## Background Context
Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:
```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 
```
OK. But what about this?
```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
```
This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should **read all documentation first (as usual :))**, then take the time to **think and brainstorm with your peers** about what you think and why. **Try to do this without coding anything for a few hours**.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. **Don’t go this route**. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, **you will most likely have to answer to these type of questions**.

All your answers should be only one line in a file. No space before or after the answer.
***
## Resources
**Read or watch**:
* [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
* [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
* [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
* [Mutation](http://composingprograms.com/pages/24-mutable-data.html#sequence-objects) *(Only this chapter)*
* [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
* [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)
* ***
## Learning Objectives
### General
* Why Python programming is awesome
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions
* Copyright - Plagiarism
***
## Requirements
### `.txt` Answer Files
* Only one line
* No Shebang
* All your files should end with a new line
***
## Tasks
### 0. Who am I?
What function would you use to print the type of an object?

Write the name of the function in the file, without `()`.

### 1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.

### 2. Right count
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = 100
```
### 3. Right count =
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = 89
```
### 4. Right count =
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = a
```
### 5. Right count =+
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = a + 1
```
### 6. Is equal
What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
### 7. Is the same
What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
### 8. Is really equal
What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
### 9. Is really the same
What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
### 10. And with a list, is it equal
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
### 11. And with a list, is it the same
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
### 12. And with a list, is it really equal
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
### 13. And with a list, is it really the same
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
### 14. List append
What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
### 15. List add
What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
#### Notes
The code creates two variables `l1` and `l2` that reference the same list object `[1, 2, 3]`. The line `l1 = l1 + [4]` creates a new list object `[1, 2, 3, 4]` and assigns it to `l1`, effectively breaking the reference to the original list object.

However, `l2` still points to the original list object `[1, 2, 3]`, so when we print `l2` after modifying `l1`, we get the output `[1, 2, 3]`.

### 16. Integer incrementation
What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
### 17. List incrementation 
What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
### 18. List assignation 
What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
#### Notes
The code above defines a function assign_value that takes two arguments, `n` and `v`, and assigns the value of `v` to `n`. Then, it creates two lists `l1` and `l2`.

Next, the `assign_value` function is called with `l1` and `l2` as arguments. However, in Python, lists are mutable objects and passed by reference, so the assignment `n = v` within the function `assign_value` creates a new reference for the `n` variable, but does not affect the original list `l1`.

Therefore, the print statement will output the original list `l1`, which is `[1, 2, 3]`.
### 19. Copy a list object 
Write a function `def copy_list(l):` that returns a copy of a list.
* The input list can contain any type of objects
* Your file should be maximum 3-line long (no documentation needed)
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 
```
**No test cases needed**

#### Notes
```
#!/usr/bin/python3
def copy_list(l):
    return l[:]
```
This is a linting error indicating that the variable name l is ambiguous. It is recommended to use a more descriptive variable name to avoid confusion and improve code readability.

In the context of the code, l is used to represent a list that needs to be copied. A better variable name for this function could be original_list. The updated code would be:
```
#!/usr/bin/python3
def copy_list(original_list):
    return original_list[:]
```
### 20. Tuple or not? 
```
a = ()
```
Is `a` a tuple? Answer with `Yes` or `No`.
 
### 21. Tuple or not? 
```
a = (1, 2)
```
Is `a` a tuple? Answer with `Yes` or `No`.

### 22. Tuple or not? 
```
a = (1)
```
Is `a` a tuple? Answer with `Yes` or `No`.
#### Notes
No.

It is not a tuple. It is just an integer.

In order to create a tuple with only one element, you should use a comma after the first element. For example:
```
a = (1,)
```
### 23. Tuple or not? 
```
a = (1, )
```
Is `a` a tuple? Answer with `Yes` or `No`.
 
### 24. Who I am? 
What does this script print?
```
a = (1)
b = (1)
a is b
```
#### Notes
True

The script creates two variables `a` and `b`, both assigned to the integer value `1`. Since the integers in Python are immutable, any two variables that have the same integer value will actually point to the same object in memory.

Therefore, when we use the `is` keyword to check whether `a` and `b` are the same object, it returns `True`.
### 25. Tuple or not 
What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```
#### Notes
The script creates two tuples `a` and `b`, each containing the elements 1 and 2. The expression `a` is `b` checks if the two variables refer to the same object in memory. In this case, the two tuples are not the same object in memory, even though they contain the same values. Therefore, the expression a is b evaluates to `False`

For strings and integers, small values are often cached and reused by Python. Therefore, if you create two variables that have the same value, they might end up pointing to the same object in memory. However, this is an implementation detail and is not guaranteed by the Python language specification. Therefore, it is still safer to compare strings and integers using the `==` operator rather than `is`.

In CPython, small integers (between -5 and 256) and strings that contain only ASCII letters, digits, and underscores are cached for performance reasons. Since these objects are immutable, it is safe to cache them because they cannot be modified. Tuples are immutable objects, meaning they cannot be changed after creation. As a result, when you create two tuples with the same values, they are still distinct objects in memory, even if their contents are identical. So, a and b are two separate tuples in memory, and the is operator checks whether they are the same object, not whether their contents are equal.
### 26. Empty is not empty 
What does this script print?
```
a = ()
b = ()
a is b
```
#### Notes
This script will print `True`.

In the script, two empty tuples `a` and `b` are created. When comparing `a` and `b` using the `is` operator, Python checks if a and b refer to the same object in memory. Since both tuples are empty and immutable, Python optimizes the memory usage and points both `a` and `b` to the same empty tuple object in memory. Therefore, `a is b` returns `True`.

### 27. Still the same? 
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

### 28. Same or not? 
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

### 29. #pythonic
Write a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration (see code):
* Format: see example
* Your file should be maximum 4-line long (no documentation needed)
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$
```
**No test cases needed**
#### Notes
* [Python getattr() Method](https://www.tutorialsteacher.com/python/getattr-method)
```
getattr(std, 'name') returns the value of the name property of the std object, which is John. It always returns the latest value even after updating a property value.
```
### 30. Low memory cost
Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$ 
```
**No test cases needed**
#### Notes
* [`__slots__`](https://docs.python.org/3/reference/datamodel.html?highlight=__slots__#slots)
* [Usage of `__slots__`?](https://stackoverflow.com/questions/472000/usage-of-slots)
### 31. int 1/3
```
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:
* How many int objects are created by the execution of the first line of the script? (`103-line1.txt`)
* How many int objects are created by the execution of the second line of the script (`103-line2.txt`)
#### Notes
When Python starts up, small integer values (e.g. 0-256) are preallocated in memory and reused throughout the program. The variables `a` and `b` in the script are assigned the preallocated integer object with a value of 1, rather than creating a new object. Therefore, no new `int` objects are created by the execution of either line of the script.

This is an optimization feature called "interning" that is specific to the CPython implementation.

* [Integer Interning in Python (Optimization)](https://www.codesansar.com/python-programming/integer-interning.htm#:~:text=In%20Python%20optimization%2C%20integer%20interning,range%20from%20%2D5%20to%20256.)
### 32. int 2/3
```
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:
* How many int objects are created by the execution of the first line of the script? (`104-line1.txt`)
* How many int objects are created by the execution of the second line of the script (`104-line2.txt`)
* After the execution of line 3, is the int object pointed by `a` deleted? Answer with `Yes` or `No` (104-line3.txt)
* After the execution of line 4, is the int object pointed by `b` deleted? Answer with `Yes` or `No` (`104-line4.txt`)
* How many int objects are created by the execution of the last line of the script (`104-line5.txt`)

### 33. int 3/3
```
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:
* Before the execution of line 2 (`print("Love")`), how many int objects have been created and are still in memory? (`105-line1.txt`)
* Why? (optional blog post :))
Hint: `NSMALLPOSINTS`, `NSMALLNEGINTS
#### Notes
Standard implementation of Python (CPython) pre-loads (caches) a global list of integers in the range from -5 to 256. Any time an integer is referenced in this range Python does not create new one but uses the cached version. This is known as integer interning.

This is basically an optimization techniques in Python. Since small integers are relatively used more in our code than large integers. So Python decides to pre-cache certain range (-5 to 256) of integers for performance reason.

### 34. Clear strings
```
guillaume@ubuntu:/python3$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
guillaume@ubuntu:/python3$
```
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):
* How many string objects are created by the execution of the first line of the script? (`106-line1.txt`)
* How many string objects are created by the execution of the second line of the script (`106-line2.txt`)
* After the execution of line 3, is the string object pointed by `a` deleted? Answer with `Yes` or `No` (`106-line3.txt`)
* After the execution of line 4, is the string object pointed by `b` deleted? Answer with `Yes` or `No` (`106-line4.txt`)
* How many string objects are created by the execution of the last line of the script (`106-line5.txt`)
***
## Author
* **[The_quadzilla](https://github.com/nyaberi-mayaka)**
***
