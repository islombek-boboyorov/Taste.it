from django.db import connection
from contextlib import closing


def get_about():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
        select * from taste_about
        """)
        about = dict_fetchall(cursor)
    return about


def get_menu():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from taste_menu""")
        men = dict_fetchall(cursor)
    return men


def get_chef():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from taste_chef""")
        chefs = dict_fetchall(cursor)
    return chefs


def get_author():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select a_name, a_image, a_description from taste_blog""")
        chefs = dict_fetchall(cursor)
    return chefs


def get_blog_id(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from taste_blog where id = %s""", [pk])
        blog = dict_fetchone(cursor)
    return blog


def get_blog():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from taste_blog""")
        blog = dict_fetchall(cursor)
    return blog


def get_our():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from taste_our""")
        blog = dict_fetchall(cursor)
    return blog


def get_product():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from taste_product""")
        blog = dict_fetchall(cursor)
    return blog




def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row))
            for row in cursor.fetchall()]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
