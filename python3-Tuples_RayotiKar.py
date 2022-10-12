'''
AUTHOR: Rayoti
Python3 Concept: Tuples in Python
GITHUB: https://github.com/RayotiKar
'''

•	A tuple is another sequence data type that is similar to the list. 
•	A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses ().
•	The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
•	Tuples can be thought of as read-only lists. tuple is immutable.

>>> tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
>>> tinytuple = (123, 'john')
>>> tuple
('abcd', 786, 2.23, 'john', 70.2)
>>> tuple[2]=6
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    tuple[2]=6
TypeError: 'tuple' object does not support item assignment
>>> tuple[0]
'abcd'
>>> tuple[2:]
(2.23, 'john', 70.2)
>>> tuple[2:4]
(2.23, 'john')
>>> tuple+tinytuple
('abcd', 786, 2.23, 'john', 70.2, 123, 'john')
