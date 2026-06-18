
from logger import write_log

write_log(
    "[ADDED]",
    "HKCU_RunOnce",
    "TestMalware",
    "NIL",
    "C:\\evil.exe"
)

print("Log entry written.")