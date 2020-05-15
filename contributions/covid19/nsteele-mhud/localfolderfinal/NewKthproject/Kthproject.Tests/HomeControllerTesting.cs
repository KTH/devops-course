using Kthproject.Controllers;
using System;
using Xunit;

namespace Kthproject.Tests
{
    public class HomeControllerTesting
    {
        [Fact]
        public void TestingViewWhenIndexCalled()
        {
            var controller = new HomeController();
            var index = controller.Index();
            Assert.NotNull(index);
        }
    }
}
