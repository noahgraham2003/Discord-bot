import random

insultList = ["fuck you", "dipshit", "minor lover"]
helpList = ["no.", "use !roll, !hello, or !insult mf", "kys"]

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'stfu'
    
    if p_message =="!insult":
        return str(random.choice(insultList))

    if message == '!roll':
        return str(random.randint(1, 6)) + ", hoe"

    if p_message == '!help':
        return str(random.choice(helpList))