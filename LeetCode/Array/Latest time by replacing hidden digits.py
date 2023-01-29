class Solution:
    def maximumTime(self, time: str) -> str:
        _time = list(time)

        if _time[0] == "?":
            if _time[1] == "?" or int(_time[1]) < 4:
                _time[0] = "2"
            else:
                _time[0] = "1"
        
        if _time[1] == "?":
            if _time[0] == "2":
                _time[1] = "3"
            else:
                _time[1] = "9"
        if _time[3] == "?":
            _time[3] = "5"
        
        if _time[4] == "?":
            _time[4] = "9"

        return "".join(_time)
