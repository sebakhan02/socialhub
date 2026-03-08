# Social Media Web App (Django)

A lightweight **social media web application built with Django** that allows users to create accounts, share posts, follow other users, and interact through likes and profiles.

This project demonstrates core **backend web development concepts** including authentication, relational data modeling, user feeds, and social interactions.

---

# Features

### User Authentication

* User registration
* Login and logout
* Secure authentication using Django's built-in auth system

### User Profiles

* Custom user profiles
* Profile picture upload
* Bio and location editing
* Profile settings management

### Posts

* Create posts with captions and images
* View posts in a feed
* Timestamped content
* Like and unlike posts

### Social Features

* Follow and unfollow users
* View follower and following counts
* Personalized feed based on followed users

### Search

* Search for other users by username

---

# System Architecture

The application is built around four main models:

**Profile**

* Stores additional user information
* Linked to Django's default `User` model

**Post**

* Stores user-generated content
* Includes captions, images, and like counts

**LikePost**

* Tracks which users liked which posts

**FollowerCount**

* Tracks follower and following relationships between users

---

# Tech Stack

**Backend**

* Python
* Django

**Database**

* SQLite (default Django development database)

**Frontend**

* Django Templates
* HTML / CSS

**Authentication**

* Django Authentication System

---

# Key Functionalities

* Feed generation from followed users
* Post creation with media uploads
* Social relationship management (follow/unfollow)
* Dynamic like system
* Profile management

---

# Project Structure

```
project/
│
├── core/
│   ├── models.py
│   ├── views.py
│
├── templates/
│   ├── index.html
│   ├── profile.html
│   ├── signup.html
│   ├── signin.html
│   └── setting.html
│
├── media/
│   ├── profile_images/
│   └── post_images/
│
└── manage.py
```

---

# Installation

### 1 Clone the repository

```bash
git clone https://github.com/sebakhan02/socialhub.git
```

### 2 Navigate to the project

```bash
cd socialhub
```

### 3 Create a virtual environment

```bash
python -m venv venv
```

### 4 Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 5 Install dependencies

```bash
pip install django
```

### 6 Run migrations

```bash
python manage.py migrate
```

### 7 Start the development server

```bash
python manage.py runserver
```

Open the browser:

```
http://127.0.0.1:8000
```

---

# Future Improvements

* REST API with Django REST Framework
* Real-time notifications
* Comment system
* Image optimization
* Feed ranking algorithm
* Frontend SPA using Angular or React

---

# Learning Objectives

This project demonstrates:

* Django MVC architecture
* Database relationships
* User authentication workflows
* Media file handling
* Social platform logic

---

# Author

**Sebakhan**

Full-stack developer focused on building scalable platforms using **Angular, Django, and PostgreSQL**.

GitHub: https://github.com/sebakhan02
