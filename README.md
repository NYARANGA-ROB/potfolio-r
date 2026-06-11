# Robert Nyaranga — Premium Portfolio

A world-class personal portfolio built with Streamlit, designed to showcase software engineering, AI/ML, and data science expertise with a premium SaaS aesthetic.

## Features

- Modern UI inspired by Stripe, Linear, Notion, and Vercel
- Light and dark mode support
- Glassmorphism cards, gradient highlights, and smooth animations
- Animated statistics counters
- Interactive project cards with search and filtering
- Expandable case studies
- Technology stack matrix with progress bars and radar chart
- Contact form with validation
- Responsive, mobile-optimized layout
- SEO meta tags

## Project Structure

```
portfolio/
├── app.py                  # Main application entry point
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── assets/
│   ├── images/             # Profile and project images
│   ├── animations/         # Lottie animation files
│   └── styles.css          # Custom CSS design system
├── components/             # Reusable UI components
│   ├── hero.py
│   ├── stats.py
│   ├── projects.py
│   ├── case_studies.py
│   ├── services.py
│   ├── tech_stack.py
│   ├── testimonials.py
│   ├── blog.py
│   ├── about.py
│   ├── contact.py
│   ├── navigation.py
│   └── footer.py
├── data/                   # Content and configuration data
│   ├── profile.py
│   ├── projects.py
│   ├── services.py
│   ├── tech_stack.py
│   ├── testimonials.py
│   └── blog.py
└── pages/                  # Additional Streamlit pages (optional)
```

## Local Development

### Prerequisites

- Python 3.9+
- pip

### Setup

```bash
# Clone or navigate to the project
cd portfolio

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The site will open at `http://localhost:8501`.

## Deployment to Streamlit Cloud

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Add premium Streamlit portfolio"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/robert-portfolio.git
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select your repository (`robert-portfolio`)
5. Set **Main file path** to `app.py`
6. Choose **Python 3.9+** as the runtime
7. Click **"Deploy"**

### Step 3: Configure (Optional)

- Add a custom subdomain in Streamlit Cloud settings (e.g., `robert-nyaranga.streamlit.app`)
- Upload a profile photo to `assets/images/` and update `components/hero.py`
- Add a `packages.txt` if you need system-level dependencies

### Environment Variables

No secrets are required for basic deployment. If you add email integration (e.g., SendGrid), set API keys in Streamlit Cloud's **Secrets** panel:

```toml
# .streamlit/secrets.toml (local only — use Cloud Secrets UI for production)
SENDGRID_API_KEY = "your-key-here"
```

## Customization

| What to change | File |
|---|---|
| Personal info | `data/profile.py` |
| Projects & case studies | `data/projects.py` |
| Services | `data/services.py` |
| Tech stack levels | `data/tech_stack.py` |
| Testimonials | `data/testimonials.py` |
| Blog posts | `data/blog.py` |
| Colors & styling | `assets/styles.css` |
| Theme defaults | `.streamlit/config.toml` |

## Adding a Profile Photo

1. Place your image in `assets/images/profile.jpg`
2. Update `components/hero.py` to use `st.image()` instead of the emoji placeholder

## License

Personal portfolio — all rights reserved © Robert Nyaranga
