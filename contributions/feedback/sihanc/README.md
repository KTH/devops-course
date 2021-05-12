# Feedback submission on tutorial #1352

- Submitted executable tutorial [#1352](https://github.com/KTH/devops-course/pull/1352)
- Tutorial proposal [#1230](https://github.com/KTH/devops-course/pull/1230)
- Feedback proposal [#1256](https://github.com/KTH/devops-course/pull/1256)

 ## Member
 Sihan Chen (sihanc@kth.se)
 Github: [Spycsh](https://github.com/Spycsh)
 

 
# Feedback

## Overall feedback

Hi guys!

As a whole, the tutorial is easy for me to follow and the GitHub Action also works fluently on my repositories with the steps listed in the tutorial. As we all know, automation testing with a well-known CI/CD tool such as GitHub Action, Jenkins or Teamcity is a hot topic in recent years and it deserves such tutorials and documents, especially in such hands-on format on web-based websites or open-source repositories. This tutorial focuses on binding python unittest with GitHub Action in building a CI workflow. The steps are clearly explained and results are correctly shown. I especially like the part when you examine in detail in Step 3 the configuration of a YAML file of the GitHub Actions, where the keywords are exhaustively explained, which can surely help readers not only know that that part of code can be used to build up automation python unittest workflow, but also learn to adapt the configuration in YAML file to their own demands as well. Generally, I would say this is a meaningful tutorial to me.

Now below I will give you some reviews and improvements maybe you can think of corresponding to the steps in the tutorial. Please notice that all ideas or suggestions are from my point of view so you can just take some as you need. :)

### Step 1
The architecture of a project is clearly shown, and in the demo example, the `review()` function in `/src/app.py` is tested with the `test_app.py` in `/test/` folder. The function is well written to check whether the number of one year is of type `int` and less than current year 2021. Also many special years are checked and the other years checks return random elements in the default array. Meanwhile, the tests are well written to cover all the scenarios yielded by the function. Three kinds of assertions are used for different purposes. 

When it comes to grammar, I would recommend three small changes:

* replace "This file can sure look..." with "This file can surely look..."

* add a comma after "First and foremost"

* add another comma between "when we review a specific year" and "we get the correct string output returned to us".

I think another point can be improved is the explanation of the usage of sub tests. As you said, "If one of these assertions would fail, unittest wouldn’t tell us which of them failed. Instead, it would only tell us in what test function the error occurred.". This line is pretty hard for me to read at first glance. Afterwards I realize that many **assertions** are contained in one **test function**. My understanding of the reason to use sub tests is that: assuming when originally without sub tests, if one assertion fails, the program will not continue checking the following assertions in one test function, which means only one failed assertion is shown even if there are many failed assertions. However, with sub tests, the failure of one assertion will not affect the check of its followings. Instead, all failure assertions will be shown at one time. Another advantage to use sub tests is that each assertion can add a message which carries extra error information for testers to diagnose. I think it would be more obvious for readers in this part if you explain a bit more about these two advantages of sub tests.


### Step 2
For grammar, I would suggest to replace "ran" in "If everything ran successfully" to "runs".

### Step 3
I would suggest that you should mention the values of `branches` keyword should be `master` and also `main` as suggested in [https://github.com/github/renaming](https://github.com/github/renaming), because there may not be a master branch in a new repository that readers create so if you write like following it should be compatible to different scenarios:

```yml
branches: [ master, main ]
```

The whole introduction of writing a YAML file for GitHub Action is very clear, including cloning the repo, installing python with assigned version, installing dependencies, lint checking with flake8 and test running. Everything is fine when I test on my own repo.

### Step 4
I would suggest you mention that after readers push all the files you have written, they should then swithch to "Actions" tab and click the button "I understand my workflows, go ahead and enable them". Only after enabling it can the workflow be triggered with a push or pull request.

## Further improvements

Personally, I have contributed to a project regarding python unittest and maybe you have interest in that project [HTMLTestRunner](https://github.com/SeldomQA/HTMLTestRunner). A normal problem that testers may encounter is to visualize the results of python unittest because they have to give reports to the team. That `HTMLTestRunner` can help us to generate HTML reports based on the result of python unittest. Since you have successfully bind the GitHub Action and python unittest, I write a demo [https://github.com/Spycsh/devops-tutorial](https://github.com/Spycsh/devops-tutorial) based on your work. The demo will automatically do the lint checks, and then do the unit tests, and then generate elegant HTML report and push to the demo repository. I will briefly explain the changes that I have made in my demo, Have fun if you have interest :)

Firstly, I add the `TestRunner` folder and the files under that folder. This folder contains the HTML templates and it can execute the unit test suite and render the results to the templates and finally generate the `result.html` under the root. 

Secondly, I add the `setup.py` which set up with the needed packages.

Thirdly, in `test_app.py` I add following code to add test to a test suite and run the `HTMLTestRunner` class to generate HTML report:

```python
from TestRunner import HTMLTestRunner
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestApp("test_review_should_return_default"))
    suit.addTest(TestApp("test_review_should_not_return_default"))
    suit.addTest(TestApp("test_review_invalid_type_raise"))
    suit.addTest(TestApp("test_review_future_year_raise"))

    with(open('result.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<project name>test report',
            description='describe: ... '
        )
        runner.run(suit)
```

In the end, in `ci.yml`, I modify the original `python -m unittest` to

```yml
- name: Test
      run: |
        python setup.py install
        python test/test_app.py
        git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"
        git config --local user.name "github-actions[bot]"
        git commit -m "Add changes" -a
    - name: Push changes
      uses: ad-m/github-push-action@master
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        branch: ${{ github.ref }}
```

That will run the `setup.py` and then run the tests, and then generate the HTML reports and push the report to the repository. You can view the `result.html` under the root directory of the repository to see the report of your python unittest results of your `test_app.py`.

You can also clone the project to your local machine to see how it works. Just execute following code:

```bash
git clone https://github.com/Spycsh/devops-tutorial.git
cd devops-tutorial
python test/test_app.py
```

Then open `result.html` to check the results.



## Conclusion
Above is all my feedback content. Welcome any ideas comments and if you have any suggestions, please do not hesitate to leave you comments below or contact [sihanc@kth.se](sihanc@kth.se). Thank you:)

