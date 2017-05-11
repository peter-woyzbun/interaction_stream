


class SlackInteractionSet(object):

    INTERACTIONS = tuple()

    def __init__(self, set_context: dict, interaction_context: dict):
        self.set_context = set_context
        self.interaction_context = interaction_context
        self.next_set = None
        self.next_set_context = None

    def num_interactions(self):
        return len(self.INTERACTIONS)

    def execute_interaction(self, num):
        getattr(self, self.INTERACTIONS[num])()


class SetupGoogle(SlackInteractionSet):

    INTERACTIONS = ('setup_message', )

    def __init__(self, *args, **kwargs):
        SlackInteractionSet.__init__(self, *args, **kwargs)

    def setup_message(self):
        print("\n")
        print("Started SetupGoogle interaction set.")
        print("Click here to setup accounts...")


class UserWelcome(SlackInteractionSet):

    INTERACTIONS = ('initial_message', 'handle_setup_response')

    def __init__(self, *args, **kwargs):
        SlackInteractionSet.__init__(self, *args, **kwargs)

    def initial_message(self):
        print("Hi, I’m fellow. I’m your new work co-pilot")
        print("I can help you get <mely feedback on the work you do. First, I’ll need "
              "to connect to some of the tools that you use daily to see who you work with.")
        # Send payload asking user if they want to setup google etc.

    def handle_setup_response(self):
        if self.interaction_context['do_setup']:
            self.next_set = 'setup_google'
        else:
            pass


def example():

    INTERACTION_SET_MAP = {'setup_google': SetupGoogle,
                           'user_welcome': UserWelcome}

    user_welcome_1 = UserWelcome(set_context=dict(), interaction_context=dict())
    user_welcome_1.execute_interaction(num=0)

    interaction_context = {'do_setup': True}
    user_welcome_2 = UserWelcome(set_context=dict(), interaction_context=interaction_context)
    user_welcome_2.execute_interaction(num=1)

    if user_welcome_2.next_set is not None:
        next_set = INTERACTION_SET_MAP[user_welcome_2.next_set](set_context=dict(), interaction_context=dict())
        next_set.execute_interaction(num=0)

example()