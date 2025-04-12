from playwright.sync_api import Page, expect
from pages.todos_page import TodosPage

def test_filter_all_shows_all_items(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Task 1")
    todos.add_todo("Task 2")
    todos.mark_todo_completed(1)

    todos.filter_by_all()

    expect(todos.todo_items.nth(0)).to_have_text("Task 1")
    expect(todos.todo_items.nth(1)).to_have_text("Task 2")

def test_filter_active_shows_only_incomplete(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Incomplete Task")
    todos.add_todo("Completed Task")
    todos.mark_todo_completed(1) # Mark the second task as completed

    todos.filter_by_active()

    expect(todos.todo_items).to_have_count(1) # Only one item should be visible
    expect(todos.todo_items.nth(0)).to_have_text("Incomplete Task") # The Incomplete task should be visible

def test_filter_completed_shows_only_completed(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Incomplete Task")
    todos.add_todo("Completed Task")
    todos.mark_todo_completed(1) # Mark the second task as completed

    todos.filter_by_completed()

    expect(todos.todo_items).to_have_count(1) # Only one item should be visible
    expect(todos.todo_items.nth(0)).to_have_text("Completed Task") # The Completed task should be visible
