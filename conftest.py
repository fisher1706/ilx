import pytest
from glbl import Log


pytest_plugins = [
    "src.fixtures.ilx_context_fixtures",
    "src.fixtures.ilx_high_level_contexts",
]


def pytest_addoption(parser):
    # main args
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: 'chrome', 'chrome-headless' or 'firefox'")
    parser.addoption('--environment', action='store', default='qa',
                     help="Choose environment: 'dev', 'qa', 'staging', 'prod'")
    parser.addoption('--credentials', action='store', nargs='?', const=True, default=False,
                     help="If selected, credentials will be retrieved ONLY from the command line")
    parser.addoption('--screenshot', action='store', nargs='?', const=True, default=False,
                     help="If selected, screenshot will be created when error occurs")

    # testrail
    parser.addoption('--testrail_email', action='store', default=None,
                     help="Enter email of testrail account")
    parser.addoption('--testrail_password', action='store', default=None,
                     help="Enter password of testrail account")

    # ilx
    parser.addoption('--ilx_environment', action='store', default='qa',
                     help="Choose environment: 'dev', 'qa', 'prod'")
    parser.addoption('--ilx_credentials', action='store', nargs='?', const=True, default=False,
                     help="If selected, credentials will be retrieved ONLY from the command line")

    parser.addoption('--ilx_erp_token', action='store', default=None,
                     help="Enter ilx_erp_token")

    parser.addoption('--edi_856_auth_token', action='store', default=None,
                     help="Enter edi_856_auth_token")
    parser.addoption('--user_name_edi_856', action='store', default=None,
                     help="Enter user_name_edi_856")
    parser.addoption('--password_edi_856', action='store', default=None,
                     help="Enter password_edi_856")

    parser.addoption('--ilx_infor_token', action='store', default='qa',
                     help="Enter ilx_infor_token")

    parser.addoption('--ilx_qa_token', action='store', default='qa',
                     help="Enter ilx_qa_token")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


def pytest_exception_interact(report):
    Log.error(f'Exception:\n{report.longreprtext}')
