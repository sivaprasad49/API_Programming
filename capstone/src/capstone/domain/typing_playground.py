from models import JobStatus

def describe_job(status: JobStatus|None) -> str:
    """
    Describe the job status.

    Args:
        status (JobStatus|None): The status of the job.

    Returns:
        str: A description of the job status.
    """
    if status is None:
        return "The job status is unknown."
    if status == JobStatus.PENDING:
        return "The job is pending and waiting to be processed."
    elif status == JobStatus.IN_PROGRESS:
        return "The job is currently being processed."
    elif status == JobStatus.COMPLETED:
        return "The job has been completed successfully."
    elif status == JobStatus.FAILED:
        return "The job has failed during processing."
    else:
        return "Unknown job status."


class Paginated[T]():
    """
    A generic class representing a paginated list of items.

    Attributes:
        items (list[T]): The list of items on the current page.
        total_count (int): The total number of items across all pages.
        page_number (int): The current page number.
        page_size (int): The number of items per page.
    """

    def __init__(self, items: list[T], total_count: int, page_number: int, page_size: int):
        self.items = items
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size

    def __repr__(self) -> str:
        return f"Paginated(items={self.items}, total_count={self.total_count}, page_number={self.page_number}, page_size={self.page_size})"


from typing import Protocol

class Notifier(Protocol):
    """
    A protocol representing a notifier that can send notifications.

    Methods:
        notify(message: str) -> None: Send a notification with the given message.
    """

    def notify(self, message: str) -> None:
        ...

class EmailNotifier:
    """
    A concrete implementation of the notifier protocol that sends email notifications.

    Methods:
        notify(message: str) -> None: Send an email notification with the given message.
    """

    def notify(self, message: str) -> None:
        print(f"Sending email notification: {message}")

class SmsNotifier:
    """
    A concrete implementation of the notifier protocol that sends SMS notifications.

    Methods:
        notify(message: str) -> None: Send an SMS notification with the given message.
    """

    def notify(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")

def send_notification(notifier: Notifier, message: str) -> None:
    """
    Send a notification using the provided notifier.

    Args:
        notifier (Notifier): An instance of a class that implements the notifier protocol.
        message (str): The message to be sent in the notification.
    """
    notifier.notify(message)

from typing import TypedDict

class RawWebhookPayload(TypedDict):
    """
    A TypedDict representing the structure of a raw webhook payload.

    Attributes:
        event (str): The type of event that triggered the webhook.
        data (dict): The data associated with the event.
        timestamp (str): The timestamp when the event occurred.
    """
    event: str
    data: dict
    timestamp: str