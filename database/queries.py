class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS surveys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            food TEXT,
            country TEXT,
            rating INTEGER
        )
    """
    DROP_COUNTRIES_TABLE = "DROP TABLE IF EXISTS countries"
    CREATE_COUNTRIES_TABLE = """
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """
    DROP_FOOD_TABLE = "DROP TABLE IF EXISTS food"
    CREATE_FOOD_TABLE = """
        CREATE TABLE IF NOT EXISTS food (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price FLOAT,
            picture TEXT,
            country_id INTEGER,
            FOREIGN KEY(country_id) REFERENCES countries(id)
        )
    """
    POPULATE_COUNTRIES = """
        INSERT INTO countries (name) VALUES
            ('Америка'),
            ('Италия'),
            ('Норвегия')
    """
    POPULATE_FOOD = """
        INSERT INTO food (name, price, picture, country_id) VALUES
        ('Блэк стар бургер', 250.0, 'burger.jpg', 1),
        ('Габагул', 1000.0, 'meat.jpg', 2),
        ('Шашлык из свинины', 1000.0, 'shaslik.jpg', 3)
    """