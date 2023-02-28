import re

from haven.instrument.load_instrument import load_instrument
from haven import registry
from haven.run_engine import RunEngine
import databroker

# Import plans
from haven import energy_scan, xafs_scan, align_slits, knife_scan, set_energy, auto_gain, calibrate_mono_gap, align_pitch2, recall_motor_position
from bluesky.plans import scan, rel_scan, list_scan, rel_list_scan, count
from bluesky.plan_stubs import sleep, pause

# Import devices
load_instrument()
for cpt in registry.components:
    # Replace spaces and other illegal characters in variable name
    name = re.sub('\W|^(?=\d)','_', cpt.name)
    # Add the device as a variable in module's globals
    globals()[name] = cpt

RE = RunEngine(connect_databroker=False)
