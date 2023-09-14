#!/usr/bin/python3

def elevator_algorithm(requests, initial_position):
    total_cylinders = 0
    seek_time = 0

    requests.sort()


    above = [r for r in requests if r >= initial_position]
    below = [r for r in requests if r < initial_position]

    # process requests above the initial position
    for request in above:
        seek_time += abs(request - initial_position)
        initial_position = request
        total_cylinders += 1

    # process requests below the initial position (in reverse order)
    for request in reversed(below):
        seek_time += abs(request - initial_position)
        initial_position = request
        total_cylinders += 1

    return total_cylinders, seek_time

if __name__ == "__main__":

    requests = [int(x) for x in input("Enter the request list (numbers separated by spaces): ").split()]
    initial_position = int(input("Enter the original location: "))

    total_cylinders, seek_time = elevator_algorithm(requests, initial_position)

    print(f"Total cylinders moved: {total_cylinders}")
    print(f"Total seek time: {seek_time}")
