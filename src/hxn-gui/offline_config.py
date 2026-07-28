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
