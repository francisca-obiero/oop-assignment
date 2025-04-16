class Reddington:
    def __init__(self, alias, network, associates):
        self.alias = alias  # His known name, "Raymond Reddington"
        self.network = network  # His vast web of contacts and influence
        self.associates = associates  # A list of key individuals he works with
        self.current_location = "Unknown"
        self.is_negotiating = False

    def leverage_network(self, information_needed):
        print(f"Reddington is leveraging his network to acquire information about: {information_needed}...")
        # In a real application, this might involve querying a database or other systems
        return "Highly valuable, potentially dangerous information"

    def consult_associate(self, associate_name, task):
        if associate_name in self.associates:
            print(f"Reddington is tasking {associate_name} with: {task}")
            return f"Result of {task} from {associate_name}"
        else:
            print(f"{associate_name} is not currently within Reddington's inner circle.")
            return None

    def negotiate(self, terms):
        self.is_negotiating = True
        print(f"Reddington has entered negotiations with the following terms: {terms}")
        return "A mutually beneficial (for Reddington) agreement"

    def end_negotiation(self, outcome):
        self.is_negotiating = False
        print(f"The negotiation has concluded with the following outcome: {outcome}")

    def travel(self, destination):
        self.current_location = destination
        print(f"Reddington has discreetly relocated to: {self.current_location}")

class ReddingtonAssociate(Reddington):
    def __init__(self, alias, network, associates, specialty):
        super().__init__(alias, network, associates)
        self.specialty = specialty

    def utilize_specialty(self, task_details):
        print(f"{self.alias}, with their specialty in {self.specialty}, is handling: {task_details}")
        return f"Outcome of {self.specialty} task: Success (likely)"

# Creating our "Red"
red = Reddington(alias="Raymond Reddington",
                  network="A global web of contacts, informants, and resources",
                  associates=["Dembe Zuma", "Elizabeth Keen (complex)", "Harold Cooper (reluctantly)"])

# Let's see him in action!
red.travel("Cape Town")
intel = red.leverage_network("the whereabouts of a blacklister")
print(f"Reddington obtained: {intel}")

dembe_result = red.consult_associate("Dembe Zuma", "secure the perimeter")
if dembe_result:
    print(f"Dembe's report: {dembe_result}")

agreement = red.negotiate("full immunity and access to classified information")
red.end_negotiation(outcome=agreement)

# Creating a specialized associate
mr_kaplan = ReddingtonAssociate(alias="Mr. Kaplan (deceased, but for example)",
                                network=red.network,
                                associates=red.associates,
                                specialty="Impeccable cleanup and discretion")
mr_kaplan.utilize_specialty("handling a delicate situation")