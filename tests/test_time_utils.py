#
# Author: Rohtash Lakra
#
from src.rslakra.utils import TimeUtils
from tests.base import AbstractTestCase


class TestTimeUtils(AbstractTestCase):
    """Test TimeUtils Class"""
    
    def setUp(self):
        pass
    
    def test_now_utc(self):
        now_utc = TimeUtils.now_utc()
        print(f"now_utc: {now_utc}")
        assert now_utc is not None
    
    def test_now_utc_str(self):
        now_utc_str = TimeUtils.now_utc_str()
        print(f"now_utc_str: {now_utc_str}")
        assert now_utc_str is not None
    
    def test_now_utc_ms(self):
        now_utc_ms = TimeUtils.now_utc_ms()
        print(f"now_utc_ms: {now_utc_ms}")
        assert now_utc_ms is not None
    
    def test_unixTimestamp(self):
        unixTimestamp = TimeUtils.unixTimestamp()
        print(f"unixTimestamp: {unixTimestamp}")
        assert unixTimestamp is not None
    
    def test_timeMillis(self):
        timeMillis = TimeUtils.timeMillis()
        print(f"timeMillis: {timeMillis}")
        assert timeMillis is not None
    
    def test_getUtcTime(self):
        utcTime = TimeUtils.getUtcTime()
        print(f"utcTime: {utcTime}")
        assert utcTime is not None
