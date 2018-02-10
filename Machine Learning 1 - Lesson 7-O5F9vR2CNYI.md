[welcome back we're going to be talking](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m00s)
00:00:00

[today about random forests we're going](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m01s)
00:00:01

[to finish building our own random forest](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m05s)
00:00:05

[from scratch but before we do I wanted](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m07s)
00:00:07

[to tackle a few things that have come up](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m12s)
00:00:12

[during the week a few questions that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m14s)
00:00:14

[I've had and I want to start with kind](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m16s)
00:00:16

[of the position of random forests in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m19s)
00:00:19

[general so we spent about half of his](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m21s)
00:00:21

[course doing random forests and then](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m25s)
00:00:25

[after today the second half of this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m27s)
00:00:27

[course will be neural networks broadly](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m29s)
00:00:29

[defined](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m32s)
00:00:32

[this is because these these to represent](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m38s)
00:00:38

[like the tea the two key classes of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m42s)
00:00:42

[techniques which cover nearly everything](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m44s)
00:00:44

[that you're likely to need to do random](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m47s)
00:00:47

[forests belong to the class of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m50s)
00:00:50

[techniques of decision tree ensembles](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m51s)
00:00:51

[along with gradient boosting machines](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m54s)
00:00:54

[being the other key type and some](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m57s)
00:00:57

[variants like extremely randomized trees](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h00m58s)
00:00:58

[they have the benefit that they're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m01s)
00:01:01

[highly interpretive all scalable](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m05s)
00:01:05

[flexible work well for most kinds of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m08s)
00:01:08

[data they have the downside that they](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m11s)
00:01:11

[don't extrapolate at all to like data](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m13s)
00:01:13

[that's outside the range that you've](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m18s)
00:01:18

[seen as we looked at at the end of last](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m19s)
00:01:19

[week's session but you know they're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m21s)
00:01:21

[there they're a great starting point and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m27s)
00:01:27

[so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m28s)
00:01:28

[I think you know there's a huge](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m31s)
00:01:31

[catalogue of machine learning tools out](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m33s)
00:01:33

[there and I got lot of courses and books](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m36s)
00:01:36

[don't attempt to kind of curate that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m39s)
00:01:39

[down and say like for these kinds of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m42s)
00:01:42

[problems use this for these kinds of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m44s)
00:01:44

[problems is that finished you know but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m46s)
00:01:46

[they're rather like here's a description](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m48s)
00:01:48

[of 100 different algorithms and you just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m51s)
00:01:51

[don't need them you know like I don't](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m54s)
00:01:54

[see why you would ever use in support](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m57s)
00:01:57

[vector machine today for instance like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h01m59s)
00:01:59

[not know no reason at all I could think](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m02s)
00:02:02

[of doing that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m04s)
00:02:04

[people love studying them in the 90s](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m05s)
00:02:05

[because they are like very theoretically](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m08s)
00:02:08

[elegant and like you can really write a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m09s)
00:02:09

[lot of math about support vector](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m12s)
00:02:12

[machines and people did but you know in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m14s)
00:02:14

[practice I don't see them as having any](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m15s)
00:02:15

[place](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m18s)
00:02:18

[there's like a lot of techniques that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m23s)
00:02:23

[you could include in an exhaustive list](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m24s)
00:02:24

[of every way that people adopt machine](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m26s)
00:02:26

[learning problems but I would rather](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m28s)
00:02:28

[tell you like how to actually solve](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m31s)
00:02:31

[machine learning problems in practice I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m32s)
00:02:32

[think they you know we've we've about to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m34s)
00:02:34

[finish today the first class which is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m36s)
00:02:36

[you know one type of decision tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m38s)
00:02:38

[ensembles in in part to you net will](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m40s)
00:02:40

[tell you about the other key type there](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m43s)
00:02:43

[being gradient boosting and we're about](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m45s)
00:02:45

[to launch next lesson into neural nets](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m47s)
00:02:47

[which includes all kinds of GLM Ridge](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m50s)
00:02:50

[regression elastic net lasso logistic](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m54s)
00:02:54

[regression etc or all variants of neural](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h02m58s)
00:02:58

[nets you know interestingly](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m01s)
00:03:01

[leo breiman who created random forests](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m07s)
00:03:07

[did so very late in his life and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m11s)
00:03:11

[unfortunately passed away not many years](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m14s)
00:03:14

[later so partly because of that very](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m17s)
00:03:17

[little has been written about them in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m21s)
00:03:21

[the academic literature partly because](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m23s)
00:03:23

[SVM's were just taken over at that point](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m26s)
00:03:26

[you know other people didn't look at](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m28s)
00:03:28

[them and also like just because they're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m30s)
00:03:30

[like quite hard to grasp at a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m35s)
00:03:35

[theoretical level like analyze them](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m38s)
00:03:38

[theoretically it's quite hard to write](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m40s)
00:03:40

[conference papers about them or academic](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m41s)
00:03:41

[papers about them so there hasn't been](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m43s)
00:03:43

[that much written about them](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m45s)
00:03:45

[but there's been a real resurgence or](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m47s)
00:03:47

[not resurgence a new wave in recent](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m49s)
00:03:49

[years of empirical machine learning like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m52s)
00:03:52

[what actually works](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m54s)
00:03:54

[kegels been part of that but also just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m56s)
00:03:56

[in part of it has just been like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h03m59s)
00:03:59

[companies using machine learning to make](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m01s)
00:04:01

[ loads of money like Amazon and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m03s)
00:04:03

[Google and so nowadays a lot of people](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m05s)
00:04:05

[are writing about decision tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m08s)
00:04:08

[ensembles in creating better software](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m11s)
00:04:11

[for decision tree ensembles like like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m12s)
00:04:12

[GBM and x3 boost and Ranger 4r and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m14s)
00:04:14

[scikit-learn and so forth but a lot of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m19s)
00:04:19

[this is being done in industry rather](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m23s)
00:04:23

[than academia but you know it's it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m25s)
00:04:25

[encouraging to see there's certainly](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m29s)
00:04:29

[more work being done in deep learning](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m33s)
00:04:33

[than in decision tree ensembles](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m36s)
00:04:36

[particularly in in academia but but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m38s)
00:04:38

[there's a lot of progress being made in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m42s)
00:04:42

[both you know if you look at like of the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m44s)
00:04:44

[packages being used today for decision](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m48s)
00:04:48

[tree ensembles like all the best ones](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m50s)
00:04:50

[the top five or six I don't know that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m53s)
00:04:53

[any of them really existed](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m55s)
00:04:55

[five years ago you know maybe other than](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h04m57s)
00:04:57

[like SK learn or even three years ago so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m00s)
00:05:00

[yet so that's that's been good but I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m02s)
00:05:02

[think there's a lot of work still to be](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m06s)
00:05:06

[done we talked about for example](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m08s)
00:05:08

[figuring out what interactions are the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m11s)
00:05:11

[most important last week and some of you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m14s)
00:05:14

[pointed out in the forum's that actually](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m17s)
00:05:17

[there is such a project already for a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m18s)
00:05:18

[gradient boosting machine](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m20s)
00:05:20

[which is great but it doesn't seem that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m22s)
00:05:22

[there's anything like that yet for](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m23s)
00:05:23

[random forests and you know random](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m24s)
00:05:24

[forests do have a nice benefit over gbms](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m27s)
00:05:27

[that they're kind of harder to screw up](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m29s)
00:05:29

[you know and easier to scale so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m32s)
00:05:32

[hopefully that's something that you know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m37s)
00:05:37

[this community might help fix another](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m39s)
00:05:39

[question I had during the week was about](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m43s)
00:05:43

[the size of your validations that how](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m45s)
00:05:45

[big should it be so like to answer this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m50s)
00:05:50

[question about how big does your](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m54s)
00:05:54

[validation set need to be you first need](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m56s)
00:05:56

[to answer the question how how accurate](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h05m59s)
00:05:59

[do I need help recite to know the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m05s)
00:06:05

[accuracy of this algorithm right so like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m08s)
00:06:08

[if the validation set that you have is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m13s)
00:06:13

[saying like this is 70% accurate and if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m16s)
00:06:16

[somebody said well is it 75% or 65% or](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m20s)
00:06:20

[70% and the answer was I don't know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m23s)
00:06:23

[anything in that range is close enough](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m25s)
00:06:25

[like that would be one answer where else](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m27s)
00:06:27

[if it's like is that 70 percent or 70](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m30s)
00:06:30

[point oh one percent or sixty nine point](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m33s)
00:06:33

[nine nine percent like then that's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m34s)
00:06:34

[something else again](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m37s)
00:06:37

[right so you need to kind of start out](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m38s)
00:06:38

[by saying like how how accurate do I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m40s)
00:06:40

[need this so like for example in the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m42s)
00:06:42

[deep learning course we've been looking](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m46s)
00:06:46

[at dogs versus cats images and the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m48s)
00:06:48

[models that we're looking at had about a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m52s)
00:06:52

[ninety nine point four ninety nine point](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m54s)
00:06:54

[five percent accuracy on the validation](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h06m58s)
00:06:58

[set and a validation set size was 2000](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h07m00s)
00:07:00

[okay in fact let's do this in Excel](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h07m08s)
00:07:08

[that'll be a bit easier so our](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h07m10s)
00:07:10

[validation set size was 2000 and was](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h07m15s)
00:07:15

[99.4% right so the number of incorrect](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h07m24s)
00:07:24

[is something around one - accuracy times](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h07m29s)
00:07:29

[and so we were getting about 12 wrong](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h07m37s)
00:07:37

[right and the number of cats we had is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h07m41s)
00:07:41

[1/2 and so the number of wrong cats is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h07m49s)
00:07:49

[about 6 ok so then like we we run a new](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h07m54s)
00:07:54

[model and we find instead that the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m02s)
00:08:02

[accuracy has gone to 99.2% right and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m05s)
00:08:05

[then it's like okay is this less good at](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m12s)
00:08:12

[finding cats that's like well it got 2](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m14s)
00:08:14

[more cats wrong](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m17s)
00:08:17

[so it's like probably not right so but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m19s)
00:08:19

[then it's like well does this matter](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m24s)
00:08:24

[there's ninety nine point four versus](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m26s)
00:08:26

[ninety nine point two matter and if this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m28s)
00:08:28

[was like it wasn't about cats and dogs](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m31s)
00:08:31

[but it was about finding fraud right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m33s)
00:08:33

[then the difference between a point six](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m36s)
00:08:36

[percent error rate and a point eight](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m39s)
00:08:39

[percent error rate is like twenty five](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m40s)
00:08:40

[percent of your cost of fraud](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m41s)
00:08:41

[so like that can be huge like it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m43s)
00:08:43

[really interesting like when imagenet](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m48s)
00:08:48

[came out earlier this year the new](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m49s)
00:08:49

[competition results came out and the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m51s)
00:08:51

[accuracy had gone down from three](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m53s)
00:08:53

[percent so the error went down from](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m55s)
00:08:55

[three percent to two percent and I saw a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h08m58s)
00:08:58

[lot of people on the internet like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m00s)
00:09:00

[famous machine learning researchers](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m02s)
00:09:02

[being like yeah some Chinese guys got it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m03s)
00:09:03

[better from like 97% to one ninety eight](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m07s)
00:09:07

[percent it's like statistically not even](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m09s)
00:09:09

[significant who cares kind of a thing](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m11s)
00:09:11

[but actually I thought like holy crap](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m13s)
00:09:13

[this Chinese team just blew away the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m17s)
00:09:17

[state-of-the-art an image recognition](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m20s)
00:09:20

[like the old one was fifty percent less](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m21s)
00:09:21

[accurate than the new one like that's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m23s)
00:09:23

[that's actually the right way to think](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m25s)
00:09:25

[about it isn't it because it's like you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m27s)
00:09:27

[know we were trying to recognize you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m29s)
00:09:29

[know like which tomatoes were ripe and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m31s)
00:09:31

[which ones weren't and like our new](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m34s)
00:09:34

[approach you know the old approach like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m38s)
00:09:38

[fifty percent of the time more was like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m40s)
00:09:40

[letting in the unripe Tomatoes or you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m43s)
00:09:43

[know 50 percent more of the time we were](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m47s)
00:09:47

[like accepting fraudulent customers like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m49s)
00:09:49

[that's a really big difference so just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m51s)
00:09:51

[because like this particular validation](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m55s)
00:09:55

[set we can't really see six versus eight](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m57s)
00:09:57

[doesn't mean the 0.2% different isn't](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h09m59s)
00:09:59

[important it could be so my kind of rule](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m01s)
00:10:01

[of thumb is that this like this number](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m05s)
00:10:05

[of like how many observations you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m07s)
00:10:07

[actually looking at I want that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m10s)
00:10:10

[generally to be somewhere higher than](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m12s)
00:10:12

[twenty-two why 22 because 22 is the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m14s)
00:10:14

[magic number where the t-distribution](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m17s)
00:10:17

[roughly turns into the normal](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m19s)
00:10:19

[distribution right so as you may have](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m22s)
00:10:22

[learned the T distribution is is the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m24s)
00:10:24

[normal distribution for small data sets](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m27s)
00:10:27

[right and so in other words once we have](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m30s)
00:10:30

[twenty-two of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m32s)
00:10:32

[thing or more it kind of starts to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m33s)
00:10:33

[behave kind of normally in both sense of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m36s)
00:10:36

[the words like it's kind of more stable](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m40s)
00:10:40

[and you can kind of understand it better](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m41s)
00:10:41

[so that's my magic number when somebody](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m43s)
00:10:43

[says do I have enough of something I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m47s)
00:10:47

[kind of start out by saying like do you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m49s)
00:10:49

[have 22 observations of the thing of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m50s)
00:10:50

[interest so if you were looking at like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m53s)
00:10:53

[Lyme cancer you know and you had a data](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m56s)
00:10:56

[set that had like a thousand people](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h10m59s)
00:10:59

[without lung cancer and 20 people with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m02s)
00:11:02

[lung cancer I'd be like I very much](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m04s)
00:11:04

[doubt we're going to make much progress](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m06s)
00:11:06

[you know because we haven't even got 20](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m08s)
00:11:08

[of the thing you want so ditto with a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m10s)
00:11:10

[validation set if you don't have twenty](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m12s)
00:11:12

[of the thing you want that is very](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m14s)
00:11:14

[unlikely to be useful or if like the at](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m16s)
00:11:16

[the level of accuracy we need it's not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m18s)
00:11:18

[plus or minus 20 it's just it's that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m20s)
00:11:20

[that's the point where I'm thinking like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m22s)
00:11:22

[be a bit careful so just to be clear you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m24s)
00:11:24

[want 22 to be the number of samples in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m28s)
00:11:28

[each set like in the validation the test](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m33s)
00:11:33

[and the Train](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m35s)
00:11:35

[so what I'm saying is like if there's if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m37s)
00:11:37

[there's less than 22 of a class in any](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m40s)
00:11:40

[of the sets then it's it's going to get](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m44s)
00:11:44

[it's getting pretty unstable at that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m48s)
00:11:48

[point right and so like that's just like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m50s)
00:11:50

[the first rule of thumb but then what I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m53s)
00:11:53

[would actually do is like start](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m56s)
00:11:56

[practicing what we learned about the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h11m58s)
00:11:58

[binomial distribution or actually very](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m00s)
00:12:00

[weak distribution so what's the what is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m04s)
00:12:04

[the mean of the binomial distribution of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m11s)
00:12:11

[n samples and probability P n times P](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m14s)
00:12:14

[okay thank you and times P is that mean](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m20s)
00:12:20

[all right so if you've got a 50% chance](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m23s)
00:12:23

[of getting ahead and you toss it a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m26s)
00:12:26

[hundred times on average you get 50](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m29s)
00:12:29

[heads okay and then what's the standard](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m31s)
00:12:31

[deviation and P 1 minus B okay so these](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m34s)
00:12:34

[are like two numbers](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m44s)
00:12:44

[the first number you don't have to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m47s)
00:12:47

[remember it's intuitively obvious the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m48s)
00:12:48

[second one is one that try to remember](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m50s)
00:12:50

[forevermore because not only does it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m52s)
00:12:52

[come up all the time the people that you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m55s)
00:12:55

[work with we'll all have forgotten it so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m57s)
00:12:57

[you'll be like the one person in the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h12m59s)
00:12:59

[conversation who could immediately go we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m00s)
00:13:00

[don't have to run this 100 times I can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m02s)
00:13:02

[tell you straight away](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m04s)
00:13:04

[it's binomial it's going to be NP q NP 1](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m05s)
00:13:05

[minus B then there's the standard error](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m08s)
00:13:08

[the standard error is if you run a bunch](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m12s)
00:13:12

[of trials each time getting a mean what](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m16s)
00:13:16

[is the standard deviation of the mean I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m21s)
00:13:21

[don't think you guys are covered this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m25s)
00:13:25

[yet is that right No](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m27s)
00:13:27

[so this is really important because this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m29s)
00:13:29

[means like if you train a hundred models](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m32s)
00:13:32

[right each time the validation set](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m35s)
00:13:35

[accuracy is like the meaning of a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m38s)
00:13:38

[distribution and so therefore the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m40s)
00:13:40

[standard deviation of that validation](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m43s)
00:13:43

[set accuracy it can be calculated with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m45s)
00:13:45

[the standard error and this is equal to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m48s)
00:13:48

[the standard deviation divided by square](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m50s)
00:13:50

[root n all right so this tells you so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h13m54s)
00:13:54

[like one approach to figuring out like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m01s)
00:14:01

[is my validation set big enough is train](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m02s)
00:14:02

[your model five times with exactly the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m05s)
00:14:05

[same hyper parameters each time and look](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m08s)
00:14:08

[at the validation set accuracy each time](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m10s)
00:14:10

[and give you know there's like a mean](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m13s)
00:14:13

[and a standard deviation of five numbers](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m15s)
00:14:15

[you could use or a maximum and a minimum](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m17s)
00:14:17

[you can choose but to save yourself some](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m18s)
00:14:18

[time you can figure out straight away](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m21s)
00:14:21

[that like okay well I I have a point](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m23s)
00:14:23

[nine nine accuracy as to you know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m29s)
00:14:29

[whether I get the cat correct or not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m33s)
00:14:33

[correct](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m35s)
00:14:35

[so therefore the standard deviation is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m36s)
00:14:36

[equal to 0.99 times 0.01 okay and then I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m39s)
00:14:39

[can get the standard error of that right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m44s)
00:14:44

[so so basically the size of the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m50s)
00:14:50

[validation set you need](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m52s)
00:14:52

[it's like however big it has to be such](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m54s)
00:14:54

[that your insights about](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h14m58s)
00:14:58

[accuracy good enough for your particular](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m01s)
00:15:01

[business problem and so like I say like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m03s)
00:15:03

[the simple way to do it is to pick a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m06s)
00:15:06

[validation set of like a size of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m09s)
00:15:09

[thousand trained five models and see how](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m10s)
00:15:10

[much the validation set accuracy varies](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m14s)
00:15:14

[and if it's like if they're if it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m16s)
00:15:16

[they're all close enough for what you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m17s)
00:15:17

[need then you're fine if it's not maybe](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m20s)
00:15:20

[you should make it bigger or maybe you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m23s)
00:15:23

[should consider using cross-validation](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m25s)
00:15:25

[instead okay so like as you can see it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m29s)
00:15:29

[really depends on what it is you're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m34s)
00:15:34

[trying to do how common you're less](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m36s)
00:15:36

[common class is and how accurate your](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m40s)
00:15:40

[model is could you pass that back to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m42s)
00:15:42

[Melissa please thank you I have a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m44s)
00:15:44

[question about the less common classes](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m48s)
00:15:48

[if you have less than 22 let's say you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m50s)
00:15:50

[have one sample of something let's say](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m53s)
00:15:53

[it's a face and I only have one](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m57s)
00:15:57

[representation from that particular](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h15m58s)
00:15:58

[country do I toss that into the training](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m01s)
00:16:01

[set and it adds variety to I pull it out](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m04s)
00:16:04

[completely out of the data set or do I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m06s)
00:16:06

[put it in a test set instead of the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m11s)
00:16:11

[validation set so he certainly couldn't](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m15s)
00:16:15

[put it in the test of the validation set](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m17s)
00:16:17

[because you're asking kind of I mean in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m19s)
00:16:19

[general because you're asking can I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m21s)
00:16:21

[recognize something I've never seen](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m22s)
00:16:22

[before but actually this this question](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m24s)
00:16:24

[of like can I recognize something I've](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m27s)
00:16:27

[not seen before there's actually a whole](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m29s)
00:16:29

[class of models specifically for that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m30s)
00:16:30

[purpose it's called either one-shot](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m32s)
00:16:32

[learning which is you get to see](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m34s)
00:16:34

[something once and you have to recognize](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m36s)
00:16:36

[it again or zero shot learning which is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m37s)
00:16:37

[where you have to recognize something](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m40s)
00:16:40

[you've never seen before we're not going](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m41s)
00:16:41

[to cover them in this course but they](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m42s)
00:16:42

[can be useful for things like face](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m47s)
00:16:47

[recognition you know like is this the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m50s)
00:16:50

[same person I've seen before and so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m52s)
00:16:52

[generally speaking obviously for](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m55s)
00:16:55

[something like that to work it's not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m57s)
00:16:57

[that you've never seen a face before](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h16m58s)
00:16:58

[it's that you've never seen Melissa's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m00s)
00:17:00

[face before you know and so you see](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m03s)
00:17:03

[Melissa's face once and you have to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m04s)
00:17:04

[recognize it again](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m06s)
00:17:06

[yeah so in general you know your](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m10s)
00:17:10

[validation set and test set need to have](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m11s)
00:17:11

[the same mix or frequency observations](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m14s)
00:17:14

[that you're going to see in production](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m19s)
00:17:19

[in the real world and then your training](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m21s)
00:17:21

[set should have an equal number in each](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m24s)
00:17:24

[class and if you don't just replicate](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m29s)
00:17:29

[the less common one until it is equal so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m33s)
00:17:33

[this is I think we've mentioned this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m38s)
00:17:38

[paper before a very recent paper that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m39s)
00:17:39

[came out they tried lots of different](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m40s)
00:17:40

[approaches to training with unbalanced](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m42s)
00:17:42

[datasets and found consistently that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m44s)
00:17:44

[over sampling the less common class](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m46s)
00:17:46

[until that is the same size as the more](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m49s)
00:17:49

[common class is always the right thing](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m51s)
00:17:51

[to do so you could literally copy you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m54s)
00:17:54

[know so like I've only got a thousand](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h17m58s)
00:17:58

[you know ten examples of people with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m00s)
00:18:00

[cancer and 100 without so I could just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m02s)
00:18:02

[copy those 10 and other you know 90](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m04s)
00:18:04

[times that's kind of a little memory and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m07s)
00:18:07

[efficient so a lot of things including I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m11s)
00:18:11

[think SK learns random forests have a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m14s)
00:18:14

[class weights parameter that says each](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m16s)
00:18:16

[time your boot strapping or resampling I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m18s)
00:18:18

[want you to sample the less common class](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m20s)
00:18:20

[with a higher probability or did or if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m23s)
00:18:23

[you do and doing deep learning you know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m26s)
00:18:26

[make sure in your mini batch it's not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m28s)
00:18:28

[randomly sampled but it's a stratified](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m29s)
00:18:29

[sample so the less common class is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m32s)
00:18:32

[picked more often okay okay so let's get](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m34s)
00:18:34

[back to finishing off our random forests](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m40s)
00:18:40

[and so what we're going to do today is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m43s)
00:18:43

[we're going to finish off writing our](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m45s)
00:18:45

[random forests and then after day you're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m47s)
00:18:47

[after today your homework will be to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m49s)
00:18:49

[take this class and to add to it all of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m51s)
00:18:51

[the random forest interpretation](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m56s)
00:18:56

[algorithms that we've learned ok so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h18m58s)
00:18:58

[obviously to be able to do that you're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m00s)
00:19:00

[going to need to totally understand how](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m02s)
00:19:02

[this class works so please you know ask](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m04s)
00:19:04

[lots of questions](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m07s)
00:19:07

[as necessary as we go along so just to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m08s)
00:19:08

[remind you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m12s)
00:19:12

[we're doing the the bulldozers tackle](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m16s)
00:19:16

[competition data set again we split it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m19s)
00:19:19

[as before into 12,000 validation the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m22s)
00:19:22

[last 12,000 records and then just to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m24s)
00:19:24

[make it easier for us to keep track of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m28s)
00:19:28

[what we're doing we're going to just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m30s)
00:19:30

[pick two columns out to start with year](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m31s)
00:19:31

[made and Machine hours on the meter okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m34s)
00:19:34

[and so what we did last time was we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m36s)
00:19:36

[started out by creating a tree ensemble](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m39s)
00:19:39

[and the tree ensemble had a bunch of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m42s)
00:19:42

[trees which was literally a list of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m45s)
00:19:45

[entries trees where each time we just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m48s)
00:19:48

[called create tree and create tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m52s)
00:19:52

[contained a sample size number of random](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h19m57s)
00:19:57

[indexes okay this one is drawn without](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m02s)
00:20:02

[replacement](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m06s)
00:20:06

[so remember bootstrapping means sampling](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m07s)
00:20:07

[with replacement so normally with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m11s)
00:20:11

[scikit-learn if you've got n rows we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m13s)
00:20:13

[grab n rows with replacement which means](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m17s)
00:20:17

[many of them will appear more than once](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m21s)
00:20:21

[so each time we get a different sample](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m23s)
00:20:23

[but it's always the same size as the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m26s)
00:20:26

[original data set and then we have our](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m28s)
00:20:28

[set our F samples a function that we can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m31s)
00:20:31

[use which does with replacement sampling](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m34s)
00:20:34

[of less than n rows this is doing](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m38s)
00:20:38

[something again which is its sampling](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m41s)
00:20:41

[without replacement sample size rows](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m44s)
00:20:44

[okay because we're permuting the numbers](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m47s)
00:20:47

[from naught to self dot y -1 and then](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m50s)
00:20:50

[grabbing the first self dot sample size](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m53s)
00:20:53

[of them actually there's a faster way to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m55s)
00:20:55

[do this you can just use NPR and embrace](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h20m57s)
00:20:57

[which is a slightly more direct way but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m00s)
00:21:00

[this way it works as well alright so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m02s)
00:21:02

[this is our random sample for this one](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m05s)
00:21:05

[of our entries trees add so then we're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m08s)
00:21:08

[going to create a decision tree and our](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m13s)
00:21:13

[decision tree we don't pass it all of X](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m15s)
00:21:15

[we pass it these specific indexes and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m18s)
00:21:18

[remember X is a panda's data frame so if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m21s)
00:21:21

[we want to index into it with a bunch of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m25s)
00:21:25

[integers we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m27s)
00:21:27

[to use iLok integer locations and that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m28s)
00:21:28

[makes it behave indexing wise just like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m32s)
00:21:32

[numpy now why vector is numpy so we can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m35s)
00:21:35

[just index into it directly and then](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m40s)
00:21:40

[we're going to keep track about minimum](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m43s)
00:21:43

[of each size and so then the only other](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m44s)
00:21:44

[thing we really need an ensemble is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m49s)
00:21:49

[somewhere to make a prediction and so we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m50s)
00:21:50

[were just going to do the mean of the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m52s)
00:21:52

[tree prediction for each tree all right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m55s)
00:21:55

[so that was that and so then in order to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h21m59s)
00:21:59

[be able to run that we need a decision](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m02s)
00:22:02

[tree class because it's being called](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m05s)
00:22:05

[here and so there we go okay so that's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m08s)
00:22:08

[the starting point so the next thing we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m13s)
00:22:13

[need to do is to flesh out our decision](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m18s)
00:22:18

[tree so the important thing to remember](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m21s)
00:22:21

[is all of our randomness happened back](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m23s)
00:22:23

[here in the tree ensemble the decision](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m27s)
00:22:27

[tree class we're going to create doesn't](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m30s)
00:22:30

[have randomness in it okay so all right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m33s)
00:22:33

[now we are building a random B regressor](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m37s)
00:22:37

[right so that's why we're taking the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m40s)
00:22:40

[mean of the tree the outputs if we were](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m42s)
00:22:42

[to work with classification do we take](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m46s)
00:22:46

[the max like the classifier will give](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m48s)
00:22:48

[you either zeros or ones no I would](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m51s)
00:22:51

[still take the mean so the so each tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m54s)
00:22:54

[is going to tell you what percentage of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h22m57s)
00:22:57

[that leaf node contains cats and what](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m00s)
00:23:00

[percentage to take contains dogs so then](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m03s)
00:23:03

[I would average all those percentages](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m06s)
00:23:06

[and say across the trees on average](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m07s)
00:23:07

[there is 19% cats and 81 percent dogs](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m10s)
00:23:10

[good question so you know random tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m16s)
00:23:16

[classifiers are almost identical or can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m21s)
00:23:21

[be almost identical the random tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m25s)
00:23:25

[regresses the technique we're going to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m26s)
00:23:26

[use to build this today will basically](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m30s)
00:23:30

[exactly work for a classification it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m32s)
00:23:32

[certainly for binary classification you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m34s)
00:23:34

[can do with exactly the same code for](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m36s)
00:23:36

[multi-class classification you just need](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m38s)
00:23:38

[to change your data structure but so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m40s)
00:23:40

[that like you have like a one hot](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m43s)
00:23:43

[encoded matrix or a list of integers](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m45s)
00:23:45

[that you treat as a one hot encoded](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m49s)
00:23:49

[matrix okay so our decision tree so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m51s)
00:23:51

[remember our idea here is that we're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h23m59s)
00:23:59

[going to like try to avoid thinking so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m01s)
00:24:01

[we're going to basically write it as if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m03s)
00:24:03

[everything we need already exists okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m06s)
00:24:06

[so we know from when we created the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m08s)
00:24:08

[decision tree we're kind of pass in the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m11s)
00:24:11

[X the Y and the minimum leaf size so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m13s)
00:24:13

[here we need to make sure we've got the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m17s)
00:24:17

[X and the y and the minimum left sides](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m18s)
00:24:18

[okay so then there's one other thing](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m21s)
00:24:21

[which is as we split our tree into sub](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m24s)
00:24:24

[trees we're going to need to keep track](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m28s)
00:24:28

[of which of the row indexes went into](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m30s)
00:24:30

[the left-hand side of the tree which](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m34s)
00:24:34

[went into the right-hand side of the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m36s)
00:24:36

[tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m37s)
00:24:37

[okay so we're going to have this thing](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m37s)
00:24:37

[called indexes as well right so at first](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m39s)
00:24:39

[we just didn't bother passing and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m44s)
00:24:44

[indexes at all so if indexes is not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m46s)
00:24:46

[passed in if it's none then we're just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m47s)
00:24:47

[going to set it to everything the entire](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m50s)
00:24:50

[length of Y right so NP dot a range is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m53s)
00:24:53

[the same as just range in Python but it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m56s)
00:24:56

[returns an umpire rate right so that the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h24m59s)
00:24:59

[root of a decision tree contains all the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m02s)
00:25:02

[roads that's the definition really of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m06s)
00:25:06

[the root of a decision tree so all the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m08s)
00:25:08

[rows is Rho naught Rho 1 Rho 2 etc up to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m10s)
00:25:10

[row y -1 okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m13s)
00:25:13

[is going to store away all that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m18s)
00:25:18

[information that we were given we're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m20s)
00:25:20

[going to keep track of how many rows are](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m22s)
00:25:22

[there and how many columns are there](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m25s)
00:25:25

[okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m27s)
00:25:27

[so then the every leaf and every node in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m28s)
00:25:28

[a tree has a value it has a prediction](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m33s)
00:25:33

[that prediction is just equal to the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m37s)
00:25:37

[average of the dependent variable okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m39s)
00:25:39

[so every node in the tree Y indexed with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m43s)
00:25:43

[the indexes is the values of the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m49s)
00:25:49

[dependent variable that are in this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m53s)
00:25:53

[branch of the tree and so here is the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m54s)
00:25:54

[main some nodes in a tree also have a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h25m57s)
00:25:57

[score which is like how effective was](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m04s)
00:26:04

[the split here right but that's only](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m07s)
00:26:07

[going to be true if it's not a leaf node](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m11s)
00:26:11

[right a leaf node has no further splits](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m13s)
00:26:13

[and at this point when we create a tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m15s)
00:26:15

[we haven't done any splits yet so it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m18s)
00:26:18

[score starts out as being infinity okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m20s)
00:26:20

[so having built that the root of the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m23s)
00:26:23

[tree our next job is to find out which](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m27s)
00:26:27

[variable should we split on and what](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m30s)
00:26:30

[level of that variable should we split](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m33s)
00:26:33

[on so let's pretend that there's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m35s)
00:26:35

[something that does them find bass bit](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m37s)
00:26:37

[so then we're done okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m41s)
00:26:41

[so how do we find a variable to split on](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m44s)
00:26:44

[so well we could just go through each](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m52s)
00:26:52

[potential variable so C contains the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m55s)
00:26:55

[number of columns we have so go through](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h26m58s)
00:26:58

[each one and see if we can find a better](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m00s)
00:27:00

[split than we have so far on that column](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m03s)
00:27:03

[okay now notice this is like not the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m07s)
00:27:07

[full random forest definition this is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m14s)
00:27:14

[assuming that max features they're set](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m16s)
00:27:16

[to all right remember we could set max](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m19s)
00:27:19

[features too like 0.5 in which case we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m21s)
00:27:21

[wouldn't check all the numbers should](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m23s)
00:27:23

[not to see we would check half the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m25s)
00:27:25

[numbers at random from not to see so if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m27s)
00:27:27

[you want to turn this into like a random](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m29s)
00:27:29

[forest that has the max features support](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m32s)
00:27:32

[we could easily like add one line of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m35s)
00:27:35

[code to do that but we're not going to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m38s)
00:27:38

[do it in our implementation today so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m40s)
00:27:40

[then we just need to find better split](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m45s)
00:27:45

[and since we're not interested in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m47s)
00:27:47

[thinking at the moment for now we're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m49s)
00:27:49

[just going to leave that empty alright](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m50s)
00:27:50

[so there one other thing I like to do](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m52s)
00:27:52

[with my kind of word start writing a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h27m58s)
00:27:58

[class is I'd like to have some way to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m00s)
00:28:00

[print out what's in that class all right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m02s)
00:28:02

[and so if you type print followed by an](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m04s)
00:28:04

[object or if it Jupiter notebook you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m07s)
00:28:07

[just type the name of the object at the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m09s)
00:28:09

[moment it's just printing out underscore](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m13s)
00:28:13

[underscore main underscore underscore](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m15s)
00:28:15

[got decision tree at blah blah blah](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m17s)
00:28:17

[which is not very helpful right so if we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m19s)
00:28:19

[want to replace this with something](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m22s)
00:28:22

[helpful we have to define the special](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m23s)
00:28:23

[Python method named dan direct crack to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m26s)
00:28:26

[get a representation of this object so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m31s)
00:28:31

[when we type when we see please just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m34s)
00:28:34

[write the name like this behind the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m36s)
00:28:36

[scenes that calls that function and the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m39s)
00:28:39

[default implementation of that method is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m41s)
00:28:41

[just to print out this unhelpful stuff](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m44s)
00:28:44

[so we can replace it by instead saying](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m47s)
00:28:47

[let's create a format string where we're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m50s)
00:28:50

[going to print out N and then show N and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m53s)
00:28:53

[then print vowel and then show Val okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m56s)
00:28:56

[so how many how many rows are in this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h28m58s)
00:28:58

[node and what's the average of the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m01s)
00:29:01

[dependent variable](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m04s)
00:29:04

[okay then if it's not a leaf node so if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m05s)
00:29:05

[it has a split then we should also be](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m10s)
00:29:10

[able to print out the score the value we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m12s)
00:29:12

[split out and the variable that we split](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m16s)
00:29:16

[on now you'll notice here self dot is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m18s)
00:29:18

[leaf is leaf is defined as a method but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m23s)
00:29:23

[I don't have any parentheses after it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m26s)
00:29:26

[this is a special kind of method code of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m28s)
00:29:28

[property and so a property is something](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m31s)
00:29:31

[that kind of looks like a regular](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m34s)
00:29:34

[variable but it's actually calculated on](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m36s)
00:29:36

[the fly so when I call is leaf it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m40s)
00:29:40

[actually calls this function right but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m43s)
00:29:43

[I've got this special decorator property](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m46s)
00:29:46

[okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m49s)
00:29:49

[and what this says is basically you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m50s)
00:29:50

[don't have to include the parentheses](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m52s)
00:29:52

[when you call it okay and so it's going](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m53s)
00:29:53

[to say all right is this a leaf or not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h29m58s)
00:29:58

[so a leaf is something that we don't](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m00s)
00:30:00

[spit on if we haven't split on it then](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m02s)
00:30:02

[it's score is still set to infinity so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m05s)
00:30:05

[that's my logic that makes sense](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m08s)
00:30:08

[so this uh this at notation is called a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m12s)
00:30:12

[decorator it's basically a way of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m17s)
00:30:17

[telling Python more information about](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m19s)
00:30:19

[your method does anybody here remember](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m22s)
00:30:22

[where you have seen decorators before](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m25s)
00:30:25

[we pass it over you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m30s)
00:30:30

[yeah where have you seen that where have](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m32s)
00:30:32

[you seen decorators tell us more about](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m34s)
00:30:34

[flask and Wow](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m36s)
00:30:36

[yeah what is that - that no words](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m39s)
00:30:39

[so flasks so anybody who's done any web](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m47s)
00:30:47

[programming before with something like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m50s)
00:30:50

[flask or a similar framework would have](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m52s)
00:30:52

[had to have said like this method is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m55s)
00:30:55

[going to respond to this bit of the URL](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h30m57s)
00:30:57

[and either to post or to get and you put](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m00s)
00:31:00

[it in a special decorator so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m02s)
00:31:02

[behind-the-scenes that's telling Python](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m07s)
00:31:07

[to treat this method in a special way so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m10s)
00:31:10

[here's another decorator okay and so you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m13s)
00:31:13

[know if you get more advanced with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m16s)
00:31:16

[Python you can actually learn how to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m18s)
00:31:18

[write your own decorators which as was](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m19s)
00:31:19

[mentioned you know basically insert some](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m21s)
00:31:21

[additional code but for now just know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m23s)
00:31:23

[there's a bunch of predefined decorators](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m25s)
00:31:25

[we can use to change how our methods](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m28s)
00:31:28

[behave and one of them is a property](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m31s)
00:31:31

[which basically means you don't have to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m33s)
00:31:33

[put parentheses anymore which of course](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m35s)
00:31:35

[means you can't add any more parameters](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m37s)
00:31:37

[beyond self.y if it's not belief why is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m39s)
00:31:39

[this for infinity because infinity mean](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m46s)
00:31:46

[you're at the root why no infinity means](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m49s)
00:31:49

[that you're not at the root it means](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m53s)
00:31:53

[you're at a leaf so the root will have a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m55s)
00:31:55

[split assuming we find one but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h31m57s)
00:31:57

[everything will have a split till we get](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m00s)
00:32:00

[all the way to the bottom and leaf and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m01s)
00:32:01

[so the leaves will have a score of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m04s)
00:32:04

[infinity because they won't split great](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m06s)
00:32:06

[all right so that's our decision tree it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m10s)
00:32:10

[doesn't do very much but at least we can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m16s)
00:32:16

[like create an ensemble right ten trees](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m18s)
00:32:18

[sample size a thousand right and we can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m20s)
00:32:20

[make print out so now when I go M trees](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m23s)
00:32:23

[zero](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m25s)
00:32:25

[it doesn't say blah blah blah blah blah](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m26s)
00:32:26

[it says what we asked it to say n called](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m28s)
00:32:28

[the thousand now : 10.8 oh wait okay and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m31s)
00:32:31

[this is the leaf because we haven't spit](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m36s)
00:32:36

[on it yet so we've got nothing more to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m39s)
00:32:39

[say](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m41s)
00:32:41

[okay so then the indexes are all the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m43s)
00:32:43

[numbers from nought to a thousand okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m47s)
00:32:47

[because the base of the tree has](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m50s)
00:32:50

[everything this is like everything in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m51s)
00:32:51

[the random sample that was passed to it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m54s)
00:32:54

[because remember by the time we get to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m57s)
00:32:57

[the point where it's a decision tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m58s)
00:32:58

[where we don't have to worry about any](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h32m59s)
00:32:59

[of the randomness in the random forest](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m02s)
00:33:02

[anymore okay all right so let's try to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m03s)
00:33:03

[write the thing which finds a split okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m11s)
00:33:11

[so we need to implement find better](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m15s)
00:33:15

[split okay and so it's going to take the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m19s)
00:33:19

[index of a variable variable number one](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m22s)
00:33:22

[variable number three whatever and it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m25s)
00:33:25

[going to figure out what's the best blit](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m27s)
00:33:27

[point is that better than any split we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m30s)
00:33:30

[have so far and for the first variable](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m33s)
00:33:33

[the answer will always be yes because](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m35s)
00:33:35

[the best one so far is none at all which](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m37s)
00:33:37

[is infinity bad okay so let's start by](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m39s)
00:33:39

[making sure we've got something to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m44s)
00:33:44

[compare to so the thing we're going to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m45s)
00:33:45

[compare two will be scikit-learn x'](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m46s)
00:33:46

[random forest and so we need to make](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m49s)
00:33:49

[sure that psychic learns random forest](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m52s)
00:33:52

[gets exactly the same data that we have](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m54s)
00:33:54

[so we start out by creating ensemble](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m56s)
00:33:56

[grab a tree out of it and then find out](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h33m58s)
00:33:58

[which particular random sample of x and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m01s)
00:34:01

[y did this tree use okay and we're going](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m04s)
00:34:04

[to store them away so that we can pass](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m07s)
00:34:07

[them to scikit-learn so we have exactly](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m09s)
00:34:09

[the same information so let's go ahead](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m11s)
00:34:11

[and now create a random forest using](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m15s)
00:34:15

[scikit-learn](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m17s)
00:34:17

[so one tree one decision](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m17s)
00:34:17

[no bootstrapping so the whole the whole](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m21s)
00:34:21

[data set that's oh this should be](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m24s)
00:34:24

[exactly the same as the thing that we're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m27s)
00:34:27

[going to create this tree okay so let's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m29s)
00:34:29

[try so we need to define find better](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m33s)
00:34:33

[split okay so fine better split takes a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m38s)
00:34:38

[variable okay so let's define our x](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m42s)
00:34:42

[independent variables and say okay well](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m47s)
00:34:47

[it's everything inside our tree but only](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m49s)
00:34:49

[those indexes that are](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m53s)
00:34:53

[in this node right which at the top of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m55s)
00:34:55

[the tree is everything all right and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h34m58s)
00:34:58

[just this one variable okay and then for](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m00s)
00:35:00

[our Y's it's just whatever a dependent](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m05s)
00:35:05

[variable is at the indexes in this node](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m08s)
00:35:08

[okay so there's our X&amp;Y so let's now go](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m10s)
00:35:10

[through every single value in our](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m15s)
00:35:15

[independent variable and so I'll show](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m19s)
00:35:19

[you what's going to happen so let's say](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m23s)
00:35:23

[our independent variable is um ade](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m25s)
00:35:25

[and not going to be an order right and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m31s)
00:35:31

[so we're going to go to the very first](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m42s)
00:35:42

[row and we're going to say okay yeah](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m44s)
00:35:44

[mate here is three right and so what I'm](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m46s)
00:35:46

[going to do is I'm going to try and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m49s)
00:35:49

[calculate the score if we decided to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m51s)
00:35:51

[branch on the number three alright so I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m55s)
00:35:55

[need to know which rows are greater than](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h35m58s)
00:35:58

[three which rows are less than equal to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m01s)
00:36:01

[three and they're going to become my](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m04s)
00:36:04

[left-hand side my right hand side but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m06s)
00:36:06

[and then we need a score right so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m07s)
00:36:07

[there's lots of schools we could use so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m10s)
00:36:10

[in random forests we call this the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m13s)
00:36:13

[information gain right the information](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m15s)
00:36:15

[gain is like how much better does our](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m17s)
00:36:17

[score get because we split it into these](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m19s)
00:36:19

[two groups of data there's lots of ways](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m21s)
00:36:21

[we could calculate it Jinni](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m23s)
00:36:23

[cross-entropy root mean squared error](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m24s)
00:36:24

[whatever if you think about it there is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m27s)
00:36:27

[an alternative formulation of root mean](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m31s)
00:36:31

[squared error which is mathematically](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m33s)
00:36:33

[the same to within a constant scale but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m35s)
00:36:35

[it's a little bit easier to deal with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m38s)
00:36:38

[which is we're gonna try and find a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m40s)
00:36:40

[split which the causes the two groups to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m42s)
00:36:42

[each have as lower standard deviation as](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m46s)
00:36:46

[possible right so like I want to find a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m49s)
00:36:49

[spirit that puts all the cats over here](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m51s)
00:36:51

[and all the dogs over here right so if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m53s)
00:36:53

[these are all cats and these are all](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m55s)
00:36:55

[dogs then this has a standard deviation](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m57s)
00:36:57

[of zero and this has a standard](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h36m59s)
00:36:59

[deviation of zero or else this is like a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m01s)
00:37:01

[total around a mix of cats and dogs this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m03s)
00:37:03

[is a totally random mix of cats and dogs](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m05s)
00:37:05

[they're going to have a much higher](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m07s)
00:37:07

[standard deviation](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m09s)
00:37:09

[make sense and so it turns out if you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m11s)
00:37:11

[find a split that minimizes those group](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m13s)
00:37:13

[standard deviations or specifically the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m15s)
00:37:15

[weighted average of the true standard](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m18s)
00:37:18

[deviations it's mathematically the same](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m20s)
00:37:20

[as minimizing the root mean square error](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m22s)
00:37:22

[that's something you can prove to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m24s)
00:37:24

[yourself after class if you want to okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m26s)
00:37:26

[so we're going to need to find first of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m29s)
00:37:29

[all split this into two groups so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m32s)
00:37:32

[where's all the stuff that is greater](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m33s)
00:37:33

[than three so greater than three is this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m36s)
00:37:36

[one this one and this one so we need the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m38s)
00:37:38

[standard deviation of that so let's go](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m40s)
00:37:40

[ahead and say standard deviation of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m43s)
00:37:43

[greater than three that one that one and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m46s)
00:37:46

[that one okay and then the next will be](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m51s)
00:37:51

[the standard deviation of less than or](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h37m56s)
00:37:56

[equal to three so that would be that one](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m00s)
00:38:00

[that one that one and then we just take](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m03s)
00:38:03

[the weighted average of those two and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m08s)
00:38:08

[that's our score that would be our score](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m09s)
00:38:09

[if we split on three that make sense and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m12s)
00:38:12

[so then the next step would be try to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m17s)
00:38:17

[spit on four try spitting on one try](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m19s)
00:38:19

[spitting on six redundantly try](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m22s)
00:38:22

[splitting on four again redundantly try](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m25s)
00:38:25

[spitting on one again and find out which](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m28s)
00:38:28

[one works best so that's our code here](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m30s)
00:38:30

[is we're going to go through every row](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m33s)
00:38:33

[and so let's say okay left hand side is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m34s)
00:38:34

[any values in X that are less than or](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m38s)
00:38:38

[equal to this particular value our right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m42s)
00:38:42

[hand side is every value in X that are](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m46s)
00:38:46

[greater than this particular value](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m49s)
00:38:49

[okay so what's the data type that's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h38m57s)
00:38:57

[going to be in LHS and RHS what are they](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m01s)
00:39:01

[actually going to contain](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m04s)
00:39:04

[they're going to be arrays arrays of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m09s)
00:39:09

[what](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m11s)
00:39:11

[rays of erosive audience yeah which we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m13s)
00:39:13

[can treat a zero and one okay so LHS](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m16s)
00:39:16

[will be an array of false every time](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m18s)
00:39:18

[it's not less than or equal to and true](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m21s)
00:39:21

[otherwise and RHS will be a boolean](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m24s)
00:39:24

[array of the opposite okay and now we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m26s)
00:39:26

[can't take a standard deviation of an](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m29s)
00:39:29

[empty set right so if there's nothing](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m31s)
00:39:31

[that's greater than this number then](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m34s)
00:39:34

[these will all be false which means the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m37s)
00:39:37

[sum will be zero okay and in that case](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m40s)
00:39:40

[let's not go any further with this step](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m43s)
00:39:43

[because there's nothing to take the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m45s)
00:39:45

[standard deviation of and it's obviously](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m47s)
00:39:47

[not a useful split okay so assuming](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m49s)
00:39:49

[we've got this far we can now calculate](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m51s)
00:39:51

[the standard deviation of the left-hand](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m53s)
00:39:53

[side and of the right-hand side and take](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m55s)
00:39:55

[the weighted average or the sums the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h39m59s)
00:39:59

[same thing to us to a scaler right and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m02s)
00:40:02

[so there's a score and so we can then](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m05s)
00:40:05

[check is this better than our best score](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m07s)
00:40:07

[so far and our best score so far we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m09s)
00:40:09

[initially initialized it to infinity](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m12s)
00:40:12

[right so initially this is this is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m14s)
00:40:14

[better so if it's better let's store](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m16s)
00:40:16

[away](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m20s)
00:40:20

[well as the information we need which](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m23s)
00:40:23

[variable has found this better split](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m25s)
00:40:25

[what was the score we found and what was](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m26s)
00:40:26

[the value that we spit on okay so there](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m30s)
00:40:30

[it is so if we run that and I'm using](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m35s)
00:40:35

[time it so what time it does is that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m41s)
00:40:41

[sees how long this command takes to run](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m43s)
00:40:43

[and it tries to give you a kind of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m46s)
00:40:46

[statistically valid measure of that so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m48s)
00:40:48

[you can see here it's run run at ten](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m50s)
00:40:50

[times to get an average and then it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m52s)
00:40:52

[done that seven times to get a mean and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m55s)
00:40:55

[standard deviation across runs and so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h40m58s)
00:40:58

[it's taking me 75 milliseconds plus or](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m00s)
00:41:00

[minus ten okay so let's check that this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m02s)
00:41:02

[works find bladder split tree zero so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m06s)
00:41:06

[zero is year made one is machine hours](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m11s)
00:41:11

[current meter so I with one we got back](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m13s)
00:41:13

[machine hours current meter thirty seven](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m20s)
00:41:20

[four four with this score and then we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m22s)
00:41:22

[ran it again with zero that's year made](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m24s)
00:41:24

[and we've got a better score 658 and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m27s)
00:41:27

[split 1974 and so 1974 let's compare](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m30s)
00:41:30

[yeah that was what this treated as well](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m35s)
00:41:35

[okay so we've got we've confirmed that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m37s)
00:41:37

[this method is doing is giving the same](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m40s)
00:41:40

[result that as K loans random forests](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m43s)
00:41:43

[did okay and you can also see here the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m46s)
00:41:46

[value 10 point oh eight and again](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m48s)
00:41:48

[matching here the value ten point oh](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m52s)
00:41:52

[eight okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m54s)
00:41:54

[so we've got something that can find](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m56s)
00:41:56

[once bit could you pass that to your net](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h41m58s)
00:41:58

[please](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m01s)
00:42:01

[so Jeremy why don't we put a unique on](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m02s)
00:42:02

[the eggs there because I'm not trying to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m05s)
00:42:05

[optimize the performance yet but do you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m11s)
00:42:11

[see that no like he is doing more yeah](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m13s)
00:42:13

[so it's like and you can see in the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m16s)
00:42:16

[excel I like checked this one twice I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m17s)
00:42:17

[check this four twice unnecessarily yeah](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m19s)
00:42:19

[okay so and so you're not already](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m24s)
00:42:24

[thinking about performance which is good](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m29s)
00:42:29

[so tell me what is the computational](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m32s)
00:42:32

[complexity of this section of the code](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m35s)
00:42:35

[and and like ever think about it but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m40s)
00:42:40

[also like feel free to talk us through](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m43s)
00:42:43

[it if you want to kind of think and talk](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m45s)
00:42:45

[at the same time what's the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m48s)
00:42:48

[computational complexity of this piece](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m50s)
00:42:50

[of code](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m52s)
00:42:52

[can I pass it over there yes all right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h42m57s)
00:42:57

[Jay take us through your thought process](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m02s)
00:43:02

[I think you have to take each different](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m04s)
00:43:04

[values through the column to calculate](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m08s)
00:43:08

[it once to see those splits so and then](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m10s)
00:43:10

[compare](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m14s)
00:43:14

[oh the cup like all the possible](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m15s)
00:43:15

[combinations between these different](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m18s)
00:43:18

[values so that can be expensive like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m20s)
00:43:20

[this yours](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m22s)
00:43:22

[huh can you do somebody else would have](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m23s)
00:43:23

[tell us the actual computational](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m25s)
00:43:25

[complexity so like yeah quite high](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m27s)
00:43:27

[Jayde's thinking how high](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m29s)
00:43:29

[I think it's great okay so tell me why](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m33s)
00:43:33

[is it N squared Oh because for the full](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m37s)
00:43:37

[loop it is in yes and I think I guess](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m40s)
00:43:40

[the standard deviation well ticket in so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m43s)
00:43:43

[it's in square okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m45s)
00:43:45

[or um this one maybe is even is yet to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m46s)
00:43:46

[know like this is like which ones are](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m49s)
00:43:49

[less than X I I'm gonna have to check](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m51s)
00:43:51

[every value to see if it's less than X I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m53s)
00:43:53

[okay and so so it's useful to know like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m55s)
00:43:55

[how do I quickly calculate computational](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h43m59s)
00:43:59

[complexity I can guarantee most of the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m01s)
00:44:01

[interviews you do are going to ask you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m03s)
00:44:03

[to calculate computational complexity on](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m05s)
00:44:05

[the fly and it's also like when you're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m07s)
00:44:07

[coding you want it to be second nature](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m08s)
00:44:08

[so the technique is basically is there a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m10s)
00:44:10

[loop okay with then we're obviously](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m13s)
00:44:13

[doing this end times](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m16s)
00:44:16

[okay so there's an N involved it's there](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m17s)
00:44:17

[a loop inside the loop if there is then](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m20s)
00:44:20

[you need to multiply those two together](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m22s)
00:44:22

[in this case there's not is there](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m23s)
00:44:23

[anything inside the loop that's not a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m26s)
00:44:26

[constant time thing so you might see a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m28s)
00:44:28

[sort in there and you just need to know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m31s)
00:44:31

[that sort is n log n like that should be](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m33s)
00:44:33

[second nature if you see a matrix](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m35s)
00:44:35

[multiply you need to know what that is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m37s)
00:44:37

[in this case there are some things that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m39s)
00:44:39

[are doing element wise array operations](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m42s)
00:44:42

[right so keep an eye out for anything](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m44s)
00:44:44

[where lump I is doing something to every](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m46s)
00:44:46

[value of an array in this case is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m48s)
00:44:48

[checking every value of x against a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m50s)
00:44:50

[constant so it's going to have to do](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m52s)
00:44:52

[that n times so to flesh this out into a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m54s)
00:44:54

[computational complexity you just take](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m57s)
00:44:57

[the number of things in the loop and you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h44m59s)
00:44:59

[multiply it by the highest computational](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m02s)
00:45:02

[complexity inside the loop n times n is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m04s)
00:45:04

[N squared and you pass them in this case](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m07s)
00:45:07

[couldn't we just pre sort the list and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m11s)
00:45:11

[then do like 1 + log n computation](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m13s)
00:45:13

[there's lots of things we can do to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m15s)
00:45:15

[speed this up so at this stage is just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m17s)
00:45:17

[like what is the computational](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m18s)
00:45:18

[complexity we have and but absolutely](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m19s)
00:45:19

[it's certainly not as good as it can be](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m22s)
00:45:22

[okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m23s)
00:45:23

[so and that's where we're going to go](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m24s)
00:45:24

[next just like alright N squared is not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m26s)
00:45:26

[is not great so let's try and make it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m29s)
00:45:29

[better](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m31s)
00:45:31

[so here's my attempt at making it better](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m34s)
00:45:34

[and the idea is this ok who wants to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m38s)
00:45:38

[first of all tell me](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m43s)
00:45:43

[what's the equation for standard](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m45s)
00:45:45

[deviation Masha can you grab the pose so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m48s)
00:45:48

[for the standard deviation it's the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m56s)
00:45:56

[difference between the value and its](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h45m59s)
00:45:59

[mean it's we take a square root of that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m00s)
00:46:00

[so that we take the the power of two](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m04s)
00:46:04

[then we sum up all of these situations](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m09s)
00:46:09

[and we take the square root out of all](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m12s)
00:46:12

[this sum yeah you have to fight divided](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m15s)
00:46:15

[by M yep yep great](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m17s)
00:46:17

[good okay now in practice we don't](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m19s)
00:46:19

[normally use that formulation because it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m23s)
00:46:23

[kind of requires us calculating you know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m25s)
00:46:25

[X minus the mean lots of times does](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m28s)
00:46:28

[anybody know the formulation that just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m31s)
00:46:31

[requires X and x squared anybody happen](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m33s)
00:46:33

[to know that one yes at the back can I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m37s)
00:46:37

[pass that back there](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m38s)
00:46:38

[square root of a mean of squares -](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m41s)
00:46:41

[squared off mean yeah great mean of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m45s)
00:46:45

[squares minus the square of the means](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m48s)
00:46:48

[right so that's a really good 1/8 that's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m50s)
00:46:50

[a really good one to know because like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m54s)
00:46:54

[you can now calculate variances or](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h46m56s)
00:46:56

[standard deviations of anything you just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m00s)
00:47:00

[have to first of all grab the column as](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m02s)
00:47:02

[it is the column squared right and as](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m04s)
00:47:04

[long as you've got those stored away](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m07s)
00:47:07

[somewhere you can immediately calculate](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m09s)
00:47:09

[the standard deviation so the reason](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m11s)
00:47:11

[this is handy for us is that if we first](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m14s)
00:47:14

[of all sort our data right let's go](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m17s)
00:47:17

[ahead and sort our data then if you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m23s)
00:47:23

[think about it as we kind of start going](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m26s)
00:47:26

[down one step at a time right then each](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m28s)
00:47:28

[group it's exactly the same as the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m31s)
00:47:31

[previous group on the left hand side](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m33s)
00:47:33

[with one more thing in it and on the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m36s)
00:47:36

[right hand side with one less thing in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m38s)
00:47:38

[it so given that we just have to keep](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m40s)
00:47:40

[track of some of X and some of x squared](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m42s)
00:47:42

[we can just add one more thing to X one](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m44s)
00:47:44

[more thing - x squared on the left and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m47s)
00:47:47

[remove one thing on the right okay so we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m49s)
00:47:49

[don't have to go through the whole lot](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m52s)
00:47:52

[each time and so we can turn this into a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m54s)
00:47:54

[order n algorithm so that's all I do](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h47m57s)
00:47:57

[here is I sort the data right and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m01s)
00:48:01

[they're going to keep track of the count](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m03s)
00:48:03

[of things on the right the sum of things](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m04s)
00:48:04

[on the right and the sum of squares on](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m07s)
00:48:07

[the right and initially everything's on](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m09s)
00:48:09

[the right hand side](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m12s)
00:48:12

[okay so initially n is the count Y sum](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m13s)
00:48:13

[is the sum on the right and Y squared](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m18s)
00:48:18

[sum is the sum of squares on the right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m21s)
00:48:21

[and then nothing is initially on the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m23s)
00:48:23

[left so it's zeros okay and then we just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m25s)
00:48:25

[have to loop through each observation](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m29s)
00:48:29

[right and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m32s)
00:48:32

[add one to the left hand count subtract](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m35s)
00:48:35

[one from the left right hand count add](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m38s)
00:48:38

[the value to the left hand count](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m40s)
00:48:40

[subtract it from the right hand count](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m42s)
00:48:42

[add the value squared to the left hand](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m43s)
00:48:43

[subtract it from the right hand okay now](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m46s)
00:48:46

[we do need to be careful though because](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m50s)
00:48:50

[if we're saying less than or equal to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m52s)
00:48:52

[one say we're not stopping here we're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m55s)
00:48:55

[stopping here like we have to have](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m58s)
00:48:58

[everything in that group so the other](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h48m59s)
00:48:59

[thing I'm going to do is I'm just going](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m01s)
00:49:01

[to make sure that the next value is not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m02s)
00:49:02

[the same as this value if it is I'm](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m06s)
00:49:06

[going to skip over it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m08s)
00:49:08

[right so I'm just going to double check](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m09s)
00:49:09

[that this value and the next one aren't](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m10s)
00:49:10

[the same okay so as long as they're not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m13s)
00:49:13

[the same I can keep going ahead and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m17s)
00:49:17

[calculate my standard deviation now](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m20s)
00:49:20

[passing in the count the sum and the sum](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m21s)
00:49:21

[squared right and there's that formula](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m24s)
00:49:24

[okay the sum is squared divided by the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m28s)
00:49:28

[square of the sum so i minus the square](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m33s)
00:49:33

[of the sum i do that's the right hand](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m36s)
00:49:36

[side and so now we can calculate the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m39s)
00:49:39

[weighted average score just like before](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m41s)
00:49:41

[and all of these lames are now the same](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m43s)
00:49:43

[okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m46s)
00:49:46

[so we've turned our order and square an](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m46s)
00:49:46

[algorithm into an order n algorithm and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m49s)
00:49:49

[in general stuff like this is going to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m52s)
00:49:52

[get you a lot more value than like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m56s)
00:49:56

[pushing something onto a spark cluster](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h49m58s)
00:49:58

[or ordering faster ram or using more](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m00s)
00:50:00

[cores and your cpu or whatever right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m03s)
00:50:03

[this is the way you want to be you know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m06s)
00:50:06

[improving your code and specifically](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m09s)
00:50:09

[write your code right without thinking](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m12s)
00:50:12

[too much about performance run it is it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m16s)
00:50:16

[fast enough for what you need then](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m19s)
00:50:19

[you're done if not profile it right so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m21s)
00:50:21

[in Jupiter instead of seeing percent](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m25s)
00:50:25

[time at you say % p run and it will tell](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m30s)
00:50:30

[you exactly where the time was spent in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m34s)
00:50:34

[your algorithm and then you can go to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m38s)
00:50:38

[the bit that's actually taking the time](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m40s)
00:50:40

[and think about like okay is this this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m42s)
00:50:42

[is algorithmically as efficient as a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m45s)
00:50:45

[can be okay so in this case we run it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m48s)
00:50:48

[and we've gone down from 76 milliseconds](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m52s)
00:50:52

[to less than 2 milliseconds and now some](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h50m57s)
00:50:57

[people that are new to programming think](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m01s)
00:51:01

[like oh great I've saved 60 something](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m03s)
00:51:03

[milliseconds but the point is this is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m06s)
00:51:06

[going to get run like tens of millions](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m09s)
00:51:09

[of clients okay so the 76 millisecond](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m12s)
00:51:12

[version is so slow that it's got to be](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m16s)
00:51:16

[impractical for any random forest you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m18s)
00:51:18

[using in practice right where else the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m21s)
00:51:21

[one millisecond version I found is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m24s)
00:51:24

[actually quite quite acceptable and then](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m25s)
00:51:25

[check the numbers should be exactly the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m30s)
00:51:30

[same as before and oh yeah okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m32s)
00:51:32

[so now that we have a function find](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m34s)
00:51:34

[better split that does what we want I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m39s)
00:51:39

[want to insert it into my decision tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m41s)
00:51:41

[class and this is a really cool Python](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m44s)
00:51:44

[trick Python does everything dynamically](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m46s)
00:51:46

[right so we can actually say the method](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m49s)
00:51:49

[called find better split in decision](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m54s)
00:51:54

[tree is that function I just created and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h51m57s)
00:51:57

[that might sticks it inside that class](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m01s)
00:52:01

[now I'll tell you what's slightly](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m05s)
00:52:05

[confusing about this is that this thing](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m08s)
00:52:08

[this word here and this word here they](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m11s)
00:52:11

[actually have no relationship to each](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m14s)
00:52:14

[other](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m15s)
00:52:15

[they just happen to have the same](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m16s)
00:52:16

[letters in the same order right so like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m17s)
00:52:17

[I could call this find better split](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m19s)
00:52:19

[underscore foo right and then I could](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m22s)
00:52:22

[like call that right and call that right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m26s)
00:52:26

[so now my function is actually called](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m35s)
00:52:35

[fine better split underscore foo but my](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m37s)
00:52:37

[method I'm expecting to call something](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m39s)
00:52:39

[called decision tree dot fine better](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m44s)
00:52:44

[split all right so here I could say](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m47s)
00:52:47

[decision tree dot fine better split](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m49s)
00:52:49

[equals find better split underscore foo](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m51s)
00:52:51

[okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m54s)
00:52:54

[you see that's the same thing okay so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m55s)
00:52:55

[like it's important to understand how](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h52m57s)
00:52:57

[namespaces](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m01s)
00:53:01

[work like in in every language that you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m02s)
00:53:02

[use one of the most important things is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m05s)
00:53:05

[kind of understanding how how it figures](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m07s)
00:53:07

[out what a name refers to so this here](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m09s)
00:53:09

[means find better split as to find](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m13s)
00:53:13

[inside this class right and nowhere else](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m16s)
00:53:16

[right well I mean there's a parent class](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m19s)
00:53:19

[but never mind about that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m22s)
00:53:22

[this one here means find better split](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m23s)
00:53:23

[fou in the global namespace a lot of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m26s)
00:53:26

[languages don't have a global namespace](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m30s)
00:53:30

[that Python does okay and so the two are](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m31s)
00:53:31

[like even if they happen to have the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m36s)
00:53:36

[same letters in the same order they're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m39s)
00:53:39

[not referring in any way to the same](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m40s)
00:53:40

[thing that makes sense it's like this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m42s)
00:53:42

[family over here may have somebody](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m46s)
00:53:46

[called Jeremy and my family has somebody](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m47s)
00:53:47

[called Jeremy and our names happen to be](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m50s)
00:53:50

[the same but we're not the same person](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m52s)
00:53:52

[okay great so now that we've stuck the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h53m54s)
00:53:54

[decision tree sorry I did a fine Bettis](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m00s)
00:54:00

[flip method inside the decision tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m02s)
00:54:02

[with his new definition when I now call](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m04s)
00:54:04

[the tree ensemble constructor all right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m07s)
00:54:07

[the decision tree ensemble instructor](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m11s)
00:54:11

[called create tree create tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m12s)
00:54:12

[instantiated decision tree decision tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m16s)
00:54:16

[called find vas whit which went through](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m19s)
00:54:19

[every column to see if it could find a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m22s)
00:54:22

[better split and we've now defined find](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m24s)
00:54:24

[better split](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m28s)
00:54:28

[and therefore tree ensemble when we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m28s)
00:54:28

[create it has gone ahead and done this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m31s)
00:54:31

[wet](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m34s)
00:54:34

[that makes sense don't have any anybody](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m37s)
00:54:37

[have any questions uncertainties about](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m39s)
00:54:39

[that like we're only creating one single](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m42s)
00:54:42

[split so far](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m44s)
00:54:44

[all right so this is pretty pretty neat](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m47s)
00:54:47

[right we kind of just do a little bit at](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m51s)
00:54:51

[a time](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m53s)
00:54:53

[testing everything as we go and so it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m54s)
00:54:54

[as as as you all implement the random](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h54m57s)
00:54:57

[forest interpretation techniques you may](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m00s)
00:55:00

[want to try programming this way too](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m02s)
00:55:02

[like every step check that you know what](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m04s)
00:55:04

[you're doing matches up with what](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m08s)
00:55:08

[scikit-learn does or with a test that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m09s)
00:55:09

[you've built or whatever so at this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m11s)
00:55:11

[point we should try to go deeper very](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m14s)
00:55:14

[inception right so let's go now max](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m18s)
00:55:18

[depth is two and so here is what](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m21s)
00:55:21

[scikit-learn did after breaking it in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m24s)
00:55:24

[made 74 it then broke at Machine hours](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m26s)
00:55:26

[later](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m30s)
00:55:30

[29:56 so we had this thing called find](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m30s)
00:55:30

[violet right which just went through](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m37s)
00:55:37

[every column and try to see if there's a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m41s)
00:55:41

[better split there](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m43s)
00:55:43

[all right but actually we need to go a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m44s)
00:55:44

[bit further than that not only do we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m47s)
00:55:47

[have to go through every column and see](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m49s)
00:55:49

[if there's a better split in this node](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m52s)
00:55:52

[but then we also have to see whether](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m54s)
00:55:54

[there's a better split in the left and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m57s)
00:55:57

[the right sides that we just created](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h55m59s)
00:55:59

[right in other words the left right side](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m01s)
00:56:01

[and the right-hand side should become](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m04s)
00:56:04

[decision trees themselves right so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m06s)
00:56:06

[there's no difference at all between](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m09s)
00:56:09

[what we do here to create this tree and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m11s)
00:56:11

[what we do here to create this tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m13s)
00:56:13

[other than this one contains 159 samples](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m15s)
00:56:15

[and this one contains a thousand so this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m18s)
00:56:18

[row of codes exactly the same as we had](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m23s)
00:56:23

[before](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m24s)
00:56:24

[right and then we check it actually we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m25s)
00:56:25

[could do this a little bit easier we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m28s)
00:56:28

[could say if self dot is leaf right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m29s)
00:56:29

[would be the same thing hey don't leave](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m34s)
00:56:34

[it here for now](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m37s)
00:56:37

[so it's self dot score so if the score](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m37s)
00:56:37

[is infinite still let's write it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m40s)
00:56:40

[properly](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m43s)
00:56:43

[yes wait so let's go back up and just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m44s)
00:56:44

[remind ourselves is leaf is self that's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m48s)
00:56:48

[poor equals in okay so since it's there](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m54s)
00:56:54

[we mostly use it so if it's a leaf node](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h56m57s)
00:56:57

[then we have nothing further to do right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m00s)
00:57:00

[so that means we're right at the bottom](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m04s)
00:57:04

[there's no split that's been made okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m06s)
00:57:06

[so we don't have to do anything further](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m08s)
00:57:08

[on the other hand if it's not a leaf](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m09s)
00:57:09

[node so it's somewhere back earlier on](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m11s)
00:57:11

[then we need to split it into the left](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m13s)
00:57:13

[hand side and the right hand side now](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m16s)
00:57:16

[earlier on we created a left hand side](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m18s)
00:57:18

[in the right hand side array of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m21s)
00:57:21

[bullying's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m23s)
00:57:23

[right now better would be to have here](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m23s)
00:57:23

[we have an array of indexes and that's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m27s)
00:57:27

[because we don't want to have a full](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m30s)
00:57:30

[array of all the volumes in every single](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m32s)
00:57:32

[node right because remember although it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m34s)
00:57:34

[doesn't look like there are many nodes](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m36s)
00:57:36

[when you see a tree of this size when](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m38s)
00:57:38

[it's fully expanded the bottom level if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m40s)
00:57:40

[there's a minimum leaf size of one](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m43s)
00:57:43

[contains the same number of nodes as the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m45s)
00:57:45

[entire data set and so if every one of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m49s)
00:57:49

[those contained a full boolean array of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m51s)
00:57:51

[size of the whole data set you've got](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m53s)
00:57:53

[squared memory requirements which would](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m55s)
00:57:55

[be bad right on the other hand if we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h57m57s)
00:57:57

[just store the indexes there for things](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m00s)
00:58:00

[in this node and that's going to get](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m02s)
00:58:02

[smaller and smaller](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m04s)
00:58:04

[okay so NP non zero is exactly the same](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m04s)
00:58:04

[as just this thing which gets the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m11s)
00:58:11

[boolean array but it turns it into the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m13s)
00:58:13

[indexes of the truths okay so this is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m15s)
00:58:15

[now a list of indexes for the left-hand](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m18s)
00:58:18

[side and indexes to the right-hand side](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m20s)
00:58:20

[alright so now that we have the indexes](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m23s)
00:58:23

[the left-hand side and the right-hand](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m25s)
00:58:25

[side we can now just go ahead and create](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m27s)
00:58:27

[a decision tree okay so there's a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m30s)
00:58:30

[decision tree for the left and there's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m32s)
00:58:32

[our decision tree for the right okay and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m34s)
00:58:34

[we don't have to do anything else we've](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m37s)
00:58:37

[already written these we already have a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m38s)
00:58:38

[function of a constructor that can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m41s)
00:58:41

[create a decision tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m44s)
00:58:44

[so like when you really think about what](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m46s)
00:58:46

[this is doing it kind of hurts your head](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m48s)
00:58:48

[right because the reason the whole](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m51s)
00:58:51

[reason that fine vast bit got called is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m54s)
00:58:54

[because find vasp lit is called by the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h58m57s)
00:58:57

[decision tree constructor but then the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m05s)
00:59:05

[decision tree that then find vast bit](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m08s)
00:59:08

[itself then causes the decision tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m11s)
00:59:11

[constructor so we actually have circular](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m12s)
00:59:12

[recursion and I'm not nearly smart](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m16s)
00:59:16

[enough to be able to think through](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m20s)
00:59:20

[recursion so I just choose not to write](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m22s)
00:59:22

[like I just write what I mean and then I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m25s)
00:59:25

[don't think about it anymore right like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m29s)
00:59:29

[what do I want well to find a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m32s)
00:59:32

[variable-speed I've got to go through a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m34s)
00:59:34

[few column see if there's something](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m35s)
00:59:35

[better](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m37s)
00:59:37

[it had managed to do a split figure out](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m37s)
00:59:37

[left-hand side of the right-hand side](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m40s)
00:59:40

[and make them into decision trees okay](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m42s)
00:59:42

[but now try to think through how these](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m45s)
00:59:45

[two methods call each other would just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m48s)
00:59:48

[drive me crazy but I don't need to write](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m50s)
00:59:50

[I know I have a decision tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m52s)
00:59:52

[constructor that works no no no I have a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m54s)
00:59:54

[vine up find basket that works so that's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m56s)
00:59:56

[it right that's how I do recursive](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=00h59m59s)
00:59:59

[programming is by pretending I don't I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m02s)
01:00:02

[just just ignore it that's my advice](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m06s)
01:00:06

[a lot of you are probably smart enough](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m08s)
01:00:08

[to be able to think through it better](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m10s)
01:00:10

[than I can so that's fine if you can all](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m11s)
01:00:11

[right so now that I've written that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m14s)
01:00:14

[again I can patch it into the decision](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m15s)
01:00:15

[tree class and as soon as I do the tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m17s)
01:00:17

[ensemble constructor will now use that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m24s)
01:00:24

[right because pythons dynamic right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m26s)
01:00:26

[that's just happens automatically so now](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m28s)
01:00:28

[I can check my left-hand side](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m32s)
01:00:32

[should have 159 samples right and a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m36s)
01:00:36

[value of nine point six six](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m41s)
01:00:41

[there it is 159 samples nine point six](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m43s)
01:00:43

[six right hand side huh 841 10.15 the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m46s)
01:00:46

[left hand side of the left hand side 150](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m53s)
01:00:53

[samples nine point six to 150 samples](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h00m56s)
01:00:56

[nine point six - okay so you can see](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m00s)
01:01:00

[like I'm because I'm not nearly clever](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m03s)
01:01:03

[enough to write machine learning](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m06s)
01:01:06

[algorithms like not only can I not write](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m07s)
01:01:07

[them correctly the first time](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m10s)
01:01:10

[often like every single line I write](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m11s)
01:01:11

[will be wrong right so I always start](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m14s)
01:01:14

[from the assumption that the the line of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m16s)
01:01:16

[code I just typed is almost certainly](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m18s)
01:01:18

[wrong and I just have to see why and how](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m21s)
01:01:21

[right and so like I just make sure and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m23s)
01:01:23

[so eventually I get to the point where](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m26s)
01:01:26

[like much to my surprise it's not broken](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m27s)
01:01:27

[anymore you know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m30s)
01:01:30

[so here I can feel like okay this it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m31s)
01:01:31

[would be surprising if all of these](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m33s)
01:01:33

[things accidentally happen to be exactly](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m35s)
01:01:35

[the same as scikit-learn so this is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m36s)
01:01:36

[looking pretty good okay so now that we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m38s)
01:01:38

[have something that can build a whole](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m44s)
01:01:44

[tree where you want to have something](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m46s)
01:01:46

[that can calculate predictions right and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m48s)
01:01:48

[so remind you we already have something](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m51s)
01:01:51

[that calculates predictions for a tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m53s)
01:01:53

[ensemble by calling trade-up predict but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h01m55s)
01:01:55

[there is nothing called treetop predict](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m00s)
01:02:00

[so we're gonna have to write that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m02s)
01:02:02

[to make this more interesting let's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m06s)
01:02:06

[start bringing up the number of columns](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m08s)
01:02:08

[that we use let's create our tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m10s)
01:02:10

[ensemble again and this time let's go to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m15s)
01:02:15

[a maximum depth of three okay so now our](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m17s)
01:02:17

[tree is getting more interesting](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m22s)
01:02:22

[and let's now define how do we create a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m27s)
01:02:27

[set of predictions for a tree and so a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m31s)
01:02:31

[set of predictions for a tree is simply](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m34s)
01:02:34

[the prediction for a row for every row](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m36s)
01:02:36

[that's it all right that's our](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m42s)
01:02:42

[predictions so the predictions for a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m44s)
01:02:44

[tree are every rows predictions in an](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m45s)
01:02:45

[array okay so again we're like skipping](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m50s)
01:02:50

[thinking thinking's hard you know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m54s)
01:02:54

[so let's just like keep pushing it back](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h02m56s)
01:02:56

[this is kind of Handy right notice that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m00s)
01:03:00

[you can do four](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m04s)
01:03:04

[in array with an umpire array regardless](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m08s)
01:03:08

[of the rank of the array regardless of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m11s)
01:03:11

[the number of axes in the array and what](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m15s)
01:03:15

[it does is it will look through the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m19s)
01:03:19

[leading axis at least these concepts are](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m20s)
01:03:20

[going to be very very important as we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m24s)
01:03:24

[get into more and more neural networks](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m26s)
01:03:26

[because we're going to be all doing](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m28s)
01:03:28

[tensor computations all the time so the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m29s)
01:03:29

[leading axis that the vector is the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m31s)
01:03:31

[vector itself the leading axis of a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m34s)
01:03:34

[matrix are the rows the leading access](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m37s)
01:03:37

[axis of a three dimensional tensor the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m40s)
01:03:40

[matrices that represent the slices and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m44s)
01:03:44

[so forth right so in this case because X](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m46s)
01:03:46

[is a matrix this is going to look](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m49s)
01:03:49

[through the rows and if you write your](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m51s)
01:03:51

[kind of tensor code this way then it'll](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m53s)
01:03:53

[kind of tend to generalize nicely to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h03m57s)
01:03:57

[higher dimensions like it doesn't really](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m00s)
01:04:00

[mention matter how many dimensions are](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m02s)
01:04:02

[in X this is going to loop through each](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m04s)
01:04:04

[of the leading axis okay so we can now](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m05s)
01:04:05

[call that decision tree do I predict](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m11s)
01:04:11

[alright so all I need to do is write](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m16s)
01:04:16

[predict row right and I've delayed](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m20s)
01:04:20

[thinking so much which is great that the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m22s)
01:04:22

[actual point where I actually have to do](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m25s)
01:04:25

[the work it's now basically trivial so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m26s)
01:04:26

[if we're at a leaf no then the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m29s)
01:04:29

[prediction is just equal to whatever](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m33s)
01:04:33

[that value was which we calculated right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m36s)
01:04:36

[back in the original tree constructor is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m39s)
01:04:39

[to assist the average of the Y's right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m41s)
01:04:41

[if it's not a leaf node then we have to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m43s)
01:04:43

[figure out whether to go down the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m46s)
01:04:46

[left-hand path or the right-hand path to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m48s)
01:04:48

[get the prediction right so if this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m50s)
01:04:50

[variable in this row is less than or](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m56s)
01:04:56

[equal to that thing we decided the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h04m59s)
01:04:59

[amount we decided to split on then we go](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m00s)
01:05:00

[down the left path otherwise we go down](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m03s)
01:05:03

[the right path okay and then having](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m06s)
01:05:06

[figured out what path we want which tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m08s)
01:05:08

[we want then we can just call predict](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m10s)
01:05:10

[row on that right and again we've](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m12s)
01:05:12

[accidentally created something recursive](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m17s)
01:05:17

[again I don't want to think about how](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m19s)
01:05:19

[that works control flow wise or whatever](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m23s)
01:05:23

[but I don't need to because like I just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m27s)
01:05:27

[it just does like I just told it what I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m30s)
01:05:30

[wanted so I'll trust it to work right if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m32s)
01:05:32

[it's a leaf return the value otherwise](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m34s)
01:05:34

[return the prediction for the left hand](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m37s)
01:05:37

[side or the right hand side as](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m39s)
01:05:39

[appropriate there notice this here this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m40s)
01:05:40

[if has nothing to do with this if all](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m45s)
01:05:45

[right this if is a control flow](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m50s)
01:05:50

[statement that tells Python to go down](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m53s)
01:05:53

[on that path or that path to do some](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m57s)
01:05:57

[calculation this if is an operator that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h05m59s)
01:05:59

[returns a value so those of you that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m05s)
01:06:05

[have done C or C++ will recognize it as](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m09s)
01:06:09

[being identical to that it's called the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m12s)
01:06:12

[ternary operator all right if you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m14s)
01:06:14

[haven't that's fine basically what we're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m16s)
01:06:16

[doing is we're going to get a value](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m18s)
01:06:18

[where we're going to say it's this value](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m20s)
01:06:20

[if this thing is true and that value](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m22s)
01:06:22

[otherwise and so you could write it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m27s)
01:06:27

[this way right but that would require](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m33s)
01:06:33

[writing four lines of code to do one](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m36s)
01:06:36

[thing and also require you to code that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m38s)
01:06:38

[if you read it to yourself or to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m41s)
01:06:41

[somebody else is not at all naturally](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m43s)
01:06:43

[the way you would express it right I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m45s)
01:06:45

[want to say the tree I going to go down](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m47s)
01:06:47

[is the left-hand side if the variables](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m50s)
01:06:50

[less than the split or the right-hand](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m53s)
01:06:53

[side otherwise right so I want to write](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m55s)
01:06:55

[my code the way I would think about all](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h06m57s)
01:06:57

[the way I would say my code okay so this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m00s)
01:07:00

[kind of ternary operator can be quite](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m03s)
01:07:03

[helpful for that alright so now that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m06s)
01:07:06

[I've got a prediction for a row I can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m10s)
01:07:10

[dump that into my class and now I can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m12s)
01:07:12

[create calculate predictions and I can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m16s)
01:07:16

[now plot my actuals against my](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m21s)
01:07:21

[predictions when you do a scatter plot](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m23s)
01:07:23

[you'll often have a lot of dots sitting](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m27s)
01:07:27

[on top of each other so a good trick is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m30s)
01:07:30

[to use alpha alpha means how transparent](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m33s)
01:07:33

[the things not just a map plot lib but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m35s)
01:07:35

[like in every graphics package in the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m37s)
01:07:37

[world pretty much and so if you set](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m39s)
01:07:39

[alpha to less than 1 then this is saying](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m40s)
01:07:40

[you would need 20 dots on top of each](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m43s)
01:07:43

[other for it to be fully blue and so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m45s)
01:07:45

[this is a good way to kind of see how](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m48s)
01:07:48

[much things are sitting on top of each](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m50s)
01:07:50

[other so it's a good trick but trick the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m52s)
01:07:52

[scatter plots](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m54s)
01:07:54

[there's my R squared not bad](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h07m57s)
01:07:57

[and so let's now go ahead and do a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m01s)
01:08:01

[random forest with no max mana spitting](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m05s)
01:08:05

[and our tree ensemble had no max amount](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m12s)
01:08:12

[of spitting we can compare our R squared](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m17s)
01:08:17

[- there are squared and so they're not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m20s)
01:08:20

[the same but actually ours is a little](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m23s)
01:08:23

[better so I don't know what we did](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m26s)
01:08:26

[differently but we'll take it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m29s)
01:08:29

[okay so we have now something which for](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m31s)
01:08:31

[a forest with a single tree in is giving](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m35s)
01:08:35

[as good accuracy on a validation set](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m39s)
01:08:39

[using an actual real-world data set you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m43s)
01:08:43

[know books for pluto's is compared to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m45s)
01:08:45

[scikit-learn so let's go ahead and round](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m48s)
01:08:48

[this out so what I would want to do now](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m52s)
01:08:52

[is to create a package that has this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m55s)
01:08:55

[coding and I created it by like creating](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m57s)
01:08:57

[a method here a method here a method](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h08m59s)
01:08:59

[here and catching them together so what](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m01s)
01:09:01

[I did with now is I went back through in](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m03s)
01:09:03

[my notebook and collected up all the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m05s)
01:09:05

[cells had implemented methods and pasted](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m07s)
01:09:07

[them all together right and I've just](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m09s)
01:09:09

[pasted them down here so here's this is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m11s)
01:09:11

[my original tree ensemble and here is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m13s)
01:09:13

[all the cells and the decision tree I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m16s)
01:09:16

[just dumped them all into one place](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m17s)
01:09:17

[without any change so that was it that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m19s)
01:09:19

[was the code we wrote together so now I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m25s)
01:09:25

[can go ahead and I can create a tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m27s)
01:09:27

[ensemble I can calculate my predictions](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m32s)
01:09:32

[I can do my scatter plot I can get my](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m35s)
01:09:35

[r-squared right and this is now with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m38s)
01:09:38

[five trees right and here we are we have](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m42s)
01:09:42

[a model of blue dog for bulldozers with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m47s)
01:09:47

[a 71% a squid with a random forest we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m50s)
01:09:50

[wrote entirely from scratch that's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m53s)
01:09:53

[pretty cool](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h09m57s)
01:09:57

[any questions about that and I know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m00s)
01:10:00

[there's like quite a lot to get through](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m03s)
01:10:03

[so I during the week feel free to ask on](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m04s)
01:10:04

[the forum about any bits of code you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m07s)
01:10:07

[come across can somebody pass the box to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m10s)
01:10:10

[Mercia others](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m12s)
01:10:12

[can we get back to the probably to the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m18s)
01:10:18

[top maybe a decision tree when we said](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m22s)
01:10:22

[the score equal to infinity right yes I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m26s)
01:10:26

[do a calculator Scott the score for the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m28s)
01:10:28

[I mean like I lost track of that and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m32s)
01:10:32

[specifically I wonder when we implement](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m35s)
01:10:35

[when we implement find VAR split we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m40s)
01:10:40

[check for self score equal to whether](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m44s)
01:10:44

[it's equal to infinity or not it says to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m47s)
01:10:47

[me it seems like I'm clear whether we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m50s)
01:10:50

[fall out of this I mean like if we ever](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m53s)
01:10:53

[implement the method if if our initial](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h10m58s)
01:10:58

[value is infinity so okay let's talk](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m02s)
01:11:02

[sure the logic so so the decision tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m06s)
01:11:06

[starts out with a score at infinity so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m10s)
01:11:10

[in other words at this point when we've](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m12s)
01:11:12

[created the mode there is no split so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m14s)
01:11:14

[it's infinitely bad okay that's why the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m18s)
01:11:18

[score is infinity and then we try to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m21s)
01:11:21

[find a variable and a split that is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m24s)
01:11:24

[better and do that we look through each](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m28s)
01:11:28

[column and say hey column do you have a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m32s)
01:11:32

[split which is better than the best one](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m37s)
01:11:37

[we have so far and so then we implement](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m39s)
01:11:39

[that let's do the slow way since it's a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m43s)
01:11:43

[bit simpler find better split](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m50s)
01:11:50

[we do that by looping through each row](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m52s)
01:11:52

[and finding out this is the current](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m55s)
01:11:55

[score if we split here is it better than](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h11m59s)
01:11:59

[the current score the current score is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m01s)
01:12:01

[infinitely bad so yes it is and so now](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m03s)
01:12:03

[we set the new score equal to what we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m05s)
01:12:05

[just calculated and we keep track of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m08s)
01:12:08

[which variable we chose and the split we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m10s)
01:12:10

[spit on okay no worries](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m12s)
01:12:12

[okay great let's take a five-minute](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m20s)
01:12:20

[break and I'll see you back here at 22](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m23s)
01:12:23

[so when I tried comparing the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m30s)
01:12:30

[performance of this against scikit-learn](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m33s)
01:12:33

[this is quite a lot slower and the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m38s)
01:12:38

[reason why is that although like a lot](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m42s)
01:12:42

[of the works being done by numpy which](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m46s)
01:12:46

[is nicely optimized c-code think about](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m49s)
01:12:49

[like the very bottom level of a tree if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m53s)
01:12:53

[we've got a million data points and the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h12m56s)
01:12:56

[bottom level of the tree has something](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m01s)
01:13:01

[like 500 thousand decision points with a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m02s)
01:13:02

[million leaves underneath right and so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m07s)
01:13:07

[that's like five hundred thousand split](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m10s)
01:13:10

[methods being called each one of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m13s)
01:13:13

[contained which contains multiple calls](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m15s)
01:13:15

[to numpy which only have like one item](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m17s)
01:13:17

[that's actually being calculated on and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m21s)
01:13:21

[so it's like that's like very](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m23s)
01:13:23

[inefficient and it's the kind of thing](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m25s)
01:13:25

[that Python is particularly not good at](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m27s)
01:13:27

[performance wise right like calling lots](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m30s)
01:13:30

[of functions lots of times I mean we can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m33s)
01:13:33

[see it's it's not bad right you know for](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m35s)
01:13:35

[a kind of a random forest which 15 years](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m38s)
01:13:38

[ago would have been considered pretty](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m42s)
01:13:42

[big this would be considered pretty good](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m44s)
01:13:44

[performance right but nowadays this is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m46s)
01:13:46

[some hundreds of times at least slower](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m48s)
01:13:48

[than than it should be so what the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m51s)
01:13:51

[scikit-learn folks did to avoid this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m55s)
01:13:55

[problem was that they wrote their](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h13m59s)
01:13:59

[implementation in something called](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m02s)
01:14:02

[siphon and siphon is a superset of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m04s)
01:14:04

[Python so any Python you've written](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m09s)
01:14:09

[pretty much you can use as siphon right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m13s)
01:14:13

[but then what happens is siphon runs it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m20s)
01:14:20

[in a very different way rather than](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m24s)
01:14:24

[passing it to the kind of the Python](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m26s)
01:14:26

[interpreter it instead converts it to C](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m29s)
01:14:29

[can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m33s)
01:14:33

[Kyle's that and then runs that C code](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m34s)
01:14:34

[right which means the first time you run](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m37s)
01:14:37

[it it takes a little long work so it has](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m40s)
01:14:40

[to go through the kind of translation](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m42s)
01:14:42

[and compilation but then after that it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m44s)
01:14:44

[can be quite a bit faster and so I want](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m47s)
01:14:47

[to just to quickly show you what that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m51s)
01:14:51

[looks like because you are absolutely](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m53s)
01:14:53

[going to be in a position where siphons](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m58s)
01:14:58

[going to help you with your work and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h14m59s)
01:14:59

[most of the people you're working with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m01s)
01:15:01

[will have never used it may not even](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m03s)
01:15:03

[know it exists and so this is like a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m06s)
01:15:06

[great superpower to have so to use](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m07s)
01:15:07

[siphon in a notebook you say load next](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m10s)
01:15:10

[load extension siphon right and so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m13s)
01:15:13

[here's a Python function bit one here is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m17s)
01:15:17

[the same as a siphon function is exactly](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m25s)
01:15:25

[the same thing with percent % at the top](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m29s)
01:15:29

[this actually runs about twice as fast](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m33s)
01:15:33

[as this right just because it does their](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m37s)
01:15:37

[compilation here is the same version](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m40s)
01:15:40

[again where I've used a special siphon](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m45s)
01:15:45

[extension called C death which defines](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m48s)
01:15:48

[the C data type of the return value and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m51s)
01:15:51

[of each variable right and so basically](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h15m55s)
01:15:55

[that's the trick that you can use to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m00s)
01:16:00

[start making things run quickly right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m02s)
01:16:02

[and at that point now it knows it's not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m06s)
01:16:06

[just some Python object called T in fact](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m08s)
01:16:08

[I probably should put one here as well](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m13s)
01:16:13

[let's try that so we've got fib 2 we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m17s)
01:16:17

[call that 53 so 453 yeah so it's exactly](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m20s)
01:16:20

[the same as before but we say what the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m29s)
01:16:29

[data type of the thing we passed to it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m31s)
01:16:31

[was is and then define the data types of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m33s)
01:16:33

[each of the variables and so then if we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m35s)
01:16:35

[call that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m38s)
01:16:38

[okay we've now got something that's 10](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m45s)
01:16:45

[times faster right so yeah it doesn't](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m47s)
01:16:47

[really take that much extra and it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m51s)
01:16:51

[just it's just Python with a few little](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m52s)
01:16:52

[bits of markup so that's like it's it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m55s)
01:16:55

[good to know that that exists because if](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h16m58s)
01:16:58

[there's something custom you're trying](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m01s)
01:17:01

[to do it's actually a find it kind of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m03s)
01:17:03

[painful having to go out and you know](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m06s)
01:17:06

[going to see and compile it and whip it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m07s)
01:17:07

[back and all that where else doing it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m09s)
01:17:09

[here is pretty easy can you pass that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m10s)
01:17:10

[just your right please not sure so when](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m12s)
01:17:12

[you're doing like for the second version](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m17s)
01:17:17

[of it so in the case an array for an NP](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m20s)
01:17:20

[array this is a specific C type of yeah](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m22s)
01:17:22

[so there's like a lot of um specific](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m26s)
01:17:26

[stuff for integrating scythe on with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m30s)
01:17:30

[numpy and there's a whole page about it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m33s)
01:17:33

[yeah so we won't worry about going over](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m39s)
01:17:39

[it but you can read that and you can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m41s)
01:17:41

[basically see the basic ideas there's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m43s)
01:17:43

[this C import which basically imports a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m45s)
01:17:45

[certain types of Python library into the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m49s)
01:17:49

[kind of the C bit of the code and you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m52s)
01:17:52

[can then use it in your siphon yeah it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h17m55s)
01:17:55

[it's pretty straightforward well good](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m00s)
01:18:00

[question](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m04s)
01:18:04

[thank you all right so your your mission](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m05s)
01:18:05

[now is to implement confidence based on](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m09s)
01:18:09

[tree variance feature importance partial](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m19s)
01:18:19

[dependence in tree interpreter for that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m22s)
01:18:22

[random first removing redundant features](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m25s)
01:18:25

[doesn't use a random forest at all so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m29s)
01:18:29

[you don't have to worry about that the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m32s)
01:18:32

[extrapolation is not an interpretation](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m33s)
01:18:33

[technique so you don't have to worry](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m35s)
01:18:35

[about that so it's just the other ones](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m36s)
01:18:36

[so confidence based on tree variance](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m38s)
01:18:38

[we've already written that code so I](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m40s)
01:18:40

[suspect that the exact same code we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m42s)
01:18:42

[would have in the notebook should](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m44s)
01:18:44

[continue to work so you can try and make](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m46s)
01:18:46

[sure it get that working feature](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m48s)
01:18:48

[importance is with the variable](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m50s)
01:18:50

[shuffling technique and once you have](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m52s)
01:18:52

[that working partial dependence it will](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m55s)
01:18:55

[just be a couple of lines of code away](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m57s)
01:18:57

[rather than you know rather than](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h18m59s)
01:18:59

[shuffling a column you're just replacing](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m01s)
01:19:01

[it with a constant value that it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m03s)
01:19:03

[nearly the same code and then tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m05s)
01:19:05

[interpreter it's going to require you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m08s)
01:19:08

[writing some code and thinking about](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m11s)
01:19:11

[that well ince you've written tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m12s)
01:19:12

[interpreter you're very close if you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m13s)
01:19:13

[want to to creating the second approach](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m16s)
01:19:16

[to feature importance the one where you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m18s)
01:19:18

[add up the importance across all of the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m22s)
01:19:22

[rows which means you would then be very](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m26s)
01:19:26

[close to doing interaction importance so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m28s)
01:19:28

[it turns out that that there are](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m32s)
01:19:32

[actually there's actually a very good](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m34s)
01:19:34

[library for interaction importance for](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m35s)
01:19:35

[extra boost but there doesn't seem to be](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m37s)
01:19:37

[one for random forests so you could like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m40s)
01:19:40

[start by getting it working on our](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m42s)
01:19:42

[version and if you want to do](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m45s)
01:19:45

[interaction importance and then you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m46s)
01:19:46

[could like get it working on the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m48s)
01:19:48

[original site SK learn version and that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m49s)
01:19:49

[would be a cool contribution all right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m53s)
01:19:53

[like sometimes writing it against your](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m56s)
01:19:56

[own implementation is kind of nicer](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m57s)
01:19:57

[because you can see exactly what's going](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h19m59s)
01:19:59

[on all right so that's that's your job](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m01s)
01:20:01

[now you don't have to rewrite the random](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m03s)
01:20:03

[forest feel free to if you want to you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m05s)
01:20:05

[know practice so if you get stuck at any](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m07s)
01:20:07

[point you know ask on the forum right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m15s)
01:20:15

[there is a whole page here on wiki dot](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m19s)
01:20:19

[fast play I about how to ask for help so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m24s)
01:20:24

[when you ask your co-workers on slack](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m27s)
01:20:27

[for help when you ask people in a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m32s)
01:20:32

[technical community on github or](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m34s)
01:20:34

[discourse for help or whatever](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m36s)
01:20:36

[asking for help the right way will go a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m40s)
01:20:40

[long way towards you know having people](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m42s)
01:20:42

[want to help you and be able to help](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m45s)
01:20:45

[here right so so like search for your](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m47s)
01:20:47

[aunt's like search for the arrow you're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m51s)
01:20:51

[getting see if somebody's already asked](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m53s)
01:20:53

[about it you know how have you tried to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h20m54s)
01:20:54

[fix it already what do you think's going](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m00s)
01:21:00

[wrong what kind of computer are you on](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m03s)
01:21:03

[how is it set up what are the software](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m05s)
01:21:05

[versions exactly what did you type at](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m07s)
01:21:07

[exactly what happened right now you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m10s)
01:21:10

[could do that by taking a screenshot so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m12s)
01:21:12

[you know make sure you've got some](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m19s)
01:21:19

[screenshot software that's really easy](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m21s)
01:21:21

[to use so if I were to take a screenshot](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m22s)
01:21:22

[I just hit a button select the area copy](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m24s)
01:21:24

[to clipboard](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m27s)
01:21:27

[go to my forum paste it in and there we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m28s)
01:21:28

[go right that looks a little bit too big](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m33s)
01:21:33

[so let's make it a little smaller all](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m36s)
01:21:36

[right and so now I've got a screenshot](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m38s)
01:21:38

[people can see exactly what happened](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m40s)
01:21:40

[better still if there's a few lines of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m42s)
01:21:42

[code and error messages to look at and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m46s)
01:21:46

[create a gist it just is a handy little](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m48s)
01:21:48

[github thing which basically lets you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m53s)
01:21:53

[share code so if I wanted to create a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h21m56s)
01:21:56

[gist of this I actually have a extension](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m00s)
01:22:00

[area that little extension so if I click](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m06s)
01:22:06

[on here](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m09s)
01:22:09

[give it a name say make public okay and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m12s)
01:22:12

[that takes my Jupiter notebook shares it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m17s)
01:22:17

[publicly](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m20s)
01:22:20

[I can then grab that URL copy link](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m21s)
01:22:21

[location right and paste it into my](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m24s)
01:22:24

[forum post right and then when people](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m27s)
01:22:27

[click on it then they'll immediately see](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m30s)
01:22:30

[my notebook when it renders](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m37s)
01:22:37

[okay so that's a really good way now](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m42s)
01:22:42

[that particular button is an extension](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m46s)
01:22:46

[so on Jupiter you need to click end the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m48s)
01:22:48

[extensions and click on just it right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m52s)
01:22:52

[while you're there you should also click](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m56s)
01:22:56

[on collapsible headiness that's this](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m58s)
01:22:58

[really handy thing I use that lets me](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h22m59s)
01:22:59

[collapse things and open them up if you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m01s)
01:23:01

[go to your Jupiter and don't see this MB](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m05s)
01:23:05

[extensions button then just Google for](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m07s)
01:23:07

[Jupiter and B extensions it'll show you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m10s)
01:23:10

[how to pip install it and and get it set](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m11s)
01:23:11

[up right where those two extensions are](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m14s)
01:23:14

[SuperDuper handy](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m17s)
01:23:17

[alright so other than that assignment](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m20s)
01:23:20

[where we're done with random forests and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m26s)
01:23:26

[until the next course when you look at](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m30s)
01:23:30

[gPMs we're done with decision tree](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m32s)
01:23:32

[ensembles and so we're going to move on](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m34s)
01:23:34

[to neural networks broadly defined and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m39s)
01:23:39

[so Dero networks are going to allow us](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m43s)
01:23:43

[to to go beyond just you know the kind](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m48s)
01:23:48

[of nearest neighbors approach of random](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m52s)
01:23:52

[forests you know all around and forests](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m54s)
01:23:54

[can do is to average data that it's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m56s)
01:23:56

[already seen it can't extrapolate it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h23m59s)
01:23:59

[can't they can't calculate right linear](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m02s)
01:24:02

[regression can calculate and can](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m05s)
01:24:05

[extrapolate but only in very limited](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m08s)
01:24:08

[ways neural nets give us the best of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m11s)
01:24:11

[both worlds we're going to start by](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m15s)
01:24:15

[applying them to unstructured data all](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m20s)
01:24:20

[right so unstructured data means like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m25s)
01:24:25

[pixels or the amplitudes of sound waves](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m27s)
01:24:27

[or words you know data where everything](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m30s)
01:24:30

[in all the columns are all the same type](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m33s)
01:24:33

[you know as opposed to like a database](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m38s)
01:24:38

[table where you've got like a revenue](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m40s)
01:24:40

[and a cost and a zip code and a state it](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m42s)
01:24:42

[should be structured data we're going to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m45s)
01:24:45

[use it for structured data as well but](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m48s)
01:24:48

[we're going to do that a little bit](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m50s)
01:24:50

[later so structured data is a little](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m51s)
01:24:51

[easier and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m54s)
01:24:54

[it's also the area which more people](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m55s)
01:24:55

[have been applying deep learning to for](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h24m57s)
01:24:57

[longer](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m00s)
01:25:00

[the if you're doing the deep learning](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m05s)
01:25:05

[course as well you know you'll see that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m10s)
01:25:10

[we're going to be approaching kind of](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m13s)
01:25:13

[the same conclusion from two different](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m15s)
01:25:15

[directions so the deep learning course](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m17s)
01:25:17

[is starting out with big complicated](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m19s)
01:25:19

[convolutional neural networks being](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m24s)
01:25:24

[solved with you know sophisticated](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m26s)
01:25:26

[optimization schemes and we're going to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m28s)
01:25:28

[kind of gradually drill down into like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m30s)
01:25:30

[exactly how they work where else with](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m32s)
01:25:32

[the machine learning course we're going](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m35s)
01:25:35

[to be starting out more with like how](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m37s)
01:25:37

[does stochastic gradient descent](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m40s)
01:25:40

[actually work what do we do what can we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m41s)
01:25:41

[do is like one single layer which would](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m44s)
01:25:44

[allow us to create things like logistic](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m46s)
01:25:46

[regression when we add regularization to](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m48s)
01:25:48

[that how does that give us things like](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m52s)
01:25:52

[Ridge regression elastic net lasso and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m54s)
01:25:54

[then as we add additional layers to that](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h25m57s)
01:25:57

[how does that let us handle more complex](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m00s)
01:26:00

[problems and so we're not going to we're](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m03s)
01:26:03

[only going to be looking at fully](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m05s)
01:26:05

[connected layers in this machine](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m07s)
01:26:07

[learning course and then I think next](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m10s)
01:26:10

[semester with your net you're probably](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m14s)
01:26:14

[going to be looking at some more](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m16s)
01:26:16

[sophisticated approaches and so yeah so](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m18s)
01:26:18

[this machine learning we're going to be](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m21s)
01:26:21

[looking much more at like what's](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m22s)
01:26:22

[actually happening with the matrices and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m23s)
01:26:23

[how they actually calculated and the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m25s)
01:26:25

[deep learning it's much more like what](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m27s)
01:26:27

[are the best practices for actually](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m29s)
01:26:29

[solving you know at a world-class level](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m31s)
01:26:31

[real-world deep learning problems right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m34s)
01:26:34

[so next week we're going to be looking](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m37s)
01:26:37

[at like the classic Emnes problem which](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m44s)
01:26:44

[is like how do we recognize digits now](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m47s)
01:26:47

[if you're interested you can like skip](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m51s)
01:26:51

[ahead and like try and do this with a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m54s)
01:26:54

[random forest and you'll find it's not](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m56s)
01:26:56

[bad but it given that a random forest is](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h26m58s)
01:26:58

[basically a type of nearest neighbors](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m00s)
01:27:00

[right it's finding like what are the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m02s)
01:27:02

[nearest neighbors in entry space then a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m03s)
01:27:03

[random forest could absolutely recognize](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m07s)
01:27:07

[that this nine those pixels you know are](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m09s)
01:27:09

[similar to pixels we've seen in these](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m13s)
01:27:13

[other ones and on average they were](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m15s)
01:27:15

[nines as well right](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m17s)
01:27:17

[so like it can absolutely solve these](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m19s)
01:27:19

[kinds of problems to an extent using](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m22s)
01:27:22

[random forests but we end up being](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m25s)
01:27:25

[rather data limited because every time](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m28s)
01:27:28

[we put in another decision point you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m30s)
01:27:30

[know we're having our data roughly and](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m33s)
01:27:33

[so this is this limitation and the](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m36s)
01:27:36

[amount of calculation that we can do](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m38s)
01:27:38

[where else with neural nets we're going](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m40s)
01:27:40

[to be able to use lots and lots and lots](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m44s)
01:27:44

[of parameters using these tricks we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m47s)
01:27:47

[don't learn about with regularization](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m50s)
01:27:50

[and so we're going to be able to do lots](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m51s)
01:27:51

[of computation and there's got to be](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m53s)
01:27:53

[very little limitation on really what we](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m55s)
01:27:55

[can actually end up calculating as a](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h27m58s)
01:27:58

[result great good luck with your random](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h28m00s)
01:28:00

[forest interpretation and I will see you](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h28m03s)
01:28:03

[next time](https://www.youtube.com/watch?v=O5F9vR2CNYI#t=01h28m05s)
01:28:05

