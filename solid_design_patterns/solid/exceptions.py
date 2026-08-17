class DomainError(Exception):
    """Base class for domain-specific exceptions."""
    pass

class NotFoundError(DomainError):
    """Exception raised when an entity is not found in the system."""
    def __init__(self, entity_name, entity_id, message=None):
        self.entity_name = entity_name
        self.entity_id = entity_id
        self.message = message or f"{self.entity_name} with ID {self.entity_id} not found."
        super().__init__(self.message)

class ConflictError(DomainError):
    """Exception raised when there is a conflict in the system."""
    def __init__(self, entity_name, entity_id, message=None):
        self.entity_name = entity_name
        self.entity_id = entity_id
        self.message = message or f"Conflict occurred for {self.entity_name} with ID {self.entity_id}."
        super().__init__(self.message)

class JobNotFoundError(NotFoundError):
    """Exception raised when a job is not found in the system."""
    def __init__(self, job_id, message=None):
        self.job_id = job_id
        self.message = message or f"Job with ID {self.job_id} not found."
        super().__init__(entity_name="Job", entity_id=self.job_id, message=self.message)

class DuplicateJobError(ConflictError):
    """Exception raised when a duplicate job is detected in the system."""
    def __init__(self, job_name, message=None):
        self.job_name = job_name
        self.message = message or f"Duplicate job detected with name '{self.job_name}'."
        super().__init__(entity_name="Job", entity_id=self.job_name, message=self.message)