"""
Create an application for a car rental business using a console based user interface.
The application must allow keeping records of the company’s list of clients, existing car pool and rental history.
The application must allow its users to manage clients, cars and rentals in the following ways:
    Clients
         Add a new client. Each client is a physical person having a unique ID, name, age and driver license series.
         Update the data for any client.
         Remove a client from active clients. Note that removing a client must not remove existing car rental statistics.
         Search for clients based on ID and name.
         All client operations must undergo proper validation!
    Cars
         Add a new car to the car pool. Each car must have a valid license plate number, a make and model taken from a
        list of makes and models. In addition, each car will have a color.
         Remove a car from the car pool.
         Search for cars based on license number, make and model and color.
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
Analyzing the problem statement

1. What are the entities in the problem domain?
    -> Client, Car, Rental, Statistic (we'll get back to this last one) 
    -> Client attributes (id - unique, name, age, driver_license_series)
    -> Car attributes (license_plate - unique and valid, make, model - taken from list, color)
        [make one of (Dacia, VW, Audi, ...), model (Sandero, Polo, A3, A4)]
        [link possible make and model combinations] 
    -> Rental attributes (client, car, start_date, end_date)
        [ Car <-> Rental <-> Client ]  
    -> History attributes (car, rental_list - list of rentals)
        [do we need History?] 
        
2. What can we start with?
    [ goal is to get a working program ASAP ]
    Let's start with implementing Car-related FUNctionality
    


WEEK 6
------
    a. Create packages (ui, service, repository, domain) [in seminar/seminar_6] 
    b. Implement test_init_car + test_car function + Car class [test_init_car adds some hard-coded Car objects]   
    c. Implement functionality of adding a new car
        i. Partially implement CarRepository class + test_car_repo function:
            - list of cars 
            - add_car (check that license_plate is unique), get_cars methods [__get_item__ instead of get_cars]
        ii. Partially implement CarService class + test_car_service function:
            - link CarService to a CarRepository implementation (depencency injection)
            - add_car, get_cars methods [__get_item__ instead of get_cars] methods 
        iii. What about license_plate is valid?
            - Let's check it is non-empty [first step]
            
            2 options:
                1. Car class - license_plate is car-specific and does not involve other entities
            ->  2. CarValidator - this allows us to change our validation without touching the Car class
                    [ eg. when moving program to a different country] 

        iv. Partially implement the UI:
            - link UI to a CarService (dependency injection again)
            - add_car and show_cars methods

WEEK 7
------        
    1. How to add Client and Rental entities to program?
        - We already have CarRepository class
        - Where do we keep our clients and rentals? 
            sol 1. - Impl. classes ClientRepository and RentalRepository
                    car_repo = CarRepository() [ -> list of objects ]
                    client_repo = ClientRepository()
                    rental_repo = RentalRepository()
            sol 2. - Have a single Repository class
                    car_repo = Repository() [ -> list of objects ]
                    client_repo = Repository()
                    rental_repo = Repository()

                adv/drawbacks?
                    +/- same methods for each entity (need a generic implementation)
                      + you only write / specify / test / maintain a single class    
    
        - How will things look at Service / functionality level?
            -> Service functionalities are (usually) entity dependent
            -> Have an independent Service for each entity
            
        - How do we link a Rental object with a Car and a Client object?
             -> Rental attributes (client, car, start_date, end_date) [ Car <-> Rental <-> Client ]

             -> Create a rental [user scenario]
                1. Identify the client (unique id) --> ClientRepository [or, client_repo]
                2. Identify the car (unique id) --> CarRepository  
                3. Ask start_date and end_date + validate (at each step) 
                ----
                client = client_service.get_client(client_id)
                car = car_service.get_car(car_id)
                rental_service.create_rental(client, car, start_date, end_date)
                    -> OK or raise RentalException
        - Assemble the program
            - What to write in __init__ ???
            - How to build each layer ???
"""

