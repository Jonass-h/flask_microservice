from v1.resources.projects import projects

def initialize_routes(api):
    api.add_namespace(projects)