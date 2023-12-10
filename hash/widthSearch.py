class Person:
    def __init__(self, Name, Job, Friend, Node):
        self.Name = Name
        self.Job = Job
        self.Friend = Friend
        self.Node = Node

    def getName(self):
        if self.Friend == 'Me':
            return 'Me'
        return self.Name

    def getJob(self):
        return self.Job

    def getNode(self):
        return self.Node

    def getFriend(self):
        return self.Friend


jobs = []
personsMas = []


def appendPerson(Person):
    persons = []
    if (Person.getJob() in jobs):
        persons = personsMas[jobs.index(Person.getJob())]
        persons.append(Person)
        personsMas[jobs.index(Person.getJob())] = persons
    else:
        jobs.append(Person.getJob())
        persons.append(Person)
        personsMas.append(persons)

Me = Person('Me', 'Охотник', '', 0)
PersonOne = Person('Alice', 'Программист', Me, 1)
PersonTwo = Person('Kolya', 'Почтальон', PersonOne, 2)
PersonThree = Person('Anna', 'Программист', PersonTwo, 3)
PersonFour = Person('Alice', 'Продавец', PersonTwo, 3)

appendPerson(PersonOne)
appendPerson(PersonTwo)
appendPerson(PersonThree)
appendPerson(PersonFour)

def Search(nameOfJob):
    nameOfJob = nameOfJob[0].upper() + nameOfJob[1:]
    if nameOfJob in jobs:
        persons = personsMas[jobs.index(nameOfJob)]
        for i in range(len(persons)):
            print(persons[i].getName()+" - "+persons[i].getJob())
            node = persons[i].getNode()
            helpPerson = persons[i]
            if node == 1:
                print("^")
                print(Me.getName()+" - "+Me.getJob())
            while node > 1:
                print("^")
                node = helpPerson.getNode()
                helpPerson = helpPerson.getFriend()
                print(helpPerson.getName()+" - "+helpPerson.getJob())
            print(f"\n\n")
    elif nameOfJob == Me.getJob():
        print(Me.getName() + " - " + Me.getJob())
    else:
        print(f"Профессии \"{nameOfJob}\" нет в списке")

Search("Инженер")