import multiprocessing
import time
import sys

N = 3

def writer(shared_records, locks, synchronized):
    print("Writer process started.", flush=True)

    for i in range(N):
        if synchronized:
            locks[i].acquire()

        shared_records[i][0] = 100 - i * 10
        shared_records[i][1] = 10 + i * 5
        shared_records[i][2] = 1

        print(
            f"Writer: Record {i + 1} updated: "
            f"Stock={shared_records[i][0]}, "
            f"Dispatch={shared_records[i][1]}",
            flush=True
        )

        if synchronized:
            locks[i].release()

        time.sleep(0.2)


def reader(shared_records, locks, synchronized):
    print("Reader process started.", flush=True)

    for i in range(N):
        if synchronized:
            # Wait until the writer publishes this record
            while True:
                with locks[i]:
                    if shared_records[i][2] == 1:
                        stock = shared_records[i][0]
                        dispatch = shared_records[i][1]
                        break
                time.sleep(0.01)
        else:
            stock = shared_records[i][0]
            dispatch = shared_records[i][1]

        if shared_records[i][2] == 1:
            print(
                f"Reader: Record {i + 1}: "
                f"Stock={stock}, Dispatch={dispatch}, READY",
                flush=True
            )
        else:
            print(
                f"Reader: Record {i + 1}: "
                "Data NOT READY",
                flush=True
            )

        time.sleep(0.1)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "sync"
    order = sys.argv[2] if len(sys.argv) > 2 else "writer-first"

    synchronized = mode == "sync"

    # Shared memory containing stock, dispatch and status
    manager = multiprocessing.Manager()
    records = manager.list([
        manager.list([0, 0, 0]) for _ in range(N)
    ])

    locks = [multiprocessing.Lock() for _ in range(N)]

    if order == "reader-first":
        r = multiprocessing.Process(
            target=reader,
            args=(records, locks, synchronized)
        )
        r.start()
        time.sleep(0.3)

        w = multiprocessing.Process(
            target=writer,
            args=(records, locks, synchronized)
        )
        w.start()
    else:
        w = multiprocessing.Process(
            target=writer,
            args=(records, locks, synchronized)
        )
        w.start()
        time.sleep(0.3)

        r = multiprocessing.Process(
            target=reader,
            args=(records, locks, synchronized)
        )
        r.start()

    w.join()
    r.join()

    print("Warehouse IPC experiment completed.")
    manager.shutdown()
