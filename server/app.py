from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Author, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Validations lab'

# @Author.validates("name")
# def validates_name(self, key, name):
#     if not name:
#         raise ValueError("Author name cannot be empty.")
#     return name

# @Author.validates("phone_number")
# def validate_author_phone_number(self, key, phone_number):
#     if phone_number and len(phone_number) != 10:
#         raise ValueError("Phone number must be 10 digits only.")
#     return phone_number

# @Post.validate("title")
# def validates_title(self, key, title):
#     titles_list = ["Won't Believe", "Secret", "Top", "Guess"]
#     if not any(keyword in title for keyword in titles_list):
#         raise ValueError(f"Title must contain any of these keywords: {titles_list}")
#     return title

# @Post.validates("content_length")
# def validates_content_length(self, key, content_length):
#     if len(content_length) < 250:
#         raise ValueError("Content must be more than 250 characters.")
#     return content_length


# @Post.validates("summary")
# def validates_summary(self, key, summary):
#     if summary and len(summary) > 250:
#         raise ValueError("Summary must not be greater than 250 words.")
#     return summary

# @Post.validates("category")
# def validates_category(self, key, category):
#     if category not in ["Fiction", "Non-Fiction"]:
#         raise ValueError("Category must be either 'Fiction' or 'Non-Fiction'.")


if __name__ == '__main__':
    app.run(port=5555, debug=True)

