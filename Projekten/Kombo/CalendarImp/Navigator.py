import time
def insert(page, info, text):
    page.fill(f"input[{info}]", "")
    page.type(f"input[{info}]", text)
    time.sleep(0.25)
    page.press(f"input[{info}]", "Enter")

def insert_and_choose_in_list(page, info, text, list_info, extraYearValue):
    page.fill(f"input[{info}]", "")
    page.type(f"input[{info}]", str(text))
    if len(str(text)) == 1:
        text = f"0{text}"
    page.click(f"li[data-value='{2024+extraYearValue}{str(text)}']")

