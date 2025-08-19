# Tech_Academy_Capstone
Final project for Tech Academy
# MovieBase — Django Capstone Project

MovieBase is a Django-powered web app for tracking your favorite movies.  
It demonstrates CRUD operations, database integration, search & filter, and template rendering.  

---

## Features & User Stories

### Story 1: Add a Movie
- Created a **Movie model** with fields (title, release date, runtime, genre, rating, notes, watched, timestamps).
- Built a **form (MovieForm)** for adding movies.
- Added a **create view** (`create_movie`) to handle form submission.
- Created `movie_form.html` template for the input form.
- Home page shows a **recent movie list with images**.

---

### Story 2: Home Page
- Added a **hero section** and quick actions (Add Movie, Browse All).
- Displayed a **short list of recent movies**.
- Styled with **cards + grid layout**.
- Linked to **details** and **browse page**.

---

### Story 3: Browse All Movies
- Implemented **`list_movies` view** with:
  - Search bar (filter by title or notes).
  - Sorting (title, rating, release date, newest/oldest).
  - Pagination with **"Load more" button**.
- Added **template filters** (e.g., `date`, `timesince`, `truncatechars`).
- Template: `movie_list.html`.

---

### Story 4: Movie Details Page
- Added **`movie_detail` view** to display a single movie.
- Linked each card to its detail page.
- Displayed **all fields** with labels.
- Template: `movie_detail.html`.
- Added navigation: **Back to Browse / Home**.

---

### Story 5: Edit & Delete
- Implemented **`edit_movie` view** with a pre-filled form.
- Implemented **`delete_movie` view** with confirmation.
- Templates:
  - `movie_form.html` (shared with edit & create).
  - `movie_confirm_delete.html` (with JS modal confirm option).
- Flash messages confirm updates and deletes.

---

## Tech Stack
- **Backend**: Django 2.2+
- **Frontend**: HTML, CSS (custom styles), Django templating
- **Database**: SQLite (default)
- **Language**: Python 3.11+

---

## Project Structure
MainProject/
│
├── movies/ # App folder
│ ├── migrations/
│ ├── templates/
│ │ └── movies/
│ │ ├── home.html
│ │ ├── movie_list.html
│ │ ├── movie_detail.html
│ │ ├── movie_form.html
│ │ └── movie_confirm_delete.html
│ ├── static/movies/ # Styles, images
│ ├── models.py
│ ├── views.py
│ └── urls.py
│
├── MainProject/ # Django project settings
├── manage.py
└── README.md # Project summary (this file)


---

## Running the Project
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd CapStone_Project

