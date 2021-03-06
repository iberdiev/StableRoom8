from collections import OrderedDict
from operator import itemgetter
import copy
from .models import Survey

########################################
def getKeyByVal(inptDict, inputVal):
    for key, val in inptDict.items():
        if val == inputVal:
            return key
def removeCycle(preferences, table):
    tmpPreferences = preferences
    # remove the cycle matches symmetrically
    for i in range(len(table[0]) - 1):
        tmpPreferences[table[1][i]].remove(table[0][i + 1])
        tmpPreferences[table[0][i + 1]].remove(table[1][i])
    return tmpPreferences
def cycleExists(table):
    tableLeft = table[0]
    tableRight = table[1]
    # check if all elements in column are unique
    if len(tableLeft) > len(set(tableLeft)):
        return True
    else:
        return False
def stableNotPossible(preferences):
    for i in preferences:
        if len(preferences[i]) == 0:
            return True
    return False
def isStable(preferences):
    for i in preferences:
        if len(preferences[i]) != 1:
            return False
    return True
def step1(inputList):
    proposals = {}
    numProposals = {}
    queue = []
    for i in inputList["preferences"]:
        queue.append(i)
        proposals[i] = None
        numProposals[i] = 0
    tmpPreferences = copy.deepcopy(inputList["preferences"])
    while not len(queue) == 0:
        i = queue[0]
        numProposals[i] += 1
        for j in inputList["preferences"][i]:
            if proposals[j] == None:
                del queue[0]
                proposals[j] = i
                break
            elif proposals[j] != i:
                current_index = inputList["preferences"][j].index(i)
                other_index = inputList["preferences"][j].index(proposals[j])

                if current_index < other_index:
                    del queue[0]
                    queue.insert(0, proposals[j])
                    # Remove old proposal symmetrically
                    tmpPreferences[proposals[j]].remove(j)
                    tmpPreferences[j].remove(proposals[j])
                    proposals[j] = i
                    break
                else:
                    # Remove invalid proposal symmetrically
                    tmpPreferences[i].remove(j)
                    tmpPreferences[j].remove(i)
        inputList["preferences"] = copy.deepcopy(tmpPreferences)
    return (proposals, inputList)
def step2(proposals, inputList):
    tmpPreferences = copy.deepcopy(inputList["preferences"])
    for i in inputList["preferences"]:
        #  Remove the right hand side of the preferred element
        proposalIndex = tmpPreferences[i].index(proposals[i])
        tmpPreferences[i] = tmpPreferences[i][:proposalIndex + 1]
        # Remove all other instances of the given element
        for j in inputList["preferences"]:
            # Try to remove element from all preference lists
            key = getKeyByVal(proposals, i)
            if j != i and j != proposals[i] and j != key:
                try:
                    tmpPreferences[j].remove(i)
                except ValueError:
                    pass
    # for i in inputList["preferences"]:
    #    pass
    return tmpPreferences
def step3(preferences):
    first = True
    # search for cycles until a stable or unstable matches are found
    while True:
        # create a table with two columns
        table = ([], [])
        # check if stable matching is possible
        if stableNotPossible(preferences):
            raise AlgorithmError("Stable matching not possible.")
        for i in preferences:
            # add the first instance that has atleast 2 preferences
            if len(preferences[i]) >= 2 and first == True:
                # add element
                firstPreference = i
                table[0].append(firstPreference)
                # add second preference of element
                secondPreference = preferences[i][1]
                table[1].append(secondPreference)
                first = False
            elif first == False:
                # check if a cycle exists in the table
                if cycleExists(table):
                    # remove cycle
                    preferences = removeCycle(preferences, table)
                    first = True
                    # start again
                    break
                # add the last preference of the previous second preference
                # from the table
                firstPreference = preferences[secondPreference][-1]
                table[0].append(firstPreference)
                # add the second preference of the first preference
                secondPreference = preferences[firstPreference][1]
                table[1].append(secondPreference)
        # If the preferences are stable, return them
        if isStable(preferences):
            return preferences
def apply(input1):
    step_1 = step1(input1)
    return step3(step2(step_1[0], step_1[1]))
########################################
def executeAlgorithm(quierySet):
    preMates = []
    chosen = []
    for person in quierySet:
        if person.year > 1 and person.want_roommate == 1:
            pair = {
                person.email,
                person.email_roommate
            }
            if pair in chosen:
                preMates.append(person.email)
                preMates.append(person.email_roommate)
            else:
                chosen.append(pair)

    country = {}
    data = []
    # code below takes the data from EXCEL file
    # data will have all the numeric values that is sent by the users
    # campus will have campus names as keys and the list of names of the students as a value to key
    # same with gender and country.
    for person in quierySet:
        if person.email not in preMates:
            data.append([
                    person.full_name,
                    person.scale1,
                    person.scale2,
                    person.scale3,
                    person.scale4,
                    person.scale5,
                    person.scale6,
                    person.scale7,
                    person.scale8
                ])
            country[person.full_name] = person.country

    # gender dictionary is in the form of gender = {'male': [person1, person2], 'female': [person3, person4]}
    # code below will give to each person their numerical values 🔥🔥🔥🔥🔥
    # code below will add another person named 'Unknown' if the number of people in each campus and in each gender has and odd number of
    # people, if a person will be matched   by the unknown the person will not have a roommate :((((

    if len(data) % 2 != 0:
        data.append(['Unknown'])
        country['Unknown'] = "Unknown"
        for i in range(1, len(data[0])):
            data[len(data) - 1].append(5)

    # code below does several stuff:
    # 1) it finds the preference value for each person to every other person within  gender
    # 2) it sorts the preferences of each person according to the preference value (ascending order)
    # 3) the preference values are removed and each person will have its preference list of individuals
    # 4) each individual preference is being sorted by country (two people from one Country cannot be roommates) unless there are no other chances
    #print(gender)
    data = sorted(data, key=lambda x: x[0])
    preferenceList = []
    for i in range(len(data)):
        subPreference = [data[i][0]]
        subOfContent = []
        for j in range(len(data)):
            if i != j:
                subOfPerson = [data[j][0]]
                difference = 0
                for u in range(1, len(data[i])):
                    difference += abs(data[i][u] - data[j][u])
                subOfPerson.append(difference)
                subOfContent.append(subOfPerson)
        subOfContent = sorted(subOfContent, key=lambda subOfContent: subOfContent[1])
        subPreference.append(subOfContent)
        preferenceList.append(subPreference)
    sortedPreference = {}
    for i in range(len(preferenceList)):
        preferences = []
        for j in range(len(preferenceList[i][1])):
            preferences.append(preferenceList[i][1][j][0])
        sortedPreference[preferenceList[i][0]] = preferences

    for key in sortedPreference:
        i = 0
        k = 0
        while i + k < len(sortedPreference[key]):
            if country[key] != country[sortedPreference[key][i]]:
                i += 1
            else:
                sortedPreference[key].append(sortedPreference[key][i])
                del sortedPreference[key][i]
                k += 1
    # Getting the information about the country of each person

    #applying the algorithm and
    beforeMainAlgorithm = {"preferences": sortedPreference}
    result = apply(beforeMainAlgorithm)
    final_result = {}
    for key, item in result.items():
        if key != final_result.get(item[0]):
                final_result[key] = item[0]

    for i in range(0, len(preMates), 2):
        person1 = Survey.objects.filter(email=preMates[i], email_roommate=preMates[i+1])[0].full_name
        person2 = Survey.objects.filter(email=preMates[i + 1], email_roommate=preMates[i])[0].full_name
        final_result[person1] = person2
    return final_result
