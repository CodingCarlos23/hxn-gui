"""Stand-in HXN devices used when the GUI is launched with ``--offline``.

These objects deliberately keep all state in memory.  They let the GUI be
opened and edited on a development computer, but they do not communicate with
or control any real hardware.
"""


class OfflineMotor:
    """Minimal motor interface used by the GUI's local controls."""

    def __init__(self, name, position=0.0):
        self.name = name
        self.position = position

    def move(self, position, wait=True):
        self.position = position
        return self


class OfflineDetector:
    """Minimal detector object used to populate detector selection widgets."""

    def __init__(self, name):
        self.name = name


class OfflineRunEngine:
    """No-op replacement for Bluesky's RunEngine on a development machine."""

    state = "idle"

    def __call__(self, plan):
        if callable(plan):
            return plan()
        return plan

    def request_pause(self, defer=False):
        return None

    def abort(self):
        return None

    def resume(self):
        return None


def caget(pv_name, *args, **kwargs):
    """Return a safe default instead of opening an EPICS channel."""
    return 0


def caput(pv_name, value, *args, **kwargs):
    """Pretend an EPICS write succeeded without communicating with hardware."""
    return True


def fly1dpd(detectors, motor, start, end, steps, dwell_time):
    """Simulate a completed one-dimensional fly scan."""
    return lambda: motor.move(end)


def fly2dpd(detectors, motor1, start1, end1, steps1,
            motor2, start2, end2, steps2, dwell_time):
    """Simulate a completed two-dimensional fly scan."""
    def complete_scan():
        motor1.move(end1)
        motor2.move(end2)

    return complete_scan


# Zone-plate and MLL fly-scan motors expected by hxn_gui_v3.py.
zpssx = OfflineMotor("zpssx")
zpssy = OfflineMotor("zpssy")
zpssz = OfflineMotor("zpssz")
dssx = OfflineMotor("dssx")
dssy = OfflineMotor("dssy")
dssz = OfflineMotor("dssz")

# Detector groups expected by the fly-scan and mosaic selectors.
dets_fast = [OfflineDetector("dets_fast")]
dets_fast_merlin = [OfflineDetector("dets_fast_merlin")]
dets_fast_fs = [OfflineDetector("dets_fast_fs")]

# The names used by the GUI's normal Bluesky scan calls.
RE = OfflineRunEngine()
