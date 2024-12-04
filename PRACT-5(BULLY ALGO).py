class BullyAlgorithm:
    def __init__(self, processes):
        self.processes = processes  # List of process IDs
        self.leader = None

    def start_election(self, initiator):
        print(f"Process {initiator} starts the election.")
        higher = [p for p in self.processes if p > initiator]
        
        if not higher:
            self.leader = initiator
            print(f"Process {initiator} becomes the leader.")
        else:
            print(f"Process {initiator} sends messages to {higher}.")
            for p in higher:
                print(f"Process {p} responds to the election message.")
            self.leader = max(higher)
            print(f"Process {self.leader} becomes the leader.")

# Example Usage
processes = [1, 2, 3, 4, 5]
bully = BullyAlgorithm(processes)
bully.start_election(3)
