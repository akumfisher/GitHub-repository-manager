# 📁 GitHub Repository Manager

A lightweight command-line tool for managing your GitHub repositories locally. Easily add, list, clone, update, and delete repos — all from your terminal.

---

## ✨ Features

- ✅ **Add repos** — Paste a GitHub URL and it validates it's live before saving
- 📋 **List repos** — View all your saved repositories at a glance
- 📥 **Clone repos** — Clone any saved repo with a single menu selection
- 🔄 **Update repos** — Pull the latest changes into a local folder
- 🗑️ **Delete repos** — Remove repos from your saved list safely

---

## 📋 Requirements

- Python 3.x
- Git (installed and accessible from your terminal)

### Python Dependencies

Install them with:

```bash
pip install colorama requests
```

| Package    | Purpose                          |
|------------|----------------------------------|
| `colorama` | Colored terminal output          |
| `requests` | Validates repo URLs before saving |

---

## 🚀 Installation & Usage

**1. Clone this repository:**

```bash
git clone https://github.com/akumfisher/GitHub-repository-manager.git
cd GitHub-repository-manager
```

**2. Install dependencies:**

```bash
pip install colorama requests
```

**3. Run the tool:**

```bash
python main.py
```

**4. Use the menu:**

```
=== GitHub Repo Manager ===
[1] Add Repo
[2] List Repos
[3] Clone Repo
[4] Update Repo
[5] Delete Repo
[6] Exit
Choose:
```

---

## 🖥️ Demo

```
=== GitHub Repo Manager ===
[1] Add Repo
...
Choose: 1
Repository URL: https://github.com/akumfisher/GitHub-repository-manager
Repository has been saved.

Choose: 2
1. https://github.com/akumfisher/GitHub-repository-manager

Choose: 3
1. https://github.com/akumfisher/GitHub-repository-manager
Repository number: 1
Cloning into 'GitHub-repository-manager'...
```

> **Note:** Saved repositories are stored locally in `repos.json`. This file is created automatically on first use.

---

## 🗺️ Roadmap

Planned features for future releases:

- [ ] **Search & filter** — Search saved repos by name or keyword
- [ ] **GitHub API integration** — Fetch repo stats (stars, forks, last commit) directly in the CLI
- [ ] **Batch clone** — Clone multiple repos at once
- [ ] **Tags / categories** — Organize repos into groups
- [ ] **Config file** — Set a default clone directory
- [ ] **Windows compatibility** — Fix `update_repo` for Windows shells
- [ ] **Interactive TUI** — Replace numbered menus with an arrow-key interface (e.g. using `curses` or `rich`)

---

## 🤝 Contributing

Contributions are welcome! Here's how to get involved:

1. **Fork** this repository
2. **Create a branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes:
   ```bash
   git commit -m "Add: your feature description"
   ```
4. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** and describe what you've changed

### Guidelines

- Keep code simple and readable
- Test your changes before submitting
- One feature or fix per pull request

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

*Made with 🐍 Python*
