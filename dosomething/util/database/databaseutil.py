'''
Created on Nov 17, 2011

@author: luochounami
'''

def encode(info):
    new_info = {}
    for each in info:
        if type(info[each]) == type(''):
            new_info[each] = info[each].replace('\'', '\'\'')
        else:
            new_info[each] = info[each]
    return new_info

if __name__ == '__main__':
    pass
