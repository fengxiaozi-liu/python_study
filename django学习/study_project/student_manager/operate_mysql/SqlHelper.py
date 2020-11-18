import pymysql


class SqlHelper:
    def __init__(self):
        self.connect_pymysql()

    def connect_pymysql(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='liu', passwd='lh284259', db='python_study',
                                    charset='utf8')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def get_all(self, sql, args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def get_one(self, sql, args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    def modify(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def multiple_modify(self, sql, args):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    def modify_get(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()
        last_row_id = self.cursor.lastrowid
        return last_row_id

    def close(self):
        self.cursor.close()
        self.conn.close()
