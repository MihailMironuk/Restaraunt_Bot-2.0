class Queries:
    DROP_CATEGORIES_TABLE = "DROP TABLE IF EXISTS categories;"
    DROP_DISHES_TABLE = "DROP TABLE IF EXISTS dishes;"

    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS surveys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            food TEXT,
            country TEXT,
            rating INTEGER
        );
    """

    CREATE_CATEGORIES_TABLE = """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        );
    """

    CREATE_DISHES_TABLE = """
        CREATE TABLE IF NOT EXISTS dishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            country TEXT,
            price FLOAT, 
            category INTEGER,
            FOREIGN KEY(category) REFERENCES categories(id)
        );
    """

    POPULATE_CATEGORIES = """
        INSERT INTO categories (name) VALUES
            ('бургеры'),
            ('мясо по-итальянски'),
            ('шашлычки');
    """

    POPULATE_DISHES = """
        INSERT INTO dishes (name, country, price, category) VALUES
            ('Дабл воппер от Тимати', 'Америка', 250.00, 1),
            ('Бургер от Гордона Рамзи', 'Великобритания', 19.00, 1),
            ('Габагул от Тони Сопрано', 'Италия', 1000.00, 2),
            ('Котлетки без пюрешки', 'Япония', 23000.00, 2),
            ('Шашлык из свинины по рецепту Юлии Высоцкой', 'Норвегия', 0.00, 3),
            ('Шашлычок и лучок на природе и при погоде', 'Россия', 1000000.00, 3);
    """
