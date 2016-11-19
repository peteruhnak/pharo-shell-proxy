I am ProcessWrapper alternative that connects to a Python socket server, which executes the actual process and sends response back.

I pack the command as B64(JSON(command)).

The response is unpacked as B64(JSON(response)).

Yes, the operations are not in symmetric order, because the command is an array - so it is serialized to string and then b64ed.

The response is a JSON array with stderr/stdout fields b64ed.