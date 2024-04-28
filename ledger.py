import psycopg2 as psyco

print(psyco.__version__)

# Connection details (replace with your own)
DATABASE_URL = "postgresql://postgres@localhost:5432/postgres"

def create_item(name, description):
    with psyco.connect(DATABASE_URL) as conn:
      with conn.cursor() as cur:
        cur.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
        conn.commit() # Commit the changes to the database
      
def read_items():
    with psyco.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM items")
    return cur.fetchall() # Fetch all results as a list of tuples
  
def update_item(id, name, description):
    with psyco.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE items SET name = %s, description = %s WHERE id = %s", (name, description, id))
            conn.commit()
      
def delete_item(id):
    with psyco.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM items WHERE id = %s", (id,))
            conn.commit()
      
# Creating/inserting the record
create_item("New Item", "This is a new item.")
items = read_items()
print(items)

# Updating the record
update_item(1, "Updated Item", "This item has been updated.")

# Deleting the record
delete_item(2)