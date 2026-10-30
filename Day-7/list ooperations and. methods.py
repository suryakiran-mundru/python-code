Python 3.15.0 (v3.15.0:d220409a13b, Oct  9 2026, 08:17:44) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
s='Python Programming'
s
'Python Programming'
s.startswith('p')
False
s.startswith('P')
True
s.startswith('Pyt')
True
s.endswith('y')
False
s.endswith('img')
False
s.endswith('ing')
True
's'. islower()
True
'U'.isupper()
True
'code123'.isalpha()
False
'code@123'.isalnum()
False
s
'Python Programming'
s.istitle()
True
'my@var'.insideidentifier()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    'my@var'.insideidentifier()
AttributeError: 'str' object has no attribute 'insideidentifier'. Did you mean '.isidentifier' instead of '.insideidentifier'?
'my@var'.isidentifier()
False
'a b c d'.split()
['a', 'b', 'c', 'd']
'a,b,c,d'.split()
['a,b,c,d']
'a,b,c,d'.split('-')
['a,b,c,d']
'a-b-c-d'.split('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.split('-',2)
['a', 'b', 'c-d']
s="""
hello
world
python
"""
s
'\nhello\nworld\npython\n'
s.splitlines()
['', 'hello', 'world', 'python']
l=['a','b','c','d']
'-'.join(1)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    '-'.join(1)
TypeError: can only join an iterable
'-'.join(l)
'a-b-c-d'
'@'.join(l)
'a@b@c@d'
'1'.join(l)
'a1b1c1d'
'_'.join(l)
'a_b_c_d'
''.join(l)
'abcd'


































s
'\nhello\nworld\npython\n'
s='a-b-c-d'
s.partition('b')
('a-', 'b', '-c-d')
'python.py'..partition('.')
SyntaxError: invalid syntax
'python.py'.partition('b')
('python.py', '', '')
'pyt.hon.py'.partition('.')
('pyt', '.', 'hon.py')
'pyt.hon.py'.rpartition('.')
('pyt.hon', '.', 'py')
s="hello"
s.encode()
b'hello'
t="Hello 🥰"
s.encode
<built-in method encode of str object at 0x101a6e880>
s.encode()
b'hello'
t.encode()
b'Hello \xf0\x9f\xa5\xb0'
b'Hello \xf0\x9f\xa5\xb0'.decode()
'Hello 🥰'
l=[]
l=list()
l=[1,2,3]
l=([1,2,3,4])
l
[1, 2, 3, 4]
type(l)
<class 'list'>
#mutable ,ordered,duplicats,hetiro,dynamic
l=[1,1,1,1,1]
l
[1, 1, 1, 1, 1]
l=[1,12.2,3+5j,'str',[1,2],(1,2),{1,2},{1,2},False,None]
l
[1, 12.2, (3+5j), 'str', [1, 2], (1, 2), {1, 2}, {1, 2}, False, None]
[1,2,3]+[6,7,8]
[1, 2, 3, 6, 7, 8]
[1,2,3]*5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
l=['python','java','c','flask','fastapi','mysql','aws']
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
l[0]
'python'
l[1]
'java'
l[2]
'c'
l[3]
'flask'
l[4]
'fastapi'
l[5]
'mysql'
l[6]
'aws'
l[::-1]
['aws', 'mysql', 'fastapi', 'flask', 'c', 'java', 'python']
l[-1::-1]
['aws', 'mysql', 'fastapi', 'flask', 'c', 'java', 'python']
l[:3]
['python', 'java', 'c']
l[-3:]
['fastapi', 'mysql', 'aws']
l[2:5]
['c', 'flask', 'fastapi']
l[1::2]
['java', 'flask', 'mysql']
l[::2]
['python', 'c', 'fastapi', 'aws']
l[::-1]
['aws', 'mysql', 'fastapi', 'flask', 'c', 'java', 'python']
l[-3:-6:-1]
['fastapi', 'flask', 'c']
l[-1::1]
['aws']
l[-1:-7]
[]
>>> l[-1:-7:-1]
['aws', 'mysql', 'fastapi', 'flask', 'c', 'java']
>>> 'c' in l
True
>>> 'p' in l
False
>>> 'mysql' in l
True
>>> 'c++'in l
False
>>> l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
>>> len(l)
7
>>> sorted(l)
['aws', 'c', 'fastapi', 'flask', 'java', 'mysql', 'python']
>>> max(l)
'python'
>>> min(l)
'aws'
>>> id(l)
4402142144
>>> l[1]
'java'
>>> l[1]='html'
>>> l
['python', 'html', 'c', 'flask', 'fastapi', 'mysql', 'aws']
>>> id(l)
4402142144
>>> l[2]='c++'
>>> l
['python', 'html', 'c++', 'flask', 'fastapi', 'mysql', 'aws']
>>> l[3]='jupiter'
>>> l
['python', 'html', 'c++', 'jupiter', 'fastapi', 'mysql', 'aws']
>>> id(l)
4402142144
>>> l
['python', 'html', 'c++', 'jupiter', 'fastapi', 'mysql', 'aws']
>>> l.append('a')
>>> l
['python', 'html', 'c++', 'jupiter', 'fastapi', 'mysql', 'aws', 'a']
>>> l.append('b')
>>> l.append('c')
>>> l
['python', 'html', 'c++', 'jupiter', 'fastapi', 'mysql', 'aws', 'a', 'b', 'c']
>>> l.insert('s')
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    l.insert('s')
TypeError: insert expected 2 arguments, got 1
>>> id(l)
4402142144
>>> l.extend([1,2,3,4,4])
>>> l
['python', 'html', 'c++', 'jupiter', 'fastapi', 'mysql', 'aws', 'a', 'b', 'c', 1, 2, 3, 4, 4]
>>> l.insert(1,'flask')
>>> l
['python', 'flask', 'html', 'c++', 'jupiter', 'fastapi', 'mysql', 'aws', 'a', 'b', 'c', 1, 2, 3, 4, 4]
>>> l.insert(2,'c')
>>> l
['python', 'flask', 'c', 'html', 'c++', 'jupiter', 'fastapi', 'mysql', 'aws', 'a', 'b', 'c', 1, 2, 3, 4, 4]
>>> id(l)
4402142144
