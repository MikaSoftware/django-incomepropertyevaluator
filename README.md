# django-incomepropertyevaluator
**This library is currently being developed and is not production quality ready!**

## Build Status
[![Build Status](https://travis-ci.org/MikaSoftware/django-incomepropertyevaluator.svg?branch=master)](https://travis-ci.org/MikaSoftware/django-incomepropertyevaluator)
[![Coverage Status](https://coveralls.io/repos/github/MikaSoftware/django-incomepropertyevaluator/badge.svg?branch=master)](https://coveralls.io/github/MikaSoftware/django-incomepropertyevaluator?branch=master)

## Overview
The web app engine which powers "Income Property Evaluator". http://incomepropertyevaluator.com

## Minimum Requirements
* Python 3.6

## Installation
1. Install the library.

  ```bash
  git clone https://github.com/MikaSoftware/django-incomepropertyevaluator.git
  ```

1b. Installation

  ```bash
  pip install -r requirements.txt
  pip install "git+https://github.com/MikaSoftware/django-trapdoor"
  pip install "git+https://github.com/MikaSoftware/py-mortgagekit"
  pip install "git+https://github.com/MikaSoftware/py-incomepropertyevaluatorkit"
  ```

2. Update.

  ```sql
  drop database incomepropertyevaluator_db;
  create database incomepropertyevaluator_db;
  \c incomepropertyevaluator_db;
  CREATE USER django WITH PASSWORD '123password';
  GRANT ALL PRIVILEGES ON DATABASE incomepropertyevaluator_db to django;
  ALTER USER django CREATEDB;
  ALTER ROLE django SUPERUSER;
  CREATE EXTENSION postgis;
  ```

3. Run:

  ```bash
  python manage.py makemigrations; \
  python manage.py migrate; \
  python manage.py populate_public; \
  python manage.py setup_fixtures;
  ```

4. Usage:

  ```bash
  sudo python manage.py runserver incomepropertyevaluator.com:80
  ```

In your browser enter ``incomepropertyevaluator.com:80``.

 5. See: https://github.com/AcademicsToday/academicstoday-django/wiki/Setup-Project-on-MacOS


## Usage
### Development
Here is an example of using the using the library in your code.

  ```python
  #TODO: Write example...
  ```

## License
This library is licensed under the **BSD** license. See [LICENSE.md](LICENSE.md) for more information.
