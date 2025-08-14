from datetime import datetime, timedelta

DAILY_THRESHOLD = 8.6  # hours
OT1_LIMIT = 2  # hours at 125%
OT1_RATE = 1.25
OT2_RATE = 1.5


def compute_daily(in_ts: datetime, out_ts: datetime, breaks: timedelta = timedelta(), threshold: float = DAILY_THRESHOLD):
    """Compute daily normal and overtime hours according to Israeli law.

    Args:
        in_ts (datetime): clock-in timestamp
        out_ts (datetime): clock-out timestamp
        breaks (timedelta): total break time
        threshold (float): daily regular hours threshold (default 8.6)

    Returns:
        dict: normal hours, overtime1 (125%), overtime2 (150%)
    """
    net_hours = (out_ts - in_ts - breaks).total_seconds() / 3600.0
    if net_hours < 0:
        net_hours = 0
    normal = min(net_hours, threshold)
    overtime1 = min(max(net_hours - threshold, 0), OT1_LIMIT)
    overtime2 = max(net_hours - threshold - OT1_LIMIT, 0)
    return {"normal": normal, "overtime1": overtime1, "overtime2": overtime2}
