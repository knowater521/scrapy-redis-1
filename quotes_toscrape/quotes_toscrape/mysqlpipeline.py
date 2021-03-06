import pymysql


class MysqlPipeline(object):
    """
    同步操作
    """
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost','root','123456','test')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
        table_sql = """create table if not exists test_zxf(quote varchar(100),author varchar(100),
                                      tags varchar(100),url varchar(100),born_date varchar(100),born_location varchar(100))
                      """
        self.cursor.execute(table_sql)
        self.conn.commit()
    def process_item(self,item,spider):
        # sql语句
        insert_sql = """
        insert into test_zxf(quote,author,tags,born_date,born_location) VALUES(%s,%s,%s,%s,%s)
        """
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql,(item['quote'],item['author'],item['tags'],item['born_date'],
                                        item['born_location']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self,spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

