# Fullstack Development — Detailed Progress Summary

This repository is a learning-focused workspace containing your notes, screenshots, a Python virtual environment, and a small Django project. Below is a detailed summary of the work present in the repository and actionable notes about next steps.

Summary of what's in this repository
- `creation process/` — documentation you wrote while learning and experimenting:
	- `creation process/django/` contains HTML guides and screenshots (e.g. `creating_app.html`, `django_project.html`, `install.png`, `start_project.png`) that document how you installed Django, created a project, and created an app.
	- `creation process/environment/` contains notes and images showing how you created the virtual environment (`environment.html`, `env.png`).
	- `creation process/styles/style.css` — stylesheet used for the HTML guides.

- `env/` — a complete Python virtual environment (venv), including `Scripts/`, `Lib/`, and installed site-packages. This indicates you created and used a local env for development.

- `one/` — your Django project and app:
	- `manage.py` — Django management script.
	- `db.sqlite3` — development SQLite database (present in the repo).
	- `one/` — Django project package with `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`.
		- Note: `settings.py` currently contains only the default Django apps in `INSTALLED_APPS` — your app `First` is present on disk but is not yet listed in `INSTALLED_APPS`.
	- `First/` — Django app scaffold with `models.py`, `views.py`, `admin.py`, `tests.py`, and a `migrations/` package. `models.py` is currently empty (no custom models defined yet).

What this tells us (actions you have completed)
- You created a virtual environment (`env/`) and installed packages into it (site-packages present).
- You created a Django project named `one` (project package and `manage.py` exist).
- You created a Django app named `First` (folder and app files exist; `creating_app.html` documents the `python manage.py startapp First` step).
- You have a development database file `db.sqlite3`, which implies at least some migrations were run (default apps' tables exist).
- You documented the process with HTML pages and screenshots inside `creation process/`.

Current gaps and recommended next steps
- Add the app `First` to `INSTALLED_APPS` in `one/settings.py` so Django recognizes it during migrations and admin registration. Example:

	```python
	INSTALLED_APPS = [
			# ... default apps ...
			'First',
	]
	```

- Define models in `First/models.py` and run `python manage.py makemigrations` and `python manage.py migrate` to create app tables.
- If you want a reproducible dependency listing, I can generate a `requirements.txt` from the packages in `env/Lib/site-packages` (recommended) or by using `pip freeze` in your activated venv.
- Consider removing `env/` from source control and adding it to `.gitignore`, then recreate a small `requirements.txt` to keep the repo lean.

Quick commands (run from `one` project root)

```powershell
# activate venv on Windows (PowerShell)
./env/Scripts/Activate.ps1

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


--
Updated: Jan 4, 2026
--
Updated: Jan 4, 2026
