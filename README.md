# Pharo Shell Socket Proxy

This is a small utility for Windows partially replacing ProcessWrapper.

It contains a small Python server that executes (shell) commands via python's subprocess.
Pharo communicates with the server through sockets, thus avoiding broken OSProcess/ProcessWrapper libraries.

Created mainly to cooperate with git command, so not really tested.

Example:

```st

shell := SocketShell new.
response := shell command: #('git' 'log' '-n' '2' '--oneline').
response exitCode. -> 0
response stderr. -> ''
response stdout. -> '373c1df Merge remote-tracking branch ''origin/master''
99e1033 Initial commit
'
```
