"""
Create an application for a car rental business using a console based user interface.
The application must allow keeping records of the company’s list of clients, existing car pool and rental history.
The application must allow its users to manage clients, cars and rentals in the following ways:
    Clients
         Add a new client. Each client is a physical person having a unique ID (driver license series), name, age.
         Update the data for any client.
         Remove a client from active clients. Note that removing a client must not remove existing car rental statistics.
         Search for clients based on ID or name
         All client operations must undergo proper validation!
    Cars
         Add a new car to the car pool. Each car must have a valid license plate number, a make and model taken from a
        list of makes and models. In addition, each car will have a color.
         Remove a car from the car pool.
         Search for cars based on license number, make and model and color.
            [search with no parameters displays everything, omitting a param disregards it]
         All car operations must undergo proper validation!
    Rentals
         An existing client can rent one or several cars from the car pool for a determined period. When rented, a car
        becomes unavailable for further renting.
         When a car is returned, it becomes available for renting once again.
         Search the rental history of a given client, car, or all rentals during any given period.
    Statistics
         The list of all cars in the car pool sorted by number of days they were rented.
         The list of clients sorted descending by the number of cars they have rented.

    The application must have support for unlimited undo/redo with cascading.
"""

"""
Seminar 6
    - How to actually start writing the code
    - How to get to an incomplete, but correctly working program quickly

1. Identify the entities in the problem domain
    - Client
        attrs: id (unique, driver license), name, age
    - Customer Base (all the clients of our car rental service)
        attrs: list/dict of Client objects
    - Car
        attrs: id (unique, license plate number), make, model, color
    - Car Pool (all the cars available to our rental company)
        attrs: list/dict of Car objects
    - Rental
        attrs: car - Car object, client - Client object, start_date, end_date - naive Python date type  
    - Rental History (all the rentals recorded in accounting)
        attrs: list/dict of Rental objects

2. Decide what functionality(ies) we start with
    - remove a client
        use case:
            -> ask user for a client ID
            -> remove client from client base
                -> if client does no exist => raise CarRentalException (create a new Exception type)
    
    - search for client(s)
        use case:
            -> ask user for a search string
            -> display all clients whose ID or name includes given string
                -> if no clients found => display a message for that

3. What do we need to implement?
    a. Client class + test_client function
       ClientValidator class + specification

    b. CustomerBase (aka. ClientRepository) + test_customer_base function + test_customer_base_init function
        [you can implement search here] 
        def search(self, search_str = '')
        customer_base.search('adi') # "name"
        customer_base.search('123') # "id"
        
        def remove(self, customer_id): ...

    c. ClientService class
        - we will get back to for statistics     
    
    d. UI class
        - just the ui for remove / search (with display clients)
        - catch all exceptions

Where do we place validation code?
    i. Client.__init__
        + cannot create Clients using invalid data
        + does not check setters
    2. Client setters (also accessed using __init__)
        - tie client data with client validation (violate single responsibility)
        - hard to modify validation algorithm (move the program to another country ?)
    3. ClientValidator class
        def validate(self, client):
            # check all fields are non-empty
            # raise Exception ...
            ... 

    # ClientFactory -> dependency inject ClientValidator
    #    def create_client(self, *fields)
    #        1. call validate
    #        2. create client object
    #        3. return it
"""
















