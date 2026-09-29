import json
import os

DATA_FILE = "data.json"

# ==========================================
# FILE HANDLING FUNCTIONS
# ==========================================

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"tasks": [], "expenses": []}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("\n[!] Warning: Corrupted data file detected. Starting fresh.")
        return {"tasks": [], "expenses": []}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# ==========================================
# TASK MANAGEMENT MODULE
# ==========================================

def add_task(data):
    print("\n--- ADD TASK ---")
    title = input("Enter task description: ").strip()
    if title:
        task = {"id": len(data["tasks"]) + 1, "title": title, "done": False}
        data["tasks"].append(task)
        save_data(data)
        print(f"[✔] Task '{title}' added successfully!")
    else:
        print("[❌] Error: Task description cannot be empty!")

def view_tasks(data):
    print("\n--- YOUR TASKS ---")
    if not data["tasks"]:
        print("No tasks found.")
        return
    
    for t in data["tasks"]:
        status = "[✔ Done]" if t['done'] else "[❌ Pending]"
        print(f"{t['id']}. {t['title']} {status}")

def complete_task(data):
    print("\n--- COMPLETE TASK ---")
    if not data["tasks"]:
        print("No tasks available to complete.")
        return

    task_id_str = input("Enter Task ID to mark complete: ").strip()
    if task_id_str:
        try:
            task_id = int(task_id_str)
            for task in data["tasks"]:
                if task["id"] == task_id:
                    task["done"] = True
                    save_data(data)
                    print(f"[✔] Task {task_id} marked complete!")
                    return
            print("[❌] Error: Task ID not found.")
        except ValueError:
            print("[❌] Error: Please enter a valid numeric ID.")

# ==========================================
# EXPENSE TRACKER MODULE
# ==========================================

def add_expense(data):
    print("\n--- ADD EXPENSE ---")
    item = input("Enter expense name: ").strip()
    if not item:
        print("[❌] Error: Expense name cannot be empty.")
        return
    
    amount_str = input("Enter amount ($): ").strip()
    if amount_str:
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("[❌] Error: Amount must be greater than zero.")
                return
            data["expenses"].append({"item": item, "amount": amount})
            save_data(data)
            print(f"[✔] Added expense: {item} (${amount:.2f})")
        except ValueError:
            print("[❌] Error: Invalid amount entered.")

def view_expenses(data):
    print("\n--- EXPENSE HISTORY ---")
    if not data["expenses"]:
        print("No expenses recorded yet.")
        return
    
    total = sum(e["amount"] for e in data["expenses"])
    for e in data["expenses"]:
        print(f"• {e['item']}: ${e['amount']:.2f}")
    print(f"\nTotal Spent: ${total:.2f}")

# ==========================================
# MAIN CONTROL LOOP
# ==========================================

def main():
    data = load_data()
    
    while True:
        print("\n=========================")
        print("    STUDENT DASHBOARD    ")
        print("=========================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Add Expense")
        print("5. View Expenses & Total")
        print("6. Exit")
        
        choice = input("\nEnter option (1-6): ").strip()
        
        if choice == "1":
            add_task(data)
        elif choice == "2":
            view_tasks(data)
        elif choice == "3":
            complete_task(data)
        elif choice == "4":
            add_expense(data)
        elif choice == "5":
            view_expenses(data)
        elif choice == "6":
            print("\nGoodbye! Data saved.")
            break
        else:
            print("[❌] Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()