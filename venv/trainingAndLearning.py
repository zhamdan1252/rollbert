
'''
What do we want as utility in bot:

rolling dice:
    -!roll:
        !roll -base d20 roll
        !roll -#d#
            -must be a d4,d6,d8,d10,d12,d20
        !roll adv
        !roll disadv
        !roll private - sends roll to dms

    -!spell name
        search json file of spells

    -history of last 10 rolls

'''


"""
client = discord.Client() -connects to client

@client.event <-a decorator
    ###DECORATOR NOTES###
    -a decorator is a wrapper function for another function
        -decorator takes in original function as an argument and returns a modified version of it
        -defining a function within a function, can return a function as a value
            -calling the function you defined allows you to retain access to inner variables that would normally
            be garbage collected
        -example:
                def printer():
                    print("Hello world")

                def display_info:
                    
                    def inner():
                        print("executing", func.__name__, "function")
                        func()
                        print("finished execution)
                    
                    return inner
                    
                CALLING PRINTER() RETURNS: "Hello World"
                
                decorated_func = display_info(printer)
                
                deccorated_func() RETURNS: "exectuing printer function\n, hello world\n finished exectuing"
                
        how to set it up it implicity with @ symbol:
            @display_info
            def_printer():
                print("hello world")
                
            def display_info: same as above
            
            NOW CALLING printer() WILL RETURN WHAT
                    "decorated_func = display_info(printer)
                     decorated func()" did in the previor example

"""
"""
#ON STARTUP             
@client.event <-register events
async def on_ready(): <-asynchronous library: callbacks-functions happen with some other function occurs
    print("we have logged in as {0.user}'.format(client))
    
"""

"""
#EVENT ON RECEIVING MESSAGE

@client.event
async def on_message(message):
    if message.author == client.user:
        return <-do not want to read messages from itself
        
    #trigger for bot to act on message
    if message.content.startswith("$hello"): 
        await message.channel.send("hi!") <- when it receives $hello, it responds in the same channel
"""

"""
#RUNNING CLIENT

(says to use an environment variable to hide token)
    on replit for this example:
        made a .env file and stored TOKEN = fal;sdfjalsdjfal
        imported os
            then runs client.run() as below
client.run(os.getenv('TOKEN'))
"""

"get info from api"