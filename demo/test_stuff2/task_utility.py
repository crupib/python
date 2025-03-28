import uuid
import requests

ENDPOINT = "https://todo.pixegami.io"

class TaskUtility:

    @staticmethod
    def new_task_payload():
        user_id = f"test_user_{uuid.uuid4().hex}"
        content = f"test_content_{uuid.uuid4().hex}"
        return {
            "content":content,
            "user_id": user_id,
            "is_done":False,
        }

    @staticmethod
    def create(payload):
        return requests.put(ENDPOINT + "/create-task", json=payload)

    @staticmethod
    def update(payload):
        return requests.put(ENDPOINT + "/update-task", json=payload)

    @staticmethod
    def get(task_id):
        return requests.get(ENDPOINT + f"/get-task/{task_id}")

    @staticmethod
    def lists(user_id):
        return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

    @staticmethod
    def delete(task_id):
        return requests.delete(ENDPOINT + f"/delete-task/{task_id}")



def test_reach_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_new_task_creation():
    #create a new task record
    payload = TaskUtility.new_task_payload()
    new_task_response = TaskUtility.create(payload)
    assert new_task_response.status_code == 200

    #check if the response data and payload is the same
    data = new_task_response.json()
    fetched_task_response = TaskUtility.get(data["task"]["task_id"])
    assert fetched_task_response.status_code == 200
    fetched_task_data = fetched_task_response.json()
    assert fetched_task_data["content"] == payload["content"]
    assert fetched_task_data["user_id"] == payload["user_id"]

def test_update_task():
    #create a new task
    payload = TaskUtility.new_task_payload()
    new_task_response = TaskUtility.create(payload)
    task_id = new_task_response.json()["task"]["task_id"]
    #update the task
    new_payload =  {
        "content": "new content",
        "user_id": payload["user_id"],
        "task_id": task_id,
        "is_done": True,
    }
    updated_task_response = TaskUtility.update(new_payload)
    assert updated_task_response.status_code == 200
    #check if the updated repsonse and new payload is same
    fetched_task_data = TaskUtility.get(task_id)
    assert fetched_task_data.status_code == 200
    fetched_task_data = fetched_task_data.json()
    assert fetched_task_data["content"] == new_payload["content"]
    assert fetched_task_data["user_id"] == new_payload["user_id"]


def test_list_tasks():
    n = 5
    #create n task record
    payload = TaskUtility.new_task_payload()
    for _ in range(n):
        new_task_response = TaskUtility.create(payload)
        assert new_task_response.status_code == 200
    #list all tasks
    fetched_task_data = TaskUtility.lists(payload["user_id"])
    assert fetched_task_data.status_code == 200
    data = fetched_task_data.json()
    #check if the number of tasks are same
    assert len(data["tasks"]) == n

def test_delete_task():
    #create a new task record
    payload = TaskUtility.new_task_payload()
    new_task_response = TaskUtility.create(payload)
    assert new_task_response.status_code == 200
    task_id = new_task_response.json()["task"]["task_id"]
    #delete that record
    deleted_task_response = TaskUtility.delete(task_id)
    assert deleted_task_response.status_code == 200
    #try to get deleted record, it should throw 404 error
    fetched_task_data = TaskUtility.get(task_id)
    assert fetched_task_data.status_code == 404
