from capstone.domain.exceptions import JobNotFoundError, DuplicateJobError

class JobManager:
    def __init__(self):
        self.jobs = {}

    def add_job(self, job_id, job_data):
        if job_id in self.jobs:
            raise DuplicateJobError(job_name=job_id)
        self.jobs[job_id] = job_data

    def get_job(self, job_id):
        if job_id not in self.jobs:
            raise JobNotFoundError(job_id=job_id)
        return self.jobs[job_id]

    def insert_into_db(self, sql, values):
        # Simulate inserting a job into a database
        print(f"Inserting job {values} into the database.")

    def update_status_to_db(self, values):
        print(f"Updated job {values} status.")