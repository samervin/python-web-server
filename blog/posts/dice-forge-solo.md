---
datetime: 2018-10-07 20:11
title: Creating an AI for playing Dice Forge solo
---

I'm a big fan of [Dice Forge](https://boardgamegeek.com/boardgame/194594/dice-forge). It's a board game where you can customize all six faces of your two dice in a quest to buy cards and score points over 9 or 10 rounds. The soul of the game is similar to some other games I like: Dice Forge allows you to develop long-term strategies, but requires you to react tactically to chance. It's pretty easy to teach new players. As a bonus, since everyone rolls their dice on everyone's turn, there isn't a lot of downtime.

I play some other dice games solo in my spare time. [Dice City](https://boardgamegeek.com/boardgame/179572/dice-city) comes to mind as a game with many similarities, but others like [Roll Player](https://boardgamegeek.com/boardgame/169426/roll-player) and [VivaJava](https://boardgamegeek.com/boardgame/139899/vivajava-coffee-game-dice-game) have seen solo play as well. There's no official solo mode for Dice Forge, though. What am I to do?

Well, the first place I went was the BoardGameGeek forums. There's a section dedicated to [variants](https://boardgamegeek.com/boardgame/194594/dice-forge/forums/69), which was a great place to gather ideas. I found that there were two general categories of solo rules: Score Attack, where you played alone and tried to maximize your score; and AI, where some set of rules guided an AI to emulate a real player.

Playing without any semblance of interaction didn't feel right, though. I also wasn't satisfied with the existing AI rulesets. They were too complicated or required resources outside the game, like a deck of cards with decisions on them. I wanted the rules to be able to fit on an index card.

So I sat down and made up this ruleset. Read the short version to see what it does, then check out the result of my first game against it. I go into more details and explain my thoughts at the bottom.

---

## Short AI rules

The first written version of these rules was a little on the long side. It also didn't put everything in order of importance. So I wrote this quick version to make it more digestible for someone not in my own head. Enjoy.

### Set up

Set up the game using the two-player rules. You take the first turn. Use the following stacks of cards:

- [1 moon] Blacksmith's Hammer and Chest
- [2 moon] Silver Hind
- [3 moon] Tenacious Boar
- [4 moon] Ferryman
- [5 moon] Helmet of Invisibility
- [6 moon] Cancer
- [1 sun] Elder and Wild Spirits
- [2 sun] Guardian's Owl
- [3 sun] Guardian's Shield
- [4 sun] Gorgon
- [5 sun] Mirror of the Abyss
- [6 sun] Sphinx
- [5 moon + 5 sun] Hydra

### Round-by-round rules

On the AI's turn, if it is...

__Round 1, 2, or 3:__

Prioritize sun > moon > gold > points.

If the AI has 8 or more gold, forge the most expensive die face(s) it can afford. Follow its resource priority.

Otherwise, buy the first card from the following list that it can afford:

- Tenacious Boar
- Silver Hind
- Guardian's Shield
- Guardian's Owl
- Wild Spirits
- Blacksmith's Chest* (unless it already has one)

__Round 4, 5, or 6:__

Prioritize sun > moon > points > gold.

Buy the first card from the following list that it can afford:

- Hydra
- Cancer
- Sphinx
- Helmet of Invisibility
- Mirror of the Abyss

Otherwise, with 8 or more gold, forge the most expensive die face(s) it can afford. Follow its resource priority.

Otherwise, buy the first card from the following list that it can afford:

- Guardian's Shield
- Elder* (unless it already has a Hammer)
- Blacksmith's Hammer* (unless it already has an incomplete Hammer or an Elder)

Otherwise, fall back to Round 1 rules.

__Round 7, 8, or 9:__

Prioritize points > sun > moon > gold.

Buy the first card from the following list that it can afford:

- Hydra
- Cancer
- Sphinx
- Gorgon
- Ferryman

Otherwise, with 8 or more gold, forge the most expensive die face(s) it can afford that grants points.

Otherwise, buy the first card from the following list that it can afford:

- Elder* (unless it already has a Hammer)
- Blacksmith's Hammer* (unless it already has an incomplete Hammer or an Elder)

Otherwise, fall back to Round 1 rules.

### Other general rules

When forging a die face, randomly determine which 1-gold face to replace. If there are none left, choose the smallest remaining gold die face.

When rolling a minor blessing, choose a die at random. Optionally, it may choose the "best" die, avoiding Boar or x3 faces.

If the AI has a Hammer or an Elder, always use it if possible.

If the AI has 2 sun left over after choosing an action, it always spends it to take another action if possible.

If the AI needs to make a choice (for example, choosing a resource from a Boar roll), it chooses in resource priority order. Optionally, it may avoid options that are not efficient, e.g. not taking 3 gold if it already has 12.

---

## Result of the first attempt

So how did it go?

Well, pretty well! The AI ended up forging only 5 die faces: two 1-sun faces, a 2-sun face, a x3 face, and the combination gold + point + sun + moon face. It managed to buy two Hydras and two Sphinxes with the help of the x3 face, and even kept an Elder running.

I went for a more esoteric strategy. I forged 6 different die faces with some kind of points on them and generally bought cheaper cards. I ended up with a little too much gold towards the end of the game and only two Cancers, but I still went into the last round with a huge number of points.

I expected to trounce the AI. It wasted several rolls by overstocking itself with sun die faces. It wasn't efficient in moving around the board and didn't care if it ousted me.

I didn't trounce the AI. I lost.

It was close. The AI's 140 to my 136. Still. I lost to a dumb robot.

I guess I know what strategy I'm using the next time I play.

---

## Full AI rules

Here's the full explanation of all the unwritten rules I ignored or didn't fully explain above. They'd be useful if you were programming a Dice Forge AI to play how I wanted it to play, but they're not always ideal for learning. I also go into details on some of the decisions I made.

### Cards chosen

In most cases here, I chose the simpler card, or the card that an AI would have a harder time misusing. I also record a short explanation of what each card does for reference.

Here's the moon-cost cards. If I didn't list an alternative, there isn't one in the box, and so every game uses it.

- [1 moon] Blacksmith's Hammer (Convert gold to points)
- [1 moon] Blacksmith's Chest (Extra storage)
- [2 moon] Silver Hind (Start of turn: Minor blessing) instead of Great Bear (3 points on oust)
    - Consistent minor blessings are perfectly fine. The AI rules don't take ousting into account.
- [3 moon] Tenacious Boar (Boar die face) instead of Satyrs (Everyone else rolls, use 2 faces)
    - The Boar die face is easier to account for in the AI's priorities. I'm not a huge fan of Satyrs anyway.
- [4 moon] Ferryman (just points) instead of Cerberus (x2 token)
    - I avoid single-use tokens so I don't have to tell the AI when to use them.
- [5 moon] Helmet of Invisibility (x3 die face)
- [6 moon] Cancer (2 divine blessings) instead of Sentinel (2 divine blessings + convert sun or moon to points)
    - Slightly reducing the decisions needed for when to convert to points.

And here's the sun-cost cards.

- [1 sun] Elder (Start of turn: -3 gold for 4 points)
- [1 sun] Wild Spirits (3 gold + 3 moon)
- [2 sun] Guardian's Owl (1 gold, 1 sun, or 1 moon) instead of Celestial Ship (Temple dice face)
    - This die face would probably work fine with the AI, since there are already rules for buying die faces. I picked the option that required less fiddling with die faces.
- [3 sun] Guardian's Shield (Conditional die faces) instead of Minotaur (Everyone else rolls, lose rolled resources)
    - Rather than risk the AI buying the Minotaur at the wrong time, it just forges a die face.
- [4 sun] Gorgon (just points) instead of Triton (6 gold, 2 sun, or 2 moon)
    - Again, avoiding the single-use tokens so the AI doesn't need to use them.
- [5 sun] Mirror of the Abyss (Mirror die face)
- [6 sun] Sphinx (4 minor blessings) instead of Cyclops (4 minor blessings + convert gold to points)
    - Slightly reducing the decisions needed for when to convert to points.

Oh, and the end-row card.

- [5 moon + 5 sun] Hydra (just points) instead of Typhon (1 point per forged die face)
    - This choice means the AI doesn't need to try to optimize the number of die faces it forges.

### AI rules that always apply

These are a bit more descriptive than I originally wrote. I codified some of the assumed interactions I encountered when I was playing. The gist of the rules is that the AI doesn't do anything wasteful if it can help it, whether that's buying cards it doesn't need or taking resources it can't hold. If you play using these rules, feel free to shorten or improv the edge cases.

Examples of _resource priority_ or _priority order_ appear below in the Round-by-round rules. It's an ordering of sun, moon, gold, and points that's specific to the round.

Unless otherwise listed, play as a normal 2-player game. The AI should go second, so it can use all the resources it accumulates. You can make all decisions on your turn independently of the AI. For the record, I don't remove die faces or cards from the board during setup, even when playing with 2 people. I think this actually benefits the AI, as it can pursue big cards more easily.

__When forging a die face:__

- if buying from the Sanctuary, choose the most expensive die face, then choose the largest value of the highest _resource priority_
    - e.g. if it's round 1 and the AI has 10 gold, it will forge a 2-sun face
    - if the AI has gold remaining after its first die face, it will try and forge another die face
        - e.g. (continued) if the AI uses its first 8 gold on a 2-sun face in round 1, it will then forge a 1-moon face with its last 2 gold
- always remove 1-gold faces first
- if both dice have 1-gold die faces remaining, randomly choose one of the two dice to forge the new face onto
- if there are no 1-gold dice faces left on both dice, replace the face that corresponds with the lowest _resource priority_
    - e.g. if it's round 6 and the AI forges its 10th die face, it will replace the face that gives it the least gold if it can

The 2-point starting face isn't bad for the AI for slowly accumulating points, so it doesn't replace it.

__When rolling a minor blessing:__

- choose the die with the most _effective faces_
    - 1-gold die faces are _not_ effective
    - Boar die faces are _not_ effective
    - x3 die faces are _not_ effective
    - all other die faces are _effective_
- if the two dice tie in effectiveness, choose in this order:
    - choose the die with fewer x3 die faces
    - choose the die with fewer Boar die faces
    - choose randomly

Essentially, choose the die that's least likely to whiff or help the opponent.

__Card-specific rules:__

- always use each Elder at the start of each turn if possible
- always use the active Blacksmith's Hammer when acquiring gold if possible
- never buy more than 1 Chest
- never buy a Hammer if the AI owns an unfinished Hammer _or_ an Elder
- never buy an Elder if the AI owns a Hammer

The AI shouldn't waste early turns buying several Chests, nor should it try to split its gold into many cards.

__Other rules:__

- if the AI takes its first action and has 2 sun left, it will always go again if it can
    - the only time it wouldn't would be if it had no sun, no moon, and less than 2 gold
- if the AI needs to make a choice, e.g. which resource to take from the Guardian's Owl or which die face to copy with the Mirror, it will choose in _priority order_
    - exception: if it cannot take the entire benefit of the choice, it will try the next _priority_ choice
    - if none of the choices can be taken fully, the AI will take the first choice in _priority order_ that gives any benefit

### Addendum: Potential changes

I didn't include any of these options in my original draft because I wanted to know how well the AI would do with simple rules. Frankly, I'm not in a hurry to implement any of these until I've got my confidence back. Anyway. Here's some ideas to change up the AI for when I step my game up:

- forge die faces differently
    - forge everything to one die first so that the other die can have more effective x3 and Mirror results
    - forge die faces with fewer gold in the earlier turns
    - some chance to specifically forge a gold die face
- change a round's resource priorities based on certain actions
    - e.g. if the AI buys an Elder or a Hammer, value gold higher than normal
- adjust the round divisions, e.g. separate the 9th round so the AI can't buy a die face
- if the AI gets too easy, try a few things to make it harder:
    - change all AI minor blessings to major blessings (this has the advantage of removing a section of rules)
    - start the AI with more resources
    - start the AI with some improved die faces
