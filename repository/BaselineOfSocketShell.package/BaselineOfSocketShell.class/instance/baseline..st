baseline
baseline: spec
	<baseline>
	spec
		for: #common
		do: [ spec package: 'SocketShell'.
			spec group: 'default' with: #('SocketShell') ]