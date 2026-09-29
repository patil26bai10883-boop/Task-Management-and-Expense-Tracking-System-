# Project Statement

**Project:** Student Dashboard
**Author:** Vishwajeet
**Language:** Python 3

---

## The problem

Most students I know (myself included) juggle two things at once without any real system for either.

First, there are the tasks: assignments, submissions, things to revise, small errands. They end up scattered across sticky notes, chat messages, and memory, and every so often one slips through.

Second, there's money. Small daily expenses like snacks, printouts, recharges, and stationery add up fast, and by the end of the month it's hard to say where it all went.

Existing apps can solve this, but many are cluttered, need an account, or come with features a student doesn't need. Sometimes you just want something simple that opens fast and does one job.

---

## What I set out to build

A lightweight tool that runs in the terminal and lets a student:

1. Write down tasks and mark them off when they're done
2. Log expenses and see the total spent at any time
3. Come back later and find everything exactly as they left it

I wanted it to be simple enough to use without reading instructions, and simple enough that someone else could open the code and understand it.

---

## Objectives

- Build a working menu-driven program using only Python's standard library
- Store data permanently so nothing is lost when the program closes
- Handle bad input properly instead of crashing (empty text, wrong numbers, invalid menu choices)
- Keep the code organized into small functions, each with one clear job
- Learn how file handling, JSON, loops, and error handling work together in a real program

---

## Scope

**What's included**
- Adding, viewing, and completing tasks
- Adding and viewing expenses, with an automatic total
- Automatic saving to a local JSON file
- Basic recovery if the data file is damaged

**What's not included (yet)**
- Editing or deleting entries
- Dates, categories, or reminders
- Multiple users or any kind of login
- A graphical interface

I kept the scope small on purpose. I'd rather have a small program that works properly than a big one that's half finished.

---

## How it works, briefly

The program loads `data.json` when it starts. If the file doesn't exist, it begins with empty lists. It then shows a menu in a loop until the user chooses to exit. Every time something is added or changed, the data is written back to the file straight away, so there's no risk of losing progress if the program is closed suddenly.

---

## What I learned

- How to read from and write to a JSON file safely
- Why validating user input matters more than it seems. People type strange things
- How breaking a program into small functions makes it much easier to fix and extend
- That a feature that looks tiny (like handling a corrupted file) still takes real thought

---

## Where it could go from here

- Add delete and edit options
- Track dates and show monthly expense summaries
- Add categories for expenses and priorities for tasks
- Let users set a budget and warn them when they're close to it
- Build a simple GUI or turn it into a small web app

---

## Conclusion

Student Dashboard is a small project, but it solves a real everyday problem and gave me hands-on practice with the basics of building a complete program: taking input, storing data, handling mistakes, and keeping the code readable. It's a starting point, and I plan to keep improving it.
