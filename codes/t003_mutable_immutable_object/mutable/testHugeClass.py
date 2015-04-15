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