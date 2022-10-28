

THE CONSOLE

-create your data model
-manage (create, update, destroy, etc) objects via a console / command interpreter
-store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

Each task is linked and will help you to:

-put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
-create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
-create the first abstracted storage engine of the project: File storage.
-create all unittests to validate all our classes and storage engine.

HOW TO RUN THE COMMAND INTERPRETER:
$./console.py

EXECUTION:
(in interactive mode)
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

(in non-interactive mode)
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
