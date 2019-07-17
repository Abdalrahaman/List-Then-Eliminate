# sky = ("Sunny", "Rainy", "Cloudy")
# temp = ("Warm", "Cold")
# humdity = ("Normal", "High")
# wind = ("Strong", "Weak")
# water = ("Warm", "Cool")
# forecast = ("Same", "Change")
# enjoy = ("+", "-")

attributesName = (
    ("Sunny", "Rainy", "Cloudy"),
    ("Warm", "Cold"),
    ("Warm", "Cool"),
    ("Same", "Change"),
    ("+", "-")
)

outputHypo = []

instances = [
    [attributesName[0][0], attributesName[1][0], attributesName[2][0], attributesName[3][0], attributesName[4][0]],
    [attributesName[0][0], attributesName[1][0], attributesName[2][1], attributesName[3][0], attributesName[4][0]],
    [attributesName[0][1], attributesName[1][1], attributesName[2][1], attributesName[3][1], attributesName[4][1]],
    [attributesName[0][0], attributesName[1][0], attributesName[2][1], attributesName[3][0], attributesName[4][1]],
]


def printAllInstances():
    for r in instances:
        for c in r:
            print(c, end=" ")
        print()


def printHypotheses(hypo, n):
    print("h" + str(n) + " =<", end=" ")
    for r in hypo:
        print(r, end=" ")
    print(">")


def isConsistentOrNot(nHypo, n):
    for h in nHypo:
        if h != "?":
            if h != instances[n][nHypo.index(h)]:
                return False
    return True


# print all instances
printAllInstances()

print("///////////// Hypotheses H ////////////////////")


def compute_ListThen_Algorithm():
    # first hypotheses ho=< don't Care, don't Care, don't Care, don't Care, don't Care, don't Care >
    hypotheses = ["?", "?", "?", "?"]
    count = 0
    for i in instances:

        if i[len(attributesName) - 1] == "-":
            if not outputHypo:
                for attribute in range(len(attributesName) - 1):
                    for attributeCase in attributesName[attribute]:
                        if i[attribute] != attributeCase:
                            outputHypo.append(list(map(lambda x: x+"", hypotheses)))
                            outputHypo[count][attribute] = attributeCase
                            # printHypotheses(outputHypo[count], count+1)
                            count += 1
            else:
                # More Than one negative hypotheses
                print("More Than one negative hypotheses")
                inconsIndex = 0
                for nextHypo in range(len(outputHypo)):
                    hypotheses = list(map(lambda x: x+"", outputHypo[inconsIndex]))
                    inconsIndex = outputHypo.index(hypotheses)
                    # print(hypotheses, end=" ")
                    # print(inconsIndex)

                    if isConsistentOrNot(hypotheses, instances.index(i)):
                        # inconsistent when true
                        del outputHypo[inconsIndex]
                        for attribute in range(len(attributesName) - 1):
                            if hypotheses[attribute] == "?":
                                for attributeCase in attributesName[attribute]:
                                    if i[attribute] != attributeCase:
                                        outputHypo.insert(inconsIndex, list(map(lambda x: x+"", hypotheses)))
                                        outputHypo[inconsIndex][attribute] = attributeCase
                                        # printHypotheses(outputHypo, inconsIndex)
                                        inconsIndex += 1

                    else:
                        inconsIndex += 1


# do operation
compute_ListThen_Algorithm()

# print all hypotheses
for h in outputHypo:
    printHypotheses(h, outputHypo.index(h) + 1)
