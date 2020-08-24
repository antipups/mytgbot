from sqlite3 import Connection, Cursor


def add_post(post_id: int):
    """
        Добавление поста в БД
    :param post_id: int > 0
    :return:
    """
    with Connection('db.sqlite') as connect:
        cursor = connect.cursor()
        cursor.execute(f'INSERT INTO `freelance_hunt_projects` (`id`) '
                       f'VALUES ({post_id})')
        cursor.connection.commit()


def check_post(post_id: int) -> bool:
    """
        Проверка наличия поста в БД
    :param post_id:
    :return:
    """
    with Connection('db.sqlite') as connect:
        cursor = connect.cursor()
        cursor.execute('SELECT * '
                       'FROM freelance_hunt_projects')
        return not bool(cursor.fetchall())


if __name__ == '__main__':
    # add_post(1212)
    # add_post(1223)
    # check_post(1)
    pass
