# Facade Pattern

This repository contains a simple example of the Facade pattern, this pattern all about implementing a common interface for accessing a variety of API's with similar goals and different representations. The Facade Pattern "extends" from the SOLID principles for software development.

Before going in to the details, we need to say that Python do not implement interfaces, like Java, instead, it use something call "Abstract Base Classes". Let me rephrase that again, in python, interfaces are made of abstract base Classes, this are referenced but no
implemented directly.

## Scripts

The `get_employees.py` is a script with a sequential definition for accessing the database, import module dependencies, instantiate a control object, run the query and close the connection.

Doing this can be harmful for the Open/Closed SOLID principle, we use a lot of code to get a simple result and if you need to change the BD engine, you will need to change all the code.

I used the AdventureWorks2012 `SQLServer` Database, its a Microsoft Sample Database provided by `RedGate`.

The `applied` folder contains a `get_employees` module will all the same example with the Facade pattern applied.

## The Facade pattern

This pattern is structural in a certain way of classification, and tries a new way of putting the program together, basically presents an unified interface to a set of interfaces (not necessary related), a high-level interface that makes the set of interfaces easier to use.

This reduces complexity from a client perspective. Internally the Facade bring it all together, the client program will have a single interface and the Facade will know the responsibility and delegates to the client requests. Then, the subsystems will handle the requests made by the Facade object to achieve the result requested by the client.

## How it works

1. Abstract Facade base class (interface): allow multiple concrete facades
2. The abstract will be implemented by the concrete facades -> get_employees
3. Client programs will call the Facade Factory to get instanced Facade to use
4. The factory will import the the desired Concrete Facade (configurable)
5. The factory then returns and instantiate a Concrete Facade - The client program will use the method to do the desired work

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
