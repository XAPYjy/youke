from datetime import datetime
from datetime import timedelta

import pymysql
from back_system.common import es_


def time_str(d:timedelta):
    return '%s %s' %(d.days, d.seconds) # d.strftime('%Y-%m-%d %H:%M:%S')


def date_str(d):
    return d.strftime('%Y-%m-%d %H:%M:%S')


def search_tables():
    connect = pymysql.connect(host='47.92.132.161',
                              port=3306, user='root',
                              password='root', database='youke')

    with connect as cursor:
        sql = 'show tables'
        try:
            cursor.execute(sql)
            all = cursor.fetchall()
            for table in all:
                es_.remove_index('%s_index' % table[0])
                es_.create_index('%s_index' % table[0])

                cursor.execute('desc %s ' % table[0] )
                columns = [row[0] for row in  cursor.fetchall()]
                sql = 'select %s from %s' %(','.join(columns), table[0])
                cursor.execute(sql)

                for row in cursor.fetchall():
                    doc = {
                        col_name:(time_str(row[index])
                                  if isinstance(row[index], timedelta)
                                  else date_str(row[index]) if isinstance(row[index], datetime)
                                  else row[index])
                        for index, col_name in enumerate(columns)
                    }
                    print('adding %s %s' % (table[0], doc))
                    es_.add_doc(doc, table[0])
        except Exception as e:
            print(e)
            print('暂无数据')


if __name__ == '__main__':
    search_tables()