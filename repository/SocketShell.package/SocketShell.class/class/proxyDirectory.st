accessing
proxyDirectory
	proxyDirectory ifNil: [ self loadProxyDirectory ].
	^ proxyDirectory