# Sellerie la vie en rose

An e-commerce website for selling artisanal products, specialized in saddlery items.

## Main Features

- Register as a user.
- Secure online payment via Stripe.
- Select products and add them to the cart.
- Manage the cart before proceeding to payment.

## Technologies Used

- HTML, CSS, JavaScript for the front-end.
- Django (Python) for the back-end.
- Stripe API for online payment processing.
- Google (various APIs or tools).
- SQLite for the database.

## Installation

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/psychohight/project.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Use SQLite Browser to access or configure the database.

## Usage

To start the local server, use the following command:
```
python3 manage.py runserver
```

Then, access the application by opening your browser at: `http://127.0.0.1:8000/`.

## Stripe Configuration

To enable online payments, you need to configure Stripe with your API keys. Here are the steps to follow:

1. Create an account on [Stripe](https://stripe.com/).
2. Retrieve your API keys (public and secret) from the Stripe dashboard.
3. Add these keys to a `.env` file at the root of your project, under the variables `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY`. Ensure that the `.env` file is ignored by Git using `.gitignore`.

Example `.env` file:
```
STRIPE_PUBLIC_KEY=your_public_key_here
STRIPE_SECRET_KEY=your_secret_key_here
```

## Django Management Commands

In addition to `migrate` and `createsuperuser`, here are other common Django commands:

- **Makemigrations**: To create new migrations based on changes in the models.
  ```
  python3 manage.py makemigrations
  ```

## Contributors

I am the sole developer of this project.

