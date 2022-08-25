"""Write a function that prints out FizzBuzz values 1 to 100."""


PHRASES = {
    3: "Fizz",
    5: "Buzz",
}


def fizzbuzz():
    for num in range(1, 101):
        output = ""
        for phrase_num, phrase in PHRASES.items():
            if num % phrase_num == 0:
                output += phrase

        print(output or num)


fizzbuzz()
