actions
terminateServer
	<script>
	| s |
	s := self new.
	s rawCommand: 'terminate'