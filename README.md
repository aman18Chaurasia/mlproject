
# 🧠 MLProject - End-to-End Machine Learning Pipeline with CI/CD and DVC

![CI](https://img.shields.io/github/actions/workflow/status/aman18Chaurasia/mlproject/main.yml?label=CI&style=flat-square)
![License](https://img.shields.io/github/license/aman18Chaurasia/mlproject?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)

An end-to-end machine learning project that covers the full ML lifecycle — from data ingestion to deployment — with CI/CD, DVC for data versioning, modular components, and scalable architecture.

---

## 🚀 Features

- 📦 Modular & Scalable Codebase
- 🔁 Data & Model Versioning with DVC
- ✅ Unit Testing & Utility Layer
- ⚙️ CI/CD Pipeline via GitHub Actions
- 📁 Clean Directory Structure
- ☁️ Cloud Deployment Ready (AWS/Render)

---

## 🗂 Project Structure

```
mlproject/
├── .github/workflows/       # GitHub Actions workflows
├── artifacts/               # Intermediate data, models
├── data/                    # Raw & processed data
├── dvc.yaml                 # DVC pipeline file
├── main.py                  # Training entrypoint
├── src/
│   ├── components/          # Modular ML pipeline pieces
│   ├── config/              # Configuration management
│   ├── pipeline/            # Training & prediction orchestration
│   ├── utils.py             # Reusable utilities
├── tests/                   # Unit tests
├── requirements.txt         # Python dependencies
├── setup.py                 # Install as package
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/aman18Chaurasia/mlproject.git
cd mlproject
python -m venv venv
venv\Scripts\activate  # For Windows
# Or source venv/bin/activate for Linux/macOS
pip install -r requirements.txt
```

---

## 💡 Usage

### To train the model:
```bash
python main.py
```

### To make predictions:
```bash
# If using a Flask web UI, access the endpoint:
http://localhost:8080/predictdata
```

---

## 💾 DVC Setup

```bash
dvc init
dvc remote add -d origin <your-dvc-remote-url>
dvc add data/raw.csv
git add data/raw.csv.dvc .gitignore
git commit -m "Add raw data to DVC"
dvc push
```

---

## 🔁 CI/CD Pipeline

- Automated via GitHub Actions (`.github/workflows/main.yml`)
- Runs on every push to `main`
  - ✅ Lint + test
  - 🚀 (Optional) Deploy or push Docker images

---

## 🧪 Running Tests

```bash
pytest tests/
```

---

## 📤 Deployment

The project is structured to support deployment using:
- Flask / FastAPI backend
- Docker
- AWS EC2 / Render / Heroku (config needed)

Let me know if you want deployment setup guides.

---

## 🤝 Contributing

Pull requests and forks are welcome. Open an issue for discussion first.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Aman Chaurasia**  
🔗 [LinkedIn](https://www.linkedin.com/in/aman-chaurasia-)  
💻 [GitHub](https://github.com/aman18Chaurasia)

---
