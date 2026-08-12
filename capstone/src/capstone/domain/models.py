from enum import Enum
from dataclasses import dataclass

class JobStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Job:
    id: int
    name: str
    priority: int
    status: JobStatus