Restaurant and Customer Management System This project is a simple Python application implementing a Restaurant and Customer Management System using Flask, Flask-SQLAlchemy, and Flask-Migrate. The system includes models for Restaurant, Customer, and Review. It provides basic functionalities such as creating tables, performing migrations, and interacting with the database.

Instructions Prerequisites:

Python 3 Flask Flask-SQLAlchemy Flask-Migrate Install dependencies using:

bash Copy code pip3 install Flask Flask-SQLAlchemy Flask-Migrate Installation:

Clone the repository:

bash Copy code git clone https://github.com/your-username/code-ch-sql.git cd code-ch-sql Install dependencies:

bash Copy code pip3 install -r requirements.txt Database Initialization:

Initialize Flask-Migrate:

bash Copy code flask db init Create a migration script:

bash Copy code flask db migrate -m "Create reviews table" Apply the migration:

bash Copy code flask db upgrade Running the Application:

Run the app.py script:

bash Copy code python3 app.py Sample Data:

Populate the database with sample data:

bash Copy code python3 seeds.py Deliverables Object Relationship Methods:

Review.customer(): Returns the Customer instance for a review. Review.restaurant(): Returns the Restaurant instance for a review. Restaurant.reviews(): Returns all reviews for the restaurant. Restaurant.customers(): Returns all customers who reviewed the restaurant. Customer.reviews(): Returns all reviews left by the customer. Customer.restaurants(): Returns all restaurants reviewed by the customer. Aggregate and Relationship Methods:

Customer.full_name(): Returns the full name of the customer. Customer.favorite_restaurant(): Returns the restaurant with the highest star rating from the customer. Customer.add_review(restaurant, rating): Adds a new review for the restaurant. Customer.delete_reviews(restaurant): Deletes all reviews for a restaurant by the customer. Review.full_review(): Returns a formatted string for a review. Restaurant.fanciest(): Returns the restaurant with the highest price. Restaurant.all_reviews(): Returns a list of strings with all reviews for the restaurant. Contributing Contributions are welcome! Feel free to submit issues or pull requests.

License This project is licensed under the MIT License.
