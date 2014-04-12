#! encoding=utf-8
from django.db import connection
def tag_list(request):
    '''获取每个标签的文章数量'''
    cursor = connection.cursor()
    sql = "SELECT title, c FROM blog_tag RIGHT JOIN \
                (SELECT tag_id AS tid, COUNT(*) AS c \
                    FROM blog_blog_tags GROUP BY tag_id) AS t2\
            ON blog_tag.id=t2.tid";
    cursor.execute(sql) 
    tags = cursor.fetchall()
    ctx = {'tags':tags}
    return ctx 

