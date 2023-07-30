import openai

API_KEY = '---'  #use own API key
openai.api_key = API_KEY

print("\nHey! Let's setup your personal biography.\n")

# getting key/personal info
expertise = input("\nWhat is your area of expertise?\n")
achievements = input("\nAny notable achievments/awards?\n")
philosophy = input("\nWhat is your professional philosophy?\n")
interests = input("\nWhat are your personal interests/hobbies?\n")
trait = input("\nWhat character trait do you want to shine through most in this bio?\n")

# check for trait sentiment
traitPositive = False
while traitPositive == False:
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = f"Answer either \"positive\", \"negative\", or \"neutral. Determine the sentiment of the character trait: {trait}",
        temperature = 0,
        max_tokens = 25,
    )
    if "negative" in response["choices"][0]["text"].lower():
        trait = input("\nPlease use a more positive character trait.\n")
    else:
        traitPositive = True

# POTENTIAL ISSUE:
# Rate limit for ai calls is 3/min. If user inputs two negative traits in a row, the third input (even if positive) will cause program to end.
# When integrated into app, is rate limit individual to each user, or does the app as a whole follow strict 3/min?

johnPrompt = f"""
Write a biography (around 200 words, one paragraph) for John Doe, a realtor in Los Angeles, based off this information:
Works for: SetSchedule
5 year(s) of experience
Area of expertise: {expertise}
Notable achievements/awards: {achievements}
Professional philosophy: {philosophy}
Personal interest(s): {interests}
John wants their {trait} to shine through in their bio.
"""

response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = johnPrompt,
    max_tokens = 250,
    temperature = 1,
    frequency_penalty = 1,
)

# POTENTIAL ISSUE:
# davinci model being used will be retired beginning of 2024

print("\nHere's your personalized biography:")
biography = response["choices"][0]["text"][1:]
print(biography)
