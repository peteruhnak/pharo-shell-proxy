tests-converting
testDecodeResponse
	self
		assert: (shell decodeResponse: '{"errorCode":0,"stdout":"b3V0","stderr":"ZXJy"}')
		equals: (Dictionary with: #errorCode -> 0 with: #stdout -> 'out' with: #stderr -> 'err')