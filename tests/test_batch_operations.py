from playwright.sync_api import Page, expect
from pages.todos_page import TodosPage

def test_mark_all_items_as_completed(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Do the Dishes") 
    todos.add_todo("Mop the floor")
    todos.add_todo("Cook Pasta")

    todos.mark_all_completed() 

    for i in range(3): 
        item = todos.todo_items.nth(i)
        expect(item).to_have_class(lambda value: "completed" in value) # Check if every item has the completed class

def test_clear_completed_removes_completed_items(page: Page, base_url: str):
    todos = TodosPage(page)
    todos.navigate(base_url)

    todos.add_todo("Wash the Dishes")
    todos.add_todo("Make cocktails")
    todos.mark_todo_completed(0)

    todos.clear_completed()

    texts = todos.get_todo_texts()
    expect(texts).not_to_contain("Wash the Dishes") # Check if the completed item is removed
    expect(texts).to_contain("Make cocktails") # Check if the incomplete item is still there
    expect(len(texts)).to_equal(1) # Only one item should remain