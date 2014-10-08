from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

MY_STATUS = ((1, 'Single'),
            (2, 'In a relationship'),
            (3, 'Married'),
            (4, 'Engaged'),
            (5, 'Divorced'),
            (6, 'Just Brokeup'),
            (7, 'Staying together for the kids'),
            (8, 'Too poor to breakup'),
            (9, 'Rebounding Hard \" I need to feel validated and wanted\"'),
            (10, 'Mentally dating a celebrity that doesn\'t know I exist'),
            (11, 'Waiting for a miracle'),
            (12, 'Playing the game'),
            (13, 'Stalking someone'),
            (14, 'It\'s over but only one of us knows it'),
            (15, 'Purely Physical'),
            (16, 'Purely Mental '))

LAST_BREAKUP = ((1, 'Wishful thinking'),
            (2, 'Social Media - Facebook/Twitter'),
            (3, 'Text'),
            (4, 'Phone'),
            (5, 'Through my lawyer'),
            (6, 'In person'),
            (7, 'Shit they still don\'t know I moved  in with their best friend.'))

ROMANCE = ((1, 'Buy Nutella, find spoon, eat'),
           (2, 'Refactoring code on a friday night'),
            (3, 'Going to couples counseling'),
            (4, 'Reading a romance novel to my cat'),
            (5, 'Meeting the in laws '),
            (6, 'Doing laundry'),
            (7, 'Installing Ubuntu Linux'),
            (8, 'Catching up on sleep'),
            (9, 'Participating in a (non irb approved) science experiment'),
            (10, 'Watching movies with a stranger over Skype.'),
            (11, 'Dumpster Diving'))

ARGUES = ((1, 'Direct - Let\'s face it you need to know why you\'re wrong'),
            (2, 'Confrontational - Oh, no you didn\'t! Don\'t you date cross that m.. fu.. line.'),
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
            (7, 'Typically they fail to meet my high standards within the first 3 months'),
            (8, 'Till I find someone better'),
            (9, 'Till I realize they\'re bonkers'),
            (10, 'I leave when I start fantasizing about (everyone) else.'),
            (11, 'Till I divorce them and take half their money'),
            (12, 'I\'m old fashioned I\'m waiting until marriage to be in a relationship and then it\'s till death do us part.'),
            (14, 'Wait you mean, I can end a relationship?'),
            (15, 'Until they escape my dungeon!'),
            (16, 'Eternity.'),)

CORE_BELIEFS = ((1, 'Relationships are like fat people, most of them don\'t work out. '),
            (2, 'I realize I have more of a chance finding waldo than getting into a relationship. '),
            (3, 'Can\'t live with \'em can\'t live without \'em. '),
            (4, 'There\'s a perfect someone out there waiting for me. My job is to kill their spouse.'),
            (5, 'Are all about pain, suffering, and sacrifice.'),
            (6, 'Give me a reason to go to the bar.'),
            (7, 'They should be fun, have no down moments and make me feel like a prince/princess.'),
            (8, 'The hottest love has the coldest end!'),
            (9, 'A good relationship should be like watching the grass grow, dull and boring. '),)

RELATION_KIND = ((1, 'Old fashioned - 0 communication and lots of babies'),
            (2, 'Open. Let\'s never pretend we\'re gonna be each other\'s everything'),
            (3, 'Facebook Relationship - I just want my friends to know I can attract someone.'),
            (4, 'Craigslist Encounter - I like surprises and have really good health insurance. '),
            (5, 'Platonic - Everything besides talking is so gross and sexual'),
            (6, 'Committed to making each other miserable'),
            (7, 'Clandestine  - No one should know we\'re together. I mean no one.'),
            (8, 'I don\'t really want one, but I\'d like to date some miserable souls via this website for personal entertainment'),)

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
    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    paid = models.BooleanField(default=False)
    location = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='static/img/', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F')
    status = models.IntegerField(max_length=2, choices=MY_STATUS, null=True, blank=True)
    breakup = models.IntegerField(max_length=2, choices=LAST_BREAKUP, null=True, blank=True)
    romance = models.IntegerField(max_length=2, choices=ROMANCE, null=True, blank=True)
    argues = models.IntegerField(max_length=2, choices=ARGUES, null=True, blank=True)
    relation_kind= models.IntegerField(max_length=2, choices=RELATION_KIND, null=True, blank=True)
    relation_last = models.IntegerField(max_length=2, choices=RELATION_LAST, null=True, blank=True)
    core_beliefs = models.IntegerField(max_length=2, choices=CORE_BELIEFS, null=True, blank=True)
    right_person = models.IntegerField(max_length=2, choices=RIGHT_PERSON, null=True, blank=True)


