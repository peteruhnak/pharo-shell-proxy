class initialization
initialize
	Smalltalk
		at: #MCFileTreeGitRepository
		ifPresent: [ :cls | 
			cls class
				compile:
					'runProcessWrapperGitCommand: anArrayOfStrings in: aDirectory
	^ self runSocketShellGitCommand: anArrayOfStrings in: aDirectory' ]