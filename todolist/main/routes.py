from todolist.main import blueprint

@blueprint.route("/")
def main():
    return "Welcome"
