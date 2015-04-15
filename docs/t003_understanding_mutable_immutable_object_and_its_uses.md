## Understanding mutable and immutable object and its uses


### Definitions

Term | Definition from [docs.python.org](https://docs.python.org/2/glossary.html)
--- | ---
[mutable](https://docs.python.org/2/glossary.html#term-mutable) | Mutable objects can change their value but keep their id()
[immutable](https://docs.python.org/2/glossary.html#term-immutable) | An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.

<br>

### Mutable object in Python

Most Python instances (new object creating from classobj) are mutable objects unless we apply some restrictions in classobj to make them act as the immutable objects.  By default, the user-defined classobject often create a mutable object.  User can customize the property(ies) of object to optimize its uses.  The mutable object can be,
* user-defined classobj type (yes, frequently uses)
* function type (none applicable)
* lambda type (none applicable)
* decorator object (none applicable)
* module type (applicable if necessary)
* built-in type such as dict, list, set, collections, and other (default object behavior)

<br>
Create user-defined class Foo and its instance foo, and then check mutable behavior of these objects.
```python
# create user-defined class Foo
class Foo(object): pass
print hex(id(Foo))     # output: 0x10070c8c0
Foo.s = 'Hi Foo'
print hex(id(Foo))     # output: 0x10070c8c0

# create instance foo
foo = Foo()
print hex(id(foo))     # output: 0x1006a6310
foo.otherstr = 'hi foo'
print hex(id(foo))     # output: 0x1006a6310
```

####<span style='color:blue;'>Use case 1</span>: partition huge class into several modules
suppose that our <strong style='color:blue;'>design spec.</strong> having one class that is huge and it is containing around +50 APIs and some APIs will need 100 - 200 lines of code and other API will have 30 - 80 lines of code.  We have three developers working on this class.  To optimize the source control, technical leader can layout this class into four files: clsABCLib.py, ABCAPI1to18.py, ABCAPI19to36.py, ABCAPI37to50.py, and then allocate the approriate task to developers.  Leader can quickly update or merge new changes to source control with minimal code conflict. 

<br>

Github [source code](https://github.com/tmduong2000/python-tutorial/tree/master/codes/t003_mutable_immutable_object/mutable): 
```python
# file1: abcapi1to18.py
def api_test1(self):
	print 'api_test1: "%s", "%s"' %(self.cls_attr1, self.instance_attr1)
	print '-' * 40
#....

# file2: abcapi19to36.py
def api_test19(self):
	print 'api_test19: "%s", "%s"' %(self.cls_attr19, self.instance_attr19)
	print '-' * 40
#....

# file3: abcapi37to50.py
def api_test37(self):
	print 'api_test37: "%s" "%s"', %(self.cls_attr37, self.instance_attr37)
	print '-' * 40
#....

from abcapi1to18  import api_test1
from abcapi19to36 import api_test19
from abcapi37to50 import api_test37 

class HugeClass(object):
	cls_attr1 = 'class attr 1'
	cls_attr19 = 'class attr 19'
	cls_attr37 = 'class attr 37'

	def __init__(self):
		self.instance_attr1 = 'instance attr 1'
		self.instance_attr19 = 'instance attr 19'
		self.instance_attr37 = 'instance attr 37'

HugeClass.test1 = api_test1
HugeClass.test19 = api_test19
HugeClass.test37 = api_test37

if __name__ == '__main__':
	hugeInstance = HugeClass()
	hugeInstance.test1()
	hugeInstance.test19()
	hugeInstance.test37()

```
<br>

####<span style='color:blue;'>Use case 2</span>: create data structure or object for OOP
The benefits of designing our software in Object-oriented programming style are leverage the reuse resources, flexible to integrate or implement with other component or interface, easy maintenance or debugging, more secure to interoperate with data, and more.

```python
# created by Tuyen M. Duong (2015-03-31)
# The MIT License (MIT)
class Point(object):
	def __init__(self, x=0.0, y=0.0):
    	self.x = x
        self.y = y
    def __str__(self):
    	return '(x=%s, y=%s)' %(self.x, self.y)
    #...

class Shape(object):
	def __init__(self, **kwargs):
    	self.location = Point() 
        for key in kwargs:
        	setattr(self, key, kwargs[key])
            
    def __str__(self):
    	lst = ['Shape Info:']
        d = self.__dict__
        for key in d:
        	lst.append('   %s: %s' %(key, d[key]))
        return '\n'.join(lst)
    #...

if __name__ == '__main__':
	loc = Point(5.0, 6.0)
    rec = Shape(name='rectangle', location=loc, width=20.0, height=12.0)
    cir = Shape(name='circle', radius=5.0)
    
    print 'location data:', loc
    print
    print '*** rectangle shape data ***'
    print rec
    print
    print '*** circle shape data ****'
    print cir
    
```

output of this problem is,

```python
location data: (x=5.0, y=6.0)

*** rectangle shape data ***
Shape Info:
   width: 20.0
   location: (x=5.0, y=6.0)
   name: rectangle
   height: 12.0

*** circle shape data ***
Shape Info:
   radius: 5.0
   location: (x=0.0, y=0.0)
   name: circle
```

<br>

####<span style='color:blue;'>Use case 3</span>: use the mutable object to pass a argument as a reference value to function.
Python doesn't support an operator or keyword in the function parameters that will allow those passing arguments acting as a reference value like C#, Java, C/C++, and other. We can use a mutable object for a reference parameter of function.

```python
class Mod(object): pass

def div(n, d, refObj):
	try:
		quo = n / d
		refObj.value = n % d
		return quo
	except:
		refObj.value = 'ZeroDivisionError'
		raise ZeroDivisionError('integer division or modulo by zero') 


result = div(11, 7, Mod)
print 'result: %s, modulo: %s' %(result, Mod.value)    # result: 1, modulo: 4


``` 
<br>

### Immutable object in Python
Immutable object is an object that user can't alter its property(ies) or attribute(s).  However, it won't restrict the container(s) object of immutable object to alter its property(ies) or attribute(s).  We often confuse the new creation of mutable object v.s immutable object because our implementation for design specification to program.  We will introspect the following example:

```python
# tuple is immutable class object type
t = (['x'], ['a'])
# list is mutable class object type
l = [['x'], ['a']]

# check their hex value of 
print (hex(id(t[-1])), hex(id(l[-1])))
                   # output: ('0x1005a63f8', '0x10059bc68')

# add new item in variable
t[-1].append('b')
l[-1].append('b')

# check their hex values again
print (hex(id(t[-1])), hex(id(l[-1])))
                   # output: ('0x1005a63f8', '0x10059bc68')


```

In this example, we see that both last items stored in tuple and list don't change their hex values because we only alter the property(ies) or attribute(s) of container (in this case, the last container of tuple and list).  However, if we pretend to assign new object to container of tuple or list, list  (mutable) object will allow us to change its properties and tuple (immutable) object won't.

```python
lst_curr_hex_val = hex(id(l[-1]))

# assign new data to last item of list
l[-1] = ['a', 'new']

lst_chg_hex_val = hex(id(l[-1]))

# check its old and new hex values and we expect they are different
print lst_curr_hex_val, lst_chg_hex_val   # output: 0x10059bc68 0x10059bb00 -> OK

# however, if we try to assign new value to tuple, tuple will raise TypeError exception
try:
	t[-1] = ['a', 'new']
except TypeError as te:
	print 'TypeError: %s' %te    # output: TypeError: 'tuple' object does not support item assignment

```
<br>
####`How to create immutable class`
Design requirements for immutable class:
* allows to instantiate a new object with arguments
* provides method(s) to retrieve its data (i.e attribute(s) value
* provides method(s) to communication with other object without changing its property(ies)
* if tries to allocate new object to its property(ies), must raise exception

<br>
Github [source code](https://github.com/tmduong2000/python-tutorial/blob/master/codes/t003_mutable_immutable_object/immutable/immutablefoo.py):
```python
################################################################################
# The MIT License (MIT)
# 
# Copyright (c) 2015 Tuyen M. Duong (www.tduongsj.com)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################

# created by Tuyen M. Duong (2015-04-14)
class ImmutableFoo(object):
    """
    create immutable object with ImmutableFoo class
       - storing mixin data type: list or dictionary
       - can be either access by using key such as foo[0] or foo['data']
       - or access by using attribute such as foo.data
    """
    
    #===========================================================================
    # special functions
    #===========================================================================
    def __init__(self, *args, **kwargs):
        if args: self.__dict__.update(zip(range(len(args)),args))
        if kwargs: self.__dict__.update(kwargs)
                
    def __getattribute__(self, attr):
        return super(ImmutableFoo, self).__getattribute__(attr)
    
    def __setattr__(self, attr, value):
        raise AttributeError("'ImmutableFoo' object does not support item assignment")
    
    def __getitem__(self, attr):
        if isinstance(attr, int):
                try: return self._getList()[attr]
                except: raise IndexError('ImmutableFoo index out of range')
        else:
            try: return self.__dict__[attr]
            except: raise KeyError("ImmutableFoo don't have this key '%s'" %attr)
    
    def __setitem__(self, attr, value):
        raise TypeError("'ImmutableFoo' object does not support item assignment")
    
    #===========================================================================
    # private functions
    #===========================================================================
    def _getList(self):
        return [val for (i, val) in self.__dict__.items() if isinstance(i, int)]
    
    def _getDict(self):
        return dict([item for item in self.__dict__.items() if not isinstance(item[0], int)])
    
    #===========================================================================
    # public functions
    #===========================================================================
    
    def getList(self): return self._getList()
    
    def getDict(self): return self._getDict()
    
    def has_key(self, key): return key in self.__dict__
    
    
if __name__ == '__main__':
    
    lst_names = ['Tyler  Wilson', 'Tyler J. Wilson']
    
    personInfo = dict(fullname='Tyler John Wilson', 
             firstname='Tyler', 
             lastname='Wilson', 
             middlename='John', 
             location='city ABC, state XY')
    person = ImmutableFoo(*lst_names, **personInfo)
    
    print person[0]             # output: 'Tyler Wilson'
    print person[1]             # output: 'Tyler J. Wilson'
    print person[-1]            # output: 'Tyler J. Wilson'
    print person.fullname       # output: 'Tyler John Wilson'
    print person['firstname']   # output: Tyler
    print person.getList()      # output: ['Tyler  Wilson', 'Tyler J. Wilson']
    print person.getDict()      # output: {  'middlename': 'John', 
                                #            'lastname': 'Wilson', 
                                #            'fullname': 'Tyler John Wilson', 
                                #            'location': 'city ABC, state XY', 
                                #            'firstname': 'Tyler'}
    print person.has_key(1)             # output: True
    print person.has_key(10)            # output: False
    print person.has_key('lastname')    # output: True
    print person.has_key('Lastname')    # output: False
    
    # can't set new value to immutable object
    #   - output will be: 'ImmutableFoo' object does not support item assignment
    try:
        person.fullname = 'Tyler John Wilson I'
    except Exception as e:
        print e.message
        
```
<br>
####`What is/are use(s) of immutable object?`
We can use immutable object to create a group of constant data.  If our passing argument of method or function is mutable object and we don't expect any changes to passing argument after function call return its signature to current scope of program, then we can render mutable object to immutable.  This concept has similar object cloning in other programming language such as java.  However, the illustration above coding only provides a minimal structure to deal with very simple data structure.  

<br>
<hr>
Thanks you for viewing this article.  Please don’t be hesitate to contact [tmduong2000@yahoo.com](mailto:tmduong2000@yahoo.com) to discuss anything regarding Python object.
<hr>





