# Accuknox Django Assignment

## 🔹 Django Signals Demonstration
Demonstrates that Django signals:
- Are synchronous by default
- Run in the same thread
- Run within the same database transaction

### How to run:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell
>>> from core.views import create_model_instance
>>> create_model_instance()
