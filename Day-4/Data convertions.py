Python 3.15.0 (v3.15.0:d220409a13b, Oct  9 2026, 08:17:44) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
a=10
a
10
int(a)
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
bool(0)
False
b=8.9
b
8.9
int(b)
8
complex(b)
(8.9+0j)
str(b)
'8.9'
list(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c=(10.3+7j)
c
(10.3+7j)
int(c)                        # complex
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(c)                        # complex
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
10.0

str(c)
'(10.3+7j)'
list(a)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
d='codegnan'
d
'codegnan'
int(d)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(d)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float(d)
ValueError: could not convert string to float: 'codegnan'
complex(d)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    complex(d)
ValueError: complex() arg is a malformed string
str(d)
'codegnan'
list(d)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(d)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(d)
{'c', 'd', 'a', 'g', 'o', 'n', 'e'}
dict(d)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(d)
True
#list
l=[1,2,3,4,]
l
[1, 2, 3, 4]
int(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
str(l)
'[1, 2, 3, 4]'
str(l)
'[1, 2, 3, 4]'
list(l)
[1, 2, 3, 4]
tuple(l)
(1, 2, 3, 4)
set(l)
{1, 2, 3, 4}
dict(l)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
#tuple
t=(1,2,3,4,)
t
(1, 2, 3, 4)
int(t)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
str(t)
'(1, 2, 3, 4)'
list(t)
[1, 2, 3, 4]
set(t)
{1, 2, 3, 4}
dict(t)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> bool(t)
True
>>> s={1,2,3,4}
>>> s
{1, 2, 3, 4}
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    complex(s)
TypeError: complex() argument must be a string or a number, not set
>>> str(s)
'{1, 2, 3, 4}'
>>> list(s)
[1, 2, 3, 4]
>>> tuple(s)
(1, 2, 3, 4)
>>> set(s)
{1, 2, 3, 4}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> bool(s)
True
>>> #dictnory
>>> e={1:2,3:4,4:5,5:6}
>>> e
{1: 2, 3: 4, 4: 5, 5: 6}
>>> int(e)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    int(e)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> float(e)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    float(e)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> complex(e)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    complex(e)
TypeError: complex() argument must be a string or a number, not dict
>>> str(e)
'{1: 2, 3: 4, 4: 5, 5: 6}'
>>> list(e)
[1, 3, 4, 5]
>>> tuple(e)
(1, 3, 4, 5)
>>> set(e)
{1, 3, 4, 5}
>>> bool(e)
True
