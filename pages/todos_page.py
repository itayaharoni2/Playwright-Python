from playwright.sync_api import Page

class TodosPage:
    def __init__(self, page: Page):
        # is it good practice with plkaceholder? and with get by_role?
        self.page = page
        self.todo_input = page.get_by_placeholder("What needs to be done?")
        self.todo_items = page.locator("ul.todo-list li")
        self.clear_completed_button = page.get_by_role("button", name="Clear completed")
        self.toggle_all = page.locator("label[for='toggle-all']")
        self.filter_all = page.get_by_role("link", name="All")
        self.filter_active = page.get_by_role("link", name="Active")
        self.filter_completed = page.get_by_role("link", name="Completed")
        self.items_left = page.locator("span.todo-count")

    def navigate(self, url: str = "https://demo.playwright.dev/todomvc/"):
        self.page.goto(url)

    def add_todo(self, text: str):
        self.todo_input.fill(text)
        self.todo_input.press("Enter")

    def get_todo_texts(self):
        return self.todo_items.all_text_contents()

    def edit_todo(self, index: int, new_text: str):
        item = self.todo_items.nth(index)
        item.dblclick()
        edit_input = item.locator("input.edit")
        edit_input.fill(new_text)
        edit_input.press("Enter")

    def mark_todo_completed(self, index: int):
        checkbox = self.todo_items.nth(index).locator("input.toggle")
        checkbox.check()

    def mark_todo_incomplete(self, index: int):
        checkbox = self.todo_items.nth(index).locator("input.toggle")
        checkbox.uncheck()

    def delete_todo(self, index: int):
        item = self.todo_items.nth(index)
        item.hover()
        destroy_button = item.locator("button.destroy")
        destroy_button.click()

    def get_items_left_count(self) -> int:
        count_text = self.items_left.text_content()
        return int(count_text.split()[0]) if count_text else 0

    def filter_by_all(self):
        self.filter_all.click()

    def filter_by_active(self):
        self.filter_active.click()

    def filter_by_completed(self):
        self.filter_completed.click()

    def mark_all_completed(self):
        self.toggle_all.click()

    def clear_completed(self):
        if self.clear_completed_button.is_visible():
            self.clear_completed_button.click()
