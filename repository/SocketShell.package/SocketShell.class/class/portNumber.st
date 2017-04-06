accessing
portNumber
	| portFile |
	portFile := FileLocator temp asFileReference / 'pharo-shell-proxy-port.txt'.
	portFile exists
		ifFalse: [ self error: 'Proxy is not running.' ].
	^ portFile contents asNumber