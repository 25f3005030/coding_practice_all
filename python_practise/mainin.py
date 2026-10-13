import psycopg2
import heapq 
import subprocess
from datetime import datetime 

# Database configuration parameters matching your pgAdmin setup
DB_CONFIG = {
    "dbname": "my_project1",
    "user": "postgres",
    "password": "hcverma#25",  # Replace with your actual password
    "host": "localhost",
    "port": "5432"
}

class Task:
    """Task object supporting priority comparison for Heap insertion."""
    def __init__(self, task_id, task_name, command, priority):
        self.task_id = task_id
        self.task_name = task_name
        self.command = command
        self.priority = priority

    def __lt__(self, other):
        # PDSA: Min-heap orders tasks by lowest priority integer first
        return self.priority < other.priority

class SystemTaskScheduler:
    def __init__(self):
        self.priority_queue = []  # Heap data structure ⚡

    def fetch_pending_tasks(self):
        """Loads pending tasks from PostgreSQL into the Min-Heap."""
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("SELECT task_id, task_name, command, priority FROM tasks WHERE status = 'PENDING';")
        rows = cursor.fetchall()
        
        for row in rows:
            task = Task(task_id=row[0], task_name=row[1], command=row[2], priority=row[3])
            heapq.heappush(self.priority_queue, task) # O(log N) insertion
            
        cursor.close()
        conn.close()
        print(f"🌸 Loaded {len(rows)} pending tasks into the Priority Queue.")

    def run_next_task(self):
        """Pops highest-priority task and executes it via system command."""
        if not self.priority_queue:
            print("🌸 No pending tasks to run!")
            return

        # PDSA: Min-Heap extraction O(log N)
        task = heapq.heappop(self.priority_queue)
        print(f"\n⚙️ Executing Task [{task.priority}]: {task.task_name} -> Command: '{task.command}'")

        # System Command Execution 🖥️
        try:
            result = subprocess.run(
                task.command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            output = result.stdout.strip() if result.returncode == 0 else result.stderr.strip()
            status = "COMPLETED" if result.returncode == 0 else "FAILED"
        except Exception as e:
            output = str(e)
            status = "ERROR"

        # DBMS Persistence 🗄️
        self._update_task_log(task.task_id, status, output)

    def _update_task_log(self, task_id, status, output):
        """Updates execution result back in PostgreSQL."""
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE tasks 
            SET status = %s, output = %s, executed_at = %s 
            WHERE task_id = %s;
        """, (status, output, datetime.now(), task_id))
        
        conn.commit()
        cursor.close()
        conn.close()
        print(f"🗄️ Task {task_id} status updated to: {status}")

# --- Example Execution Workflow ---
if __name__ == "__main__":
    scheduler = SystemTaskScheduler()
    
    # 1. Sync state from DB
    scheduler.fetch_pending_tasks()
    
    # 2. Execute tasks in exact priority order
    while scheduler.priority_queue:
        scheduler.run_next_task()