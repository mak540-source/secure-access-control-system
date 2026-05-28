# Secure Access Control System

A simple authentication system built with Python and MySQL. It features secure password hashing, role-based user registration, login verification, action logging, and access log review functionality.

## 🔒 Features

- User registration with bcrypt password hashing
- Secure login verification with hashed password check
- Role-based user creation (e.g., `admin`, `user`)
- Action logging to MySQL (`Login Success`, `Login Failed`, `Logout`, etc.)
- Admin tool to review access logs by user
- Clean modular Python code structure

## 🗂️ Project Structure

## How to Run

1. Clone the repository:

   `git clone https://github.com/mak540-source/secure-access-control-system.git`

## Security Notes

- Passwords are hashed using bcrypt.
- Access attempts are logged for review.
- Database credentials should not be publicly shared.
   
