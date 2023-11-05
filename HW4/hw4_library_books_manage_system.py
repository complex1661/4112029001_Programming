import manage_module as manage

# 主程式


def main():
    while True:
        print("""\n圖書管理系統
        1. 新增書籍
        2. 借閱書籍
        3. 歸還書籍
        4. 查詢書籍
        5. 退出""")

        choice = input("請選擇操作：")

        if choice == '1':
            title = input("輸入書名：")
            author = input("輸入作者：")
            publication_date = input("輸入出版日期：")
            isbn = input("輸入ISBN編號：")
            stock = int(input("輸入庫存數量："))
            manage.add_book(title, author, publication_date, isbn, stock)
        elif choice == '2':
            title_or_isbn = input("輸入書名或ISBN編號：")
            result = manage.borrow_book(title_or_isbn)
            print(result)
        elif choice == '3':
            title_or_isbn = input("輸入書名或ISBN編號：")
            result = manage.return_book(title_or_isbn)
            print(result)
        elif choice == '4':
            title_or_isbn = input("輸入書名或ISBN編號：")
            result = manage.search_book(title_or_isbn)
            print(result)
        elif choice == '5':
            print("感謝使用圖書管理系統！")
            break
        else:
            print("請輸入有效的選項。")


if __name__ == '__main__':
    main()
