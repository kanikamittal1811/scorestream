# imaginAI-backend


why python3.8-slim image?
The official Python image is based on a lightweight Linux distribution (Debian), and it already includes Python and pip. This means you can use it to set up a Python environment for your Flask application without the need for additional manual installations.
## Project setup

``````

```bash
docker build -t imaginai-backend:latest -f Dockerfile.dev .
docker run -p 4000:5000 -v $(pwd):/app imaginai-backend:latest
```

```bash
python -m unittest tests/test_app.py
```

Todo:
-> create a home api that fetches random images from mongo with pagination and session id


Resources:
https://www.freecodecamp.org/news/how-to-setup-a-ci-cd-pipeline-with-github-actions-and-aws/