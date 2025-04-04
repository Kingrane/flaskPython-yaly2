import flask
from flask import jsonify, make_response, request
from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api', __name__
)


@blueprint.route('/api/jobs')
def get_jobs():
    sess = db_session.create_session()
    for i in range(5):
        j = Jobs()
        j.job = "JOB" + str(i + 1)
        j.work_size = i * 3
        j.team_leader = 1
        j.collaborators = '1'
        j.is_finished = False
        sess.add(j)
    sess.commit()
    jobs = db_session.create_session().query(Jobs).all()
    return jsonify({"jobs": [j.to_dict(only=["job",
                                             "work_size",
                                             "is_finished",
                                             ])
                             for j in jobs]})


@blueprint.route('/api/jobs/<int:job_id>')
def get_job_by_id(job_id):
    job = db_session.create_session().get(Jobs, job_id)
    if job is not None:
        return jsonify(job.to_dict())
    return make_response(404, "No such job")


@blueprint.app_errorhandler(404)
def error_not_found(e):
    return make_response(jsonify({'error': e.description}), 404)


@blueprint.route('/api/jobs', methods=['POST'])
def add_jobs():
    if request.json:
        j = Jobs()
        j.job = request.json["job"]
        j.work_size = int(request.json["work_size"])
        j.collaborators = request.json["collaborators"]
        j.is_finished = bool(request.json["is_finished"])
        j.team_leader = int(request.json["team_leader"])
        sess = db_session.create_session()
        sess.add(j)
        sess.commit()
        return make_response(jsonify({"ok": j.id}), 201)

    return flask.abort(500)


@blueprint.route('/api/jobs', methods=['PUT'])
def change_jobs():
    return flask.abort(500)


@blueprint.route('/api/jobs', methods=['DELETE'])
def delete_jobs():
    return flask.abort(500)
