from src.db import connect


def reset_queue() -> None:
    conn, cur = connect()
    try:
        cur.execute("UPDATE task SET status = 'pending' WHERE status = 'in_progress'")
        rows_affected = cur.rowcount
        conn.commit()
        print(f"{rows_affected} rows were updated.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()


if __name__ == "__main__":
    reset_queue()
