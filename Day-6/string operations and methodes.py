Python 3.15.0 (v3.15.0:d220409a13b, Oct  9 2026, 08:17:44) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
s='python'
s
'python'
p=''
p
''
s
'python'
t='programming'
s+t
'pythonprogramming'
t*3
'programmingprogrammingprogramming'
s*7
'pythonpythonpythonpythonpythonpythonpython'
'*'*20
'********************'
'0'*30
'000000000000000000000000000000'
s='python java flask mysql fastapi'
s
'python java flask mysql fastapi'
s[0]
'p'
s[7]
'j'
s[-1]
'i'
s[-4]
't'
s[-7]
'f'
s[12]
'f'
s[12]
'f'
s[17]
' '
s
'python java flask mysql fastapi'
s[0:6:1]
'python'
s[7:12]
'java '
s[13:18]
'lask '
s[12:18]
'flask '
s[18:23]
'mysql'
s23
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s23
NameError: name 's23' is not defined
s[24]
'f'
s[24:]
'fastapi'
s[::1]
'python java flask mysql fastapi'
s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
s[-7:]
'fastapi'
s[::2]
'pto aafakmslfsai'
s[-15:-20:-1]
'ksalf'
s[5::-1]
'nohtyp'
'java'in s
True
'python'in s
True
'python'not in s
False
len(s)
31
ord('a')
97
ord('g')
103
>>> chr(10)
'\n'
>>> chr(50)
'2'
>>> chr(90)
'Z'
>>> max(s)
'y'
>>> min(s)
' '
>>> sorted(s)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'f', 'f', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'p', 'q', 's', 's', 's', 't', 't', 'v', 'y', 'y']
>>> s
'python java flask mysql fastapi'
>>> s.upper()
'PYTHON JAVA FLASK MYSQL FASTAPI'
>>> s.lower()
'python java flask mysql fastapi'
>>> s.swapcase()
'PYTHON JAVA FLASK MYSQL FASTAPI'
>>> s.title()
'Python Java Flask Mysql Fastapi'
>>> s.capitalize()
'Python java flask mysql fastapi'
>>> s='python'
>>> s
'python'
>>> s.center(40,'_')
'_________________python_________________'
>>> s.center(40,' ')
'                 python                 '
>>> s.center(40,'*')
'*****************python*****************'
>>> s.ljust(40,'*')
'python**********************************'
>>> s.rjust(40,'*')
'**********************************python'
>>> '1'.zfill(5)
'00001'
>>> '123'.zfill(5)
'00123'
>>> '123456789'.zfill(5)
'123456789'
>>> s='python java flask mysql fastapi'
>>> s
'python java flask mysql fastapi'
>>> s.count('a')
5
>>> s.count('p')
2
>>> s = '        code    gnan      '
>>> s
'        code    gnan      '
>>> s.strip()
'code    gnan'
>>> s.lstrip()
'code    gnan      '
>>> s.rstrip()
'        code    gnan'
>>> s='python java flask mysql fastapi'
>>> s.replace('a','*')
'python j*v* fl*sk mysql f*st*pi'
>>> s.replace('p','1')
'1ython java flask mysql fasta1i'
>>> s.maketrans('apkqs','12345')
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
>>> s.translate
<built-in method translate of str object at 0x106eb2b00>
>>> s.translate(s.maketrans('apkqs','12345'))
'2ython j1v1 fl153 my54l f15t12i'
>>> s.translate(s.maketrans('apkqs','*****'))
'*ython j*v* fl*** my**l f**t**i'
