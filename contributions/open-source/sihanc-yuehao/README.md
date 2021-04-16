# open-source: Bug fixing for the open-source project HTMLTestRunner



## Members

Sihan Chen: Email: sihanc@kth.se Github: [Spycsh](https://github.com/Spycsh)

Yuehao Sui: Email:  yuehao@kth.se Github: [amaothree](https://github.com/amaothree)

## Proposal

The open source project [HTMLTestRunner](https://github.com/SeldomQA/HTMLTestRunner) is used widely as a way to automatically generate elegant HTML testing report for Python unittest and send to mailboxes. It is used in several open-source projects such as [Seldom](https://pypi.org/project/seldom/).

Our contribution is aimed to address the following bugs:
1. expand the email support on email sending service with the functions in python smtplib (let it support Gmail, QQ, and 126, 163 mail etc.)
2. fix the bugs when scaling down web browser, the testing chart will overlap with the testing results by using responsive design
3. fix some typos and wrong references
