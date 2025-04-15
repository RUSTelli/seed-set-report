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
### Add plots directory
```bash
mkdir plots
```
### Install packages 
```bash
pip install -r requirements.txt
```
### Setup the packages
```bash
python setup.py install
```
---
## 🚀 To run, move inside project's directory, substitute 'x' with 'influenced' or 'performances':
```bash
python plotting/main.py --plot_type x 
```

---
## Project structure
```bash
Project/
├── methods/              # Core algorithm implementations
├── plottings/            # Plotting methods
    └── main.py           # Can plot algorithm 'performances' or graph 'influenced' nodes
├── shared/               # constants
├── plots/                # Generated outputs
├── requirements.txt      # Python dependencies
├── setup.py              # Package configuration
└── ...                   # Additional project files
```