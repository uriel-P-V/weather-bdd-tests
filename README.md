# weather-bdd-tests


![CI](https://github.com/uriel-P-V/weather-bdd-tests/actions/workflows/tests.yml/badge.svg)
Breve descripción del proyecto...

## Tech Stack
- **behave** e   (framework) para Python diseñado para realizar pruebas de software mediante el enfoque de Desarrollo Guiado por el Comportamiento
- **GitHub Actions** — CI/CD pipeline
- **Requests** libreria de python para testear 
## Project Structure
```
WEATHER-BDD-TESTS/
├── features/
│   ├── steps/
│   └── weather.feature
├── README.md
└── requirements.txt
```


## Requirements
- Python 3.10+
- pip
## Setup & Run

```bash
git clone https://github.com/uriel-P-V/weather-bdd-tests.git 
cd weather-bdd-tests
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
behave            
```

---

## Author

**Uriel Alejandro Pérez Valdovinos**  
[github.com/uriel-P-V](https://github.com/uriel-P-V) · [linkedin.com/in/uriel-pv](https://linkedin.com/in/uriel-pv)