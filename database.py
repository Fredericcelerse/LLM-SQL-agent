import duckdb

def connect_db(db_name="my_database.db"):
    conn = duckdb.connect(db_name)
    return conn

def setup_example_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER,
            date DATE,
            product VARCHAR,
            quantity INTEGER,
            unit_price DECIMAL(10,2),
            region VARCHAR
        )
    """)
    
    conn.execute("""
        INSERT INTO sales VALUES
        (1, '2024-01-15', 'Laptop', 5, 999.99, 'Europe'),
        (2, '2024-01-16', 'Smartphone', 10, 599.99, 'North America'),
        (3, '2024-01-17', 'Tablet', 8, 399.99, 'Asia'),
        (4, '2024-01-18', 'Laptop', 3, 999.99, 'Europe')
    """)

def execute_query(conn, sql_query):
    try:
        result = conn.execute(sql_query).fetchall()
        return result
    except Exception as e:
        return f"Error executing query: {str(e)}"
