# 儲存書籍資料的列表
books = []

"""
函數：add_book
功能: 新增書籍，將輸入的書籍增加到books串列裡
輸入: 書名(title)、作者(author)、出版日期(publication_date)、ISBN、庫存(stock)
輸出: 書籍已新增成功!
"""


def add_book(title, author, publication_date, isbn, stock):
    book = {
        "title": title,
        "author": author,
        "publication_date": publication_date,
        "isbn": isbn,
        "stock": stock
    }
    books.append(book)
    print("\n書籍已新增成功！")


"""
函數：borrow_book
功能: 借閱書籍，將輸入的書籍(且在books串列裡查詢的到)借閱並改變庫存數量
輸入: 書名或ISBN(title_or_isbn)
輸出: 尚有庫存->借閱成功
      沒有庫存->書籍庫存不足
      沒有此書->找不到該書籍
"""


def borrow_book(title_or_isbn):
    for book in books:
        if title_or_isbn == book["title"] or title_or_isbn == book["isbn"]:
            if book["stock"] > 0:
                book["stock"] -= 1
                return f"\n書籍'{book['title']}'借閱成功"
            else:
                return "\n書籍庫存不足"
    return "\n找不到該書籍"


"""
函數：return_book
功能: 歸還書籍，將輸入的書籍(且在books串列裡查詢的到)歸還並改變庫存數量
輸入: 書名或ISBN(title_or_isbn)
輸出: 有該書籍->歸還成功
      沒有此書->找不到該書籍
"""


def return_book(title_or_isbn):
    for book in books:
        if title_or_isbn == book["title"] or title_or_isbn == book["isbn"]:
            book["stock"] += 1
            return f"\n書籍'{book['title']}'歸還成功"
    return "\n找不到該書籍"


"""
函數：search_book
功能: 查找書籍，將輸入的書籍(且在books串列裡查詢的到)之資料印出
輸入: 書名或ISBN(title_or_isbn)
輸出: 有該書籍->印出其書名(title)、作者(author)、出版日期(publication_date)、ISBN、庫存(stock)
      沒有此書->找不到該書籍
"""


def search_book(title_or_isbn):
    for book in books:
        if title_or_isbn == book["title"] or title_or_isbn == book["isbn"]:
            return f"\n書名：{book['title']}\n作者：{book['author']}\n出版日期：{book['publication_date']}\nISBN編號：{book['isbn']}\n庫存數量：{book['stock']}"
    return "\n找不到該書籍"
