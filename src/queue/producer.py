from src.queue.db import connect


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


if __name__ == "__main__":
    pass
