def multiple_returns(sentence):
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)

if __name__ == "__main__":
    sentence = "At Holberton school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))