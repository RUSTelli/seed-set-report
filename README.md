# 🌐 Reti Sociali - Algorithm Visualization Package 📊

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Code Style: PEP8](https://img.shields.io/badge/code%20style-PEP8-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)

**Visual comparison toolkit for seed-set discovery algorithms**  

---

## 🔧 Quick Installation

### Create Virtual Environment
```bash
python -m venv reti-env
```
### Activate the environment
```bash
source reti-env/bin/activate  # Linux/MacOS
.\reti-env\Scripts\activate   # Windows
```
### add plots directory and install packages 
```bash
### 2. Install packages and setup
mkdir plots/  # Create output directory structure
pip install -r requirements.txt
python setup.py install  # Install as editable package
```

### add plots directory and install packages 
```bash
### 2. Install packages and setup
mkdir plots/  # Create output directory structure


```
---
## 🚀 To run, move inside project's directory, substitute 'x' with 'influenced' or 'performances':
```bash
python plotting/main.py --plot_type x 
```


```bash
Project/
├── methods/              # Core algorithm implementations
├── plottings/             # Plotting methods
├── shared/               # constants
├── plots/                # Generated outputs
├── requirements.txt      # Python dependencies
├── setup.py              # Package configuration
└── ...                   # Additional project files
```