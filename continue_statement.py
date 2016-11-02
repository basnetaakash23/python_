def PrintSumOfNumbers():
    accumulator = 0
    prompt = ''
    while prompt != 'done':
        prompt = input("Number? ")
        if prompt != 'done':
            number = int(prompt)
            accumulator += number
            print("Running sum:", accumulator)
    print("Goodbye")

PrintSumOfNumbers()
