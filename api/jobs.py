import flask
from flask import jsonify, make_response
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
