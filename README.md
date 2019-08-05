# NFL Player Ids

This repo is an attempt to merge pro-football-reference roster information with nflscrapR player ids.

### Part 1: scraping pro-football-reference data

The nflplayerattr folder in this repo is a scrapy project. Assuming you have scrapy installed, it should be ready to crawl pro-football-reference rosters with the command ``` scrapy crawl pfr ```

### Part 2: merging ids with nflscrapR ids

Merging these sets of data was somewhat difficult, and I'm still working on validating accuracy. Unfortunately nflscrapR only gives the first initial of a player's name, which makes it hard when there are multiple J.Browns at the same position on the Arizona Cardinals for example. Also, pro-football-reference doesn't have complete positional data. Sometimes players with hybrid roles like Taysum Hill for the Saints or Kyle Juszczyk will give my merge process fits. Speaking of merge process, I:

1) made ids in the form of 'season' + 'team abbreviation' + 'first initial' + 'last name'

2) made a list of players I'm confident that I have right. For nflscrapR, I isolated players with more than 20 pass attempts and assumed they were QBs. If I merged in pro-football-focus data, and those players were also labeled QBs, then I marked them as QBs

3) Did the same for running backs and receivers. I did QBs first so that I could isolate players with over 50 rush attempts, and then subtract the QB list so that presumably all that were left were running backs.

4) About 89% of the reception rows were matched, 93% of the running rows in the dataset, and 99% of the passer rows in the dataset. I then merged in players without positions listed in pfr. So if the player had the same team, season, first initial, and last name, and they weren't already labeled as a Center or Kicker or something, they would match. Where this could fail is if there's a common first initial, last name like D. Williams that might match the wrong player on the same team.

5) Lastly, I merged in players with other positions labeled. This ends up matching in punters for example that attempt a pass. I assumed this was the most reckless merge, because anyone with the same season/team/first initial/last initial could be matched. For my application, I only need the top running backs, wide receivers, etc....so I don't really have to worry too much about it. I'm confident with a little work someone could get in the high 90%s of accuracy. Let me know if you do!
