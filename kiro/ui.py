def show_success(state):
    print("\n✨ Project created successfully!\n")
    print(f"📦 Project   : {state.project_name}")
    print(f"⚙ Runtime   : {state.runtime}")
    print(f"🚀 Framework : {state.framework}")

    if state.language:
        print(f"💻 Language  : {state.language}")

    print(f"📁 Location  : ./{state.project_name}\n")