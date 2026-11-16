Feature: initialise rover

    Scenario: Successful initialisation
        Given the rover has not been initialised
        And the system is prompting the operator "Please enter initial X, Y coordinates and direction for rover"
        When the operator enters "1,1,N"
        Then the rover is initialised at X=1, Y=1, facing north
        And the system displays "The rover is at X=1, Y=1, facing north. Please enter instructions..."
