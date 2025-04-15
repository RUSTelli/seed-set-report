# 🌐 Reti Sociali - Algorithm Visualization Package 📊

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Code Style: PEP8](https://img.shields.io/badge/code%20style-PEP8-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)

**Visual comparison toolkit for seed-set discovery algorithms**  

---

## 🚀 Quick Installation

### 1. Create Virtual Environment
```bash
python -m venv reti-env
source reti-env/bin/activate  # Linux/MacOS
.\reti-env\Scripts\activate   # Windows
```
```bash
### 2. Install packages and setup
mkdir plots/  # Create output directory structure
pip install -r requirements.txt
python setup.py install  # Install as editable package
```
```bash
## 🚀 To run, move inside project's directory:
python plotting/main.py --plot_type x, where 'x' may be 'influenced' or 'performances'
```



Project/
├── methods/              # Core algorithm implementations
├── plotings/             # Plotting methods
├── shared/               # constants
├── plots/                # Generated outputs
├── requirements.txt      # Python dependencies
├── setup.py              # Package configuration
└── ...                   # Additional project files