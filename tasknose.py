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
    if t.startswith("2016-06-12 22:") is True:
        result = True
    assert result


class TestTask():

    def setup(self):
        print("TestTask():setup() before each test method")


    def teardown(self):
        print ("TestTask():teardown() after each test method")

    @classmethod
    def setup_class(cls):
        print ("setup_class() before any methods in this class")

    @classmethod
    def teardown_calss(cls):
        print ("teardown_class() after any methods in this class")

    def test_datetime_format(self):
        now = datetime.now()
        t = now.strftime("%Y-%m-%d %H:%M:%S")
        assert len(t) == 19

    def test_datetime_content(self):
        now = datetime.now()
        t = now.strftime("%Y-%m-%d %H:%M:%S")
        result = False
        if t.startswith("2016-06-12 22:") is True:
            result = True
        assert result
