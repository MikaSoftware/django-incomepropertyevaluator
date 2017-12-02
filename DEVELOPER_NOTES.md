# Developer Notes
## Library
The goal of this article is to keep track the libraries that this project is dependent on.

### Python
Here are the libraries that this project utilizes, please update this list as
new libraries get added.

```bash
pip install django                        # Our MVC Framework
pip install django-environ                # Environment Variables with 12factorization
pip install Pillow                        # Req: ImageField
pip install psycopg2                      # Postgres SQL ODBC
pip install django-tenants                # Multi-Tenancy Handler
pip install djangorestframework           # RESTful API Endpoint Generator
pip install django_filter                 # Filter querysets dynamically
pip install django-crispy-forms           # Req: djangorestframework
pip install django-cors-headers           # Allow External Cors Headers
pip install gunicorn                      # Web-Server Helper
pip install django-rq                     # Redis Queue Library
pip install rq-scheduler                  # Redis Queue Scheduler Library
pip install django-anymail[mailgun]       # Third-Party Email
pip install django-htmlmin                # HTML Minifier
pip install django-trapdoor               # Automatically Exploit Scanners
pip install py-mortgagekit                # Mortgage Computation Library
pip install py-incomepropertyevaluatorkit # Real Estate Computation Library
```

```bash
No longer used...
pip install python-dotenv                 # Environment Variables
```

And run this command to save:

```
pip freeze > requirements.txt
```
