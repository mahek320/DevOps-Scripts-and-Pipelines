h1 align="center">🚀 Python Code Quality CI Pipeline</h1>

<p align="center">
  <a href="https://sonarcloud.io/dashboard?id=mahek320_python-ci-code-quality">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=mahek320_python-ci-code-quality&metric=alert_status" alt="Quality Gate Status">
  </a>
  <a href="https://sonarcloud.io/dashboard?id=mahek320_python-ci-code-quality">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=mahek320_python-ci-code-quality&metric=coverage" alt="Coverage">
  </a>
</p>

---

## 🛠️ Features

- ✅ Code Linting with `pylint`  
- 🎨 Code Formatting Check using `black`  
- 🔐 Security Scanning via `bandit`  
- 🧪 Unit Testing & Coverage with `pytest`  
- 📊 Code Quality Analysis using `SonarQube`  
- 📧 Automated Email Notifications with reports  
- ☁️ Artifact Uploads for easy access to reports  

---

## 📂 Pipeline Workflow

1. **Checkout Code**
2. **Set Up Python Environment**
3. **Install Dependencies**
4. **Run Linting & Formatting Checks**
5. **Security Scan with Bandit**
6. **Run Tests with Coverage**
7. **Upload Reports as Artifacts**
8. **SonarQube Analysis**
9. **Send Email Notification with Reports**

---

## 📊 Reports & Dashboard

- 🔗 [SonarQube Dashboard](https://sonarcloud.io/dashboard?id=mahek320_python-ci-code-quality)
- 📄 Pylint Report
- 📄 Bandit Security Report
- 📈 HTML Coverage Report

---

## 📧 Email Notification

After every push, an email is sent with:

- 📎 Attached reports (Pylint, Bandit, Coverage)
- 🔗 Link to SonarQube Dashboard

---


