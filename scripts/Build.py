import subprocess as sp
import shutil

SCRIPTS = [
    'CheckReposIntegrity.py',
    'CopySnapshotsFromUsb.py',
    'CopySnapshotsToUsb.py',
    'MakeBackup.py',
    'MakeBackupToUsbRepo.py',
    'MountRepo.py',
    'MountUsbRepo.py',
    'RemoveOldSnapshots.py'
]

for script in SCRIPTS:
    sp.run([
        shutil.which('pyinstaller'),
        '-F',
        script
    ])
