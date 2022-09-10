import pymysql

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "abc@123",
    "db": "test",
    "charset": "utf8"
}

try:
    # Create Connection
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        #SELECT
        # command = "SELECT * FROM tb_test"
        # cursor.execute(command)
        # result = cursor.fetchall()
        # print(result)
        # print(result[0][1])
        
        # INSERT
        # command = "INSERT INTO tb_test(id, name)VALUES(001, 'betsy')"
        # cursor.execute(command)
        # conn.commit()

        # DELETE
        # command = "DELETE FROM tb_test where ID =1"
        # cursor.execute(command)
        # conn.commit()

        # UPDATE
        command = "UPDATE tb_test SET NAME = 'betsy1' where ID =1"
        cursor.execute(command)
        conn.commit()


except Exception as ex:
    
    print('Conncetion Failed!')
    print(ex)