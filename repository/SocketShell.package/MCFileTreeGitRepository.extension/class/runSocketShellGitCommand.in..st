*SocketShell
runSocketShellGitCommand: anArrayOfStrings in: aDirectory
	| r commandArgs response |
	commandArgs := {'-C'.
	MCFileTreeFileUtils current directoryPathString: aDirectory} , anArrayOfStrings.
	(Smalltalk at: #SocketShell ifAbsent: [ self error: 'Please load SocketShell' ])
		ifNotNil: [ :sS | 
			response := sS new command: {self gitCommand} , commandArgs.
			r := ''.
			response exitCode = 0
				ifTrue: [ r := response stdout ]
				ifFalse: [ response stderr
						ifNotEmpty: [ MCFileTreeGitError new signal: 'Git error: ' , response stderr ] ] ].
	^ r