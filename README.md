# Sml_Project

Small ML project that demonstrates data ingestion and a simple training pipeline using the StudentsPerformance dataset.

**Setup**
- **Python:** Use Python 3.10+.
- **Create venv (recommended):**

```
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

- If you already have the project's venv, run with its Python executable. Example on this workspace:

```
c:/Users/Shlok/sml_project/myenv/Scripts/python.exe raw_data_ingestion.py
```

**Run (quick)**
- Prepare and ingest raw data:

```
python raw_data_ingestion.py
```

- Train a simple model and save it to `artifact/model.pkl`:

```
python train_model.py
```

**Key outputs**
- [artifact/train_data.csv](artifact/train_data.csv) — training split produced by ingestion.
- [artifact/test_data.csv](artifact/test_data.csv) — test split produced by ingestion.
- [artifact/model.pkl](artifact/model.pkl) — trained RandomForest model (joblib).

**Important files**
- [raw_data_ingestion.py](raw_data_ingestion.py) — copies dataset and runs ingestion.
- [train_model.py](train_model.py) — training script and model saver.
- [src/components/data_injestion.py](src/components/data_injestion.py) — ingestion component.
- [src/custom_exception.py](src/custom_exception.py) — improved exception helper.
- [requirements.txt](requirements.txt) — Python dependencies.

**Commits & push**
- Commit locally and push to remote:

```
git add .
git commit -m "Describe changes"
git push -u origin main
```

**Notes**
- The project expects the raw CSV at `artifact/StudentsPerformance.csv`.
- If you run into import issues, ensure the venv from this repo is activated or install the packages in your active environment.

