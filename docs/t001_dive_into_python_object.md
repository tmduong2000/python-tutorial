## Dive into Python Object

The main philosophy of Python is creating a truly object-oriented programming language where it is based on the concepts of 'objects'.  So, we can say that everything in Python is object **except keyword**.  In general, keyword of Python interpreter is almost the same for many different Python flavor.  To find out which keywords are currently supported in our Python, we can run the small script to retrieve keywords:
```python
import keyword
print keyword.kwlist
```
Let's reclaim the phrase "everything in Python is object **except keyword**" to "everything is instantiated by Python interpreter is an object".  Let's check a few examples to understand Python object

####Example 1: creating old-style class
```python
# 1) create old-style class
# 2) print object Foo
# 3) convert object Foo to string using repr
class Foo: pass         # 1)
print Foo               # 2) output: __main__.Foo
print repr(Foo)         # 3) output: <class __main__.Foo at 0x10047db48>

```
At instruction print repr(Foo), we see the information regarding object Foo as 
```text
<class __main__.Foo at 0x10047db48>
```
to let us know that object Foo is being instantiated at location
```text
0x10047db48
```

To verify Foo object, we will run two checks

 * verify its type
 * verify its id in hex value

```python
# 1) verify its type
# 2) verify its id in hex value
print type(Foo)         # 1) output: <type 'classobj'>
print hex(id(Foo))      # 2) output: 0x10047db48

```

Now, we can know that Foo object is 'classobj' type and its id is 0x10047db48.  Therefore, using keyword **class** to defining the representation of notation Foo of classobj type is an Python object.


####Example 2: creating new-style class
```python
# 1) create new-style class
# 2) print object Bar
# 3) convert object Bar to string using repr
class Bar(object): pass   # 1)
print Bar                 # 2) output: <class '__main__.Bar'>
print repr(Bar)           # 3) output: <class '__main__.Bar'>

```
After print out notation Bar, it said ...class '__main__.Bar'...  , but we don't sure that the representation of notation Bar is an Python object or not eventhrough we know that Bar is inherited from class object.  Therefore, we must run a few verification

```python
# 1) find out its type
# 2) find out its id in hex value
# 3) find out its bases class
print type(Bar)                 # 1) output: <type 'type'>
print hex(id(Bar)               # 2) output: 0x10036ae80
print Bar.__class__.__bases__   # 3) output: (<type 'object'>,)
```

Now, we know that notation Bar is type of type.  It has id and its based class is object type.  Because its based class is object type, therefore, notation Bar is a Python object.


####Example 3: verifying characteristics of class object - part 1

**Question**: what is object?

There are million answers for this question, but the fundamental answer is an object is an instance of class where class is blueprint of group +/-attribute(s) or +/-method(s).

Now, if we are able to verify that class object Foo and Bar can have attribute, then Foo and Bar are absolutely the "object" as claimed in Python.


```python
# 1) add class attribute to class object Foo
# 2) add class attribute to class object Bar
Foo.cls_attr = 'adding Foo class attribute'   # 1) add attribute to Foo
Bar.cls_attr = 'adding Bar class attribute'   # 1) add attribute to Bar
```

Bingo, we don't get any complaint message during assigned the attribute to instance of class object.  So, Foo and Bar meet the requirement that "everything is instantiated by Python interpreter is an object"


####Example 4: verifying characteristics of class object - part 2

**Question**: Can class object create a new instance?

For class object Foo, we will ask question,

* can **class object** Foo create new a instance which **type is Foo**?

For object Bar, we will ask question,

* can Bar object which **type is type** create a new instance of which **type is Bar**?

The answer is, **Yes, we could**

```python
# 1) create new instance from class object Foo
# 2) create new instance from class object Bar
instance_foo = Foo()
instance_bar = Bar()


print repr(instance_foo)      # output: <class __main__.Foo instance at 0x10047db48>
print hex(id(instance_foo)    # output: 0x10047db48

print repr(instance_bar)      # output: <__main__.Bar object at 0x10049afd0>
print hex(id(instance_bar)    # output: 0x10049afd0
```

We see that both instance of Foo or Bar have allocated the memory at some locations.  The only difference between old-style and new-style is that Python interpreter see **an new instance** of old-style as **instance** while as **object** in new-style.


<hr>
Thanks you for viewing this article.  Please don’t be hesitate to contact [tmduong2000@yahoo.com](mailto:tmduong2000@yahoo.com) to discuss anything regarding Python object.
<hr>