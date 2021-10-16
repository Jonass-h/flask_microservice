# flask_microservice

Yet another simple RESTful API wrote with Python, MongoDB and Flask microframework.

## Usage

```sh
$ docker-compose up
```

It will run both Web and Mongodb containers in Development environment on `localhost:5100`.
For other environments change ENV in `docker-compose.yml`:

```sh
web:
   ...
    environment:
      - ENV=Testing
```

You can use Development, Production or Testing or add your own environment in `api/config.py`.

### get all project

``bash
curl --location --request GET 'http://127.0.0.1:5100/v1/projects'
```
### get a single project with id

```bash
curl --location --request GET 'http://127.0.0.1:5100/v1/projects/get/616b09a792f3124f2c87d9a5'
```

### add a Project

```bash
curl --location --request POST 'http://127.0.0.1:5100/v1/projects/add' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "SOA Mini Project",
    "description": "yet another project !"
}'
```


## Structure

Here is a folder and file structure with explanation.

```
├── Dockerfile
├── LICENSE
├── README.md
├── api
│   ├── app.py - Entry point of application
│   ├── config.py - Configuration with environments
│   └── v1 - API version 1
│       ├── database
│       │   └── models.py - All data models app uses
│       └── resources
│           ├── routes.py - List of namespaces for routing
│           └── todos.py - Example Todo resource
├── docker-compose.yml
├── requirements.txt - Dependencies
└── tests
    └── text_base.py - Example test file
```

## Documentation

Thanks to handy decorators this boilerplate will generate Swagger with documentation on the fly.
By default Swagger runs on `/` so you should see it on `http://localhost:5100`. Read more [here](https://flask-restplus.readthedocs.io/en/stable/swagger.html).


## License

See LICENSE file.