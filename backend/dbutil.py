import MySQLdb
import MySQLdb.cursors



def getData(list_symbols):
    list_dict_data = []
    dbcon = MySQLdb.connect(
        host='18.188.218.82', user='riapro', passwd='Riapro123$',
        db='riapro', cursorclass=MySQLdb.cursors.DictCursor)

    cursor = dbcon.cursor()
    formatted_symbols=map(lambda  x: "'"+x+"'",list_symbols)
    symbols = ','.join(formatted_symbols)
    query = "SELECT * from list_symbol where symbol in ({})".format(symbols)
    print query
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        list_dict_data.append(row)
    dbcon.close()
    return list_dict_data