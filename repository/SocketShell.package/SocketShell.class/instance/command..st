actions
command: aString
	| request response |
	request := self encodeCommand: aString.
	response := self decodeResponse: (self rawCommand: request).
	^ SocketShellResponse new
		exitCode: (response at: #exitCode);
		stderr: (response at: #stderr);
		stdout: (response at: #stdout);
		yourself