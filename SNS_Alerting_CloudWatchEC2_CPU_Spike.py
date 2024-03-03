import time

class CPUSpiker:
    def __init__(self, duration_seconds=30, cpu_percentage=80, workload_multiplier=5000000):
        self.duration_seconds = duration_seconds
        self.cpu_percentage = cpu_percentage
        self.workload_multiplier = workload_multiplier

    def simulate(self):
        print(f"Simulating CPU spike at {self.cpu_percentage}%...")
        start_time = time.time()

        target_percentage = self.cpu_percentage / 100
        total_iterations = int(target_percentage * self.workload_multiplier)

        for _ in range(total_iterations):
            result = 0
            for i in range(1, 1001):
                result += i

        elapsed_time = time.time() - start_time
        remaining_time = max(0, self.duration_seconds - elapsed_time)
        time.sleep(remaining_time)

        print("CPU spike simulation completed.")

if __name__ == '__main__':
    cpu_spiker = CPUSpiker(duration_seconds=30, cpu_percentage=80, workload_multiplier=5000000)
    cpu_spiker.simulate()
