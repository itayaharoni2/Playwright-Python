from playwright.sync_api import Page
from pages.todos_page import TodosPage
# what to do with the asserts?

def test_mark_all_items_as_completed(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Do the Dished") 
    todos.add_todo("Mop the floor")
    todos.add_todo("Cook Pasta")

    todos.mark_all_completed() 

    for i in range(3): 
        item = todos.todo_items.nth(i)
        assert "completed" in item.get_attribute("class")

def test_clear_completed_removes_completed_items(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Wash the Dishes")
    todos.add_todo("Make cocktails")
    todos.mark_todo_completed(0) # Marks the first one

    todos.clear_completed()

    texts = todos.get_todo_texts()
    assert "Wash the Dishes" not in texts # The first one should be removed
    assert "Make cocktails" in texts 
    assert len(texts) == 1 # Only one item should be left
