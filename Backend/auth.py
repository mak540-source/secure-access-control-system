import bcrypt
from db_connect import create_connection

# This module handles user authentication, including password verification.
def verify_user(username, password):
    conn = create_connection()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        query = "SELECT id, password_hash FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result:
            user_id = result[0]
            stored_hash = result[1].encode('utf-8')
            success = bcrypt.checkpw(password.encode('utf-8'), stored_hash)

            # Log access
            action = "Login Success" if success else "Login Failed"
            log_access(user_id, action)

            return success
        else:
            print("User not found.")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        conn.close()
# This module handles user registration and access logging.

# This function registers a new user in the users table with a hashed password.
def register_user(username, password, role='user'):
    conn = create_connection()
    if conn is None:
        print("Failed to connect to database.")
        return 
    
    cursor = conn.cursor()

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        # Insert user into the database
        cursor.execute("""
            INSERT INTO users (username, password_hash, role)
            VALUES (%s, %s, %s)
        """, (username, hashed_password.decode('utf-8'), role))

        conn.commit()
        print("User registered successfully.")

    except Exception as e:
        print(f"Error registering user: {e}")

    finally:
        cursor.close()
        conn.close()

def log_access(user_id, action):
    conn = create_connection()
    if conn is None:
        print("Failed to connect to database.")
        return

    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO access_logs (user_id, action)
            VALUES (%s, %s)
        """, (user_id, action))
        conn.commit()
    except Exception as e:
        print(f"Error logging access: {e}")
    finally:
        cursor.close()
        conn.close()

def view_logs_by_user(user_id):
    conn = create_connection()
    if conn is None:
        print("Failed to connect to database.")
        return

    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT action, timestamp FROM access_logs
            WHERE user_id = %s
            ORDER BY timestamp DESC
        """, (user_id,))
        logs = cursor.fetchall()
        print(f"\nAccess log for user ID {user_id}:")
        for action, timestamp in logs:
            print(f"{timestamp}: {action}")
    except Exception as e:
        print(f"Error retrieving logs: {e}")
    finally:
        cursor.close()
        conn.close()
# This code verifies the credentials of a user by checking the provided password against the stored hash in the database.
# It uses the verify_user function to check if the login is successful or not.
# If successful, it logs the action as "Login Success"; otherwise, it logs "Login Failed".
# The function returns True for a successful login and False otherwise. 
