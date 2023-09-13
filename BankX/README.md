# Salem Bank

Salem Bank is a simple web application built using Django, designed to manage user accounts, deposits, withdrawals, and account balances.

## Features

- User Signup: Users can create an account with a username and password.
- User Login: Registered users can log in to their accounts.
- Account Overview: Users can view their account balance and recent transactions.
- Deposit Money: Users can make deposits into their accounts.
- Withdraw Money: Users can make withdrawals from their accounts.
- Delete Account: Users can delete their accounts.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Django (installed via `pip install django`)
- Virtual Environment (optional but recommended)

### Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/Adjanour/BankX.git
    ```

2. Navigate to the project directory.

   ```bash
   cd BankX
   ```

3. Create a virtual environment and activate it (optional but recommended).

   ```bash
    python -m venv venv
    source venv/bin/activate
    ```

4. Install the project dependencies.

   ```bash
   pip install -r requirements.txt
   ```

5. Create the database.

   ```bash
   python manage.py migrate
   ```

6. Create a superuser.

   ```bash
    python manage.py createsuperuser
    ```

7. Run the project.

   ```bash  
    python manage.py runserver
    ```

8. Open the project in your browser at `http://localhost:8000`.

### Usage

- Visit the signup page to create a new account.
- Log in using your credentials.
- Explore the different features of the application.
- Use the admin panel (<http://localhost:8000/admin/>) to manage user accounts (requires superuser access).

## Contributing

Contributions are welcome! Please follow our contributing guidelines to get started.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Thank you to the Django community for the powerful framework.

> Bernard Kirk Adjanor Katamanso
