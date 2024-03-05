import time


def highlight(element, effect_time):
    driver1 = element._parent

    def apply_style(s):
        driver1.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(10, "blue"))
    time.sleep(effect_time)
    apply_style(original_style)
