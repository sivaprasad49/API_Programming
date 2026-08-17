from .exceptions import JobNotFoundError, DuplicateJobError

class JobManager:
    def __init__(self):
        self.jobs = {}

    def add_job(self, job_id, job_data):
        if job_id in self.jobs:
            raise DuplicateJobError(job_name=job_id)
        self.jobs[job_id] = job_data