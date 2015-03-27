## Dive into Python Object - Part 2

* [Create Python Object](#create_python_object)
* [Object characteristics](#object_characteristics)
   1. [object must has an identity](#object_must_has_an_identity)
   2. [object must has type](#object_must_has_type)
   3. [object can store data](#object_can_store_data)
   4. [object can contains other object](#object_can_contains_other_object)
   5. [classobj can inherite from other classobj](#classobj_can_inherite_from_other_classobj)
* [View object hierarchy](#view_object_hierarchy)

<br>
<a id="create_python_object" />
### Create Python object
There are several ways to create object in Python.  Python object can be created from built-in object such as object, int, float, dict, list, and so on or it can be created from user-defined type.

1. using **class** keyword to create classobj.
2. object can be constructed by assigning from a new instance from class object to variable.
3. assigned from **built-in object** to variable.
4. result of evaluating expression can be set to variable.
5. using **def** keyword to create function object.
6. from return result of invoking function.
7. using **lambda** keyword to create anonymous function object.
8. from lambda execution.

```python
class Foo(object): pass          # 1. using class keyword

foo = Foo()                      # 2. assigning from a new instance from classobj

d = dict(age=-1, name='unknown') # 3. assigning from built-in

# 4. result of evaluating expression
lst = iter(range(100))
subLst = [x * 2 for x in lst if x>=20 and x<=80 and x%7==1 ]

# 5. using def keyword to create test_func object
def test_func(): return 'Hello test_func'

# 6. from return result of invoking function
retVar = test_func()

# 7. using lambda to create anonymouns function object
anony_sqrt = lambda x: x * x

# 8. from lambda execution
val = anony_sqrt(3)
```
<a id="object_characteristics" />
### Object characteristics

1. object must has an identity.
2. object must has type.
3. object can store data.
4. object can contains other object(s) (in other word, attribute(s)).
5. classobj can inherite from other classobj or built-in object.

<br>
<a id="object_must_has_an_identity" />
**`Object must has an identity`**
```python
s = 'Hello World'           # creating string object which value is 'Hello World'
print hex(id(s))			# id: 0x10287cc60

s = 'Hi'                    # creating string object which value is 'Hi'
print hex(id(s))            # id: 0x1028e3a30

s = 'Hello World'           # creating string object which value is 'Hello World'
print hex(id(s))            # id: 0x1005a3a20 -> this id is different from above s.  Good.

class Foo(object): pass
print hex(id(Foo)           # id: 0x1004165b0

foo = Foo()                 # creating new instance for foo
print hex(id(foo)           # id: 0x10286be10

foo = Foo()                 # creating new instance for foo
print hex(id(foo))          # id: 0x102875590 -> this id is different from above foo.  Good.
```


Sometime, we see that the new created object which is storing the same data of previous created object has the same identity.  
Question is: is a new object being created?  
Answer is: Yes.

```python
i=1; print hex(id(i))          # id: 0x100312828
i=5; print hex(id(i))          # id: 0x1003127c8
i=1; print hex(id(i))          # id: 0x100312828

# we will delete variable notation i, and then create integer object with value 1 to i
del i; i=1; print hex(id(i))   # id: 0x100312828
```

from Data model in url [docs.python.org](https://docs.python.org/2/reference/datamodel.html), it quotes,
> **Objects are never explicitly destroyed**;  however, when they become unreachable they may be garbage-collected. An implementation is allowed to postpone garbage collection or omit it altogether — it is a matter of implementation quality how garbage collection is implemented, as long as no objects are collected that are still reachable.

<br>
<a id="object_must_has_type" />
**`Object must has type`**

```python
print str(type(s))      # output: <type 'str'>
print str(type(i))      # output: <type 'int'>
print str(type(Foo))    # output: <type 'type'>
print str(type(foo))    # output: <class '__main__.Foo'>
```

<br>
<a id="object_can_store_data" />
**`Object can store data`**

object **s** store value 'Hello world' or 'Hi'  
object **i** store value 1 or 5   
object **foo** is an instance of classobj Foo.  To store data in **foo**, we can store data in attributes of object **foo**

```python
foo.x = 10
foo.y = 20
foo.str_data = 'Hello foo'
foo.lst_data = ['abc', 'xyz', 1, 1.1, dict(item1='item abc', item2='item xyz')]
```

<br>
**`object can contains other object(s)`**

```python
obj_dict = dict(item1='item abc', item2='item xyz')
obj_lst = list(1, 2, 'abc', 2.2, 'xyz')
obj_str = 'Hello World'

def func_greeting(msg):
	print 'Hi %s,' %msg


# store other objects into object
foo.dict_data = obj_dict       # store dictionary into foo
foo.list_data = obj_list       # store built-in data structure list into foo
foo.str_data = obj_str         # store str data into foo
foo.greeting = func_greeting   # store function into foo

```
<br>
<a id="classobj_can_inherite_from_other_classobj" />
**`classobj can inherite from other classobj`**

```python
# inherite class Foo from built-in class object
class Foo(object): pass
```

```python
# inherite class Bar from built-in class object
class Bar(object): pass
```

```python
# inherite class FooBarInt from classobj Foo and Bar and built-in class integer
class FooBarInt(Foo, Bar, int): pass
```

<br><br>
<a id="view_object_hierarchy" />
### View object hierarchy
Starting from **new-style** class declaration, all user-defined classobj must inherite from built-in class to take the benefits (faster, safer, better garbage collection, OO, and more ...) of Python object.  classobj object is the top most base class in Python.

```python
print object.__bases__      # output: ()  -> top most base class

print int.__bases__         # output: (<type 'object'>,)  -> classobj int inherite from object
```
<br>
check classobj hierarchy of Foo, Bar, and FooBarInt
```python
print Foo.__bases__      # output: (<type 'object'>,) -> parent of Foo is object
print Bar.__bases__      # output: (<type 'object'>,) -> parent of Bar is object

print FooBarInt.__bases__  
      # output: (<class '__main__.Foo'>, <class '__main__.Bar'>, <type 'int'>)
      # parent of FooBarInt is Foo, Bar, and int


.....
##############################################################
# type help(FooBarInt) on console, we will see the following #
##############################################################
Help on class FooBarInt in module __main__:

class FooBarInt(Foo, Bar, __builtin__.int)
 |  Method resolution order:
 |      FooBarInt
 |      Foo
 |      Bar
 |      __builtin__.int
 |      __builtin__.object
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 
...
...
...

```

<br>
check instance hierarchy from FooBarInt

```python
fbarint = FooBarInt()

print fbarint.__class__    # output: <class '__main__.FooBarInt'>

print fbarint.__class__.__bases__    # output: (<class '__main__.Foo'>, <class '__main__.Bar'>, <type 'int'>)


.....
##############################################################
# type help(fbarint) on console, we will see the following #
##############################################################
Help on class FooBarInt in module __main__:

class FooBarInt(Foo, Bar, __builtin__.int)
 |  Method resolution order:
 |      FooBarInt
 |      Foo
 |      Bar
 |      __builtin__.int
 |      __builtin__.object
 |  
 
...
...
...
```



