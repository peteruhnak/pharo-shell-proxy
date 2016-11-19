converting
encodeCommand: anArray
	^ (STON toJsonString: anArray) base64Encoded