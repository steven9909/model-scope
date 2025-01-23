import enum
import typing

import firebase_admin.firestore as firestore
import pydantic

import app.services.firebase as firebase

# Create your models here.


class TaskStatus(str, enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


class Task(pydantic.BaseModel):
    collection_path: str = pydantic.Field("/tasks", exclude=True)

    id: str
    dataset_reference: firestore.firestore.DocumentReference
    model_reference: firestore.firestore.DocumentReference
    status: TaskStatus

    def to_firebase(self):
        try:
            firebase.Firestore().client().collection(Task.collection_path).document(
                self.id
            ).set(self.model_dump())

        except Exception as e:
            raise Exception(
                f"Error saving document `{self.id}` to `{Task.collection_path}`: {e}"
            )

    @staticmethod
    def from_firestore(document_id: str) -> "Task":
        try:
            document_snapshot = typing.cast(
                firestore.firestore.DocumentReference,
                firebase.Firestore()
                .client()
                .collection(Task.collection_path)
                .document(document_id),
            ).get()

            return Task(id=document_snapshot.id, **document_snapshot.to_dict())

        except Exception as e:
            raise Exception(
                f"Error fetching document `{document_id}` from `{Task.collection_path}`: {e}"
            )
