from datetime import datetime
from nose import with_setup


def setup_module():
    print "setup_module."


def teardown_module():
    print "teardown_module."


def my_setup_func():
    print "my_setup_func."


def my_teardown_func():
    print "my_teardown_func."


@with_setup(my_setup_func, my_teardown_func)
def test_datetime_format():
    now = datetime.now()
    t = now.strftime("%Y-%m-%d %H:%M:%S")
    assert len(t) == 19


@with_setup(my_setup_func, my_teardown_func)
def test_datetime_content():
    now = datetime.now()
    t = now.strftime("%Y-%m-%d %H:%M:%S")
    result = False
    if t.startswith("2016-06-12 19:") is True:
        result = True
    assert result
