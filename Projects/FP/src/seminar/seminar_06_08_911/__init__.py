"""
Create an application for a car rental business using a console based user interface.
The application must allow keeping records of the company’s list of clients, existing car pool and rental history.
The application must allow its users to manage clients, cars and rentals in the following ways:
    Clients
         Add a new client. Each client is a physical person having a unique ID (driver license series), name, age.
         Update the data for any client.
         Remove a client from active clients. Note that removing a client must not remove existing car rental statistics.
         Search for clients based on ID and name [both at the same time]
         All client operations must undergo proper validation!
    Cars
         Add a new car to the car pool. Each car must have a valid license plate number, a make and model taken from a
        list of makes and models. In addition, each car will have a color.
         Remove a car from the car pool.
         Search for cars based on license number, make and model and color.
            [search with no parameters displays everything, omitting a param disregards it]
            [make = VW, model = Polo, CJ01ABC], [make = VW, model = Polo, CJ01XYZ]
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
    1. Discuss problem statement
    2. You implement some functionalities
    3. You commit & push - get seminar bonus and/or attendance
---------
SEMINAR 6
1. What are the problem domain entities?
    - Client (id - unique the driver license series, name, age)
    - Car (id - unique license plate number, make, model, color) [make = Dacia, model = Duster]
    - Rental (client, car, start_date, end_date) [*_date are naive dates, e.g. 29.05.2020]
    - Statistic (??)

2. Which functionality(-ies) do we implement first?
    a. Remove a car 
    b. Search for a car
    
3. What's the order for writing code to implement this?
    a. Car class + test_car function
    b. CarValidator class + test_car_validator function
        validate(self, car) method 
            1st version return True
            2nd version check license plate etc...
    c. Repository class + test_repository function + test_init_car function (to add car instances) 
        - remove, find methods    
    d. CarService class + test_car_service function
        - has a dependency to a Repository which stores cars
        - remove, find methods 
    e. UI
        - populate the car repo
        - remove / search functionality
    + implement CarRepoException -> custom exception class

SEMINAR 7
    - Layered architecture
    - Validating entities
    - How to assemble the program



"""
