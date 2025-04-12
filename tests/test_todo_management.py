import re
from playwright.sync_api import Page, expect
from pages.todos_page import TodosPage

def test_create_todo(page: Page, base_url: str):
    todos_page = TodosPage(page)
    todos_page.navigate(base_url)

    todos_page.add_todo("Task 1")
    expect(todos_page.todo_items).to_have_count(1)
    expect(todos_page.todo_items).to_have_text("Task 1")
    expect(todos_page.items_left).to_have_text("1 item left")

def test_edit_todo(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Edit me")
    todos.edit_todo(0, "Edited task")
    expect(todos.todo_items.nth(0)).to_have_text("Edited task")

def test_mark_todo_completed(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Complete me")
    todos.mark_todo_completed(0)

    todo_item = todos.todo_items.nth(0)
    expect(todo_item).to_have_class(re.compile(".*completed.*"))

def test_mark_todo_incomplete(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Uncheck me")
    todos.mark_todo_completed(0)
    todos.mark_todo_incomplete(0)

    todo_item = todos.todo_items.nth(0)
    expect(todo_item).not_to_have_class(re.compile(".*completed.*"))

def test_delete_todo(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Delete me")
    todos.delete_todo(0)

    expect(todos.todo_items).to_have_count(0)

def test_items_left_counter(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Task 1")
    todos.add_todo("Task 2")
    todos.mark_todo_completed(0)

    expect(todos.items_left).to_have_text("1 item left")
