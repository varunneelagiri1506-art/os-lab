import multiprocessing as mp
import time

TOTAL_RECORDS = 5

def writer(shared_data, ready, lock, delay):
    for i in range(1, TOTAL_RECORDS + 1):
        time.sleep(delay)

        # TODO 1: Acquire the lock.
        # TODO 2: Write stock item ID and quantity
        #         into shared_data.
        # TODO 3: Set ready = 1 after writing.
        # TODO 4: Release the lock.

        print("Writer: Stock record updated", i)


def reader(shared_data, ready, lock, delay):
    for i in range(1, TOTAL_RECORDS + 1):
        time.sleep(delay)

        # TODO 5: Acquire the lock.
        # TODO 6: Check whether ready == 1.
        # TODO 7: Read and display the shared record.
        # TODO 8: Reset ready = 0 after reading.
        # TODO 9: Release the lock.


if __name__ == "__main__":
    # Shared memory: [stock item ID, quantity]
    shared_data = mp.Array('i', 2)
    ready = mp.Value('i', 0)
    lock = mp.Lock()

    w = mp.Process(
        target=writer,
        args=(shared_data, ready, lock, 0.5)
    )

    r = mp.Process(
        target=reader,
