#
# Author: Rohtash Lakra
#
import time
from datetime import datetime, timezone


class TimeUtils:
    
    @classmethod
    def now_utc(cls):
        """Returns the current UTC datetime."""
        return datetime.now(timezone.utc)
    
    @classmethod
    def now_utc_str(cls, pattern: str = "%Y-%m-%d %H:%M:%S") -> str:
        """Returns the current UTC datetime string."""
        return cls.now_utc().strftime(pattern)
    
    @classmethod
    def now_utc_ms(cls, pattern: str = "%Y-%m-%d %H:%M:%S.%f") -> str:
        """Returns the current UTC datetime string."""
        return cls.now_utc().strftime(pattern)
    
    @classmethod
    def date(cls) -> str:
        """Returns the current UTC datetime string."""
        return cls.now_utc().strftime("%Y-%m-%d")
    
    @classmethod
    def time(cls) -> str:
        """Returns the current UTC datetime string."""
        return cls.now_utc().strftime("%H:%M:%S")
    
    @classmethod
    def unixTimestamp(cls) -> int:
        """Returns the Unix timestamp (seconds since epoch) from the datetime object."""
        return cls.now_utc().timestamp()
    
    @classmethod
    def timeMillis(cls) -> int:
        """Returns the Unix timestamp (seconds since epoch)."""
        return int(cls.now_utc().timestamp() * 1000)
    
    @classmethod
    def getUtcTime(cls) -> int:
        """Returns the Unix timestamp (seconds since epoch)."""
        return int(time.time() * 1000)
