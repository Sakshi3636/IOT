def berkeley_algorithm(process_clocks):
    """
    Perform clock synchronization using the Berkeley Algorithm.
    :param process_clocks: Dictionary of process IDs and their clocks (in seconds).
    :return: Synchronized process clocks.
    """
    print("--- Berkeley Algorithm ---")
    print("Initial clocks:", process_clocks)

    # Step 1: Calculate average time
    average_time = sum(process_clocks.values()) / len(process_clocks)
    print(f"Average time: {average_time:.2f}s")

    # Step 2: Calculate offsets and synchronize clocks
    synchronized_clocks = {}
    for pid, clock in process_clocks.items():
        offset = average_time - clock
        print(f"Process {pid}: Offset {offset:+.2f}s")
        synchronized_clocks[pid] = clock + offset

    print("Synchronized clocks:", synchronized_clocks)
    return synchronized_clocks

# Example Usage
process_clocks = {1: 100, 2: 105, 3: 98, 4: 102}  # Example clocks
synchronized_clocks = berkeley_algorithm(process_clocks)
