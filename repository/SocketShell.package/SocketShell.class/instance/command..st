actions
command: anArray
	| request response |
	request := self encodeCommand: anArray.
	response := self decodeResponse: (self rawCommand: request).
	^ SocketShellResponse new
		exitCode: (response at: #exitCode);
		stderr: (response at: #stderr);
		stdout: (response at: #stdout);
		yourself