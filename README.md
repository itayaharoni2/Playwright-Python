# Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/itayaharoni2/Playwright-Python
cd Playwright-Python
```

2. Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

- If you also want to generate HTML test reports, install:

```bash
pip install pytest-html
```

-----------

# Commands to Run the Tests

- Run all the tests (defaults to Chromium):

```bash
pytest
```

- Run tests with a specific browser (chromium, firefox, or webkit):

```bash
pytest --browser=firefox
```

- Run the tests and gives more detailed results:

```bash
pytest -v
```

- Run the tests with visual browser - slowed down so its possible to follow (you can control the speed if you change the '500' to another number):

```bash
pytest --headed --slowmo=500
```

- Run a specific test file (just change the file name to the file you want to run):

```bash
pytest tests/test_todo_management.py
```

---

Optional: Generate an HTML report

To get a full test report in your browser:

```bash
pytest --html=report.html --self-contained-html
```

Then open `report.html` to see a styled report with pass/fail status.

---

Tip: If you want to run tests in other browsers (like Firefox or WebKit), make sure they are installed:

```bash
playwright install
pytest --browser=firefox
```
---

# Test Organization Approach

- Tests are divided by the categories in the instructions:

  - `test_todo_management.py` – core create/edit/delete functionality
  - `test_filtering.py` – filter options (All, Active, Completed)
  - `test_batch_operations.py` – mark all as complete, clear completed
  - `test_persistence.py` – data persistence after page reload
  - `test_edge_cases.py` – edge case handling like long text, empty input, and whitespace-only todos
  - `test_visual_testing.py` – takes a UI screenshot for basic visual comparison (optional)

- The `pages/todos_page.py` file follows the Page Object to encapsulate all element selectors and actions, keeping test logic clean, reusable, and separated from UI structure.

- `conftest.py` can be used for creating reusable logic across multiple tests, currently printing an ASCII message at the end of the test run.

- `pytest.ini` sets a base URL, enables HTML test reports, and restricts test discovery to the tests/ folder..

- `requirements.txt` contains all necessary Python packages to run the test suite, including:
  - `playwright` – browser automation engine
  - `pytest` – test runner
  - `pytest-playwright` – integration of Playwright with pytest

----------

# Challenges and Solutions

- I initially learned Playwright through YouTube videos and began writing tests right away. However, after reviewing the official Playwright API documentation, I realized there were better practices — such as using `get_by_text()` instead of raw locators, and `expect()` instead of Python's native `assert`. This led me to refactor much of my early code for better reliability and readability.

- Since I was working with Python, the built-in test recording feature in VSCode didn’t work. Instead, I used the `playwright codegen` command directly from the terminal. Although the recorder was confusing at first, once I understood how it worked, it became a very helpful tool for generating test code quickly.

- Test flakiness: Solved by relying on Playwright’s `expect()` assertions, which include automatic waiting for element states and prevent race conditions.
