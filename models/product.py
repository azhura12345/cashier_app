# /models/product.py
from services.db import get_connection

def get_products_by_category(category_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, price, discount, stock, image_path, width, depth, height 
        FROM products
        WHERE category_id = %s
    """, (category_id,))
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    return [dict(zip(columns, row)) for row in rows]
