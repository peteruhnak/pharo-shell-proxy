# Pharo Shell Socket Proxy

This is a small utility for Windows partially replacing ProcessWrapper.

It contains a small Python server that executes (shell) commands via python's subprocess.
Pharo communicates with the server through sockets, thus avoiding broken OSProcess/ProcessWrapper libraries.

Created mainly to cooperate with git command, so not really tested.

## Example

```st

shell := SocketShell new.
response := shell command: #('git' 'log' '-n' '2' '--oneline').
response exitCode. -> 0
response stderr. -> ''
response stdout. -> '373c1df Merge remote-tracking branch ''origin/master''
99e1033 Initial commit
'
```

## Installation

If for whatever reason you want to try this abomination, you can install it in Pharo

```st
Metacello new
    baseline: #SocketShell;
    repository: 'github://peteruhnak/pharo-shell-proxy/repository';
    load
```

Upon installation `SocketShell class>>initialize` will override `MCFileTreeGitRepository class>>runProcessWrapperGitCommand:in:` to use `SocketShell` instead.
If you installed `GitFileTree` after `SocketShell`, then you need to manually reinitialize the `SocketShell` class.

The Python server `proxy.py` has to be started separately (for painfully obvious reasons not from Pharo).
The server can also be stopped with `SocketShell class>>terminateServer` on by running the `stopProxy.py` script.
