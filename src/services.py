from time import sleep
from src.db import connect
from src.utils import create_response


def create_task(file_name: str) -> int:
    conn, cur = connect()
    cur.execute(
        "INSERT INTO task (file_name, status) VALUES (:file_name, :status)",
        {"file_name": file_name, "status": "pending"},
    )
    data = list(cur.execute("SELECT id FROM task ORDER BY id DESC LIMIT 1;"))[0][0]
    conn.commit()
    print("\n✅ New task created!")
    conn.close()
    return data


def get_status(id: str) -> str:
    conn, cur = connect()
    id = list(
        cur.execute("SELECT status, num_of_people FROM task WHERE id = :id", {"id": id})
    )[0]
    conn.close()
    return id


def await_analysis_result(file_name: str | None) -> dict:
    id = create_task(file_name) if file_name else None
    if not id:
        return {"message": "Invalid data provided"}
    status = "pending"
    num_of_people = 0
    while status != "done":
        sleep(2)
        status, num_of_people = get_status(str(id))
    return create_response(id=id, status=status, num_of_people=int(num_of_people))


def update_task(task_id: int, status: str, num_of_people: int | None = None) -> None:
    conn, cur = connect()
    if num_of_people:
        cur.execute(
            "UPDATE task SET status = :status, num_of_people = :num_of_people WHERE id = :id",
            {"status": status, "num_of_people": num_of_people, "id": task_id},
        )
    else:
        cur.execute(
            "UPDATE task SET status = :status WHERE id = :id",
            {"status": status, "id": task_id},
        )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    pass
