import bcrypt
from db_connect import create_connection

def create_user(username, password, role='user'):
    conn = create_connection()
    if not conn:
        print("Failed to connect to database.")
        return

    try:
        cursor = conn.cursor()
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        query = "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, hashed.decode('utf-8'), role))
        conn.commit()
        print("User created successfully.")
    except Exception as e:
        print(f"Error creating user: {e}")
    finally:
        conn.close()

# ✅ Run it
# Backend/main.py
# This code creates a new user in the database with a hashed password.
# It uses bcrypt for hashing and connects to the database using a function from db_connect.py.
# The user is created with a default role of 'user', but can be set to 'admin' or other roles as needed.
# This code creates a new user in the database with a hashed password.
# It uses bcrypt for hashing and connects to the database using a function from db_connect.py.
# The user is created with a default role of 'user', but can be set to 'admin' or other roles as needed.

from auth import verify_user
is_validd = verify_user("admin", "admin123")
print("Login successful!" if is_validd else "Login failed!")
# This code verifies the credentials of a user by checking the provided password against the stored hash in the database.
# It uses the verify_user function from auth.py to check if the login is successful or not.     

from auth import log_access

log_access(1, "Logout")
log_access(1, "Access Denied")
# This code logs user actions such as logout and access denial.
# It uses the log_access function from auth.py to record these actions in the database.
# The user ID and action are passed as parameters to the function, which handles the database connection and logging.   

from auth import view_logs_by_user
view_logs_by_user(1)  # Replace 1 with actual user ID
# This code retrieves and displays access logs for a specific user. 