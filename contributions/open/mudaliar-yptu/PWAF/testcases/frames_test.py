"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 05-June-18
"""
from pages.frames_page import FramesPage
from pages.multiple_window_page import MultipleWindowsPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class FramesTest(DriverManager):
    def test_frames(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Frames")

        frames = FramesPage(self.driver)
        frames.verify_multiple_windows_page()
        frames.click_on_link("Nested Frames")
        frames.verify_next_frame_txt()
