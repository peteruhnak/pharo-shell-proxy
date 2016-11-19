converting
decodeResponse: aString
	| d |
	d := NeoJSONReader fromString: aString.
	d at: #stdout put: (d at: #stdout) base64Decoded.
	d at: #stderr put: (d at: #stderr) base64Decoded.
	^ d