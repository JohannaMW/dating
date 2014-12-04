from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField


AGE = ((1, 'Barely Legal'),
            (2, '20\'s, loving it & getting in debt'),
            (3, '30\'s wishing I was 20'),
            (4, '40\'s wishing I was 30'),
            (5, '50\'s --- about to buy a sports car and/or get plastic surgery'),
            (6, 'Curmudgeon'),
            (7, 'Over the hill'),
            (8, 'Old Fart'),
            (9, 'Fucked'))

GENDER = ((1, 'Alien'),
            (2, 'Animal'),
            (3, 'Female'),
            (4, 'Male'),
            (5, 'Other'))

LOCATION = ((1, 'Bus'),
            (2, 'Campground'),
            (3, 'Cementary'),
            (4, 'Data Center (probably hosted by amazon, maybe dropbox, or even rackspace)'),
            (5, 'Disney Fairytale'),
            (6, 'Dorm'),
            (7, 'Jail'),
            (8, 'Nearby galaxy'),
            (9, 'Parent\'s house'),
            (10, 'Second Life'))

MY_STATUS = ((1, 'Single'),
            (2, 'Depends on who\'s asking'),
            (3, 'Who cares I\'m awesome'),
            (4, 'Long distance relationship, because my boyfriend/girlfriend lives in the future.'),
            (5, 'In a relationship'),
            (6, 'In a relationship, but creeping on the inside'),
            (7, 'Married'),
            (8, 'Engaged'),
            (9, 'Divorced'),
            (10, 'Just Broke-up'),
            (11, 'Staying together for the kids'),
            (12, 'Too poor to breakup'),
            (13, 'Rebounding Hard \" I need to feel validated and wanted\"'),
            (14, 'Mentally dating a celebrity that doesn\'t know I exist'),
            (15, 'Waiting for a miracle'),
            (16, 'Playing \"the game\"'),
            (17, 'Stalking someone'),
            (18, 'It\'s over but only one of us knows it'),
            (19, 'In a purely physical relationship'),
            (20, 'In a purely mental relationship'),
            (21, 'One bad relationship away from having 30 cats. '),
            (22, 'Sexually Forsaken'),
            (23, 'Vulnerable'))

FAMILY = ((1, 'Nonexistent - they abandoned me hoping I would become the next Steve Jobs'),
           (2, 'Pathetic - They\'re losers, I\'m better than them and they know it. '),
            (3, 'Love 20% - Hate 80%'),
            (4, 'Full of gratitude - They made me the intolerable beast I am today.'),
            (5, 'Daddy Issues'),
            (6, 'Mommy Issues'),
            (7, 'Favorite Child'),
            (8, 'Forgotten Child'),
            (9, 'Least Favorite Child'),
            (10, 'Spoiled Rotten'),
            (11, 'Purely antagonistic - I\'m planning on killing them during Thanksgiving.'))

LAST_BREAKUP = ((1, 'Wishful thinking'),
            (2, 'Social Media - Facebook/Twitter'),
            (2, 'Flyer on lamp post'),
            (3, 'Text'),
            (2, '1-800-Collect'),
            (4, 'Phone'),
            (5, 'Through my lawyer'),
            (2, 'Via friends'),
            (6, 'In person'),
            (7, 'Shit they still don\'t know I moved  in with their best friend.'))

ROMANCE = ((1, 'Buy Nutella, find spoon, eat'),
           (2, 'Refactoring code on a friday night'),
            (3, 'Going to couples counseling'),
            (4, 'Reading a romance novel to my cat'),
            (5, 'Meeting the in laws '),
            (6, 'Doing laundry (at a coin laundry)'),
            (7, 'Attending a divorce court hearing'),
            (8, 'Installing Ubuntu Linux'),
            (9, 'Playing truth or dare'),
            (10, 'Catching up on sleep'),
            (11, 'Participating in a (non irb approved) science experiment'),
            (12, 'Watching movies with a stranger over Skype.'),
            (13, 'Feeding the homeless.'),
            (14, 'Dumpster Diving'))

ARGUES = ((1, 'Direct - Let\'s face it you need to know why you\'re wrong'),
            (2, 'Confrontational - Oh, no you didn\'t! Don\'t you dare cross that m.. fu.. line. Get ready to rumble.'),
            (3, 'Avoidant - Omg I can\'t believe he/she like did that to me. I\'m going to sit here and pretend '
                  'like it didn\'t happen. That\'ll teach them.'),
            (4, 'Passive Agressive - I\'m not gonna get angry but (sooner or later) you\'re gonna know you did something bad. '
                'I\'ll make sure you know when we\'re about to do something you really want to do.'),
            (5, 'Reconciliatory. Yeah right, I\'m just buying time to plot my revenge'),
            (6, 'I don\'t argue, I learn. Meaning every time we fight I learn how to push your buttons, muahahaha'))

RELATION_LAST = ((1, 'I don\'t do relationships'),
            (2, 'Before a relationship can end you gotta be in one.'),
            (3, 'Until I open my mouth'),
            (4, 'Shit, my phone\'s battery last longer than most of them'),
            (5, 'I don\'t chase them I replace em.'),
            (6, 'I juggle several on tinder so they last longer'),
            (7, 'Typically they fail to meet my high standards within the first 3 days'),
            (8, 'Till I find someone better'),
            (9, 'Till I realize they\'re bonkers'),
            (9, 'Till they realize I\'m bonkers'),
            (10, 'I leave when I start fantasizing about anyone else.'),
            (11, 'Till I divorce them and take half their money'),
            (12, 'I\'m old fashioned I\'m waiting until marriage to be in a relationship and then it\'s till death do us part.'),
            (14, 'Wait you mean, I can end a relationship?'),
            (15, 'Until they escape my dungeon!'),
            (16, 'Eternity.'),)

CORE_BELIEFS = ((1, 'Relationships are like fat people, most of them don\'t work out. '),
            (2, 'Only work after lawyering up.'),
            (3, 'I realize I have more of a chance finding waldo than getting into a relationship. '),
            (4, 'Can\'t live with \'em can\'t live without \'em. '),
            (5, 'There\'s a perfect someone out there waiting for me. My job is to kill their spouse.'),
            (6, 'Are all about pain, suffering, and sacrifice.'),
            (7, 'Are all about bom chicka wah wah!'),
            (8, 'They give me a reason to go to the bar.'),
            (9, 'They should be fun, free of drama and make me feel like a prince/princess.'),
            (10, 'The hottest love has the coldest end!'),
            (11, 'A good relationship should be like watching the grass grow, dull and boring. '),
            (12, 'Marriage lets you annoy one special person for the rest of your life. '),)

RELATION_KIND = (
            (1, 'Backup - I\'m already in a relationship but want to have a backup plan in case this one fails.'),
            (1, 'Old fashioned - 0 communication and lots of babies'),
            (1, 'Miserable - Committed to making each other miserable'),
            (2, 'Open. Let\'s never pretend we\'re gonna be each other\'s everything'),
            (3, 'Social media relationship - I just want my friends to know I can attract someone.'),
            (4, 'Craigslist Encounter - I like surprises and have really good health insurance. '),
            (5, 'Platonic - Everything besides talking is so gross and sexual'),
            (6, 'Committed to making each other miserable'),
            (7, 'Clandestine  - No one should know we\'re together. I mean no one.'),
            (7, 'Tragic - I\'d like to date some miserable souls via this website for personal entertainment'),
            (7, 'Wedding appearance - I just want someone who will go to weddings with me so I don\'t feel pathetic. '),
            (8, 'I don\'t really want one, but I\'d like to date some miserable souls via this website for personal entertainment'),)

IN_RELATIONSHIP = ((1, 'Thinking about my next relationship'),
           (2, 'Avoidant'),
            (3, 'Needy'),
            (4, 'Distant'),
            (5, 'Annoying'),
            (6, 'Emotionally volatile'),
            (7, 'Condescending'),
            (8, 'Know-It-All'),
            (9, 'Bundle of love'),
            (10, 'Depressed'))

RIGHT_PERSON = ((1, 'Mommy and Daddy tell me'),
            (2, 'You stop comparing everyone to your ex.'),
            (3, 'you Have less than 10 complaints  per week about the person.'),
            (4, 'You stop watching sex in the city reruns. '),
            (5, 'When you can be in the same room with the other person. '),
            (6, 'Your co-workers are jealous'),
            (7, 'I have no clue, but I know you will tell me who the right '
                  'person is because your the fucking bosses of match-making.'),)

#class Location(models.Model):
 #   name = models.CharField(max_length=100)

class Single(AbstractUser):
    paid = models.BooleanField(default=False)
    location = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(max_length=2, choices=AGE, null=True, blank=True)
    image = models.ImageField(upload_to='static/img/', null=True, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER, null=True, blank=True)
    family = models.IntegerField(max_length=2, choices=FAMILY, null=True, blank=True)
    status = models.IntegerField(max_length=2, choices=MY_STATUS, null=True, blank=True)
    breakup = models.IntegerField(max_length=2, choices=LAST_BREAKUP, null=True, blank=True)
    romance = models.IntegerField(max_length=2, choices=ROMANCE, null=True, blank=True)
    argues = models.IntegerField(max_length=2, choices=ARGUES, null=True, blank=True)
    relation_kind= models.IntegerField(max_length=2, choices=RELATION_KIND, null=True, blank=True)
    relation_last = models.IntegerField(max_length=2, choices=RELATION_LAST, null=True, blank=True)
    core_beliefs = models.IntegerField(max_length=2, choices=CORE_BELIEFS, null=True, blank=True)
    in_relationship = models.IntegerField(max_length=2, choices=IN_RELATIONSHIP, null=True, blank=True)
    right_person = models.IntegerField(max_length=2, choices=RIGHT_PERSON, null=True, blank=True)
