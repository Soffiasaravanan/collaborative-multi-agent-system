from agents import Agent, ManagerAgent

researcher = Agent(
    "Researcher",
    "You are a meticulous researcher. Gather and summarize accurate information."
)

designer = Agent(
    "Designer",
    "You design beautiful and user-friendly web interfaces."
)

frontend = Agent(
    "Frontend",
    "You are an expert HTML, CSS and JavaScript developer. Create responsive websites."
)

backend = Agent(
    "Backend",
    "You are an expert Flask and Python developer."
)

tester = Agent(
    "Tester",
    "You are a software testing expert. Test websites and suggest improvements."
)

writer = Agent(
    "Writer",
    "You write professional documentation and explain code clearly."
)

manager = ManagerAgent({
    "Researcher": researcher,
    "Designer": designer,
    "Frontend": frontend,
    "Backend": backend,
    "Tester": tester,
    "Writer": writer,
})

if __name__ == "__main__":
    goal = input("Enter your goal: ")
    final_output = manager.execute(goal)

    print("\n=== FINAL OUTPUT ===\n")
    print(final_output)
