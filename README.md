# What is it?

School Bot would simulate what a school would be like if they used Discord as their platform for education during lockdown.
The bot will manage each server seperately, and would require you to make your own application to run it.
I will not host the bot.

---
## How do I run it?
You can install the bot by running 
```
git clone https://github.com/TheUntraceable/School-Bot.git
```
After this you should go to the `config.json` and fill in the with your information.
Example:
```python
{
    "classes" : ["maths","english","science","computer science"], #What classes you have
    "timetable" : {
        "maths" : "9 00", # What time Maths starts
        "break 1" : "10 00", # What time break 1 starts, can be a lesson
        "english" : "10 20", # What time English starts
        "science" : "11 20", # What time Science starts
        "computer science" : "12 20", # What time Computer Science starts
        "lunch" : "13 20" # What time Lunch is, can be a lesson
        # All lesson names can be customised
    },

    "classnames" : [
        {
        "subject" : "maths", 
        "class name" : "7X",
        "time" : "9 00"
        }, {
            "subject" : "english",
            "class name" : "7Y",
            "time" : "10 20"
        }, {
            "subject" : "science",
            "class name" : "8X",
            "time" : "11 20"
        }, {
            "subject" : "computer science",
            "class name" : "7X",
            "time" : "12 : 20"
        }
    ]
}

```
After configurating the bot to your likings, run `main.py`.
# I want to contribute! How?
If you really want to contribute on this joke of a bot, go ahead, I'm not gonna stop you, but I doubt anyone will use the bot, I made this because I got bored, so I guess the only reason you'd want to contribute is because you're bored or you want to fix some stupid mistakes I made with the bot. ~~I mostly expect you to contribute for the second reason.~~

**Note:** I won't be able to reward you with anything other than a thank you for your contribution.

---
# License
I am not a lawyer but when using my software you must:
1. Not distribute it as your own software
2. Sell it for any profit

Pretty sure that's it.
```Python
'''
<-- Todo -->
    Add Class changing
    Add Classes
    Check for errors in JSON
'''
```
