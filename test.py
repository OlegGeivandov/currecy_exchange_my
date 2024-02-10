import pymysql

connection = pymysql.connect(host='192.168.1.46', user = 'obmen', password = '123456', database='bank', port=3306)
cursor = connection.cursor()
cursor.execute('select * from valute_rate')

# cursor.execute('SELECT rate  from valute_rate  WHERE valute = "USD" AND  date  = "20240202";')



print(cursor.fetchall())
# print(type(cursor.fetchall()))
#
# # print(cursor.fetchall()[0])
#
# print(float(cursor.fetchall()[0][0]))


# # список
# my_list1 = ['20240118', 'AUD', '58.046']
# print(my_list1)
# print(my_list1[2])
# print(float( my_list1[2]))
#
# # список списков
# my_list2 = [['20240118', 'AUD', '58.046'], ['20240118', 'AZN', '51.931']]
# print(my_list2)
# print(my_list2[1])
# print( my_list2[1][2])

# # кортеж
# my_tuple1 = ('20240118', 'AUD', '58.046')
# print(my_tuple1)
# print(my_tuple1[2])
# print(float( my_tuple1[2]))
#
# my_tuple2 = ('90.663',)
# print(my_tuple2)
# print(my_tuple2[0])



# список кортежей


# кортеж кортежей
my_tuple3 = (('90.663',),)
print(my_tuple3)
print(my_tuple3[0])
print(my_tuple3[0][0])

