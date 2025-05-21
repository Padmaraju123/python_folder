import unittest
from HtmlTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover("tests")

runner = HTMLTestRunner(
    output='reports',
    report_title='Naukri Automation Report',
    report_name='naukri_test_report'
)

runner.run(suite)