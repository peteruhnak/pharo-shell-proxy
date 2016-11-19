accessing
portNumber
	| portFile |
	portFile := self proxyDirectory / 'port.txt'.
	portFile exists
		ifFalse: [ self error: 'Proxy is not running.' ].
	^ portFile contents asNumber