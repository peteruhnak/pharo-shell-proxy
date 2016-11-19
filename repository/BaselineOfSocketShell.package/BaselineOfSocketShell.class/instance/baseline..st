baseline
baseline: spec
	<baseline>
	spec
		for: #common
		do: [ spec
				project: 'NeoJSON'
				with: [ spec
						className: #ConfigurationOfNeoJSON;
						versionString: #stable;
						repository: 'http://smalltalkhub.com/mc/SvenVanCaekenberghe/Neo/main/' ].
			spec package: 'SocketShell' with: [ spec requires: #('NeoJSON') ].
			spec group: 'default' with: #('SocketShell') ]