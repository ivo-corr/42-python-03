import random


def gen_event():
    names = ["bob", "alice", "dylan", "charlie"]
    events = ["run", "eat", "sleep", "grab", "move",
              "climb", "swim", "release"]
    yield (names[random.randint(0, len(names) - 1)],
           events[random.randint(0, len(events) - 1)])


def consume_event(list_ten: list):
    while (len(list_ten) > 0):
        element = list_ten.pop(random.randint(0, len(list_ten) - 1))
        
        yield element


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        event = next(gen_event())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    list_ten = [next(gen_event()), next(gen_event()), next(gen_event()), next(gen_event()),
                next(gen_event()), next(gen_event()), next(gen_event()), next(gen_event()),
                next(gen_event()), next(gen_event())]
    print(f"Built list of 10 events: {list_ten}")
    for i in consume_event(list_ten):
        print(f"Got event from list: {i}")
        print(f"Remains in list: {list_ten}")
