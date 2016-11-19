accessing
loadProxyDirectory
	<script>
	(UIManager default chooseDirectory: 'Select directory containing the shell proxy')
		ifNotNil: [ :dir | proxyDirectory := dir ]