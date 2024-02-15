from flask import Flask, render_template, request, redirect, url_for
import Opengauss_Action
app = Flask(__name__)


@app.route('/reader_home/<trans_username>', methods=['GET', 'POST'])
def reader_home(trans_username):
    print("reader_user ", trans_username)
    results = Opengauss_Action.get_reader_novels(trans_username)
    flag = len(results)
    if flag != 0:
        print(trans_username + " novels = ", results)
        return render_template('reader_home.html', username=trans_username, novels=results)
    else:
        results=[]
        print("该读者没有收藏书")
        return render_template('reader_home.html', username=trans_username,novels=results)

#实现读者跳转到书籍页面
@app.route('/author_to_novel/<novel_id>')
def author_to_novel(novel_id):
    print("novelid: ", novel_id)
    results = Opengauss_Action.get_novel_content(novel_id)
    novel_chapters = Opengauss_Action.get_novel_chapter(novel_id)
    flag = len(results)
    if flag != 0:
        #print(trans_username + " novels = ", results)
        print("novel_info : ", results)
        print("novel_chapters : ", novel_chapters)
        return render_template('author_novel_info.html', novels=results, chapters=novel_chapters)
    else:
        print("该书没有章节")
        return render_template('author_novel_info.html', novels='failed to get book')

@app.route('/set_to_novel/<novel_id>/<chapter_id>' , methods=['GET', 'POST'])
def set_to_novel(novel_id, chapter_id):
    print("novelid: ", novel_id)
    print("chapterid: ", chapter_id)

    novel_chapters = Opengauss_Action.get_novel_chapter(novel_id)
    read_chapter_content = novel_chapters[int(chapter_id)-1]
    print("novel_chapters: ", read_chapter_content)
    if request.method == 'POST':
        chapter_new_content = request.form.get('chapter_new_content')
        print( "chapter_new_content ", chapter_new_content)
        results = Opengauss_Action.update_chapter_content(novel_id, chapter_id, chapter_new_content)
        print("set result: ", results)
        return redirect(url_for('author_to_novel', novel_id=novel_id))
    flag = len(novel_chapters)
    if flag != 0:
        #print(trans_username + " novels = ", results)
        #print("novel_chapters : ", novel_chapters)
        return render_template('change_chapter_content.html', chapters=novel_chapters[int(chapter_id)-1])
    else:
        print("该读者没有收藏书")
        return render_template('change_chapter_content.html', chapters='')

#实现读者跳转到书籍页面
@app.route('/reader_to_novel/<novel_id>')
def reader_to_novel(novel_id):
    print("novelid: ", novel_id)
    results = Opengauss_Action.get_novel_content(novel_id)
    novel_chapters = Opengauss_Action.get_novel_chapter(novel_id)
    flag = len(results)
    if flag != 0:
        #print(trans_username + " novels = ", results)
        print("novel_info : ", results)
        print("novel_chapters : ", novel_chapters)
        return render_template('novel_info.html', novels=results, chapters=novel_chapters)
    else:
        print("该读者没有收藏书")
        return render_template('novel_info.html', novels='failed to get book')

@app.route('/reader_novels_store/<trans_username>', methods=['GET', 'POST'])
def reader_novels_store(trans_username):
    if request.method == 'POST':
        print("in post")
        book_name = request.form.get('search_bookname')
        author_name = request.form.get('search_authorname')
        print("authorname", author_name, " bookname ", book_name)
        if len(book_name) != 0:
            results = Opengauss_Action.search_book(book_name)
            print("store_search_result " ,results)
            return render_template('reader_novels_store.html', username=trans_username, novels=results)
        else:
            results = Opengauss_Action.search_author(author_name)
            print("store_search_result " ,results)
            return render_template('reader_novels_store.html', username=trans_username, novels=results)
    print("reader_novels_store: ", trans_username)
    results = Opengauss_Action.get_novels_info()
    flag = len(results)
    if flag != 0:
        print("result = ", results)
        # (0,'仙侠'),(1,'都市'),(2,'言情'),(3,'历史'),(4,'网游'),(5,'科幻'),(6,'恐怖');
        return render_template('reader_novels_store.html', username=trans_username, novels=results)
    else:
        print("该读者没有收藏书")
        return render_template('reader_novels_store.html', username=trans_username, novels=results)
#读者添加书
@app.route('/reader_add_novel/<novel_name>/<novel_id>/<username>', methods=['GET', 'POST'])
def reader_add_novel(novel_name, novel_id, username):
    print("reader_add_novel_id: ", novel_id, " reader: ", username)
    results = Opengauss_Action.reader_add_novel(novel_name, novel_id, username)
    flag = len(results)
    if flag != 0:
        print("result = ", results)
        return redirect(url_for('reader_home', trans_username=username))
    else:
        print("该读者没有收藏书")
        return redirect(url_for('reader_home', trans_username=username))

#实现读者删除书籍
@app.route('/reader_delete_novel/<novel_id>/<username>')
def reader_delete_novel(novel_id, username):
    print("delete novelid = ", novel_id, "username = ", username)
    flag = Opengauss_Action.delete_reader_novel(username, novel_id)
    if flag != 0:
        return redirect(url_for('reader_home', trans_username=username))
    else:
        return redirect(url_for('reader_home', trans_username=username))

@app.route('/update_to_novel/<novel_id>' , methods=['GET', 'POST'])
def update_to_novel(novel_id):
    if request.method == 'POST':
        chapter_title = request.form.get('new_chapter_title')
        chapter_content = request.form.get('new_chapter_content')
        print("novel_id ",novel_id, "chapter_title: ", chapter_title, "chapter_content: ", chapter_content)
        results = Opengauss_Action.update_novel(novel_id, chapter_title, chapter_content)
        print("result ",results)
        results = Opengauss_Action.get_novel_content(novel_id)
        novel_chapters = Opengauss_Action.get_novel_chapter(novel_id)
    return render_template('update_novel.html')

@app.route('/author_home/<trans_username>?<trans_authorname>', methods=['GET', 'POST'])
def author_home(trans_username, trans_authorname):
    print("autho_user ", trans_username, "author_name", trans_authorname)
    results = Opengauss_Action.get_author_novels(trans_username)
    print("author_write_book: ", results)
    #[(0, '遮天', '11247891235', '辰东', '在破败中崛起，在寂被打开了，一个全新的世界就此揭开神秘的一角……', '0', 0)]
    flag = len(results)
    if flag != 0:
        print(trans_username + " novels = ", results)
        return render_template('author_home.html', username=trans_username, authorname=trans_authorname, novels=results)
    else:
        print("该作者没有收藏书")
        return render_template('author_home.html', username=trans_username, authorname=trans_authorname, novels=results)

#?<chapter_id>
@app.route('/novel_to_chapter/<novel_id>/<chapter_id>')
def novel_to_chapter(novel_id, chapter_id):
    print("novelid: ", novel_id)
    print("chapterid: ", chapter_id)
    #results = Opengauss_Action.get_novel_content(novel_id)
    novel_chapters = Opengauss_Action.get_novel_chapter(novel_id)
    read_chapter_content = novel_chapters[int(chapter_id)-1]
    print("novel_chapters: ", read_chapter_content)
    flag = len(novel_chapters)
    if flag != 0:
        #print(trans_username + " novels = ", results)
        #print("novel_chapters : ", novel_chapters)
        return render_template('chapter_content.html', chapters=novel_chapters[int(chapter_id)-1])
    else:
        print("该读者没有收藏书")
        return render_template('chapter_content.html', chapters='')

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        authorname = request.form.get('author_name')
        print("authorname", authorname)
        #author_check_box = request.form.getlist("flexRadioDefault")
        check_box_value = request.form.get("flexRadioDefault")
        print("user: ", username, "passwd: ", password, "check_box_value: ", check_box_value)
        if (check_box_value == 'login_admin'):  # 登录管理员
            result = Opengauss_Action.verify_admin(username, password)
            flag = len(result)
            #
            print("flag ", flag)
            if flag == 1:
                print("Login to admin_home.html .....")
                return redirect(url_for('admin_home', trans_username=username))
            else:
                print("管理员账户名或者密码错误")
                return redirect('/')

        elif(check_box_value == 'login_reader'):  #登录读者
            result = Opengauss_Action.verify(username, password,'reader')
            flag = len(result)
            #
            print("flag ", flag)
            if flag == 1:
                print("Login to reader_home.html .....")
                return redirect(url_for('reader_home', trans_username=username))
            else:
                print("读者账户名或者密码错误")
                return redirect('/')
        elif (check_box_value == 'regist_reader'):  #注册读者
            flag = Opengauss_Action.register_reader(username, password)
            if flag == 1:
                print("Register to reader_home .....")
                return redirect(url_for('reader_home', trans_username=username))
            else:
                print("注册读者失败，请确保您输入账号小于等于11位")
                return redirect('/')


        elif(check_box_value == 'login_author'):    #登录作者
            result = Opengauss_Action.verify(username, password, 'author')
            print("result", result[0][1])
            flag = len(result)
            if flag == 1:
                print("Login to author_home.html .....")
                print(url_for('author_home', trans_username=username, trans_authorname=result[0][1]))
                return redirect(url_for('author_home', trans_username=username, trans_authorname=result[0][1]))
            else:
                print("作者账户名或密码错误")
                return redirect('/')

        elif (check_box_value == 'regist_author'):  #注册作者
            result = Opengauss_Action.register_author(username, password, authorname)
            print("result", result[0][1])
            flag = len(result)
            if flag == 1:
                print("Register to author_home .....")
                return redirect(url_for('author_home', trans_username=username, trans_authorname=result[0][1]))
            else:
                print("注册作者失败")
                return redirect('/')
    return render_template('homepage.html')

@app.route('/admin_home/<trans_username>', methods=['GET', 'POST'])
def admin_home(trans_username):
    print("admin:  ", trans_username)
    author_list = Opengauss_Action.get_author_list()
    reader_list = Opengauss_Action.get_reader_list()
    return render_template('admin_home.html', username=trans_username, authors=author_list, readers=reader_list)


@app.route('/delete_author/<author>/<trans_username>', methods=['GET', 'POST'])
def delete_author(author, trans_username):
    print("delete_author:  ", author)
    flag = Opengauss_Action.delete_author(author)
    return redirect(url_for('admin_home', trans_username=trans_username))
@app.route('/delete_reader/<reader>/<trans_username>', methods=['GET', 'POST'])
def delete_reader(reader, trans_username):
    print("delete_author:  ", reader)
    flag = Opengauss_Action.delete_reader(reader)
    return redirect(url_for('admin_home', trans_username=trans_username))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        return redirect('/admin')
    return render_template('login.html')

@app.route('/write_new_novel/<authorname>/<username>', methods=['GET', 'POST'])
def write_new_novel(username, authorname):


    if request.method == 'POST':
        book_id = Opengauss_Action.get_newid()[0][0]
        print("book_id1 ", book_id)
        novel_title = request.form.get('novel_title')
        novel_intro = request.form.get('novel_introduce')
        print(novel_title, novel_intro)
        Opengauss_Action.Create_newbook(book_id, username, authorname, novel_title, novel_intro)
        print("book_id after_create ", book_id)
        #Opengauss_Action.update_novel(book_id, novel_title, novel_intro)

        return redirect(url_for('author_home', trans_username=username, trans_authorname=authorname))

    return render_template('create_new_table.html', username=username, authorname=authorname)

@app.route('/user_home', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html',student='abc')

if __name__ == '__main__':
    app.run()