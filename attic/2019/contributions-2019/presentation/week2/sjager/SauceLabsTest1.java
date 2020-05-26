import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.Test;
import org.testng.Assert;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
 
public class InstantSauceTestNGTest1 {
    private WebDriver driver;
 
    @Test
    public void shouldOpenSafari() throws MalformedURLException {
 
        /**
         * In this section, we will configure our SauceLabs credentials in order to run our tests on saucelabs.com
         */
        String sauceUserName = "";
        String sauceAccessKey = "";
 
        /**
         * In this section, we will configure our test to run a specific
         * browser/os combination in Sauce Labs
         */
 
        DesiredCapabilities capabilities = new DesiredCapabilities();
 
        capabilities.setCapability("username", sauceUserName);
        capabilities.setCapability("accessKey", sauceAccessKey);
 
        capabilities.setCapability("browserName", "Safari");
        capabilities.setCapability("platform", "macOS 10.13");
        capabilities.setCapability("version", "11.1");

        capabilities.setCapability("build", "TestApp1");
        capabilities.setCapability("name", "Test1");
    
        driver = new RemoteWebDriver(new URL("http://ondemand.saucelabs.com:80/wd/hub"), capabilities);
 
        driver.navigate().to("https://www.kth.se/");
 
        WebDriverWait wait = new WebDriverWait(driver, 5);
 
        // //wait for the user name field to be visible and store that element into a variable
        // By userNameFieldLocator = By.cssSelector("[type='text']");
        // wait.until(ExpectedConditions.visibilityOfElementLocated(userNameFieldLocator));
 
        // //type the user name string into the user name field
        // driver.findElement(userNameFieldLocator).sendKeys("standard_user");
 
        // //type the password into the password field
        // driver.findElement(By.cssSelector("[type='password']")).sendKeys("secret_sauce");
 
        // //hit Login button
        // driver.findElement(By.cssSelector("[type='submit']")).click();
 
        // //Synchronize on the next page and make sure it loads
        // By inventoryPageLocator = By.id("inventory_container");
        // wait.until(ExpectedConditions.visibilityOfElementLocated(inventoryPageLocator));
 
        // /**
        //  * In this section, we confirm the test ran correctly, howerver we don't post the results to saucelabs.com
        //  */
        // //Assert that the inventory page displayed appropriately
        // Assert.assertTrue(driver.findElement(inventoryPageLocator).isDisplayed());
 
        //Here we tear down the WebDriver session
        driver.quit();
    }
}