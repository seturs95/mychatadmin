Title: Bot Commands
Date: 2019-09-05
Category: Support

### Basic information

Commands can be send either via direct message or via group chat. In the following document, they are grouped by "DM" commands and "Group" commands.
At the moment, the bot only interacts with group admins. If the bot does not respond to your commands, make sure, you are owner or admin of the group you are in.

All commands are case insensitive and whitespaces are irgnored.

### DM commands
* `friend`
   The bot will add you to his "friendlist". This is necessary for you to add the bot to your groups.  

* `help`
   The bot will show you a short help with commands it is currently able to execute.  


### Group commands
* `kick mode on`
   Defaults to "on"      
   Enable auto kicking of inactive members. Kicking starts at the specified cap set by `kick mode <number>`  

* `kick mode off`
   Disables all automatic kicking.  

* `kick mode <number>`
   Defaults to "48"  
   Start kicking inactive members after the member count reached <number>.   
   Example: Start kicking after 48 Users joined the group `kick mode 48`    

* `kick mode ban`
   Defaults to "kick"  
   Instead if just kicking inactive people, ban them.  

* `kick mode kick`
   Kick inactive people from your group  

* `kick message <on|off>`
   Turns on or off the kick message. Default is `There are more users in this group than expected. Removing inactive users.`

* `kick message <message>`
   Customize your kick message

* `welcome message <on|off>`
   Turns on or off the welcome message. This will be sent to everyone joining the group.

* `welcome message <message>`
   Customize your welcome message

* `clean`
   Kick or ban the 5 least active members manually.   
