from splinter import Browser
from pyvirtualdisplay import Display

display = Display(visible=0)
display.start()

browser = Browser()
browser.visit('http://google.com')
browser.fill('q', 'splinter - python acceptance testing for web applications')
browser.find_by_name('btnG').click()

if browser.is_text_present('splinter.cobrateam.info'):
    print "Yes, the official website was found!"
else:
    print "No, it wasn't found... We need to improve our SEO techniques"

browser.quit()
