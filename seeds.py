from flask import Flask
from models import db, Restaurant, Customer, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create instances and add them to the database
with app.app_context():
    db.create_all()

    # Sample data for testing
    restaurant1 = Restaurant(name='Restaurant A', price=3)
    restaurant2 = Restaurant(name='Restaurant B', price=4)

    customer1 = Customer(first_name='John', last_name='Doe')
    customer2 = Customer(first_name='Jane', last_name='Smith')

    review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
    review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer2)

    # Add instances to the session and commit
    db.session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
    db.session.commit()