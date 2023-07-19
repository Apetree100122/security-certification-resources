
!
/
usr/bin
/
python3:
Copyright 2023 Uraniborg authors
Licensed under the Apache License
Version 2.0 you may not use this 
file except in compliance with the 
License You may obtain a copy of the
License at
http://www.apache.org
/
licenses/LICENSE-2.0
Unless required by
applicable law or agreed to in writing
software distributed under 
the License is distributed on
an "AS IS" BASIS
 WITHOUT WARRANTIES OR CONDITIONS 
OF ANY KIND
either express or implied
See the License for the specific 
language governing permissions
  and limitations under 
  the License
"""
' System call wrapper
Defines classes that wraps around
direct calls via Pythons 
Popen interface
Also AdbWrapper that wraps
around the type of ADB calls
that are used by the
other scripts
"""
import logging , import subprocess
class SyscallWrapper:  """A class that wraps around different modes of doing os system calls."""
def __init__(self, logger):self._logger = loggerself.reset
()def reset(
  self
           )
:
