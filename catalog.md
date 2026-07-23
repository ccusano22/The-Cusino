---
layout: page
title: "Complete Dealer's Choice Poker Catalog"
description: "The complete long-form source catalog used to generate the card index and individual rules pages."
permalink: /catalog/
source_reviewed: "2026-07-20"
main_catalog_games: 35
supplemental_calls: 4
format: "Markdown"
---

> A practical, single-file rules catalog for a home game in which the deal passes and each dealer calls the next poker variant.

## Scope and editorial method

The main catalog covers all **35 games and variants listed in the OnlinePoker.net Dealer's Choice index** as reviewed on July 20, 2026. Each entry is an original, concise rules summary with a direct source link; it is not a copy of the source text. The supplemental section adds **Five-Card Draw, High Chicago, Low Chicago, and Wild Widow** because they are common dealer calls or explicitly requested examples, but they are not four additional entries in OnlinePoker.net's 35-game index.

Primary index: [OnlinePoker.net - Dealer's Choice](https://www.onlinepoker.net/games)

OnlinePoker.net's index blurbs and detailed pages occasionally disagree. This catalog generally treats the detailed game page as authoritative, flags material conflicts, and supplies a clearly labeled editorial player recommendation when a page omits a feasible count.

All games assume a standard 52-card deck unless the entry says otherwise. Home-game rules vary widely, especially for wild cards, kill cards, pay cards, match-the-pot liabilities, split pots, and declaration procedures. The dealer's spoken call controls only when it is complete and understood by the table.

## How this repository uses the master catalog

This file is the long-form master catalog. The GitHub Pages build runs `python3 scripts/build_games.py`, which reads the templated game sections below and generates one page per game in `_games/`. The home page then turns those generated pages into searchable, filterable cards.

This arrangement keeps the content portable and reviewable in one Markdown file while giving site visitors a faster browsing experience. Edit the game rules here, preserve the existing field labels and heading structure, and let the build script regenerate the individual pages.

## Pass-the-deck operating rule

When the deal moves clockwise, the new dealer should call the game **before collecting antes or dealing any cards**. Use this sentence pattern:

> **Game - stakes - pot format - cards and board - wild/kill/pay cards - declaration - cap - tie and split rules.**

Example:

> **Low Chicago, $1/$2 fixed limit, seven-card stud, ace of spades is high so 2 of spades is low, down-card spades only, cards speak, odd chip to the high-hand winner.**

For any match-the-pot game, the call is incomplete until the dealer announces a **hard loss cap**.

## House-rule vocabulary

| Term | Working definition for this catalog |
|---|---|
| Wild card | May represent another rank or card as allowed by the called rule. |
| Personal wild | A wild rank that applies to only one player, often based on that player's own card. |
| Pay card | Requires the holder or recipient to add a called amount to the pot. |
| Kill card | Makes a card, rank, or entire hand dead under the called rule. |
| Drop / burn | A simultaneous decision to leave the hand or continuing pot before a later deal or showdown. |
| Match the pot | A losing entrant contributes an amount equal to the current pot, normally into a continuing pot. |
| Leg | One qualifying win toward collecting a continuing race bank. |
| Cards speak | The exposed cards determine the result; a verbal declaration does not change the actual hand. |
| Declare | A player must announce high, low, both, in, or out under a fixed simultaneous procedure. |
| Scoop | One player wins every available share of a split pot. |

<a id="quick-index"></a>
## Quick index

| # | Game | Players | Family | Defining feature |
|---:|---|---|---|---|
| 1 | [3-5-7 Guts](#3-5-7-guts) | 2-7; 4-7 recommended | Guts / match-the-pot | The 3-card hand uses 3s wild, the 5-card hand uses 5s wild, and the 7-card hand uses 7s wild. |
| 2 | [7-27](#7-27) | 4-7 | Hit-or-stand / split pot | No wild cards. |
| 3 | [Anaconda](#anaconda) | 3-7; 4-7 recommended | Pass poker / high-low split | No wild cards by default. |
| 4 | [Badugi](#badugi) | 2-8 practical; 2-6 preferred | Four-card draw lowball | No wild cards. |
| 5 | [Baseball and Blind Baseball](#baseball) | 4-5 with one 52-card deck | Nine-card expose-to-beat / stud-style | A dealt 4 is a pay card that earns an extra card under the source rules; it is not automatically wild. |
| 6 | [Burn the Biffel](#burn-the-biffel) | 2-7; 4-7 recommended | Community-card elimination | Bad-row ranks remove matching hole cards. |
| 7 | [Connect Four](#connect-four) | 2-6 | Multi-draw wild-card poker | All 4s are wild. |
| 8 | [Crazy Pineapple](#crazy-pineapple) | 3-8 | Hold'em / discard | No wild cards. |
| 9 | [Criss Cross](#criss-cross) | 6-8; playable shorter | Community-card cross with wild center | The center community card is wild, and cards of the same rank in a player's hand are also wild under the source rules. |
| 10 | [Elevator](#elevator) | 6-10 | Community-card H board | No wild cards by default; the center or a called rank may be wild as a variation. |
| 11 | [Follow the Queen](#follow-the-queen) | 2-7; 4-7 recommended | Seven-card stud with changing wild rank | Every face-up queen is wild. |
| 12 | [Guts](#guts) | 2-17 theoretical; 4-10 recommended | Three-card simultaneous declaration | No wild cards by default. |
| 13 | [HORSE](#horse) | 2-6 recommended | Fixed-limit mixed-game rotation | No wild cards in the standard rotation. |
| 14 | [In Between / First Past Post](#in-between) | 2-8 | Table banking / red-dog style | No wild cards. |
| 15 | [Iron Cross](#iron-cross) | 4-7 | Community-card cross | No wild cards by default. |
| 16 | [Jacks or Better](#jacks-or-better) | 2-6 recommended | Five-card draw with opening qualifier | No wild cards by default. |
| 17 | [Kings and Little Ones](#kings-and-little-ones) | 2-7; 4-7 recommended | Seven-card stud with personal wilds | Kings are wild, and each player's lowest rank is also wild. |
| 18 | [Monterey](#monterey) | 4-7 | Stud with personal river-rank wilds | Each player's seventh and final card is dealt down and is wild; every matching rank in that player's hand is also wild. |
| 19 | [No Holds Barred](#no-holds-barred) | 5-7 | Touching-card community square | The four corner cards may be called wild. |
| 20 | [Omaha](#omaha) | 2-10 | Four-hole-card community poker | No wild cards in standard Omaha. |
| 21 | [Omaha Burn](#omaha-burn) | 2-11 | Omaha with drop-and-match decision | No wild cards by default. |
| 22 | [Outhouse](#outhouse) | 2-7 | Progressive side-pot and main-pot poker | No wild cards by default. |
| 23 | [Piranha](#piranha) | 2-11 | Omaha-like community match-the-pot | No wild cards by default. |
| 24 | [Position Poker](#position-poker) | 2-7 | Seven-card stud with seat-assigned wilds | All 8s are wild. |
| 25 | [Pregnant 3s](#pregnant-3s) | 2-6 recommended | Five-card draw with many wilds | 3s, 6s, and 9s are wild, for as many as twelve wild cards. |
| 26 | [Razz](#razz) | 2-6 | Seven-card stud lowball | No wild cards. |
| 27 | [Roll Your Own](#roll-your-own) | 5-7 | Stud with player-selected exposed cards | No wild cards in the standard form. |
| 28 | [Russian Poker](#russian-poker) | 2-4 | Thirteen-card arrangement / Chinese-poker style | No wild cards by default. |
| 29 | [Sevens Take All](#sevens-take-all) | 2-7; 4-7 recommended | Seven-card stud with special winning pair | No conventional wild cards. |
| 30 | [Shifting Sands](#shifting-sands) | 2-7 | Roll-your-own stud with personal wild rank | Each player's first chosen exposed card establishes that player's personal wild rank; all matching cards in that hand are wild. |
| 31 | [Stud](#stud) | 2-6 | Seven-card stud | No wild cards in standard stud. |
| 32 | [Texas Hold'em](#texas-holdem) | 2-10 | Two-hole-card community poker | No wild cards in standard Hold'em. |
| 33 | [The Good, The Bad, The Ugly](#good-bad-ugly) | 2-7; 4-7 recommended | Seven-card stud with wild, discard, and kill ranks | The Good rank is wild, the Bad rank must be discarded, and the Ugly rank kills any hand containing it. |
| 34 | [Three Legged Race](#three-legged-race) | 2-6 | Multi-leg draw poker | No wild cards by default; the dealer may call a wild rank for one or all legs. |
| 35 | [Two More Inches](#two-more-inches) | 4-7 | Five-card draw plus two-card match-the-pot showdown | No wild cards by default. |

## Main catalog: OnlinePoker.net's 35 Dealer's Choice entries

The entries are alphabetized for table use. Numbering corresponds to this catalog, not the order on the source index.

---

<a id="3-5-7-guts"></a>
## 1. 3-5-7 Guts

**Family:** Guts / match-the-pot

**Players:** 2-7; 4-7 recommended

**Pot format:** One continuing pot; losing entrants match the pot, subject to a declared cap.

**Wild / kill / pay cards:** The 3-card hand uses 3s wild, the 5-card hand uses 5s wild, and the 7-card hand uses 7s wild.

**Call before the deal:** Ante, match cap, whether declarations are simultaneous, the three-card ranking, and whether the pot is awarded to a sole entrant or after five consecutive hand wins.

### Deal and play

1. Deal three cards to each player for the first hand. Players simultaneously declare in or out.
2. Show the hands of all players who stayed in. The best hand wins that stage; the lowest participating hand pays the winner an amount equal to the pot, while the original pot remains.
3. Add two cards to every player for the five-card stage, then repeat the simultaneous declaration and showdown.
4. Add two more cards for the seven-card stage and repeat. Begin another 3-5-7 cycle if the pot remains live.

**Winning condition:** The pot is normally taken by a player who is the only entrant, or under the source rule, by a player who wins five hands in succession.

**Variations:**

- Hard-cap each match at a fixed dollar amount or number of antes.
- Require exactly two players to stay in before a showdown; otherwise redeal that stage.
- Use standard poker rankings for three cards, or call a house ranking in which a straight beats a flush.

> **Game tip:** This game can create runaway liabilities. Put the match cap in the dealer call and keep it visible beside the pot.

**Source:** [OnlinePoker.net - 3-5-7 Guts](https://www.onlinepoker.net/games/3-5-7-guts)

[Back to quick index](#quick-index)

---

<a id="7-27"></a>
## 2. 7-27

**Family:** Hit-or-stand / split pot

**Players:** 4-7

**Pot format:** Single pot, normally split between the high target and low target winners.

**Wild / kill / pay cards:** No wild cards. Aces count as 1 or 11, face cards as 0.5, and number cards at face value. A-A-5 is an automatic scoop under the source rules.

**Call before the deal:** Ante, betting structure, exact tie treatment, whether players may change an ace value after betting, and whether A-A-5 always scoops.

### Deal and play

1. Deal one card down and one card up to each player.
2. Beginning left of the dealer, each player either takes another card or passes. Betting may occur after each circuit.
3. A player who passes three times is locked and takes no more cards.
4. Continue until all players are locked, then expose the down cards and total each hand.

**Winning condition:** Half the pot goes to the total closest to 7 without exceeding it; half goes to the total closest to 27 without exceeding it. A qualifying scoop rule overrides the split if called.

**Variations:**

- Play only the 7 side or only the 27 side.
- Make totals over the target bust and ineligible, or rank them by distance on both sides of the target.
- Require a minimum number of cards before a player may lock.

> **Game tip:** Treat visible face cards as cheap half-points, not as danger cards. Track both targets at once before taking a hit.

**Source:** [OnlinePoker.net - 7-27](https://www.onlinepoker.net/games/7-27-poker)

[Back to quick index](#quick-index)

---

<a id="anaconda"></a>
## 3. Anaconda

**Family:** Pass poker / high-low split

**Players:** 3-7; 4-7 recommended

**Pot format:** Single pot, usually split between the best and worst five-card hands.

**Wild / kill / pay cards:** No wild cards by default.

**Call before the deal:** Ante, pass direction, low-hand ranking, whether players must declare high or low, and how odd chips are awarded.

### Deal and play

1. Deal seven cards face down to each player and complete an opening betting round.
2. Each player simultaneously passes two selected cards in the called direction, receives two, and bets again.
3. Pass one card, bet, then pass two cards and bet a final time.
4. At showdown, each player forms a five-card high hand and a five-card low or worst hand from the seven cards held.

**Winning condition:** The best high hand takes one half and the called low or worst hand takes the other. A player may scoop both halves.

**Variations:**

- Pass 3-2-1 instead of 2-1-2.
- Alternate pass direction after each exchange.
- Play high only, low only, or cards-speak high-low without declaration.
- Use ace-to-five, deuce-to-seven, or simple weakest-poker-hand rules for the low half.

> **Game tip:** Do not merely pass your worst cards. Infer what the receiving player is building, especially after the direction reverses.

**Source:** [OnlinePoker.net - Anaconda](https://www.onlinepoker.net/games/anaconda)

[Back to quick index](#quick-index)

---

<a id="badugi"></a>
## 4. Badugi

**Family:** Four-card draw lowball

**Players:** 2-8 practical; 2-6 preferred

**Pot format:** Single pot.

**Wild / kill / pay cards:** No wild cards. Duplicate ranks or suits reduce the number of cards in the qualifying Badugi hand.

**Call before the deal:** Ante or blinds, fixed-limit/pot-limit/no-limit structure, number of draws, and whether aces are always low.

### Deal and play

1. Deal four cards face down to each player and complete the first betting round.
2. Allow a draw of zero to four cards, followed by a betting round.
3. Repeat for a total of three draws and four betting rounds unless a shorter structure was called.
4. At showdown, remove duplicate ranks and duplicate suits to identify each player's best valid one-, two-, three-, or four-card Badugi.

**Winning condition:** Any four-card Badugi beats every three-card hand; any three-card hand beats every two-card hand, and so on. Among hands of equal size, compare the highest card downward, with lower better.

**Variations:**

- Single-draw or double-draw Badugi.
- Pot-limit, half-pot-limit, fixed-limit, or no-limit betting.
- Badacey or Badeucy split-pot hybrids, if the group already knows those rankings.

> **Game tip:** A rough four-card Badugi is usually stronger than a smooth three-card hand. Preserve four unique suits and ranks unless the draw clearly warrants breaking it.

**Source:** [OnlinePoker.net - Badugi](https://www.onlinepoker.net/games/badugi)

**Editorial note:** OnlinePoker.net describes the structure but does not publish a player cap on the detailed page; the range above is an editorial one-deck recommendation.

[Back to quick index](#quick-index)

---

<a id="baseball"></a>
## 5. Baseball and Blind Baseball

**Family:** Nine-card expose-to-beat / stud-style

**Players:** 4-5 with one 52-card deck

**Pot format:** Single pot.

**Wild / kill / pay cards:** A dealt 4 is a pay card that earns an extra card under the source rules; it is not automatically wild. Classic Baseball Stud commonly makes 3s and 9s wild and treats 4s as pay-for-an-extra-card cards.

**Call before the deal:** Regular or Blind Baseball, the cost and timing of a 4, whether extra cards are face up or down, the ranking of partial exposed hands, and whether classic 3s-and-9s wild rules are in force.

### Deal and play

1. Deal nine cards face down to every player. In regular Baseball, players may privately inspect them; in Blind Baseball, they may not.
2. The first player turns cards face up until the exposed holding establishes the hand to beat.
3. Each later player turns cards one at a time until the exposed holding beats the current leader or the player runs out of cards. Bet when the called structure requires it.
4. Resolve any pay-card extra deals, continue around the table, and award the pot to the final leading exposed hand.

**Winning condition:** The last player showing the highest ranked exposed poker hand wins.

**Variations:**

- Classic seven-card Baseball Stud: 3s and 9s wild; a 4 can buy an extra card.
- Make 4s wild as well as pay cards.
- Play Blind Baseball, in which no player sees a card before exposing it.
- Use a second deck for a larger table, but call how identical cards are handled.

> **Game tip:** With nine cards per player, deck capacity is the first constraint. For six or more players, change the deal or use a second deck before the hand starts.

**Source:** [OnlinePoker.net - Baseball and Blind Baseball](https://www.onlinepoker.net/games/baseball)

**Editorial note:** The source says up to seven players, but nine cards each cannot be dealt to six or seven players from one 52-card deck. This catalog uses the mathematically feasible one-deck range.

[Back to quick index](#quick-index)

---

<a id="burn-the-biffel"></a>
## 6. Burn the Biffel

**Family:** Community-card elimination

**Players:** 2-7; 4-7 recommended

**Pot format:** Single pot.

**Wild / kill / pay cards:** Bad-row ranks remove matching hole cards. A Good-row card is canceled if its rank also appears in the Bad row. The last Bad card is often called wild or as a kill card, but that is a house option.

**Call before the deal:** Ante, reveal order, whether the final Bad card is wild or a kill card, whether a canceled Good rank removes all copies, and minimum cards needed to remain live.

### Deal and play

1. Deal four cards face down to each player.
2. Lay out two rows of five community cards: a Good row and a Bad row.
3. Reveal cards alternately from the two rows, with a betting round after each reveal or reveal pair as called.
4. Whenever a Bad card appears, each player discards matching hole-card ranks. If that rank is also in the Good row, that Good card is no longer usable.
5. After all reveals, build the best five-card hand from surviving hole cards and active Good cards.

**Winning condition:** The highest legal five-card hand wins the pot.

**Variations:**

- Make the final Bad rank wild in surviving hands.
- Make the final Bad card a kill card that eliminates any player holding that rank.
- Reveal Good and Bad cards in pairs to shorten the hand.

> **Game tip:** Do not overvalue an early Good card. Until the matching Bad position is resolved, its contribution is provisional.

**Source:** [OnlinePoker.net - Burn the Biffel](https://www.onlinepoker.net/games/burn-the-biffel)

[Back to quick index](#quick-index)

---

<a id="connect-four"></a>
## 7. Connect Four

**Family:** Multi-draw wild-card poker

**Players:** 2-6

**Pot format:** Single pot.

**Wild / kill / pay cards:** All 4s are wild. A player holding a 4 also treats that player's lowest-ranked card as wild; if the lowest card is itself a 4, no additional rank becomes wild. The index describes wilds as pay cards, so the price must be called.

**Call before the deal:** Ante, three-draw structure, minimum and maximum discard, whether discards are recycled, the amount owed for each wild/pay card, and whether cards speak or players are bound by a declared hand.

### Deal and play

1. Deal five cards face down to each player and bet.
2. Run three draw rounds. On each draw, a player discards and replaces one to three cards, then the table bets.
3. Recycle and reshuffle the muck only if required and only under the procedure announced before the deal.
4. At showdown, apply the 4 and lowest-card wild rules to each player independently.

**Winning condition:** The highest five-card poker hand wins.

**Variations:**

- Make each 4 cost one ante, a fixed chip amount, or a contribution to a side pot.
- Limit the game to two draws.
- Require exactly one discarded card on the final draw.
- Make only natural 4s wild and remove the lowest-card extension.

> **Game tip:** With twelve or more replacement cards possible per player, deck exhaustion is real. Use a precise muck-recycling rule and never mix live folded hands into the draw pile.

**Source:** [OnlinePoker.net - Connect Four](https://www.onlinepoker.net/games/connect-four)

[Back to quick index](#quick-index)

---

<a id="crazy-pineapple"></a>
## 8. Crazy Pineapple

**Family:** Hold'em / discard

**Players:** 3-8

**Pot format:** Single pot.

**Wild / kill / pay cards:** No wild cards.

**Call before the deal:** Crazy Pineapple or regular Pineapple, betting limit, discard timing, and whether the discarded card is shown.

### Deal and play

1. Deal three hole cards to each player and complete the preflop betting round.
2. Deal the three-card flop and bet.
3. In Crazy Pineapple, each remaining player discards one hole card after the flop betting round. In regular Pineapple, discard before the flop is dealt.
4. Deal and bet the turn and river as in Texas Hold'em, then show down using any combination of the two remaining hole cards and five board cards.

**Winning condition:** The best five-card poker hand wins.

**Variations:**

- Regular Pineapple: discard before the flop.
- Lazy Pineapple: keep all three hole cards to showdown but use no more than two.
- Crazy Pineapple high-low, with a declared low qualifier.

> **Game tip:** Plan the discard before the flop arrives, then reassess. Keeping two attractive but redundant cards often sacrifices the stronger turn-and-river coverage.

**Source:** [OnlinePoker.net - Crazy Pineapple](https://www.onlinepoker.net/games/crazy-pineapple)

[Back to quick index](#quick-index)

---

<a id="criss-cross"></a>
## 9. Criss Cross

**Family:** Community-card cross with wild center

**Players:** 6-8; playable shorter

**Pot format:** Single pot.

**Wild / kill / pay cards:** The center community card is wild, and cards of the same rank in a player's hand are also wild under the source rules.

**Call before the deal:** Ante, betting after each reveal, whether the center itself is wild, and the exact board-use rule: one complete horizontal or vertical three-card line only.

### Deal and play

1. Deal five cards face down to each player.
2. Lay five community cards face down in a cross.
3. Reveal the four outer cards one at a time, betting after each reveal.
4. Reveal the center card last and complete the final betting round.
5. At showdown, combine personal cards with either the complete horizontal three-card line or the complete vertical three-card line. Do not mix arms of the cross.

**Winning condition:** The highest legal five-card hand wins.

**Variations:**

- Center card is wild but matching hole-card ranks are natural.
- Center rank is wild only in a player's private cards.
- High-low split.
- Reveal opposite arms together to reduce betting rounds.

> **Game tip:** Evaluate both legal three-card lines independently. A strong-looking pair of outer cards is useless if they do not belong to one complete line.

**Source:** [OnlinePoker.net - Criss Cross](https://www.onlinepoker.net/games/cris-cross)

[Back to quick index](#quick-index)

---

<a id="elevator"></a>
## 10. Elevator

**Family:** Community-card H board

**Players:** 6-10

**Pot format:** Single pot.

**Wild / kill / pay cards:** No wild cards by default; the center or a called rank may be wild as a variation.

**Call before the deal:** Ante, reveal schedule, whether the center is wild, and the legal H-shaped three-card board lines.

### Deal and play

1. Deal four personal cards to each player, two face down and two face up.
2. Lay seven community cards face down in an H pattern.
3. Reveal the outer community cards according to the called sequence, betting between reveals.
4. Reveal the center connector last and complete the final betting round.
5. Make a five-card hand using exactly two personal cards and exactly one complete legal three-card line from the H board.

**Winning condition:** The highest legal five-card hand wins.

**Variations:**

- Center card wild.
- Center rank wild in all hands.
- High-low split.
- Deal all four personal cards face down for less information.

> **Game tip:** Count legal lines before judging your hand. Elevator punishes players who mentally combine community cards that are not on the same path.

**Source:** [OnlinePoker.net - Elevator](https://www.onlinepoker.net/games/elevator)

[Back to quick index](#quick-index)

---

<a id="follow-the-queen"></a>
## 11. Follow the Queen

**Family:** Seven-card stud with changing wild rank

**Players:** 2-7; 4-7 recommended

**Pot format:** Single pot.

**Wild / kill / pay cards:** Every face-up queen is wild. The next face-up card dealt after a queen sets the current wild rank; a later queen can reset that rank. Many games use No Queen, No Game. Wild cards may also be pay cards.

**Call before the deal:** Ante, No Queen No Game, whether a down-card queen activates the rule, whether a later queen cancels the prior follower rank, and the price of wild/pay cards.

### Deal and play

1. Deal seven-card stud: two cards down and one up, then additional up cards with betting, and a final card down.
2. When a queen appears face up, mark it wild. The next exposed card dealt establishes the follower rank as wild.
3. If another queen appears, apply the called reset rule and identify the new follower rank.
4. At showdown, make the best five-card hand from seven cards using the active wild rules.

**Winning condition:** The highest five-card poker hand wins, unless No Queen No Game forces a redeal.

**Variations:**

- No Queen No Game.
- Queen and every follower rank remain wild cumulatively rather than resetting.
- Only the most recent follower rank is wild.
- Queens are natural but the follower rank is wild.
- Each wild card costs one ante or a fixed amount.

> **Game tip:** Track the current follower rank with a marker. Most disputes happen because players remember an obsolete wild rank after a second queen appears.

**Source:** [OnlinePoker.net - Follow the Queen](https://www.onlinepoker.net/games/follow-the-queen)

[Back to quick index](#quick-index)

---

<a id="guts"></a>
## 12. Guts

**Family:** Three-card simultaneous declaration

**Players:** 2-17 theoretical; 4-10 recommended

**Pot format:** Continuing pot; every losing entrant matches the pot, subject to a declared cap.

**Wild / kill / pay cards:** No wild cards by default.

**Call before the deal:** Ante, three-card hand ranking, declaration method, match cap, treatment of ties, and whether a sole entrant immediately wins the pot.

### Deal and play

1. Deal three cards face down to each player.
2. After looking, all players simultaneously declare in or out, commonly by holding or dropping a chip.
3. Players who stayed in expose their hands. The best participating hand wins the amount of the pot, while each losing participant matches that amount into the continuing pot.
4. Redeal and repeat until one player is the sole entrant or another called ending condition is met.

**Winning condition:** A sole entrant normally takes the pot. In a contested hand, the best three-card hand wins the current amount while matched payments replenish the pot.

**Variations:**

- Two-card Guts or four-card Guts.
- Best hand and worst hand split.
- Progressive Guts, adding a card after each unresolved deal.
- Cap matches at a fixed amount, one pot, or a set number of antes.

> **Game tip:** Do not call this game without a cap. A small starting pot can multiply quickly when several players stay in and lose.

**Source:** [OnlinePoker.net - Guts](https://www.onlinepoker.net/games/guts-poker)

[Back to quick index](#quick-index)

---

<a id="horse"></a>
## 13. HORSE

**Family:** Fixed-limit mixed-game rotation

**Players:** 2-6 recommended

**Pot format:** Each component game awards its own pot; the rotation continues by orbit, time, or blind level.

**Wild / kill / pay cards:** No wild cards in the standard rotation.

**Call before the deal:** Rotation order, exact Omaha form, stakes, number of hands or time per game, and whether dealer-choice substitutions are allowed.

### Deal and play

1. Play Hold'em for the called number of hands or one dealer orbit.
2. Rotate to Omaha, then Razz, Seven-Card Stud, and Eight-or-Better Stud.
3. Keep the betting structure fixed-limit unless the group explicitly calls another structure.
4. Continue cycling through the five games for the agreed session length.

**Winning condition:** Each hand is won under the rules of the active component game. In Eight-or-Better Stud, the pot is split when a qualifying low exists.

**Variations:**

- Use Omaha high or Omaha high-low; announce which one because conventions differ.
- SHOE, HOSE, or another reduced mixed-game rotation.
- Dealer calls the next game from an approved rotation instead of following a fixed order.

> **Game tip:** Post a rotation card. Mixed games become slow and error-prone when players must ask which variant, limit, or bring-in applies every hand.

**Source:** [OnlinePoker.net - HORSE](https://www.onlinepoker.net/games/horse)

[Back to quick index](#quick-index)

---

<a id="in-between"></a>
## 14. In Between / First Past Post

**Family:** Table banking / red-dog style

**Players:** 2-8

**Pot format:** A central pot acts as the bank; players wager against it in turn.

**Wild / kill / pay cards:** No wild cards. Aces may be declared high or low under the called rule.

**Call before the deal:** Ante, minimum and maximum wager, ace treatment, whether equal posts trigger a redeal or an automatic penalty, and whether a tie to either post costs double.

### Deal and play

1. Deal two cards face up as posts for the active player. Arrange them low to high.
2. The player wagers up to the pot or the called table limit that a third card will fall strictly between the posts.
3. Deal the third card. A card strictly between wins the wager from the pot; a card outside loses the wager to the pot.
4. A card equal to either post normally loses double the wager. Then move the action to the next player.

**Winning condition:** This is a banking game rather than a showdown game. Each turn resolves independently against the pot.

**Variations:**

- Red Dog spread payout: pay more for a narrow spread.
- Equal posts pay a bonus only if the third card matches, otherwise push.
- Allow the player to choose high or low when an ace appears.
- Cap any double-loss penalty at the amount currently in the pot.

> **Game tip:** The number of ranks between the posts, not the visual size of the cards, determines the wager. Paired or adjacent posts are traps unless the house rule compensates them.

**Source:** [OnlinePoker.net - In Between / First Past Post](https://www.onlinepoker.net/games/in-between)

[Back to quick index](#quick-index)

---

<a id="iron-cross"></a>
## 15. Iron Cross

**Family:** Community-card cross

**Players:** 4-7

**Pot format:** Single pot.

**Wild / kill / pay cards:** No wild cards by default. The center card is a common wild-card option.

**Call before the deal:** Ante, reveal order, whether the center or center rank is wild, and the exact personal-card and board-line requirements.

### Deal and play

1. Deal two cards face down and one card face up to each player.
2. Lay five community cards face down in a cross.
3. Reveal the four outer cards one at a time, betting after each reveal.
4. Reveal the center card, then deal the final personal card face down and complete the last betting round.
5. At showdown, use exactly two personal cards plus either the full horizontal or full vertical three-card board line.

**Winning condition:** The highest legal five-card hand wins.

**Variations:**

- Center card wild.
- Center rank wild in each player's hand.
- High-low split.
- Deal four personal cards at the start instead of delaying the final down card.

> **Game tip:** The detailed rule page and index blurb do not fully agree. State the private-card count and legal board lines before dealing, not after the first bet.

**Source:** [OnlinePoker.net - Iron Cross](https://www.onlinepoker.net/games/iron-cross)

**Editorial note:** This entry follows the detailed OnlinePoker.net rule page, which lists 4-7 players and a two-down/one-up opening deal.

[Back to quick index](#quick-index)

---

<a id="jacks-or-better"></a>
## 16. Jacks or Better

**Family:** Five-card draw with opening qualifier

**Players:** 2-6 recommended

**Pot format:** Single pot or a continuing pot if nobody can open.

**Wild / kill / pay cards:** No wild cards by default.

**Call before the deal:** Ante, betting limit, minimum opening hand, opener-proof requirement, draw limit, and what happens if nobody opens.

### Deal and play

1. Deal five cards face down to each player.
2. Beginning left of the dealer, a player may open only with at least a pair of jacks or the called qualifying hand. Others may check.
3. If someone opens, complete the betting round, allow one draw, and bet again.
4. If nobody opens, redeal and apply the called progression, commonly queens, then kings, then aces, then back to jacks.

**Winning condition:** The highest five-card poker hand wins after the draw.

**Variations:**

- Jackpots or progressive opener requirements.
- Split the pot after a set number of unopened deals.
- Switch to ace-to-five or deuce-to-seven lowball when nobody opens.
- Play for legs: a player must win a called number of pots to collect the bank.

> **Game tip:** Keep the cards that prove the opening qualification separate when drawing. That avoids disputes over whether the opener actually had jacks or better.

**Source:** [OnlinePoker.net - Jacks or Better](https://www.onlinepoker.net/games/jacks-or-better)

[Back to quick index](#quick-index)

---

<a id="kings-and-little-ones"></a>
## 17. Kings and Little Ones

**Family:** Seven-card stud with personal wilds

**Players:** 2-7; 4-7 recommended

**Pot format:** Single pot.

**Wild / kill / pay cards:** Kings are wild, and each player's lowest rank is also wild. The lowest rank can differ from player to player.

**Call before the deal:** Whether a player must hold a king to activate little ones, whether only a door-card king is wild, whether ties for lowest rank create multiple wild cards, and any pay-card cost.

### Deal and play

1. Deal and bet as in seven-card stud.
2. At showdown, identify every king as wild under the called rule.
3. For each player separately, identify the lowest rank in that seven-card holding; all cards of that rank are wild for that player.
4. Make the best five-card hand from the seven cards.

**Winning condition:** The highest five-card poker hand wins.

**Variations:**

- A player must hold at least one king for little ones to become wild.
- Only a king dealt face up is wild.
- Kings are natural; only the lowest personal rank is wild.
- Kings and little ones are pay cards.

> **Game tip:** Your lowest card is not always disposable. In this game it may be the most valuable rank in your hand, especially when paired.

**Source:** [OnlinePoker.net - Kings and Little Ones](https://www.onlinepoker.net/games/kings-little-ones)

[Back to quick index](#quick-index)

---

<a id="monterey"></a>
## 18. Monterey

**Family:** Stud with personal river-rank wilds

**Players:** 4-7

**Pot format:** Single pot.

**Wild / kill / pay cards:** Each player's seventh and final card is dealt down and is wild; every matching rank in that player's hand is also wild.

**Call before the deal:** Ante, betting structure, whether the final down card itself is wild, whether all matching ranks become wild, and whether players must declare the final hand before exposing the river.

### Deal and play

1. Deal three cards face down to each player.
2. Each player chooses one of those cards to expose, then the table bets.
3. Deal the fourth, fifth, and sixth cards face up, with betting after each street.
4. Deal the seventh card face down and complete the final betting round.
5. Apply the personal wild rank created by each player's final down card and show down the best five-card hand.

**Winning condition:** The highest five-card hand wins under the player-specific wild rule. Under the source's declaration rule, a player is bound to the hand verbally announced even when the cards support a stronger one.

**Variations:**

- The final card sets a wild rank but is itself natural.
- Only one matching card may be used as wild.
- Use cards-speak showdowns so a verbal miscall does not bind the player.
- High-low split.

> **Game tip:** Because every player can have a different wild rank, announce your five-card hand clearly at showdown and expose all seven cards together.

**Source:** [OnlinePoker.net - Monterey](https://www.onlinepoker.net/games/monterey-poker)

[Back to quick index](#quick-index)

---

<a id="no-holds-barred"></a>
## 19. No Holds Barred

**Family:** Touching-card community square

**Players:** 5-7

**Pot format:** Single pot.

**Wild / kill / pay cards:** The four corner cards may be called wild. No wild cards are mandatory.

**Call before the deal:** Ante, corner-card wild rule, reveal order, what counts as three touching consecutive board cards, and whether rows are revealed card-by-card or together.

### Deal and play

1. Deal four cards face down to each player.
2. Lay eight community cards face down in the source square pattern.
3. Reveal the community cards in the called sequence, usually leaving the four corners until last and betting after each reveal.
4. At showdown, use exactly two hole cards plus exactly three touching consecutive community cards.

**Winning condition:** The highest legal five-card hand wins.

**Variations:**

- All four corners wild.
- Only the last corner revealed is wild.
- Reveal a full row at a time to reduce the game to five betting rounds.
- High-low split.

> **Game tip:** Before betting, trace the specific three-card runs your hole cards can use. Adjacency rules matter more than raw board texture.

**Source:** [OnlinePoker.net - No Holds Barred](https://www.onlinepoker.net/games/no-holds-barred)

[Back to quick index](#quick-index)

---

<a id="omaha"></a>
## 20. Omaha

**Family:** Four-hole-card community poker

**Players:** 2-10

**Pot format:** Single pot, or a split pot in Omaha high-low.

**Wild / kill / pay cards:** No wild cards in standard Omaha.

**Call before the deal:** High only or high-low, low qualifier, limit/pot-limit/no-limit structure, and the mandatory two-hole/three-board construction rule.

### Deal and play

1. Deal four hole cards to each player.
2. Run preflop betting, then deal a three-card flop and bet.
3. Deal and bet a turn card, then a river card.
4. At showdown, every player must use exactly two hole cards and exactly three board cards to make the five-card hand.

**Winning condition:** In Omaha high, the best high hand wins. In Omaha high-low, the best high and qualifying low split; a player may scoop both.

**Variations:**

- Pot-Limit Omaha.
- Omaha Eight-or-Better high-low.
- Five-card or six-card Omaha, with exactly two hole cards still required.
- Courchevel, in which one flop card is exposed before preflop betting.

> **Game tip:** The board does not play by itself. Reconstruct every candidate hand with exactly two hole cards and three board cards before calling a straight, flush, or full house.

**Source:** [OnlinePoker.net - Omaha](https://www.onlinepoker.net/games/omaha)

[Back to quick index](#quick-index)

---

<a id="omaha-burn"></a>
## 21. Omaha Burn

**Family:** Omaha with drop-and-match decision

**Players:** 2-11

**Pot format:** Continuing pot; players who remain through the burn decision and lose match the pot, subject to a cap.

**Wild / kill / pay cards:** No wild cards by default.

**Call before the deal:** Omaha high or high-low, exact hand-construction rule, timing and secrecy of the burn/drop declaration, match cap, and tie treatment.

### Deal and play

1. Deal and play Omaha through the turn under the called betting structure.
2. Before the river, all live players simultaneously declare whether to burn/drop out or remain in.
3. Deal the river to the remaining players and complete any final betting required by the house rule.
4. Show down. The winner takes the current pot; each losing player who stayed in matches the pot into the continuing bank.

**Winning condition:** The best legal Omaha hand among the players who stayed in wins the current pot. The game continues if matched money remains.

**Variations:**

- Omaha Eight-or-Better Burn.
- Move the burn decision to after the flop.
- Let a sole remaining player take the pot immediately without a river.
- Cap matches at one pot, a fixed amount, or a number of antes.

> **Game tip:** The river is only one card; price the decision on made equity and matching liability, not on hope. A hard cap is essential.

**Source:** [OnlinePoker.net - Omaha Burn](https://www.onlinepoker.net/games/omaha-burn)

[Back to quick index](#quick-index)

---

<a id="outhouse"></a>
## 22. Outhouse

**Family:** Progressive side-pot and main-pot poker

**Players:** 2-7

**Pot format:** One main pot plus staged side pots funded by split wagers.

**Wild / kill / pay cards:** No wild cards by default. Ordinary flushes do not count under the source rules, but a straight flush still does.

**Call before the deal:** Ante, how every wager is divided between main and side pots, two-card ranking, the no-flush rule, and exactly when exposed pairs return to the deck and are reshuffled.

### Deal and play

1. Deal five cards face down to each player, one card at a time. Bet after the third, fourth, and fifth cards; split every wager equally between the current side pot and the main pot.
2. Each player selects and exposes two cards. The best two-card poker hand wins the first side pot. Return those exposed cards to the deck, reshuffle, and leave each player with three private cards.
3. Deal three more cards face down to each player, with a split betting round after each card. Each player now has six private cards; expose the best two-card holding and award the second side pot.
4. Return or recycle the second exposed pairs under the preannounced deck procedure. Deal three more cards face down to each player, again splitting each wager between the side pot and main pot.
5. Each player exposes a final two-card holding for the third side pot, then exposes the five cards left in hand for the main-pot showdown. Ignore ordinary flushes, but recognize a straight flush.

**Winning condition:** Three staged side pots go to the best two-card holdings, and the main pot goes to the best legal five-card hand - four winning opportunities in one deal.

**Variations:**

- Allow normal flushes.
- Award all side pots only at the final showdown.
- Use fixed side-pot contributions instead of splitting every wager.
- Play high-low on the main pot only.

> **Game tip:** Use separate, labeled chip stacks for every pot. Trying to reconstruct split wagers after the action is the fastest way to ruin this game.

**Source:** [OnlinePoker.net - Outhouse](https://www.onlinepoker.net/games/outhouse)

**Editorial note:** The source explicitly returns the first exposed pair to the deck and reshuffles. Later recycling is not stated as clearly, but it is necessary at larger tables; announce the complete recycling procedure before dealing.

[Back to quick index](#quick-index)

---

<a id="piranha"></a>
## 23. Piranha

**Family:** Omaha-like community match-the-pot

**Players:** 2-11

**Pot format:** Continuing pot; showdown losers match the pot, subject to a cap.

**Wild / kill / pay cards:** No wild cards by default.

**Call before the deal:** Ante, match cap, the simultaneous in/out procedure, tie treatment, and whether any five of the nine available cards may be used without an Omaha-style two-hole/three-board restriction.

### Deal and play

1. Deal four hole cards face down to each player, then place three community cards face up and two community cards face down.
2. Every player simultaneously declares in or out with the closed-fist chip procedure. The detailed source page does not specify an ordinary betting round before this declaration.
3. If two or more players are in, reveal the two down community cards. Each entrant makes the best five-card hand from the four hole cards and five board cards, with no requirement to use exactly two hole cards and three board cards.
4. The best hand takes the current pot. Every other entrant matches the pot, subject to the cap, to create the next pot.
5. Redeal and repeat until exactly one player declares in and takes the pot uncontested. If everyone declares out, apply the preannounced redeal rule.

**Winning condition:** A contested deal pays the current pot to the best entrant and replenishes it through matches; the continuing bank is finally scooped by a sole entrant.

**Variations:**

- Require standard Omaha two-hole/three-board construction.
- Run a burn/drop declaration before the last board card.
- High-low split.
- Cap matches at a fixed amount or one pot.

> **Game tip:** Do not import Omaha construction rules by habit. Piranha permits a broader card mix unless the dealer explicitly narrows it.

**Source:** [OnlinePoker.net - Piranha](https://www.onlinepoker.net/games/piranha)

[Back to quick index](#quick-index)

---

<a id="position-poker"></a>
## 24. Position Poker

**Family:** Seven-card stud with seat-assigned wilds

**Players:** 2-7

**Pot format:** Split pot when a qualifying assigned-rank spade is dealt down: half to the best poker hand and half to the spade qualifier. With two qualifiers, each receives one quarter under the source rules.

**Wild / kill / pay cards:** All 8s are wild. Each seat also receives a position rank: ace for the first player left of the dealer, then 2, 3, and so on. A designated spade tied to position can award half the pot if down, or trigger a cancellation/redeal if up.

**Call before the deal:** Seat-to-rank mapping, treatment of the dealer seat, whether the final card may be chosen up or down, the assigned-spade restart rule, and whether any wild cards are pay cards.

### Deal and play

1. Assign a position rank before the deal: ace to the first player left of the dealer, 2 to the next player, then 3, 4, and so on.
2. Deal two cards down and four cards up with stud-style betting. For the seventh card, each remaining player chooses face up or face down.
3. For each player, all 8s and all cards matching that player's assigned position rank are wild.
4. An assigned-rank spade dealt face down qualifies that player for half the pot at showdown, regardless of poker-hand strength. If two players qualify, each receives one quarter under the source rules.
5. If an assigned-rank spade is dealt face up, stop immediately and muck the hand. Only players still live at that moment re-ante and receive the redeal; players who had already folded remain excluded.
6. If the hand reaches showdown, award the unclaimed share to the best five-card poker hand.

**Winning condition:** The best five-card poker hand wins the poker-hand share; one or two players holding their assigned spade face down receive the special spade share.

**Variations:**

- Remove the special spade half-pot rule and use only position wilds.
- Make 8s natural and retain only the seat-assigned wild rank.
- Rotate position ranks by deal rather than by seat.
- Use a kill-card rule for the exposed designated spade instead of a full redeal.

> **Game tip:** Write the seat-to-rank assignments on a card before the deal. This game is not playable from memory once several position ranks and a special spade are active.

**Source:** [OnlinePoker.net - Position Poker](https://www.onlinepoker.net/games/position-poker)

[Back to quick index](#quick-index)

---

<a id="pregnant-3s"></a>
## 25. Pregnant 3s

**Family:** Five-card draw with many wilds

**Players:** 2-6 recommended

**Pot format:** Single pot.

**Wild / kill / pay cards:** 3s, 6s, and 9s are wild, for as many as twelve wild cards. Optional kill cards include a one-eyed jack or a called man-with-an-axe card.

**Call before the deal:** Ante, number and size of draws, whether drawing is compulsory, exact kill-card identities, whether wilds are pay cards, and natural-hand tie rules.

### Deal and play

1. Deal five cards face down to each player and bet.
2. Allow the called draw or draws, replacing the permitted number of cards.
3. Apply 3, 6, and 9 as wild ranks, plus any announced kill-card rule.
4. Complete the final betting round and show down.

**Winning condition:** The highest five-card poker hand wins, unless a kill card makes a hand ineligible.

**Variations:**

- One draw, double draw, or forced draw.
- Each wild costs one ante or a fixed chip amount.
- Add a one-eyed-jack kill card or remove all kill cards.
- Natural hands beat otherwise equal wild-assisted hands.

> **Game tip:** With twelve wilds, five of a kind is common and hand values compress near the top. Do not treat an ordinary full house as a premium holding.

**Source:** [OnlinePoker.net - Pregnant 3s](https://www.onlinepoker.net/games/pregnant-3s)

[Back to quick index](#quick-index)

---

<a id="razz"></a>
## 26. Razz

**Family:** Seven-card stud lowball

**Players:** 2-6

**Pot format:** Single pot.

**Wild / kill / pay cards:** No wild cards. Aces are low; straights and flushes are ignored in standard ace-to-five ranking.

**Call before the deal:** Ante, bring-in, betting limits, ace-to-five ranking, and whether a qualifier is required.

### Deal and play

1. Deal two cards down and one card up to each player.
2. Use the usual stud streets, dealing additional cards with betting after each street and a final card down.
3. At showdown, choose the lowest five-card combination from seven cards.

**Winning condition:** The lowest ace-to-five hand wins. A-2-3-4-5, the wheel, is best.

**Variations:**

- Deuce-to-seven Razz.
- Razzdugi or other split hybrids for an experienced group.
- Eight-or-better qualifier.

> **Game tip:** Visible low cards are partly blocked. A live 7 can be stronger than a dead 5 when several 5s are already exposed.

**Source:** [OnlinePoker.net - Razz](https://www.onlinepoker.net/games/razz)

[Back to quick index](#quick-index)

---

<a id="roll-your-own"></a>
## 27. Roll Your Own

**Family:** Stud with player-selected exposed cards

**Players:** 5-7

**Pot format:** Single pot.

**Wild / kill / pay cards:** No wild cards in the standard form.

**Call before the deal:** Ante, simultaneous exposure procedure, betting limits, and whether the player who opens each betting round rotates clockwise as in the source rules.

### Deal and play

1. Deal three cards face down to every player and complete the first betting round.
2. Each player selects one of the three cards and exposes it simultaneously. Bet again.
3. Deal a fourth card face down. Each player selects one of the remaining down cards to expose simultaneously, then bet. Rotate the player who opens the betting round clockwise under the source procedure.
4. Repeat the deal-one-down, expose-one cycle for the fifth and sixth cards. Each player should now show four cards and hold two down.
5. Deal the seventh card face down with no additional exposure. Complete the final betting round and show down the best five-card hand from four up cards and three down cards.

**Winning condition:** The highest five-card hand made from the seven-card holding wins.

**Variations:**

- High-low split.
- Roll two cards at selected stages.
- Shifting Sands, in which each player's first exposed rank becomes that player's wild rank.
- Force players to expose their lowest or highest card on a called street.

> **Game tip:** Expose cards for information control, not merely hand strength. Showing a card that blocks an opponent's likely draw can be more valuable than advertising your pair.

**Source:** [OnlinePoker.net - Roll Your Own](https://www.onlinepoker.net/games/roll-your-own)

[Back to quick index](#quick-index)

---

<a id="russian-poker"></a>
## 28. Russian Poker

**Family:** Thirteen-card arrangement / Chinese-poker style

**Players:** 2-4

**Pot format:** Three pot shares: bottom hand one quarter, middle hand one quarter, and top hand one half under the source rules.

**Wild / kill / pay cards:** No wild cards by default.

**Call before the deal:** Ante, hand-placement order, whether placement is open or closed, foul-hand penalty, tie treatment, and optional wild cards.

### Deal and play

1. Deal thirteen cards to each player.
2. Each player arranges a five-card top hand, five-card middle hand, and three-card bottom hand under the source naming convention.
3. The five-card hands must satisfy the called strength order, and the three-card hand must not violate the arrangement rule.
4. Compare corresponding rows among all players and award the stated pot fractions.

**Winning condition:** The strongest legal hand in each row wins that row's share. An illegal or fouled arrangement loses according to the called penalty.

**Variations:**

- Use standard Chinese Poker row naming and 1/3-1/3-1/3 scoring instead of the source fractions.
- Add royalties for premium hands.
- Open-face placement.
- One or more wild cards, with a natural-hand tie preference.

> **Game tip:** Set the weakest legal row first, then work upward. A spectacular top hand is worthless if it forces an illegal middle or bottom arrangement.

**Source:** [OnlinePoker.net - Russian Poker](https://www.onlinepoker.net/games/russian-poker)

[Back to quick index](#quick-index)

---

<a id="sevens-take-all"></a>
## 29. Sevens Take All

**Family:** Seven-card stud with special winning pair

**Players:** 2-7; 4-7 recommended

**Pot format:** Single pot.

**Wild / kill / pay cards:** No conventional wild cards. Any pair of 7s outranks every ordinary poker hand under the source rule.

**Call before the deal:** Ante, whether exactly one pair of 7s is required, how trips or four 7s rank, and how ties between multiple pairs of 7s are broken or split.

### Deal and play

1. Deal two cards down, then four cards up, with stud-style betting between streets.
2. Let each remaining player choose whether the seventh card is dealt face up or face down, then complete the last betting round.
3. At showdown, first identify every hand containing the called pair-of-7s condition.
4. If at least one qualifying pair of 7s exists, compare or split those hands under the called rule. Otherwise compare normal five-card poker hands.

**Winning condition:** A qualifying pair of 7s takes precedence; absent that pair, the highest standard five-card hand wins.

**Variations:**

- Any hand containing two 7s splits equally with every other such hand.
- Compare kickers among pair-of-7s hands.
- Trip 7s scoop automatically.
- Make 7s wild instead of giving the pair priority.

> **Game tip:** The entire game pivots on four cards. Track exposed 7s precisely; once three are visible, the special hand is either impossible or concentrated in one player.

**Source:** [OnlinePoker.net - Sevens Take All](https://www.onlinepoker.net/games/sevens-take-all)

[Back to quick index](#quick-index)

---

<a id="shifting-sands"></a>
## 30. Shifting Sands

**Family:** Roll-your-own stud with personal wild rank

**Players:** 2-7

**Pot format:** Single pot.

**Wild / kill / pay cards:** Each player's first chosen exposed card establishes that player's personal wild rank; all matching cards in that hand are wild.

**Call before the deal:** Ante, whether the first exposed card itself is wild, whether the personal wild rank can change, reveal order, and pay-card costs.

### Deal and play

1. Deal the opening private cards as in Roll Your Own.
2. Each player selects one card to expose. Its rank becomes that player's personal wild rank.
3. Continue the Roll Your Own dealing and exposure sequence, with betting after each stage.
4. At showdown, apply each player's personal wild rank and form the best five-card hand.

**Winning condition:** The highest five-card poker hand wins under player-specific wild rules.

**Variations:**

- The personal wild rank changes each time a player exposes a new card.
- Only one matching card may act as wild.
- First exposed card is natural but its matching ranks are wild.
- Wild cards are pay cards.

> **Game tip:** Choose the first exposed rank based on multiplicity, not face value. A paired low rank often creates more wild-card leverage than a lone ace.

**Source:** [OnlinePoker.net - Shifting Sands](https://www.onlinepoker.net/games/shifting-sands)

[Back to quick index](#quick-index)

---

<a id="stud"></a>
## 31. Stud

**Family:** Seven-card stud

**Players:** 2-6

**Pot format:** Single pot.

**Wild / kill / pay cards:** No wild cards in standard stud. Dealer-choice variations frequently add fixed, personal, changing, community, or pay-card wilds.

**Call before the deal:** Ante, bring-in, betting limits, number of cards, high or high-low, low qualifier, and any wild/pay/kill cards.

### Deal and play

1. Deal two cards face down and one card face up to each player.
2. Complete the bring-in and betting round.
3. Deal fourth, fifth, and sixth streets face up with betting after each street.
4. Deal seventh street face down, bet, and show down the best five-card hand from seven cards.

**Winning condition:** The highest five-card hand wins in standard stud; split variants award a low half under the called qualifier.

**Variations:**

- Five-card stud.
- Seven-card stud high-low or Eight-or-Better.
- Chicago High or Low.
- Baseball Stud: 3s and 9s wild, 4s can buy an extra card.
- Follow the Queen, Kings and Little Ones, or other changing-wild forms.

> **Game tip:** Door cards are public inventory. Recalculate which ranks and suits are live before every call, especially in split-pot and wild-card versions.

**Source:** [OnlinePoker.net - Stud](https://www.onlinepoker.net/games/stud)

[Back to quick index](#quick-index)

---

<a id="texas-holdem"></a>
## 32. Texas Hold'em

**Family:** Two-hole-card community poker

**Players:** 2-10

**Pot format:** Single pot.

**Wild / kill / pay cards:** No wild cards in standard Hold'em.

**Call before the deal:** Blinds or ante, fixed-limit/pot-limit/no-limit structure, stakes, and any unusual board or bomb-pot rule.

### Deal and play

1. Post blinds and deal two hole cards to each player.
2. Complete preflop betting, then deal a three-card flop and bet.
3. Deal the turn and bet, then the river and bet.
4. At showdown, make the best five-card hand from any combination of the two hole cards and five board cards; playing the board is allowed.

**Winning condition:** The highest five-card poker hand wins.

**Variations:**

- Fixed-limit, pot-limit, or no-limit Hold'em.
- Double-board Hold'em.
- Bomb pot with everyone anteing and action beginning on the flop.
- Pineapple or Crazy Pineapple with a third hole card and discard.

> **Game tip:** In a dealer-choice mix, announce the betting limit as clearly as the game. Most costly errors come from carrying a fixed-limit assumption into a no-limit hand.

**Source:** [OnlinePoker.net - Texas Hold'em](https://www.onlinepoker.net/games/texas-holdem)

[Back to quick index](#quick-index)

---

<a id="good-bad-ugly"></a>
## 33. The Good, The Bad, The Ugly

**Family:** Stud-derived wild, discard, and kill game; the source's written street count is internally inconsistent

**Players:** 2-7; 4-7 recommended

**Pot format:** Single pot.

**Wild / kill / pay cards:** The Good rank is wild, the Bad rank must be discarded, and the Ugly rank kills any hand containing it.

**Call before the deal:** Ante, whether to use the source's literal five-personal-card sequence or a completed seven-card-stud sequence, reveal timing, whether matching down cards are affected, and whether the Ugly kills immediately.

### Deal and play

1. Deal two cards face down to each player, place three center cards face down in a row, and complete the opening betting round.
2. Reveal the first center card as the Good. Its rank is wild. Deal one personal card face up to each player and bet.
3. Reveal the second center card as the Bad. Every player discards cards matching that rank. Deal another personal card face up and bet.
4. Reveal the third center card as the Ugly. Any player holding that rank is immediately killed and folds. Deal one final personal card face down to each survivor and complete the last betting round.
5. Show down the best five-card hand among survivors. Note that the written procedure above accounts for only five personal cards even though the page calls the game seven-card stud; a true seven-card version must add two preannounced up-card streets.

**Winning condition:** The highest five-card hand among players not killed by the Ugly card wins.

**Variations:**

- Ugly only kills matching exposed cards.
- Bad rank is ignored rather than physically discarded.
- Good card itself is wild, but matching ranks are natural.
- Reveal all three center cards at the start for a lower-variance version.

> **Game tip:** A strong early hand can become worthless. Preserve optionality until the Ugly rank is known, and do not expose dead-card information carelessly.

**Source:** [OnlinePoker.net - The Good, The Bad, The Ugly](https://www.onlinepoker.net/games/the-good-the-bad-the-ugly)

**Editorial note:** The source labels the game seven-card stud but its written sequence deals only five personal cards. The dealer must resolve that discrepancy before the first card is dealt.

[Back to quick index](#quick-index)

---

<a id="three-legged-race"></a>
## 34. Three Legged Race

**Family:** Multi-leg draw poker

**Players:** 2-6

**Pot format:** A continuing race bank, usually awarded only after one player wins the required number of legs.

**Wild / kill / pay cards:** No wild cards by default; the dealer may call a wild rank for one or all legs.

**Call before the deal:** Number of legs required, whether legs must be consecutive, ante and carryover, mandatory three-card discard, high/low structure, and any wild cards.

### Deal and play

1. Deal five-card draw and complete the opening betting round.
2. Require each live player to discard exactly three cards and draw three replacements.
3. Complete the final betting round and award one leg to the winning hand.
4. Keep the bank live and repeat deals until a player completes the called race condition.

**Winning condition:** The player who first wins the required number of legs takes the bank.

**Variations:**

- Best two of three legs.
- Three consecutive legs required.
- Alternate high and low legs.
- Call a different wild rank for each leg.
- Force every player to play all three legs with no folding after the draw.

> **Game tip:** A leg is not the same as the pot. Track leg ownership with physical markers so a contested deal does not become a memory argument.

**Source:** [OnlinePoker.net - Three Legged Race](https://www.onlinepoker.net/games/three-legged-race)

[Back to quick index](#quick-index)

---

<a id="two-more-inches"></a>
## 35. Two More Inches

**Family:** Five-card base plus two exposed cards; match-the-pot

**Players:** 4-7

**Pot format:** Continuing pot; losing entrants match the pot, subject to a cap.

**Wild / kill / pay cards:** No wild cards by default. A called rank can be wild when face up and can kill a hand when held face down.

**Call before the deal:** Ante, simultaneous in/out declaration, match cap, ranking of the seven-card holding, and any face-up-wild/face-down-kill rank.

### Deal and play

1. Deal five cards face down to each player. The detailed source page does not include a draw or an ordinary betting round before the declaration.
2. Players declare in or out. Use a simultaneous closed-fist chip procedure if the table wants to prevent positional signaling.
3. Deal two additional cards face up to every player who stayed in.
4. Each entrant makes the best five-card hand from seven cards. The winner takes the current pot; losing entrants match it into the continuing bank.
5. If everyone declares out, end the deal and have all players re-ante under the source rule.

**Winning condition:** The best five-card hand among entrants wins the current pot. The continuing bank ends when one player remains or another called condition is met.

**Variations:**

- Select a rank that is wild only when dealt face up and kills the hand when present face down.
- Use the two extra cards as community cards instead of personal cards.
- High-low split.
- Cap matches at one pot or a fixed amount.

> **Game tip:** Your five-card decision is only provisional because two exposed cards are coming. Stay in with hands that can improve broadly, not only with one narrow out.

**Source:** [OnlinePoker.net - Two More Inches](https://www.onlinepoker.net/games/two-more-inches)

[Back to quick index](#quick-index)

---

<a id="supplemental-calls"></a>
# Supplemental dealer calls

These four calls use the same template but sit outside the main count of 35. Five-Card Draw is the foundation for several indexed draw variants. High Chicago, Low Chicago, and Wild Widow are included because they are common home-game calls and were specifically relevant to the requested variation coverage.

## Supplemental quick index

| Game | Players | Family | Defining feature |
|---|---|---|---|
| [Five-Card Draw](#five-card-draw) | 2-6 recommended | Draw poker foundation | No wild cards by default. |
| [High Chicago](#high-chicago) | 2-7; 4-7 recommended | Seven-card stud split pot | No wild cards by default. |
| [Low Chicago](#low-chicago) | 2-7; 4-7 recommended | Seven-card stud split pot | No wild cards by default. |
| [Wild Widow](#wild-widow) | 4+; 4-6 recommended | Five-card draw with a shared wild-rank card | A face-up widow card establishes the wild rank. |

---

<a id="five-card-draw"></a>
## Five-Card Draw

**Family:** Draw poker foundation

**Players:** 2-6 recommended

**Pot format:** Single pot.

**Wild / kill / pay cards:** No wild cards by default.

**Call before the deal:** Ante or blinds, betting limit, maximum draw, whether the opener must retain proof, and any wild cards.

### Deal and play

1. Deal five cards face down to each player and complete an opening betting round.
2. Each remaining player discards zero to the called maximum and receives replacements.
3. Complete a final betting round and show down.

**Winning condition:** The highest five-card poker hand wins.

**Variations:**

- Jacks or Better opening qualifier.
- Double draw or triple draw.
- Ace-to-five or deuce-to-seven lowball.
- Wild Widow, deuces wild, joker wild, or other called wild-card forms.

> **Game tip:** Your draw size is public information. Balance obvious hand improvement with the story your discard count tells the table.

**Source:** [OnlinePoker.net - Five-Card Draw](https://www.onlinepoker.net/games/draw)

**Editorial note:** Supplemental foundation. It is not a separate entry in the 35-game Dealer's Choice index used for the main catalog.

[Back to quick index](#quick-index)

---

<a id="high-chicago"></a>
## High Chicago

**Family:** Seven-card stud split pot

**Players:** 2-7; 4-7 recommended

**Pot format:** Split pot: best five-card poker hand and highest spade dealt face down.

**Wild / kill / pay cards:** No wild cards by default.

**Call before the deal:** Ante, stud betting limits, whether an ace is the highest spade, what happens when no live player has a down-card spade, and whether one player may scoop.

### Deal and play

1. Deal and bet as in seven-card stud.
2. At showdown, identify the best five-card poker hand.
3. Separately identify the highest spade among cards that were dealt face down to live players.
4. Split the pot between those two winners; one player may win both halves.

**Winning condition:** Half goes to the best poker hand and half to the highest down-card spade.

**Variations:**

- High Chicago with declare.
- Award the spade half only if the player also has a qualifying poker hand.
- Use the highest spade in the full seven-card holding rather than down cards only.
- Add a wild-card Stud rule, but call whether a wild spade can claim the Chicago half.

> **Game tip:** Protect down-card information. A mediocre stud hand can still be worth continuing when you hold a concealed ace or king of spades.

**Source:** [OnlinePoker.org - Chicago High and Low](https://onlinepoker.org/dealers-choice/chicago-high-low/)

**Editorial note:** Supplemental call. OnlinePoker.net mentions Chicago as a Stud variation but does not provide a dedicated rule page in its 35-game index.

[Back to quick index](#quick-index)

---

<a id="low-chicago"></a>
## Low Chicago

**Family:** Seven-card stud split pot

**Players:** 2-7; 4-7 recommended

**Pot format:** Split pot: best five-card poker hand and lowest spade dealt face down.

**Wild / kill / pay cards:** No wild cards by default.

**Call before the deal:** Ante, stud betting limits, whether ace of spades or 2 of spades is considered lowest, what happens with no down-card spade, and scoop eligibility.

### Deal and play

1. Deal and bet as in seven-card stud.
2. At showdown, identify the best five-card poker hand.
3. Separately identify the lowest spade among cards that were dealt face down to live players, using the called ace rule.
4. Split the pot between the two winners; one player may win both halves.

**Winning condition:** Half goes to the best poker hand and half to the lowest down-card spade.

**Variations:**

- Ace of spades is low; 2 of spades is then next-lowest.
- Ace of spades is high, making 2 of spades the lowest.
- Low Chicago with declare.
- Use the lowest spade anywhere in the seven-card holding rather than down cards only.

> **Game tip:** The ace rule changes the value of the most important card in the game. Put A-low or A-high in the dealer call every time.

**Source:** [OnlinePoker.org - Chicago High and Low](https://onlinepoker.org/dealers-choice/chicago-high-low/)

**Editorial note:** Supplemental call. OnlinePoker.net mentions Chicago as a Stud variation but does not provide a dedicated rule page in its 35-game index.

[Back to quick index](#quick-index)

---

<a id="wild-widow"></a>
## Wild Widow

**Family:** Five-card draw with a shared wild-rank card

**Players:** 4 or more per the cited rules; 4-6 recommended for practical one-deck draw play

**Pot format:** Single pot.

**Wild / kill / pay cards:** A face-up widow card establishes the wild rank. House rules differ on whether the widow itself is usable or merely marks the rank.

**Call before the deal:** Ante, timing of the widow reveal, whether the widow card itself is wild and usable, whether all matching ranks are wild, draw size, and natural-hand tie preference.

### Deal and play

1. Deal five cards face down to each player and place one card face down in the center as the widow.
2. Complete the opening betting round, then expose the widow at the called time.
3. Treat cards matching the widow rank as wild; apply the called rule to the widow card itself.
4. Allow the final draw, complete the last betting round, and show down.

**Winning condition:** The highest five-card poker hand wins under the called widow rule.

**Variations:**

- Widow is only a marker; the other three cards of its rank are wild.
- Widow itself is a shared wild community card and matching ranks are wild.
- Spit in the Ocean: each player receives four cards and the widow acts as a fifth shared card.
- Widow rank is wild only if the player holds a natural card of that rank.

> **Game tip:** Do not say only Wild Widow. State whether the center card itself plays, because reputable rule sets differ on that exact point.

**Source:** [Bicycle Cards - Wild Widow Poker](https://bicyclecards.com/how-to-play/wild-widow-poker/); [Poker.com - Wild Widow](https://poker.com/game/draw-poker-games/wild-widow/)

**Editorial note:** Supplemental call. The two cited rule sets differ on whether the center card itself plays as a wild, so that point must be included in the dealer call.

[Back to quick index](#quick-index)

---

# House-rule checklist

Copy this block to the top of a shared note or print it beside the table:

```text
GAME:
DEALER:
PLAYERS / DECK LIMIT:
ANTE OR BLINDS:
BETTING LIMIT:
POT FORMAT:
CARDS PER PLAYER:
BOARD / REVEAL ORDER:
HAND-CONSTRUCTION RULE:
WILD CARDS:
PAY CARDS AND COST:
KILL CARDS AND EFFECT:
DECLARE / DROP METHOD:
MATCH-THE-POT CAP:
HIGH / LOW / SPLIT RULE:
TIES AND ODD CHIPS:
DECK-RECYCLING RULE:
```

# Repository maintenance

- Treat `catalog.md` as the editable master for game rules.
- Do not hand-edit files in `_games/`; the build script regenerates them from this document.
- Keep the bold field labels and the `##` game headings uniform so the parser can validate the catalog.
- Deployment and local-preview instructions are in the repository `README.md`.

# Source and accuracy notes

- Main scope: the 35-item OnlinePoker.net Dealer's Choice index.
- Detailed game pages were preferred over short index blurbs when they conflicted.
- Baseball's one-deck player count was corrected to the feasible range for a nine-card deal; the source's larger count would require a second deck or a reduced deal.
- The Good, The Bad, The Ugly is labeled seven-card stud, but its written procedure accounts for only five personal cards; both interpretations are disclosed.
- Outhouse explicitly recycles the first exposed pairs, while later recycling is implicit and must be called for a full table.
- Badugi and several foundation games use editorial player recommendations where the cited page does not provide a clear cap.
- Chicago and Wild Widow rules vary by room. Their dealer-call fields deliberately force the disputed ace, down-card, and widow-card details into the pre-deal announcement.
- Gambling can create financial harm. Set stakes and hard loss caps that every participant can comfortably afford, and comply with local law.

# Revision record

| Date | Revision |
|---|---|
| 2026-07-20 | Initial single-file catalog: 35 OnlinePoker.net index games plus four supplemental calls. |
| 2026-07-20 | GitHub Pages edition: generated game sub-pages, card catalog, search, filters, and deployment workflow. |
