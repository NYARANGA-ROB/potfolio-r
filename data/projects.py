"""Featured solutions and project data."""

PROJECTS = [
    {
        "id": "school-management",
        "name": "School Management System",
        "category": "Enterprise",
        "tags": ["Django", "React", "PostgreSQL", "SMS"],
        "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "icon": "🏫",
        "features": [
            "Student Records",
            "Fee Management",
            "Examinations",
            "Attendance",
            "Parent Portal",
            "Bus Tracking",
            "SMS Notifications",
        ],
        "impact": "Reduced administrative workload and improved operational efficiency.",
        "description": "Comprehensive school administration platform for modern educational institutions.",
    },
    {
        "id": "precision-agriculture",
        "name": "Precision Agriculture Platform",
        "category": "AI & ML",
        "tags": ["TensorFlow", "Python", "FastAPI", "IoT"],
        "gradient": "linear-gradient(135deg, #11998e 0%, #38ef7d 100%)",
        "icon": "🌾",
        "features": [
            "Crop Recommendation",
            "Pest Detection",
            "Yield Prediction",
            "Weather Analysis",
            "Soil Intelligence",
        ],
        "impact": "Improved farming decisions through AI-powered insights.",
        "description": "AI-driven agricultural intelligence for smarter farming operations.",
    },
    {
        "id": "career-portal",
        "name": "Career Portal System",
        "category": "Web Application",
        "tags": ["Spring Boot", "React", "MySQL", "AWS"],
        "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
        "icon": "💼",
        "features": [
            "Job Listings",
            "Employer Dashboard",
            "Candidate Tracking",
            "Resume Management",
        ],
        "impact": "Simplified recruitment processes.",
        "description": "End-to-end recruitment platform connecting employers and talent.",
    },
    {
        "id": "bi-dashboard",
        "name": "Business Intelligence Dashboard",
        "category": "Data Science",
        "tags": ["Power BI", "Python", "Pandas", "AWS"],
        "gradient": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
        "icon": "📈",
        "features": [
            "Real-Time Analytics",
            "Forecasting",
            "KPI Monitoring",
            "Executive Reporting",
        ],
        "impact": "Enabled data-driven decision making.",
        "description": "Executive-grade analytics platform for strategic business insights.",
    },
]

CASE_STUDIES = [
    {
        "id": "school-case",
        "title": "School Administration Transformation",
        "project_id": "school-management",
        "problem": (
            "A growing school network struggled with manual record-keeping, delayed fee "
            "collections, and fragmented communication between staff and parents."
        ),
        "solution": (
            "Built a unified school management platform with automated fee tracking, "
            "digital examinations, real-time attendance, and SMS parent notifications."
        ),
        "technologies": ["Django", "React", "PostgreSQL", "Twilio SMS", "Docker", "AWS"],
        "results": [
            "60% reduction in administrative processing time",
            "95% parent engagement via SMS portal",
            "Real-time bus tracking for 500+ students",
        ],
        "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    },
    {
        "id": "agriculture-case",
        "title": "AI-Powered Farming Intelligence",
        "project_id": "precision-agriculture",
        "problem": (
            "Smallholder farmers lacked access to data-driven insights for crop selection, "
            "pest management, and yield optimization."
        ),
        "solution": (
            "Developed an ML platform with computer vision pest detection, soil analysis "
            "models, and weather-integrated crop recommendations."
        ),
        "technologies": ["TensorFlow", "FastAPI", "Python", "OpenCV", "AWS S3", "React"],
        "results": [
            "35% improvement in crop yield predictions",
            "Early pest detection with 92% accuracy",
            "500+ farmers onboarded in pilot program",
        ],
        "gradient": "linear-gradient(135deg, #11998e 0%, #38ef7d 100%)",
    },
    {
        "id": "recruitment-case",
        "title": "Streamlined Talent Acquisition",
        "project_id": "career-portal",
        "problem": (
            "Employers faced lengthy hiring cycles with scattered candidate data and "
            "inefficient resume screening processes."
        ),
        "solution": (
            "Created a career portal with intelligent candidate matching, employer "
            "dashboards, and automated application tracking workflows."
        ),
        "technologies": ["Spring Boot", "React", "MySQL", "Elasticsearch", "AWS"],
        "results": [
            "40% faster time-to-hire",
            "10,000+ job listings managed",
            "Integrated resume parsing and scoring",
        ],
        "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
    },
    {
        "id": "bi-case",
        "title": "Executive Analytics Platform",
        "project_id": "bi-dashboard",
        "problem": (
            "Leadership teams relied on outdated spreadsheets with no real-time visibility "
            "into KPIs and business performance metrics."
        ),
        "solution": (
            "Delivered a real-time BI dashboard with forecasting models, automated "
            "reporting, and executive-level data visualizations."
        ),
        "technologies": ["Power BI", "Python", "Pandas", "AWS", "PostgreSQL", "Plotly"],
        "results": [
            "Real-time KPI monitoring across 12 departments",
            "Automated weekly executive reports",
            "Forecasting accuracy improved by 28%",
        ],
        "gradient": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
    },
]
