class GroupMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
member1= GroupMember("Jennie", "rapper")
member2= GroupMember("Jisoo", "visual")
member3= GroupMember("Lisa", "dancer")
member4= GroupMember("Rose", "singer")

commands = {
         "rapper": ["rap", "sing"],
         "visual": ["pose", "sing"],
         "dancer": ["dance", "rap"],
         "singer": ["sing", "dance"]
        }

def checking_decorator(command):
    def decorator(func):
        def wrapper(self, member):
            role = member.role
            if command in commands.get(role, []):
                func(self, member)
            else:
                print(f"{member.name} не может выполнить команду {command}")
        return wrapper
    return decorator

class CommandHandler:

    @checking_decorator("rap")
    def rap(self, member):
        print(f"{member.name} читает рэп.")

    @checking_decorator("sing")
    def sing(self, member):
        print(f"{member.name} поёт.")

    @checking_decorator("dance")
    def dance(self, member):
        print(f"{member.name} танцует.")

    @checking_decorator("pose")
    def pose(self, member):
        print(f"{member.name} позирует.")

handler = CommandHandler()
handler.pose(member2)
handler.dance(member1)



