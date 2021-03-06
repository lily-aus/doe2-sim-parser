import os
from pathlib import Path

CWD = Path(os.getcwd())

if CWD.stem == "tests":
    SAMPLE_SIM = CWD / "sample" / "sample.sim"
else:
    SAMPLE_SIM = CWD / "tests" / "sample" / "sample.sim"

if CWD.stem == "tests":
    SAMPLE_SIM_BEPS = CWD / "sample" / "sample - BEPS.sim"
else:
    SAMPLE_SIM_BEPS = CWD / "tests" / "sample" / "sample - BEPS.sim"

if CWD.stem == "tests":
    SAMPLE_SIM_BEPU = CWD / "sample" / "sample - BEPU.sim"
else:
    SAMPLE_SIM_BEPU = CWD / "tests" / "sample" / "sample - BEPU.sim"

if CWD.stem == "tests":
    SAMPLE_SIM_ES_D = CWD / "sample" / "sample - ES-D.sim"
else:
    SAMPLE_SIM_ES_D = CWD / "tests" / "sample" / "sample - ES-D.sim"
