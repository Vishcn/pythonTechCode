'''
Created on Nov 21, 2011

@author: Zhaobo Luo
'''

STR = 'str'
DEC = 'dec'

FIELD_TOKEN = '__field__'
VALUE_TOKEN = '__value__'

def generateReplaceSql(conf_file_path, key_value):
    conf_file = open(conf_file_path, 'r')
    table_name = conf_file.readline().strip()
    replace_sql = 'replace into `%s`(%s) values(%s)' % (table_name, FIELD_TOKEN, VALUE_TOKEN)
    while True:
        conf_file_line = conf_file.readline().strip()
        if len(conf_file_line) == 0:
            break
        parts = conf_file_line.split()
        keys = parts[2].split('.')
        value = key_value
        try:
            for each_key in keys:
                value = value[each_key]
            if None == value:
                parts[1] = DEC
                value = 'null'
            replace_sql = replace_sql.replace(FIELD_TOKEN, '`%s`, %s' % (parts[0], FIELD_TOKEN)).replace(VALUE_TOKEN, '%s, %s' % ((parts[1] == STR and ('\'%s\'' % value) or value), VALUE_TOKEN))
        except:
            pass
    conf_file.close()
    return replace_sql.replace(', %s' % FIELD_TOKEN, '').replace(', %s' % VALUE_TOKEN, '')

if __name__ == '__main__':
    key_value = {'id': 888, 'city': 'beijing', 'loc': {'lat': 3.14, 'lng': 8.16}}
    print generateReplaceSql('database.conf', key_value)
