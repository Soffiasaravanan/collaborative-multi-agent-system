import ollama

MODEL = "llama3.2"

def call_llm(system_prompt, user_prompt):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response["message"]["content"]


class Agent:
    def __init__(self, name, role_prompt):
        self.name = name
        self.role_prompt = role_prompt

    def run(self, task):
        print(f"\n[{self.name}] working on: {task}")
        result = call_llm(self.role_prompt, task)
        print(f"[{self.name}] done.")
        return result


class ManagerAgent:
    def __init__(self, specialists):
        self.specialists = specialists

    def plan(self, goal):
        specialist_list = ", ".join(self.specialists.keys())

        planning_prompt = f"""
Break the goal into 2-4 subtasks.
Assign each subtask to exactly one of these specialists:
{specialist_list}

Return only:
SPECIALIST | TASK

Goal:
{goal}
"""

        raw_plan = call_llm("You are a precise project planner.", planning_prompt)

        tasks = []
        for line in raw_plan.strip().splitlines():
            if "|" in line:
                name, task = line.split("|", 1)
                name = name.strip()
                if name in self.specialists:
                    tasks.append({"specialist": name, "task": task.strip()})
        return tasks

    def execute(self, goal):
        tasks = self.plan(goal)

        results = []
        for t in tasks:
            agent = self.specialists[t["specialist"]]
            output = agent.run(t["task"])
            results.append(f"### {t['specialist']}\n{output}")

        synthesis_prompt = (
            f"Combine these specialist outputs into one final answer for '{goal}'.\n\n"
            + "\n\n".join(results)
        )

        return call_llm(
            "You are a synthesis editor.",
            synthesis_prompt,
        )
    
