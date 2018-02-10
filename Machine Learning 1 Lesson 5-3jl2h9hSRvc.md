[okay so welcome back so we're going to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m00s)
00:00:00

[start by doing some review and we're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m02s)
00:00:02

[going to talk about test sets training](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m04s)
00:00:04

[sets validation sets and oob something](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m09s)
00:00:09

[we haven't covered yet but we will cover](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m14s)
00:00:14

[in more detail later is also cross](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m16s)
00:00:16

[validation but I'm going to talk about](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m19s)
00:00:19

[that as well right so we have a data set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m20s)
00:00:20

[with a bunch of rows in it and we've got](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m25s)
00:00:25

[some dependent variable and so what's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m29s)
00:00:29

[the difference between my machine](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m34s)
00:00:34

[learning and kind of pretty much any](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m37s)
00:00:37

[other kind of work that the the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m41s)
00:00:41

[difference is that in machine learning](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m44s)
00:00:44

[the thing we care about is the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m46s)
00:00:46

[generalization accuracy or the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m48s)
00:00:48

[generalization error where else in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m50s)
00:00:50

[pretty much everything else all we care](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m52s)
00:00:52

[about is is how well we could have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m55s)
00:00:55

[mapped to the observations all stop and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h00m58s)
00:00:58

[so this this thing about generalization](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m01s)
00:01:01

[is the key unique piece of with machine](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m04s)
00:01:04

[learning and so if we want to know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m08s)
00:01:08

[whether we could doing a good job of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m11s)
00:01:11

[machine learning we need to do know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m12s)
00:01:12

[whether we're doing a good job of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m14s)
00:01:14

[generalizing if we don't know that we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m16s)
00:01:16

[know nothing right](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m19s)
00:01:19

[by generalizing do you mean like scaling](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m25s)
00:01:25

[being able to scale larger no III don't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m28s)
00:01:28

[mean scaling at all so scaling is an](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m31s)
00:01:31

[important thing in many many areas it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m34s)
00:01:34

[like okay we've got something that works](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m36s)
00:01:36

[I'm on my computer with ten thousand](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m38s)
00:01:38

[items I do need to work make it work on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m42s)
00:01:42

[ten thousand items per second or](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m45s)
00:01:45

[something so scaling is important but](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m46s)
00:01:46

[not just a machine learning for just](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m49s)
00:01:49

[about everything we put in production](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m51s)
00:01:51

[generalization is where I say okay here](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m53s)
00:01:53

[is a model that can predict cats from](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h01m57s)
00:01:57

[dogs I've looked at five pictures of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m01s)
00:02:01

[cats five pictures of dogs and I've](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m03s)
00:02:03

[built a model that is perfect and then I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m05s)
00:02:05

[look at a different set of five cats and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m08s)
00:02:08

[dogs and it gets them all wrong so in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m10s)
00:02:10

[that case when it learned was not a good](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m13s)
00:02:13

[Street a cat and a dog that it learned](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m14s)
00:02:14

[what those five exact cats looked like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m16s)
00:02:16

[in those five exact dogs the play or I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m18s)
00:02:18

[built a model of predicting grocery](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m21s)
00:02:21

[sales for a particular product so for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m25s)
00:02:25

[toilet rolls in New Jersey last month](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m30s)
00:02:30

[and then I go and put it into production](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m34s)
00:02:34

[and it scales great in other words it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m37s)
00:02:37

[can have the great latency I don't have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m39s)
00:02:39

[a high CPU load but it fails to predict](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m41s)
00:02:41

[anything well other than toilet rolls in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m45s)
00:02:45

[New Jersey it also it turns out it only](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m48s)
00:02:48

[did it well for last month not the next](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m50s)
00:02:50

[month so these are all generalization](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m52s)
00:02:52

[failures so the most common way that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h02m54s)
00:02:54

[people check for the ability to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m00s)
00:03:00

[generalize is to create a random sample](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m03s)
00:03:03

[so they'll grab a few rows at random and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m07s)
00:03:07

[pull it out into a test set and then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m11s)
00:03:11

[they'll build all of their models on the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m18s)
00:03:18

[rest of the rows and then when they're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m20s)
00:03:20

[finished they'll check that the accuracy](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m24s)
00:03:24

[they got on there so the rest of the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m27s)
00:03:27

[rows are called the training set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m29s)
00:03:29

[everything else everything](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m30s)
00:03:30

[else we could call the training set and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m33s)
00:03:33

[so at the end of their modeling process](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m41s)
00:03:41

[on the training set they got an accuracy](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m43s)
00:03:43

[of 99 percent of predicting cats from](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m45s)
00:03:45

[dogs at the very end they check it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m48s)
00:03:48

[against a test set to make sure that the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m50s)
00:03:50

[model really does generalize now the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m52s)
00:03:52

[problem is what if it doesn't right so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m54s)
00:03:54

[okay well I could go back and change](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h03m59s)
00:03:59

[some hyper parameters do some data](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m01s)
00:04:01

[augmentation and whatever else try to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m03s)
00:04:03

[create a more generalizable model and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m05s)
00:04:05

[then I'll go back again after doing all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m07s)
00:04:07

[that and check and it's still no good](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m09s)
00:04:09

[and I'll keep doing this again and again](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m12s)
00:04:12

[until eventually after fifty attempts it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m14s)
00:04:14

[does generalize but does it really](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m18s)
00:04:18

[generalize because maybe all I've done](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m21s)
00:04:21

[is accidentally found this one which](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m23s)
00:04:23

[happens to work just for that test set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m25s)
00:04:25

[because I've tried 50 different things](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m27s)
00:04:27

[right and so if I've got something which](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m28s)
00:04:28

[is like right coincidentally 0.05 5](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m31s)
00:04:31

[percent of the time they're not very](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m36s)
00:04:36

[likely to accidentally get a good result](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m38s)
00:04:38

[so what we generally do is we put aside](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m40s)
00:04:40

[a second data set they'll get a couple](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m44s)
00:04:44

[more of these and put these aside into a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m49s)
00:04:49

[validation set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m53s)
00:04:53

[it's an audacious set right and then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m55s)
00:04:55

[everything that's not in the validation](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m58s)
00:04:58

[or tests is now training and so what we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h04m59s)
00:04:59

[do is we train a model check it against](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m02s)
00:05:02

[the validation to see if it generalizes](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m04s)
00:05:04

[do that a few times and then when we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m06s)
00:05:06

[finally got something we were like okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m09s)
00:05:09

[we think this generalizes successfully](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m11s)
00:05:11

[based on the validation set and then at](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m13s)
00:05:13

[the end of the project we check it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m14s)
00:05:14

[against the test set yeah so basically](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m16s)
00:05:16

[if I making this two layer test that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m20s)
00:05:20

[validation said if he gets one right the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m22s)
00:05:22

[other one wrong you're kind of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m24s)
00:05:24

[double-checking your errors it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m25s)
00:05:25

[checking that we have an overfit to the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m28s)
00:05:28

[validation set so if we're using the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m30s)
00:05:30

[validation set again and again then we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m32s)
00:05:32

[could end up not coming up with a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m35s)
00:05:35

[generalizable sort of hyper parameters](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m37s)
00:05:37

[and a set of private creditors that just](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m38s)
00:05:38

[so happened to work on the training set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m40s)
00:05:40

[and the validation set so so if we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m41s)
00:05:41

[try 50 different models against the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m46s)
00:05:46

[validation set and then at the end of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m52s)
00:05:52

[all that we then check that against the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m54s)
00:05:54

[test set and it's still generalized as](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m55s)
00:05:55

[well then we're kind of going to say](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m57s)
00:05:57

[okay that's good we've actually come up](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h05m59s)
00:05:59

[with generalizable model if it doesn't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m00s)
00:06:00

[then that's going to say okay we've](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m03s)
00:06:03

[actually now overfit to the validation](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m04s)
00:06:04

[set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m05s)
00:06:05

[at which point you're kind of in trouble](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m06s)
00:06:06

[right because you don't you know you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m08s)
00:06:08

[don't have anything left behind right so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m12s)
00:06:12

[the idea is to use effective techniques](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m15s)
00:06:15

[during the modeling so that so that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m19s)
00:06:19

[doesn't happen right but but if it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m21s)
00:06:21

[going to happen you want to find out](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m22s)
00:06:22

[about it like you need that test set to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m24s)
00:06:24

[be there because otherwise when you put](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m26s)
00:06:26

[it in production and then it turns out](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m27s)
00:06:27

[that it doesn't generalize that would be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m30s)
00:06:30

[a really bad outcome right you end up](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m32s)
00:06:32

[with less people clicking on your ads or](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m34s)
00:06:34

[selling less with your products or](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m36s)
00:06:36

[providing car insurance to very risky](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m38s)
00:06:38

[vehicles or whatever so just make sure](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m41s)
00:06:41

[to need to ever check if the validation](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m44s)
00:06:44

[set and the test antics is coherent or](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m47s)
00:06:47

[you just keep tested so if you've done](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m50s)
00:06:50

[what I've just done here which is to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m53s)
00:06:53

[randomly sample there's no particular](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m55s)
00:06:55

[reason to check as long as there as long](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m57s)
00:06:57

[as they're big enough right but we're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h06m59s)
00:06:59

[going to come back to your question in a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m00s)
00:07:00

[different context in just a moment now](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m03s)
00:07:03

[another trick we've learned for renin](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m10s)
00:07:10

[forests is a way of not needing a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m12s)
00:07:12

[validation set and the way what we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m15s)
00:07:15

[learnt was to use instead use the oob](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m18s)
00:07:18

[era for the OO be scored and so this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m22s)
00:07:22

[idea was to say well every time we train](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m26s)
00:07:26

[a tree in a random forest there's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m29s)
00:07:29

[bunch of observations that are held out](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m31s)
00:07:31

[anyway because that's how we get some of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m33s)
00:07:33

[the randomness and so let's calculate](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m35s)
00:07:35

[our score for each tree based on those](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m38s)
00:07:38

[held out samples and therefore the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m41s)
00:07:41

[forest by averaging the trees that that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m43s)
00:07:43

[each row was not part of training okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m46s)
00:07:46

[and so the oob score gives us something](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m51s)
00:07:51

[which is pretty similar to the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m54s)
00:07:54

[validation score but on average it's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h07m58s)
00:07:58

[little less good can anybody either](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m03s)
00:08:03

[remember or figure out why on average](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m06s)
00:08:06

[it's a little less good quite a subtle](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m08s)
00:08:08

[one don't give it to Kenji I'm not sure](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m12s)
00:08:12

[but is it because you are treating like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m16s)
00:08:16

[you're doing every kind of probe](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m19s)
00:08:19

[pre-processing on your tests and so the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m22s)
00:08:22

[OB score is reflecting the performance](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m26s)
00:08:26

[on testing set no for the other piece](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m30s)
00:08:30

[because not using the test set at all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m32s)
00:08:32

[the other Peace Corps is using the held](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m34s)
00:08:34

[out rows in the training set at page](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m36s)
00:08:36

[tree so I mean Z you are basically](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m38s)
00:08:38

[testing each tree of some data from Z](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m41s)
00:08:41

[training set yes so you are you have the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m44s)
00:08:44

[potential of over feeding with agents it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m47s)
00:08:47

[shouldn't cause overfitting because each](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m52s)
00:08:52

[one is looking at a held out sample so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m54s)
00:08:54

[it's not an overfitting issue it's quite](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m57s)
00:08:57

[a subtle issue](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h08m59s)
00:08:59

[Enes through never trained aren't this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m00s)
00:09:00

[sample is from OB bootstrap samples they](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m05s)
00:09:05

[also then you're never gonna grab 63% of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m08s)
00:09:08

[writes chance to OB is one minus 63](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m12s)
00:09:12

[percent exactly yeah both you sure so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m16s)
00:09:16

[then if you know why would the score be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m19s)
00:09:19

[lower than the validation school and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m21s)
00:09:21

[then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m23s)
00:09:23

[that you're leaving sort of like a black](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m23s)
00:09:23

[hole in the data that there's like there](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m25s)
00:09:25

[two points you're never going to sample](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m26s)
00:09:26

[and I'm not gonna be represented by the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m27s)
00:09:27

[model ah no that's not true though](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m28s)
00:09:28

[because each tree is looking at a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m30s)
00:09:30

[different set right so that I won't be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m32s)
00:09:32

[so like we've got like I don't know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m33s)
00:09:33

[dozens of models right and a niche one](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m36s)
00:09:36

[there's a different set of rows which](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m38s)
00:09:38

[which happened to be held out right and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m43s)
00:09:43

[so when we calculate the oeob score for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m48s)
00:09:48

[like let's say row three we say okay row](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m51s)
00:09:51

[three is in this tree this tree and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m54s)
00:09:54

[that's it and so we calculate the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h09m57s)
00:09:57

[prediction on that tree and for that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m00s)
00:10:00

[tree and we'd average those two](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m02s)
00:10:02

[predictions and so with enough trees you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m04s)
00:10:04

[know each one has a 30 or so percent](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m08s)
00:10:08

[chance](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m10s)
00:10:10

[sorry forty or so percent chance that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m10s)
00:10:10

[the row is in that tree so if you have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m12s)
00:10:12

[fifty trees it's almost certain that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m14s)
00:10:14

[every row is going to be mentioned](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m17s)
00:10:17

[somewhere did you have an idea term](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m18s)
00:10:18

[which relevation said we can use the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m23s)
00:10:23

[whole forest to make the predictions but](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m25s)
00:10:25

[here we cannot use the whole forest so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m27s)
00:10:27

[we cannot exactly see exactly so every](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m29s)
00:10:29

[road is going to be using a subset of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m32s)
00:10:32

[the trees to make its prediction and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m36s)
00:10:36

[with less trees we know we get a less](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m38s)
00:10:38

[accurate prediction so that's that's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m40s)
00:10:40

[subtle one right and if you didn't get](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m43s)
00:10:43

[it have a think during the week until](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m45s)
00:10:45

[you understand why this is because it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m49s)
00:10:49

[a really interesting test of your](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m52s)
00:10:52

[understanding of random forests it like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m54s)
00:10:54

[why is our B score on average less good](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h10m56s)
00:10:56

[and your validation is for they're both](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m00s)
00:11:00

[using random subnet subsets anyway it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m02s)
00:11:02

[really close enough right so why have a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m07s)
00:11:07

[validation set at all when you're using](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m11s)
00:11:11

[random forests if it's a randomly chosen](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m15s)
00:11:15

[validation set it's not strictly](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m21s)
00:11:21

[speaking necessary but you know you've](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m23s)
00:11:23

[got like four levels of things to test](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m25s)
00:11:25

[right so you could like test on the oeob](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m27s)
00:11:27

[when that's working well you can test on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m29s)
00:11:29

[the validation set you know and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m31s)
00:11:31

[hopefully by the time you check against](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m33s)
00:11:33

[the test set there's going to be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m35s)
00:11:35

[surprises so that'll be one good reason](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m37s)
00:11:37

[then what cattle do the way they do this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m39s)
00:11:39

[is kind of clever](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m43s)
00:11:43

[while CAG will do is they split the test](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m44s)
00:11:44

[set into two pieces a public and a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m46s)
00:11:46

[private and they don't tell you which is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m50s)
00:11:50

[rich so you submit your predictions to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m53s)
00:11:53

[cattle and then a random 30% of those](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h11m56s)
00:11:56

[are used to tell you the leaderboard](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m00s)
00:12:00

[score but then at the end of the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m02s)
00:12:02

[competition that gets thrown away and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m06s)
00:12:06

[they use the other 70% to calculate your](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m08s)
00:12:08

[real score so what that's doing is that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m10s)
00:12:10

[you're making sure that you're not like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m15s)
00:12:15

[continually using that feedback from the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m16s)
00:12:16

[leaderboard to figure out some set of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m18s)
00:12:18

[hyper parameters that happens to do well](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m20s)
00:12:20

[on the public that actually doesn't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m22s)
00:12:22

[generalize okay so it's a great test](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m25s)
00:12:25

[like this is one of the reasons why it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m28s)
00:12:28

[good practice to use cattle because at](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m29s)
00:12:29

[the end of a competition at some point](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m32s)
00:12:32

[this will happen to you and you'll drop](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m34s)
00:12:34

[a hundred places on the leaderboard the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m36s)
00:12:36

[last day of the competition when they](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m38s)
00:12:38

[use the private test set and say oh okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m39s)
00:12:39

[that's what it feels like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m42s)
00:12:42

[to overfit and it's much better to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m44s)
00:12:44

[practice and get that sense there than](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m46s)
00:12:46

[it is to do it in a company where](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m48s)
00:12:48

[there's hundreds of millions of dollars](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m50s)
00:12:50

[on the line okay so this is like the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m52s)
00:12:52

[easiest possible situation where you're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h12m57s)
00:12:57

[able to use a random sample for your](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m00s)
00:13:00

[validation set why might I not be able](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m04s)
00:13:04

[to use a random sample from my](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m09s)
00:13:09

[validation set or possibly fail](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m10s)
00:13:10

[in the case of something where we're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m16s)
00:13:16

[forecasting we can't randomly sample](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m17s)
00:13:17

[because we need to maintain the temporal](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m19s)
00:13:19

[ordering hello what is that because it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m22s)
00:13:22

[doesn't it doesn't make sense so in the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m26s)
00:13:26

[case of like an ARMA model I can't use](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m27s)
00:13:27

[like I can't pull out random rows](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m31s)
00:13:31

[because there's I'm thinking that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m32s)
00:13:32

[there's like a certain dependency or I'm](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m36s)
00:13:36

[trying to model a certain dependency](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m38s)
00:13:38

[that relies on like a specific lag turn](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m40s)
00:13:40

[and if I randomly sample those things](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m42s)
00:13:42

[then that lag term isn't there for me to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m45s)
00:13:45

[okay so it could be like a technical](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m47s)
00:13:47

[modeling issue that like I'm using a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m51s)
00:13:51

[model that relies on like yesterday the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m54s)
00:13:54

[day before and the day before that and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m56s)
00:13:56

[if I randomly removed some things I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m58s)
00:13:58

[don't have yesterday and my model might](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h13m59s)
00:13:59

[just fail okay that's true but there's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m01s)
00:14:01

[more fundamental issue you want to pass](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m05s)
00:14:05

[it to Tyler and it's a really good point](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m06s)
00:14:06

[although you know in general we're going](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m10s)
00:14:10

[to try to build models that are not](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m12s)
00:14:12

[little more resilient than that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m14s)
00:14:14

[particularly with yet temporal order we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m16s)
00:14:16

[expect things that are close by in time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m21s)
00:14:21

[to be related to things close to them so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m23s)
00:14:23

[weeks so we destroy the water like if if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m27s)
00:14:27

[we destroy the order we really aren't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m33s)
00:14:33

[going to be able to use that this time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m36s)
00:14:36

[is close to this other time I don't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m38s)
00:14:38

[think that's true because I can pull out](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m41s)
00:14:41

[a random sample for a validation set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m43s)
00:14:43

[and still keep everything nicely ordered](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m45s)
00:14:45

[well lame reject things in the future](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m48s)
00:14:48

[which we would require as much data](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m51s)
00:14:51

[close to the hand alert okay that's true](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h14m56s)
00:14:56

[I mean we could be like limiting the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m00s)
00:15:00

[amount of data that we have by taking](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m02s)
00:15:02

[some of it out but my claim is stronger](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m05s)
00:15:05

[my claim is that by using a random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m08s)
00:15:08

[validation set we could get totally the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m10s)
00:15:10

[wrong idea about our model Caribou wanna](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m14s)
00:15:14

[have a try so if our data is imbalanced](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m16s)
00:15:16

[for example we can if you're randomly](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m23s)
00:15:23

[sampling it we can only](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m25s)
00:15:25

[one class in our validation set so our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m27s)
00:15:27

[fitted model maybe that's true as well](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m30s)
00:15:30

[so maybe you're trying to predict in a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m33s)
00:15:33

[medical situation who's going to die of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m34s)
00:15:34

[lung cancer and that's only one out of a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m36s)
00:15:36

[hundred people and we pick out a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m39s)
00:15:39

[validation set that we accidentally have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m40s)
00:15:40

[nobody that died of lung cancer that's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m43s)
00:15:43

[also true these are all good niche](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m45s)
00:15:45

[examples but none of them quite say like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m49s)
00:15:49

[why could the validation set just be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m52s)
00:15:52

[plain wrong like give you a totally](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m55s)
00:15:55

[inaccurate idea of whether this is going](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h15m59s)
00:15:59

[to generalize and so let's talk about](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m01s)
00:16:01

[and the closest is is what Tyler was](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m04s)
00:16:04

[saying about time closeness in time the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m07s)
00:16:07

[important thing to remember is when you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m11s)
00:16:11

[build a model you're always you always](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m13s)
00:16:13

[have a systematic error which is that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m16s)
00:16:16

[you're going to use the model at a later](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m19s)
00:16:19

[time than the time that you built it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m21s)
00:16:21

[right like you're going to put it into](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m23s)
00:16:23

[production by which time the world is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m26s)
00:16:26

[different to the world that you're in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m29s)
00:16:29

[now and even when you're building the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m31s)
00:16:31

[model you're using data which is older](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m33s)
00:16:33

[than today anyway right so there's some](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m35s)
00:16:35

[lag between the data that you're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m37s)
00:16:37

[building it on and the data that it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m39s)
00:16:39

[going to actually be used on your life](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m41s)
00:16:41

[and a lot of the time if not most of the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m43s)
00:16:43

[time that matters right so if we're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m46s)
00:16:46

[doing stuff in like predicting who's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m49s)
00:16:49

[going to buy toilet paper in New Jersey](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m52s)
00:16:52

[and it takes us two weeks to put it in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m54s)
00:16:54

[production and we did it using data from](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h16m57s)
00:16:57

[the last couple of years and by that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m01s)
00:17:01

[time you know things may look very](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m02s)
00:17:02

[different right and particularly our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m05s)
00:17:05

[validation said if we randomly sampled](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m09s)
00:17:09

[it right and it was like from a four](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m11s)
00:17:11

[year period then the vast majority of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m13s)
00:17:13

[that data is going to be over a year old](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m16s)
00:17:16

[right and it may be that the toilet](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m17s)
00:17:17

[buying habits of folks in New Jersey may](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m21s)
00:17:21

[have dramatically shifted maybe they've](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m24s)
00:17:24

[got a terrible recession there now and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m27s)
00:17:27

[they can't afford a high-quality toilet](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m29s)
00:17:29

[paper anymore or maybe they know their](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m31s)
00:17:31

[paper making industry has gone through](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m35s)
00:17:35

[the roof and suddenly you know they](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m37s)
00:17:37

[they're buying what's more toilet paper](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m39s)
00:17:39

[because it's so cheap or whatever right](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m40s)
00:17:40

[so the world changes and therefore if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m42s)
00:17:42

[you use a random sample for your](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m47s)
00:17:47

[validation set then you're actually](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m49s)
00:17:49

[checking how good are you at predicting](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m51s)
00:17:51

[things that are totally obsolete now but](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m53s)
00:17:53

[how good are you at predicting things](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m56s)
00:17:56

[that happened four years ago that's not](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h17m58s)
00:17:58

[interesting okay so what we want to do](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m00s)
00:18:00

[in practice anytime there's some temper](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m03s)
00:18:03

[or peace is to instead say assuming that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m07s)
00:18:07

[we've ordered it by time all right so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m13s)
00:18:13

[this is old and this is new](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m19s)
00:18:19

[that's our validation set okay or if we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m25s)
00:18:25

[you know I suppose actually do it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m31s)
00:18:31

[properly](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m33s)
00:18:33

[that's how a validation set that's our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m33s)
00:18:33

[test set make sense right so here's that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m36s)
00:18:36

[training set and we use that and we try](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m42s)
00:18:42

[and be able to model that still works on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m45s)
00:18:45

[stuff that's later in time than anything](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m47s)
00:18:47

[the model was built on and so we're not](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m51s)
00:18:51

[just testing generalization in some kind](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m53s)
00:18:53

[of abstract sense but in a very specific](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m56s)
00:18:56

[time sense which is it generalizes to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h18m58s)
00:18:58

[the future could you pass it to Suraj](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m01s)
00:19:01

[please](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m02s)
00:19:02

[so when we are as you said as you said](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m07s)
00:19:07

[there is some temporal ordering in the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m11s)
00:19:11

[data so in that case is it wise to take](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m13s)
00:19:13

[the entire full data for training or](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m15s)
00:19:15

[only a few recent data set for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m18s)
00:19:18

[validation test or training training](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m21s)
00:19:21

[yeah that's a whole other question all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m25s)
00:19:25

[right so how do you how do you get the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m27s)
00:19:27

[validation set to be good so I build a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m30s)
00:19:30

[random forest on all the training data](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m32s)
00:19:32

[it looks good on the training data it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m35s)
00:19:35

[looks good on the oob right and this is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m38s)
00:19:38

[actually a really good reason to have OB](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m41s)
00:19:41

[if it looks good on the OB that it means](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m43s)
00:19:43

[you're not overfitting in a statistical](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m45s)
00:19:45

[sense right like it's it's working well](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m48s)
00:19:48

[on a random sample but then it looks bad](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m50s)
00:19:50

[on the validation set so what happened](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m54s)
00:19:54

[well what happened was that you you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m56s)
00:19:56

[somehow failed to predict the future](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h19m58s)
00:19:58

[you're only predicted the past and so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m02s)
00:20:02

[Suraj had an idea about how we could fix](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m04s)
00:20:04

[that would be okay well maybe we should](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m06s)
00:20:06

[just train so like maybe we shouldn't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m07s)
00:20:07

[use the whole training set we should try](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m10s)
00:20:10

[a recent period only and now it on the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m11s)
00:20:11

[downside we're now using less data so we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m14s)
00:20:14

[can create less rich models on the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m17s)
00:20:17

[upside it's it's more up-to-date data](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m19s)
00:20:19

[and this is something you have to play](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m22s)
00:20:22

[around with most machine learning](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m25s)
00:20:25

[functions have the ability to provide a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m28s)
00:20:28

[weight that is given to each road solve](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m30s)
00:20:30

[for example with a random forest rather](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m34s)
00:20:34

[than bootstrapping at random you could](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m36s)
00:20:36

[have a weight on every row and randomly](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m39s)
00:20:39

[pick that row with some probability](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m41s)
00:20:41

[right and we could like say here's our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m42s)
00:20:42

[like probability we could like pick a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m46s)
00:20:46

[curve that looks like that so that the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m50s)
00:20:50

[most recent rows have a higher](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m54s)
00:20:54

[probability of being selected that can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m56s)
00:20:56

[work really well yeah it's it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h20m59s)
00:20:59

[something that you have to try and and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m02s)
00:21:02

[if you don't have a validation set that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m04s)
00:21:04

[represents the future compared to what](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m06s)
00:21:06

[you're training on you have no way to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m08s)
00:21:08

[know which of your techniques are](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m10s)
00:21:10

[working how do you make the compromise](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m11s)
00:21:11

[between amount of data versus recency of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m13s)
00:21:13

[data](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m16s)
00:21:16

[so what I tend to do is is when I have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m19s)
00:21:19

[this kind of temporal issue which is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m22s)
00:21:22

[probably most of the time once I have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m25s)
00:21:25

[something that's working well on the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m28s)
00:21:28

[validation set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m30s)
00:21:30

[I wouldn't then go and just use that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m31s)
00:21:31

[model on the test set because the thing](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m32s)
00:21:32

[that I've trained on is now like but you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m35s)
00:21:35

[know the test set is much more in the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m38s)
00:21:38

[future](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m40s)
00:21:40

[compared to the training set so I would](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m40s)
00:21:40

[then replicate building that model again](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m42s)
00:21:42

[but this time I would combine the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m45s)
00:21:45

[training and validation sets together](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m47s)
00:21:47

[okay and retrain the model and at that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m50s)
00:21:50

[point you've got no way to test against](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m53s)
00:21:53

[a validation set so you have to make](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m57s)
00:21:57

[sure you have a reproducible script or](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h21m59s)
00:21:59

[notebook that does exactly the same](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m02s)
00:22:02

[steps in exactly the same ways because](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m04s)
00:22:04

[if you get something wrong then you're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m07s)
00:22:07

[going to find on the test set that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m09s)
00:22:09

[you've you've got a problem so so what](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m10s)
00:22:10

[what I do in practice is I need to know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m16s)
00:22:16

[is my validation set a truly](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m19s)
00:22:19

[representative of the test set so what I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m23s)
00:22:23

[do is I build five models on the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m26s)
00:22:26

[training set I build five models on the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m29s)
00:22:29

[training set and I try to have them kind](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m37s)
00:22:37

[of vary in how good I think they are](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m38s)
00:22:38

[right and then and then I score them my](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m41s)
00:22:41

[five models on the validation set all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m45s)
00:22:45

[right and then I also score them on the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m49s)
00:22:49

[test set that so I'm not cheating so I'm](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m52s)
00:22:52

[not using any feedback from the test set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m55s)
00:22:55

[to change my hyper parameters I'm only](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m57s)
00:22:57

[using it for this one thing which is to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h22m59s)
00:22:59

[check my validation set so I get my five](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m01s)
00:23:01

[scores from the test set and then I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m03s)
00:23:03

[check that they fall in a line okay and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m08s)
00:23:08

[if they don't then you're not going to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m13s)
00:23:13

[get good enough feedback from the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m16s)
00:23:16

[validation set so keep doing that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m17s)
00:23:17

[process until you're getting a line and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m19s)
00:23:19

[that can be quite tricky right sometimes](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m22s)
00:23:22

[the the test set you know trying to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m26s)
00:23:26

[create something that's as similar to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m30s)
00:23:30

[the real-world outcome as possible it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m31s)
00:23:31

[difficult right and when you're it kind](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m34s)
00:23:34

[of in the real world the same is true of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m37s)
00:23:37

[creating the test set like the test set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m39s)
00:23:39

[has to be a close to production as](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m40s)
00:23:40

[possible so like what's the actual mix](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m42s)
00:23:42

[of customers that are going to be using](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m46s)
00:23:46

[this how much time is there actually](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m47s)
00:23:47

[going to be between when you build the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m49s)
00:23:49

[model and when you put it in production](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m50s)
00:23:50

[how often you're going to be able to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m51s)
00:23:51

[refresh the model these are all the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m53s)
00:23:53

[things to think about when you build](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m55s)
00:23:55

[that test set okay so you want to say](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h23m56s)
00:23:56

[that first make five models on the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m02s)
00:24:02

[training data yeah and then dilute get a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m05s)
00:24:05

[straight-line relationship change your](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m07s)
00:24:07

[validation and death set you can't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m10s)
00:24:10

[really change the test set generally so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m12s)
00:24:12

[this is assuming that the test sets](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m13s)
00:24:13

[given it changed to change the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m14s)
00:24:14

[validation set so if you start with a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m16s)
00:24:16

[random sample validation set and then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m19s)
00:24:19

[it's all over the place and you realize](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m21s)
00:24:21

[oh I should have picked the last two](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m23s)
00:24:23

[months and then you pick the last two](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m24s)
00:24:24

[months it's still going all over the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m26s)
00:24:26

[place in your eyes oh I should have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m27s)
00:24:27

[picked it so that's also from the first](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m29s)
00:24:29

[of the month to the fifteenth of the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m30s)
00:24:30

[month and they'll keep going until](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m32s)
00:24:32

[changing your validation set until you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m34s)
00:24:34

[found a validation set which is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m37s)
00:24:37

[indicative of your test set results](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m38s)
00:24:38

[no sort of five models like he was](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m44s)
00:24:44

[started maybe like just random data and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m47s)
00:24:47

[average and they just make it their own](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m49s)
00:24:49

[yeah yeah yeah yeah maybe a exactly](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m51s)
00:24:51

[maybe yeah I kind of five like not](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m54s)
00:24:54

[terrible ones but you want some variety](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m57s)
00:24:57

[and you also particularly want some](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h24m59s)
00:24:59

[variety and like how well they might](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m00s)
00:25:00

[generalize through time so one that was](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m03s)
00:25:03

[trained on the whole training set one](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m05s)
00:25:05

[that was trained on the last two weeks](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m07s)
00:25:07

[one that was trained on the last six](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m08s)
00:25:08

[weeks one which used as you know lots](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m11s)
00:25:11

[and lots of columns and might have a fit](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m14s)
00:25:14

[a bit more yeah so you kind of want to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m16s)
00:25:16

[get a sense of like oh if my validation](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m18s)
00:25:18

[set fails to generalize temporarily I'd](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m20s)
00:25:20

[want to see that if it fell to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m23s)
00:25:23

[generalize statistically I'd want to see](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m25s)
00:25:25

[that sorry can you explain a bit more](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m26s)
00:25:26

[detail what you mean by change your](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m29s)
00:25:29

[validation set so it indicates the test](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m31s)
00:25:31

[set like what does that look like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m32s)
00:25:32

[so posit so let's take the groceries](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m35s)
00:25:35

[competition where we're trying to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m37s)
00:25:37

[predict the next two weeks of grocery](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m39s)
00:25:39

[sales so possible validation sets that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m42s)
00:25:42

[Terrence and I played with was a random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m44s)
00:25:44

[sample the last month of data the last](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m48s)
00:25:48

[two weeks of data and the other one we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h25m55s)
00:25:55

[tried was same day range one month](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m00s)
00:26:00

[earlier so that the test set in this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m09s)
00:26:09

[competition was the first to the 15th of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m12s)
00:26:12

[August sorry if this 15 that maybe the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m15s)
00:26:15

[15 to the 30th of August so we tried](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m19s)
00:26:19

[like a random sample as four years we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m23s)
00:26:23

[tried the 15th of July to the 15th of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m24s)
00:26:24

[August we tried the 1st of August to the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m29s)
00:26:29

[15th of August and we tried the 15th of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m31s)
00:26:31

[July to the 30th of July and so there](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m35s)
00:26:35

[were four different validation sets we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m37s)
00:26:37

[tried and so with random you know our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m40s)
00:26:40

[kind of results were all over the place](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m42s)
00:26:42

[with last month you know they were like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m44s)
00:26:44

[not bad but not great the last two weeks](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m47s)
00:26:47

[there was a couple that didn't look good](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m50s)
00:26:50

[but on the whole they were good and same](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m51s)
00:26:51

[day range of months early](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m53s)
00:26:53

[they've got a basically perfect line](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m55s)
00:26:55

[that's the part I'm talking right there](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m56s)
00:26:56

[what exactly are you comparing it to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h26m58s)
00:26:58

[from the test site I just confused what](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m00s)
00:27:00

[you're creating that graph so for each](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m02s)
00:27:02

[of those so for each of my so I build](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m05s)
00:27:05

[five models right so there might be like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m08s)
00:27:08

[just predict the average do some kind of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m11s)
00:27:11

[simple group mean of the whole data set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m14s)
00:27:14

[do some group mean over the last month](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m16s)
00:27:16

[of the data set build a read on forests](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m17s)
00:27:17

[of the whole thing build a random forest](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m19s)
00:27:19

[from the last three weeks on each of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m21s)
00:27:21

[those I calculate the validation score](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m23s)
00:27:23

[and then I retrain the model on the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m26s)
00:27:26

[whole training set and calculate the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m28s)
00:27:28

[same thing on the test set and so each](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m30s)
00:27:30

[of these points now she tells me how](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m33s)
00:27:33

[about it ago in the validation set how](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m36s)
00:27:36

[well did it go in the test set and so if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m38s)
00:27:38

[the validation set is useful we would](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m40s)
00:27:40

[say every time the validation set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m43s)
00:27:43

[improves the test set should also score](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m44s)
00:27:44

[should also improve yes so you just said](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m47s)
00:27:47

[rate ring dreaming rich rings in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m51s)
00:27:51

[modeling on training and validations](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m53s)
00:27:53

[yeah that was a step I was talking about](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m55s)
00:27:55

[here so once I've got the validation](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m57s)
00:27:57

[score based on just the training set and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h27m58s)
00:27:58

[then retrain it on the train and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m00s)
00:28:00

[validation and check against history](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m02s)
00:28:02

[somebody else so just to clarify my test](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m06s)
00:28:06

[set you mean submitting it to kaibaland](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m14s)
00:28:14

[and checking the school if it's cattle](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m18s)
00:28:18

[then your test set is Carol's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m21s)
00:28:21

[leaderboard in the real world the test](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m23s)
00:28:23

[set is this third data set that you put](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m26s)
00:28:26

[aside and it's that third data set that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m28s)
00:28:28

[having it reflect real world production](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m32s)
00:28:32

[differences is the most important step](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m35s)
00:28:35

[in a machine learning project](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m38s)
00:28:38

[why is it the most important step](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m41s)
00:28:41

[because if you screw up everything else](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m43s)
00:28:43

[that you don't screw up that you're no](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m46s)
00:28:46

[you screwed up right like if you've got](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m49s)
00:28:49

[a good test set then you'll know you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m51s)
00:28:51

[screw it up because you screwed up](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m54s)
00:28:54

[something else and you tested it and it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m56s)
00:28:56

[didn't work out and it's like okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m57s)
00:28:57

[you're not going to destroy the company](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h28m58s)
00:28:58

[right if you screwed up creating the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m00s)
00:29:00

[test set that would be awful right](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m02s)
00:29:02

[because then you don't know if you've](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m05s)
00:29:05

[made a mistake right you try to build a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m07s)
00:29:07

[model you test it on the test set it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m10s)
00:29:10

[looks good but the test set was not](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m12s)
00:29:12

[indicative of real-world environment so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m13s)
00:29:13

[you don't actually know if you better](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m19s)
00:29:19

[destroy the company right now hopefully](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m20s)
00:29:20

[you've got ways to put things into](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m22s)
00:29:22

[production gradually so you won't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m23s)
00:29:23

[actually destroy the company but you'll](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m25s)
00:29:25

[at least destroy your reputation at work](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m27s)
00:29:27

[right it's like Oh Jeremy tried to put](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m29s)
00:29:29

[this thing into production and in the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m31s)
00:29:31

[first week the cohort we tried it on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m34s)
00:29:34

[their sales halved and we're never](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m36s)
00:29:36

[better give Jeremy machine-learning job](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m38s)
00:29:38

[again right but if Jeremy had used a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m39s)
00:29:39

[proper test set then like he would have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m42s)
00:29:42

[known oh this is like half as good as my](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m44s)
00:29:44

[validation set said it would be I'll](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m47s)
00:29:47

[keep trying right and now I'm not going](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m49s)
00:29:49

[to get in any trouble I was actually](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m51s)
00:29:51

[like Oh Jeremy is awesome he identifies](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m53s)
00:29:53

[ahead of time when there's going to be a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m55s)
00:29:55

[generalization problem okay so this is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h29m58s)
00:29:58

[like this is something that kind of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m08s)
00:30:08

[everybody talks about a little bit in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m12s)
00:30:12

[machine learning classes but often it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m14s)
00:30:14

[kind of stops at the point where you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m17s)
00:30:17

[learned that there's a thing in SK learn](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m19s)
00:30:19

[called make test trains flipped and it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m20s)
00:30:20

[returns these things and off you go](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m23s)
00:30:23

[right but the fact that like or here's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m25s)
00:30:25

[the cross-validation function right so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m29s)
00:30:29

[the fact that these things always give](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m32s)
00:30:32

[you random samples tells you that like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m35s)
00:30:35

[much if not most of the time you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m39s)
00:30:39

[shouldn't be using them the fact that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m41s)
00:30:41

[random forest gives you an oo B for free](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m45s)
00:30:45

[it's useful but it only tells you that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m47s)
00:30:47

[this generalizes in a statistical sense](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m50s)
00:30:50

[not in a practice](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m52s)
00:30:52

[since right so then finally there's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m54s)
00:30:54

[cross-validation right which](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h30m57s)
00:30:57

[outside of class you guys have been](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m01s)
00:31:01

[talking about a lot which makes me feel](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m02s)
00:31:02

[somebody's been over emphasizing the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m05s)
00:31:05

[value of this technique so I'll explain](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m07s)
00:31:07

[what cross-validation is and then I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m10s)
00:31:10

[explain why you probably shouldn't be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m12s)
00:31:12

[using it most of the time so cross](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m14s)
00:31:14

[validation says let's not just pull out](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m17s)
00:31:17

[one validation set but let's pull out](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m19s)
00:31:19

[five say so let's assume that we're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m21s)
00:31:21

[going to randomly shuffle the data first](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m25s)
00:31:25

[all right this is critical right we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m27s)
00:31:27

[first randomly shuffle the data and then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m30s)
00:31:30

[we're going to split it into five groups](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m32s)
00:31:32

[and then for model number one we'll call](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m37s)
00:31:37

[this the validation set and we'll call](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m42s)
00:31:42

[this the training set okay and we'll](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m46s)
00:31:46

[train and we'll check against the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m51s)
00:31:51

[validation and we'll get some rmse R](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m53s)
00:31:53

[squared whatever and then we'll throw](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m56s)
00:31:56

[that away](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m59s)
00:31:59

[and we'll call this the validation set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h31m59s)
00:31:59

[and we'll call this the training set and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m05s)
00:32:05

[we'll get another score we'll do that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m12s)
00:32:12

[five times and then we'll take the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m16s)
00:32:16

[average okay so that's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m21s)
00:32:21

[cross-validation average accuracy so who](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m27s)
00:32:27

[can tell me like a benefit of using](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m32s)
00:32:32

[cross-validation over a the kind of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m34s)
00:32:34

[standard validation set I talked about](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m38s)
00:32:38

[before how could you pass the phone if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m39s)
00:32:39

[you have a smokiness an chosen course](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m48s)
00:32:48

[validation will make you solve with a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m51s)
00:32:51

[data you have yeah you can use all of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m53s)
00:32:53

[the data you don't have to put anything](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m55s)
00:32:55

[aside and you kind of get a little](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m57s)
00:32:57

[benefit as well in that like you've now](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h32m59s)
00:32:59

[got five models that you could ensemble](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m01s)
00:33:01

[together each one of used which used 80%](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m03s)
00:33:03

[of the data so you know sometimes that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m06s)
00:33:06

[ensemble lane can be helpful](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m07s)
00:33:07

[I'm fun could you tell me like what what](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m11s)
00:33:11

[could be some reasons that you wouldn't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m13s)
00:33:13

[use cross-validation we have enough data](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m15s)
00:33:15

[so we don't not want the validations and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m19s)
00:33:19

[to be included in the model trainings](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m22s)
00:33:22

[process - - like - okay yeah I'm not](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m25s)
00:33:25

[sure the cross-validation is necessarily](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m35s)
00:33:35

[polluting the model what would be a key](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m36s)
00:33:36

[like downside of cross-validation but](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m39s)
00:33:39

[like for deepening if you have learned](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m42s)
00:33:42

[them P be chosen as annual Network will](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m44s)
00:33:44

[know the pictures it's more likely to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m48s)
00:33:48

[predicative as is right so sure but if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m51s)
00:33:51

[we if we put aside some data each time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m54s)
00:33:54

[in the cross-validation can you pass it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m57s)
00:33:57

[to Suraj I'm not so worried about like I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h33m58s)
00:33:58

[don't think there's like one of these](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m03s)
00:34:03

[validation sets is more statistically](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m05s)
00:34:05

[accurate yes Suraj Steven will you be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m09s)
00:34:09

[all fitting together late I think that's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m14s)
00:34:14

[what fun was worried about I don't see](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m17s)
00:34:17

[why that would happen like each time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m19s)
00:34:19

[we're fitting a model just 100 each time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m20s)
00:34:20

[we're fitting a model we are absolutely](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m24s)
00:34:24

[holding in 20 percent of the sample](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m26s)
00:34:26

[right so yes the five models between](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m28s)
00:34:28

[them have seen all of the data but but](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m31s)
00:34:31

[it's kind of like a random forest](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m33s)
00:34:33

[independence is a lot like a random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m34s)
00:34:34

[first each model has only been trained](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m36s)
00:34:36

[on a subset of the data yes you should](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m38s)
00:34:38

[see please David largely received like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m41s)
00:34:41

[it is deep load of time oh yes exactly](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m43s)
00:34:43

[right so we have to fit five models](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m45s)
00:34:45

[rather than one so here's a key downside](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m48s)
00:34:48

[number one it's time and so if we're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m50s)
00:34:50

[doing deep learning and it takes a day](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m55s)
00:34:55

[to run suddenly it takes five days or we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h34m57s)
00:34:57

[need five GPUs okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m00s)
00:35:00

[what about my earlier issues about](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m03s)
00:35:03

[validation sets Jona pass it over there](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m05s)
00:35:05

[what's remaining was a so if you had](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m07s)
00:35:07

[like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m12s)
00:35:12

[temporal data wouldn't you be like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m13s)
00:35:13

[shuffling when you e breaking that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m16s)
00:35:16

[relation](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m18s)
00:35:18

[well we could unravel it afterwards we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m20s)
00:35:20

[could reorder it like we could shuffle](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m23s)
00:35:23

[get the training set out and then sort](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m24s)
00:35:24

[it by time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m26s)
00:35:26

[like and like this presumably there's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m28s)
00:35:28

[date column there so I don't think I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m30s)
00:35:30

[don't think it's going to stop us from](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m34s)
00:35:34

[building a model did you have with](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m34s)
00:35:34

[cross-validation your building five even](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m44s)
00:35:44

[validation sets and if there is some](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m46s)
00:35:46

[sort of structure that you're trying to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m48s)
00:35:48

[capture in your validation sets of Mary](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m49s)
00:35:49

[your test set you're essentially just](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m51s)
00:35:51

[throwing that a chance to construct that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m53s)
00:35:53

[yourself right I think you're gonna say](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m55s)
00:35:55

[that I think you said the same thing as](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h35m59s)
00:35:59

[I'm gonna say which is which is that our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m00s)
00:36:00

[earlier concerns about why random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m02s)
00:36:02

[validation sets are a problem are](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m05s)
00:36:05

[entirely relevant here well these](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m06s)
00:36:06

[validation sets a random so if a random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m08s)
00:36:08

[validation set is not appropriate for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m12s)
00:36:12

[your problem most likely because for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m14s)
00:36:14

[example of temporal issues then none of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m18s)
00:36:18

[these four validation set of five](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m21s)
00:36:21

[validation sets are any good they're all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m22s)
00:36:22

[random right and so if you have temporal](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m24s)
00:36:24

[data like we did here there's no way to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m29s)
00:36:29

[do cross validation really or like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m32s)
00:36:32

[probably no good way to do cross](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m34s)
00:36:34

[validation I mean you're wanna have your](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m36s)
00:36:36

[validation set be as close to the test](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m40s)
00:36:40

[set as possible and so you can't do that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m41s)
00:36:41

[by randomly sampling different things so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m44s)
00:36:44

[so as fone said you may well not need to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m48s)
00:36:48

[do cross validation because most of the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m53s)
00:36:53

[time in the real world we don't really](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m55s)
00:36:55

[have that little data right unless your](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m57s)
00:36:57

[data is based on some very very](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h36m59s)
00:36:59

[expensive labeling process or some](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m01s)
00:37:01

[experiments that take a look cost a lot](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m03s)
00:37:03

[to run or whatever but nowadays that's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m05s)
00:37:05

[data scientists are not very often doing](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m07s)
00:37:07

[that kind of work some um in which case](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m10s)
00:37:10

[this is an issue](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m12s)
00:37:12

[it must have assigned so we probably](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m13s)
00:37:13

[don't need to as nishan said if we do do](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m15s)
00:37:15

[it it's going to take a whole lot of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m19s)
00:37:19

[time all right and then as earnest said](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m20s)
00:37:20

[even if we did do it and we took up all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m22s)
00:37:22

[that time it's like it was totally the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m25s)
00:37:25

[wrong answer because random validation](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m27s)
00:37:27

[sets are inappropriate for a problem](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m29s)
00:37:29

[okay so I'm not going to be spending](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m30s)
00:37:30

[much time on cross validation because I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m33s)
00:37:33

[just I think it's an interesting tool to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m35s)
00:37:35

[have it's easy to use Sosuke learn has a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m37s)
00:37:37

[cross validation thing you can go](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m39s)
00:37:39

[ahead and use but it's it's it's not](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m41s)
00:37:41

[that often that it's going to be an](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m46s)
00:37:46

[important part of your toolbox in my](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m48s)
00:37:48

[opinion you'll come up some points okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m50s)
00:37:50

[so that is validation tips so then the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h37m58s)
00:37:58

[other thing we started talking about](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m03s)
00:38:03

[last week and got a little bit stuck on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m05s)
00:38:05

[because I screwed it up was tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m11s)
00:38:11

[interpretation so I'm actually going to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m15s)
00:38:15

[cover that again without the error and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m17s)
00:38:17

[dig into it in a bit more detail so can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m22s)
00:38:22

[anybody tell me what tree interpreter](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m26s)
00:38:26

[does and how it does it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m30s)
00:38:30

[what do you remember it's a difficult](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m36s)
00:38:36

[one to explain I don't think I did a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m38s)
00:38:38

[good job of explaining it so don't worry](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m40s)
00:38:40

[if you don't do a great job but does](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m42s)
00:38:42

[anybody wanna have a go explaining it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m43s)
00:38:43

[well okay that's fine so let's start](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m46s)
00:38:46

[with the output of tree interpreter so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m52s)
00:38:52

[if we look at a single model a single](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m55s)
00:38:55

[tree in other words here is a single](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h38m59s)
00:38:59

[tree okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m03s)
00:39:03

[so to remind us the top of a tree is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m07s)
00:39:07

[before there's been any split at all so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m11s)
00:39:11

[ten point one eight nine is the average](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m15s)
00:39:15

[log price of all of the options in our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m19s)
00:39:19

[training set so I'm going to go ahead](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m23s)
00:39:23

[and draw right here](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m26s)
00:39:26

[ten point one a nine eight nine is the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m30s)
00:39:30

[average of all okay and then if I go a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m32s)
00:39:32

[couple of system less than or equal to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m37s)
00:39:37

[0.5 then I get ten point three four five](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m38s)
00:39:38

[okay so for this subset of 16,800](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m42s)
00:39:42

[coupler is less than or equal to point](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m48s)
00:39:48

[five the average is ten point three four](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m50s)
00:39:50

[five and then off the people with a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m51s)
00:39:51

[couple of system less than or equal to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m56s)
00:39:56

[point 5 we then take the subset we're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m57s)
00:39:57

[enclosure at less than or equal to two](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h39m59s)
00:39:59

[and the average there of rob sale price](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m01s)
00:40:01

[is nine point nine five five against](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m04s)
00:40:04

[nine point nine five and then final step](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m07s)
00:40:07

[in our tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m10s)
00:40:10

[as model ID just for this group with no](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m12s)
00:40:12

[capitalist system with enclosed lesson](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m16s)
00:40:16

[or - then let's just take model ID less](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m18s)
00:40:18

[than or equal to forty five seventy](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m21s)
00:40:21

[three and that gives us ten point two](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m23s)
00:40:23

[two six okay so then we can say all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m26s)
00:40:26

[right starting with ten point one oh](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m32s)
00:40:32

[nine one eight nine average for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m34s)
00:40:34

[everybody in our training set for this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m36s)
00:40:36

[particular tree subsample of twenty](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m38s)
00:40:38

[thousand adding in the capital decision](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m39s)
00:40:39

[or couple or less than a two point five](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m44s)
00:40:44

[increased our prediction by point one](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m47s)
00:40:47

[five six so if we predict it with a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m50s)
00:40:50

[naive model of just the mean that would](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m52s)
00:40:52

[have been ten point when I known adding](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m54s)
00:40:54

[in just the coupler decision would have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m56s)
00:40:56

[changed it to ten point three four five](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h40m59s)
00:40:59

[so this variable is responsible for a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m01s)
00:41:01

[point one five six increase in a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m03s)
00:41:03

[prediction from that the enclosure no](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m05s)
00:41:05

[decision was responsible for a - point](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m08s)
00:41:08

[three nine five decrease the model ID](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m11s)
00:41:11

[was responsible for eight point two](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m14s)
00:41:14

[seven six increase until eventually that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m16s)
00:41:16

[was our final decision that is our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m18s)
00:41:18

[prediction for this option of this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m21s)
00:41:21

[particular sale price so we can draw](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m24s)
00:41:24

[that as what's called a waterfall block](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m27s)
00:41:27

[right and what our four plots are one of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m29s)
00:41:29

[the most useful plots I know about and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m32s)
00:41:32

[weirdly enough there's nothing in Python](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m34s)
00:41:34

[to do them and this is one of these](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m37s)
00:41:37

[things where there's this disconnect](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m39s)
00:41:39

[between like the world of management](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m40s)
00:41:40

[consulting and business where everybody](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m42s)
00:41:42

[uses water for plots all the time and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m44s)
00:41:44

[like academia who have no idea what](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m46s)
00:41:46

[these things are but like every time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m49s)
00:41:49

[like you're looking at say here is last](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m51s)
00:41:51

[year's sales for Apple and then there](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m56s)
00:41:56

[was a change in that iPhones increased](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h41m59s)
00:41:59

[by this amount](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m01s)
00:42:01

[max decreased by that amount and iPads](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m02s)
00:42:02

[increased by that amount](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m05s)
00:42:05

[every time you have a starting point in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m06s)
00:42:06

[a number of changes and a finishing](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m08s)
00:42:08

[point waterfall charts are pretty much](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m10s)
00:42:10

[always the best way to show it so here](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m12s)
00:42:12

[our prediction for price based on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m14s)
00:42:14

[everything ten point one eight nine](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m16s)
00:42:16

[there was an increased blue means](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m17s)
00:42:17

[increase of 0.156 the coupler decrease](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m19s)
00:42:19

[of 0.395 or enclosure increase](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m23s)
00:42:23

[model ID of point two seven six so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m26s)
00:42:26

[decrease but I increase decrease](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m29s)
00:42:29

[increase to get to our final ten point](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m32s)
00:42:32

[two six six so you see how what a porch](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m35s)
00:42:35

[light works so with Excel 2016 its](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m37s)
00:42:37

[built-in you just click insert waterfall](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m41s)
00:42:41

[chart and there it is if you want to be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m43s)
00:42:43

[a hero](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m45s)
00:42:45

[create a waterfall chart package format](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m46s)
00:42:46

[plot lab put it on pip and everybody](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m50s)
00:42:50

[will love you for it there are some like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m52s)
00:42:52

[really crappy gist's and manual](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m55s)
00:42:55

[notebooks and stuff around these are](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h42m58s)
00:42:58

[actually super easy to build like you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m01s)
00:43:01

[basically do a stacked column plot where](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m04s)
00:43:04

[the the bottom of this is like all white](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m06s)
00:43:06

[right like you can kind of do it but if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m08s)
00:43:08

[you can wrap that up or all and put the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m11s)
00:43:11

[data the points in the right spots and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m13s)
00:43:13

[color them nicely that would be totally](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m15s)
00:43:15

[awesome I think you've all got the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m17s)
00:43:17

[skills to do it and would make you know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m19s)
00:43:19

[be a terrific thing for your portfolio](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m21s)
00:43:21

[so there's an idea could make an](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m24s)
00:43:24

[interesting cattle Colonel even like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m28s)
00:43:28

[here's how to build a waterfall plot can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m30s)
00:43:30

[scratch and by the way I've been putting](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m32s)
00:43:32

[this up on yep you can all use it so in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m33s)
00:43:33

[general therefore obviously going from](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m38s)
00:43:38

[the all and then going through each](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m40s)
00:43:40

[change then the some both all of those](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m42s)
00:43:42

[is going to be equal to the final](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m45s)
00:43:45

[prediction so that's how we could say if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m48s)
00:43:48

[we were just doing a decision tree then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m52s)
00:43:52

[you know you're coming along and saying](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m54s)
00:43:54

[like how come this particular option was](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m55s)
00:43:55

[this particular price and it's like well](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h43m58s)
00:43:58

[your prediction for it and like oh it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m00s)
00:44:00

[because of these three things had these](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m02s)
00:44:02

[three impacts right so for a random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m05s)
00:44:05

[forest we could do that across all of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m08s)
00:44:08

[the trees right so every time we see](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m11s)
00:44:11

[coupler we add up that change every time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m13s)
00:44:13

[we see enclosure we add up that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m16s)
00:44:16

[change every time we see model we add up](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m17s)
00:44:17

[that change okay and so then we combine](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m20s)
00:44:20

[them all together we get what tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m22s)
00:44:22

[interpreter does right so you could go](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m26s)
00:44:26

[into the source code for tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m28s)
00:44:28

[interpreter right and it's not at all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m30s)
00:44:30

[complex logic or you could build it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m32s)
00:44:32

[yourself and you can see how it does](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m33s)
00:44:33

[exactly this so when you go tree and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m37s)
00:44:37

[predict with a random forest model for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m39s)
00:44:39

[some specific option so I've got a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m42s)
00:44:42

[specific row here this my zero index row](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m45s)
00:44:45

[it tells you okay this is the prediction](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m49s)
00:44:49

[the same as the random forest prediction](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m52s)
00:44:52

[bias this is going to be always the same](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m55s)
00:44:55

[it's the average sale price for for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h44m57s)
00:44:57

[everybody for each of the random samples](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m01s)
00:45:01

[in the tree and then contributions is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m04s)
00:45:04

[the average of all so the total of all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m09s)
00:45:09

[our contributions for each time we see](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m12s)
00:45:12

[that specific column appear in a tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m14s)
00:45:14

[right so last time I made the mistake of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m18s)
00:45:18

[not sorting this correctly so this time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m21s)
00:45:21

[MP dot arc sort is a super handy](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m23s)
00:45:23

[function at sorts it doesn't actually](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m26s)
00:45:26

[sort contribution zero it just tells you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m29s)
00:45:29

[where each item would move to if it were](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m32s)
00:45:32

[sorted so now by passing ID access to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m36s)
00:45:36

[each one of the column the level](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m39s)
00:45:39

[contribution I can then print out all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m47s)
00:45:47

[those in the right order so I can see](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m50s)
00:45:50

[here here's my column here's the level](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m52s)
00:45:52

[and the contribution so the fact that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h45m56s)
00:45:56

[it's a small version of this piece of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m00s)
00:46:00

[industrial equipment meant that it was](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m02s)
00:46:02

[less expensive right but the fact that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m04s)
00:46:04

[was made pretty recently meant that was](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m07s)
00:46:07

[more expensive the fact that it's pretty](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m09s)
00:46:09

[old however made that it was less](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m11s)
00:46:11

[expensive right so this is not going to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m13s)
00:46:13

[really help you much at all with like a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m16s)
00:46:16

[cattle styled situation where you just](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m19s)
00:46:19

[need predictions it's going to help you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m21s)
00:46:21

[a lot in a production environment or](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m23s)
00:46:23

[even pre production right so like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m26s)
00:46:26

[something which any good manager should](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m27s)
00:46:27

[you should do if you say here's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m30s)
00:46:30

[machine learning model I think we should](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m32s)
00:46:32

[use as they should go away and grab a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m33s)
00:46:33

[few examples of actual customers or](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m36s)
00:46:36

[actual options or whatever and check](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m39s)
00:46:39

[whether your model looks intuitive](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m42s)
00:46:42

[alright and if it says like my](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m44s)
00:46:44

[prediction is that you know lots of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m46s)
00:46:46

[if people are going to really enjoy this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m52s)
00:46:52

[crappy movie you know it is like wow](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m55s)
00:46:55

[that was a really crappy movie then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m58s)
00:46:58

[they're going to come back to you and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h46m59s)
00:46:59

[say like explain why your models telling](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m00s)
00:47:00

[me that I'm going to like this movie](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m03s)
00:47:03

[because I hate that movie and then you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m07s)
00:47:07

[can go back and you say well it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m09s)
00:47:09

[because you like this movie and because](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m10s)
00:47:10

[you're this age range and you're this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m12s)
00:47:12

[gender on average actually people like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m14s)
00:47:14

[you did like that movie okay yeah](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m16s)
00:47:16

[what's the second element of each temple](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m24s)
00:47:24

[this is saying for this particular row](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m28s)
00:47:28

[it was a mini and it was 11 years old](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m31s)
00:47:31

[and it was a hydraulic excavator track 3](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m35s)
00:47:35

[to 4 metric tons so it's just feeding](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m38s)
00:47:38

[back and telling you it's because this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m42s)
00:47:42

[is actually what it was it was these](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m45s)
00:47:45

[numbers so I just went back to the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m47s)
00:47:47

[original data to actually pull out the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m51s)
00:47:51

[descriptive versions of each one okay so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h47m55s)
00:47:55

[if we sum up all the contributions](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m03s)
00:48:03

[together and then add them to the bias](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m05s)
00:48:05

[then that would be the same as adding up](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m11s)
00:48:11

[those three things adding it to this and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m14s)
00:48:14

[as we know from our waterfall chart that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m18s)
00:48:18

[gives us our final prediction this is a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m20s)
00:48:20

[almost totally unknown technique and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m27s)
00:48:27

[this particular library is almost](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m29s)
00:48:29

[totally unknown as well so like it's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m34s)
00:48:34

[great opportunity to you know show](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m37s)
00:48:37

[something that a lot of people like it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m40s)
00:48:40

[totally critical in my opinion but but](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m42s)
00:48:42

[rarely none so that's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m45s)
00:48:45

[that's kind of the end of the random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m51s)
00:48:51

[forest interpretation piece and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m52s)
00:48:52

[hopefully you've now seen enough that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m54s)
00:48:54

[when somebody says we can't use modern](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m56s)
00:48:56

[machine learning techniques because](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h48m59s)
00:48:59

[they're black boxes that are](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m00s)
00:49:00

[interpretive all you have enough](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m01s)
00:49:01

[information to say you're full of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m03s)
00:49:03

[right like they're extremely](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m05s)
00:49:05

[interpretable and the stuff that we've](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m08s)
00:49:08

[just done you know trying to do that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m09s)
00:49:09

[with a linear model good luck to you you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m11s)
00:49:11

[know even where you can do something](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m13s)
00:49:13

[similar with a linear model trying to do](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m15s)
00:49:15

[it so that's not giving you totally the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m17s)
00:49:17

[wrong answer and you had no idea it's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m18s)
00:49:18

[wrong answer it's going to be a real](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m20s)
00:49:20

[challenge so the last step we're going](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m22s)
00:49:22

[to do before we try and build up our own](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m26s)
00:49:26

[random forest is deal with this tricky](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m28s)
00:49:28

[issue of extrapolation so in this case](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m31s)
00:49:31

[if we look at our tree let's look at the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m34s)
00:49:34

[accuracy of our most recent trees](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m41s)
00:49:41

[we still have you know a big difference](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m49s)
00:49:49

[between our validation score and our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m53s)
00:49:53

[training score the actually in this case](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h49m57s)
00:49:57

[it's not too bad that the difference](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m04s)
00:50:04

[between the oob and the validation is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m07s)
00:50:07

[actually pretty close so if there was a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m10s)
00:50:10

[big difference between validation and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m13s)
00:50:13

[olb like I'd be very worried about that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m14s)
00:50:14

[we've dealt with the temporal side of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m17s)
00:50:17

[things correctly let's just have a look](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m19s)
00:50:19

[at I think the most recent model here it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m24s)
00:50:24

[was yeah so there's a tiny difference](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m27s)
00:50:27

[right and so on Tagle at least you kind](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m29s)
00:50:29

[of need that last decimal place in the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m34s)
00:50:34

[real world I probably stopped here but](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m36s)
00:50:36

[quite often you'll see there's a big](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m39s)
00:50:39

[difference between your validation score](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m40s)
00:50:40

[and your OB score now I will show you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m42s)
00:50:42

[how you would deal with that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m44s)
00:50:44

[particularly because actually we know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m47s)
00:50:47

[that the the oeob should be a little](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m49s)
00:50:49

[worse because it's using this less trees](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m51s)
00:50:51

[so it gives me a sense that we should](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m53s)
00:50:53

[get to do a little bit better and so the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m54s)
00:50:54

[reason we the way we should be able to a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m56s)
00:50:56

[little bit better is by handling the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h50m58s)
00:50:58

[time component a little bit better so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m00s)
00:51:00

[here's the problem with random forests](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m05s)
00:51:05

[when it comes to extrapolation when you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m08s)
00:51:08

[when you've got a data set that's like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m14s)
00:51:14

[you know four got four years of sales](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m17s)
00:51:17

[data in it and you create your tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m19s)
00:51:19

[right and it says like oh if these if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m22s)
00:51:22

[it's in some particular store and at](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m26s)
00:51:26

[some particular item and it is on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m28s)
00:51:28

[special you know here's the average](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m31s)
00:51:31

[price and it actually tells us the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m35s)
00:51:35

[average price you know over the whole](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m37s)
00:51:37

[training set which could be pretty old](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m40s)
00:51:40

[right and so when you then want to step](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m42s)
00:51:42

[forwards like what's going to be the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m47s)
00:51:47

[price next month it's never seen next](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m48s)
00:51:48

[month and and where else with a kind of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m51s)
00:51:51

[a linear model it can find a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m54s)
00:51:54

[relationship between time and price](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m56s)
00:51:56

[where even though we only had this much](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h51m58s)
00:51:58

[day](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m00s)
00:52:00

[when you then go and predict something](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m01s)
00:52:01

[in the future it can extrapolate that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m02s)
00:52:02

[but a random forest can't do that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m05s)
00:52:05

[there's no wave if you think about it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m07s)
00:52:07

[for a tree to be able to say well next](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m09s)
00:52:09

[month it would be higher still so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m11s)
00:52:11

[there's a few ways to deal with this and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m14s)
00:52:14

[we'll talk about it over the next couple](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m16s)
00:52:16

[of lessons but one simple way is just to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m18s)
00:52:18

[try to avoid using time variables as](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m20s)
00:52:20

[predictors if there's something else we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m27s)
00:52:27

[could use that's going to give us a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m29s)
00:52:29

[better](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m31s)
00:52:31

[you know something that kind of a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m31s)
00:52:31

[stronger relationship that's actually](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m33s)
00:52:33

[going to work in the future so in this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m35s)
00:52:35

[case what I wanted to do was to first of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m37s)
00:52:37

[all figure out](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m42s)
00:52:42

[what's the difference between our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m47s)
00:52:47

[validation set and our training set like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m49s)
00:52:49

[if I understand that difference between](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m52s)
00:52:52

[our validation set and our training set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m54s)
00:52:54

[then that tells me what are the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m55s)
00:52:55

[predictors which which have a strong](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h52m58s)
00:52:58

[temporal component and therefore they](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m01s)
00:53:01

[may be irrelevant by the time I get to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m03s)
00:53:03

[the future time period so I do something](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m07s)
00:53:07

[really interesting which is I create a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m09s)
00:53:09

[random forest where my dependent](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m11s)
00:53:11

[variable is is it in the validation set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m15s)
00:53:15

[right so I've gone back and I've got my](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m20s)
00:53:20

[whole data frame with the training and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m22s)
00:53:22

[validation altogether and I've created a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m24s)
00:53:24

[new column Court is valid which I've set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m27s)
00:53:27

[to one and then for all of the stuff in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m30s)
00:53:30

[the training set I set it to zero that's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m33s)
00:53:33

[about a new column which is just is this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m36s)
00:53:36

[in the validation set or not and then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m37s)
00:53:37

[I'm going to use that as my dependent](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m40s)
00:53:40

[variable and build a random first so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m42s)
00:53:42

[this is a random forest not to predict](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m46s)
00:53:46

[price that protect is this in the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m47s)
00:53:47

[validation set or not and so if your](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m50s)
00:53:50

[variables were not time dependent then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m53s)
00:53:53

[it shouldn't be possible to figure out](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m57s)
00:53:57

[if something's in the validation set or](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h53m58s)
00:53:58

[not this is a great trick in cattle](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m00s)
00:54:00

[records in cattle they often won't tell](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m02s)
00:54:02

[you whether the test set is a random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m06s)
00:54:06

[sample or not so you could put the test](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m08s)
00:54:08

[set and the training set together create](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m11s)
00:54:11

[a new column called is test and see if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m13s)
00:54:13

[you can predict it if you can you don't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m16s)
00:54:16

[have a random sample which means you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m18s)
00:54:18

[have to come and figure out how to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m20s)
00:54:20

[create a validation set from it right](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m22s)
00:54:22

[and so in this case I can see I don't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m25s)
00:54:25

[have a random sample because my](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m27s)
00:54:27

[validation set can be predicted with a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m29s)
00:54:29

[0.9999](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m31s)
00:54:31

[r-squared and so then if I look at](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m33s)
00:54:33

[future importance the top thing is sales](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m37s)
00:54:37

[ID and so this is really interesting it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m39s)
00:54:39

[tells us very clearly sales ID is not a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m42s)
00:54:42

[random identifier but probably it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m44s)
00:54:44

[something that's just set consecutively](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m47s)
00:54:47

[as time goes on we just increase the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m49s)
00:54:49

[sales ID so elapsed that was the number](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m52s)
00:54:52

[of days since the first date in our data](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m55s)
00:54:55

[set so not surprisingly that also is a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h54m58s)
00:54:58

[good predictor interestingly machine ID](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m01s)
00:55:01

[clearly each machine is being labeled](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m05s)
00:55:05

[with some consecutive identifier as well](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m07s)
00:55:07

[and then there's a big don't just look](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m09s)
00:55:09

[at the order look at the value so 0.7](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m12s)
00:55:12

[0.1 0.0 7.00 - okay stop right these top](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m14s)
00:55:14

[three are hundreds of times more](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m19s)
00:55:19

[important than the rest right so let's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m21s)
00:55:21

[next grab those top three right and we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m23s)
00:55:23

[can then have a look at their values](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m27s)
00:55:27

[both from the training set and in the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m31s)
00:55:31

[validation set and so we can see for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m35s)
00:55:35

[example sales ID on average is divided](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m37s)
00:55:37

[by thousand on averages 1.8 million in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m40s)
00:55:40

[the training set and 5.8 million in the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m43s)
00:55:43

[validation set right so you'd like you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m47s)
00:55:47

[can see just confirm like okay they're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m49s)
00:55:49

[very different so let's drop them okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m52s)
00:55:52

[so after I drop them let's now see if I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m56s)
00:55:56

[can predict whether something's in the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h55m59s)
00:55:59

[validation set I still can with 0.98](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m00s)
00:56:00

[pass quit](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m03s)
00:56:03

[so once you remove some things then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m06s)
00:56:06

[other things can like come to the front](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m08s)
00:56:08

[and it now turns out okay that's not](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m10s)
00:56:10

[surprisingly age you know things that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m12s)
00:56:12

[are old are you know more likely I guess](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m15s)
00:56:15

[to be in the validation set because](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m20s)
00:56:20

[there's you know earlier on in the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m22s)
00:56:22

[training set yet they can't be old yeah](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m24s)
00:56:24

[yeah made same reason so then we can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m26s)
00:56:26

[try removing those as well](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m35s)
00:56:35

[and so once we let's see where do we go](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m40s)
00:56:40

[up here yeah so what we can try doing is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m43s)
00:56:43

[we can then say alright let's take the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m46s)
00:56:46

[saleslady so let's machine ID from the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m47s)
00:56:47

[first one the age year made sale day of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m50s)
00:56:50

[year from the second one and say okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m54s)
00:56:54

[these are all time dependent features so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h56m56s)
00:56:56

[I still want them in my random forest if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m02s)
00:57:02

[they're important right but if they're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m04s)
00:57:04

[not important then taking them out if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m07s)
00:57:07

[there are some other long-term dependent](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m10s)
00:57:10

[variables that that work just as well](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m11s)
00:57:11

[that would be better right because now](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m14s)
00:57:14

[I'm going to have a model that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m16s)
00:57:16

[generalizes over time better so here I'm](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m17s)
00:57:17

[just going to go ahead and go through](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m19s)
00:57:19

[each one of those features and drop each](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m20s)
00:57:20

[one one at a time okay retrain a new](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m23s)
00:57:23

[random forest and print out the score](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m26s)
00:57:26

[okay so before we do any of that our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m29s)
00:57:29

[score was](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m32s)
00:57:32

[point eight eight for our validation](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m35s)
00:57:35

[versus point eight 900 B and you can see](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m40s)
00:57:40

[here when I remove sales ID my score](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m44s)
00:57:44

[goes up and this this is like what we're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m48s)
00:57:48

[hoping for we've removed a time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m51s)
00:57:51

[dependent variable there were other](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m53s)
00:57:53

[variables that could find similar](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m55s)
00:57:55

[relationships without the time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m56s)
00:57:56

[dependency so removing it cost our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h57m58s)
00:57:58

[validation to go up now oob didn't go up](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m00s)
00:58:00

[right because this is genuinely](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m04s)
00:58:04

[statistically you're useful predictor](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m06s)
00:58:06

[right but it's a time dependent one when](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m08s)
00:58:08

[we have a time dependent validation set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m10s)
00:58:10

[so this is like really subtle but it can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m12s)
00:58:12

[be really important right it's trying to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m15s)
00:58:15

[find the things that gives you a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m17s)
00:58:17

[generalizable time across time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m19s)
00:58:19

[prediction and here's how you can see it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m21s)
00:58:21

[so it's like okay we should remove sales](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m23s)
00:58:23

[ID for sure right but sale elapsed](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m25s)
00:58:25

[didn't get better okay so we don't want](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m29s)
00:58:29

[that machine ID did get better right](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m32s)
00:58:32

[from eight eight eight to eight nine](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m35s)
00:58:35

[three right so it's actually quite a bit](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m36s)
00:58:36

[better](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m38s)
00:58:38

[age got a bit better you made got worse](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m41s)
00:58:41

[sale day of year got a bit better okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m46s)
00:58:46

[so now we can say alright let's get rid](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m49s)
00:58:49

[of the three where we know that getting](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m53s)
00:58:53

[rid of it actually made it better okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h58m57s)
00:58:57

[and as a result look at this we're now](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m00s)
00:59:00

[up to nine one five okay so we've got](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m02s)
00:59:02

[rid of three time dependent things and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m05s)
00:59:05

[now as expected validation is better](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m07s)
00:59:07

[than our Obi](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m11s)
00:59:11

[okay so that was a super successful](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m14s)
00:59:14

[approach there right and so now we can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m16s)
00:59:16

[check the feature importance and let's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m18s)
00:59:18

[go ahead and say all right that was](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m22s)
00:59:22

[pretty damn good](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m24s)
00:59:24

[let's now leave it for a while so give](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m26s)
00:59:26

[it a hundred and sixty trees don't show](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m29s)
00:59:29

[it and see how that goes](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m31s)
00:59:31

[okay and so as you can see like we did](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m33s)
00:59:33

[all of our interpretation all of our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m36s)
00:59:36

[fine-tuning basically with smaller](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m38s)
00:59:38

[models subsets and at the end we run the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m41s)
00:59:41

[whole thing you actually still only took](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m43s)
00:59:43

[16 seconds and so we've now got an RMS](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m45s)
00:59:45

[see of 0.21 okay so now we can check](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m50s)
00:59:50

[that against cattle again we can't we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m53s)
00:59:53

[unfortunately this older competition](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=00h59m59s)
00:59:59

[we're not allowed to enter anymore to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m02s)
01:00:02

[see how he would have gone so the best](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m04s)
01:00:04

[we can do is check whether it looks like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m05s)
01:00:05

[we could have done we're all based on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m08s)
01:00:08

[their validation set so it should be in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m09s)
01:00:09

[the right area and yeah based on that we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m11s)
01:00:11

[would have come first](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m14s)
01:00:14

[okay so you know I think this is an](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m16s)
01:00:16

[interesting series of steps right so you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m20s)
01:00:20

[can go through the same series of steps](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m24s)
01:00:24

[in your cattle projects and more](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m26s)
01:00:26

[importantly your real-world projects so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m29s)
01:00:29

[one of the challenges is once you leave](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m31s)
01:00:31

[this learning environment](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m33s)
01:00:33

[suddenly you're surrounded by people who](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m35s)
01:00:35

[they they've had not have enough time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m37s)
01:00:37

[they always want you to be in a hurry](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m39s)
01:00:39

[they're always telling you you know do](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m40s)
01:00:40

[this and then do that you need to find](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m43s)
01:00:43

[the time to step away right and go back](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m44s)
01:00:44

[because this is a genuine real-world](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m47s)
01:00:47

[modeling process you can use and it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m49s)
01:00:49

[gives when I said kids world-class](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m52s)
01:00:52

[results I mean it right like this guy](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m54s)
01:00:54

[who won this lista costs sadly he's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h00m57s)
01:00:57

[passed away but he is the top kaggle](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m00s)
01:01:00

[competitor of all time like he he won I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m05s)
01:01:05

[believe like dozens of competitions so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m09s)
01:01:09

[we can get a score even within cuy of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m11s)
01:01:11

[him then we are doing really really well](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m14s)
01:01:14

[okay so let's take a five-minute break](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m18s)
01:01:18

[and we're going to come back and build](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m21s)
01:01:21

[our own random first I just wanted to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m23s)
01:01:23

[clarify something quickly a very good](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m33s)
01:01:33

[point during the break was going back to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m36s)
01:01:36

[the change in R squared between here and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m43s)
01:01:43

[here it's not just due to the fact that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m50s)
01:01:50

[we removed these three predictors we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m53s)
01:01:53

[also went reset our F samples right so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h01m58s)
01:01:58

[they actually see the impact of just](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m01s)
01:02:01

[removing we need to compare it to the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m02s)
01:02:02

[final step earlier so it's actually](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m07s)
01:02:07

[compared to 907 so removing those three](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m09s)
01:02:09

[things took us from 907](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m11s)
01:02:11

[nine one five okay so I mean and you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m20s)
01:02:20

[know in the end of course what matters](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m23s)
01:02:23

[is our final model that yep just to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m24s)
01:02:24

[clarify okay so um some of you have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m27s)
01:02:27

[asked me about writing your own random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m35s)
01:02:35

[forests from scratch I don't know if any](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m37s)
01:02:37

[of you have given it a try](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m38s)
01:02:38

[yet my original plan here was to do it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m40s)
01:02:40

[in real time and then as I started to do](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m44s)
01:02:44

[it I realized that that would have kind](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m46s)
01:02:46

[of been boring because to you because I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m48s)
01:02:48

[screw things up all the time so instead](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m50s)
01:02:50

[we might do more of like a walk through](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m52s)
01:02:52

[the code together](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m55s)
01:02:55

[just as an aside this reminds me talking](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h02m59s)
01:02:59

[about the exam hammock she somebody](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m03s)
01:03:03

[asked on the forum about like what what](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m04s)
01:03:04

[can you expect on the exam the basic](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m06s)
01:03:06

[plan is to make it a exam be very](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m08s)
01:03:08

[similar to these notebooks so it'll](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m13s)
01:03:13

[probably be a notebook that you have to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m14s)
01:03:14

[you know get a data set create a model](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m16s)
01:03:16

[trainer feature importance whatever](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m20s)
01:03:20

[right and the plan is that it'll be open](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m23s)
01:03:23

[block open Internet you can use whatever](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m26s)
01:03:26

[resources you like so basically if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m28s)
01:03:28

[you're entering competitions the exam](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m29s)
01:03:29

[should be very straightforward I also](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m32s)
01:03:32

[expect that there will be some pieces](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m35s)
01:03:35

[about like here's a partially completed](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m37s)
01:03:37

[random forest or something you know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m40s)
01:03:40

[finish finish writing this step here or](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m42s)
01:03:42

[here's a random forest implement feature](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m45s)
01:03:45

[importance or in you know implement one](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m47s)
01:03:47

[of the things we've talked about so it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m50s)
01:03:50

[open it you know the exam will be much](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m53s)
01:03:53

[like what we do in class and what you're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m55s)
01:03:55

[expected to be doing during the week](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m57s)
01:03:57

[there won't be any define this or tell](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h03m59s)
01:03:59

[me the difference between this word and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m03s)
01:04:03

[that word or whatever there's not going](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m05s)
01:04:05

[to be any rote learning it'll be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m06s)
01:04:06

[entirely like are you an effective](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m07s)
01:04:07

[machine learning practitioner ie can use](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m09s)
01:04:09

[the algorithms do you know can you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m11s)
01:04:11

[create an effective validation set and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m14s)
01:04:14

[can you can you create parts of the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m16s)
01:04:16

[algorithm implement them from scratch so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m19s)
01:04:19

[it'll be all about writing code](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m21s)
01:04:21

[basically so if you're not comfortable](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m23s)
01:04:23

[writing code to practice machine](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m27s)
01:04:27

[learning then you should be practicing](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m29s)
01:04:29

[that all the time if you are comfortable](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m33s)
01:04:33

[you should be practicing that all the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m34s)
01:04:34

[time also whatever you're doing write](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m35s)
01:04:35

[code to implement random to do machine](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m37s)
01:04:37

[learning okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m40s)
01:04:40

[so I I kind of have a particular way of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m48s)
01:04:48

[writing code and I'm not going to claim](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m51s)
01:04:51

[it's the only way of writing code but it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m54s)
01:04:54

[might be a little bit different to what](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m56s)
01:04:56

[you're used to and hopefully you'll find](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h04m58s)
01:04:58

[it at least interesting](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m00s)
01:05:00

[creating implementing random forest](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m01s)
01:05:01

[algorithms is actually quite tricky not](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m04s)
01:05:04

[because the codes tricky like generally](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m08s)
01:05:08

[speaking](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m10s)
01:05:10

[most random first algorithms are pretty](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m12s)
01:05:12

[conceptually easy at all that generally](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m14s)
01:05:14

[speaking academic papers and books have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m17s)
01:05:17

[a knack of making them look difficult](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m21s)
01:05:21

[but they're not difficult conceptually](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m23s)
01:05:23

[what's difficult is getting all the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m26s)
01:05:26

[details right and knowing and knowing](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m28s)
01:05:28

[when you're right and so in other words](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m31s)
01:05:31

[we need a good way of doing testing so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m33s)
01:05:33

[if we're going to reimplemented a we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m37s)
01:05:37

[want to create a random forest in some](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m41s)
01:05:41

[different framework different language](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m43s)
01:05:43

[different operating system you know I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m47s)
01:05:47

[would always start with something that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m48s)
01:05:48

[does exist right so in this case we're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m50s)
01:05:50

[just going to do is learning its](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m52s)
01:05:52

[exercise writing a random forest in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m53s)
01:05:53

[Python so for testing I'm going to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m54s)
01:05:54

[compare it to an existing random forest](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m56s)
01:05:56

[implementation okay so that's like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h05m59s)
01:05:59

[critical anytime you're doing anything](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m02s)
01:06:02

[involving like non-trivial amounts of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m05s)
01:06:05

[code and machine learning knowing](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m07s)
01:06:07

[whether you've got it right or wrong is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m10s)
01:06:10

[kind of the hardest fit I always assume](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m12s)
01:06:12

[that I've screwed everything up at every](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m14s)
01:06:14

[step and so I'm thinking like okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m16s)
01:06:16

[assuming that I screwed it up how do I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m18s)
01:06:18

[figure out that I screwed it up](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m20s)
01:06:20

[right and then much to my surprise from](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m22s)
01:06:22

[time to time I actually get something](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m24s)
01:06:24

[right and then I can move on okay but](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m25s)
01:06:25

[most of the time I get it wrong so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m28s)
01:06:28

[unfortunately with machine learning](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m31s)
01:06:31

[there's a lot of ways you can get things](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m33s)
01:06:33

[wrong that don't give you an error they](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m35s)
01:06:35

[just make your result like slightly less](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m37s)
01:06:37

[good and so that's that's what you want](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m40s)
01:06:40

[to pick up so given that I want to kind](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m43s)
01:06:43

[of compare it to an existing](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m46s)
01:06:46

[implementation I'm going to use our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m47s)
01:06:47

[existing data set our existing](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m49s)
01:06:49

[validation set and then to simplify](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m51s)
01:06:51

[things I'm just going to use two columns](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m53s)
01:06:53

[to start with so let's go ahead and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h06m55s)
01:06:55

[start writing a random forest so my way](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m00s)
01:07:00

[of writing nearly all code is top-down](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m03s)
01:07:03

[just let my teaching and so if I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m07s)
01:07:07

[top-down I start by assuming that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m09s)
01:07:09

[everything I want already exists](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m12s)
01:07:12

[so in other words the first thing I want](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m16s)
01:07:16

[to do I'm going to call this a tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m19s)
01:07:19

[ensemble right so to create a random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m20s)
01:07:20

[forest the first question I have is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m22s)
01:07:22

[what do I need to pass in right why I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m27s)
01:07:27

[need to initialize my random first so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m30s)
01:07:30

[I'm going to need some independent](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m33s)
01:07:33

[variables some dependent variable pick](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m35s)
01:07:35

[how many trees I want I'm going to use](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m39s)
01:07:39

[the sample size parameter from the start](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m41s)
01:07:41

[here so how big you want each sample to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m43s)
01:07:43

[be and then maybe some optional](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m45s)
01:07:45

[parameter of what's the smallest leaf](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m48s)
01:07:48

[size okay for testing it's nice to use a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m50s)
01:07:50

[constant random seed so we'll get the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m55s)
01:07:55

[same result each time so this is just](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m57s)
01:07:57

[how you set a random seed okay maybe](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h07m59s)
01:07:59

[it's worth mentioning is for those of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m03s)
01:08:03

[you unfamiliar with it random number](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m05s)
01:08:05

[generators on computers aren't random at](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m07s)
01:08:07

[all now actually constitute a random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m09s)
01:08:09

[number generators and what they do is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m12s)
01:08:12

[given some initial starting point in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m14s)
01:08:14

[this case 42 a pseudo-random number](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m16s)
01:08:16

[generator is a mathematical function](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m20s)
01:08:20

[that generates a deterministic always](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m22s)
01:08:22

[the same sequence of numbers such that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m25s)
01:08:25

[those numbers are designed to be as](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m28s)
01:08:28

[uncorrelated with the previous number as](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m30s)
01:08:30

[possible okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m32s)
01:08:32

[and as unpredictable as possible and as](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m34s)
01:08:34

[uncorrelated as possible with something](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m38s)
01:08:38

[with a different random seed so the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m41s)
01:08:41

[second number in in the sequence](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m43s)
01:08:43

[starting with 42 should be very](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m45s)
01:08:45

[different to the second number starting](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m47s)
01:08:47

[with 41 and generally they involve kind](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m48s)
01:08:48

[of like taking you know you know using](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m51s)
01:08:51

[big prime numbers and taking mods and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m55s)
01:08:55

[stuff like that it's kind of an](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h08m58s)
01:08:58

[interesting area of math if you want](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m00s)
01:09:00

[real random numbers the only way to do](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m04s)
01:09:04

[that is again you can actually buy](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m06s)
01:09:06

[hardware called a hardware random number](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m08s)
01:09:08

[generator that'll have inside them like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m10s)
01:09:10

[a little bit of some radioactive](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m12s)
01:09:12

[substance and and like something that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m14s)
01:09:14

[detects how many things it's spitting](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m16s)
01:09:16

[out or you know there will be some](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m18s)
01:09:18

[hardware thing](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m19s)
01:09:19

[any current system time is is it a valid](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m25s)
01:09:25

[random like random number generation no](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m30s)
01:09:30

[sense so that would be for maybe for a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m33s)
01:09:33

[random seed right so this thing of like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m35s)
01:09:35

[what do we start the function with so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m37s)
01:09:37

[one of the really interesting areas is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m39s)
01:09:39

[like in your computer if you don't set](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m41s)
01:09:41

[the random seed what is it set to and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m43s)
01:09:43

[yeah quite often people use the current](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m47s)
01:09:47

[time for security like obviously we use](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m51s)
01:09:51

[a lot of random number stuff for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m54s)
01:09:54

[security stuff like if you're generating](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m55s)
01:09:55

[an SSH key you need some it needs to be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h09m57s)
01:09:57

[random it turns out like you know people](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m00s)
01:10:00

[can figure out roughly when you created](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m03s)
01:10:03

[a key like they could look at like oid](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m06s)
01:10:06

[RSA has a timestamp and they could try](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m08s)
01:10:08

[you know all the different nanoseconds](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m11s)
01:10:11

[starting points for a random number](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m13s)
01:10:13

[generator around that time step and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m15s)
01:10:15

[figure out your key so in practice a lot](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m16s)
01:10:16

[of like really random high randomness](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m20s)
01:10:20

[requiring applications actually have a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m25s)
01:10:25

[step that say please move your mouse and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m26s)
01:10:26

[type random stuff at the keyboard for a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m29s)
01:10:29

[while and so it like gets you to be a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m30s)
01:10:30

[sort that's called entropy to be a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m33s)
01:10:33

[source of entropy other approaches is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m34s)
01:10:34

[they'll look at like you know the hash](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m37s)
01:10:37

[of some of your log files or you know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m39s)
01:10:39

[stuff like that it's a really really fun](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m43s)
01:10:43

[area so in our case our purpose actually](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m46s)
01:10:46

[is to remove randomness](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m50s)
01:10:50

[so we're saying okay generate a series](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m51s)
01:10:51

[of pseudo-random numbers starting with](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m53s)
01:10:53

[42 so it always should be the same so if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h10m55s)
01:10:55

[you haven't done much stuff in Python oo](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m00s)
01:11:00

[this is a basically standard idiom at](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m02s)
01:11:02

[least I mean I write it this way most](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m05s)
01:11:05

[people don't but if you pass in like 1 2](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m06s)
01:11:06

[3 4 5 things that you're going to want](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m10s)
01:11:10

[to keep inside this object then you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m12s)
01:11:12

[basically have to say self dot x equals](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m14s)
01:11:14

[x self dot y equals y self that sample](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m17s)
01:11:17

[equals sample right and so we can assign](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m19s)
01:11:19

[to a tuple from at a port so you know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m22s)
01:11:22

[okay this is like my way of coding most](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m27s)
01:11:27

[people think this is horrible but I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m28s)
01:11:28

[prefer to be able to see everything at](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m30s)
01:11:30

[once and so I know in my code anytime I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m32s)
01:11:32

[see something that looks like this it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m34s)
01:11:34

[always all of the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m35s)
01:11:35

[stuff in the method being set if I did](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m37s)
01:11:37

[it a different way than half the codes](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m39s)
01:11:39

[now come off the bottom of the page and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m41s)
01:11:41

[you can't see it all right so um so that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m43s)
01:11:43

[was the first thing I thought about is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m49s)
01:11:49

[like okay to create a random forest what](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m50s)
01:11:50

[information do you need then I'm going](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m51s)
01:11:51

[to need to store that information inside](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m53s)
01:11:53

[my object and so then I need to create](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m55s)
01:11:55

[some treats](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m59s)
01:11:59

[I had a random forest is something that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h11m59s)
01:11:59

[creates and is something that has some](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m01s)
01:12:01

[trees so I fit basically figured okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m03s)
01:12:03

[list comprehension to create a list of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m05s)
01:12:05

[trees how many trees do we have or you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m07s)
01:12:07

[put n trees trees that's what we asked](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m10s)
01:12:10

[for so range entries gives me the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m13s)
01:12:13

[numbers from 0 up to n trees minus 1 ok](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m16s)
01:12:16

[so if I create a list comprehension that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m20s)
01:12:20

[lips through that range calling create](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m22s)
01:12:22

[tree each time I now have entries trees](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m26s)
01:12:26

[and also I add to write that I didn't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m29s)
01:12:29

[have to think at all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m33s)
01:12:33

[like that's all like obvious and so I've](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m35s)
01:12:35

[kind of delayed the thinking to the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m38s)
01:12:38

[point where it's like well wait we don't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m41s)
01:12:41

[have something to create a tree okay no](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m43s)
01:12:43

[worries but let's pretend we did if we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m46s)
01:12:46

[did we've now created a random forest](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m48s)
01:12:48

[okay we'd still need to like do a few](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m51s)
01:12:51

[things on top of that for example once](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m53s)
01:12:53

[we have it we need a predict function so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m55s)
01:12:55

[okay well let's write a prediction](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m58s)
01:12:58

[function how do you predict in a random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h12m59s)
01:12:59

[forest can somebody tell me either based](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m02s)
01:13:02

[on their own understanding or based on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m07s)
01:13:07

[this line of code what would be like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m09s)
01:13:09

[your one or two-sentence answer how do](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m11s)
01:13:11

[you make a prediction in a random forest](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m13s)
01:13:13

[positive Spencer](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m16s)
01:13:16

[uh you would want to over every tree for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m20s)
01:13:20

[your like the row that you're trying to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m23s)
01:13:23

[predict on average the values that your](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m25s)
01:13:25

[that each tree would produce for that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m28s)
01:13:28

[book good and so you know that's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m30s)
01:13:30

[summary of what this says right so for a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m33s)
01:13:33

[particular row right or maybe this is a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m35s)
01:13:35

[number of rows go through each tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m37s)
01:13:37

[calculate its prediction so here is a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m43s)
01:13:43

[list comprehension that is calculating](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m45s)
01:13:45

[the prediction for every tree for X I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m47s)
01:13:47

[don't know if X is one row or multiple](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m51s)
01:13:51

[rows it doesn't matter right](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m52s)
01:13:52

[as long as as long as trade I predict](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m55s)
01:13:55

[works on it and then once you've got a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h13m58s)
01:13:58

[list of things a cool trick to know is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m01s)
01:14:01

[you can pass numpy dot mean a regular](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m03s)
01:14:03

[non mum pie list okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m07s)
01:14:07

[and it'll take the mean you just need to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m10s)
01:14:10

[tell it access equals zero means everage](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m12s)
01:14:12

[it across the lists okay so this is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m15s)
01:14:15

[going to return the average of that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m18s)
01:14:18

[predict for each tree and so I find list](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m22s)
01:14:22

[comprehensions allow me to write the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m26s)
01:14:26

[code in the way that the brain was like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m29s)
01:14:29

[you could take the word Spencer said and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m32s)
01:14:32

[like translate them into this code or](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m35s)
01:14:35

[you could take this code and translate](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m37s)
01:14:37

[them into words like the one Spencer](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m38s)
01:14:38

[said right and so when I write code I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m40s)
01:14:40

[want it to be as much like that as](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m42s)
01:14:42

[possible all right I want it to be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m45s)
01:14:45

[readable and so hopefully you'll find](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m46s)
01:14:46

[like when you look at the past AI code](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m49s)
01:14:49

[you can understand how to journey](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m50s)
01:14:50

[through X I try to write things in a way](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m52s)
01:14:52

[that you can read it and like it kind of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m54s)
01:14:54

[turn it into English in your head](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h14m56s)
01:14:56

[so if I say correctly that predict](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m01s)
01:15:01

[method is recursive it's no it's calling](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m04s)
01:15:04

[trade predict and we haven't written a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m08s)
01:15:08

[tree yet so self trees is going to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m10s)
01:15:10

[contain a tree object so this is tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m14s)
01:15:14

[Ensemble dot predict and inside the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m18s)
01:15:18

[trees is a tree not a tree ensemble so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m20s)
01:15:20

[this is called an trade product not tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m23s)
01:15:23

[ensemble dotted it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m25s)
01:15:25

[the question okay so we nearly finished](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m27s)
01:15:27

[riding around and for our seventh week](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m32s)
01:15:32

[all we need to do now is write create](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m33s)
01:15:33

[tree right so um based on this code here](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m35s)
01:15:35

[or on your own understanding of how we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m42s)
01:15:42

[create trees in a random forest can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m45s)
01:15:45

[somebody tell me let's take a few](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m48s)
01:15:48

[seconds have a raid have to think and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m51s)
01:15:51

[then I'm going to try and come up with a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m53s)
01:15:53

[way of saying how do you create a tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m54s)
01:15:54

[in a random forest](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h15m57s)
01:15:57

[okay who wants to tell me yes](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m01s)
01:16:01

[okay let's tireless work cluster](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m05s)
01:16:05

[you take your you're essentially taking](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m09s)
01:16:09

[a random sample or of the original data](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m14s)
01:16:14

[and then you're just it just](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m17s)
01:16:17

[constructing a tree however that happens](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m20s)
01:16:20

[so construct a decision tree like a non](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m23s)
01:16:23

[random tree from a random sample of the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m26s)
01:16:26

[data ok so again like we've delayed any](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m29s)
01:16:29

[actual thought process here we've](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m33s)
01:16:33

[basically said ok we could pick some](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m35s)
01:16:35

[random IDs this is a good trick to know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m37s)
01:16:37

[if you call NP random permutation](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m40s)
01:16:40

[passing in an inch it'll give you back a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m43s)
01:16:43

[randomly shuffled sequence from zero to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m47s)
01:16:47

[that inch right and so then if you grab](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m51s)
01:16:51

[the first : n items of that that's now a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m53s)
01:16:53

[random subsample so this is not doing](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h16m58s)
01:16:58

[bootstrapping we're not doing sampling](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m01s)
01:17:01

[with replacement here which i think is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m03s)
01:17:03

[fine you know for my random forest I'm](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m07s)
01:17:07

[deciding that it's going to be something](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m10s)
01:17:10

[where we do subsampling not](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m11s)
01:17:11

[bootstrapping](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m13s)
01:17:13

[ok so here's a good line of code to know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m14s)
01:17:14

[how to write because it comes up all the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m17s)
01:17:17

[time like I find in machine learning](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m21s)
01:17:21

[most algorithms I use are somewhat](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m22s)
01:17:22

[random and so often I need some kind of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m26s)
01:17:26

[random sample can you pass that tartaric](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m28s)
01:17:28

[entry won't they give you 1 1 extra](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m30s)
01:17:30

[because the easier it will go from 0 to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m37s)
01:17:37

[length no so this will give you if lens](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m40s)
01:17:40

[self dot y is of size n this will give](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m45s)
01:17:45

[you n a sequence of length n so 0 to n](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m50s)
01:17:50

[minus 1 and then from that I'm picking](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m53s)
01:17:53

[out : self dot sample size so the first](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h17m57s)
01:17:57

[sample size ladies I have a comment on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m00s)
01:18:00

[bootstrapping I think this method is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m07s)
01:18:07

[better because we have transfer giving](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m09s)
01:18:09

[more weights to each observation or am I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m12s)
01:18:12

[thinking wrong I think you proposed](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m16s)
01:18:16

[wrapping we could also give weights I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m18s)
01:18:18

[mean we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m20s)
01:18:20

[single observations more than they are](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m23s)
01:18:23

[like without one thing that weights](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m25s)
01:18:25

[because I'm bootstrapping with with](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m28s)
01:18:28

[replacement we can have a single](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m30s)
01:18:30

[observation and dr. pitz of it yeah the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m33s)
01:18:33

[same tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m36s)
01:18:36

[yeah it just feel weird but I think](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m36s)
01:18:36

[the actual theory or empirical results](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m43s)
01:18:43

[backs up higher intuition that it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m45s)
01:18:45

[worse it'd be interesting to look look](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m47s)
01:18:47

[back at that actually personally I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m51s)
01:18:51

[prefer this because I feel like most of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m55s)
01:18:55

[the time we have more data than we want](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h18m57s)
01:18:57

[to put a tree at once I feel like back](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m00s)
01:19:00

[when Bremen created random forests it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m02s)
01:19:02

[was 1999 it was kind of a very different](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m04s)
01:19:04

[world you know where we pretty much](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m06s)
01:19:06

[always wanted to use all the data we had](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m08s)
01:19:08

[but nowadays I would say that's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m09s)
01:19:09

[generally not what we want we normally](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m12s)
01:19:12

[have too much data and so what people](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m15s)
01:19:15

[tend to do is they'll like fire up a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m16s)
01:19:16

[spark cluster and they'll run it on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m19s)
01:19:19

[hundreds of machines when it makes no](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m20s)
01:19:20

[sense because if they had just used a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m24s)
01:19:24

[subsample each time they could have done](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m25s)
01:19:25

[it on one machine and like the the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m27s)
01:19:27

[overhead of like spark is a huge amount](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m29s)
01:19:29

[of i/o overhead like I know you guys are](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m32s)
01:19:32

[doing distributed computing now if you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m34s)
01:19:34

[if you've looked at some of the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m36s)
01:19:36

[benchmarks yeah yeah exactly so if you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m37s)
01:19:37

[do something on a single machine it can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m42s)
01:19:42

[often be hundreds of times faster](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m44s)
01:19:44

[because you don't have all this this i/o](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m46s)
01:19:46

[overhead it also tends to be easier to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m48s)
01:19:48

[write the algorithms like you can use](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m51s)
01:19:51

[like SK learn easier to visualize and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m52s)
01:19:52

[cheaper so forth so like I almost always](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h19m56s)
01:19:56

[avoid distributed computing and I have](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m00s)
01:20:00

[my whole life like even 25 years ago](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m02s)
01:20:02

[when I was studying in machine learning](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m04s)
01:20:04

[I you know still didn't use clusters](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m06s)
01:20:06

[because I so I always feel like whatever](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m09s)
01:20:09

[I could do with a cluster now I could do](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m11s)
01:20:11

[with a single machine in five years time](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m14s)
01:20:14

[so one of us focus on always being as](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m15s)
01:20:15

[good as possible with the single machine](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m18s)
01:20:18

[you know and that's going to be more](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m19s)
01:20:19

[interactive and more iterative and work](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m21s)
01:20:21

[for me so ah okay so so again we've like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m24s)
01:20:24

[delayed thinking to the point where we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m29s)
01:20:29

[have to write decision tree and so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m32s)
01:20:32

[hopefully you get an idea that this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m34s)
01:20:34

[top-down approach that goal is going to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m36s)
01:20:36

[be that we're going to keep delaying](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m38s)
01:20:38

[thinking so long that that we delay it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m39s)
01:20:39

[forever](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m42s)
01:20:42

[like like eventually we've somehow](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m42s)
01:20:42

[written the whole thing without actually](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m44s)
01:20:44

[having to think right and that's that's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m46s)
01:20:46

[kind of what I need is I'm kind of slow](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m48s)
01:20:48

[right so this is why I write code this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m49s)
01:20:49

[way and notice like you never have to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m52s)
01:20:52

[design anything in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m54s)
01:20:54

[you just say hey what if somebody](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m56s)
01:20:56

[already gave me the exact API I needed](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m57s)
01:20:57

[how would I use it okay and then and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h20m59s)
01:20:59

[then okay to implement that next stage](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m02s)
01:21:02

[what would be the exact API I would need](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m04s)
01:21:04

[to implement that right you keep going](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m07s)
01:21:07

[down until eventually you're like oh](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m09s)
01:21:09

[that already exists okay so this assumes](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m10s)
01:21:10

[we've got a class port decision tree so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m14s)
01:21:14

[we're going to have to create that so a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m17s)
01:21:17

[decision tree is something so we already](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m21s)
01:21:21

[know what we're going to have to pass it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m25s)
01:21:25

[because we just passed it right so we're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m26s)
01:21:26

[passing in a random sample of X's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m28s)
01:21:28

[random sample of Y's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m32s)
01:21:32

[um](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m36s)
01:21:36

[uhh](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m38s)
01:21:38

[indexers is actually so we know that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m40s)
01:21:40

[down the track so I've got a plan a tiny](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m43s)
01:21:43

[bit we know that a decision tree is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m46s)
01:21:46

[going to contain decision trees which](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m48s)
01:21:48

[themselves contain decision trees and so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m51s)
01:21:51

[as we go down the decision tree there's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m52s)
01:21:52

[going to be some subset of the original](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m55s)
01:21:55

[data that we've kind of got and so I'm](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m56s)
01:21:56

[going to pass in the indexes of the data](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h21m59s)
01:21:59

[that we're actually going to use here](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m02s)
01:22:02

[okay so initially it's the entire random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m03s)
01:22:03

[sample all right so I've got the whole](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m07s)
01:22:07

[team I've got the whole range and I turn](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m09s)
01:22:09

[that into an array so that's 0 the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m15s)
01:22:15

[indexes from 0 to the size of the sample](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m17s)
01:22:17

[and then what is passed down the mean](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m19s)
01:22:19

[left side so everything that we got for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m22s)
01:22:22

[constructing the random forest where to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m24s)
01:22:24

[pass down the decision tree except of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m27s)
01:22:27

[course num trees which is irrelevant for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m29s)
01:22:29

[the decision tree so again now that we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m31s)
01:22:31

[know that's the information we need we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m34s)
01:22:34

[can go ahead and store it inside this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m35s)
01:22:35

[object so I'm pretty likely to need to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m38s)
01:22:38

[know how many rows we have in this tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m42s)
01:22:42

[which I generally call n how many](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m46s)
01:22:46

[columns do I have which I generally call](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m49s)
01:22:49

[C so the number of rows is just equal to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m51s)
01:22:51

[the number of indexes well given and the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m54s)
01:22:54

[number of columns is just like however](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m56s)
01:22:56

[many columns there are in our](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h22m58s)
01:22:58

[independent variables so then we're](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m00s)
01:23:00

[going to need this value here](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m04s)
01:23:04

[we need to know for this tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m11s)
01:23:11

[what's its prediction right so the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m14s)
01:23:14

[prediction for this tree is the mean of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m20s)
01:23:20

[our dependent variable or those indexes](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m23s)
01:23:23

[which are inside this part of the tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m29s)
01:23:29

[alright so at the very top of the tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m31s)
01:23:31

[it contains all the indexes right I'm](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m34s)
01:23:34

[assuming that by the time we've got to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m38s)
01:23:38

[this point remember we've already done](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m40s)
01:23:40

[the random sampling right so when we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m42s)
01:23:42

[talk about indexes we're not talking](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m47s)
01:23:47

[about the random sampling to create the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m49s)
01:23:49

[tree we're assuming this tree now has](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m51s)
01:23:51

[some random sample inside decision tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m53s)
01:23:53

[this is this is the one of the nice](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m57s)
01:23:57

[things right inside decision tree hole](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h23m58s)
01:23:58

[random sampling things gone right that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m01s)
01:24:01

[was done by the random forest right so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m02s)
01:24:02

[at this point we're building something](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m04s)
01:24:04

[that's just a plain old decision tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m06s)
01:24:06

[it's not in any way a random sampling](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m08s)
01:24:08

[anything it's just a plain old position](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m10s)
01:24:10

[tree right so the indexes is literally](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m11s)
01:24:11

[like which subset of the data that we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m15s)
01:24:15

[got to so far in this tree and so at the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m19s)
01:24:19

[top of the decision tree it's all the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m21s)
01:24:21

[data right so it's all of the indexes](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m23s)
01:24:23

[okay so all of the indexes so this is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m25s)
01:24:25

[therefore all of the dependent variable](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m31s)
01:24:31

[that are in this part of the tree and so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m34s)
01:24:34

[this is the value mean of that that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m36s)
01:24:36

[makes sense](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m40s)
01:24:40

[anybody could be any questions about](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m41s)
01:24:41

[about that so ah yes hey pastor Chen Qi](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m42s)
01:24:42

[actually just to let you know there's a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m50s)
01:24:50

[large portion of us don't have a over B](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m52s)
01:24:52

[I mean all P experiments okay yeah sure](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m55s)
01:24:55

[so so quick so quick over P prenup would](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h24m59s)
01:24:59

[be helpful](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m03s)
01:25:03

[great yeah okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m04s)
01:25:04

[who is done object-oriented programming](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m08s)
01:25:08

[in some programming language okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m11s)
01:25:11

[so you've all used actually lots of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m18s)
01:25:18

[object-oriented programming in terms of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m21s)
01:25:21

[using existing classes right so every](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m23s)
01:25:23

[time we've created a random forest we've](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m26s)
01:25:26

[called the random forests constructor](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m31s)
01:25:31

[and it's returned an object and then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m34s)
01:25:34

[we've called methods and attributes on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m38s)
01:25:38

[that object so fit is a method you can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m42s)
01:25:42

[tell because it's got parentheses after](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m45s)
01:25:45

[it right where else yeah](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m46s)
01:25:46

[oh I'll be score is a property or an](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m52s)
01:25:52

[attribute doesn't have parentheses after](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m56s)
01:25:56

[it okay](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m58s)
01:25:58

[so inside an object there are kind of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h25m59s)
01:25:59

[two kinds of things there the functions](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m01s)
01:26:01

[that you can call so you have object dot](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m03s)
01:26:03

[function parentheses arguments or there](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m07s)
01:26:07

[are the properties or attributes you can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m10s)
01:26:10

[grab which is object dot and then just](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m12s)
01:26:12

[the attribute name no parentheses so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m16s)
01:26:16

[when and then the other thing that we do](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m19s)
01:26:19

[with objects is we create them okay we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m21s)
01:26:21

[pass in the name of a class and it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m26s)
01:26:26

[returns us the object and you have to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m28s)
01:26:28

[tell it all of the parameters necessary](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m30s)
01:26:30

[to get constructed so let's just copy](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m32s)
01:26:32

[this code and see how we're going to go](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m37s)
01:26:37

[ahead and build this so the first step](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m46s)
01:26:46

[is we're not going to go n equals random](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m49s)
01:26:49

[forest regressor we're going to go M](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m52s)
01:26:52

[equals tree ensemble we're creating a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m53s)
01:26:53

[classical tree ensemble and we're going](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m56s)
01:26:56

[to pass in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h26m58s)
01:26:58

[various bits of information okay so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m04s)
01:27:04

[maybe we'll have ten trees sample size](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m09s)
01:27:09

[of a thousand or maybe a min leaf of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m12s)
01:27:12

[three okay and you can always like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m15s)
01:27:15

[choose to name your admits or not so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m17s)
01:27:17

[when you've got quite a few it's kind of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m19s)
01:27:19

[nice to name them so that just so we can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m21s)
01:27:21

[see what each one means it's always](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m23s)
01:27:23

[optional so we're going to try and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m27s)
01:27:27

[create a class that we can use like this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m32s)
01:27:32

[and then the notional we're going to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m35s)
01:27:35

[bother with dot fit because we've passed](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m39s)
01:27:39

[in the X and the y right like in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m41s)
01:27:41

[scikit-learn they use an approach where](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m44s)
01:27:44

[first of all you construct something](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m46s)
01:27:46

[without telling it what they did here is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m48s)
01:27:48

[and then you pass in the day we're doing](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m49s)
01:27:49

[these two steps at once](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m52s)
01:27:52

[we're actually passing in the data right](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m53s)
01:27:53

[and so then after that we're going to be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m55s)
01:27:55

[going and dot so we're going to go creds](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h27m57s)
01:27:57

[equals m predict passing in maybe some](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m01s)
01:28:01

[validations there okay so we that's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m06s)
01:28:06

[that's the API we're kind of creating](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m09s)
01:28:09

[here so this thing here is called a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m11s)
01:28:11

[constructor something that creates an](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m14s)
01:28:14

[object is called a constructor and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m16s)
01:28:16

[Python there's a lot of ugly hideous](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m19s)
01:28:19

[things about Python one of which is they](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m23s)
01:28:23

[it uses these special magic method names](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m26s)
01:28:26

[underscore underscore init underscore](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m30s)
01:28:30

[underscore is a special magic method](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m33s)
01:28:33

[that's caught it's called](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m35s)
01:28:35

[when you try to construct a class so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m37s)
01:28:37

[when I call tree ensemble parentheses it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m40s)
01:28:40

[actually calls tree ensemble dot they](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m43s)
01:28:43

[see people say dunder init I kind of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m45s)
01:28:45

[hate it but anyway timed it you know](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m47s)
01:28:47

[double underscore in it double](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m49s)
01:28:49

[underscore dunder init](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m52s)
01:28:52

[so that's why we've got this method](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m54s)
01:28:54

[called dunder init okay so when I call](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m56s)
01:28:56

[tree ensemble is going to call this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h28m59s)
01:28:59

[method](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m01s)
01:29:01

[another hideously ugly thing about](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m02s)
01:29:02

[pythons oo is that there's this special](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m06s)
01:29:06

[thing where if you have a class and to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m10s)
01:29:10

[create a class you just wrecked class in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m13s)
01:29:13

[the name of us all of its methods](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m14s)
01:29:14

[automatically get sent one extra](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m17s)
01:29:17

[parameter when extra arguments which is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m20s)
01:29:20

[the first argument and you can call it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m23s)
01:29:23

[anything you like if you call it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m25s)
01:29:25

[anything other than self everybody will](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m27s)
01:29:27

[hate you and you're a bad person so call](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m30s)
01:29:30

[it anything you like as long as it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m33s)
01:29:33

[self so so that's why you always see](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m34s)
01:29:34

[this and in fact I can immediately see](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m40s)
01:29:40

[here I have a bug anybody see the bug in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m42s)
01:29:42

[my predict function I should have so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m45s)
01:29:45

[right I like it always do it right so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m48s)
01:29:48

[anytime you try and call a method on](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m52s)
01:29:52

[your own class and you get something](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m54s)
01:29:54

[saying you're passed in two parameters](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m56s)
01:29:56

[and it was only expecting one you forgot](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h29m58s)
01:29:58

[so okay so like this is a really dumb](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m00s)
01:30:00

[way to add oh okay to a programming](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m04s)
01:30:04

[language but the older languages like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m06s)
01:30:06

[Python often did this because they kind](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m08s)
01:30:08

[of needed to they started out not being](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m10s)
01:30:10

[oo and then they kind of added oo in a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m12s)
01:30:12

[way that was hideously ugly so Perl](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m15s)
01:30:15

[which predates plaything by a little bit](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m17s)
01:30:17

[kind of I think really came up with this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m20s)
01:30:20

[approach and unfortunately other](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m22s)
01:30:22

[languages of that era stuck with it so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m24s)
01:30:24

[you have to add in this magic self so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m28s)
01:30:28

[the magic self now when you're inside](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m31s)
01:30:31

[this class you can now pretend as if any](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m35s)
01:30:35

[property name you like exists so I can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m39s)
01:30:39

[now pretend there's something called](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m42s)
01:30:42

[self dot X I can read from it I can](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m43s)
01:30:43

[write to it right but if I read from it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m46s)
01:30:46

[and I haven't yet written to it I'll get](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m48s)
01:30:48

[an error so the stuff that's passed to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m50s)
01:30:50

[the constructor gets thrown away by](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m55s)
01:30:55

[default like there's nothing that like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m58s)
01:30:58

[says you need to rip this class needs to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h30m59s)
01:30:59

[remember what these things are but](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m02s)
01:31:02

[anything that we stick inside self is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m04s)
01:31:04

[remembered for all time you know as long](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m06s)
01:31:06

[as this object exists you can access it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m09s)
01:31:09

[it's remembered so now that I've gone](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m12s)
01:31:12

[in fact let's do this right so that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m15s)
01:31:15

[let's create the tree ensemble class and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m17s)
01:31:17

[let's now instantiate it okay of course](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m21s)
01:31:21

[we haven't got X we need to call X train](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m26s)
01:31:26

[y trade ok decision tree is not defined](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m31s)
01:31:31

[so let's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m39s)
01:31:39

[we had a really minimal decision tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m43s)
01:31:43

[there we go okay so here is enough to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m51s)
01:31:51

[actually instantiate our tree ensemble](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m54s)
01:31:54

[okay so we have to find the inert for it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m56s)
01:31:56

[we have to find the inert for decision](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h31m59s)
01:31:59

[tree we need decision trees in it to be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m01s)
01:32:01

[defined because inside our ensemble in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m03s)
01:32:03

[it they're called self directory and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m06s)
01:32:06

[then self create tree called the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m08s)
01:32:08

[decision tree constructor and then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m11s)
01:32:11

[decision tree constructor basically does](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m13s)
01:32:13

[nothing at all other than save some](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m16s)
01:32:16

[information right so at this point we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m18s)
01:32:18

[can now go m dot okay and if I press tab](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m20s)
01:32:20

[at this point can anybody tell me what I](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m27s)
01:32:27

[would expect to see press it to Taylor](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m31s)
01:32:31

[tension could you possibly say like we](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m34s)
01:32:34

[would see a drop-down of all available](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m40s)
01:32:40

[methods for that class okay it would be](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m42s)
01:32:42

[in this case so if M is a tree ensemble](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m44s)
01:32:44

[we would have create tree and predict](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m48s)
01:32:48

[okay anything else what](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m49s)
01:32:49

[oh yeah as well as earnest whispered to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m53s)
01:32:53

[variables as well yeah so that the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m55s)
01:32:55

[variable could made a lot of things well](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h32m59s)
01:32:59

[attributes so the things that we put](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m01s)
01:33:01

[inside self so if I hit tab right there](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m03s)
01:33:03

[they are right as Taylor said there's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m06s)
01:33:06

[create tree there's predict and then](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m07s)
01:33:07

[there's everything else we put inside so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m10s)
01:33:10

[all right so if I look at m dot min leaf](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m11s)
01:33:11

[if I hit shift enter what will I see yep](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m19s)
01:33:19

[the number that I just put there I put](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m24s)
01:33:24

[in leaf is three so that went up the air](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m26s)
01:33:26

[dam in leaf this here is a default](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m29s)
01:33:29

[argument such as if I don't pass](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m31s)
01:33:31

[anything it'll be five but I did pass](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m33s)
01:33:33

[something right so three self dot min](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m34s)
01:33:34

[leaf here is it going to be equal to min](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m37s)
01:33:37

[leaf yeah so something which like](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m41s)
01:33:41

[because of this rather annoying way of](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m45s)
01:33:45

[doing oh oh](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m47s)
01:33:47

[it does mean that it's very easy to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m49s)
01:33:49

[accidentally forget so do that right so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m51s)
01:33:51

[if I don't assign it to self dot min](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m55s)
01:33:55

[leaf right then I get an error and so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h33m57s)
01:33:57

[here tree ensemble doesn't happen in](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m02s)
01:34:02

[leaf right so how do I create that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m04s)
01:34:04

[attribute](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m06s)
01:34:06

[I just put something in it okay so if](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m07s)
01:34:07

[you want to like if you don't know what](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m12s)
01:34:12

[a value of it should be yet but you kind](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m14s)
01:34:14

[of need to be able to refer to it you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m16s)
01:34:16

[can always feel like self dot min leaf](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m18s)
01:34:18

[equals none that's at least there's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m21s)
01:34:21

[something you can read check for](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m24s)
01:34:24

[numbness and not have an error great now](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m25s)
01:34:25

[interestingly I was able to instantiate](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m34s)
01:34:34

[tree ensemble even if I predict refers](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m36s)
01:34:36

[to a method of decision tree that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m40s)
01:34:40

[doesn't exist and this is actually](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m42s)
01:34:42

[something very nice about the dynamic](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m45s)
01:34:45

[nature of Python is that because it's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m48s)
01:34:48

[not like compiling it it's not checking](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m52s)
01:34:52

[anything unless you're using it right so](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m55s)
01:34:55

[we can go ahead and create decision to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h34m58s)
01:34:58

[predict later](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m01s)
01:35:01

[and then our our instantiated object](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m02s)
01:35:02

[will magically start working right it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m05s)
01:35:05

[doesn't actually look up that functions](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m08s)
01:35:08

[that methods details until you use it](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m10s)
01:35:10

[and so it really helps with top-down](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m12s)
01:35:12

[programming](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m14s)
01:35:14

[okay so when you're inside a class](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m18s)
01:35:18

[definition in other words you're at that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m22s)
01:35:22

[indentation level you know indented one](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m24s)
01:35:24

[in so these are all class definitions](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m27s)
01:35:27

[any function that you create unless you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m29s)
01:35:29

[do some special things that we're not](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m32s)
01:35:32

[going to talk about yet is automatically](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m34s)
01:35:34

[a method of that class and so every](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m37s)
01:35:37

[method of that class magically gets a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m40s)
01:35:40

[self passed to it so we could call since](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m42s)
01:35:42

[we've got a tree ensemble we could call](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m49s)
01:35:49

[em create tree and we don't put anything](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m50s)
01:35:50

[inside those parentheses because the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m54s)
01:35:54

[magic self will be passed and the magic](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m56s)
01:35:56

[self will be whatever M is okay so m dot](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h35m58s)
01:35:58

[create tree returns a decision tree just](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m03s)
01:36:03

[like we asked it to right so m dot](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m06s)
01:36:06

[create tree dot e excess will give us](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m09s)
01:36:09

[the self ID access inside the decision](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m15s)
01:36:15

[tree okay which is set to NP dot a range](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m17s)
01:36:17

[range self dot sample size Y is data](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m23s)
01:36:23

[scientists do we care about](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m29s)
01:36:29

[object-oriented programming because a](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m30s)
01:36:30

[lot of the stuff you use is going to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m34s)
01:36:34

[require you to implement stuff with oo P](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m37s)
01:36:37

[for example every single PI torch model](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m40s)
01:36:40

[of any kind is created with olp it's the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m44s)
01:36:44

[only way to create by torch models um](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m47s)
01:36:47

[good news is what you see here is the](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m50s)
01:36:50

[entirety of what you need to know so you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m55s)
01:36:55

[this is all you need to know you need to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m58s)
01:36:58

[know to create some in code in it to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h36m59s)
01:36:59

[assign the things to the pasta in it to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m02s)
01:37:02

[something call it self and then just](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m04s)
01:37:04

[stick the word self after it give your](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m07s)
01:37:07

[methods okay and so the nice thing is](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m09s)
01:37:09

[like now to think as an AOP programmer](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m11s)
01:37:11

[is to realize you don't now have to pass](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m14s)
01:37:14

[around X Y sample size and min leaf to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m17s)
01:37:17

[every function that uses them by](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m20s)
01:37:20

[assigning them to attributes itself](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m22s)
01:37:22

[they're now available like magic all](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m25s)
01:37:25

[right so this is why our peas super](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m29s)
01:37:29

[handy](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m31s)
01:37:31

[if you're particularly I started trying](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m32s)
01:37:32

[to create a decision tree initially](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m34s)
01:37:34

[without using oot and try to like keep](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m35s)
01:37:35

[track of like what that decision tree](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m38s)
01:37:38

[was meant to know about it was very](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m41s)
01:37:41

[difficult you know where else with our P](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m43s)
01:37:43

[you can just say even side the decision](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m45s)
01:37:45

[tree you know self indexes equals this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m48s)
01:37:48

[and everything displace okay okay that's](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m50s)
01:37:50

[great so we're out of time I think](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m54s)
01:37:54

[that's that's great timing because](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m55s)
01:37:55

[there's an introduction 200 P but this](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h37m59s)
01:37:59

[week you know next class I'm going to](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m02s)
01:38:02

[assume that you can use it right so you](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m05s)
01:38:05

[should create some classes instantiate](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m07s)
01:38:07

[some classes look at their methods and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m09s)
01:38:09

[properties have them call each other and](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m12s)
01:38:12

[so forth until you feel comfortable with](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m15s)
01:38:15

[them and maybe for those of you doesn't](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m17s)
01:38:17

[haven't done our P before you can find](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m20s)
01:38:20

[some other useful resources you could](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m22s)
01:38:22

[flop them onto the wiki thread so that](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m24s)
01:38:24

[other people know what you find useful](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m26s)
01:38:26

[right thanks everybody](https://www.youtube.com/watch?v=3jl2h9hSRvc#t=01h38m28s)
01:38:28

