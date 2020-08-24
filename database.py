from sqlite3 import Connection, Cursor


cursor = Connection('db.sqlite').cursor()


def add_post(post_id: int):
    cursor.execute(f'INSERT INTO `freelance_hunt_projects` (`id`) '
                   f'VALUES ({post_id})')
    cursor.connection.commit()


if __name__ == '__main__':
    # add_post(1212)
    # add_post(1223)
    pass
