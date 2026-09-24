class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = Counter(tasks)
        tasks_to_process = [-val for val in task_freq.values()]
        heapq.heapify(tasks_to_process)
        cooldown = deque()

        time = 0
        while tasks_to_process or cooldown:
            time += 1
            if tasks_to_process:
                freq = 1 + heapq.heappop(tasks_to_process)
                if freq:
                    cooldown.append([freq, time + n])
            else:
                time = cooldown[0][1]
        
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(tasks_to_process, cooldown.popleft()[0])
            
        return time
            