from types import MappingProxyType
from dis import dis 
from unicodedata import name
if __name__ == '__main__':
    print()
    d = {'key1':'value1'}
    d_frozen = MappingProxyType(d)
    print(d, type(d))

    print('<<<<<<set>>>>>>')
    se_1 = {'apple', 'orange', 'kiwi', 'apple', 'orange', 'kiwi'}
    se_2 = set(['apple', 'orange', 'apple', 'orange', 'kiwi'])
    se_3 = {3}
    se_4 = set()
    se_5 = frozenset({'apple', 'orange', 'kiwi', 'apple', 'orange', 'kiwi'})
    print(se_5)

    print(se_1)
    se_1.add('melon')
    print(se_1)

    print(se_1, type(se_1))
    print(se_2, type(se_2))
    print(se_3, type(se_3))
    print(se_4, type(se_4))
    print(se_5, type(se_5))

    print('---------------')
    print(dis('{10}'))
    print('---------------')
    print(dis('set({[10]})'))

    print('---------------')
    print({name(chr(i), '') for i in range(1, 256)})