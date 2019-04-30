# PWAF (Python Webdriver Automation Framework)

This is web automation framework, implemented using Python & Webdriver. 
Page Object Model (POM) is used to  make the code more readable, maintainable, and reusable.

## _Prerequisite:_

1. Python
2. pip
3. Selenium/WebDriver
4. nosetests & nose-html-reporting
5. Browsers (Firefox, Chrome, IE)
6. Respective Browser drivers
7. Pycharm

### How to run?

**Test scripts can be executed by nosetests:**

>nosetests -s -v --nologcapture <test-script.py>

>e.g: `nosetests -s -v --nologcapture checkbox_page_test.py`

**Execute different group of test:**

>nosetests -s -v --nologcapture  -a group=<group-name> <test-script.py>

>e.g: `nosetests -s -v --nologcapture group=smoke all_tests.py`

**Execute same group of test:**

>nosetests -s -v --nologcapture -a group=<group-name>

>e.g: `nosetests -s -v --nologcapture -a group=kth`

**Get Test-reports:**

>nosetests -s -v --nologcapture --with-html --html-report=<test-report-file-path> <test-script.py>

>e.g: `nosetests -s -v --nologcapture --with-html --html-report=test_report.html checkbox_page_test.py`

**_Note:_** Kindly set the respective browser's driver path either to System variable or update it in `drivermanager.py`

e.g: self.driver = webdriver.Firefox(executable_path="geckodriver path") # in case of Firefox browser.


***

## _Coverage Plan:_

| Contents                  |                                 | Status |
|---------------------------|---------------------------------|--------|
|                           |                                 |        |
| Framework level           | Page Object Model               | Done   |
|                           | Profiles                        | Done   |
|                           | Grids                           |        |
|                           | Cross browsers & cross platform | Yi-Pei |
|                           |                                 |        |
| Locators                  | Learning how to get locators.   |        |
|                           |                                 |        |
| Functionality To Automate | Challenging DOM                 | Done   |
|                           | Checkboxes                      | Done   |
|                           | Context Menu                    | Fixed  |
|                           | Disappearing Elements           | Done   |
|                           | Drag and Drop                   | Done   |
|                           | Dropdown                        | Done   |
|                           | Dynamic Content                 | Yi-Pei |
|                           | Dynamic Controls                | Done   |
|                           | Dynamic Loading                 | Done   |
|                           | File Download                   | Fixed  |
|                           | File Upload                     | Fixed  |
|                           | Floating Menu                   | Yi-Pei |
|                           | Frames                          | Done   |
|                           | Horizontal Slider               | Kartik |
|                           | Hovers                          | Done   |
|                           | Infinite Scroll                 | Kartik |
|                           | JQuery UI Menus                 | Yi-Pei |
|                           | JavaScript Alerts               | Kartik |
|                           | Key Presses                     | Yi-Pei |
|                           | Large & Deep DOM                | Yi-Pei |
|                           | Multiple Windows                | Done   |
|                           | Nested Frames                   | Done   |
|                           | Notification Messages           | Kartik |
|                           | Redirect Link                   | Yi-Pei |
|                           | Shifting Content                | Kartik |
