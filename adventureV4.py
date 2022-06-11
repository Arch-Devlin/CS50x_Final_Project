import random
import numpy as np
from cs50 import SQL
import re
from werkzeug.security import check_password_hash, generate_password_hash
import getpass

def main():

    user = 0

    items = ["Rusty Sword", "Rusty Armour", "Gold Coin"]

    inventory = {
        "Rusty Sword": 0,
        "Rusty Armour": 0,
        "Gold Coin": 0
    }

    rooms = np.array([(0,"You've entered The Dungeon. Before you lies a dark room lit by two torches on the left and right moss covered walls. Ahead of you is a door.",first,""),
    (1,"The room is empty with a door on the other side.",empty,"\
__________________________________________________________________________\n\
=================================================================    -----|\n\
=========================================================    -------/     |\n\
 _____________________________________________________------/       ][    |\n\
|       ][       ][       ][       ][       ][       |      ][       -----|\n\
|       ][       ][       ][       ][       ][       |       -------/     |\n\
|_______][_______][_______][_______][_______][_______|------/       ][    |\n\
|       ][       ][       ][       ][       ][       |      ][       -----|\n\
|       ][       ][       ][       ][       ][       |       -------/     |\n\
|_______][_______][_______][_______][_______][_______|------/       ][    |\n\
|       ][       ][     ______     ][       ][       |      ][       -----|\n\
|       ][       ][  ,-'  ||  `-.  ][       ][       |       -------/     |\n\
|_______][_______][_/ {~~~||~~~} \_][_______][_______|------/       ][    |\n\
|       ][        /'{~~~~~||~~~~~}'\        ][       |      ][       -----|\n\
|       ][       | {~~~~~~||~~~~~~} |       ][       |       -------/     |\n\
|_______][_______|        ||        |_______][_______|------/       ][    |\n\
|       ][       |        ||        |       ][       |      ][       -----|\n\
|       ][       |        ||        |       ][       |       -------/     |\n\
|_______][_______|        ||        |_______][_______|------/       ][    |\n\
|       ][       |     () || ()     |       ][       |      ][       -----|\n\
|       ][       |        ||        |       ][       |       -------/     |\n\
|_______][_______|        ||        |_______][_______|------/       ][    |\n\
|       ][       |        ||        |       ][       |      ][       -----|\n\
|       ][       |        ||        |       ][       |       -------/     |\n\
|_______][_______|________||________|_______][_______|------/       ][    |\n\
 \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@\_    ][       -----|\n\
  \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_   -------/     |\n\
   \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\/       ][    |\n\
    \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_     -----|\n\
     \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\--/     |\n\
      \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_    |\n\
       \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\--|\n\
        \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~|\n\
         \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@|"),
    (2,"The room opens out to the outside and there is a door to another room.",cave,"\
 ____________________________________________________\n\
|       ][       ][       ][       ][       ][       |\n\
|       ][       ][       ][       ][       ][       |\n\
|_______][_______][_______][_______][_______][_______|\n\
|       ][       ][       ][       ][       ][       |\n\
|       ][       ][       / \      ][       ][       |\n\
|_______][_______][______/_|_\_____][_______][_______|\n\
|       ][       ][    /( /'\ )\   ][       ][       |\n\
|       ][       ][ ///.\>   </.\ \][       ][       |\n\
|_______][_______][//(.\>     </.) \[_______][_______|\n\
|       ][       ]/(.\>         </.)\       ][       |\n\
|       ][       //.\>           </.\       ][       |\n\
|_______]_______/(.\>             </.)\_____][_______|\n\
|       ][    (/(.\>               </.)\)   ][       |\n\
|       ][    (//.\>               </.\,)   ][       |\n\
|_______][___(//.\>                 </.\,)__][_______|\n\
|       ][  (//.\>                   </.\,) ][       |\n\
|       ][   (//.\>         ~~~~\   </.\,)  ][       |\n\
|_______][____(//.\>    ~~~/~~~ \  </.\,)___][_______|\n\
|       ][     (//.\> ~/ ~~       </.\,)    ][       |"),
    (3,"There is a monster looming over you. You must defeat, or evade it to get to the door you can see past its hulking body.",monster,"\
                                             ,--,  ,.-.\n\
                                    .       '-,-`,'-.' | ._\n\
                ,          .    .   |\         }  )/  / `-,',\n\
               /|          |\  /|   | |        /  \|  |/`  ,`\n\
              [ ,       ,.`  `,` `, | |  _,...(   (      .',\n\
              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\ \n\
               \  \_\,``,   ` , ,  /  |         )         _,/\n\
                \  '  `  ,_ _`_,-,<._.<        /         /\n\
                 ', `>.,`  `  `   ,., |_      |         /\n\
                   \/`  `,   `   ,`  | /__,.-`    _,   `\ \n\
               -,-..\  _  \  `  /  ,  / `._) _,-\`       \ \n\
                \_,,.) /\    ` /  / ) (-,, ``    ,        |\n\
               ,` )  | \_\       '-`  |  `(               \ \n\
              /  /```(   , --, ,' \   |`<`    ,            |\n\
             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)\n\
       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`\n\
      (-, \           ) \ ('_.-._)/ /,`    /\n\
      | /  `          `/ \ V   V ,/`     /\n\
   ,--\(        ,     <_/`\      ||      /\n\
  (   ,``-     \/|         \-A.A-`|     /\n\
 ,>,_ )_,..(    )\          ',,_-`  _--`\n\
(_ \|`   _,/_  /  \_            ,--`\n\
 \( `   <.,../`     `-.._   _,-`\n"),
    (4,"The room is empty save a closed chest between you and the door across the room",chest,"*******************************************************************************\n\
          |                   |                  |                     |\n\
 _________|________________.="'"'""'"'"_;=.______________|_____________________|_______\n\
|                   |  ,-"'"'"_,="'"'""'"'"     `"'"'"=.|                  |                   |\n\
|___________________|__"'"'"=._o`"'"'"-._        `"'"'"=.______________|___________________|\n\
          |                `"'"'"=._o`"'"'"=._      _`"'"'"=._                     |\n\
 _________|_____________________:=._o "'"'"=._."'"'"_.-="'"'"'"'"'"=.__________________|_______\n\
|                   |    __.--"'"'" , ; `"'"'"=._o."'"'" ,-"'"'""'"'""'"'"-._ "'"'".   |                   |\n\
|___________________|_._"'"'"  ,. .` ` `` ,  `"'"'"-._"'"'"-._   "'"'". '__|___________________|\n\
          |           |o`"'"'"=._` , "'"'"` `; ."'"'". ,  "'"'"-._"'"'"-._; ;              |\n\
 _________|___________| ;`-.o`"'"'"=._; ."'"'" ` '`."'"'"\` . "'"'"-._ /_______________|_______\n\
|                   | |o;    `"'"'"-.o`"'"'"=._``  '` "'"'" ,__.--o;   |                   |\n\
|___________________|_| ;     (#) `-.o `"'"'"=.`_.--"'"'"_o.-; ;___|___________________|\n\
____/______/______/___|o;._    "'"'"      `"'"'".o|o_.--"'"'"    ;o;____/______/______/____\n\
/______/______/______/_"'"'"=._o--._        ; | ;        ; ;/______/______/______/_\n\
____/______/______/______/__"'"'"=._o--._   ;o|o;     _._;o;____/______/______/____\n\
/______/______/______/______/____"'"'"=._o._; | ;_.--"'"'"o.--"'"'"_/______/______/______/_\n\
____/______/______/______/______/_____"'"'"=.o|o_.--"'"'""'"'"___/______/______/______/____\n\
/______/______/______/______/______/______/______/______/______/______/_____/__\n\
*******************************************************************************"),
    (5,"Three plinths lie before you each with an item on top.",choose,"\n\n\n\n\
   ___________             ___________             ___________\n\
 (___,.....,___)         (___,.....,___)         (___,.....,___)\n\
  \__,.....,__/           \__,.....,__/           \__,.....,__/\n\
    =========               =========               =========\n\
     |||||||                 |||||||                 |||||||\n\
     |||||||                 |||||||                 |||||||\n\
     [=====]                 [=====]                 [=====]\n\
     |||||||                 |||||||                 |||||||\n\
     |||||||                 |||||||                 |||||||\n\
     [=====]                 [=====]                 [=====]\n\
     |||||||                 |||||||                 |||||||\n\
     |||||||                 |||||||                 |||||||\n\
    ,_______,               ,_______,               ,_______,\n\
      )   (                   )   (                   )   (\n\
    ,      `                ,      `                ,      `\n\
  _/_________\_           _/_________\_           _/_________\_\n\
 |_____________|         |_____________|         |_____________|\n"),
    (6,"The room is empty with a door on the other side.",arrow,"\
__________________________________________________________________________\n\
=================================================================    -----|\n\
=========================================================    -------/ ()  |\n\
 _____________________________________________________------/   ()  ][ () |\n\
|   _   ][   _   ][   _   ][   _   ][   _   ][   _   | ()   ][   ()  -----|\n\
|  ( )  ][  ( )  ][  ( )  ][  ( )  ][  ( )  ][  ( )  |  ()   -------/ ()  |\n\
|_______][_______][_______][_______][_______][_______|------/  ()   ][ () |\n\
|   _   ][   _   ][   _   ][   _   ][   _   ][   _   | ()   ][  ()   -----|\n\
|  ( )  ][  ( )  ][  ( )  ][  ( )  ][  ( )  ][  ( )  |  ()   -------/ ()  |\n\
|_______][_______][_______][_______][_______][_______|------/  ()   ][ () |\n\
|   _   ][   _   ][     ______     ][   _   ][   _   | ()   ][   ()  -----|\n\
|  ( )  ][  ( )  ][  ,-'  ||  `-.  ][  ( )  ][  ( )  |   ()  -------/ ()  |\n\
|_______][_______][_/ {~~~||~~~} \_][_______][_______|------/  ()   ][ () |\n\
|   _   ][   _    /'{~~~~~||~~~~~}'\    _   ][   _   | ()   ][   ()  -----|\n\
|  ( )  ][  ( )  | {~~~~~~||~~~~~~} |  ( )  ][  ( )  |    () -------/ ()  |\n\
|_______][_______|        ||        |_______][_______|------/  ()   ][ () |\n\
|   _   ][   _   |        ||        |   _   ][   _   | ()   ][  ()   -----|\n\
|  ( )  ][  ( )  |        ||        |  ( )  ][  ( )  |   ()  -------/ ()  |\n\
|_______][_______|        ||        |_______][_______|------/  ()   ][ () |\n\
|   _   ][   _   |     () || ()     |   _   ][   _   | ()   ][  ()   -----|\n\
|  ( )  ][  ( )  |        ||        |  ( )  ][  ( )  |   ()  -------/ ()  |\n\
|_______][_______|        ||        |_______][_______|------/  ()   ][ () |\n\
|   _   ][   _   |        ||        |   _   ][       |  ()  ][   ()  -----|\n\
|  ( )  ][  ( )  |        ||        |  ( )  ][  ( )  |   ()  -------/  () |\n\
|_______][_______|________||________|_______][_______|------/ ()    ][ () |\n\
 \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@\_ () ][    () -----|\n\
  \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_   -------/ ()  |\n\
   \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\/   ()  ][ () |\n\
    \~@~@~@~@~@~@~@~@~@~\-----------\~@~@~@~@~@~@~@~@~@~@~@~@~\_  () -----|\n\
     \~@~@~@~@~@~@~@~@~@~\===========\~@~@~@~@~@~@~@~@~@~@~@~@~@~\--/ ()  |\n\
      \~@~@~@~@~@~@~@~@~@~\___________\~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_  ()|\n\
       \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\--|\n\
        \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~|\n\
         \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@|"),
    (7,"The room is covered in web and your way forward is obsucred.",web,"\
__________________________________________________________________________\n\
=================================================================    -----|\n\
=========================================================    -------/     |\n\
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$_____________------/       ][    |\n\
$$$$____]$______$][___$$__][_$$____][_$$    ][       |      ][       -----|\n\
$$$_$__$$$_____$_][__$$___]$$______]$$      ][       |       -------/     |\n\
$____$$$][$$$$_$_][_$$____$$_______$$_______][_______|------/       ][    |\n\
$$_$$_$$][__$$$$$$$__$____$[______$$[       ][       |      ][       -----|\n\
$$_$$___$$_$_____]$$$$$___]$______$$[       ][       |       -------/     |\n\
$___$$__$$$$_____$$____$$$$$$_____$$[_______][_______|------/       ][    |\n\
$__$$$$$][__$$__$][_____$$$$$$$$___$$       ][       |      ][       -----|\n\
$$$__$$_][___$$$$][__$$$$______$$$$]$$      ][       |       -------/     |\n\
$$____$$][$$$$$$$][__$____________$$$$$_____][_______|------/       ][    |\n\
$______$]$$______$$_$$__________$$$\        ][       |      ][       -----|\n\
$__$$$$$$$______$$$$$$________$$~~} |       ][       |       -------/     |\n\
$$$$____$$___$$$___$$$_______$$     |_______][_______|------/       ][    |\n\
$$______]$__$$________$$____$$      |       ][       |      ][       -----|\n\
$_______][$_$___________$$__$       |       ][       |       -------/     |\n\
$$__$$$$$$$$_____________$$_$       |_______][_______|------/       ][    |\n\
$_$$____][$$_______$$$$$$$$$$       |       ][       |      ][       -----|\n\
$$$_____][__$____$$$      ||        |       ][       |       -------/     |\n\
$$______][__$$___$        ||        |_______][_______|------/       ][    |\n\
$_______][___$__$$        ||        |       ][       |      ][       -----|\n\
$$__$$$$$$$$__$$$$        ||        |       ][       |       -------/     |\n\
$__$$___][_$$$$$__________||________|_______][_______|------/       ][    |\n\
 \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@\_    ][       -----|\n\
  \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_   -------/     |\n\
   \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\/       ][    |\n\
    \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_     -----|\n\
     \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~/ _ \~@~@~@~\--/     |\n\
      \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~~\_\(_)/_/~~@~@~@~\_    |\n\
       \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~~_//o\\_~~@~@~@~@~@~\--|\n\
        \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~~/ ~ \~~@~@~@~@~@~@~@~|\n\
         \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@|"),
    (8,"A fiend stands between you and the outside. Luckily you notice that there is a door back in to the dungeon across the hall.",outside,"\n\
⠀⠀⠀⠀⠀⣠⡀⠀⠙⢶⣦⣤⠀⠀⡀⢀⠀⠀⣤⣴⡶⠋⠀⢀⣄\n\
⠀⠀⢀⣠⡾⠋⠙⠷⣤⡀⠛⠋⣠⣿⣇⣸⣿⣄⠙⠛⢀⣤⠾⠋⠙⢷⣄⡀\n\
⠀⠀⣾⢋⣠⣶⠀⣦⣄⠙⠃⣸⣿⣿⣿⣿⣿⣿⣇⠘⠋⣠⣴⠀⣶⣄⡙⣷\n\
⠀⢸⣿⣿⣿⡟⢀⣿⣿⣿⠀⢿⣤⣈⡉⢉⣁⣤⡿⠀⣿⣿⣿⡀⢻⣿⣿⣿⡇\n\
⠀⢸⣿⣿⣿⣷⡾⠿⠿⠿⠓⠀⠛⠋⣁⣈⠙⠛⠀⠚⠿⠿⠿⢷⣾⣿⣿⣿⡇\n\
⠀⠘⣿⡟⠛⠟⠀⠀⠀⣴⣾⣿⣦⣈⣉⣉⣁⣴⣿⣷⣦⠀⠀⠀⠻⠛⢻⣿⠃\n\
⠀⠀⠹⠀⠀⠀⠀⠀⠀⢹⣿⣿⠛⣿⣿⣿⣿⠛⣿⣿⡏⠀⠀⠀⠀⠀⠀⠏⠀\n\
⠀⠀⠀⠀⠀⠀⠀⣠⣴⡀⢻⣿⡆⢸⣿⣿⡇⢰⣿⡟⢀⣦⣄\n\
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⠈⣿⡇⠀⣭⣭⠀⢸⣿⠁⣾⣿⡿\n\
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡇⢸⣿⠀⢻⡟⠀⣿⡇⢸⣿⡿⠁\n\
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⠘⣿⣇⠘⠃⣸⣿⠃⣿⡿⠁\n\
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣿⡄⢻⣿⡀⢀⣿⡟⢠⣿⣤⣀\n\
⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⠛⠁⠼⢿⡇⢸⡿⠧⠈⠛⠙⠂\n\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈"),
    (9,"On your left as you walk into the room there is a stall on your left.",stall,"\n\
   ______________________________ \n\
  /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\ \n\
 /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\ \n\
   ||V-V-V-V-V-V-V-V-V-V-V-V-V-||\n\
   ||            _             ||\n\
   ||           ( )            ||\n\
   ||____________X_____________||\n\
   ||==========================||\n\
   ||==========================||"),
    (10,"The room is empty with a door on the other side.",jam,"\
__________________________________________________________________________\n\
=================================================================    -----|\n\
=========================================================    -------/     |\n\
 _____________________________________________________------/       ][    |\n\
|       ][       ][       ][       ][       ][       |      ][       -----|\n\
|       ][       ][       ][       ][       ][       |       -------/     |\n\
|_______][_______][_______][_______][_______][_______|------/       ][    |\n\
|       ][       ][       ][       ][       ][       |      ][       -----|\n\
|       ][       ][       ][       ][       ][       |       -------/     |\n\
|_______][_______][_______][_______][_______][_______|------/       ][    |\n\
|       ][       ][     ______     ][       ][       |      ][       -----|\n\
|       ][       ][  ,-'|  |  `-.  ][       ][       |       -------/     |\n\
|_______][_______][_/{~~|  |~~~} \_][_______][_______|------/       ][    |\n\
|       ][        /{~~~~|  |~~~~~}'\        ][       |      ][       -----|\n\
|       ][       |{~~~~~|  |~~~~~~} |       ][       |       -------/     |\n\
|_______][_______|       | |        |_______][_______|------/       ][    |\n\
|       ][       |       | |        |       ][       |      ][       -----|\n\
|       ][       |       | |        |       ][       |       -------/     |\n\
|_______][_______|       | |        |_______][_______|------/       ][    |\n\
|       ][       |    () | | ()     |       ][       |      ][       -----|\n\
|       ][       |       | |        |       ][       |       -------/     |\n\
|_______][_______|       | |        |_______][_______|------/       ][    |\n\
|       ][       |       | |        |       ][       |      ][       -----|\n\
|       ][       |       | |        |       ][       |       -------/     |\n\
|_______][_______|_______| |________|_______][_______|------/       ][    |\n\
 \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@\_    ][       -----|\n\
  \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_   -------/     |\n\
   \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\/       ][    |\n\
    \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_     -----|\n\
     \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\--/     |\n\
      \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_    |\n\
       \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\--|\n\
        \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~|\n\
         \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@|"),
    (11,"A floc of birds fills the large room.",floc,"\n\
           /^v^\ \n\
    /^v^\                           /^v^\ \n\
            /^v^\          /^v^\  \n\
\n\
\n\
   ___     ___     ___     ___     ___ \n\
  (o o)   (o o)   (o o)   (o o)   (o o) \n\
 (  V  ) (  V  ) (  V  ) (  V  ) (  V  ) \n\
/--m-m--/--m-m--/--m-m--/--m-m--/--m-m-- \n\
  ")])

    current_room = 0
    room_count = 0
    start(rooms, items, inventory, current_room, room_count, user)


def enter(rooms, items, inventory, current_room, room_count, user):

    room_count = room_count + 1
    print(rooms[current_room][1], f"\nInventory:{inventory}\n", rooms[current_room][3])
    event(rooms, items, inventory, current_room, room_count, user)

def change_room(rooms, items, inventory, current_room, room_count, user):

    new_room = random.randint(1, (len(rooms) - 1))
    current_room = new_room
    enter(rooms, items, inventory, current_room, room_count, user)

def get_item(rooms, items, inventory, current_room, room_count, user):

    item = random.choice(items)
    print(f"You got a {item}.")
    inventory[item] = inventory[item] + 1
    if item == "Rusty Sword":
        print("\
               />\n\
 (           //-------------------------------------(\n\
(*)OXOXOXOXO(*>======================================\ \n\
 (            \---------------------------------------)\n\
               \>")
    elif item == "Rusty Armour":
        print("\
                     _,--~~--,_\n\
                   ,`          `,\n\
                  /              \ \n\
                 ,=_            _=,\n\
                 |  "'"'"_        _"'"'"  |\n\
                 |_   '"'"'"-..-"'"'"'   _|\n\
                 | "'"'"-.        .-"'"'" |\n\
                 |    "'"'"\    /"'"'"    |\n\
                 |      |  |      |\n\
         ___     |      |  |      |     ___\n\
     _,-"'"'",  "'"'",   '_     |  |     _'   ,"'"'"  ,"'"'"-,_\n\
   _(  \  \   \ =--"'"'"-.  |  |  .-"'"'"--= /   /  /  )_\n\
 ,"'"'"  \  \  \   \      "'"'"-'--'-"'"'"      /   /  /  /  "'"'".\n\
!     \  \  \   \       \  /       /   /  /  /     !\n\
:      \  \  \   \       \/       /   /  /  /      :")
    elif item == "Gold Coin":
        print("\
                     ______________\n\
         __,.,---'''''              '''''---..._\n\
      ,-'                  ____                 '`-,\n\
    /'                   //----\                    '\  \n\
  ;                      ||    ||                    '\  \n\
|'                       ||  | ||                       \n\
                         ||  | ||                       \n\
                         ||  | ||                       \n\
                         ||  | ||                      }\n\
                         ||  | ||                     ;\n\
                          \__|_//                    ,\n\
   \ -.._                  ----             __,,- -/\n\
      '-.._''`---.....______________.....---''__,,-\n\
          ''`---.....______________.....---''\n")

def event(rooms, items, inventory, current_room, room_count, user):

    rooms[current_room][2](rooms, items, inventory, current_room, room_count, user)

def empty(rooms, items, inventory, current_room, room_count, user):

    while True:
        ans = input("Do you want to go through the door.[y/n]:")
        if ans == "y":
            current_room = change_room(rooms, items, inventory, current_room, room_count, user)
            return current_room
        elif ans == "n":
            print("You have no choice.")
        else:
            print("You must type y or n.")

def cave(rooms, items, inventory, current_room, room_count, user):

    while True:
        ans = input("Do you want to go through the door.[y/n]:")
        if ans == "y":
            current_room = change_room(rooms, items, inventory, current_room, room_count, user)
            break
        elif ans == "n":
            out = input("Do you want to leave to the outside.[y/n]:")
            if out == "y":
                leave(rooms, items, inventory, current_room, room_count, user)
            elif out != "n":
                print("You must type y or n.")
        else:
            print("You must type y or n.")

def leave(rooms, items, inventory, current_room, room_count, user):

    db = SQL("sqlite:///adventure.db")
    rows = db.execute("SELECT * FROM users WHERE id = ?", user)
    high_score = rows[0]["high_score"]
    coins = rows[0]["Coins"]

    if current_room != 0 and current_room != 2:
        score = int(room_count) / 2
        print(f"Your time in the dungeon has come to an end (because of death).\nYou have a score of {score}")
        if score > high_score:
            new_highscore = db.execute("UPDATE users SET high_score = ? WHERE id = ?", score, user)
        start(rooms, items, inventory, current_room, room_count, user)
    else:
        score = int(room_count) + int(inventory["Gold Coin"])
        print(f"Your time in the dungeon has come to an end.\nYou have a score of {score}, your inventory had {inventory}.")
        add_coins = coins + int(inventory["Gold Coin"])
        new_coins = db.execute("UPDATE users SET Coins = ? WHERE id = ?", add_coins, user)
        if score > high_score:
            new_highscore = db.execute("UPDATE users SET high_score = ? WHERE id = ?", score, user)
            print("NEW HIGH SCORE")
        start(rooms, items, inventory, current_room, room_count, user)

def chest(rooms, items, inventory, current_room, room_count, user):

    while True:
        ans = input("Do you want to go through the door or open the chest. [d/c]:")
        if ans == "d":
            current_room = change_room(rooms, items, inventory, current_room, room_count, user)
            break
        elif ans == "c":
            trap = random.randint(1, 100)

            if trap >= 1:
                print("The chest was trapped. A green gass fills the air and enters your lungs. You look to the door you'll never enter as you fall gasping for your last breath.")
                leave(rooms, items, inventory, current_room, room_count, user)
            elif trap == 100:
                print("The chest had two items")
                get_item(rooms, items, inventory, current_room, room_count, user)

            get_item(rooms, items, inventory, current_room, room_count, user)

            ans = input("Do you want to go through the door.[y/n]:")
            ref_door(rooms, items, inventory, current_room, room_count, user, ans)
        else:
            print("You must type d or c.")

def first(rooms, items, inventory, current_room, room_count, user):

    while True:
        ans = input("Do you want to go through the door.[y/n]:")
        if ans == "y":
            current_room = change_room(rooms, items, inventory, current_room, room_count, user)
            break
        elif ans == "n":
            out = input("Do you want to leave.[y/n]:")
            if out == "y":
                leave(rooms, items, inventory, current_room, room_count, user)
            elif ans != "n":
                print("You must type y or n.")
        else:
            print("You must type y or n.")

def monster(rooms, items, inventory, current_room, room_count, user):

    if int(inventory["Rusty Sword"]) == 0 and int(inventory["Rusty Armour"]) == 0:
        print("The monster reaches across and grabs you in its hand. Your brief life flashes before your eyes as you look into the creatures gaping jaw closing on your head.")
        leave(rooms, items, inventory, current_room, room_count, user)

    elif int(inventory["Rusty Sword"]) != 0 and int(inventory["Rusty Armour"]) != 0:

        while True:
            option = input("Would you like to fight the monster or make a run for the door. [f/d]:")
            if option == "f":
                inventory["Rusty Sword"] = inventory["Rusty Sword"] - 1
                print("Your trusty rusty sword betrays you, breaking on first contact with the monster.\n\
Luckily the blade does enough damage to distract it, enough that you can make a brake for it.")

                while True:
                    ans = input("Do you want to go through the door.[y/n]:")
                    if ans == "y":
                        current_room = change_room(rooms, items, inventory, current_room, room_count, user)
                        break
                    elif ans == "n":
                        print("Get out of here the monster is still alive.")
                    else:
                        print("You must type y or n.")

            elif option == "d":
                inventory["Rusty Armour"] = inventory["Rusty Armour"] - 1
                print("You make a break for the door, the monster reaches towards you as you pass geting a hit in, your trusty armour breaks on first contact with the monster.\n\
Luckily the armour defends you enough that you make it to the door.")
                current_room = change_room(rooms, items, inventory, current_room, room_count, user)
            else:
                print("You must type f or d.")

    elif int(inventory["Rusty Sword"]) != 0 and int(inventory["Rusty Armour"]) == 0:
        print("You can use your sword to fight the monster")
        inventory["Rusty Sword"] = inventory["Rusty Sword"] - 1
        print("Your trusty rusty sword betrays you , breaking on first contact with the monster.\n\
Luckily the blade does enough damage to injure it enough that you can leave or finish it at leasure.")

        while True:
            ans = input("Do you want to go through the door.[y/n]:")
            if ans == "y":
                current_room = change_room(rooms, items, inventory, current_room, room_count, user)
                break
            elif ans == "n":
                print("Why, what are you planing on here?. The monster isn't dead you know.")
            else:
                print("You must type y or n.")

    elif int(inventory["Rusty Sword"]) == 0 and int(inventory["Rusty Armour"]) != 0:
        print("You hope your armour will defend you as you run to door")
        inventory["Rusty Armour"] = inventory["Rusty Armour"] - 1
        print("You make a break for the door, the monster reaches towards you as you pass geting a hit in, your trusty armour breaks on first contact with the monster.\n\
Luckily the armour defends you enough that you make it to the door.")
        current_room = change_room(rooms, items, inventory, current_room, room_count, user)

def choose(rooms, items, inventory, current_room, room_count, user):

    while True:
        ans = input("Do you want to take one. [y/n]:")
        if ans == "y":
            trap = random.randint(1, 100)

            if trap == 1:
                print("The plinth was trapped. The room fills with water, you try to swim to the top but you hit the ceiling.\n\
Changing tactic you head towards the door which turns out to be locked.\n\
You bang against the door in futility untill you can no longer help but gasp for breath.\nWater fills your lungs.\nYou drown.")
                leave(rooms, items, inventory, current_room, room_count, user)
            elif trap < 80:
                 print("The plinths slide into the floor.")
                 get_item(rooms, items, inventory, current_room, room_count, user)
                 ref_door(rooms, items, inventory, current_room, room_count, user, ans)
            elif trap >= 80:
                get_item(rooms, items, inventory, current_room, room_count, user)
                ans = input("Do you want to take another one. [y/n]:")
                if ans == "y":
                    trap = random.randint(1, 100)

                    if trap < 30:
                        print("The plinth was trapped. The room fills with water, you try to swim to the top but you hit the ceiling.\n\
Changing tactic you head towards the door which turns out to be locked.\n\
You bang against the door in futility untill you can no longer help but gasp for breath. Water fills your lungs. You drown.")
                        leave(rooms, items, inventory, current_room, room_count, user)
                    elif trap < 90:
                        print("The plinths slide into the floor.")
                        get_item(rooms, items, inventory, current_room, room_count, user)
                        ref_door(rooms, items, inventory, current_room, room_count, user, ans)
                    elif trap >= 30:
                        get_item(rooms, items, inventory, current_room, room_count, user)
                        ans = input("Do you want to take another one. [y/n]:")
                        if ans == "y":
                            trap = random.randint(1, 100)
                            if trap <= 70:
                                print("The plinth was trapped. The room fills with water, you try to swim to the top but you hit the ceiling.\n\
Changing tactic you head towards the door which turns out to be locked.\n\
You bang against the door in futility untill you can no longer help but gasp for breath. Water fills your lungs. You drown.")
                                leave(rooms, items, inventory, current_room, room_count, user)
                            elif trap > 70:
                                get_item(rooms, items, inventory, current_room, room_count, user)
                                ref_door(rooms, items, inventory, current_room, room_count, user, ans)

                        if ans == "n":
                            ref_door(rooms, items, inventory, current_room, room_count, user, ans)

                if ans == "n":
                    ref_door(rooms, items, inventory, current_room, room_count, user, ans)

        if ans == "n":
            ref_door(rooms, items, inventory, current_room, room_count, user, ans)

def arrow(rooms, items, inventory, current_room, room_count, user):
    while True:
        ans = input("Do you want to go move across the hall.[y/n]:")
        if ans == "y":
            print("Arrows fly at you from all directions out of the walls...")
            if int(inventory["Rusty Armour"]) == 0:
                print("they pierce your soft and vunerable skin.\nAs you lay bleeding on the floor you think that pressure plate on the floor was a trap after all.")
                leave(rooms, items, inventory, current_room, room_count, user)
            else:
                print("and ping uselessly against your trusty armour.\nAs the damage causes your armour to come apart around you you realise it might be best not to place to much trust in it after all.")
                inventory["Rusty Armour"] = inventory["Rusty Armour"] - 1
                while True:
                    ans = input("Do you want to go through the door.[y/n]:")
                    if ans == "y":
                        current_room = change_room(rooms, items, inventory, current_room, room_count, user)
                        break
                    elif ans == "n":
                        print("What, you want to collect the arrows?. The game doesnt let you do that.")
                    else:
                        print("You must type y or n.")

        elif ans == "n":
            print("The way back has been closed off. What are you afraid of anyway?")
        else:
            print("You must type y or n.")

def jam(rooms, items, inventory, current_room, room_count, user):
    while True:
        ans = input("Do you want open the door.[y/n]:")
        if ans == "y":
            print("its jammed...")
            if int(inventory["Rusty Sword"]) == 0:
                print("After being locked in the room for so long you bang your head against the door.\n\
The door opens but your head injury kills you.")
                leave(rooms, items, inventory, current_room, room_count, user)
            else:
                print("You use your sword to pry open the door breaking it in the process")
                inventory["Rusty Sword"] = inventory["Rusty Sword"] - 1
                while True:
                    ans = input("Do you want to go through the door.[y/n]:")
                    if ans == "y":
                        current_room = change_room(rooms, items, inventory, current_room, room_count, user)
                        break
                    elif ans == "n":
                        print("But you tried so hard to open it.")
                    else:
                        print("You must type y or n.")

        elif ans == "n":
            print("The way back has been closed off.")
        else:
            print("You must type y or n.")

def floc(rooms, items, inventory, current_room, room_count, user):

    if int(inventory["Rusty Armour"]) == 0:
        print("The tiny birds tiny beaks cut your exposed skin.\n\
You bleed to death before you make it to the door")
        leave(rooms, items, inventory, current_room, room_count, user)
    else:
        trap = random.randint(1, 100)
        ans = input("Do you want to go strait to the door or look around.[d/l]:")
        while True:
            if ans == "d":
                print("Your amour protects you from the flock as you walk to the door.")
                current_room = change_room(rooms, items, inventory, current_room, room_count, user)
                break
            elif ans == "l":
                if trap < 6:
                    print("You come across a nest, it's bigger than the others.\n\
Above you is the cry of a bird.\n\
You look up to see the massive talons of a massive bird come towards you.\n\
You stumble around blind and in pain untill eventualy colapsing.")
                    leave(rooms, items, inventory, current_room, room_count, user)
                elif trap > 50:
                    print("You come across a nest, it has an item.\n\
You leave after finding nothing else.")
                    get_item(rooms, items, inventory, current_room, room_count, user)
                    current_room = change_room(rooms, items, inventory, current_room, room_count, user)
                else:
                    print("You don't find anything and decide to leave.")
                    current_room = change_room(rooms, items, inventory, current_room, room_count, user)
            else:
                print("You must type d or l.")

def web(rooms, items, inventory, current_room, room_count, user):

    if int(inventory["Rusty Sword"]) == 0:
        print("You make your way into the room through the web.\n As you move forward the webs cling to you restricting your movement.\n\
You loose your way, eventualy turning back to make try and your way out of the web however becoming stuck in place.\n\
You notice a spider larger than your head aproaching from your right.\n Struggling, now in panic, has no effect as the creature draws closer.\n\
During your anguished cries of pain you spot the door two paces in front.\n If only you had made it a bit further.")
        leave(rooms, items, inventory, current_room, room_count, user)
    else:
        ans = input("Do you want to use your sword to clear the webs infront.[y/n]:")
        while True:
            if ans == "y":
                print("Webs fall as you swing your sword, covering the sword in webbing.\n\
A spider larger than your head falls from above and you beat it to death with your sword.\n Eventualy you clear enough web and manage to make it to the door.")
                current_room = change_room(rooms, items, inventory, current_room, room_count, user)
                break
            elif ans == "n":
                print("You make your way into the room through the web.\n As you move forward the webs cling to you restricting your movement.\n\
You loose your way, eventualy turning back to make try and make your way out of the web however become stuck in place.\n\
You notice a spider larger than your head aproaching from your right.\n Struggling, now in panic, has no effect as the creature draws closer.\n\
During your anguished cries of pain you spot the door two paces in front.\n If only you had used your sword fool.")
                leave(rooms, items, inventory, current_room, room_count, user)
            else:
                print("You must type y or n.")

def outside(rooms, items, inventory, current_room, room_count, user):
    trap = random.randint(1, 100)
    while True:
        ans = input("Would you like to try and make it outside or head for the door. [o/d]:")
        if ans == "o":
            if int(inventory["Rusty Sword"]) == 0 and int(inventory["Rusty Armour"]) == 0:
                if trap == 100:
                    print("As you walk past the fiend you realise it was just a statue.\n\
You look to the roling fields in front of you and contemplate how foolish it realy was to confront what you thought was a fiend with wout any wepons or armour.\n\
You take a deep breath and an large step.")
                    current_room = 0
                    leave(rooms, items, inventory, current_room, room_count, user)
                else:
                    print("The fiend pounces at you as you aproach. Without any means to defend yourself and counter attack you are easily killed.")
                    leave(rooms, items, inventory, current_room, room_count, user)

            elif int(inventory["Rusty Sword"]) != 0 and int(inventory["Rusty Armour"]) != 0:
                if trap == 100:
                    print("As you walk past the fiend you realise it was just a statue.\n You take a deep breath and an large step.")
                    current_room = 0
                    leave(rooms, items, inventory, current_room, room_count, user)
                else:
                    print("Your rusty armour allows you leaway to using your rusty sword to attack the fiend eventualy sending it back to wherever it came from.")
                    inventory["Rusty Sword"] = inventory["Rusty Sword"] - 1
                    inventory["Rusty Armour"] = inventory["Rusty Armour"] - 1
                    current_room = 0
                    leave(rooms, items, inventory, current_room, room_count, user)

            elif int(inventory["Rusty Sword"]) != 0 and int(inventory["Rusty Armour"]) == 0:
                if trap == 100:
                    print("As you walk past the fiend you realise it was just a statue.\n You take a deep breath and an large step.")
                    current_room = 0
                    leave(rooms, items, inventory, current_room, room_count, user)
                else:
                    print("You use your trusty sword to attack the fiend but it betrays you,\
 and without a means of defence the fiend takes to opportunity to collect your soul or somthing like that.")
                    inventory["Rusty Sword"] = inventory["Rusty Sword"] - 1
                    leave(rooms, items, inventory, current_room, room_count, user)

            elif int(inventory["Rusty Sword"]) == 0 and int(inventory["Rusty Armour"]) != 0:
                print("You hope your armour will defend you but without a means to a means to counter-attack\
 the fiend attacks you till your trusty armour breaks.\n\
The fiend proceeds to toy with your life as you imagine a cat might.\n\
Distracted by this thought you don't notice the obviously telegraphed attack which accidentily takes your life.")
                inventory["Rusty Armour"] = inventory["Rusty Armour"] - 1
                leave(rooms, items, inventory, current_room, room_count, user)
        elif ans == "d":
            if trap == 1:
                if int(inventory["Rusty Sword"]) == 0 and int(inventory["Rusty Armour"]) == 0:
                    print("The fiend approaches you from behind and merders you when you arn't looking.")
                    leave(rooms, items, inventory, current_room, room_count, user)
                elif int(inventory["Rusty Sword"]) != 0 and int(inventory["Rusty Armour"]) != 0:
                    print("You notice the fiend is coming for you anyway and manage to drive it back whith the combination of your trusty armour and weapon.")
                    while True:
                        opt = input("Do you want to continue through the door or leave the dungeon. [d/l]")
                        if opt == "d":
                            current_room = change_room(rooms, items, inventory, current_room, room_count, user)
                            break
                        elif opt == "l":
                                current_room = 0
                                leave(rooms, items, inventory, current_room, room_count, user)
                        else:
                            print("You must type d or l.")
                elif int(inventory["Rusty Sword"]) != 0 and int(inventory["Rusty Armour"]) == 0:
                    print("The fiend runs at you from behind. Without any armour to block its attack you die trying to run away.\n\
Perhaps it was bored or somthing")
                    leave(rooms, items, inventory, current_room, room_count, user)
                elif int(inventory["Rusty Sword"]) == 0 and int(inventory["Rusty Armour"]) != 0:
                    print("The fiend runs at you from behind and blocks of your way to the door\n\
Eventualy after destroying your armour the fiend becomes tired of playing with you and leaves\n\
You wearaly leave through the door hoping the fiend dosen't remember you.")
                    inventory["Rusty Armour"] = inventory["Rusty Armour"] - 1
                    current_room = change_room(rooms, items, inventory, current_room, room_count, user)
            else:
                print("You leave through the door")
                current_room = change_room(rooms, items, inventory, current_room, room_count, user)
        else:
            print("You must type o or d.")

def stall(rooms, items, inventory, current_room, room_count, user):

    while True:
        ans = input("Do you want to go through the door or talk to the guy at the stall. [d/s]:")
        if ans == "d":
            print("You turn around as get to the door.\n You are alone in the room.\n\
It's as if nothing was ever there.\n You quickly hurry into the next room.")
            current_room = change_room(rooms, items, inventory, current_room, room_count, user)
            break
        elif ans == "s":
            purchek = 0
            trap = random.randint(1, 100)
            print("The person on the stall silently looks at you as you approach.\n\
When you make to speak he cuts you of with a gesture and motions to his sign")

            if trap >= 50:
                print("Can exchange a sword or an armour set for a coin")

                if int(inventory["Rusty Sword"]) == 0 and int(inventory["Rusty Armour"]) == 0:
                    print("You don't seem to have anything to trade.")

                while int(inventory["Rusty Sword"]) != 0:
                    ans = input("Do you want to give him a sword.[y/n]:")
                    if ans == "y":
                        print("You hand over a rusty sword and he wordlesly places a coin in your hand")
                        inventory["Rusty Sword"] = inventory["Rusty Sword"] - 1
                        inventory["Gold Coin"] = inventory["Gold Coin"] + 1
                        print(f"\nInventory:{inventory}\n")
                        purchek = purchek + 1
                    elif ans == "n":
                        break
                    else:
                        print("You must type y or n.")

                while int(inventory["Rusty Armour"]) != 0:
                    ans = input("Do you want to give him a piece of armour.[y/n]:")
                    if ans == "y":
                        print("You hand over some rusty armour and he wordlesly places a coin in your hand")
                        inventory["Rusty Armour"] = inventory["Rusty Armour"] - 1
                        inventory["Gold Coin"] = inventory["Gold Coin"] + 1
                        print(f"\nInventory:{inventory}\n")
                        purchek = purchek + 1
                    elif ans == "n":
                        break
                    else:
                        print("You must type y or n.")

            else:
                print("Can exchange a coin for a sword or an armour set")

                if int(inventory["Gold Coin"]) == 0:
                    print("You seem to be too poor.")

                while int(inventory["Gold Coin"]) != 0:
                    ans = input("Do you want to buy a sword.[y/n]:")
                    if ans == "y":
                        print("You hand over a coin and he wordlesly places a rusty sword in your hand")
                        inventory["Rusty Sword"] = inventory["Rusty Sword"] + 1
                        inventory["Gold Coin"] = inventory["Gold Coin"] - 1
                        print(f"\nInventory:{inventory}\n")
                        purchek = purchek - 1
                    elif ans == "n":
                        break
                    else:
                        print("You must type y or n.")

                while int(inventory["Gold Coin"]) != 0:
                    ans = input("Do you want to buy a piece of armour.[y/n]:")
                    if ans == "y":
                        print("You hand over a coin and he wordlesly places some rusty armour in your hand")
                        inventory["Rusty Armour"] = inventory["Rusty Armour"] + 1
                        inventory["Gold Coin"] = inventory["Gold Coin"] - 1
                        print(f"\nInventory:{inventory}\n")
                        purchek = purchek - 1
                    elif ans == "n":
                        break
                    else:
                        print("You must type y or n.")

            print("You blink and are suddenly alone... ")
            if purchek == 0:
                print("Perhaps being in the dungeon has made you lonely.")
            elif purchek > 0:
                print("Only your lighter pack and shiny gold convince you somthing happend at all.")
            elif purchek > 0:
                print("Only your heavier pack and lack of gold convince you somthing happend at all.")

            ans = input("Do you want to go through the door.[y/n]:")
            ref_door(rooms, items, inventory, current_room, room_count, user, ans)
        else:
            print("You must type d or s.")


def ref_door(rooms, items, inventory, current_room, room_count, user, ans):

    if ans == "n":
        while True:
            ans = input("Do you want to go through the door.[y/n]:")
            if ans == "y":
                current_room = change_room(rooms, items, inventory, current_room, room_count, user)
            elif ans == "n":
                print("You plan on staying here till you starve?")
                ref_door(rooms, items, inventory, current_room, room_count, user, ans)
            else:
                print("You must type y or n.")
    elif ans == "y":
        print("You leave into the next room.")
        current_room = change_room(rooms, items, inventory, current_room, room_count, user)
    else:
        print("You must type y or n.")
        ans = input("Do you want to go through the door.[y/n]:")
        ref_door(rooms, items, inventory, current_room, room_count, user, ans)

def log_in():

    name = input("Type your username")

    pas = input("Type your password")

    # Query database for username
    rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

    # Ensure username exists and password is correct
    if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
        return apology("invalid username and/or password", 400)

def register():

    log_out()

    name = input("Choose a username")

    password = input("choose a password.\n Passwords must be at least 6 characters, contain at least 1 upper and at least 1 lower case letter and at leaast 1 number.\n Paswords musst be only contain alphanumeric characters.")
    x = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$", password)

def log_in():
    db = SQL("sqlite:///adventure.db")

    name = input("Type your username: ")

    password = getpass.getpass("Type your password: ")

    rows = db.execute("SELECT * FROM users WHERE username = ?", name)

    if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
        while True:
            a = input("invalid username and/or password register/try again. [r/t]: ")
            if a == "r":
                id = register()
                return id
                break
            elif a == "t":
                id = log_in()
                return id
                break
            else:
                print("Must input r or t")
    else:
        id = rows[0]["id"]
        return id

def register():
    db = SQL("sqlite:///adventure.db")

    name = input("Choose a username: ")

    x = None
    while x == None:
        password = getpass.getpass("choose a password.\nPasswords must be at least 6 characters, contain at least 1 upper and at least 1 lower case letter and at leaast 1 number.\nPaswords musst be only contain alphanumeric characters: ")
        x = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$", password)

    # Query database for username
    rows = db.execute("SELECT * FROM users WHERE username = ?", "username")

    # Ensure username exists and password is correct
    if len(rows) != 0:
        print("This username is already taken, try again.")
    else:
        hashed = generate_password_hash(password)

        new = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, hashed)
        # get "user_id"
        rows = db.execute("SELECT * FROM users WHERE username = ?", name)

        # Remember which user has logged in
        id = rows[0]["id"]
        return id

def log_out(user):
     while True:
        a = input("Would you like to log out.[y/n]: ")
        if a == "y":
            return 0
        elif a == "n":
            return user
        else:
            print("Must input y or n.")
def start(rooms, items, inventory, current_room, room_count, user):

    inventory = {
        "Rusty Sword": 1,
        "Rusty Armour": 1,
        "Gold Coin": 0
    }

    current_room = 0

    room_count = 0

    if user != 0:
        user = log_out(user)
    if user == 0:
        while True:
            a = input("Would you like to log in/register.[l/r]: ")
            if a == "l":
                user = log_in()
                break
            elif a == "r":
                user = register()
                break
    db = SQL("sqlite:///adventure.db")
    rows = db.execute("SELECT * FROM users WHERE id = ?", user)
    high_score = rows[0]["high_score"]
    coins = rows[0]["Coins"]
    print(f"You have a high score of {high_score}!")
    print(f"You have accumulated {coins} coins!")

    while True:
        a = input("Would you like to play/exit.[p/e]: ")
        if a == "p":
            enter(rooms, items, inventory, current_room, room_count, user)
            break
        elif a == "e":
            exit(0)

main()
