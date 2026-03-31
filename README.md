![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
A lightweight Python-based authentication system that demonstrates basic user registration, login functionality, and data persistence using a custom "soft encryption" algorithm.
The system utilizes a custom encryption logic (referred to as "soft encryption"). Unlike standard hashing algorithms like SHA-256 or bcrypt, this method typically shifts or maps characters to different values. 

1.  **Input:** The user enters a plain text password.
2.  **Encryption:** The program iterates through each character, applying a mathematical offset or mapping.
3.  **Storage:** The encrypted string is saved to a text file alongside the username.
4.  **Verification:** During login, the entered password is encrypted using the same logic and compared to the stored value.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Thanmay121/Simple-login-system-with-soft-encryption.git](https://github.com/Thanmay121/Simple-login-system-with-soft-encryption.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd Simple-login-system-with-soft-encryption
    ```

### Usage

Run the main script to start the interface:
```bash
python loginsystem.py
