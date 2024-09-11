from flask import Flask, make_response, request

from lab07_solution_utils.task import Task
from lab07_solution_utils.storage import read_tasks, reset_storage, write_tasks


app = Flask(__name__)

@app.route('/reset', methods=['POST'])
def reset():
    reset_storage()
    return make_response('Reset storage succesfully', 200)


# TODO: Implement all the other endpoints
