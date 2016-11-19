actions
rawCommand: aString
	self socket sendCommand: aString.
	^ self socket upToEnd
	