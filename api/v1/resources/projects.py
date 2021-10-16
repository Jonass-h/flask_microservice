import json
from flask import abort, request
from flask_restplus import Namespace, Resource
from mongoengine import DoesNotExist

from v1.database.models import Project


projects = Namespace('v1/projects', description='Projects namespace')

@projects.route('/')
class ProjectsApi(Resource):
    def get(self):
        '''List all Projects'''
        projects = Project.objects.all()
        return json.loads(projects.to_json()), 200
@projects.route('/add')
class AddProjectApi(Resource):
    def post(self):
        '''Add a given project'''
        body = request.get_json()
        p = Project(**body)
        p.save()

        id = p.id

        return {"message":"project Added with id = " + str(id)}, 200

@projects.route('/get/<id>')
@projects.response(404, 'Project not found')
@projects.param('id', 'The project identifier')
class ProjectApi(Resource):
    def get(self, id):
        '''Fetch a given project'''
        try:
            project = Project.objects.get(id=id)
            return json.loads(project.to_json()), 200
        except(DoesNotExist):
            abort(404)
        except:
    
            abort(500)
