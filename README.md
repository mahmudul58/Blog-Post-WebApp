# MyBlog - Django Blog Application

## About
A feature-rich, full-stack blog application built with Django. It provides a platform for users to create, manage, and engage with blog posts. The application features a rich text editor for creating engaging content, post categorization by topics, and a social aspect allowing users to like and comment on posts.

## Functionalities

* **User Authentication**: Secure user registration, login, and logout capabilities.
* **Blog Post Management (CRUD)**:
  * Create new posts with rich text formatting using the integrated CKEditor.
  * Attach cover images to posts via URL or direct file upload.
  * Edit and update existing posts.
  * Delete your own posts.
* **Content Organization & Discovery**:
  * Categorize posts into different Topics for easier discovery
  * View a personalized "My Posts" dashboard to manage your authored content.
  * Highlight specific content with "Featured Posts" functionality.
* **User Engagement**:
  * **Likes**: Like and unlike posts, with a visible like count.
  * **Comments**: Leave comments on posts to participate in discussions.
  * **View Tracking**: Track the number of views for each blog post.
* **Rich Text Editing**: Integrated `django-ckeditor` allows authors to format text, add media, and structure their blog posts professionally.

## Tech Stack
* **Backend**: Django (Python)
* **Database**: PostgreSQL (via `psycopg2-binary`)
* **Static File Management**: WhiteNoise
* **Rich Text Editor**: django-ckeditor
