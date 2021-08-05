import os
import tempfile

temp_directory = tempfile.gettempdir()  # Here, the target file is in the temp directory. So, to delete that, user must be in the required directory, or...
os.chdir(temp_directory)                # ... should give complete address of the target to be deleted in the "os.remove" command.
os.remove("targetfile.exe")
