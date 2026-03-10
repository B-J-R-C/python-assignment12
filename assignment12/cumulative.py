import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def main():
    conn = sqlite3.connect('../db/lesson.db')

    # Query to get total_price per order
    query = """
    SELECT o.order_id, SUM(p.price * l.quantity) AS total_price 
    FROM orders o 
    JOIN line_items l ON o.order_id = l.order_id 
    JOIN products p ON l.product_id = p.product_id 
    GROUP BY o.order_id
    ORDER BY o.order_id;
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    # Add cumulative column using cumsum()
    df['cumulative'] = df['total_price'].cumsum()

    # Create a line plot
    df.plot.line(x='order_id', y='cumulative', color='green', marker='o', figsize=(10, 6))

    # Add titles labels
    plt.title('Cumulative Revenue Over Time (by Order ID)')
    plt.xlabel('Order ID')
    plt.ylabel('Cumulative Revenue ($)')
    plt.grid(True)
    
    # Show plot
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()