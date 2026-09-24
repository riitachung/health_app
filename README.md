# AI Health

AI Health is a personal health and wellness application designed to transform Apple Health data into understandable and explainable insights about sleep, recovery, and daily energy.

The project is currently under active development.

## 🎯 Project Goal

The goal of AI Health is to build a system that uses personal health data collected through Apple Health to provide three main metrics:

- **Sleep Score** — evaluates sleep quality relative to the user's personal baseline, considering sleep duration, stages such as REM, Core and Deep sleep, awakenings, and relevant physiological indicators.
- **Recovery Score** — estimates overnight physiological recovery using indicators such as HRV, resting heart rate, sleep, respiratory rate, and deviations from personal baselines.
- **Energy Score** — an estimated daily energy/readiness level that starts from the user's overnight state and can evolve throughout the day according to activity and physiological signals.

A core principle of the project is **explainability**.

A score should never simply display a number. The application should also be able to explain which measured factors contributed to it.

For example:

> Recovery is lower today mainly because HRV is below your 28-day baseline and resting heart rate is above your usual range.

The application is intended for **wellness and personal data exploration**, not medical diagnosis.

---

## 🧠 Design Principles

The project follows several principles:

### Personal baselines

Health metrics are interpreted primarily relative to the user's own historical data rather than generic population thresholds.

### Explainable scores

Sleep, Recovery and Energy scores should be deterministic and understandable before more advanced machine learning approaches are considered.

### Measured data vs calculated metrics

The system explicitly distinguishes between:

1. data measured by Apple Health / Apple Watch;
2. metrics calculated by the application;
3. interpretations generated from those metrics.

### Data-driven AI

AI will eventually be used to explain and interpret structured findings rather than being given raw health data and asked to generate unsupported conclusions.

### Privacy

Health data is sensitive. Raw Apple Health exports are stored locally and excluded from version control.

---

## 🏗️ Current Architecture

The current data pipeline is:

```text
Apple Watch
     │
     ▼
Apple Health
     │
     ▼
Apple Health Export (XML)
     │
     ▼
Streaming Health Importer
     │
     ▼
Normalized HealthMetric objects
     │
     ▼
Baseline Engine          [planned]
     │
     ▼
Scoring Engine           [planned]
 ┌───────┼────────┐
 ▼       ▼        ▼
Sleep  Recovery  Energy
     │
     ▼
Dashboard                [planned]
```

The Apple Health export currently used for development is approximately 2.2 GB, so the importer processes the XML as a stream rather than loading the complete document into memory.

---

## ✅ Current Progress

The project currently supports:

- Python development environment using a virtual environment
- Git/GitHub version control
- Apple Health XML ingestion
- memory-efficient streaming XML parsing using `lxml`
- normalization of Apple Health records into internal `HealthMetric` objects
- extraction of:
  - Heart Rate Variability (HRV SDNN)
  - Resting Heart Rate
  - Respiratory Rate
- protection of raw health data through `.gitignore`

The importer has been tested against a real Apple Health export containing thousands of physiological measurements.

---

## 🚧 Development Roadmap

### Phase 1 — Health Data Ingestion

- [x] Parse Apple Health XML
- [x] Support large exports using streaming
- [x] Import HRV
- [x] Import Resting Heart Rate
- [x] Import Respiratory Rate
- [ ] Import sleep data
- [ ] Import sleep stages
- [ ] Import relevant activity/workout data

### Phase 2 — Personal Baselines

- [ ] Build daily health summaries
- [ ] Calculate rolling personal baselines
- [ ] Handle missing data
- [ ] Handle outliers
- [ ] Compare current measurements with historical baseline

### Phase 3 — Scoring

- [ ] Sleep Score v1
- [ ] Recovery Score v1
- [ ] Energy Score v1
- [ ] Factor contribution/explanation system
- [ ] Document scoring methodology and limitations

### Phase 4 — Application

- [ ] Build dashboard
- [ ] Display current scores
- [ ] Explain score contributors
- [ ] Add 7-day trends
- [ ] Add 30-day trends
- [ ] Add 90-day trends

### Phase 5 — AI Insights

- [ ] Detect meaningful patterns in historical data
- [ ] Generate structured health observations
- [ ] Integrate an LLM for natural-language explanations
- [ ] Add safeguards against unsupported health claims
- [ ] Evaluate generated insights for factual consistency

### Phase 6 — Production Engineering

- [ ] Automated tests
- [ ] CI pipeline
- [ ] Persistent data storage
- [ ] API/backend if required
- [ ] Security and privacy review
- [ ] Architecture documentation
- [ ] Deployment strategy
- [ ] Native HealthKit integration when an appropriate macOS development environment is available

---

## 🛠️ Technology Stack

### Currently used

- **Python 3**
- **lxml**
- **Git**
- **GitHub**
- **WSL / Ubuntu**
- **Apple Health data**

### Planned / under evaluation

- Data analysis: Python / Pandas / NumPy
- Local persistence: SQLite
- Backend: FastAPI
- AI: LLM APIs with structured outputs
- Mobile: Swift / SwiftUI / HealthKit
- Testing: pytest
- CI/CD: GitHub Actions

Technologies are intentionally introduced only when they solve a concrete project requirement.

---

## 📁 Project Structure

```text
health_app/
│
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── apple_health_parser.py
│   └── health_importer.py
│
├── data/                   # Local health data — never committed
├── import_data.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

This structure will evolve as the project grows.

---

## 🔐 Privacy

Apple Health exports may contain highly sensitive personal health information.

For this reason:

- the `data/` directory is excluded from Git;
- raw Apple Health exports must never be committed;
- future development will follow data-minimization principles;
- external AI services should receive only the minimum information required for a specific task.

No personal health dataset is included in this repository.

---

## ⚕️ Health Disclaimer

AI Health is a software engineering and personal wellness project.

It is **not a medical device**, does not provide medical diagnoses, and should not be used as a substitute for professional medical advice.

Calculated scores represent estimates derived from available health data and their methodology and limitations will be documented.

---

## 🎓 Project Motivation

This project is being developed as an individual Computer Science / Software Engineering project with two goals:

1. build a genuinely useful personal health application;
2. develop practical experience in software engineering, data processing, APIs, databases, mobile development, AI/LLMs, testing, security, architecture and deployment.

The project is intentionally being developed incrementally, with an emphasis on understanding and documenting technical decisions rather than generating a finished application as quickly as possible.
