import random
import time
from multiprocessing import Process, Manager

def process_function(process_id, data, connections):
    for _ in range(5):  # Simulate 5 rounds of communication
        time.sleep(random.uniform(0.1, 0.5))  # Simulate random processing time
        
        # Each process updates its own data
        data[process_id] += f"Round {_ + 1} update from Process {process_id}"

        # Share data with randomly selected connected processes
        for neighbor_id in connections[process_id]:
            data[neighbor_id] = data[process_id]

        # Display the updated data of the current process
        print(f"Process {process_id} updated data: {data[process_id]}")

def main():
    # Number of processes
    num_processes = 5

    # Create a shared data structure using Manager
    with Manager() as manager:
        # Initialize data and connections
        data = manager.list([f"Initial data for Process {i}" for i in range(num_processes)])
        connections = {i: random.sample([j for j in range(num_processes) if j != i], k=random.randint(1, 2)) for i in range(num_processes)}

        # Create processes
        processes = []
        for i in range(num_processes):
            processes.append(Process(target=process_function, args=(i, data, connections)))

        # Start processes
        for process in processes:
            process.start()

        # Join processes
        for process in processes:
            process.join()

if __name__ == "__main__":
    main()

