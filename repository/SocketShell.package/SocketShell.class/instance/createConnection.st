instance creation
createConnection
	^ SocketStream openConnectionToHostNamed: self class hostName port: self class portNumber