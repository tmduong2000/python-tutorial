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