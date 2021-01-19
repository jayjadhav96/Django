# Creating of project
django-admin startproject project

# Creating a projectapp
python manage.py startapp app

# Running the server
python manage.py runserver

# made changes
python manage.py makemigrations
python manage.py migrate

# Creating a superuser
python manage.py createsuperuser

# Opening django python shell
python manage.py shell

# Inserting the values in database

    from blog.models import Post
    from django.contrib.auth.models import User

    user = User.objects.filter(username='JaySJ')
    # creating new post
    post_2 = Post(title='Blog 1', content='First Blog Post', author_id=user.id)
    # saving the post
    post_2.save()

# Seeing the data inserted in database
Post.objects.all()

# Accessing the data from database
post = Post.objects.first()
post.content
post.date_posted
post.author
post.author.email

# Seeing the posts that user have created
user.post_set
user.post_set.all()

# Creating further posts using same user
user.post_set.create(title='Blog 3', content='Third Post Content!')


# Inserting a json object to the database.
import json
from blog.models import Post
with open('posts.json') as f:
     posts_json = json.load(f)
for post in posts_json:
    post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
    post.save()  
