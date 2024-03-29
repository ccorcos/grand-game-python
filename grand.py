import random
import web




dem0 = """(Card 1).  No elections held this year.  Domestic tranquility.  Obtain 3 Francs.
(Card 2).  Minor corruption trials related to weapons programs.  Lose 2 Francs to hush it up unless you had more atomic research (at the end of your previous turn) than any other player.  
(Card 3).  Success buys tranquility.  If you have full possession of more economic zones than with which you began the game, obtain 1 Franc.  Otherwise, lose 1 Franc.  
(Card 4).  Retrospective voting.  If GDP increased over the turn, face no negative political consequences.  Otherwise, pay 5 Francs.
(Card 5).  Peace dividends.  If you took no casualties over the last year, obtain 5 Francs.  Otherwise, pay 5 Francs.
(Card 6).  Peace Party obtain majority.  Military units abroad not returned within your original boundaries by the end of the following winter are disbanded.  
(Card 7).  Isolationists obtain majority.  You may not attack the units of any power in the next turn unless you either (a) fought units of that power in this last turn or (b) are attacked by units of that power.
(Card 8).  Idealists obtain majority.  Your units may not fight in allied combinations with dictatorships for two full turns (display this card over that entire period; may be canceled by subsequent political cards).
(Card 9).  Anti-Imperialists demand recognition of national independence movements.  Any territories acquired through the action of the league of nations on your part must be returned to independence and neutrality - including any units currently in those territories that belong to you.  Allied units are evacuated to their nearest exit point or sold back to the bank for 1 Franc each.
(Card 10).  Anti-communists gain a majority.  Your units may not fight in conjunction in the next year with any Democracy or Dictatorship that spent more than 10\% on politics in this year.
(Card 11).  Peace Party defeats defense budget.  You may not spend anything on military units, supplies, or atomic development in this upcoming turn.  You must spend 30\% of your budget on politics.  You must spend as much as you can on economic development.  Any unspent GDP (due to costs of development) is simply lost.
(Card 12).  Hawks defeat budget.  You must spend your entire budget on military units and supplies.
(Card 13).  Government gridlock.  You repeat your expenditures by category from the previous year (so, same amount for military units, supplies, politics, atomic research, and development).  Anything not obtainable is lost.
(Card 14).  The Coburn Committee seeks to eliminate waste, fraud, and abuse; you may not make any political spending for the next turn.  Additionally, lose 5 Francs.
(Card 15).  Payoffs to Tammany Hall.  Spend 50 percent of your GDP on politics to obtain the 30\% outcome - or lose 20 Francs at the end of the next turn.  Keep this card out (decide privately).  
(Card 16).  War Party Takes Control of Parliament.  If any of your territories are adjacent to a neutral territory, you must invade it or pay 10 Francs per combat season (paid once orders are revealed in that season) in which this action does not take place.
(Card 17).  Idealist Fanatics demand that the world be made safe for Democracy!  If you do not occupy a city of a foreign dictatorship within the next two turns (six combat seasons), lose 20 Francs.  Void if canceled by subsequent political card or the end of the game.  Keep this card on the table.       
(Card 18).  Isolationists Force Exit from League of Nations.  You may not participate in the League of Nations for the next two turns.  Keep this card out on the table.
(Card 19).  Parliament Favors Internationalists.  For the remainder of the game, you may only invade a foreign country to conquer it with a majority vote in the League of Nations (vote taken after orders issued; if failed, orders do not execute and units defend).  Pay each nation, other than the one you are invading, 3 Francs for the privilege of holding the vote, regardless of the outcome.
(Card 20).  Parliament Favors League of Democracies.  For the remainder of the game, you may only initiate hostilities with a foreign power if all the Democracies unanimously consent.  Must obtain consent after orders have been issued; if withheld, orders do not execute and units defend.     
(Card 21).  Atomic Protestors Win Vote in Congress.  Although you may develop the atomic bomb, you may not use it in this game.
(Card 22).  Dissatisfied Socialists Leak Secrets.  One nation is chosen at random: if you have more atomic research than they do, a spy brings their research up to your level.  
(Card 23).  Independence Vote Successful.  One of your economic zones (other than those with which you began the game with full control), chosen at random, votes for independence.  All units, supplies, and development in that territory becomes part of an independent neutral country.
(Card 24).  Anti-War Protestors weaken army.  All armor and infantry units fight at a combat value of 1 in the next turn (if fully supplied) and a combat value of .5 if unsupplied.  
(Card 25).  Anti-War Protestors prevent recruitment.  All infantry units slated to be produced this turn refuse to enlist and are disbanded."""




dem10 = """(Card 1): No elections held this year.  Obtain an additional 3 Francs.
(Card 2):  Peace Party offers conditional support.  If in your last turn you purchased no additional atomic research, obtain 2 Francs.  Otherwise, nothing happens.
(Card 3): Military Success Bonus.  If your frontiers have expanded since the start of the game, obtain 1 additional Franc.
(Card 4): Retrospective Voting.  If GDP increased over the last turn, obtain 5 additional Francs.  If not, lose 2 Francs.
(Card 5): Peace Dividends.  If you took no casualties over the last tun, obtain 5 additional Francs.  Otherwise, lose 2 Francs.  
(Card 6): Peace Party makes gains in legislature.  If combat took place over the last turn involving your units, pay 5 Francs.    
(Card 7).  Isolationists obtain majority.  You may not attack the units of any power in the next turn unless you either (a) fought units of that power in this last turn or (b) are attacked by units of that power.
(Card 8).  Idealists make gains in legislature.  Your units may not fight in allied combinations with dictatorships for one full turn unless you pay 1 Franc per combat season in which they fight.  
(Card 9).  Anti-Imperialists demand recognition of national independence movements.  Any territories acquired through the action of the league of nations on your part must be returned to independence and neutrality if the league votes on their independence and pays at least 1 Franc per unit in the territories.  Your units and allied units are evacuated to their nearest exit point or sold back to the bank for 1 Franc each.
(Card 10).  Anti-communists gain a majority.  Your units may not fight in conjunction in the next year with any Democracy or Dictatorship that spent more than 10\% on politics in this year.
(Card 11).  Peace Party defeats defense budget.  You may not purchase any additional military units in the upcoming turn although you may purchase supplies.  
(Card 12).  Hawks insist on the construction of two heavy fleets.  You must comply if your budget allows and you have port facilities.  If you do not have port facilities, pay 2 Francs.  If you have ports but your budget does not allow the construction of two heavy fleets, pay 5 Francs.   
(Card 13).  Government gridlock.  You must produce precisely the same military units this year as you produced last year.  
(Card 14).  The Coburn Committee finds waste, fraud, and abuse.  You may not spend more than 10\% on politics in the next year and you must pay 4 Francs immediately to the bank.  
(Card 15).  Payoffs to Tammany Hall.  Spend 50 percent of your GDP on politics to obtain the 30\% outcome - or lose 5 Francs at the end of the next turn.  Keep this card out (decide privately).  
(Card 16).  War Party Takes Control of Parliament.  If any of your territories are adjacent to a neutral territory, you must invade it or pay 3 Francs per combat season (paid once orders are revealed in that season) in which this action does not take place.
(Card 17).  Idealist Fanatics demand that the world be made safe for Democracy!  If you do not occupy a city of a foreign dictatorship within the next two turns (six combat seasons), lose 20 Francs.  Void if canceled by subsequent political card or the end of the game.  Keep this card on the table.       
(Card 18).  Isolationists Force Exit from League of Nations.  You may not participate in the League of Nations for the next two turns.  Keep this card out on the table.
(Card 19).  Parliament Favors Internationalists.  For the remainder of the game, you may only invade a foreign country to conquer it with a majority vote in the League of Nations (vote taken after orders issued; if failed, orders do not execute and units defend).  Pay each nation, other than the one you are invading, 3 Francs for the privilege of holding the vote, regardless of the outcome.
(Card 20).  Parliament Favors League of Democracies.  For the remainder of the game, you may only initiate hostilities with a foreign power if all the Democracies unanimously consent.  Must obtain consent after orders have been issued; if withheld, orders do not execute and units defend.     
(Card 21).  Atomic Protestors Win Vote in Congress.  Although you may develop the atomic bomb, you may not use it in this game.
(Card 22).  Dissatisfied Socialists Leak Secrets.  One nation is chosen at random: if you have more atomic research than they do, a spy brings their research up to your level.  
(Card 23).  Surprise victory in a midterm election.  You may pay 1 Franc to remove the effects of any previous political card (of yours) currently operating against you.  You must decide now.  
(Card 24).  Anti-War Protestors weaken army.  All armor and infantry units fight at a combat value of 1 in the next turn (if fully supplied) and a combat value of .5 if unsupplied.  
(Card 25).  Anti-War Protestors prevent recruitment.  All infantry units slated to be produced this turn refuse to enlist and are disbanded."""


dem20 = """(Card 1): No elections held this year.  Obtain an additional 3 Francs.
(Card 2):  Peace Party offers conditional support.  If in your last turn you purchased no additional atomic research, obtain 3 Francs.  Otherwise, nothing happens.
(Card 3): Military Success Bonus.  If your frontiers have expanded since the start of the game, obtain 5 additional Francs.
(Card 4): Retrospective Voting.  If GDP increased over the last turn, obtain 5 additional Francs.  If not, lose 1 Franc.  
(Card 5): Peace Dividends.  If you took no casualties over the last turn, obtain 7 additional Francs.  Otherwise, lose 1 Franc.    
(Card 6): Peace Party makes gains in legislature.  If combat took place over the last turn involving your units, pay 3 Francs.    
(Card 7).  Isolationists obtain majority.  You may not attack the units of any power in the next turn unless you either (a) fought units of that power in this last turn or (b) are attacked by units of that power.
(Card 8).  Idealists make gains in legislature.  Your units may not fight in allied combinations with dictatorships for one full turn unless you pay 1 Franc per combat season in which they fight.  
(Card 9).  Propaganda Victory.  For every vote at the League of Nations this turn, each of your Francs counts as two.   
(Card 10).  Anti-communists gain a majority.  Your units may not fight in conjunction in the next year with any Democracy or Dictatorship that spent more than 10\% on politics in this year unless you pay 2 Francs for the turn (now).   
(Card 11).  Peace Party defeats defense budget.  You may not purchase any armor or heavy fleets in this turn.  
(Card 12).  Navy advocates insist on the construction of one heavy fleet.  If you do not comply, or cannot comply, lose 2 Francs.  Keep this card on the table.       
(Card 13).  Government gridlock.  You must produce precisely the same military units this year as you produced last year.  
(Card 14).  The Coburn Committee finds waste, fraud, and abuse.  You may not spend more than 10\% on politics in the next year and you must pay 4 Francs immediately to the bank.  
(Card 15).  War enthusiasm lowers infantry cost by 1 pound per unit this turn.    
(Card 16).  War Party Takes Control of Parliament.  If any of your territories are adjacent to a neutral territory, you must invade it or pay 1 Franc per combat season (paid once orders are revealed in that season) in which this action does not take place.
(Card 17).  Idealist Fanatics demand that the world be made safe for Democracy!  If you do not occupy a city of a foreign dictatorship within the next two turns (six combat seasons), lose 10 Francs.  Void if canceled by subsequent political card or the end of the game.  Keep this card on the table.       
(Card 18).  Isolationists Wish to Exit from League of Nations.  If you leave the League of Nations for the next two turns, collect 5 Francs.  Keep this card out on the table.
(Card 19).  Parliament Favors Internationalists.  For the next turn, you may only invade a foreign country to conquer it with a majority vote in the League of Nations (vote taken after orders issued; if failed, orders do not execute and units defend).  Pay each nation, other than the one you are invading, 3 Francs for the privilege of holding the vote, regardless of the outcome.
(Card 20).  Parliament Favors League of Democracies.  For the next turn, you may only initiate hostilities with a foreign power if all the Democracies unanimously consent.  Must obtain consent after orders have been issued; if withheld, orders do not execute and units defend.     
(Card 21).  Atomic Protestors Win Vote in Congress.  Although you may develop the atomic bomb, you may not use it in this game.
(Card 22).  Dissatisfied Socialists Leak Secrets.  One nation is chosen at random: if you have more atomic research than they do, a spy brings their research up to your level.  
(Card 23).  Surprise victory in a midterm election.  You may pay 1 Franc to remove the effects of any previous political card (of yours) currently operating against you.  You must decide now.  
(Card 24).  Anti-War Protestors weaken army.  All armor and infantry units fight at a combat value of 2 in the next turn (if fully supplied) and a combat value of 1 if unsupplied.  
(Card 25).  Anti-War Protestors increase the cost of recruitment.  Infantry and Armor units cost an additional pound this turn."""

dem30 = """(Card 1): No elections held this year.  Obtain an additional 5 Francs.
(Card 2):  Form national government.  In the next political cycle, obtain 30\% payout in Francs but retain the GDP and draw no political cards.  
(Card 3): Military Success Bonus.  If your frontiers have expanded since the start of the game, obtain 5 additional Francs.
(Card 4): Retrospective Voting.  If GDP increased over the last turn, obtain 5 additional Francs.  If not, lose 1 Franc.  
(Card 5): Peace Dividends.  If you took no casualties over the last turn, obtain 10 additional Francs.
(Card 6): Peace Party makes gains in legislature.  If combat took place over the last turn involving your units, pay 3 Francs.    
(Card 7).  Isolationists obtain majority.  You may not attack the units of any power in the next turn unless you either (a) fought units of that power in this last turn or (b) are attacked by units of that power.
(Card 8).  Idealists make gains in legislature.  Your units may not fight in allied combinations with dictatorships for one full turn unless you pay 1 Franc per combat season in which they fight.  
(Card 9).  Propaganda Victory.  For every vote at the League of Nations this turn, each of your Francs counts as two.   
(Card 10).  Anti-communists ask you to form dictatorship.  Obtain one-time payout of 15 Francs and then play the rest of the game as a dictator if you choose.  Otherwise, obtain a one-time payout of 20 Francs.   
(Card 11).  Peace Party defeats defense budget.  You may not purchase any armor or heavy fleets in this turn.  
(Card 12).  Navy advocates insist on the construction of one heavy fleet.  If you pay 2 Francs now, you may produce the fleet at a 5 pound discount.  If you do not produce the fleet by the end of the next turn, pay 1 Franc.          
(Card 13).  Government gridlock.  You must produce precisely the same military units this year as you produced last year.  
(Card 14).  The Coburn Committee suspends operation because Senator Coburn dies of a heart attack.  Obtain 3 Francs.  
(Card 15).  War enthusiasm lowers infantry and armor costs by 1 pound per unit this turn.    
(Card 16).  War Party Takes Control of Parliament.  If any of your territories are adjacent to a neutral territory, you must invade it or pay 1 Franc per combat season (paid once orders are revealed in that season) in which this action does not take place.
(Card 17).  Idealist Fanatics demand that the world be made safe for Democracy!  If you do not occupy a city of a foreign dictatorship within the next turn, lose 5 Francs.         
(Card 18).  Isolationists Wish to Exit from League of Nations.  If you leave the League of Nations for the next two turns, collect 5 Francs.  Keep this card out on the table.
(Card 19).  Parliament Favors Internationalists.  For the next turn, you may only invade a foreign country to conquer it with a majority vote in the League of Nations (vote taken after orders issued; if failed, orders do not execute and units defend).  Pay each nation, other than the one you are invading, 1 Franc for the privilege of holding the vote, regardless of the outcome.
(Card 20).  Parliament Favors League of Democracies.  For the next turn, you may only initiate hostilities with a foreign power if all the Democracies unanimously consent.  Must obtain consent after orders have been issued; if withheld, orders do not execute and units defend.     
(Card 21).  Atomic Protestors Win Vote in Congress.  Although you may develop the atomic bomb, you may not use it in this game.
(Card 22).  Dissatisfied Socialists Leak Secrets.  One nation is chosen at random: if you have more atomic research than they do, a spy brings their research up to your level.  
(Card 23).  Surprise victory in a midterm election.  You may pay 1 Franc to remove the effects of any previous political card (of yours) currently operating against you.  You must decide now.  
(Card 24).  Anti-War Protestors shot by national guard.  Pay 1 Franc.    
(Card 25).  Anti-War Protestors increase the cost of recruitment.  Infantry and Armor units cost an additional pound this turn. """ 

dic0 = """(Card 1).  War Weariness.  Lose 3 Francs if you do not possess all of your original territories.  Otherwise, nothing happens.    
(Card 2).  Disturbances in Captured Cities.  Lose 1 Franc for every city beyond your initial territory that you currently occupy.  
(Card 3).   Major Riot in Capital.  Lose 2 Francs.  May substitute 4 supplies (if available in one of your original cities) if you wish.
(Card 4).   Show Trial Poorly Received.  The witnesses were too sympathetic.  Pay 2 Francs.
(Card 5).   Minor Underground activity.  Remove two supplies (you choose) from territories behind your original borders (if you have any).
(Card 6).  Briefcase Bomb Plot.  You are disabled in a bombing at headquarters and subsequently execute a top general.  Blitzkrieg orders are no longer available to you in the subsequent turn.
(Card 7).  Major Coup Attempt!  The subsequent fighting consumes all of the new production - supplies and units - from one of the cities in your home territories (chosen randomly). 
(Card 8).  Air Chief Defects.  Remove one of your air units from the map (chosen by you).  
(Card 9).  Oligarchs Assert Power.  Unless you have conquered and control two full economic zones beyond your initial borders (as of drawing this card), you must pay the oligarchs (the bank) 15 Francs the next time you conquer a new territory (after a successful invasion, during that combat phase).  This card lasts until canceled by some other card or the action is fulfilled.   
(Card 10).  Assassin Hits Mark.  Fortunately, Mark is merely your twin brother.  Military units in your home territories all participate in the hunt for the killer - and use one supply each (drawn from anywhere in your home territories; you choose).  
(Card 11).  John has a Long Mustache.  Resistance fighters destroy railways in foreign territories occupied by you.  For the next turn, you may not move units or supplies by rail outside of your home territories.
(Card 12).  Resistance Proclaims Independence!  A full economic zone outside your home territories, chosen randomly, becomes neutral and obtains 5 neutral infantry placed in some random territory of that province.  The League of Nations will vote for control of those armies immediately; it requires only 3 Francs total contribution to control.  If League fails to vote to secure the armies, remove both the neutral infantry and three of your own units in the economic zone from the board.       
(Card 13).  Terrorism Damages Economy.  All economic zones lose one unit of added GDP (effective immediately).
(Card 14).  Ghetto Uprising!  Choose randomly among cities you have captured.  If the city is garrisoned with less than 3 units, it proclaims neutrality and adds 3 infantry.  The League of Nations votes immediately for control.  Your units evacuate to an adjacent territory that you control (if impossible, your units are lost).  If the League fails to provide 3 Francs, the freedom fighters disappear from the map.
(Card 15).  Guerilla's Plot to Aid Invaders.  Keep this card out until canceled otherwise.  Choose a province randomly.  Within that province, Democracies draw one extra combat card in combats.  
(Card 16).  Low Morale.  Enlistees seek to dodge the draft.  Infantry and armor costs increase by 1 Pound for this next allocation phase.
(Card 17).  Political Corruption Damages Your Supply Chain.  In every location you have ordered new supplies produced, 3 less supplies are actually produced than ordered in this turn. 
(Card 18).  Weapons Program Corruption.  Your nuclear scientists have been lying to you.  Your nuclear progress is actually... 0, including any production ordered this turn.
(Card 19).  Work Camps Produce Poor Ammunition.  Supplies cost 2 pounds this turn.
(Card 20).  Lack of Freedom Damages Economic Growth.  Remove 2 (added) GDP points from all of your fully conquered economic zones.
(Card 21).  Navy Avoids Battle.  Your poorly paid admirals all choose "hide" for all combat phases during the next turn rather than risk their lives for you.   
(Card 22).  Political Generals Are Idiots.  Your generals were appointed by their connections rather than by their merits.  In all land combats during the next turn, draw at most one combat card.
(Card 23).  Massive Supply Theft!  Remove ten supplies from your stocks currently on the board.  While you shoot those responsible, unfortunately it is impossible to locate the lost goods.
(Card 24).  Low Infantry Morale.  With idiots like you in charge, the war is hopeless.  Who wants to be the last to die in a lost cause?  Fully supplied infantry in the next turn fight at (1 attack, 2 defense); unsupplied infantry fight at (0 attack, 1 defense).  
(Card 25).  Bagdad Bob.  If you have lost any of your starting territory, lose 15 Francs for the embarrassment."""

dic10 = """(Card 1).  War Weariness.  Lose 3 Francs if you do not possess all of your original territories.  Otherwise, nothing happens.    
(Card 2).  Disturbances in Captured Cities.  Lose 1 Franc for every city beyond your initial territory that you currently occupy.  
(Card 3).   Major Riot in Capital.  Lose 2 Francs.  May substitute 4 supplies (if available in one of your original cities) if you wish.
(Card 4).   Show Trial Poorly Received.  The witnesses were too sympathetic.  Pay 2 Francs.
(Card 5).   Minor Underground activity.  Remove two supplies (you choose) from territories behind your original borders (if you have any).
(Card 6).  Briefcase Bomb Plot.  You are disabled in a bombing at headquarters and subsequently execute a top general.  Blitzkrieg orders are no longer available to you on this turn.  
(Card 7).  Major Coup Attempt!  The subsequent fighting consumes all of the new production - supplies and units - from one of the cities in your home territories (chosen randomly). 
(Card 8).  Air Chief Defects.  Remove one of your air units from the map (chosen by you).  
(Card 9).  Oligarchs Assert Power.  Unless you have conquered and control two full economic zones beyond your initial borders (as of drawing this card), you must pay the oligarchs (the bank) 10 Francs the next time you conquer a new territory (after a successful invasion, during that combat phase).  This card lasts until canceled by some other card or the action is fulfilled.   
(Card 10).  Assassin Hits Mark.  Fortunately, Mark is merely your twin brother.  Military units in your home territories all participate in the hunt for the killer - and use one supply each (drawn from anywhere in your home territories; you choose).  
(Card 11).  John has a Long Mustache.  Resistance fighters destroy railways in foreign territories occupied by you.  For the next turn, you may not move units or supplies by rail outside of your home territories.
(Card 12).  Resistance Proclaims Independence!  A full economic zone outside your home territories, chosen randomly, becomes neutral and obtains 5 neutral infantry placed in some random territory of that province.  The League of Nations will vote for control of those armies immediately; it requires only 3 Francs total contribution to control.  If League fails to vote to secure the armies, remove both the neutral infantry and three of your own units in the economic zone from the board.       
(Card 13).  Terrorism Damages Economy.  All economic zones lose one unit of added GDP (effective immediately).
(Card 14).  Ghetto Uprising!  Choose randomly among cities you have captured.  If the city is garrisoned with either no units or only one unit, it proclaims neutrality and adds 3 infantry.  The League of Nations votes immediately for control.  Your unit evacuates to an adjacent territory that you control (if impossible, your unit is lost).  If the League fails to provide 3 Francs, the freedom fighters disappear from the map.
(Card 15).  Guerilla's Plot to Aid Invaders.  Choose a province randomly.  Within that province, Democracies draw one extra combat card in combats on this turn.   
(Card 16).  Low Morale.  Enlistees seek to dodge the draft.  Infantry and armor costs increase by 1 Pound for this next allocation phase.
(Card 17).  Political Corruption Damages Your Supply Chain.  In every location you have ordered new supplies produced, 2 less supplies are actually produced than ordered in this turn. 
(Card 18).  Weapons Program Corruption.  Your nuclear scientists have been lying to you.  Your nuclear progress is actually... 0, including any production ordered this turn.
(Card 19).  Work Camps Produce Poor Ammunition.  Supplies cost 2 pounds this turn.
(Card 20).  Lack of Freedom Damages Economic Growth.  Remove 1 (added) GDP point from all of your fully conquered economic zones.
(Card 21).  Obtain intelligence of uprising; spectacular show trials increase support.  Obtain 2 additional Francs.  
(Card 22).  Political Generals Are Idiots.  Your generals were appointed by their connections rather than by their merits.  In all land combats during the next turn, draw at most one combat card.
(Card 23).  Massive Supply Theft!  Remove 5 supplies from your stocks currently on the board.  While you shoot those responsible, unfortunately it is impossible to locate the lost goods.
(Card 24).  Low Infantry Morale.  With idiots like you in charge, the war is hopeless.  Who wants to be the last to die in a lost cause?  Fully supplied infantry in the next turn fight at (1 attack, 2 defense); unsupplied infantry fight at (0 attack, 1 defense).  
(Card 25).  Bagdad Bob.  If you have lost any of your starting territory, lose 10 Francs for the embarrassment.     
"""

dic20 = """(Card 1).  War Weariness.  Lose 1 Franc if you do not possess all of your original territories.  Otherwise, nothing happens.    
(Card 2).  Disturbances in Captured Cities easily contained.  Nothing happens.    
(Card 3).  Opposition figure caught in bed with "dead girl or live boy."  Gain 5 Francs.   
(Card 4).   Show Trial Poorly Received.  The witnesses were too sympathetic.  Pay 1 Franc.
(Card 5).   Minor Underground activity.  Remove two supplies (you choose) from territories beyond your original borders (if you have any).
(Card 6).  Briefcase Bomb Plot Fails.  You are disabled in a bombing at headquarters and subsequently execute a top general.  Pay 1 Franc to smooth things over.  Wipes away any negative political cards still in effect.    
(Card 7).  Major Coup Attempt Caught!  Obtain two additional Francs from selling the plotter's stolen art collections.  Wipes away any negative political cards still in effect. 
(Card 8).  Air Chief Defects.  Remove one of your air units from the map (chosen by you).  
(Card 9).  Key opposition figure "has accident."  Gain 3 Francs.   
(Card 10).  Assassin Hits Mark.  Fortunately, Mark is merely your twin brother.  Gives you an excuse to round up the usual suspects.  Obtain 1 Franc.  
(Card 11).  John has a Long Mustache.  Resistance fighters destroy railways in foreign territories occupied by you.  For the next turn, you may not move units or supplies by rail outside of your home territories.
(Card 12).  Resistance Movement Betrayed.  All attempts to destabilize your government fail; nothing happens.         
(Card 13).  Terrorism Damages Economy.  All economic zones lose one unit of added GDP (effective immediately).
(Card 14).  Ghetto Uprising Crushed!  You lose one supply (from anywhere, your choice) but obtain 3 Francs.  
(Card 15).  Guerilla's Plot to Aid Invaders.  Choose a province randomly.  Within that province, Democracies draw one extra combat card in combats on this turn.   
(Card 16).  Youth program success!  Obtain an extra infantry unit that may be placed in any of your original cities (immediately).  
(Card 17).  Foreign Loot Supports War Effort.  For every full economic zone you have conquered, obtain 3 extra supplies (place anywhere you control, immediately).   
(Card 18).  Weapons Program Espionage.  Randomly choose among the Democracies.  Obtain at least their level of atomic research.  
(Card 19).  Work Camps Produce Poor Ammunition.  Supplies cost 2 pounds this turn.
(Card 20).  Lack of Freedom Damages Economic Growth.  Remove 1 (added) GDP point from all of your fully conquered economic zones.
(Card 21).  Obtain intelligence of uprising; spectacular show trials increase support.  Obtain 2 additional Francs.  
(Card 22).  Political Generals Are Idiots.  Your generals were appointed by their connections rather than by their merits.  In all land combats during the next turn, draw at most three combat cards.
(Card 23).  All Quiet on the Western Front.  Nothing happens.  
(Card 24).  Held Military Review.  Obtain 1 Franc.    
(Card 25).  Impressive Party Rally.  Obtain 2 Francs."""

dic30 = """(Card 1).  Swim a mile in a river to demonstrate your health.  Obtain 2 Francs.      
(Card 2).  Drink champagne for breakfast.  Nothing happens.      
(Card 3).   Opposition figure caught in bed with "dead girl or live boy."  Gain 5 Francs.   
(Card 4).   Show Trial Poorly Received.  The witnesses were too sympathetic.  Pay 1 Franc.
(Card 5).   Loot Conquered Territory.  For every full economic zone you have conquered, get 5 Francs.   Wipes away any negative political cards still in effect.  
(Card 6).  Briefcase Bomb Plot Fails.  You are disabled in a bombing at headquarters and subsequently execute a top general.  Pay 1 Franc to smooth things over.  Wipes away any negative political cards still in effect.    
(Card 7).  Major Coup Attempt Caught!  Obtain two additional Francs from selling the plotter's stolen art collections.  Wipes away any negative political cards still in effect. 
(Card 8).  Air Chief Found Incompetent.  Lose 2 supplies from anywhere (you choose).    
(Card 9).  Oligarchs Support Regime with technical assistance.  Gain 2 supplies (place anywhere) and 3 Francs.       
(Card 10).  Assassin Hits Mark.  Fortunately, Mark is merely your twin brother.  Gives you an excuse to round up the usual suspects.  Obtain 1 Franc.  
(Card 11).  John has a Long Mustache.  Resistance fighters destroy railways in foreign territories occupied by you.  For the next turn, you may not move units or supplies by rail outside of your home territories.
(Card 12).  Resistance Movement Betrayed.  All attempts to destabilize your government fail; nothing happens.         
(Card 13).  Terrorism Damages Economy.  All economic zones lose one unit of added GDP (effective immediately).
(Card 14).  Pro-regime fanatics undermine the domestic life of the democracies.  Obtain 3 Francs for every Democracy still in the game.  
(Card 15).  Guerillas Plot to Aid Invaders.  Choose a province randomly.  Within that province, Democracies draw one extra combat card in combats on this turn.   
(Card 16).  Youth program success!  Obtain an extra infantry unit that may be placed in any of your original cities (immediately).  
(Card 17).  Foreign Loot Supports War Effort.  For every full economic zone you have conquered, obtain 3 extra supplies (place anywhere you control, immediately).   
(Card 18).  Weapons Program Espionage.  Randomly choose among the Democracies.  Obtain at least their level of atomic research.  
(Card 19).  Youth program encourages fanaticism in the army.  Defending (all order types) land units fight at an additional +1 for this turn.  
(Card 20).  Lack of Freedom Damages Economic Growth.  Remove 1 (added) GDP point from all of your fully conquered economic zones.
(Card 21).  Obtain intelligence of uprising; spectacular show trials increase support.  Obtain 2 additional Francs.  
(Card 22).  Political Generals Are Idiots.  You fire them - but it costs you some to smooth things over, make them Field Marshals, and shunt them out of the way.  Pay 3 Francs.  
(Card 23).  All Quiet on the Western Front.  Nothing happens.  
(Card 24).  Held Military Review.  Obtain 1 Franc.    
(Card 25).  Impressive Party Rally.  Obtain 2 Francs."""

cards = {
    'democracy': {
        '0': dem0.split('\n'),
        '10': dem10.split('\n'),
        '20': dem20.split('\n'),
        '30': dem30.split('\n')
    },
    'dictatorship': {
        '0': dic0.split('\n'),
        '10': dic10.split('\n'),
        '20': dic20.split('\n'),
        '30': dic30.split('\n')
    }
}



# def result(government, investment):
#     roll = random.randint(0,24)
#     result = cards[government][investment][roll]
#     return result

# urls = (
#   '/', 'index'
# )

# app = web.application(urls, globals())
# render = web.template.render('templates/')

# class index:
#     def GET(self):
#         return render.politics(result = '')

#     def POST(self):
#         form = web.input(government="", investment="")
#         res = result(form.government, form.investment)
#         return render.politics(result=res)

# if __name__ == "__main__":
#     app.run()

import json

print json.dumps(cards)
    




