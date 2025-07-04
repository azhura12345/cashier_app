# /cashier_app/models/product.py

from services.db import fetch_all

def get_all_products():
    query = "SELECT * FROM products ORDER BY id"
    return fetch_all(query)

def get_products_by_category(category_name):
    query = """
        SELECT p.*
        FROM products p
        JOIN categories c ON p.category_id = c.id
        WHERE c.name = %s
        ORDER BY p.id
    """
    return fetch_all(query, (category_name,))
