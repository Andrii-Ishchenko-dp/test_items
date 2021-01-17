link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_coders_at_work(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button=browser.find_element_by_css_selector('#add_to_basket_form')
    button.click()
    assert\
         f"Товар не добавлен в корзину"

