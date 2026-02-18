# 🎵 Soundboard — Musician Directory App

A Python Flask web application showcasing iconic musicians with bios, genres, and profiles. Built for CI/CD deployment on AWS.

---

## 📁 Project Structure

```
simple-musician-app/
├── app.py               # Flask app (main application)
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container definition
├── buildspec.yml        # AWS CodeBuild — builds & pushes Docker image
├── appspec.yml          # AWS CodeDeploy — deploys to EC2
├── start_container.sh   # Script to start the Docker container
├── stop_container.sh    # Script to stop the Docker container
└── README.md
```

---

## 🚀 Run Locally

### Option 1 — Python directly
```bash
pip install -r requirements.txt
python app.py
```
Visit: http://localhost:5000

### Option 2 — Docker
```bash
docker build -t musician-app .
docker run -p 5000:5000 musician-app
```
Visit: http://localhost:5000

---

## ☁️ CI/CD Pipeline (AWS)

### How it works
1. You push code to GitHub
2. **AWS CodePipeline** detects the push
3. **AWS CodeBuild** runs `buildspec.yml` → builds Docker image → pushes to ECR
4. **AWS CodeDeploy** runs `appspec.yml` → stops old container → starts new container

### Required AWS Environment Variables (set in CodeBuild)
| Variable | Description |
|---|---|
| `AWS_ACCOUNT_ID` | Your AWS account ID |
| `AWS_DEFAULT_REGION` | e.g. `us-east-1` |
| `IMAGE_REPO_NAME` | Your ECR repository name |

### Setup Steps
1. Create an ECR repository in AWS
2. Create a CodeBuild project pointing to your GitHub repo
3. Create a CodeDeploy application + deployment group targeting your EC2 instance
4. Create a CodePipeline connecting Source (GitHub) → Build (CodeBuild) → Deploy (CodeDeploy)
5. Push to GitHub — it auto-deploys!

---

## 🌐 API Endpoints

| Endpoint | Description |
|---|---|
| `GET /` | Main musician directory UI |
| `GET /health` | Health check (returns JSON) |
| `GET /api/musicians` | All musicians as JSON |

---

## ✏️ Customizing Musicians

Edit the `MUSICIANS` list in `app.py`:

```python
{
    "name": "Your Musician",
    "emoji": "🎸",
    "genre": "Rock",
    "era": "2000s",
    "born": "1980, City",
    "instrument": "Guitar",
    "tagline": "Short catchy tagline",
    "bio": "Full biography text here...",
    "known_for": ["Song 1", "Album 1", "Achievement"],
},
```

Push your changes → CI/CD deploys automatically!

---

## 🛠️ Tech Stack

- **Backend:** Python 3.11, Flask
- **Frontend:** HTML, CSS, JavaScript (inline, no build step)
- **Container:** Docker
- **CI/CD:** AWS CodePipeline + CodeBuild + CodeDeploy
- **Registry:** Amazon ECR
