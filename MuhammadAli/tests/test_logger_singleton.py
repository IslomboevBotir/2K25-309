def test_logger_is_singleton():
    from smartcity.logger import Logger
    assert Logger() is Logger()