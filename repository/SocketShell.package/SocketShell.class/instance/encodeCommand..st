converting
encodeCommand: anArray
	^ (NeoJSONWriter toString: anArray) base64Encoded