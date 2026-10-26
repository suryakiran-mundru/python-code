Python 3.15.0 (v3.15.0:d220409a13b, Oct  9 2026, 08:17:44) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
a = 10
type(a)
<class 'int'>
b = 12.3
type(b)
<class 'float'>
c = 2+5j
c
(2+5j)
type(c)
<class 'complex'>
s = "codegnan"
type(s)
<class 'str'>
s
'codegnan'
l = [1,3,6,9]
l
[1, 3, 6, 9]
l.append 10
SyntaxError: invalid syntax
l.append (10)
l
[1, 3, 6, 9, 10]
[1, 3, 6, 9, 10]
[1, 3, 6, 9, 10]
type(l)
<class 'list'>
>>> id =[19765498343]
>>> type id
SyntaxError: invalid syntax
>>> id
[19765498343]
>>> [19765498343]
[19765498343]
>>> s='code'
>>> id(s)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    id(s)
TypeError: 'list' object is not callable
>>> id
[19765498343]
>>> type(s0)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    type(s0)
NameError: name 's0' is not defined. Did you mean: 's'?
>>> type(s)
<class 'str'>
>>> id(s)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    id(s)
TypeError: 'list' object is not callable
>>> s+ = 'gnan
SyntaxError: unterminated string literal (detected at line 1)
>>> s+='gnan'
>>> s
'codegnan'
>>> id(s)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    id(s)
TypeError: 'list' object is not callable
>>> t=(1,2,3,4)
>>> t=(1,1,1,1)
>>> t
(1, 1, 1, 1)
>>> t=(1,1.23)
>>> t
(1, 1.23)
>>> type (t)
<class 'tuple'>
>>> s={34,123,1564,7689,55,55,55}
>>> s
{34, 55, 7689, 123, 1564}
>>> 
>>> type(s)
<class 'set'>
>>> d={1:"one",2: 4, 3:[1,2,3],5:(1,23)}
>>> d
{1: 'one', 2: 4, 3: [1, 2, 3], 5: (1, 23)}
>>> pro = {"pro name":'lalptop',"price":55000,"discount":10}
>>> pro
{'pro name': 'lalptop', 'price': 55000, 'discount': 10}
>>> type(d)
<class 'dict'>
>>> status =True
>>> type(status)
<class 'bool'>
>>> s = False
>>> type(s)
<class 'bool'>
>>> s=None
>>> type(s)
<class 'NoneType'>
