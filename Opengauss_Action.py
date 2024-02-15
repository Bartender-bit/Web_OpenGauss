import jaydebeapi

def connect():
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    return conn.cursor()

def verify(username, user_password, role):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    sql = 'SELECT * FROM '+ role +' WHERE ' + role + '_account=' + username +' AND '+ role + '_password=' + '\'%s\''%user_password +';'
    print("sql: ", sql)
    try:
        curs.execute(sql)
        result = curs.fetchall()
        print("Login success: ", result)
        curs.close()
        conn.close()
        return result
    except:
        print("Login failed....")
        result=[]
        curs.close()
        conn.close()
        return result

def verify_admin(username, user_password):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    print("un ",username , "paswd", password)
    #sql = 'SELECT * FROM admin WHERE admin_account= ' + username + ' AND admin_password=' + '\'%s\''%user_password +';'
    sql = 'SELECT * FROM admin_new WHERE admin_account=1071518 AND admin_password=\'123456\';'
    print("sql: ", sql)
    try:
        curs.execute(sql)
        result = curs.fetchall()
        print("Login Admin success: ", result)
        curs.close()
        conn.close()
        return result
    except:
        print("Login Admin failed....")
        result=[]
        curs.close()
        conn.close()
        return result

def register_reader(username, user_password):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    sql = 'INSERT INTO reader VALUES ' + '(\'' + username +'\',\''+ user_password + '\')' + ';'
    print("sql: ", sql)
    curs.execute(sql)
    sql = 'SELECT * FROM reader WHERE reader_account=' + username +' AND reader_password=' + '\'%s\''%user_password +';'
    print("sql: ", sql)

    curs.execute(sql)
    result = curs.fetchall()
    curs.close()
    conn.close()
    if len(result)!=0:
        return 1
    else:
        return 0


def register_author(username, user_password,authorname):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    sql = 'INSERT INTO author VALUES ' + '(\'' + username + '\',\'' + authorname + '\',\'' + user_password + '\')' + ';'
    #INSERT INTO author VALUES ('15789123421','爱吃西红柿','tbc123');

    try:
        print("sql: ", sql)
        curs.execute(sql)
        sql = 'SELECT * FROM author WHERE author_account=' + username + ' AND author_password=' + '\'%s\'' % user_password + ';'
        print("sql: ", sql)
        curs.execute(sql)
        result = curs.fetchall()
        curs.close()
        conn.close()
        return result
    except:
        print("Login author failed....")
        result=[]
        curs.close()
        conn.close()
        return result

def get_reader_novels(username):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    sql = 'SELECT * FROM reader_novel WHERE ' + 'reader_novel_account = ' + username + ';'
    print("sql: ",sql)
    curs.execute(sql)
    result = curs.fetchall()
    print(result)
    curs.close()
    conn.close()
    # print("len(curs.fetchall() ",type(result))
    # return 1
    if len(result) != 0:
        return result
    else:
        return result

def get_author_novels(username):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    print("in")
    sql = 'SELECT * FROM novel_info WHERE ' + 'author_novel_account = ' + username + ';'
    print("sql: ", sql)
    curs.execute(sql)
    result = curs.fetchall()
    print(result)
    curs.close()
    conn.close()
    # print("len(curs.fetchall() ",type(result))
    # return 1
    return result

def get_novel_content(novel_id):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    sql = 'SELECT * FROM novel_info WHERE novel_id = ' + novel_id + ';'
    # print("sql: ", sql) SELECT * FROM novel_info WHERE novel_id = 0;
    curs.execute(sql)
    result = curs.fetchall()
    #print(result)
    curs.close()
    conn.close()
    # print("len(curs.fetchall() ",type(result))
    # return 1
    if len(result) != 0:
        return result
    else:
        return 0

def get_novels_info():
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;"""
    curs.execute(sqlStr)
    sql = 'SELECT * FROM novel_info;'
    try:
        curs.execute(sql)
        result = curs.fetchall()
        print("小说商城内容: ", result)
        return result
    except:
        print("小说商城内容获取失败")
        result = []
        curs.close()
        conn.close()
        return result

def get_novel_chapter(novel_id):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    sql = 'SELECT * FROM novel_chapter_' + novel_id + ' order by chapter_id;'
    # print("sql: ", sql) SELECT * FROM novel_info WHERE novel_id = 0;
    try:
        curs.execute(sql)
        result = curs.fetchall()
        #print(result)
        curs.close()
        conn.close()
        return result
    except:
        print("Get chapter failed....")
        result=[]
        curs.close()
        conn.close()
        return result

    #new
    # if len(result) != 0:
    #     return result
    # else:
    #     return 0

def update_novel(novel_id, chapter_title, chapter_content):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    sql = 'INSERT INTO novel_chapter_' + novel_id + ' (book_id_chapter,chapter_title,chapter_content) VALUES'\
        '(\'' + novel_id + '\',\'' + chapter_title + '\',\'' + chapter_content + '\');'
    #INSERT INTO novel_chapter_0(book_id_chapter,chapter_title,chapter_content) VALUES ('0','九龙拉棺','这是新内容这是新内容这是新内容这是新内容');
    # print("sql: ", sql) SELECT * FROM novel_info WHERE novel_id = 0;
    try:
        curs.execute(sql)
        curs.close()
        conn.close()
    except:
        print("failed to update")
        curs.close()
        conn.close()

def reader_add_novel(novel_name, novel_id, username):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    #print("username ", username, "novel_name ", novel_name, "novel_id ", novel_id)
    sql = 'INSERT INTO reader_novel  VALUES(\''+ username+ '\', \'' + novel_name + '\', \'' + novel_id +'\'' + ');'
    #print("sql ", sql)
    try:
        curs.execute(sql)
        print("sql ", sql)
        sql = 'SELECT * FROM reader_novel WHERE reader_novel_account=' + username + ' AND reader_book_id='+ novel_id + ' ;'
        curs.execute(sql)
        result = curs.fetchall()
        curs.close()
        conn.close()
        print("添加小说到书架成功: ", result)
        return result
    except:
        print("添加小说失败")
        result = []
        curs.close()
        conn.close()
        return result

    #INSERT INTO reader_novel  VALUES('13702935388', '遮天', '0');

def delete_reader_novel(username, novel_id):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)

    sql = 'DELETE FROM reader_novel WHERE reader_novel_account = ' + username +' AND reader_book_id = ' + str(novel_id) +' ;'
    try:
        curs.execute(sql)
        print("删除成功")
        return 1
    except:
        print("删除失败")
        return 0

def delete_author(authorname):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    curs.execute("""DELETE FROM author WHERE author_account =? """,(authorname,))
    return 1
def delete_reader(readername):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    curs.execute("""DELETE FROM reader WHERE reader_account =? """,(readername,))
    return 1

def get_newid():
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;"""
    curs.execute(sqlStr)
    sql = 'SELECT count(*) FROM novel_info;'
    curs.execute(sql)
    result = curs.fetchall()
    print("result ", result)
    return result

def Create_newbook(book_id, username, authorname, novel_title, novel_intro):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    print("in create",book_id)
    sql = 'INSERT INTO novel_info (novel_name,author_novel_account,author_novel_name,novel_info,novel_type) VALUES (\'' + \
          novel_title + \
          '\',\'' + username + '\',\'' +  authorname + '\',\'' + novel_intro + \
          '\',\'' + str(0)+'\');'
    curs.execute(sql)
    # #sql = 'INSERT INTO reader_novel VALUES ('13702935388','盘龙','1');'

    sql1 = "CREATE TABLE novel_chapter_"+str(book_id)+" (book_id_chapter VARCHAR(100) NOT NULL,chapter_id serial PRIMARY KEY," \
                                                      "chapter_title VARCHAR(100) NOT NULL,chapter_content text NOT NULL DEFAULT '" \
                                                      "',FOREIGN KEY (book_id_chapter) REFERENCES novel_info(novel_id));"
    curs.execute(sql1)

def write_update(novel_id, chapter_title, chapter_content):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)

    sql = 'INSERT INTO novel_chapter_' + str(novel_id) + ' (book_id_chapter,chapter_title,chapter_content) VALUES'\
        '(\'' + str(novel_id) + '\',\'' + str(chapter_title) + '\',\'' + str(chapter_content) + '\');'
    #INSERT INTO novel_chapter_0(book_id_chapter,chapter_title,chapter_content) VALUES ('0','九龙拉棺','这是新内容这是新内容这是新内容这是新内容');
    # print("sql: ", sql) SELECT * FROM novel_info WHERE novel_id = 0;
    curs.execute(sql)
    curs.close()
    conn.close()
# def write_new_chapter(book_id, novel_title, novel_intro):
#     url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
#     user = 'project_maker'
#     password = 'user@123456'
#     dirver = 'org.postgresql.Driver'
#     jarFile = 'E:/School2/database/postgresql.jar'
#     conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
#     curs = conn.cursor()
#     sqlStr = """SET search_path TO db_schema;;"""
#     curs.execute(sqlStr)
#     sql = "INSERT INTO novel_chapter_0
# (book_id_chapter,chapter_title,chapter_content) VALUES ('0','九龙拉棺','这是新内容这是新内容这是新内容这是新内容');
# # def write_new_book(author_account,chapter_introduce,chapter_title,chapter_content):
# #     #len = select count(*) from novel_info
# #     # Create table novel_chapter_len ();
# #     #Insert novel_info_(bookname author type)
# #     # Insert novel_chapter_len(chapter_title, chapter_content)
# #     # VALUES( '九龙拉棺', '这是新内容这是新内容这是新内容这是新内容');
def search_book(bookname):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    print(type(bookname))


    try:
        curs.execute("""SELECT * FROM novel_info WHERE novel_name= ?""", (bookname,))
        result = curs.fetchall()
        print("result ", result)
        curs.close()
        conn.close()
        print("搜索小说成功: ", result)
        return result
    except:
        print("搜索小说失败")
        result = []
        curs.close()
        conn.close()
        return result

def search_author(authorname):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)

    try:
        curs.execute("""SELECT * FROM novel_info WHERE author_novel_name= ?""", (authorname,))
        result = curs.fetchall()
        print("result ", result)
        curs.close()
        conn.close()
        print("搜索小说成功: ", result)
        return result
    except:
        print("搜索小说失败")
        result = []
        curs.close()
        conn.close()
        return result

def update_chapter_content(novel_id, chapter_id, chapter_new_content):
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    print("nov" , novel_id, "chapter_id ", chapter_id, " content ", chapter_new_content)


    try:
        curs.execute("UPDATE novel_chapter_%s" % str(novel_id) + " SET chapter_content=? WHERE chapter_id=?",
                     (str(chapter_new_content), chapter_id))
        curs.close()
        conn.close()
        print("修改章节成功")
        return 1
    except:
        print("修改章节失败")
        curs.close()
        conn.close()
        return 0

def get_author_list():
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    sql = 'SELECT * FROM author'
    curs.execute(sql)
    result = curs.fetchall()
    #print(result)
    curs.close()
    conn.close()
    return result
def get_reader_list():
    url = 'jdbc:postgresql://120.46.168.174:26000/db_project'
    user = 'project_maker'
    password = 'user@123456'
    dirver = 'org.postgresql.Driver'
    jarFile = 'E:/School2/database/postgresql.jar'
    conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
    curs = conn.cursor()
    sqlStr = """SET search_path TO db_schema;;"""
    curs.execute(sqlStr)
    sql = 'SELECT * FROM reader'
    curs.execute(sql)
    result = curs.fetchall()
    #print(result)
    curs.close()
    conn.close()
    return result