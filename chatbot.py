from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?"]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you ",]
    ],
    [
        r"(.*)your name?",
        ["My name is thecleverprogrammer, but you canjust call me robot and i'm a chat bot .",]
    ],
    [
        r"how are you(.*) ?",
        ["I'm doing very well", "I am great!",]
    ],
    [
        r"sorry(.*)",
        ["It is alright", "It is OK, nevermind that.",]
    ],
    [
        r"I'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    # [
    #     r"(.*)created(.*)",
    #     ["Aman Kharwal created me using Python's NLTK library ","top secret ;)",]
    # ],
    [
        r"(.*)(Location city) ?",
        ['New Delhi, India',]
    ],
    [
        r"(.*)raining in(.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan Cricket",]
    ],
    [
        r"who (.*) (Cricket|Batsman)?",
        ["Virat kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"How is your day?",
        ["It's a great day",]
    ],
    [
        r"are you a robot?",
        ["Yes,I'm.",]
    ],
    [
        r"How was you created?",
        ["I was created by python and nltk.",]
    ],
    [
        r"what is python?",
        ["Python is a programming language.",]
    ],
    [
        r"is python good?",
        ["Yes, it's the best programming language.",]
    ],
    [
        r"(.*) programs (.*) created with python?",
        ["Programs like lottery games and calculator are created with python.",]
    ],
    [
        r"(.*) elements are used in creating web pages?",
        ["HTML and CSS are used in creating web pages.",],
    ],
    [
        r"Is HTML used for what?",
        ["HTML is used for creating web pages",]
    ],
    [
        r"Is CSS used for what?",
        ["CSS is used for designing web pages",]
    ],
    [
        r"Which page did your creator create with then?",
        ["I created my profilio and manga website.",]
    ],
    [
        r"(.*)",
        ["That is nice to hear",]
    ],
]

#defult message at the start of chat
print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#create chat bot
chat = Chat(pairs, reflections)
#Start conversation
chat.converse()