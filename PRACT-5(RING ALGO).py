class RingAlgorithm:
    def __init__(self, processes):
        self.processes = sorted(processes)  # Sorted for ring structure
        self.leader = None

    def start_election(self, initiator):
        print(f"Process {initiator} starts the election.")
        election_message = [initiator]
        current = (self.processes.index(initiator) + 1) % len(self.processes)

        while self.processes[current] != initiator:
            election_message.append(self.processes[current])
            print(f"Process {self.processes[current]} passes the election message.")
            current = (current + 1) % len(self.processes)
        
        self.leader = max(election_message)
        print(f"Process {self.leader} becomes the leader.")

# Example Usage
processes = [1, 2, 3, 4, 5]
ring = RingAlgorithm(processes)
ring.start_election(3)
