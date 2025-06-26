# Quant Project Template

Your base for developing trading strategies.

This repository provides a clean and minimal project structure for coding and testing trading ideas. It includes:

- A Poetry-based environment setup  
- Directory structure suitable for real projects (`src/`, `tools/`, `tests/`, etc.)  
- A utility to summarize your project structure (`project_summary.md`)  
- Ready-to-use Makefile for common commands  

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/githubvctr/quant-project-template.git
cd quant-project-template
```

### Install Dependencies

This project uses Poetry for dependency management. If not already installed:

```bash
pip install poetry
```

Then install dependencies (without installing the project itself):

```bash
poetry install --no-root
```

### Activate the Virtual Environment

```bash
poetry shell
```

---

## Usage

### Project Summarization Utility

To generate a Markdown summary (`project_summary.md`) of all Python files in the `src/`, `tools/`, `tests/`, and `streamlit_app/` directories:

```bash
make summary
```

This summary lists function and class definitions and can be useful for documentation or usage with local LLMs (e.g., Continue, Ollama).

---

## Directory Structure

```
quant-project-template/
├── src/                  # Source code of your trading logic
├── tools/                # Utility scripts like summarizers or batch tools
├── tests/                # Unit tests
├── streamlit_app/        # If applicable, dashboards or demos
├── pyproject.toml        # Poetry config
├── Makefile              # Utility commands
└── README.md             # Project instructions
```

---

## Using This Template for a New Quant Project

### 1. Clone without Git history

```bash
git clone --depth=1 https://github.com/githubvctr/quant-project-template.git your-new-project
cd your-new-project
rm -rf .git
git init
```

### 2. Rename the project in `pyproject.toml`

```toml
[tool.poetry]
name = "your-project-name"
```

### 3. (Optional) Create your own GitHub repo and push

```bash
git remote add origin https://github.com/yourname/your-new-project.git
git add .
git commit -m "Initial commit from quant-project-template"
git push -u origin main
```

### 4. Off you go, enjoy!