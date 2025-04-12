from playwright.sync_api import Page
from pages.todos_page import TodosPage

def test_prevent_adding_empty_todo(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("")  # Try to add an empty todo
    assert len(todos.get_todo_texts()) == 0  # Should not add anything

def test_add_long_todo_text(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    long_text = "A" * 500 # Long string of 500 characters
    todos.add_todo(long_text) 

    assert long_text in todos.get_todo_texts() # Should be added

def test_add_whitespace_only(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("     ")  # Just spaces
    assert len(todos.get_todo_texts()) == 0 # Should not add anything
