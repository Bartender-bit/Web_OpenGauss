import jaydebeapi
#初始化数据库表
url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
user = 'project_maker'
password = 'user@123456'
dirver = 'org.postgresql.Driver'
jarFile = 'E:/School2/database/postgresql.jar'

conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
curs = conn.cursor()

#
sqlStr = """SET search_path TO db_schema;;"""
#author : account  name  pass
sqlStr0 = """CREATE TABLE admin_new
(
        admin_account VARCHAR(15) PRIMARY KEY,
        admin_password VARCHAR(30) NOT NULL
);"""
sqlStr1 = """CREATE TABLE reader
(
        reader_account VARCHAR(15) PRIMARY KEY,
        reader_password VARCHAR(30) NOT NULL
);"""

#author : account  name  pass
sqlStr2 = """CREATE TABLE author
(
        author_account VARCHAR(15) PRIMARY KEY,
        author_name VARCHAR(100) NOT NULL,
        author_password VARCHAR(30) NOT NULL
);"""

sqlStr3 = """CREATE TABLE reader_novel
(
        reader_novel_account VARCHAR(15) NOT NULL,
        novel_name VARCHAR(100) NOT NULL,
        reader_book_id VARCHAR(10) NOT NULL,
        PRIMARY KEY (reader_novel_account,novel_name),
        FOREIGN KEY (reader_novel_account) REFERENCES reader(reader_account),
        FOREIGN KEY (reader_book_id) REFERENCES novel_info(novel_id)
);"""

sqlStr4 = """CREATE TABLE novel_info
(
        novel_id serial PRIMARY KEY,
        novel_name VARCHAR(100) NOT NULL,
        author_novel_account VARCHAR(15) NOT NULL,
        author_novel_name VARCHAR(100) NOT NULL,
        novel_info text NOT NULL DEFAULT '',
        novel_type VARCHAR(5) CHECK(novel_type>=0 AND novel_type<=6),
        thumbs_up INT NOT NULL DEFAULT 0,
        FOREIGN KEY (author_novel_account) REFERENCES author(author_account)
);"""

sqlStr5 = """CREATE TABLE novel_chapter_0
(
        book_id_chapter VARCHAR(100) NOT NULL,
        chapter_id serial PRIMARY KEY,
        chapter_title VARCHAR(100) NOT NULL,
        chapter_content text NOT NULL DEFAULT '',
        FOREIGN KEY (book_id_chapter) REFERENCES novel_info(novel_id)
);"""




curs.execute(sqlStr)
curs.execute(sqlStr1)
curs.execute(sqlStr2)
curs.execute(sqlStr3)
curs.execute(sqlStr4)


#result = curs.fetchall()
#sqlStr3 = 'SELECT * FROM client'
#print(result)
#curs.execute(sqlStr2)
#curs.execute(sqlStr3)
#print(curs.fetchall())

#print(result)

curs.close()

conn.close()

