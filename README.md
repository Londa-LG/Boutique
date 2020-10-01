# [Boutique](https://boutique-store-1.herokuapp.com/)

# Description
Boutique is a registered users online store.
 
## How to run the website
1. Download all the master repository files.
2. Activate the virtual environment ( run: botenv\Scripts\activate in command prompt) 
3. cd to the ecommerce folder.
4. Run a "python manage.py runserver" command.
5. View website on your web browser of choice at http://127.0.0.1:8000/

## How to use the website
* As the owner
  1. Run the "python manage.py createsuperuser" command and follow the user creation steps
  2. Go to the admin login page as http://127.0.0.1:8000/admin
  3. Login with your created username and password
  4. Add and delete products as you see fit.
  5. View orders and find the email address of customers.

* As a User
  1. Visit [Boutique](https://boutique-store-1.herokuapp.com/).
  2. Register as a user via the "Register" option on the Login page
  3. Click on a product's picture or title to view more detail or simply add it to your cart 
  4. Place an order by filling in the checkout form

### Dependencies
* Python 

### Features
* Products
* Product categories
* Post search
* Pagination on products page
* Categories
* Related products on product details page
* Order restriction (customers who aren't registered can't make orders)

### Future Features
* A review products section.
* Direct on website payments.

