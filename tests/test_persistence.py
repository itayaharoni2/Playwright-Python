import re
from playwright.sync_api import Page, expect
from pages.todos_page import TodosPage

def test_todos_persist_after_reload(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Persistent task 1")
    todos.add_todo("Persistent and completed task 2")
    todos.mark_todo_completed(1) # Mark the second task as completed

    page.reload()

    # Confirm both tasks are still visible
    expect(todos.todo_items.nth(0)).to_have_text("Persistent task 1")
    expect(todos.todo_items.nth(1)).to_have_text("Persistent and completed task 2")


    # Check that second item is still marked completed
    completed_item = todos.todo_items.nth(1)
    expect(completed_item).to_have_class(re.compile(".*completed.*"))

def test_items_left_count_persists(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Task 1")
    todos.add_todo("Task 2")
    todos.mark_todo_completed(0)

    expect(todos.items_left).to_have_text("1 item left")

    page.reload()

    # Count should still be 1
    expect(todos.items_left).to_have_text("1 item left")
