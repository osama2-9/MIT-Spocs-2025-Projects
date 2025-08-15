# ⏰ Task Manager with Reminders (Tkinter + Notifications)

A Python desktop application for managing tasks with **time-based reminders**.  
Supports custom **video** and **audio** alerts, search, edit, and delete features.  
Built with **Tkinter**, **Plyer**, and **Pygame**.

---

## 📌 Features
- 📝 **Add, Edit, Delete Tasks** — Manage your to-do list easily.
- 🔍 **Search** — Filter tasks instantly by title or time.
- ⏰ **Reminders** — Notifications appear 5 minutes before a task.
- 🎵 **Custom Audio Alerts** — Play your own `.mp3` file when a task is near.
- 🎥 **Custom Video Alerts** — Automatically open an `.mp4` file at reminder time.
- 💾 **Persistent Storage** — Tasks are saved in `tasks.json` so they remain after closing the app.
- 🖥 **User-Friendly Interface** — Simple Tkinter GUI with color-coded buttons.

---

## ⚙️ Requirements
- Python **3.6+**
- **Tkinter** (built into Python)
- **Plyer** (for desktop notifications)
- **Pygame** (for playing sounds)

Install dependencies:
```bash
pip install plyer pygame
