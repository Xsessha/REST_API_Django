#!/usr/bin/env python
"""
Script to populate sample data for the media app.
Run with: python manage.py shell < populate_data.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from media.models import Media, Comment

# Clear existing data
Media.objects.all().delete()
Comment.objects.all().delete()

# Create sample media items with comments
sample_data = [
    {
        'title': 'Django Tutorial',
        'description': 'Learn the basics of Django web framework. This comprehensive tutorial covers models, views, templates, and more.',
        'url': 'https://www.djangoproject.com/weblog/',
        'comment': {
            'author': 'John Developer',
            'text': 'This is a great resource for learning Django! Highly recommended for beginners.'
        }
    },
    {
        'title': 'Python Best Practices',
        'description': 'A guide to writing clean, maintainable Python code. Covers PEP 8, testing, and code organization.',
        'url': 'https://www.python.org',
        'comment': {
            'author': 'Sarah Python',
            'text': 'Very informative article. The best practices here have improved our code quality significantly.'
        }
    },
    {
        'title': 'Web Development Guide',
        'description': 'Complete guide to modern web development including frontend and backend technologies.',
        'url': 'https://developer.mozilla.org',
        'comment': {
            'author': 'Mike Web',
            'text': 'Excellent comprehensive guide! Very helpful for anyone starting web development.'
        }
    },
    {
        'title': 'Database Design Fundamentals',
        'description': 'Learn about relational databases, normalization, and SQL optimization techniques.',
        'url': 'https://en.wikipedia.org/wiki/Database',
        'comment': {
            'author': 'Emma Data',
            'text': 'This article perfectly explains database design principles. Very well written!'
        }
    },
    {
        'title': 'API Development with REST',
        'description': 'Build robust and scalable REST APIs. Learn about best practices, error handling, and versioning.',
        'url': 'https://restfulapi.net',
        'comment': {
            'author': 'Alex Backend',
            'text': 'Great insights on building professional REST APIs. This helped us redesign our API.'
        }
    }
]

# Create media items with comments
for item in sample_data:
    media = Media.objects.create(
        title=item['title'],
        description=item['description'],
        url=item['url']
    )
    Comment.objects.create(
        media=media,
        author=item['comment']['author'],
        text=item['comment']['text']
    )
    print(f"Created: {media.title} with comment by {item['comment']['author']}")

print("\nSuccessfully created sample data!")
print(f"Total Media items: {Media.objects.count()}")
print(f"Total Comments: {Comment.objects.count()}")
