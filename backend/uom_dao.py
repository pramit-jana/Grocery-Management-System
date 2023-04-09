from sql_connection import get_sql_connection


def get_uoms(connection):
    cursor=connection.cursor()
    query=("SELECT * FROM uom")
    cursor.execute(query)
    respose=[]
    for (uom_id,uom_name) in cursor:
        respose.append({
            'uom_id':  uom_id,
            'uom_name':uom_name
        })

    return respose


if __name__=='__main__':
    connection=get_sql_connection()
    get_uoms(connection)
    print(get_uoms(connection))

