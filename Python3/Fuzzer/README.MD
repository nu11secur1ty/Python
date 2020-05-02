This blog post will demonstrate how you can leverage Python to create a custom fuzzer script.  When performing exploit research and development it is very useful to leverage a scripting language to send in varying amounts of input to try to cause an application to crash.  Python can be very useful to spinning up a quick script to repeatedly connect to a service and send in varying amounts of input.

The first thing to understand is how the application handles user input.  Once we have an idea of the type of input to send to the service, we can begin varying levels of input to the service.  The basic idea is we connect to a service, send the buffer, increase the buffer, and then attempt it again.  We can achieve this with a “while” loop and loop until we hit an exception with “while True”.

Here is our basic starter script/Pseudocode:
```
script.py
```
The above script can be adopted to several different types of services.  You can build up your script based on the type service you’d like to fuzz.  Below is an example of a Python script to fuzz an FTP server based on the “USER” command.

```
scriptsecond.py
```
This demonstrated some basic proof of concept fuzzer script, keep in mind that depending on the application sending in ‘x41’ wont crash the service.  In some instances you need to send in different types of characters to generate a crash.  A more advanced fuzzing tool is Spike, this will send in differently amounts and types of characters to try to crash the service.  Practice making a Python fuzzer that makes an HTTP request to a service instead of an FTP server.
