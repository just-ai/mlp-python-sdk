import time


def wait_for(condition, timeout=5):
    """Wait for a condition to be true with a timeout."""
    start_time = time.time()
    counter = 1
    while not condition() and time.time() - start_time < timeout:
        if counter % 10 == 0:
            print(f"Waiting for condition {condition} ...")
        time.sleep(0.1)
        counter += 1
    assert condition()


def wait_for_state(expected, actual, timeout=5):
    """Wait for the connector to reach the expected state with a timeout."""
    start_time = time.time()
    counter = 1
    while True:
        val = actual()
        if val == expected or time.time() - start_time > timeout:
            break
        if counter % 10 == 0:
            print(f"Waiting for transition to state: {expected}, current state: {val} ...")
        time.sleep(0.1)
        counter += 1
    assert actual() == expected
