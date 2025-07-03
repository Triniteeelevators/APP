# Entry Form Application

A simple web application built with Flask that allows users to enter and store information.

## Features

- User-friendly form for entering name, email, phone, and address
- Data storage using Excel files
- Real-time display of entries
- Modern, responsive UI using Bootstrap

## Deployment

This application is deployed to GitHub Pages. The frontend is served statically, while the backend API runs on a separate server.

### GitHub Pages Setup

1. Create a new repository on GitHub
2. Push your code to the repository
3. GitHub Actions will automatically deploy the static files to GitHub Pages
4. Access the application through the GitHub Pages URL

## Local Development

To run the application locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python app.py
```

Then open your browser and navigate to `http://localhost:5000`
