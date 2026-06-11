"""Profile and personal information."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent
PROFILE_PHOTO = DATA_DIR / "profile.png"

PROFILE = {
    "name": "Robert Nyaranga",
    "title": "Software Engineer | AI Engineer | Data Scientist",
    "bio": (
        "I specialize in building intelligent web applications, AI-powered systems, "
        "machine learning solutions, and data-driven platforms that help organizations "
        "automate operations, improve efficiency, and make better decisions."
    ),
    "email": "nyarangaro@gmail.com",
    "linkedin": "https://www.linkedin.com/in/robert-nyaranga/",
    "headline": "Building Intelligent Systems That Solve Real Business Problems",
    "subtitle": (
        "I develop scalable software platforms, AI solutions, and data-driven applications "
        "that help organizations grow faster and operate smarter."
    ),
}

SKILLS = [
    "Python", "Java", "JavaScript", "SQL", "React", "Django", "FastAPI",
    "Spring Boot", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
    "Data Science", "Business Intelligence", "AWS", "Docker",
]

STATS = [
    {"label": "Years Experience", "value": 5, "suffix": "+", "icon": "⏱"},
    {"label": "Projects Completed", "value": 20, "suffix": "+", "icon": "🚀"},
    {"label": "AI & ML Specialist", "value": None, "text": "AI & ML Specialist", "icon": "🧠"},
    {"label": "Full Stack Engineer", "value": None, "text": "Full Stack Engineer", "icon": "⚡"},
    {"label": "Data Science Expert", "value": None, "text": "Data Science Expert", "icon": "📊"},
    {"label": "Business Solutions", "value": None, "text": "Business Solutions Developer", "icon": "💼"},
]

TIMELINE = [
    {
        "year": "2019",
        "title": "Software Engineering Foundation",
        "description": "Began building web applications and enterprise systems with Java, Python, and modern frameworks.",
    },
    {
        "year": "2021",
        "title": "Data Science & Analytics",
        "description": "Expanded into data science, business intelligence, and predictive analytics for organizations.",
    },
    {
        "year": "2023",
        "title": "AI & Machine Learning",
        "description": "Specialized in deep learning, computer vision, and AI-powered automation platforms.",
    },
    {
        "year": "2025",
        "title": "Full-Stack AI Solutions",
        "description": "Delivering end-to-end intelligent systems for schools, agriculture, enterprises, and NGOs.",
    },
]
