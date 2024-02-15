import jaydebeapi
import random

url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
user = 'project_maker'
password = 'user@123456'
dirver = 'org.postgresql.Driver'
jarFile = 'E:/School2/database/postgresql.jar'
author_account = [
    ['15789123421', '爱吃西红柿'],
    ['11247891235', '辰东'],
    ['98721392134', '潜水乌贼'],
    ['58721324131', '刘慈欣'],
    ['124124', '新显示'],
    ['1231238', 'b'],
    ['9798012345', '瓦德'],
    ['9798324131', '青蛙'],
    ['4134123561', '墨香铜臭'],
    ['1254112365', '天蚕土豆']
]
novel_name = ['A','B','C','D','E','F','G','H','I','J']
novel_type =[0, 1, 2, 3, 4, 5, 6]
conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
curs = conn.cursor()
sqlStr = """SET search_path TO db_schema;"""
curs.execute(sqlStr)


# sqlStr4 = """CREATE TABLE novel_info
# (
#         novel_id serial PRIMARY KEY,
#         novel_name VARCHAR(100) NOT NULL,
#         author_novel_account VARCHAR(15) NOT NULL,
#         author_novel_name VARCHAR(100) NOT NULL,
#         novel_info text NOT NULL DEFAULT '',
#         novel_type VARCHAR(5) CHECK(novel_type>=0 AND novel_type<=6),
#         thumbs_up INT NOT NULL DEFAULT 0,
#         FOREIGN KEY (author_novel_account) REFERENCES author(author_account)
# );"""
# INSERT INTO novel_info
# (novel_name,author_novel_account,author_novel_name,novel_info,novel_type) VALUES (
# '三体','58721324131','刘慈欣',
# '光年四百年外正是三体行球，科技远不如他们的地球人如何抵抗即将到来的危机?','5');
for i in range(970000):
    random_author_account = author_account[random.randint(0, 9)]
    random_novel_name = novel_name[random.randint(0, 9)] + novel_name[random.randint(0, 9)]
    random_novel_info = novel_name[random.randint(0, 9)] + novel_name[random.randint(0, 9)] + novel_name[random.randint(0, 9)]
    random_novel_type = novel_type[random.randint(0, 6)]

    print("(%s,"%random_novel_name, random_author_account[0], ",", random_author_account[1]
          , ",", random_novel_info , "," , random_novel_type, ");")

    sql = 'INSERT INTO novel_info (novel_name,author_novel_account,author_novel_name,novel_info,novel_type) VALUES (\'' + \
          random_novel_name + \
          '\',\'' + random_author_account[0] + '\',\'' + random_author_account[1] + '\',\'' + random_novel_info + \
          '\',\'' + str(random_novel_type)+'\');'
    # #sql = 'INSERT INTO reader_novel VALUES ('13702935388','盘龙','1');'
    curs.execute(sql)
curs.close()
conn.close()
#

#author : account  name  pass







#result = curs.fetchall()
#sqlStr3 = 'SELECT * FROM client'
#print(result)
#curs.execute(sqlStr2)
#curs.execute(sqlStr3)
#print(curs.fetchall())

#print(result)

curs.close()

conn.close()

