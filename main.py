import heapq

from playsound import playsound


# functions
def add_business():
    # hubla
    pass


def table1_calling():
    global table1

    called = heapq.heappop(queue)
    playsound('sounds/queue_number.mp3')
    playsound(f'sounds/{called[0]}.mp3')
    playsound(f'sounds/{called[1]}.mp3')
    playsound(f'sounds/{called[2]}.mp3')
    playsound(f'sounds/{called[3]}.mp3')
    playsound('sounds/to_table_two.mp3')
    table1 = called


def table2_calling():
    global table2

    called = heapq.heappop(queue)
    playsound('sounds/queue_number.mp3')
    playsound(f'sounds/{called[0]}.mp3')
    playsound(f'sounds/{called[1]}.mp3')
    playsound(f'sounds/{called[2]}.mp3')
    playsound(f'sounds/{called[3]}.mp3')
    playsound('sounds/to_table_two.mp3')
    table2 = called


# heap
queue = ["B001", "B002", "P001"]
table1 = ""
table2 = ""

# run
# do
table1_calling()
table2_calling()

print('=' * 50)
print(f"{'TABLE 1': <20}{'TABLE 2': <20}{'NEXT': <20}")
print('=' * 50)
print(f"{table1: <20}{table2: <20}{queue[0]: <20}")
print('-' * 50)

print('1. Add Queue Business')
print('2. Add Queue Personal')
print('3. Table 1 Calling')
print('4. Table 2 Calling')
print('5. Exit')

# input

# if else from input

# while input != exit
