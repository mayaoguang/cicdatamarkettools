import pymysql

class Mysqldb:
    def getCon(self):
        try:
            conn = pymysql.connect(host='127.0.0.1', user='root',passwd='xxx', db='xxx', port=3306, charset='utf8')
            return conn
        except MySQLdb.Error as e:
            print("Mysqldb con Error:%s");

    def select(self, sql):
        try:
            con = self.getCon()
            cur = con.cursor()
            cur.execute(sql)
            fc = cur.fetchall()
            return fc
        except MySQLdb.Error as e:
            print("Mysqldb select Error:%s");
        finally:
            cur.close()
            con.close()

    def updateByParam(self, sql, params):
        try:
            con = self.getCon()
            cur = con.cursor()
            count = cur.execute(sql, params)
            con.commit()
            return count
        except MySQLdb.Error as e:
            con.rollback()
            print("Mysqldb updateByParam Error:%s");
        finally:
            cur.close()
            con.close()

    def update(self, sql):
        try:
            con = self.getCon()
            cur = con.cursor()
            count = cur.execute(sql)
            con.commit()
            return count
        except MySQLdb.Error as e:
            con.rollback()
            print("Mysqldb update Error:%s");
        finally:
            cur.close()
            con.close()

    def insert(self, sql):
        try:
            con = self.getCon()
            cur = con.cursor()
            count = cur.execute(sql)
            con.commit()
            return count
        except MySQLdb.Error as e:
            con.rollback()
            print("Mysqldb insert Error:%s");
        finally:
            cur.close()
            con.close()
    def delete(self, sql):
        try:
            con = self.getCon()
            cur = con.cursor()
            count = cur.execute(sql)
            con.commit()
            return count
        except MySQLdb.Error as e:
            con.rollback()
            print("Mysqldb delete Error:%s");
        finally:
            cur.close()
            con.close()
"""
if __name__ == "__main__":
    db = Mysqldb()

    fc = db.selectALL("select id from eth_pending")
    print(fc)
"""



