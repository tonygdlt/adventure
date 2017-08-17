v1.20 July 26 - add quit, fix room connection during setup
<br>
v1.21 July 26 - revise frontyard.json and add rock.json. Stuff class has a new attribute "relatedItems" to indicate relationship between items, such as key in the fake rock. Room class has a new "hidden" attribue to identify which item is hidden.<br>
v1.22 July 27 - add items to foyer. revise "look at" parsing method for two-words items. fix bug in "go [direction]" command, causing player moving 2 rooms in a row<br>
v1.23 July 30 - fixed room loading for room in the west. Added the door lock in Porch room, requiring the key hidden in the fake rock in front yard to open it. Added more rooms and items.<br>
v1.24 Aug 7th - merge penny's works. merge Anthony's works. fix bugs caused by integration.<br>
v1.25 Aug 13th - fix key.json for available verb<br>
v1.25 Aug 14th - Add upstairs window to front yard. Add description about family to picture. Add dining room, kitchen, living room, basement, bathroom, backyard, shed and the related objects. Add loading items from files. <br>
v1.26 Aug 15th - Edit parsing system to handle 'go + adjective + room', 'adjective + room'<br>
v1.27 Aug 16th - Merge Anthony's works. Connect all the rooms 1-15 in the document <em>Storyline Progress.</em> Add go upstairs and downstairs behavior in game engine.<br>
v1.28 Aug 16th - Temporarily put necklace and doll in upstairs hallway. journal in master bedroom. Tested if taking all three objects and dropping them in the hidden room, the player wins the game.<br>
v1.29 Aug 17th - Merge Anthony's works.<br>
v1.30 Aug 17th - Merge Penny's works.<br>
v1.31 Aug 17th - Rollback to previous state at v1.28 since the game does not function properly.<br>
v1.32 Aug 17th - Fix bugs occur when player taking items other than key and and when the game engine accessing non-existent attribute game.bedroomUnlocked<br>
v1.33 Aug 17th - Fix bugs regarding accessing non-existent attribute. Put crowbar in tool box, doll in backyard, necklace in the basement. Tested that user can win after following the instructions in the Progression.doc.<br>
v1.34 Aug 17th - Fix bugs regarding moving two rooms in a row. Player can use "go upstairs" or "go downstairs" between Basement and Kitchen. Tested that user can win after following the instructions in the Progression.doc.<br>
v1.35 Aug 17th - Fix bug regarding moving two rooms in a row using direction command such as "north".