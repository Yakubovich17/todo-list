from todolist.tasks import blueprint

@blueprint.route("/")
def index():
    return "Hello world"
