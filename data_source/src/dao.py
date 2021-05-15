import psycopg2


def insert(table, data, columns=None):
    """
    Database insert wrapper
    :param table: table name
    :param data: list of records
    :param columns: list of columns, None for all columns
    """
    if data:
        connection = psycopg2.connect(dbname='air_data', user='docker', password='docker', host='dbserver')
        cursor = connection.cursor()

        expression = f"INSERT INTO {table}{(' (' + ', '.join(columns) + ')') if columns else ''} VALUES " + \
                     ', '.join(f'({", ".join(_format_value(val) for val in row.values())})' for row in data)

        cursor.execute(expression)
        connection.commit()
        cursor.close()
        connection.close()


def _format_value(value):
    """
    Formats values to a format accepted by database
    :param value: a value to parse
    :return: parsed value
    """
    if isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'NULL'
    else:
        return str(value)


def select(table, columns, where=None):
    """
    Select wrapper
    :param table: table name
    :param columns: list of columns to select
    :param where: optional where condition
    :return: tuples returned from database
    """
    connection = psycopg2.connect(dbname='air_data', user='docker', password='docker', host='dbserver')
    cursor = connection.cursor()
    gen = (f'"{col}"' for col in columns)

    expression = f"SELECT {', '.join(gen)} FROM {table}"

    if where:
        expression += f" WHERE {where}"

    cursor.execute(expression)
    res = cursor.fetchall()
    cursor.close()
    connection.close()

    return res
