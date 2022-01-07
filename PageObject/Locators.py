class HomePageLocators (object):
    input_box = "number"
    calculate_btn = "getFactorial"
    terms_link = "body > div.col-md-12 > div > p:nth-child(1) > a:nth-child(1)"
    privacy_link = "body > div.col-md-12 > div > p:nth-child(1) > a:nth-child(2)"
    result_text = "//*[@id='resultDiv' and contains(text(),'The factorial of')]"
