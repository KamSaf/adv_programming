from src.queue.db import connect


def get_status(id: str) -> str:
    conn, cur = connect()
    id = list(cur.execute("SELECT status FROM task WHERE id = :id", {"id": id}))[0][0]
    conn.close()
    return id
