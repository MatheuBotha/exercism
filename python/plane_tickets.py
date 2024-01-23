"""Functions to automate Conda airlines ticketing system."""
seats = ['A', 'B', 'C', 'D']

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D
    """
    result = []
    for i in range(number):
        yield seats[i%4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    row = 0
    for i in range(number):
        if i%4 == 0:
            row += 1
            if row == 13:
                row += 1
        yield f'{row}{seats[i%4]}'



def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        yield f'{seat + flight_id:0<12}'


if __name__ == '__main__':
    test_data = [1, 2, 3, 4, 5, 100]
    result_data = [["A"],
               ["A", "B"],
               ["A", "B", "C"],
               ["A", "B", "C", "D"],
               ["A", "B", "C", "D", "A"],
               []]

    # for (number, expected) in zip(test_data, result_data):
    #     print(number)
    #     print(expected)
    #     print(list(generate_seat_letters(number)))


    # for (number, expected) in zip(test_data, result_data):
    #     print(number)
    #     print(expected)
    #     print(list(generate_seats(number)))

    passengers = ["Adele", "Björk"]

    print(assign_seats(passengers))

    # print(list(generate_codes(generate_seats(12),'Cxxx')))