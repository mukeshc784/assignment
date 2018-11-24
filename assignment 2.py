Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> m=30
>>> l=12
>>> x=30%%12
SyntaxError: invalid syntax
>>> x=m%%l
SyntaxError: invalid syntax
>>> x=m%l
>>> 
>>> x
6
>>> print("The quotient of x:",x)
The quotient of x: 6
>>> y=m//l
>>> y
2
>>> a=int(input("Enter the first integer:"))
Enter the first integer:2
>>> b=int(input("Enter the second integer:"))
Enter the second integer:4
>>> c=int(input("Enter the third integer:"))
Enter the third integer:5
>>> d=[]
>>> d.append(a)
>>> d.append(b)
>>> d.append(c)
>>> for i in range (0,3):
	for j in range (0,3):
		for k in range (0,3):
			if (i!=j&j!=k&k!=i):
				print(d[i],d[j],d[k])

				
2 4 5
2 5 4
4 2 5
4 5 2
5 2 4
5 4 2
>>> import itertools
>>> my_list = [1,2,3]
>>> combinations=itertools.cominations(my_list,2)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    combinations=itertools.cominations(my_list,2)
AttributeError: module 'itertools' has no attribute 'cominations'
>>> combinations=itertools.combinations(my_list,2)
>>> for c in combinations:
	print(c)

	
(1, 2)
(1, 3)
(2, 3)
>>> import itertools
>>> my_list = [1,2,3]
>>> permutations=itertools.permutations(my_list,2)
>>> for p in permutations
SyntaxError: invalid syntax
>>> for p in permutations:
	print(p)

	
(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
>>> import itertools
>>> my_list = [1,2,3,4,5,6]
>>> combinations=itertools.cominations(my_list,3)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    combinations=itertools.cominations(my_list,3)
AttributeError: module 'itertools' has no attribute 'cominations'
>>> combinations=itertools.combinations(my_list,3)
>>> permutations=itertools.permutations(my_list,3)
>>> print[result for result in combinations if sum(result)==10]
SyntaxError: invalid syntax
>>> print(result for result in combinations if sum(result)==10)
<generator object <genexpr> at 0x0000020963C90FC0>
>>> 
>>> for c in combinations:
	if sum(c)==10:
		print(c)

		
(1, 3, 6)
(1, 4, 5)
(2, 3, 5)
>>> for i in range (0,50):
	if (i/2==%1):
		
SyntaxError: invalid syntax
>>> for i in range (0,50):
	x=i/2
	if x%1:
		print(x)

		
0.5
1.5
2.5
3.5
4.5
5.5
6.5
7.5
8.5
9.5
10.5
11.5
12.5
13.5
14.5
15.5
16.5
17.5
18.5
19.5
20.5
21.5
22.5
23.5
24.5
>>> for i in range (0,50):
	if (i%2!=0):
		print(i)

		
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
>>> 2+6















		
		




		
	


		




		
	


		
	


		
		print(i)
