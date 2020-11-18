import pymysql


def get_formation(sql, args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='liu', passwd='lh284259', db='python_study',
                           charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def modify_formation(sql, args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='liu', passwd='lh284259', db='python_study',
                           charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()


def get_one(sql, args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='liu', passwd='lh284259', db='python_study',
                           charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def create(sql, args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='liu', passwd='lh284259', db='python_study',
                           charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    last_row_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return last_row_id



