accessing
socket
	^ socket ifNil: [ socket := self createConnection ]