

# Django Blog API

This project is a simple blog API built with Django and Django REST framework. It provides endpoints to create, read, update, and delete blog posts.

## Features

- List all blog posts
- Create a new blog post
- Retrieve a specific blog post by ID
- Update a blog post
- Delete a blog post

## Requirements

- Python 3.x
- Django
- Django REST framework

## Installation

1. Clone the repository:

```bash
git clone https://github.com/fahad0samara/django-blog.git
cd django-blog
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

## Usage

- To list all blog posts, send a GET request to `/api/blog/`.
- To create a new blog post, send a POST request to `/api/blog/` with the blog post data.
- To retrieve a specific blog post by ID, send a GET request to `/api/blog/<id>/`.
- To update a blog post by ID, send a PUT request to `/api/blog/<id>/` with the updated data.
- To delete a blog post by ID, send a DELETE request to `/api/blog/<id>/`.

## Project Structure

```plaintext
mysite/
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.


```

## Adding the Remote Repository

To add the remote repository and push your code to GitHub, use the following commands:

```bash
git remote add origin https://github.com/fahad0samara/django-blog.git
git branch -M main
git push -u origin main
```

