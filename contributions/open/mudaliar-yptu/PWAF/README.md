# Simple Selenium framework for Python 

Based on Anuj Kumar's work - "PWAF", we want to continue his work to complete the rest work to make the open source become more concrete and sound.

Thus, this open project could benefit web developers/QA engineers with their projects.

This is web automation framework, implemented using Python & Webdriver. 
Page Object Model (POM) is used to  make the code more readable, maintainable, and reusable.

## _Prerequisite:_

1. Python2.7
2. Run to install virtual env: **python -m pip install --user virtualenv**
3. Run to create virtual env: **python -m virtualenv env**
4. Run to activate virtual env: **source env/bin/activate**
5. Run to install dependent packages: **pip install** -r **requirements**.**txt**
6. Selenium/WebDriver
7. nosetests & nose-html-reporting
8. Browsers (Firefox, Chrome, IE)
9. Respective Browser drivers
10. Pycharm

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
| ------------------------- | ------------------------------- | ------ |
|                           |                                 |        |
| Framework level           | Page Object Model               | Done   |
|                           | Profiles                        | Done   |
|                           | Cross browsers & cross platform | Done   |
|                           |                                 |        |
| Locators                  | Learning how to get locators.   | Done   |
|                           |                                 |        |
| Functionality To Automate | Challenging DOM                 | Done   |
|                           | Checkboxes                      | Done   |
|                           | Context Menu                    | Done   |
|                           | Disappearing Elements           | Done   |
|                           | Drag and Drop                   | Done   |
|                           | Dropdown                        | Done   |
|                           | Dynamic Content                 | Done   |
|                           | Dynamic Controls                | Done   |
|                           | Dynamic Loading                 | Done   |
|                           | File Download                   | Done   |
|                           | File Upload                     | Done   |
|                           | Floating Menu                   | Done   |
|                           | Frames                          | Done   |
|                           | Horizontal Slider               | Done   |
|                           | Hovers                          | Done   |
|                           | Infinite Scroll                 | Done   |
|                           | JQuery UI Menus                 | Done   |
|                           | JavaScript Alerts               | Done   |
|                           | Key Presses                     | Done   |
|                           | Large & Deep DOM                | Done   |
|                           | Multiple Windows                | Done   |
|                           | Nested Frames                   | Done   |
|                           | Notification Messages           | Done   |
|                           | Redirect Link                   | Done   |
|                           | Shifting Content                | Done   |

## Contributors:
	- Kartik Kandavel Mudaliar(mudaliar@kth.se)
	- Yi-Pei Tu(yptu@kth.se)