# weather-bdd-tests

![CI](https://github.com/uriel-P-V/weather-bdd-tests/actions/workflows/tests.yml/badge.svg)

A BDD-based test suite for the Open-Meteo weather API —
demonstrates behavior-driven development with Behave and Gherkin,
mock-based testing, and tag-driven execution for smoke and regression suites.

---

## Project Structure

```
weather-bdd-tests/
├── .github/
│   └── workflows/
│       └── tests.yml             ← GitHub Actions CI
├── features/
│   ├── steps/
│   │   └── weather_steps.py      ← Step definitions in Python
│   ├── environment.py            ← Hooks and mock setup
│   └── weather.feature           ← Gherkin scenarios
├── reports/
│   └── report.html               ← Generated test report (gitignored)
├── behave.ini                    ← Behave configuration
└── requirements.txt
```

---

## Features

- **BDD with Gherkin** — human-readable scenarios with Given/When/Then
- **Scenario Outline** — data-driven tests across multiple cities
- **Tag-driven execution** — `@smoke` for critical path, `@regression` for full suite
- **Mock-based testing** — regression suite runs without hitting the real API
- **HTML report** — visual test results with pass/fail per step
- **GitHub Actions CI** — smoke runs first, regression only if smoke passes

---

## BDD Example

```gherkin
Feature: Current Weather API

  Background:
    Given the weather API is available

  @smoke
  Scenario: Get current weather for valid coordinates
    When I request the current weather for latitude 20.6767 and longitude -103.3475
    Then the response status code should be 200
    And the response should contain weather data

  @regression
  Scenario Outline: Get current weather for different cities
    When I request the current weather for latitude <lat> and longitude <lon>
    Then the response status code should be 200

    Examples:
      | lat     | lon       |
      | 20.6767 | -103.3475 |
      | 51.5074 | -0.1278   |
      | 35.6762 | 139.6503  |
```

---

## Setup

```bash
git clone https://github.com/uriel-P-V/weather-bdd-tests.git
cd weather-bdd-tests
pip install -r requirements.txt
behave
```

---

## Running Tests

```bash
# All scenarios
behave

# Smoke only — hits the real API, fast critical check
behave --tags=smoke

# Regression only — fully mocked, no internet required
behave --tags=regression

# Generate HTML report
behave --no-capture -f html -o reports/report.html
```

---

## CI/CD Pipeline

Two dependent jobs run on every push and pull request to `main`:

```
push / PR → smoke (real API) → regression (mocked) → upload HTML report
```

If `smoke` fails, `regression` is skipped automatically.
The HTML report is available as a downloadable artifact in the Actions tab.

---

## Tech Stack

- **Python 3.11+**
- **Behave** — BDD framework with Gherkin support
- **Requests** — HTTP client for API calls
- **unittest.mock** — mock-based testing with side_effect
- **behave-html-formatter** — visual HTML test reports
- **GitHub Actions** — CI/CD pipeline with artifact upload

---

## Author

**Uriel Alejandro Pérez Valdovinos**  
[github.com/uriel-P-V](https://github.com/uriel-P-V) · [linkedin.com/in/uriel-pv](https://linkedin.com/in/uriel-pv)