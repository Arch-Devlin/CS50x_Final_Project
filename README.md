# Adventure
#### Video Demo:  <https://youtu.be/7ArAJx442_o>
#### Description:

Adventure is a small text based dungeon crawling game. The user logs in an tries to get through as many rooms as possible and make it out alive, to get the highest score or bring back gold coins to add to their collection. The rooms entered are randomly selected from 10 possible rooms. There are events in some rooms that give the user an item of 3 possible items (armour, a sword or coin) and rooms that require one or more of these items to progress or do certain things in these rooms.

adventure.db: A database with 5 fields, id, username, hash, high_score and Coins all type integer. id is a primary key. username and hash store the registered username and hash of the password respectively. high_score stores the highest score ever attained by the user. Coins stores the coins that the user has accumulated by leaving the dungeon alive with them.

adventureV3.py: A python file containing everything else.
The item types are stored in an array and the inventory of the items the user has is stored in a dictionary.
The rooms are stored in a 3d array with information for each room including its id/number text to inform the user, a function to execute and more ascii art to represent an image of the room to display.
There are 25 defined functions including the main function, one for each room, the start, logging in, logging out, registering, getting an item, changing room, entering the new room and leaving.
Events (the funcions executed in the different rooms) are generaly if elif/else statements that check the users input and other conditions including the presence of items in the inventory.
I ended up having to pass almost everything from one funcion to the next. How the whole thing works is a function is executed which executes another. For example one of the events calls for the change room function which changes the current room number to a random number between 1 and 10 and then calls the enter function which adds +1 to the room counter and calls the event function for the current room number and all the info like inventory is passed on. Or when you leave the dungeon the current room number is checked to determin if the you made it out alive.
When leaving the dongeon the useres high score  on the database is commpared to the current score and if the current score is higher the high score is updated on the database. Additionaly if the user made it out alive the database is updated to add the number of gold coins in the inventory to the Coins.
