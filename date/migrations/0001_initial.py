# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('gender', models.CharField(default=b'F', max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('status', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, b'Single'), (2, b'In a relationship'), (3, b'Married'), (4, b'Engaged'), (5, b'Divorced'), (6, b'Just Brokeup'), (7, b'Staying together for the kids'), (8, b'Too poor to breakup'), (9, b'Rebounding Hard " I need to feel validated and wanted"'), (10, b"Mentally dating a celebrity that doesn't know I exist"), (11, b'Waiting for a miracle'), (12, b'Playing the game'), (13, b'Stalking someone'), (14, b"It's over but only one of us knows it"), (15, b'Purely Physical'), (16, b'Purely Mental ')])),
                ('breakup', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, b'Wishful thinking'), (2, b'Social Media - Facebook/Twitter'), (3, b'Text'), (4, b'Phone'), (5, b'Through my lawyer'), (6, b'In person'), (7, b"Shit they still don't know I moved  in with their best friend.")])),
                ('romance', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, b'Buy Nutella, find spoon, eat'), (2, b'Refactoring code on a friday night'), (3, b'Going to couples counseling'), (4, b'Reading a romance novel to my cat'), (5, b'Meeting the in laws '), (6, b'Doing laundry'), (7, b'Installing Ubuntu Linux'), (8, b'Catching up on sleep'), (9, b'Participating in a (non irb approved) science experiment'), (10, b'Watching movies with a stranger over Skype.'), (11, b'Dumpster Diving')])),
                ('argues', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, b"Direct - Let's face it you need to know why you're wrong"), (2, b"Confrontational - Oh, no you didn't! Don't you date cross that m.. fu.. line."), (3, b"Avoidant - Omg I can't believe he/she like did that to me. I'm going to sit here and pretend like it didn't happen. That'll teach them."), (4, b"Passive Agressive - I'm not gonna get angry but (sooner or later) you're gonna know you did something bad. I'll make sure you know when we're about to do something you really want to do."), (5, b"Reconciliatory. Yeah right, I'm just buying time to plot my revenge"), (6, b"I don't argue, I learn. Meaning every time we fight I learn how to push your buttons, muahahaha")])),
                ('relation_kind', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, b'Old fashioned - 0 communication and lots of babies'), (2, b"Open. Let's never pretend we're gonna be each other's everything"), (3, b'Facebook Relationship - I just want my friends to know I can attract someone.'), (4, b'Craigslist Encounter - I like surprises and have really good health insurance. '), (5, b'Platonic - Everything besides talking is so gross and sexual'), (6, b'Committed to making each other miserable'), (7, b"Clandestine  - No one should know we're together. I mean no one."), (8, b"I don't really want one, but I'd like to date some miserable souls via this website for personal entertainment")])),
                ('relation_last', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, b"I don't do relationships"), (2, b'Before a relationship can end you gotta be in one.'), (3, b'Until I open my mouth'), (4, b"Shit, my phone's battery last longer than most of them"), (5, b"I don't chase them I replace em."), (6, b'I juggle several on tinder so they last longer'), (7, b'Typically they fail to meet my high standards within the first 3 months'), (8, b'Till I find someone better'), (9, b"Till I realize they're bonkers"), (10, b'I leave when I start fantasizing about (everyone) else.'), (11, b'Till I divorce them and take half their money'), (12, b"I'm old fashioned I'm waiting until marriage to be in a relationship and then it's till death do us part."), (14, b'Wait you mean, I can end a relationship?'), (15, b'Until they escape my dungeon!'), (16, b'Eternity.')])),
                ('core_beliefs', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, b"Relationships are like fat people, most of them don't work out. "), (2, b'I realize I have more of a chance finding waldo than getting into a relationship. '), (3, b"Can't live with 'em can't live without 'em. "), (4, b"There's a perfect someone out there waiting for me. My job is to kill their spouse."), (5, b'Are all about pain, suffering, and sacrifice.'), (6, b'Give me a reason to go to the bar.'), (7, b'They should be fun, have no down moments and make me feel like a prince/princess.'), (8, b'The hottest love has the coldest end!'), (9, b'A good relationship should be like watching the grass grow, dull and boring. ')])),
                ('right_person', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, b'Mommy and Daddy tell me'), (2, b'You stop comparing everyone to your ex.'), (3, b'you Have less than 10 complaints  per week about the person.'), (4, b'You stop watching sex in the city reruns. '), (5, b'When you can be in the same room with the other person. '), (6, b'Your co-workers are jealous'), (7, b'I have no clue, but I know you will tell me who the right person is because your the fucking bosses of match-making.')])),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
    ]
