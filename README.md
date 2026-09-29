# Student Dashboard

A small command-line app I built in Python to keep track of two things every student deals with: **things to do** and **money spent**.

No fancy setup, no extra libraries. You run one file, pick an option from a menu, and your stuff gets saved so it's still there the next time you open it.

---

## Why I made this

I kept losing track of my tasks in random notes and had no idea where my pocket money was going. Instead of downloading yet another app, I figured I'd write my own. It also turned out to be a good way to practice working with files, functions, and user input in Python.

---

## What it can do

**Tasks**
- Add a new task
- See all your tasks, with a clear Done / Pending status
- Mark a task as complete using its ID

**Expenses**
- Add an expense with a name and an amount
- See every expense you've logged, plus the total at the bottom

**Other stuff**
- Everything is saved automatically in a `data.json` file
- If the file gets corrupted, the app doesn't crash. It warns you and starts fresh
- Empty inputs, negative amounts, and typing letters where numbers should go are all handled with a friendly error message

---

## What you need

- Python 3.6 or newer
- That's it. It only uses `json` and `os`, which come with Python

---

## How to run it

1. Download or clone the project
2. Open a terminal in the project folder
3. Run:

```bash
python main.py
```

(On some systems you might need `python3 main.py` instead.)

The first time you run it, a `data.json` file gets created for you as soon as you add something.

---

## How it looks

```
=========================
    STUDENT DASHBOARD
=========================
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Add Expense
5. View Expenses & Total
6. Exit

Enter option (1-6):
```

Type a number, press Enter, and follow the prompts.

---

## How the data is stored

Everything lives in one JSON file, `data.json`, which looks something like this:

```json
{
    "tasks": [
        { "id": 1, "title": "Finish physics assignment", "done": false }
    ],
    "expenses": [
        { "item": "Notebook", "amount": 45.0 }
    ]
}
```

You can open it in any text editor if you're curious. If you ever want a clean slate, just delete the file.

---

## Project structure

```
.
├── main.py       # the whole app
├── data.json     # created automatically when you save something
├── README.md
└── statement.md  # the problem statement behind this project
```

Inside `main.py` the code is split into three parts to keep it readable:

1. **File handling** – `load_data()` and `save_data()`
2. **Task module** – `add_task()`, `view_tasks()`, `complete_task()`
3. **Expense module** – `add_expense()`, `view_expenses()`
4. **Main loop** – the menu that ties it all together

---

## Things I know could be better

I'd rather be upfront about the limits of this version:

- You can't delete or edit tasks and expenses yet
- Expenses don't have dates or categories
- The currency symbol is hardcoded as `$`
- Task IDs are based on how many tasks exist, so if delete gets added later, IDs will need a smarter system

## Ideas for next time

- Delete and edit options
- Dates on expenses and a monthly summary
- Categories (food, travel, books, etc.)
- Due dates and priorities for tasks
- Maybe a simple GUI down the line

---

## Author

Made by **Vishwajeet**, as a student project.

Feel free to use it, tweak it, or break it and fix it. That's how I learned most of this anyway.
