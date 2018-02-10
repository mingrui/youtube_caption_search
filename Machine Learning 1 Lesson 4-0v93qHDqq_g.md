[all right welcome back something to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m00s)
00:00:00

[mention somebody asked on the forums](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m04s)
00:00:04

[really good question](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m06s)
00:00:06

[was like how do I deal with version](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m07s)
00:00:07

[control and notebooks the question was](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m10s)
00:00:10

[something like every time I change the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m14s)
00:00:14

[notebook Jeremy goes and changes it on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m15s)
00:00:15

[git and then I do a git pull and I end](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m17s)
00:00:17

[up with a conflict and I love that and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m19s)
00:00:19

[that's that happens a lot with notebooks](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m21s)
00:00:21

[because notebooks behind the scenes at](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m24s)
00:00:24

[JSON files which like every time you run](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m27s)
00:00:27

[even a cell without changing it it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m29s)
00:00:29

[updates that little number saying like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m32s)
00:00:32

[what numbered cell this is and so now](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m33s)
00:00:33

[suddenly there's a change and so trying](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m35s)
00:00:35

[to merge notebook changes is a nightmare](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m37s)
00:00:37

[so my suggestion I'd like a simple way](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m40s)
00:00:40

[to do it is is when you're looking at](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m44s)
00:00:44

[some notebook like less than 200 if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m48s)
00:00:48

[interpretation you want to start playing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m52s)
00:00:52

[around with this the first thing I would](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m54s)
00:00:54

[do would be to go file make a copy and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h00m58s)
00:00:58

[then in the copy say file rename and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m01s)
00:01:01

[give it a name that starts with TMP that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m04s)
00:01:04

[will hide it from get right and so now](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m08s)
00:01:08

[you've got your own version of that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m10s)
00:01:10

[workbook that you can that you can play](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m11s)
00:01:11

[with okay and so if you now do a git](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m13s)
00:01:13

[pull and see that the original changed](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m15s)
00:01:15

[it won't conflict with yours and you can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m17s)
00:01:17

[now see there are two different versions](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m19s)
00:01:19

[there are different ways of kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m23s)
00:01:23

[dealing with this Jupiter notebook get](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m25s)
00:01:25

[problem like everybody has it one one is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m27s)
00:01:27

[there are some hooks you can use it like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m29s)
00:01:29

[remove all of the cell outputs before](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m31s)
00:01:31

[you commit to get but in this case I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m34s)
00:01:34

[actually want the outputs to be in the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m36s)
00:01:36

[repo so you can read it on github and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m37s)
00:01:37

[see it so it's a minor issue but it's a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m40s)
00:01:40

[it's something which catches everybody](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m43s)
00:01:43

[ah yes before we move on to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m48s)
00:01:48

[interpretation of the random forest](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m54s)
00:01:54

[model I wonder if we could summarize the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m56s)
00:01:56

[relationship between the hyper](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h01m58s)
00:01:58

[parameters on the random forest and its](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m01s)
00:02:01

[effect on you know overfitting and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m03s)
00:02:03

[dealing with collinearity and yeah that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m06s)
00:02:06

[sounds like a question born from](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m09s)
00:02:09

[experience absolutely so I gotta go back](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m11s)
00:02:11

[to lesson 1 RF if you're ever unsure](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m18s)
00:02:18

[about where I am you can always see my](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m21s)
00:02:21

[top here courses mly and lesson 1 on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m23s)
00:02:23

[earth in terms of the hyper parameters](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m25s)
00:02:25

[that are interesting and I'm ignoring](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m31s)
00:02:31

[I'm ignoring like pre-processing but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m36s)
00:02:36

[just the actual hyper parameters the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m39s)
00:02:39

[first one of interest I would say is the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m42s)
00:02:42

[set RF samples command which determines](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m45s)
00:02:45

[how many rows are in each sample so in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m49s)
00:02:49

[each tree you're created from how many](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m53s)
00:02:53

[rows n each tree so before we start a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h02m55s)
00:02:55

[new tree we either bootstrap a sample so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m01s)
00:03:01

[sampling with replacement from the whole](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m05s)
00:03:05

[thing or we pull out a subsample of a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m07s)
00:03:07

[smaller number of rows and then we build](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m10s)
00:03:10

[a tree from there so so step one is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m12s)
00:03:12

[we've got our whole big data set and we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m19s)
00:03:19

[grab a few rows at random from it and we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m21s)
00:03:21

[turn them into a smaller data set and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m24s)
00:03:24

[then from that we build a tree right so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m26s)
00:03:26

[that's the size of that is set our F](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m29s)
00:03:29

[samples so when we change that size](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m32s)
00:03:32

[let's say this originally had like a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m35s)
00:03:35

[million rows and we said set our F](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m38s)
00:03:38

[samples twenty thousand right and then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m40s)
00:03:40

[we're going to grow a tree from there](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m43s)
00:03:43

[assuming that the tree remains kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m46s)
00:03:46

[balanced as we grow it can somebody tell](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m51s)
00:03:51

[me how many layers deep with this tree](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m53s)
00:03:53

[be and assuming we're growing it until](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m57s)
00:03:57

[every leaf is of size one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h03m59s)
00:03:59

[yes log base 2 of 20,000](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m02s)
00:04:02

[right okay so the the depth of the tree](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m08s)
00:04:08

[doesn't actually vary that much](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m14s)
00:04:14

[depending on the month samples right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m16s)
00:04:16

[because it's it's related to the log of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m18s)
00:04:18

[the size can somebody tell me at the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m22s)
00:04:22

[very bottom so once we go all the way](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m26s)
00:04:26

[down to the bottom](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m28s)
00:04:28

[how many leaf nodes would there be speak](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m28s)
00:04:28

[up what what do you think right because](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m36s)
00:04:36

[every single leaf node has a single](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m39s)
00:04:39

[thing in it so we've got obviously a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m41s)
00:04:41

[linear relationship between the number](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m45s)
00:04:45

[of leaf nodes in the size of the sample](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m46s)
00:04:46

[so when you decrease the sample size it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m49s)
00:04:49

[means that there are less kind of final](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m55s)
00:04:55

[decisions that can be made right so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h04m58s)
00:04:58

[therefore the tree is is going to be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m01s)
00:05:01

[less rich in terms of what it can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m04s)
00:05:04

[predict because it's just making less](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m06s)
00:05:06

[different individual decisions and it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m07s)
00:05:07

[also is making less binary choices to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m10s)
00:05:10

[get to those decisions so therefore](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m13s)
00:05:13

[setting RS samples lower is going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m15s)
00:05:15

[mean that you over fit less but it also](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m19s)
00:05:19

[means that you're going to have a less](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m23s)
00:05:23

[accurate individual tree model right and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m25s)
00:05:25

[so remember the way Braman the inventor](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m29s)
00:05:29

[of random first described this is that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m32s)
00:05:32

[you're trying to do two things when you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m34s)
00:05:34

[build a model when you build a model](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m36s)
00:05:36

[with bagging one is that each individual](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m38s)
00:05:38

[tree or as SQL you say each individual](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m42s)
00:05:42

[estimator is as accurate as possible](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m45s)
00:05:45

[right on the training set so it's like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m52s)
00:05:52

[each model is a strong predictive model](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m55s)
00:05:55

[but then the across the estimators](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h05m58s)
00:05:58

[relation between them is as low as](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m08s)
00:06:08

[possible so that when you average them](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m12s)
00:06:12

[out together you end up with something](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m14s)
00:06:14

[that generalizes so by decreasing the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m17s)
00:06:17

[set RF samples number we are actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m19s)
00:06:19

[decreasing the power of the estimator](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m22s)
00:06:22

[and increasing the correlation and so is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m24s)
00:06:24

[that going to result in a better or a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m27s)
00:06:27

[worse validation set result for you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m29s)
00:06:29

[it depends right this is the kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m32s)
00:06:32

[compromise which you have to figure out](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m35s)
00:06:35

[when you do machine learning models can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m37s)
00:06:37

[you pass that back there](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m42s)
00:06:42

[if I wait if I put the Bovie value equal](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m46s)
00:06:46

[to so it is basically dividing every 30](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m49s)
00:06:49

[it ensures that the data won't be there](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m53s)
00:06:53

[in each three right now our page second](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h06m57s)
00:06:57

[probably if I put all the equal to two](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m00s)
00:07:00

[yeah random voice yeah so is it that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m02s)
00:07:02

[make sure that out of my entire data 37](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m05s)
00:07:05

[personal data would be there in every](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m08s)
00:07:08

[tree so all our P equals true does is it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m10s)
00:07:10

[says whatever your sub sample is it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m15s)
00:07:15

[might be a bootstrap sample or it might](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m19s)
00:07:19

[be a subsample take all with the other](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m21s)
00:07:21

[rows right and put them into a tree tree](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m26s)
00:07:26

[and put them into a different data set](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m31s)
00:07:31

[and calculate the the error on those so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m32s)
00:07:32

[it doesn't actually impact training at](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m37s)
00:07:37

[all it just gives you an additional](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m38s)
00:07:38

[metric which is the oob error so if you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m40s)
00:07:40

[don't have a validation set then this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m45s)
00:07:45

[allows you to get kind of a quasi](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m49s)
00:07:49

[validation set for free if you want to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h07m52s)
00:07:52

[set out a sample](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m00s)
00:08:00

[Aref sample so that the default is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m03s)
00:08:03

[actually if you say reset our F samples](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m07s)
00:08:07

[and that causes it to bootstrap so it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m12s)
00:08:12

[all sample our new data set as big as](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m17s)
00:08:17

[the original one but with replacement](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m20s)
00:08:20

[okay so obviously the second benefit of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m27s)
00:08:27

[set our samples is that you can run more](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m30s)
00:08:30

[quickly and particularly if you're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m33s)
00:08:33

[running on a really large data set like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m35s)
00:08:35

[a hundred million rows you know it won't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m37s)
00:08:37

[be possible to run it on the full data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m39s)
00:08:39

[set so you would either have to pick a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m41s)
00:08:41

[subsample if yourself before you start](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m43s)
00:08:43

[or you set our examples](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m45s)
00:08:45

[the second key parameter that we learnt](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m48s)
00:08:48

[about was min samples leaf okay so if I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m51s)
00:08:51

[changed min samples leaf](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m56s)
00:08:56

[for we assumed that men samples leaf was](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h08m59s)
00:08:59

[equal to 1 all right if I set it equal](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m02s)
00:09:02

[to 2 then what would be my new depth how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m07s)
00:09:07

[deep would it be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m12s)
00:09:12

[yes](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m17s)
00:09:17

[log base to 20,000 minus one okay so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m18s)
00:09:18

[each time we double the min samples leaf](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m21s)
00:09:21

[we're removing one layer from the tree](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m24s)
00:09:24

[and fine I'll come back to you again](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m27s)
00:09:27

[since you're doing so well](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m30s)
00:09:30

[how many leaf nodes would there be in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m31s)
00:09:31

[that case](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m34s)
00:09:34

[but how many leaf nodes would there be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m38s)
00:09:38

[in that case](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m41s)
00:09:41

[10,000 okay so we're gonna be again](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m46s)
00:09:46

[dividing the number of leaf nodes by](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m49s)
00:09:49

[that number so the result of increasing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m51s)
00:09:51

[min samples leaf is that now each of our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m54s)
00:09:54

[leaf nodes has more than one thing in so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m57s)
00:09:57

[we're going to get a more stable average](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h09m59s)
00:09:59

[that we're calculating in each tree okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m03s)
00:10:03

[we've got a little bit less depth okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m08s)
00:10:08

[we've got less decisions to make and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m11s)
00:10:11

[we've got a smaller number of leaf nodes](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m13s)
00:10:13

[so again we would expect the result of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m14s)
00:10:14

[that would be that each estimator would](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m16s)
00:10:16

[be less predictive but the estimators](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m18s)
00:10:18

[would be also less correlated so again](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m22s)
00:10:22

[this might help us to avoid overfitting](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m26s)
00:10:26

[could you pass the microphone over here](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m28s)
00:10:28

[please oh hi Jimmy I'm not sure if in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m31s)
00:10:31

[that case every node will have exactly](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m36s)
00:10:36

[two no it won't necessarily have exactly](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m39s)
00:10:39

[two and I thank you for mentioning that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m41s)
00:10:41

[so it might try to do a split and so one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m43s)
00:10:43

[reason well what would be an example](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m47s)
00:10:47

[Chen XI that you wouldn't split even if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m48s)
00:10:48

[you had a hundred nodes what might be a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m52s)
00:10:52

[reason for that sorry 100 items in a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m55s)
00:10:55

[leaf node they're all the same they're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h10m57s)
00:10:57

[all the same in terms of the independent](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m00s)
00:11:00

[to saw the dependent and it has the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m04s)
00:11:04

[dependent right now I mean I guess](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m09s)
00:11:09

[either but much more likely would be the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m10s)
00:11:10

[dependent so if you get to a leaf node](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m12s)
00:11:12

[where every single one of them has the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m13s)
00:11:13

[same option price or in classification](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m17s)
00:11:17

[like every single one of them is a dog](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m19s)
00:11:19

[then there is no split that you can do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m20s)
00:11:20

[that's going to improve your information](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m23s)
00:11:23

[all right and remember information is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m25s)
00:11:25

[the term we use in a kind of a general](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m27s)
00:11:27

[sense in random for us to describe the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m30s)
00:11:30

[amount of difference about at that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m33s)
00:11:33

[additional information we create from a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m36s)
00:11:36

[split is like how much are we improving](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m38s)
00:11:38

[the model so you'll often see this word](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m40s)
00:11:40

[information gain which means like how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m42s)
00:11:42

[much better did the model get by adding](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m44s)
00:11:44

[an additional split point and it could](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m46s)
00:11:46

[be based on our MSC or it could be based](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m49s)
00:11:49

[on cross-entropy or it could be based on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m51s)
00:11:51

[how different to the standard deviations](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m52s)
00:11:52

[or whatever so that's just a general](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m54s)
00:11:54

[term okay so that's the second thing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m56s)
00:11:56

[that we can do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m58s)
00:11:58

[again it's going to speed up our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h11m59s)
00:11:59

[training because it's like one less set](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m01s)
00:12:01

[of decisions to make remember even](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m03s)
00:12:03

[though there's one less set of decisions](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m05s)
00:12:05

[those decisions like have as much data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m07s)
00:12:07

[again as the previous set so like each](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m11s)
00:12:11

[layer of the tree can take like twice as](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m13s)
00:12:13

[long as the previous layer so it could](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m15s)
00:12:15

[definitely speed up training and it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m17s)
00:12:17

[could definitely make it generalize](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m19s)
00:12:19

[better so then the third one that we had](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m20s)
00:12:20

[was max features who wants to tell me](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m25s)
00:12:25

[what max features does](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m29s)
00:12:29

[I want to pass that back over there okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m34s)
00:12:34

[Vinay we just leave their minds](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m38s)
00:12:38

[how many features you're going to use in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m42s)
00:12:42

[HP in this case it's a fraction up so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m44s)
00:12:44

[you're going to use up other be just for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m48s)
00:12:48

[each three nearly right what kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m50s)
00:12:50

[right can you be more specific or can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m54s)
00:12:54

[somebody else be more specific it's not](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m56s)
00:12:56

[exactly for each tree can she](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h12m57s)
00:12:57

[that is that for each tree randomly](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m03s)
00:13:03

[simple healthy so not quite it's not for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m06s)
00:13:06

[each tree so the the set don't possibly](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m10s)
00:13:10

[care them so the scent are of samples](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m12s)
00:13:12

[picks a picks a subset of samples subset](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m14s)
00:13:14

[of rows for each tree but min samples](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m21s)
00:13:21

[leaf sorry that max features doesn't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m25s)
00:13:25

[quite do that it's not something](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m27s)
00:13:27

[different at each set smell ant will](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m28s)
00:13:28

[yeah right so it kind of sounds like a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m37s)
00:13:37

[small difference but it's actually quite](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m42s)
00:13:42

[a different way of thinking about it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m43s)
00:13:43

[which is we do our set our samples so we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m44s)
00:13:44

[pull out our sub sample or a bootstrap](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m47s)
00:13:47

[sample and that's kept for the whole](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m49s)
00:13:49

[tree and we have all of the columns in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m51s)
00:13:51

[there right and then with max features](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m54s)
00:13:54

[equals 0.5 at each point we then at each](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h13m59s)
00:13:59

[split we'd pick a different half of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m01s)
00:14:01

[features and then here what you could](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m05s)
00:14:05

[pick a different half of the features](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m06s)
00:14:06

[and here we'll pick a different half of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m08s)
00:14:08

[the features and so the reason we do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m09s)
00:14:09

[that is because we want the trees to be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m11s)
00:14:11

[as as rich as possible right so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m14s)
00:14:14

[particularly like if you if you were](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m17s)
00:14:17

[only doing a small number of trees like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m19s)
00:14:19

[you had only ten trees and you picked](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m21s)
00:14:21

[the same column set all the way through](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m23s)
00:14:23

[the tree you're not really getting much](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m26s)
00:14:26

[variety and what kind of things are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m28s)
00:14:28

[confined okay so this this way at least](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m30s)
00:14:30

[in theory seems to be something which is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m33s)
00:14:33

[going to give us a better set of trees](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m37s)
00:14:37

[picking a different random subset of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m38s)
00:14:38

[features at every decision point so the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m41s)
00:14:41

[overall effective max features again](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m48s)
00:14:48

[it's the same it's going to mean that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m50s)
00:14:50

[the traits individual tree is probably](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m51s)
00:14:51

[going to be less accurate but the trees](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m54s)
00:14:54

[are going to be more buried and in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h14m59s)
00:14:59

[particular here this can be critical](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m00s)
00:15:00

[because like imagine that you've got one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m03s)
00:15:03

[feature that's just super predictive](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m06s)
00:15:06

[it's so predictive that like every](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m08s)
00:15:08

[random subsample you look at always](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m09s)
00:15:09

[starts out by splitting on that same](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m12s)
00:15:12

[feature then the trees are going to be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m13s)
00:15:13

[very similar in the sense like they all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m16s)
00:15:16

[have the same initial split right but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m18s)
00:15:18

[there may be some other are interesting](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m20s)
00:15:20

[initial splits because they create](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m23s)
00:15:23

[different interactions of variables so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m25s)
00:15:25

[by like half the time that feature won't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m27s)
00:15:27

[even be available at the top of the tree](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m30s)
00:15:30

[so half at least half the trees are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m32s)
00:15:32

[going to have a different initial split](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m34s)
00:15:34

[so it definitely can give us more](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m35s)
00:15:35

[variation and therefore again it can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m38s)
00:15:38

[help us to create more generalized trees](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m40s)
00:15:40

[that have less correlation with each](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m42s)
00:15:42

[other even though the individual trees](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m44s)
00:15:44

[probably won't be as predictive](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m46s)
00:15:46

[in practice we actually looked at have a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m49s)
00:15:49

[little picture of this that as as you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m51s)
00:15:51

[add more trees right if you have max](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m53s)
00:15:53

[features equals none that's going to use](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m57s)
00:15:57

[all the features every time right then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h15m58s)
00:15:58

[with like very very few trees that can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m00s)
00:16:00

[still give you a pretty good error but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m03s)
00:16:03

[as you create more trees it's not going](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m06s)
00:16:06

[to help as much because they're all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m09s)
00:16:09

[pretty similar because they're all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m10s)
00:16:10

[trying every single variable where else](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m12s)
00:16:12

[if you say max features equal square](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m15s)
00:16:15

[root or max pictures equals log two then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m17s)
00:16:17

[as we add more estimators we see](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m19s)
00:16:19

[improvements okay so there's an](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m22s)
00:16:22

[interesting interaction between those](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m24s)
00:16:24

[two and this is from the SK loan Docs](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m26s)
00:16:26

[this cool little chat okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m28s)
00:16:28

[so then things which don't impact out](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m32s)
00:16:32

[our training at all and jobs simply says](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m35s)
00:16:35

[how many cpu how many cause do we run on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m39s)
00:16:39

[okay so it'll make it faster up to a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m42s)
00:16:42

[point](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m44s)
00:16:44

[generally speaking making this more than](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m44s)
00:16:44

[like eight or so they may have](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m47s)
00:16:47

[diminishing returns -1 says use all of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m49s)
00:16:49

[your cause](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m52s)
00:16:52

[so there's wrote there's I don't know](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m54s)
00:16:54

[why the default is to only use one core](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m56s)
00:16:56

[that's seems weird to me you'll](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h16m59s)
00:16:59

[definitely get more performance by using](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m02s)
00:17:02

[more cause because all of you have](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m03s)
00:17:03

[computers with more than one core](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m05s)
00:17:05

[nowadays and then our base core equals](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m06s)
00:17:06

[true simply allows us to see the low B](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m09s)
00:17:09

[score if you don't say that it doesn't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m14s)
00:17:14

[calculate it and particularly if you had](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m16s)
00:17:16

[set RF samples pretty small compared to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m19s)
00:17:19

[a big data set or B is going to take](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m22s)
00:17:22

[forever to calculate hopefully at some](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m24s)
00:17:24

[point we'll be able to fix the library](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m26s)
00:17:26

[so that doesn't happen there's no reason](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m28s)
00:17:28

[that need be that way but right now](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m30s)
00:17:30

[that's that's how the Bible place okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m32s)
00:17:32

[our base Kuhn okay basic parameters that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m38s)
00:17:38

[we can change there are more that you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m43s)
00:17:43

[can see in the docs or shift tab to have](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m46s)
00:17:46

[a look at them but the ones you've seen](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m48s)
00:17:48

[are the ones that I've found useful to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m50s)
00:17:50

[play with so feel free to play with](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m52s)
00:17:52

[others as well and generally speaking](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m53s)
00:17:53

[you know max features as I said max](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h17m57s)
00:17:57

[features are like either non means all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m00s)
00:18:00

[of them about 0.5 or square root or log](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m06s)
00:18:06

[you know kind of those trees seem to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m18s)
00:18:18

[work pretty well and then some in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m21s)
00:18:21

[samples leaf you know I would generally](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m23s)
00:18:23

[try kind of 1 3 5 10 25 you know 100 and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m27s)
00:18:27

[like as you start doing that if you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m34s)
00:18:34

[notice by the time you get to 10 it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m36s)
00:18:36

[already getting worse then there's no](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m37s)
00:18:37

[point going further if you get to 100](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m38s)
00:18:38

[it's still going better then you can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m41s)
00:18:41

[keep trying right but they're the kind](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m42s)
00:18:42

[of general amounts that most things in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m44s)
00:18:44

[to sit in all right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m47s)
00:18:47

[so random forest interpretation is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m51s)
00:18:51

[something which you could use to create](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m55s)
00:18:55

[some really cool cattle kernels now](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h18m59s)
00:18:59

[obviously one issue is the faster I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m01s)
00:19:01

[library is not available in Cabell](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m04s)
00:19:04

[kernels but if you look inside fast AI](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m06s)
00:19:06

[dot structured right remember you can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m09s)
00:19:09

[just use double question mark to look at](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m12s)
00:19:12

[the source code for something or you can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m15s)
00:19:15

[go into the editor to have a look at it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m17s)
00:19:17

[you'll see that most of the methods](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m18s)
00:19:18

[we're using or a small number of lines](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m21s)
00:19:21

[of code in this library and have no](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m23s)
00:19:23

[dependencies on anything so you could](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m26s)
00:19:26

[just copy that little if you need to use](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m28s)
00:19:28

[one of those functions just copy it into](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m30s)
00:19:30

[your kernel and and if you do to say](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m32s)
00:19:32

[this is from the first day a library you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m35s)
00:19:35

[can link to it on github because it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m37s)
00:19:37

[available on github as open-source but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m39s)
00:19:39

[you don't need to import the whole thing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m41s)
00:19:41

[right so this is a cool trick is that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m43s)
00:19:43

[because you're the first people to learn](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m45s)
00:19:45

[how to use these tools you couldn't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m47s)
00:19:47

[start to show things that other people](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m49s)
00:19:49

[haven't seen right so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m51s)
00:19:51

[for example this confidence based on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m52s)
00:19:52

[tree variance is something which doesn't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m55s)
00:19:55

[exist anywhere else feature importance](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m56s)
00:19:56

[definitely does and that's already in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h19m59s)
00:19:59

[quite a lot of cable kernels if you're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m01s)
00:20:01

[looking at a competition or a data set](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m03s)
00:20:03

[that where nobody's done feature](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m05s)
00:20:05

[importance being the first person to do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m06s)
00:20:06

[that is always going to win lots of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m08s)
00:20:08

[votes because it's like the most](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m10s)
00:20:10

[important thing is like which features](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m11s)
00:20:11

[are important so last time we let's just](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m14s)
00:20:14

[make sure we put our tree data so we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m21s)
00:20:21

[need to change this to add one extra](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m27s)
00:20:27

[thing all right so that's no load no](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m29s)
00:20:29

[data yet there's that data okay so as I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m32s)
00:20:32

[mentioned when we do mobile](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m44s)
00:20:44

[interpretation I tend to set our of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m45s)
00:20:45

[samples to some subset something small](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m47s)
00:20:47

[enough that I can ran a model in under](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m50s)
00:20:50

[10 seconds or so because there's just no](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m52s)
00:20:52

[point run running a super accurate model](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m55s)
00:20:55

[fifty thousand is more than enough to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h20m57s)
00:20:57

[see you'll basically see each time you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m00s)
00:21:00

[run an interpretation you'll get the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m03s)
00:21:03

[same results back and so as long as](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m05s)
00:21:05

[that's true then you you're already](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m07s)
00:21:07

[using enough data okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m08s)
00:21:08

[so feature importance we learnt it works](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m14s)
00:21:14

[by randomly shuffling a column each](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m19s)
00:21:19

[column one at a time and then seeing how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m24s)
00:21:24

[accurate the model the pre trained model](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m27s)
00:21:27

[the model we've already built is when](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m29s)
00:21:29

[you pass it in all the data as before](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m31s)
00:21:31

[but with one column shuffled so some of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m34s)
00:21:34

[the questions I got after class kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m40s)
00:21:40

[reminded me that it's very easy to under](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m44s)
00:21:44

[appreciated and kind of magic this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m49s)
00:21:49

[approach is and so to explain I'll](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m53s)
00:21:53

[mention a couple of the questions that I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m57s)
00:21:57

[heard and so one question was like why](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h21m59s)
00:21:59

[don't we or what if we just um](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m03s)
00:22:03

[we took one column at a time and created](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m05s)
00:22:05

[a tree on just each one column at a time](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m08s)
00:22:08

[so we've got our data set it's got a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m12s)
00:22:12

[bunch of columns so why don't we just](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m14s)
00:22:14

[like we have that column and just build](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m15s)
00:22:15

[a tree from that right and then like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m17s)
00:22:17

[we'll see which which columns tree is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m20s)
00:22:20

[the most predictive can anybody tell me](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m23s)
00:22:23

[why what why that may give misleading](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m27s)
00:22:27

[results about feature importance okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m30s)
00:22:30

[we're going to lose the interactions](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m39s)
00:22:39

[between the features yeah if we just](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m42s)
00:22:42

[shuffle them it will be a bad randomness](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m45s)
00:22:45

[and we were able to both capture the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m48s)
00:22:48

[interactions and the importance of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m50s)
00:22:50

[future it's great yeah and and so this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m52s)
00:22:52

[issue of interactions is not a minor](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m56s)
00:22:56

[detail it's like it's massively](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h22m58s)
00:22:58

[important so like think about this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m01s)
00:23:01

[bulldozes data set where for example](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m04s)
00:23:04

[where there's one field called year made](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m07s)
00:23:07

[and there's one field called sale date](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m09s)
00:23:09

[and like if we think about it it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m13s)
00:23:13

[pretty obvious that what matters is the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m18s)
00:23:18

[combination of these two which in other](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m20s)
00:23:20

[words is like how old is the piece of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m22s)
00:23:22

[equipment when it got sold so if we only](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m25s)
00:23:25

[included one of these we're going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m28s)
00:23:28

[massively underestimate how important](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m31s)
00:23:31

[that feature is now here's a really](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m33s)
00:23:33

[important point though if you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m37s)
00:23:37

[it's pretty much always possible to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m40s)
00:23:40

[create a simple like logistic regression](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m43s)
00:23:43

[which is as good as pretty much any](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m46s)
00:23:46

[random first if you know ahead of time](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m49s)
00:23:49

[exactly what variables you need exactly](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m51s)
00:23:51

[how they interact exactly how they need](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m54s)
00:23:54

[to be transformed and so forth right so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m56s)
00:23:56

[in this case for example we could have](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h23m58s)
00:23:58

[created a new field which was equal to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m00s)
00:24:00

[year made as a sale date or sale year -](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m03s)
00:24:03

[year made and we could have fed that to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m07s)
00:24:07

[a model and got you know got that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m09s)
00:24:09

[interaction for us but the point is we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m12s)
00:24:12

[never know that like you never like you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m16s)
00:24:16

[might have a guess of it I think some of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m18s)
00:24:18

[these things are interacted in this way](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m20s)
00:24:20

[and I think this thing we need to take](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m21s)
00:24:21

[the log and so forth but you know the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m23s)
00:24:23

[truth is that the way the world works](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m26s)
00:24:26

[the causal structures you know they've](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m29s)
00:24:29

[got many many things interacting in many](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m30s)
00:24:30

[many subtle ways right and so that's why](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m33s)
00:24:33

[using trees whether it be gradient](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m35s)
00:24:35

[boosting machines or random forests](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m38s)
00:24:38

[works so well so can you pass that to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m40s)
00:24:40

[Terrance please one thing that bit me](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m44s)
00:24:44

[years ago was also I tried that doing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m50s)
00:24:50

[one variable at a time thinking oh well](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m55s)
00:24:55

[I'll figure out which one's most](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m57s)
00:24:57

[correlated with the dependent variable](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h24m58s)
00:24:58

[but what it doesn't pull apart is that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m00s)
00:25:00

[what if all variables are basically](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m04s)
00:25:04

[copied the same variable then they're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m06s)
00:25:06

[all going to seem equally important but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m08s)
00:25:08

[in fact it's really just one factor yeah](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m10s)
00:25:10

[and that's also true here so if we had](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m14s)
00:25:14

[like a column appeared twice right then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m16s)
00:25:16

[shuffling that column isn't going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m22s)
00:25:22

[make the model much worse right there'll](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m24s)
00:25:24

[be if you think about like how it was](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m27s)
00:25:27

[built](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m28s)
00:25:28

[some of the times particularly if we had](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m29s)
00:25:29

[like max features is 0.5 and some of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m31s)
00:25:31

[times we're going to get version a of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m34s)
00:25:34

[the column some of the time to get going](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m36s)
00:25:36

[to get version B of the column so like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m37s)
00:25:37

[half the time shuffling version a of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m39s)
00:25:39

[column is going to make a tree a bit](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m43s)
00:25:43

[worse half the time it's going to make](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m45s)
00:25:45

[you know column B you'll make it a bit](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m46s)
00:25:46

[worse and so it'll show that both of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m47s)
00:25:47

[those features are somewhat important](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m50s)
00:25:50

[and it'll kind of like share the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m54s)
00:25:54

[importance between the two features and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m56s)
00:25:56

[so this is why a reco linearity but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h25m58s)
00:25:58

[collinearity literally means that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m04s)
00:26:04

[they're linearly related so this isn't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m05s)
00:26:05

[quite right but this is why having two](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m08s)
00:26:08

[variables that are related closely](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m11s)
00:26:11

[related to each other or more variables](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m13s)
00:26:13

[that are closely related to each other](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m15s)
00:26:15

[means that you will often underestimate](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m16s)
00:26:16

[their importance using this this random](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m20s)
00:26:20

[first technique um yes](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m22s)
00:26:22

[Terrence and so once we've shuffled and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m26s)
00:26:26

[we get a new model what exactly are the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m29s)
00:26:29

[units of these importances is this a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m33s)
00:26:33

[change in the R squared yeah I mean it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m35s)
00:26:35

[depends on the library we're using so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m38s)
00:26:38

[the units are kind of like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m40s)
00:26:40

[I never think about them I kind of know](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m43s)
00:26:43

[that like in this particular library](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m46s)
00:26:46

[you know 0.005 is often kind of a cutoff](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m49s)
00:26:49

[I would tend to use but all I actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m52s)
00:26:52

[care about is is this picture right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m53s)
00:26:53

[which is the feature importance ordered](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h26m57s)
00:26:57

[for each variable and then kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m02s)
00:27:02

[zooming in turning into a bar plot and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m04s)
00:27:04

[I'm kind of like okay you know here](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m06s)
00:27:06

[they're all pretty flat and I can see](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m09s)
00:27:09

[okay that's about 0.05 and so I removed](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m12s)
00:27:12

[them at that point and just see like the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m15s)
00:27:15

[model hopefully the validation score](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m18s)
00:27:18

[didn't get worse and if it did get worse](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m20s)
00:27:20

[I'll just increase this a little bit so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m22s)
00:27:22

[I decrease this a little bit until it it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m24s)
00:27:24

[doesn't get worse so yeah the units of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m26s)
00:27:26

[measure of this don't matter too much](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m31s)
00:27:31

[and we'll learn later about a second way](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m33s)
00:27:33

[of doing variable importance by the way](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m36s)
00:27:36

[can you pass that over there](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m38s)
00:27:38

[is one of the goals here to remove](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m42s)
00:27:42

[variables that I guess your state your](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m45s)
00:27:45

[score will not get worse if you remove](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m51s)
00:27:51

[them so you might as well get rid of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m55s)
00:27:55

[them yeah so that's what we're going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m57s)
00:27:57

[do next so so what having looked at our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h27m58s)
00:27:58

[feature importance plot we said okay it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m02s)
00:28:02

[looks like the ones like less than 0.005](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m05s)
00:28:05

[you know that kind of this long tail of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m08s)
00:28:08

[boringness so I said let's try removing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m11s)
00:28:11

[them right so let's just try grabbing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m15s)
00:28:15

[the columns where it's greater than](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m17s)
00:28:17

[0.005 and I said let's create a new data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m18s)
00:28:18

[frame called DF keep which is DF train](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m21s)
00:28:21

[with just those cap columns create a new](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m24s)
00:28:24

[training and validation set with just](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m28s)
00:28:28

[those columns created a new random](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m30s)
00:28:30

[forest and I looked see how the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m31s)
00:28:31

[validation set score and the validation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m35s)
00:28:35

[set our MSC changed and I found they got](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m37s)
00:28:37

[a tiny bit better so if they're about](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m41s)
00:28:41

[the same or a tiny bit better than the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m44s)
00:28:44

[thinking my thinking is well this is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m46s)
00:28:46

[just as good a model but it's now](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m48s)
00:28:48

[simpler and so now when I redo the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m51s)
00:28:51

[feature importance there's less](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m53s)
00:28:53

[collinearity right and so in this case I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m55s)
00:28:55

[saw that year maid went from being like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h28m59s)
00:28:59

[quite a bit better than the next best](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m02s)
00:29:02

[thing which was couple system - way](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m04s)
00:29:04

[better than the next best thing okay and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m08s)
00:29:08

[coupler system went from being like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m10s)
00:29:10

[quite a bit more important than the next](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m13s)
00:29:13

[two - equally important to the next two](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m15s)
00:29:15

[so it did seem to definitely change](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m19s)
00:29:19

[these feature importances and hopefully](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m22s)
00:29:22

[give me some more insight there](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m23s)
00:29:23

[so how did that help our model in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m29s)
00:29:29

[general look what does it mean that your](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m34s)
00:29:34

[maid is no way yeah so we're going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m35s)
00:29:35

[dig into that kind of now but basically](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m38s)
00:29:38

[it tells us that for example if we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m42s)
00:29:42

[looking for like how we're dealing with](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m47s)
00:29:47

[missing values is there noise and the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m50s)
00:29:50

[data you know it's a high cardinality](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m52s)
00:29:52

[categorical variable they're all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m56s)
00:29:56

[different steps we would take so for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m58s)
00:29:58

[example if it was a high cardinality](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h29m59s)
00:29:59

[categorical variable that was originally](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m01s)
00:30:01

[a string right like for example I think](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m03s)
00:30:03

[like maybe fi product class description](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m06s)
00:30:06

[I remember one of the ones we looked at](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m09s)
00:30:09

[the other day he had like first of all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m12s)
00:30:12

[was the type of vehicle and then a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m14s)
00:30:14

[hyphen and then like the size of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m15s)
00:30:15

[vehicle we might look at that and be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m16s)
00:30:16

[like okay well that was an important](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m18s)
00:30:18

[column let's try like splitting it into](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m20s)
00:30:20

[two on - and then take that bit which is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m22s)
00:30:22

[like a size of it and trying you know](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m25s)
00:30:25

[posit and convert convert it into an](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m26s)
00:30:26

[integer you know we can try and do some](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m28s)
00:30:28

[feature engineering and basically until](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m30s)
00:30:30

[you know which ones are important you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m32s)
00:30:32

[don't know where to focus that feature](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m35s)
00:30:35

[engineering time you can talk to your](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m36s)
00:30:36

[client you know and say you know or you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m39s)
00:30:39

[know and if you're doing this inside](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m42s)
00:30:42

[your workplace you go and talk to the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m43s)
00:30:43

[folks that like we're responsible for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m46s)
00:30:46

[creating this data so in this if you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m48s)
00:30:48

[were actually working at a bulldozer](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m51s)
00:30:51

[auction company you might now go to the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m53s)
00:30:53

[actual auctioneers and say I'm really](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m56s)
00:30:56

[surprised that couply system seems to be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h30m58s)
00:30:58

[driving people's pricing decisions so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m00s)
00:31:00

[much why do you think that might be and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m02s)
00:31:02

[they can say to you oh it's actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m05s)
00:31:05

[because only these classes of vehicles](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m07s)
00:31:07

[have capital systems or only this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m09s)
00:31:09

[manufacturer has couple of systems and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m12s)
00:31:12

[so frankly this is actually not telling](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m14s)
00:31:14

[you about couple of systems but about](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m17s)
00:31:17

[something else and oh hey that reminds](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m18s)
00:31:18

[me that's that that's something else we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m20s)
00:31:20

[actually have measured that it's in this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m22s)
00:31:22

[different CSV file I'll go get it for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m25s)
00:31:25

[you but kind of helps you focus your](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m27s)
00:31:27

[attention](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m30s)
00:31:30

[so I hello](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m33s)
00:31:33

[little problem this weekend as you know](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m34s)
00:31:34

[I introduced a couple of crazy](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m36s)
00:31:36

[computations in into my random forest](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m39s)
00:31:39

[and all of a sudden they're like oh my](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m42s)
00:31:42

[god these are the most important](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m44s)
00:31:44

[variables ever squashing all of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m45s)
00:31:45

[others but then I got a terrible score](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m47s)
00:31:47

[and then is that because now that I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m49s)
00:31:49

[think I have my scores computed](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m52s)
00:31:52

[correctly what I noticed is that the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m55s)
00:31:55

[importance went through the roof but the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m56s)
00:31:56

[validation set was still bad or got](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h31m59s)
00:31:59

[worse is that because somehow that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m03s)
00:32:03

[computation allow the training to almost](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m05s)
00:32:05

[like an identifier map exactly what the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m10s)
00:32:10

[answer was going to be for training but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m12s)
00:32:12

[of course that doesn't generalize to the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m15s)
00:32:15

[validation set is that what is that what](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m18s)
00:32:18

[I observed okay so this there's two](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m19s)
00:32:19

[reasons why your validation score might](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m23s)
00:32:23

[not be very good um let's go up here](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m27s)
00:32:27

[okay so we got these five numbers right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m36s)
00:32:36

[the rmse of the training validation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m40s)
00:32:40

[r-squared of the training validation and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m45s)
00:32:45

[the r-squared of the oeob okay so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m48s)
00:32:48

[there's two reasons and really in the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m51s)
00:32:51

[end what we care about like for this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m53s)
00:32:53

[Cargill competition is the rmse of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m55s)
00:32:55

[validation set assuming we've created a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m57s)
00:32:57

[good validation set](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h32m59s)
00:32:59

[so an Terrance's case he's saying this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m01s)
00:33:01

[number is this thing I care about got](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m04s)
00:33:04

[worse when I did some feature](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m07s)
00:33:07

[engineering why is that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m09s)
00:33:09

[okay there's two possible reasons reason](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m10s)
00:33:10

[one is that you're overfitting if you're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m15s)
00:33:15

[overfeeding](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m18s)
00:33:18

[then your mobiie will also get worse if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m19s)
00:33:19

[you're doing a huge data set with a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m25s)
00:33:25

[small set RF sample so you can't use a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m28s)
00:33:28

[know a B then instead create a second](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m30s)
00:33:30

[validation set which is a random sample](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m33s)
00:33:33

[okay and and do that right so in other](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m35s)
00:33:35

[words if your OB or your random sample](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m40s)
00:33:40

[validation set is has got much worse](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m42s)
00:33:42

[then you must be overfitting](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m45s)
00:33:45

[I think in your case Terrence it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m49s)
00:33:49

[unlikely that's the problem because](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m53s)
00:33:53

[random forests](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m55s)
00:33:55

[don't over fit that badly like it's very](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h33m57s)
00:33:57

[hard to get them to overfit that badly](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m00s)
00:34:00

[unless you use some really weird](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m02s)
00:34:02

[parameters like only one estimator for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m05s)
00:34:05

[example like once we've got ten trees in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m08s)
00:34:08

[there there should be enough variation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m10s)
00:34:10

[that you're you know you can definitely](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m12s)
00:34:12

[over fit but not so much that you're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m14s)
00:34:14

[going to destroy your validation score](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m16s)
00:34:16

[by adding a variable so I'd think you'll](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m17s)
00:34:17

[find that's probably not the case but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m20s)
00:34:20

[it's easy to check and if it's not the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m22s)
00:34:22

[case](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m24s)
00:34:24

[then you'll see that your oob score or](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m25s)
00:34:25

[your random sample validation score](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m27s)
00:34:27

[hasn't got worse okay so the second](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m28s)
00:34:28

[reason your validation score can get](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m32s)
00:34:32

[worse if your mobiie score hasn't got](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m34s)
00:34:34

[worse you're not overfitting but your](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m36s)
00:34:36

[validation score is got worse that means](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m38s)
00:34:38

[you're you're doing something that is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m41s)
00:34:41

[true in the training set but not true in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m43s)
00:34:43

[the validation set so this can only](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m47s)
00:34:47

[happen when your validation set is not a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m50s)
00:34:50

[random sample so for example in this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m53s)
00:34:53

[bulldozes competition or in the grocery](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m56s)
00:34:56

[shopping competition we've intentionally](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h34m59s)
00:34:59

[made a validation set that's for a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m00s)
00:35:00

[different date range it's for the most](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m02s)
00:35:02

[recent two weeks right and so if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m04s)
00:35:04

[something different happened in the last](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m07s)
00:35:07

[two weeks to the previous weeks then you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m10s)
00:35:10

[could totally break your validation set](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m15s)
00:35:15

[so for example if there was some kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m18s)
00:35:18

[unique identifier which is like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m22s)
00:35:22

[different in the to date periods then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m27s)
00:35:27

[you could learn to identify things using](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m30s)
00:35:30

[that identifier in the training set but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m32s)
00:35:32

[then like the last two weeks may have a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m34s)
00:35:34

[totally different set of ID's or the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m36s)
00:35:36

[different set of behavior could get a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m38s)
00:35:38

[lot worse yeah what you're describing is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m40s)
00:35:40

[not common though and so I'm a bit](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m45s)
00:35:45

[skeptical it might be a bug but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m48s)
00:35:48

[hopefully there's enough things you can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m52s)
00:35:52

[now use to figure out if it is about](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m55s)
00:35:55

[will be interested to hear what you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m56s)
00:35:56

[learned](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h35m58s)
00:35:58

[okay so that's that's feature importance](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m00s)
00:36:00

[and so I'd like to compare that to how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m05s)
00:36:05

[feature importance is normally done in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m10s)
00:36:10

[industry and in academic communities](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m14s)
00:36:14

[outside of machine learning like in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m18s)
00:36:18

[psychology and economics and so forth](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m20s)
00:36:20

[and generally speaking people in those](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m22s)
00:36:22

[kind of environments tend to use some](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m24s)
00:36:24

[kind of linear regression logistic](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m27s)
00:36:27

[regression general linear models so they](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m28s)
00:36:28

[start with their data set and they](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m32s)
00:36:32

[basically say that was weird](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m34s)
00:36:34

[oh okay so they start with their data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m38s)
00:36:38

[set and they say I'm going to assume](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m41s)
00:36:41

[that I know the kind of parametric](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m44s)
00:36:44

[relationship between my independent](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m47s)
00:36:47

[variables and my dependent variable so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m50s)
00:36:50

[I'm going to assume that it's a linear](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m52s)
00:36:52

[relationship say or it's a linear](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m54s)
00:36:54

[relationship with a link function like a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m56s)
00:36:56

[sigmoid to create logistic regression](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h36m58s)
00:36:58

[say and so assuming that I already know](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m01s)
00:37:01

[that I can now write this as an equation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m04s)
00:37:04

[so if I've got like x1 x2 so forth right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m06s)
00:37:06

[I can say all right my Y values are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m09s)
00:37:09

[equal to ax 1 plus BX 2 equals y and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m12s)
00:37:12

[therefore I can find out the feature](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m20s)
00:37:20

[importance easily enough by just looking](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m22s)
00:37:22

[at these coefficients and saying like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m24s)
00:37:24

[which one's the highest particularly if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m27s)
00:37:27

[you've normalized the data first right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m29s)
00:37:29

[so there's this kind of trope out there](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m31s)
00:37:31

[it's it's very common which is that like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m35s)
00:37:35

[this is somehow more accurate or more](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m38s)
00:37:38

[pure or in some way better way of doing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m43s)
00:37:43

[feature importance but that couldn't be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m46s)
00:37:46

[further from the truth right if you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m49s)
00:37:49

[think about it if you were like if you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m51s)
00:37:51

[were missing an interaction right or if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m54s)
00:37:54

[you were missing a transformation you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m57s)
00:37:57

[needed or if you have any way being](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h37m59s)
00:37:59

[anything less than a hundred percent](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m03s)
00:38:03

[perfect in all of your pre-processing so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m05s)
00:38:05

[that your model is the absolute correct](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m08s)
00:38:08

[truth of this situation right unless](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m11s)
00:38:11

[you've got all of that correct then your](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m13s)
00:38:13

[coefficients are wrong right your](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m15s)
00:38:15

[coefficients are telling you in you're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m17s)
00:38:17

[totally wrong model this is how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m19s)
00:38:19

[important those things are right which](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m21s)
00:38:21

[is basically meaningless so where else](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m23s)
00:38:23

[do the random forest feature importance](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m27s)
00:38:27

[it's telling you in this extremely high](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m30s)
00:38:30

[parameter highly flexible functional](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m33s)
00:38:33

[form with few if any statistical](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m36s)
00:38:36

[assumptions this is your future](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m37s)
00:38:37

[importance right so I would be very](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m39s)
00:38:39

[cautious you know and and again I can't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m44s)
00:38:44

[stress this enough when you when you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m46s)
00:38:46

[leave ence and when you leave this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m48s)
00:38:48

[program you are much more often going](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m50s)
00:38:50

[see people talk about logistic](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m52s)
00:38:52

[regression coefficients then you're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m54s)
00:38:54

[going to see them talk about random](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m56s)
00:38:56

[first variable importance and every time](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m57s)
00:38:57

[you see that happen you should be very](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h38m59s)
00:38:59

[very very skeptical of what you're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m00s)
00:39:00

[seeing anytime you read a paper in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m03s)
00:39:03

[economics or in psychology or the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m04s)
00:39:04

[marketing department tells you that this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m06s)
00:39:06

[regression or whatever every single time](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m08s)
00:39:08

[those coefficients are going to be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m11s)
00:39:11

[massively biased by any issues in the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m13s)
00:39:13

[model furthermore if they've done so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m17s)
00:39:17

[much pre-processing that actually the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m22s)
00:39:22

[model is pretty accurate then now you're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m25s)
00:39:25

[looking at coefficients that are going](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m27s)
00:39:27

[to be of like a coefficient of some](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m29s)
00:39:29

[principal component from a CA or a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m31s)
00:39:31

[coefficient of some distance from some](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m33s)
00:39:33

[cluster or something](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m36s)
00:39:36

[at which point they're very very hard to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m37s)
00:39:37

[interpret anyway they're not actual](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m40s)
00:39:40

[variables right so they're kind of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m41s)
00:39:41

[two options I've seen when people try to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m43s)
00:39:43

[use classic statistical techniques to do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m45s)
00:39:45

[recover a variable importance equivalent](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m49s)
00:39:49

[I think things are starting to change](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m53s)
00:39:53

[slowly you know there there are some](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h39m58s)
00:39:58

[fields that are starting to realize that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m00s)
00:40:00

[this is totally the wrong way to do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m02s)
00:40:02

[things but it's been you know nearly 20](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m03s)
00:40:03

[years since random forests appeared so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m07s)
00:40:07

[it takes a long time you know people say](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m09s)
00:40:09

[that the only way that knowledge really](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m12s)
00:40:12

[advances is when the previous generation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m14s)
00:40:14

[dies and that's kind of true right like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m16s)
00:40:16

[particularly academics you know they](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m18s)
00:40:18

[make a career of being good at a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m20s)
00:40:20

[particular sub thing and you know often](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m22s)
00:40:22

[don't if you know it's not until the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m26s)
00:40:26

[next generation comes along that that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m28s)
00:40:28

[people notice that oh that's actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m31s)
00:40:31

[longer no good way to do things and I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m32s)
00:40:32

[think that's what's happened here okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m35s)
00:40:35

[so we've got now a model which isn't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m39s)
00:40:39

[really any better as a predictive](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m43s)
00:40:43

[accuracy wise but it's kind of we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m44s)
00:40:44

[getting a good sense that there seems to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m47s)
00:40:47

[be like four main important things when](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m48s)
00:40:48

[it was made the capital system its size](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m52s)
00:40:52

[and its product classification okay so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m54s)
00:40:54

[that's cool there is something else that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h40m58s)
00:40:58

[we can do however which is we can do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m02s)
00:41:02

[something called one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m05s)
00:41:05

[hot encoding so this is going to where](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m06s)
00:41:06

[we're talking about categorical](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m09s)
00:41:09

[variables so remember a categorical](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m10s)
00:41:10

[variable let's say we had like a string](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m12s)
00:41:12

[high and remember the order we got was](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m18s)
00:41:18

[kind of back weird it was high low](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m22s)
00:41:22

[medium so it was in alphabetical order](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m25s)
00:41:25

[by default right was their original](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m27s)
00:41:27

[category for like usage banned or](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m30s)
00:41:30

[something](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m32s)
00:41:32

[and so we mapped it to 0 1 2 right and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m33s)
00:41:33

[so by the time it gets into our data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m38s)
00:41:38

[frame it's now a number so the random](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m40s)
00:41:40

[forest doesn't know that it was](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m43s)
00:41:43

[originally a category it's just a number](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m46s)
00:41:46

[right so when the random forest is built](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m48s)
00:41:48

[it basically says oh is it greater than](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m50s)
00:41:50

[1 or not or is it greater than naught or](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m53s)
00:41:53

[not you know basically the two possible](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m56s)
00:41:56

[decisions it could have made for for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h41m58s)
00:41:58

[something with like five or six bands](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m07s)
00:42:07

[you know it could be that just one of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m09s)
00:42:09

[the levels of a category is actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m12s)
00:42:12

[interesting right so like if it was like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m14s)
00:42:14

[very high very low or unknown right then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m17s)
00:42:17

[we know that like six levels and maybe](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m26s)
00:42:26

[the only thing that mattered was whether](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m28s)
00:42:28

[it was like unknown maybe like not](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m30s)
00:42:30

[nothing it's sighs somehow impacts the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m32s)
00:42:32

[price and so if we wanted to be able to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m34s)
00:42:34

[recognize that and particularly if like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m37s)
00:42:37

[it just so happened that the way that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m39s)
00:42:39

[the numbers were coded was it unknown](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m41s)
00:42:41

[ended up in the middle right then what](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m44s)
00:42:44

[it's going to do is it's going to say](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m49s)
00:42:49

[okay there is a difference between these](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m50s)
00:42:50

[two groups you know less than or equal](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m52s)
00:42:52

[to two versus greater than two and then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m54s)
00:42:54

[when it gets into this this leaf here](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m57s)
00:42:57

[it's going to say oh there's a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h42m59s)
00:42:59

[difference between these two between](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m00s)
00:43:00

[less than four and greater than or equal](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m02s)
00:43:02

[to four and since going to take two](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m04s)
00:43:04

[splits to get to the point where we can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m06s)
00:43:06

[see that it's actually unknown that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m09s)
00:43:09

[matters so this is a little inefficient](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m12s)
00:43:12

[and we're kind of like wasting tree](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m15s)
00:43:15

[computation and like wasting tree](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m17s)
00:43:17

[computation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m19s)
00:43:19

[because every time we do a split we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m20s)
00:43:20

[having the amount of data at least that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m22s)
00:43:22

[we have to do more analysis so it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m23s)
00:43:23

[going to make our tree less rich less](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m26s)
00:43:26

[effective if we're not giving the data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m29s)
00:43:29

[in a way that's kind of convenient for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m32s)
00:43:32

[it to do the work it needs to do so what](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m34s)
00:43:34

[we could do instead is create six](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m38s)
00:43:38

[columns we could create a column cord is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m44s)
00:43:44

[very high is very low is high is unknown](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m47s)
00:43:47

[is low is medium and h1 would be ones](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m52s)
00:43:52

[and zeros right so the one or a zero so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h43m57s)
00:43:57

[we had six columns this one moment](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m04s)
00:44:04

[so having added six additional columns](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m08s)
00:44:08

[to our data set the random first now has](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m12s)
00:44:12

[the ability to pick one of these and say](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m17s)
00:44:17

[like oh let's have a look at is unknown](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m19s)
00:44:19

[there's one possible fit I can do which](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m21s)
00:44:21

[is one versus zero let's see if that's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m24s)
00:44:24

[any good right so it actually now has](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m26s)
00:44:26

[the ability in a single step to pull out](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m27s)
00:44:27

[a single category level and so this this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m30s)
00:44:30

[kind of coding is called one-hot](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m36s)
00:44:36

[encoding and for many many types of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m39s)
00:44:39

[machine learning model this is like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m44s)
00:44:44

[necessary something like this is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m47s)
00:44:47

[necessary like if you are doing logistic](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m50s)
00:44:50

[regression](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m52s)
00:44:52

[you can't possibly put in a categorical](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m52s)
00:44:52

[variable that goes not through five](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m54s)
00:44:54

[because there's obviously no written](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m56s)
00:44:56

[linear relationship between that and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m58s)
00:44:58

[anything right so one part encoding a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h44m59s)
00:44:59

[lot of people incorrectly assume that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m03s)
00:45:03

[all machine learning requires one pod](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m05s)
00:45:05

[encoding but in this case I'm going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m08s)
00:45:08

[show you how we could use it optionally](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m10s)
00:45:10

[and see whether it might improve things](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m12s)
00:45:12

[sometimes yeah](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m14s)
00:45:14

[hi Jeremy so we have six categories like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m16s)
00:45:16

[in this case would there would be any](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m19s)
00:45:19

[problems with adding a column for each](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m21s)
00:45:21

[of the categories Oh Chris in linear](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m24s)
00:45:24

[regression we saw we had to do it like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m27s)
00:45:27

[if there's six categories we should only](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m29s)
00:45:29

[do it for five of them yeah so um](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m30s)
00:45:30

[it you certainly can say oh let's not](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m34s)
00:45:34

[worry about adding is medium because we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m37s)
00:45:37

[can infer it from the other five I would](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m40s)
00:45:40

[say include it anyway because like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m45s)
00:45:45

[rather than otherwise the random forest](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m49s)
00:45:49

[would have to say is very high know is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m52s)
00:45:52

[very low know is high know is unknown](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m55s)
00:45:55

[mode is low know okay and finally on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m57s)
00:45:57

[there right so it's like five decisions](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h45m59s)
00:45:59

[to get to that point so the reason in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m01s)
00:46:01

[linear models that you need to not](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m07s)
00:46:07

[include one is because linear models](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m10s)
00:46:10

[hate collinearity but we don't care](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m12s)
00:46:12

[about about that here so we can do one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m15s)
00:46:15

[hot encoding easily enough and the way](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m21s)
00:46:21

[we do it is we pass one extra parameter](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m24s)
00:46:24

[to proc DF which is what's the max](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m29s)
00:46:29

[number of categories right so if we say](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m33s)
00:46:33

[it's seven then anything with less than](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m38s)
00:46:38

[seven levels is going to be turned into](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m41s)
00:46:41

[a one hot encoded bunch of columns right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m44s)
00:46:44

[so in this case this has got six levels](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m48s)
00:46:48

[so this would be one hot encoded where](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m50s)
00:46:50

[else like zip code has more than six](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m53s)
00:46:53

[levels and so that would be left as a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m55s)
00:46:55

[number and so generally speaking you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m57s)
00:46:57

[obviously probably wouldn't want a one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h46m59s)
00:46:59

[hot in code zip code right because](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m01s)
00:47:01

[that's just going to create masses of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m03s)
00:47:03

[data memory problems computation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m05s)
00:47:05

[problems and so forth right so so this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m07s)
00:47:07

[is like another parameter that you can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m10s)
00:47:10

[play around with so if I do that try it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m12s)
00:47:12

[out run the random forest as per usual](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m18s)
00:47:18

[you can see what happens to the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m20s)
00:47:20

[r-squared of the validation set and to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m23s)
00:47:23

[the rmse of the validation set and in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m26s)
00:47:26

[this case I found it got a little bit](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m28s)
00:47:28

[worse this isn't always the case and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m30s)
00:47:30

[it's going to depend on your data set](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m34s)
00:47:34

[you know do you have a data set where](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m36s)
00:47:36

[you know single categories tend to be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m37s)
00:47:37

[quite important or not in this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m40s)
00:47:40

[particular case it didn't make it more](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m43s)
00:47:43

[predictive how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m46s)
00:47:46

[what it did do is that we now have](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m48s)
00:47:48

[different features right so proc TF puts](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m51s)
00:47:51

[the name of the variable and then an](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m54s)
00:47:54

[underscore and then the level name and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m56s)
00:47:56

[so interestingly it turns out that where](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h47m58s)
00:47:58

[else before it said that enclosure was](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m02s)
00:48:02

[somewhat important when we do it as one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m06s)
00:48:06

[hot encoded it actually says enclosure](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m09s)
00:48:09

[erupts with AC is the most important](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m12s)
00:48:12

[thing so for at least the purpose of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m15s)
00:48:15

[like interpreting your model you should](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m19s)
00:48:19

[always try one hot encoding you know](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m21s)
00:48:21

[quite a few of your variables and so I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m26s)
00:48:26

[often find somewhere around six or seven](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m28s)
00:48:28

[is pretty good you can try like making](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m30s)
00:48:30

[that number as high as you can so that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m34s)
00:48:34

[it doesn't take forever to compute and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m37s)
00:48:37

[the feature importance doesn't include](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m39s)
00:48:39

[like really tiny levels that aren't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m41s)
00:48:41

[interesting so that's kind of up to you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m45s)
00:48:45

[to play it play around with but in this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m46s)
00:48:46

[case like this is actually I found this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m50s)
00:48:50

[very interesting it clearly tells me I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m53s)
00:48:53

[need to find out what enclosure erupts](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m55s)
00:48:55

[with AC is why is it important because](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h48m58s)
00:48:58

[like means nothing to me right and but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m02s)
00:49:02

[it's the most important thing so I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m05s)
00:49:05

[should go figure that out so then I had](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m07s)
00:49:07

[a question you plus it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m09s)
00:49:09

[so can you explain how changing the max](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m15s)
00:49:15

[number of categories worse because for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m18s)
00:49:18

[me it just seems like there's five](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m20s)
00:49:20

[categories or site categories oh yeah](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m21s)
00:49:21

[sorry so it's it's just like all it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m23s)
00:49:23

[doing is saying like okay here's a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m28s)
00:49:28

[column called zip code here's a column](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m30s)
00:49:30

[called usage band and here's a column](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m33s)
00:49:33

[sex right I don't know whatever right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m39s)
00:49:39

[and so like zip code has whatever five](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m42s)
00:49:42

[thousand levels the number of levels in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m45s)
00:49:45

[a category we call its cardinality okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m48s)
00:49:48

[so it has a cardinality of five thousand](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m53s)
00:49:53

[usage banned maybe has a cardinality of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m56s)
00:49:56

[six sex has maybe a cardinality of - so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h49m58s)
00:49:58

[when proc TF goes through and it says](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m01s)
00:50:01

[okay this is a categorical variable](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m03s)
00:50:03

[should i one-hot encode it it checks the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m06s)
00:50:06

[cardinality against max and hats and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m10s)
00:50:10

[says all five thousand is bigger than](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m13s)
00:50:13

[seven so I don't one hot encoder and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m15s)
00:50:15

[then it goes to usage band 6 is less](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m18s)
00:50:18

[than 7 I do one hot encode it goes to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m21s)
00:50:21

[sex 2 is less than 7 I do want to encode](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m24s)
00:50:24

[it so it just says for each variable how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m26s)
00:50:26

[do I decide whether the one hot encoded](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m30s)
00:50:30

[or not we are keeping legal in cause no](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m32s)
00:50:32

[once we decide to one hot in code it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m38s)
00:50:38

[does not keep the original variable](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m39s)
00:50:39

[maybe the best will be an interval well](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m47s)
00:50:47

[you don't need a labeling code if the if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m53s)
00:50:53

[so if the best is an interval it can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m55s)
00:50:55

[approximate that with multiple one hot](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m57s)
00:50:57

[encoding levels yeah so like you know](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h50m59s)
00:50:59

[it's a the the truth is that each column](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m04s)
00:51:04

[is going to have some you know different](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m09s)
00:51:09

[you know should it be label encoded or](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m12s)
00:51:12

[not you know which you could make on a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m15s)
00:51:15

[case-by-case basis I find in practice](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m16s)
00:51:16

[it's just not that sensitive to this and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m21s)
00:51:21

[so I find like just using a single](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m23s)
00:51:23

[number for the whole data set gives me](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m26s)
00:51:26

[what I need but you know if you were](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m28s)
00:51:28

[building a model that really had to be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m31s)
00:51:31

[as awesome as possible and you had lots](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m34s)
00:51:34

[and lots of time to do it you can go](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m36s)
00:51:36

[through men you know don't use property](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m38s)
00:51:38

[if you can go through manually and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m39s)
00:51:39

[decide which things to use dummies or](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m40s)
00:51:40

[not your you'll see in the code if you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m43s)
00:51:43

[look at the code for property F Rock D F](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m47s)
00:51:47

[right like I never want you to feel like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m52s)
00:51:52

[the code that happens to be in the fast](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m56s)
00:51:56

[AI library is the code that you're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h51m58s)
00:51:58

[limited to right so where is that done](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m00s)
00:52:00

[you can see that the max n cat gets](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m03s)
00:52:03

[passed to numerical eyes and numerical](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m11s)
00:52:11

[eyes simply checks okay is that a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m15s)
00:52:15

[numeric type and it's the number of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m22s)
00:52:22

[categories either not in pass to us at](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m24s)
00:52:24

[all or we've got more unique values than](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m27s)
00:52:27

[there are categories and if so we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m31s)
00:52:31

[going to use the categorical codes so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m32s)
00:52:32

[for any column where that's where it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m35s)
00:52:35

[skipped over that right so it's remained](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m38s)
00:52:38

[as a category then at the very end we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m40s)
00:52:40

[just go pandas get dummies we pass in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m42s)
00:52:42

[the whole data frame and so a pandas get](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m45s)
00:52:45

[that means you pass in a whole data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m47s)
00:52:47

[frame it checks for anything that's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m48s)
00:52:48

[still a categorical variable and it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m50s)
00:52:50

[turns it into a dummy variable which is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m52s)
00:52:52

[another way of saying a one-pot encoding](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m54s)
00:52:54

[so you know with that kind of approach](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m56s)
00:52:56

[you can easily override it into your own](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h52m57s)
00:52:57

[dummy verification variable ization did](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m01s)
00:53:01

[you have a question so some data has a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m05s)
00:53:05

[quite obvious order like if you have](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m11s)
00:53:11

[like a grading system like food bad or](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m13s)
00:53:13

[whatever things like that there's an](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m17s)
00:53:17

[order to that and showing that order by](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m20s)
00:53:20

[doing the dummy variable thing probably](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m23s)
00:53:23

[will your benefit so is there a way to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m25s)
00:53:25

[just force it to leave alone one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m29s)
00:53:29

[variable just like invert it or](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m31s)
00:53:31

[yourself not not in the library and to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m34s)
00:53:34

[remind you like unless we explicitly do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m40s)
00:53:40

[something about it we're not going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m43s)
00:53:43

[get that order so when we when we import](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m45s)
00:53:45

[the data so this is in Lesson one RF we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m51s)
00:53:51

[showed how by default the categories are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h53m59s)
00:53:59

[ordered alphabetically and we have the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m02s)
00:54:02

[ability to order them properly so yeah](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m05s)
00:54:05

[if you've actually made an effort to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m09s)
00:54:09

[turn your ordinal variables into proper](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m11s)
00:54:11

[ordinals using prop D F can destroy that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m14s)
00:54:14

[if you have max MCATs](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m22s)
00:54:22

[so the simple thing the simple way to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m24s)
00:54:24

[avoid that is if we know that we always](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m26s)
00:54:26

[want to use the codes for usage banned](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m29s)
00:54:29

[rather than the you know like never one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m31s)
00:54:31

[hot encoder you could just go ahead and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m35s)
00:54:35

[replace it right you could just say okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m37s)
00:54:37

[let's just go D F dot u s-- taband](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m39s)
00:54:39

[equals DF q suspend cat codes and it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m41s)
00:54:41

[now an integer and so it'll never get](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m44s)
00:54:44

[page all right so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m46s)
00:54:46

[we kind of already seen how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h54m57s)
00:54:57

[variables which are basically measuring](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m01s)
00:55:01

[the same thing can kind of confuse our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m04s)
00:55:04

[variable importance and there can also](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m07s)
00:55:07

[make our random forest slightly less](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m10s)
00:55:10

[good because it requires like more](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m12s)
00:55:12

[computation to do the same thing there's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m14s)
00:55:14

[more columns to check so I'm going to do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m16s)
00:55:16

[some more work to try and remove](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m20s)
00:55:20

[redundant features and the way I do that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m22s)
00:55:22

[is to do something called a dendrogram](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m25s)
00:55:25

[and it's a kind of hierarchical](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m28s)
00:55:28

[clustering so cluster analysis is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m31s)
00:55:31

[something where you're trying to look at](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m35s)
00:55:35

[objects they can be either rows in the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m37s)
00:55:37

[data set or columns and find which ones](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m39s)
00:55:39

[are similar to each other so often](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m41s)
00:55:41

[you'll see people particularly talking](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m44s)
00:55:44

[about cluster analysis they normally](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m46s)
00:55:46

[refer to rows of data and they'll say](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m47s)
00:55:47

[like oh let's plot it right and like oh](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m50s)
00:55:50

[there's a cluster and there's a cluster](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m53s)
00:55:53

[right a common type of cluster analysis](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m55s)
00:55:55

[time - permitting we may get around to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h55m59s)
00:55:59

[talking about this in some detail is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m01s)
00:56:01

[called k-means which is basically where](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m03s)
00:56:03

[you assume that you don't have any](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m07s)
00:56:07

[labels at all and you take basically a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m08s)
00:56:08

[couple of data points at random and you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m12s)
00:56:12

[gradually find the ones that are near to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m16s)
00:56:16

[it and move them closer and closer to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m18s)
00:56:18

[centroids and you kind of repeat it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m21s)
00:56:21

[again and again and it's an iterative](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m22s)
00:56:22

[approach that you basically tell how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m24s)
00:56:24

[many clusters you want and it'll tell](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m26s)
00:56:26

[you where it thinks that classes are I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m28s)
00:56:28

[really I don't know why but I really](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m31s)
00:56:31

[under use technique 20 30 years ago it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m34s)
00:56:34

[was much more popular than it is today](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m37s)
00:56:37

[is hierarchical clustering](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m39s)
00:56:39

[hierarchical also known as agglomerated](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m42s)
00:56:42

[clustering and in hierarchical order](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m47s)
00:56:47

[agglomerative clustering we basically](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m49s)
00:56:49

[look at every pair of option up every](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m51s)
00:56:51

[pair of objects and say okay which two](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m54s)
00:56:54

[objects are the closest alright so in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h56m57s)
00:56:57

[this case we might go okay those two](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m00s)
00:57:00

[objects are the closest and so we've](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m04s)
00:57:04

[kind of like delete them and replace it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m06s)
00:57:06

[with the midpoint of the two and then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m08s)
00:57:08

[okay here the next two closest if we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m10s)
00:57:10

[delete them and replace them with the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m12s)
00:57:12

[midpoint of the two and you keep doing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m13s)
00:57:13

[that again](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m15s)
00:57:15

[again right since we're kind of removing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m15s)
00:57:15

[points and replacing them with their](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m17s)
00:57:17

[averages you're gradually reducing a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m19s)
00:57:19

[number of points by pairwise combining](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m21s)
00:57:21

[and the cool thing is you can plot that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m24s)
00:57:24

[like so right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m27s)
00:57:27

[so if rather than looking at points you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m28s)
00:57:28

[look at variables we can say okay which](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m30s)
00:57:30

[two variables are the most similar it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m33s)
00:57:33

[says okay say year and sale elapsed](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m36s)
00:57:36

[they're very similar so the kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m37s)
00:57:37

[horizontal axis here is how similar are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m40s)
00:57:40

[the two points that are being compared](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m45s)
00:57:45

[right so if they're closer to the right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m46s)
00:57:46

[that means they're very similar so sale](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m48s)
00:57:48

[year and sale elapsed have been combined](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m50s)
00:57:50

[and they were very similar again it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m53s)
00:57:53

[like okay as you know it'll be like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m58s)
00:57:58

[correlation coefficient or something](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h57m59s)
00:57:59

[like that you know in this particular](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m02s)
00:58:02

[case what I actually did so you get to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m04s)
00:58:04

[tell it so in this case I actually used](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m07s)
00:58:07

[Spearman's R so you guys familiar with](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m10s)
00:58:10

[correlation coefficients already all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m15s)
00:58:15

[right so correlation is cut as almost](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m18s)
00:58:18

[exactly the same as the r-squared right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m20s)
00:58:20

[but it's between two variables rather](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m24s)
00:58:24

[than a variable and it's prediction the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m27s)
00:58:27

[problem with a normal correlation is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m30s)
00:58:30

[that if the I create a new workbook here](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m33s)
00:58:33

[if you have data that looks like this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m41s)
00:58:41

[then you can do a correlation and you'll](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m46s)
00:58:46

[get a good result right but if you've](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m49s)
00:58:49

[got data which looks like this right and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m51s)
00:58:51

[you try and do a correlation it assumes](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h58m58s)
00:58:58

[linearity that's not very good right so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m00s)
00:59:00

[there's a thing called a rank](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m03s)
00:59:03

[correlation a really simple idea](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m04s)
00:59:04

[it's replace every point by its rank](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m06s)
00:59:06

[right so instead of like so we basically](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m11s)
00:59:11

[say okay this is the smallest so we'll](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m14s)
00:59:14

[call that one - there's the next one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m16s)
00:59:16

[three is next one four five right so you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m19s)
00:59:19

[just replace every number by its rank](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m23s)
00:59:23

[and then you do the same for the y-axis](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m26s)
00:59:26

[so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m29s)
00:59:29

[that 1 2 3 and so forth right and so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m29s)
00:59:29

[then you do it like a new plot where you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m34s)
00:59:34

[don't plot the data but you plot the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m37s)
00:59:37

[rank of the data and if you think about](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m39s)
00:59:39

[it the rank of this data set is going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m41s)
00:59:41

[look an exact line because every time](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m44s)
00:59:44

[something was greater on the x-axis](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m47s)
00:59:47

[it was also greater on the y-axis so if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m49s)
00:59:49

[we do a correlation on the rank that's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m54s)
00:59:54

[called a rank correlation okay and so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=00h59m56s)
00:59:56

[because I want to find the columns that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m05s)
01:00:05

[are similar in a way that the random](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m08s)
01:00:08

[forest would find them similar random](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m10s)
01:00:10

[forests don't care about linearity they](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m13s)
01:00:13

[just care about ordering so a rank](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m15s)
01:00:15

[correlation is the the right way to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m17s)
01:00:17

[think about that so Spearman's are is is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m20s)
01:00:20

[the name of the most common rank](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m23s)
01:00:23

[correlation but you can literally](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m25s)
01:00:25

[replace the data with its rank and chuck](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m27s)
01:00:27

[it at the regular correlation and you'll](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m29s)
01:00:29

[get basically the same answer the only](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m31s)
01:00:31

[difference is in how ties are handled](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m33s)
01:00:33

[it's a pretty minor issue if you had](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m35s)
01:00:35

[like a full parabola in that rank](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m40s)
01:00:40

[correlation you'll will not write right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m43s)
01:00:43

[it has to be has to be monotonic yeah](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m47s)
01:00:47

[yeah](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m49s)
01:00:49

[okay so once I've got a correlation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h00m56s)
01:00:56

[matrix there's basically a couple of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m00s)
01:01:00

[standard steps you do to turn that into](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m02s)
01:01:02

[a dendogram which I have to look up on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m04s)
01:01:04

[stackoverflow each time I do it you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m08s)
01:01:08

[basically turn it into a distance matrix](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m11s)
01:01:11

[and then you create something that tells](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m13s)
01:01:13

[you you know which things are connected](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m15s)
01:01:15

[to which other things hierarchically so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m17s)
01:01:17

[this kind of these two and this step](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m19s)
01:01:19

[here like just three standard steps that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m23s)
01:01:23

[you always have to do to create a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m25s)
01:01:25

[dendogram and so then you can plot it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m27s)
01:01:27

[and so alright so say your and sell a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m33s)
01:01:33

[lot soon to be measuring basically the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m36s)
01:01:36

[same thing at least in terms of rank](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m38s)
01:01:38

[which is not surprising because they](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m40s)
01:01:40

[elapsed is the number of days since the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m41s)
01:01:41

[first day in my data set so obviously](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m45s)
01:01:45

[these two are nearly entirely correlated](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m48s)
01:01:48

[with some ties browser tracks and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m50s)
01:01:50

[hydraulics flow and coupla system all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m53s)
01:01:53

[seem to be measuring the same thing and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m55s)
01:01:55

[this is interesting because remember](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m57s)
01:01:57

[coupla system it said was super](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h01m58s)
01:01:58

[important right and so this rather](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m00s)
01:02:00

[supports our hypothesis there's nothing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m01s)
01:02:01

[to do with whether it's a coupler system](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m04s)
01:02:04

[but whether it's whatever kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m05s)
01:02:05

[vehicle it is it has these kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m07s)
01:02:07

[features product group and product](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m08s)
01:02:08

[groups desk seem to be measuring the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m12s)
01:02:12

[same thing if I base model on fi model](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m14s)
01:02:14

[desk seem to be measuring the same thing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m16s)
01:02:16

[and so once we get past that everything](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m17s)
01:02:17

[else like suddenly the things are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m21s)
01:02:21

[further away so I'm probably going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m23s)
01:02:23

[not worry about those so we're going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m25s)
01:02:25

[look into these one two three four](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m26s)
01:02:26

[groups that are very similar could you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m30s)
01:02:30

[pass that over there](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m32s)
01:02:32

[the citizen that grabbed that the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m39s)
01:02:39

[similarity between stick glint and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m42s)
01:02:42

[enclosure is higher than with stick lens](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m44s)
01:02:44

[and anything that's higher yeah pretty](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m47s)
01:02:47

[much I mean it it's a little hard to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m49s)
01:02:49

[interpret but given that stick length](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m51s)
01:02:51

[and enclosure don't join up until way](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m53s)
01:02:53

[over here yeah it would strongly suggest](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m55s)
01:02:55

[that then that they're a long way away](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h02m59s)
01:02:59

[from each other otherwise you would](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m01s)
01:03:01

[expect them we were joined up earlier I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m03s)
01:03:03

[mean it's it's possible to construct](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m04s)
01:03:04

[like a synthetic data set where you kind](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m06s)
01:03:06

[of end up joining things that were close](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m09s)
01:03:09

[to each other through different paths so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m11s)
01:03:11

[you've got to be a bit careful but I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m15s)
01:03:15

[think it's fair to is probably assume](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m16s)
01:03:16

[that stick length or enclosure are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m18s)
01:03:18

[probably very different so they are very](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m19s)
01:03:19

[different but would they be more similar](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m22s)
01:03:22

[than for example stick length and sale](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m24s)
01:03:24

[day of year no which is in a very top no](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m28s)
01:03:28

[there's nothing to suggest that here](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m33s)
01:03:33

[because like the key point is to notice](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m35s)
01:03:35

[where they sit in this tree right and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m36s)
01:03:36

[they both that they sit in totally](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m39s)
01:03:39

[different halves of the tree thank you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m41s)
01:03:41

[but really to actually know that the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m43s)
01:03:43

[best way would be to actually look at](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m45s)
01:03:45

[this p.m. and our correlation matrix and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m47s)
01:03:47

[if you just want to know how similar is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m50s)
01:03:50

[this thing or this thing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m52s)
01:03:52

[the Spearman our correlation matrix](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m53s)
01:03:53

[tells you that can you plus that over](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m55s)
01:03:55

[there](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h03m56s)
01:03:56

[so today's we are passing the leader](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m00s)
01:04:00

[cream right second we are passing the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m03s)
01:04:03

[cream this is just a data frame so we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m06s)
01:04:06

[passing in DF Cape so that's the data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m11s)
01:04:11

[frame containing the whatever it was 30](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m13s)
01:04:13

[or so features that our random forest](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m16s)
01:04:16

[thought was interesting](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m18s)
01:04:18

[so there's no random first being used](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m20s)
01:04:20

[here the measure the distance measure is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m22s)
01:04:22

[being done entirely on rent correlation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m24s)
01:04:24

[so what I then do is I take these these](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m28s)
01:04:28

[groups right and I create a little](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m31s)
01:04:31

[function that I call get out of fans](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m34s)
01:04:34

[score right which is it does a random](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m36s)
01:04:36

[forest for some data frame I make sure](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m38s)
01:04:38

[that I've taken that data frame and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m45s)
01:04:45

[split it into a training and validation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m46s)
01:04:46

[set and then I call fit and return the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m48s)
01:04:48

[oeob score right so basically what I'm](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m52s)
01:04:52

[going to do is I'm going to try removing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m55s)
01:04:55

[each one of these one two three four](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h04m57s)
01:04:57

[five six seven and eight nine or so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m00s)
01:05:00

[variables one at a time and see which](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m03s)
01:05:03

[ones I can remove and it doesn't make](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m06s)
01:05:06

[the oob score get worse and each time I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m08s)
01:05:08

[run this I get slightly different](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m13s)
01:05:13

[results so actually it looks like last](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m14s)
01:05:14

[time I had seven things not not eight](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m15s)
01:05:15

[things so you can see I just do a loop](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m17s)
01:05:17

[through each of the things that I'm](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m19s)
01:05:19

[thinking like maybe I could get rid of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m21s)
01:05:21

[this because it's redundant and I print](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m23s)
01:05:23

[out the column name and the oeob score](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m25s)
01:05:25

[of a model that is trained after](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m29s)
01:05:29

[dropping that one column okay so the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m31s)
01:05:31

[oeob score on my whole data frame is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m37s)
01:05:37

[point eight nine and then after dropping](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m39s)
01:05:39

[each one of these things](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m43s)
01:05:43

[they're basically none of them get much](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m47s)
01:05:47

[worse sale elapsed is getting quite a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m49s)
01:05:49

[bit worse than say all year but like it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m52s)
01:05:52

[looks like pretty much everything else I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m55s)
01:05:55

[can drop with like only like a third](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m56s)
01:05:56

[decimal place problem so obviously](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h05m58s)
01:05:58

[though you've got to remember the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m03s)
01:06:03

[dendogram let's take fi model discs and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m04s)
01:06:04

[Fi based model right they're very](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m07s)
01:06:07

[similar to each other right so what this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m09s)
01:06:09

[says isn't that I can get rid of both of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m11s)
01:06:11

[them right I can get rid of one of them](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m13s)
01:06:13

[because they're basically measuring the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m15s)
01:06:15

[same thing okay so so then I try it I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m18s)
01:06:18

[say okay let's try getting rid of one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m21s)
01:06:21

[from each group say oh yeah F by based](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m24s)
01:06:24

[model and grouse attracts okay and like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m26s)
01:06:26

[let's now have a look it's like okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m31s)
01:06:31

[I've gone from point eight nine oh two](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m32s)
01:06:32

[point eight eight eight it's like again](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m34s)
01:06:34

[so close as to be meaningless so that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m37s)
01:06:37

[sounds good simpler is better so I'm now](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m40s)
01:06:40

[going to drop those columns from my data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m44s)
01:06:44

[frame and then I can try running the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m48s)
01:06:48

[full model again and I can see you know](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m52s)
01:06:52

[so reset our air samples means I'm using](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m56s)
01:06:56

[my whole data frame my whole bootstrap](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h06m59s)
01:06:59

[sample used for tea estimators and I've](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m01s)
01:07:01

[got 0.90 seven okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m05s)
01:07:05

[so I've now got a model which is smaller](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m08s)
01:07:08

[and simpler and I'm getting a good score](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m11s)
01:07:11

[for so at this point I've now got rid of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m15s)
01:07:15

[as many columns as I feel I comfortably](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m21s)
01:07:21

[can ones that either didn't have a good](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m24s)
01:07:24

[feature importance or were highly](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m26s)
01:07:26

[related to other variables and the model](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m28s)
01:07:28

[didn't get worse significantly whenever](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m31s)
01:07:31

[when I removed them so now I'm at the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m32s)
01:07:32

[point where I want to try and really](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m35s)
01:07:35

[understand my data better by taking](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m37s)
01:07:37

[advantage of the model and we're going](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m39s)
01:07:39

[to use something called partial](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m42s)
01:07:42

[dependence and again this is something](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m43s)
01:07:43

[that you could like using the Carroll](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m44s)
01:07:44

[kernel and lots of people are going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m46s)
01:07:46

[appreciate this because almost nobody](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m47s)
01:07:47

[knows about partial dependence and it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m49s)
01:07:49

[a very very powerful technique what](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m51s)
01:07:51

[we're going to do is we're going to find](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m54s)
01:07:54

[out for the features that are important](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m55s)
01:07:55

[how do they relate to the dependent](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h07m58s)
01:07:58

[variable right so let's have a look](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m01s)
01:08:01

[right so let's again since we're doing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m04s)
01:08:04

[interpretation we'll set set our samples](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m06s)
01:08:06

[to 50,000 to run things quickly we'll](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m09s)
01:08:09

[take our data frame we'll get our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m13s)
01:08:13

[feature importance and notice that we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m17s)
01:08:17

[using Max and Kat because I'm actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m19s)
01:08:19

[pretty interested in terms of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m23s)
01:08:23

[interpretation and seeing the individual](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m25s)
01:08:25

[levels and so here's the top 10 and so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m27s)
01:08:27

[let's try and learn more about those top](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m32s)
01:08:32

[10 so year made is the second most](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m33s)
01:08:33

[important so one obvious thing we could](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m38s)
01:08:38

[do would be to plot year made against](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m41s)
01:08:41

[sale elapsed because as we've talked](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m48s)
01:08:48

[about already like it just seems to make](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m50s)
01:08:50

[sense that both important but it seems](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m52s)
01:08:52

[very likely that they kind of combine](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m55s)
01:08:55

[together to find like how old was the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h08m57s)
01:08:57

[product when it was sold so we could try](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m01s)
01:09:01

[plotting year made against sale elapsed](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m04s)
01:09:04

[to see how they relate to each other and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m07s)
01:09:07

[when we do we get this very ugly graph](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m08s)
01:09:08

[and it shows us that year made actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m12s)
01:09:12

[has a whole bunch that are a thousand](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m15s)
01:09:15

[right so clearly you know this is where](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m17s)
01:09:17

[I would tend to go back to the client or](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m20s)
01:09:20

[whatever and say ok I'm guessing that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m22s)
01:09:22

[these bulldozers weren't actually made](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m24s)
01:09:24

[in the Year 1000 and they would](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m25s)
01:09:25

[presumably say to me oh yes they're ones](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m27s)
01:09:27

[where we don't know where it was made](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m30s)
01:09:30

[you know maybe before 1986 we didn't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m31s)
01:09:31

[track that or maybe the things that are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m35s)
01:09:35

[sold in Illinois we don't have that data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m37s)
01:09:37

[provided or or whatever they tell us](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m39s)
01:09:39

[some reason so in order to understand](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m41s)
01:09:41

[this plot better I'm just going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m48s)
01:09:48

[remove them from this interpretation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m49s)
01:09:49

[section of the analysis so I'm just](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m52s)
01:09:52

[going to say ok let's just grab things](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m53s)
01:09:53

[where year made is greater than 1930](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m54s)
01:09:54

[ok so let's now look at the relationship](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h09m57s)
01:09:57

[between year made and sale press and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m01s)
01:10:01

[there's a really great package called GG](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m05s)
01:10:05

[plot GG plot originally was an](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m09s)
01:10:09

[package G G stands for the grammar of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m12s)
01:10:12

[graphics and the grammar of graphics is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m14s)
01:10:14

[like this very powerful way of thinking](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m17s)
01:10:17

[about how to produce charts in a very](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m20s)
01:10:20

[flexible way I'm not going to be talking](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m25s)
01:10:25

[about it much in this class there's lots](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m27s)
01:10:27

[of information available online but I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m29s)
01:10:29

[definitely recommend it as a great](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m31s)
01:10:31

[package to use ggplot which you can pip](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m34s)
01:10:34

[install it's part of the first AI](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m37s)
01:10:37

[environment already ggplot in python has](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m39s)
01:10:39

[basically the same parameters and API as](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m44s)
01:10:44

[the R version the R version is much](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m48s)
01:10:48

[better documented so you should read](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m50s)
01:10:50

[it's documentation to learn how to use](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m51s)
01:10:51

[it but basically you say okay I want to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m53s)
01:10:53

[create a plot of this data frame now](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h10m56s)
01:10:56

[when you create plots most of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m02s)
01:11:02

[datasets you're using are going to be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m05s)
01:11:05

[too big to plot as in like if you do a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m07s)
01:11:07

[scatter plot it'll create so many dots](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m11s)
01:11:11

[that it's just a big mess it'll take](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m12s)
01:11:12

[forever](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m15s)
01:11:15

[and remember when you're plotting things](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m16s)
01:11:16

[you just you're you're looking at it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m18s)
01:11:18

[right so there's no point putting](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m21s)
01:11:21

[something with a hundred million samples](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m22s)
01:11:22

[when if you're only used a hundred](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m24s)
01:11:24

[thousand samples it's going to be pixel](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m26s)
01:11:26

[identical right so that's why I call get](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m28s)
01:11:28

[sample first so get sample just grabs a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m31s)
01:11:31

[random sample okay so I'm just going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m33s)
01:11:33

[grab five hundred points for now okay so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m35s)
01:11:35

[I've got a grab five at a point from my](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m39s)
01:11:39

[data frame I got a plot a year made](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m42s)
01:11:42

[against sale price a EES stands for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m45s)
01:11:45

[aesthetic this is the basic way that you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m47s)
01:11:47

[set up your columns in ggplot okay so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m49s)
01:11:49

[this says to plot these columns from](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m53s)
01:11:53

[this data frame and then there's this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m54s)
01:11:54

[weird thing and GG plot where plus means](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m56s)
01:11:56

[basically add chart elements okay so I'm](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h11m59s)
01:11:59

[going to add a smoother so most of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m02s)
01:12:02

[very very often you'll find that a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m07s)
01:12:07

[scatter plot is very hard to see what's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m08s)
01:12:08

[going on because there's too much](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m10s)
01:12:10

[randomness or else a smoother basically](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m12s)
01:12:12

[creates a little linear regression for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m14s)
01:12:14

[every little subset of the graph and so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m17s)
01:12:17

[it kind of joins it up and allows you to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m20s)
01:12:20

[see a nice smooth curve okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m22s)
01:12:22

[so this is like the main way that I tend](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m25s)
01:12:25

[to look at univariate relationships and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m27s)
01:12:27

[by adding standard error equals true it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m31s)
01:12:31

[also shows me the confidence interval of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m34s)
01:12:34

[this smoother right so low S stands for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m36s)
01:12:36

[locally weighted regression which is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m40s)
01:12:40

[this idea of like doing kind of out](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m42s)
01:12:42

[doing lots of little mini regressions so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m43s)
01:12:43

[we can see here the relationship between](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m48s)
01:12:48

[year made and sale price is kind of all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m50s)
01:12:50

[over the place right which is like not](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m54s)
01:12:54

[really what I would expect](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m56s)
01:12:56

[I would I would have expected that more](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m57s)
01:12:57

[recent stuff it sold more recently would](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h12m59s)
01:12:59

[probably be like more expensive because](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m04s)
01:13:04

[of inflation and because there like more](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m06s)
01:13:06

[current models and so forth and the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m08s)
01:13:08

[problem is that when you look at a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m11s)
01:13:11

[univariate relationship like this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m12s)
01:13:12

[there's a whole lot of collinearity](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m14s)
01:13:14

[going on a whole lot of interactions](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m17s)
01:13:17

[that are being lost so for example why](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m19s)
01:13:19

[did the price drop yeah is it actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m23s)
01:13:23

[because like things made between 1991](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m26s)
01:13:26

[and 1997 are less valuable or is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m28s)
01:13:28

[actually because most of them were also](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m33s)
01:13:33

[sold during that time and actually there](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m34s)
01:13:34

[was like maybe a recession then or maybe](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m37s)
01:13:37

[it was like products sold during that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m40s)
01:13:40

[time a lot more people but buying types](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m41s)
01:13:41

[of vehicle that were less expensive like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m45s)
01:13:45

[there's all kinds of reasons for that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m48s)
01:13:48

[and so again as data scientists one of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m50s)
01:13:50

[the things are going to keep seeing is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m53s)
01:13:53

[that at the companies that you join](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m55s)
01:13:55

[people will come to you with with these](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m57s)
01:13:57

[kind of univariate charts where they'll](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h13m58s)
01:13:58

[say like oh my god our sales in Chicago](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m00s)
01:14:00

[have disappeared that got really bad or](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m03s)
01:14:03

[people aren't clicking on this add](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m06s)
01:14:06

[anymore and they'll show you a chart](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m07s)
01:14:07

[that looks like this and they'll be like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m09s)
01:14:09

[what happened and most of the time](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m11s)
01:14:11

[you'll find the answer to the question](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m14s)
01:14:14

[what happened is that there's something](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m15s)
01:14:15

[else going on right so I actually are in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m17s)
01:14:17

[Chicago last week actually we were doing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m19s)
01:14:19

[a new promotion and that's why you know](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m23s)
01:14:23

[revenue went down it's not because](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m26s)
01:14:26

[people are buying stuff in Chicago](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m28s)
01:14:28

[anymore it's because the prices were](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m29s)
01:14:29

[lower for instance so what we really](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m31s)
01:14:31

[want to be able to do is say well what's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m34s)
01:14:34

[the relationship between sale price and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m36s)
01:14:36

[year made](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m38s)
01:14:38

[all other things being equal so all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m39s)
01:14:39

[other things being equal basically means](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m46s)
01:14:46

[if we sold something in 1990 versus 1980](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m49s)
01:14:49

[and it was exactly the same thing -](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m53s)
01:14:53

[exactly the same person in exactly the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m55s)
01:14:55

[same option so on and so forth what](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h14m57s)
01:14:57

[would have been the difference in price](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m00s)
01:15:00

[and so to do that we do something called](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m01s)
01:15:01

[a partial dependence plot and this is a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m05s)
01:15:05

[partial dependence plot there's a really](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m08s)
01:15:08

[nice library which nobody's heard of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m10s)
01:15:10

[called PDP which does these partial](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m12s)
01:15:12

[dependence plots and what happens is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m17s)
01:15:17

[this we've got our sample of 500 data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m19s)
01:15:19

[points right and we're going to do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m21s)
01:15:21

[something really interesting we're going](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m23s)
01:15:23

[to take each one of those hundred](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m25s)
01:15:25

[randomly chosen options and we're going](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m27s)
01:15:27

[to make a little data set out of it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m31s)
01:15:31

[right so like here's our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m32s)
01:15:32

[here's elf come on here's our data set](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m36s)
01:15:36

[of like 500 options and here's our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m42s)
01:15:42

[columns one of which is the thing that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m46s)
01:15:46

[we're interested in which is year made](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m50s)
01:15:50

[so here's year made okay and what we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m52s)
01:15:52

[going to do is we're now going to try](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m56s)
01:15:56

[and create a chart where we're going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h15m58s)
01:15:58

[try and say all other things being equal](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m00s)
01:16:00

[in 1960](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m02s)
01:16:02

[how much did bulldozers cost how much](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m06s)
01:16:06

[did things cost in options and so the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m10s)
01:16:10

[way we're going to do that is we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m13s)
01:16:13

[going to replace the year made column](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m14s)
01:16:14

[with 1960 we're going to copy in the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m16s)
01:16:16

[value 1960 again and again and again all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m19s)
01:16:19

[the way down right so now every row the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m22s)
01:16:22

[year made is 1960 and all of the other](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m25s)
01:16:25

[data is going to be exactly the same and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m27s)
01:16:27

[we're going to take our random forest](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m29s)
01:16:29

[we're going to pass all this through our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m31s)
01:16:31

[random forest to predict the sale price](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m33s)
01:16:33

[so that will tell us for everything that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m38s)
01:16:38

[was auctioned how much do we think it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m42s)
01:16:42

[would have been sold for if that thing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m45s)
01:16:45

[was made in 1960 and that's what we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m48s)
01:16:48

[going to plot here all right that's the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m52s)
01:16:52

[price we're going to put here and then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m55s)
01:16:55

[we're going to do the same thing for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m56s)
01:16:56

[1961 alright we're going to replace all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h16m57s)
01:16:57

[these and do 1961 yeah so to be clear](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m02s)
01:17:02

[we've already fit the random forest yes](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m13s)
01:17:13

[and then we're just passing a new year](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m16s)
01:17:16

[and seeing what it determines the price](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m18s)
01:17:18

[should be yeah so this is a lot like the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m20s)
01:17:20

[way we did feature importance but rather](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m22s)
01:17:22

[than randomly shuffling the column we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m24s)
01:17:24

[going to replace the column with a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m26s)
01:17:26

[constant value all right so randomly](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m27s)
01:17:27

[shuffle in the column tells us how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m30s)
01:17:30

[accurate it is when you don't use that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m33s)
01:17:33

[column anymore](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m35s)
01:17:35

[replacing the whole column with a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m37s)
01:17:37

[constant tells us or estimates for us](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m38s)
01:17:38

[how much we would have sold that product](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m41s)
01:17:41

[for in that auction on that day in that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m43s)
01:17:43

[place if that product had been made in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m46s)
01:17:46

[1961](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m49s)
01:17:49

[right so we basically then take the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m50s)
01:17:50

[average of all of the sale prices that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m52s)
01:17:52

[we calculate from that random first and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m55s)
01:17:55

[so we drew it in 1961 and we get this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m57s)
01:17:57

[value right so what the partial](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h17m59s)
01:17:59

[dependence plot here shows us is each of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m02s)
01:18:02

[these light blue lines actually is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m04s)
01:18:04

[showing us all 500 lions so it says for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m07s)
01:18:07

[row number 1 in our data set if we sold](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m12s)
01:18:12

[it in 1960 we're going to index that to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m17s)
01:18:17

[0 right so call that zero right if we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m19s)
01:18:19

[sold it in 1970 that particular auction](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m22s)
01:18:22

[would have been here if we sold it in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m26s)
01:18:26

[1980 I would have been here if he sold](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m28s)
01:18:28

[in 1990 would have been here so we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m30s)
01:18:30

[actually plot all 500 predictions of how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m32s)
01:18:32

[much every one of those 500 auctions](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m37s)
01:18:37

[would have gone for if we replace it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m40s)
01:18:40

[before replacing a year made with each](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m43s)
01:18:43

[of these different values and then then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m45s)
01:18:45

[this dark line here is the average right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m48s)
01:18:48

[so this tells us how much would we have](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m52s)
01:18:52

[sold on average all of those options for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m55s)
01:18:55

[if all of those products were actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h18m59s)
01:18:59

[made in 1985 1990 1993 1994 and so forth](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m01s)
01:19:01

[and so you can see what's happened here](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m07s)
01:19:07

[is at least in the period where we have](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m09s)
01:19:09

[a reasonable out of data which is since](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m11s)
01:19:11

[1990 this is basically a totally](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m13s)
01:19:13

[straight line which is what you would](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m15s)
01:19:15

[expect right because if it was sold on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m17s)
01:19:17

[the same date and it was the same kind](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m20s)
01:19:20

[of tractor it sold to the same person in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m22s)
01:19:22

[the same option house then you would](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m25s)
01:19:25

[expect more recent vehicles to be more](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m27s)
01:19:27

[expensive because of inflation and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m31s)
01:19:31

[because they're they're newer right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m34s)
01:19:34

[they're not they're not as secondhand](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m37s)
01:19:37

[and you would expect that relationship](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m39s)
01:19:39

[to be roughly linear and that's exactly](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m41s)
01:19:41

[what we're finding ok so by removing all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m42s)
01:19:42

[of these externalities it often allows](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m46s)
01:19:46

[us to see the truth much more clearly as](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m50s)
01:19:50

[a question the back can you pass that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m54s)
01:19:54

[back there you're done ok so um](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h19m55s)
01:19:55

[this this partial dependents plot](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m01s)
01:20:01

[concept is something which is using a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m04s)
01:20:04

[random forest to get us a more clear](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m07s)
01:20:07

[interpretation of what's going on in our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m11s)
01:20:11

[data and so the steps were to first of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m14s)
01:20:14

[all look at the feature importance to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m17s)
01:20:17

[tell us like which things do we think we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m21s)
01:20:21

[care about and then to use the partial](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m23s)
01:20:23

[dependence plot to tell us what's going](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m26s)
01:20:26

[on on average right there's another cool](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m29s)
01:20:29

[thing we can do with PDP as we can use](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m35s)
01:20:35

[clusters and what clusters does is it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m37s)
01:20:37

[uses cluster analysis to look at all of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m39s)
01:20:39

[these each one of the 500 rows and say](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m42s)
01:20:42

[to some of those 500 roads kind of move](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m46s)
01:20:46

[in the same way and like we could kind](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m49s)
01:20:49

[of see it seems like there's a whole lot](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m51s)
01:20:51

[of rows that kind of go down and then up](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m53s)
01:20:53

[and there seems to be a bunch of rows](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m56s)
01:20:56

[that kind of go up and then go flat like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h20m58s)
01:20:58

[it does seem like there's some kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m00s)
01:21:00

[different types of behaviors being](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m01s)
01:21:01

[hidden and so here is the result of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m03s)
01:21:03

[doing that cluster analysis right is we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m06s)
01:21:06

[still get the same average but it says](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m09s)
01:21:09

[here kind of the five most common shapes](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m12s)
01:21:12

[that we see and this is where you could](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m15s)
01:21:15

[then go in and say all right it looks](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m17s)
01:21:17

[like some kinds of vehicle actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m20s)
01:21:20

[after 1990 their prices are pretty flat](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m24s)
01:21:24

[and before that they were pretty linear](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m26s)
01:21:26

[some kinds of vehicle and of exactly the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m28s)
01:21:28

[opposite and so like different kinds of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m31s)
01:21:31

[vehicle have these different shapes](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m33s)
01:21:33

[right and so this is something you could](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m35s)
01:21:35

[dig into I think it was one at the back](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m37s)
01:21:37

[oh you could okay so what we're going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m39s)
01:21:39

[do with this information well the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m42s)
01:21:42

[purpose of interpretation is to learn](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m45s)
01:21:45

[about a data set and so why do you want](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m49s)
01:21:49

[to learn about a data set it's because](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m51s)
01:21:51

[you it's because you want to do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m53s)
01:21:53

[something with it right so in this case](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m54s)
01:21:54

[it's not so much something if you're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m56s)
01:21:56

[trying to win a cogwheel competition I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h21m59s)
01:21:59

[mean it can be a little bit like some of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m01s)
01:22:01

[these insights might make you realize](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m03s)
01:22:03

[all I could transform this variable or](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m05s)
01:22:05

[create this interaction or whatever](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m08s)
01:22:08

[obviously feature importance is super](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m10s)
01:22:10

[important for cowgirl competitions but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m12s)
01:22:12

[this one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m14s)
01:22:14

[much more for like real life you know so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m15s)
01:22:15

[this is when you're talking to somebody](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m17s)
01:22:17

[and you say to them like okay those](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m19s)
01:22:19

[plots you've been showing me which](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m23s)
01:22:23

[actually say that like there was this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m24s)
01:22:24

[kind of dip in prices you know based on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m27s)
01:22:27

[like things made between 1990 and 1997](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m29s)
01:22:29

[there wasn't really you know actually it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m32s)
01:22:32

[was they were increasing there was](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m35s)
01:22:35

[actually something else going on at that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m37s)
01:22:37

[time](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m39s)
01:22:39

[no it's basically the thing that allows](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m40s)
01:22:40

[you to say like so whatever this outcome](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m42s)
01:22:42

[I'm trying to drive in my business is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m45s)
01:22:45

[this is how something's driving it all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m46s)
01:22:46

[right so if it's like I'm looking at you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m48s)
01:22:48

[know kind of advertising technology](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m53s)
01:22:53

[what's driving clicks that I'm actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m55s)
01:22:55

[digging into say okay this is actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m57s)
01:22:57

[how clicks are being driven this is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h22m59s)
01:22:59

[actually the variable that's driving it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m01s)
01:23:01

[this is how it's related so therefore we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m02s)
01:23:02

[should change our behavior in this way](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m04s)
01:23:04

[that's really the goal of any model I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m06s)
01:23:06

[guess there's two possible goals 1 goal](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m09s)
01:23:09

[of a model is just to get the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m10s)
01:23:10

[predictions like if you're doing hedge](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m12s)
01:23:12

[fund trading you probably want to know](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m14s)
01:23:14

[what the price of that equity is going](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m15s)
01:23:15

[to be if you're doing insurance you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m17s)
01:23:17

[probably just want to know how much](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m19s)
01:23:19

[claims that guy's going to have but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m21s)
01:23:21

[probably most of the time you're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m23s)
01:23:23

[actually trying to change something](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m25s)
01:23:25

[about how you do business how you do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m27s)
01:23:27

[marketing how you do just sticks so the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m29s)
01:23:29

[thing you actually care about is how the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m31s)
01:23:31

[things are related to each other all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m33s)
01:23:33

[right I'm sorry can you explain again](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m38s)
01:23:38

[when you scroll up and you were looking](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m39s)
01:23:39

[at the sale pricier may looking at the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m41s)
01:23:41

[entire model and you saw that dip and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m43s)
01:23:43

[you said something about that dip didn't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m48s)
01:23:48

[signify what we thought it did can you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m50s)
01:23:50

[explain why yeah so this is like a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m52s)
01:23:52

[classic boring univariate plot right so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m55s)
01:23:55

[this is basically just taking all of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h23m59s)
01:23:59

[dots all of the options plotting year](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m01s)
01:24:01

[made against sale price and we're gonna](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m03s)
01:24:03

[just fitting a rough average through](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m05s)
01:24:05

[them and so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m09s)
01:24:09

[true that products made between 1992 and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m14s)
01:24:14

[1997 on average in our data set are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m18s)
01:24:18

[being sold for less so like very often](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m22s)
01:24:22

[in business you'll hear somebody look at](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m26s)
01:24:26

[something like this and they'll be like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m28s)
01:24:28

[oh we should we should stop auctioning](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m29s)
01:24:29

[equipment that is made in that year in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m32s)
01:24:32

[those years because like we're getting](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m34s)
01:24:34

[less money for example but if the truth](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m35s)
01:24:35

[actually is that during those years it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m40s)
01:24:40

[just that people were making more small](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m45s)
01:24:45

[industrial equipment where you would](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m49s)
01:24:49

[expect it to be sold for less and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m51s)
01:24:51

[actually our profit on it is just as](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m53s)
01:24:53

[high for instance or during those years](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m55s)
01:24:55

[it's not that it's not things made](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h24m58s)
01:24:58

[during those years now would have repeat](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m01s)
01:25:01

[cheaper it's that during those years](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m04s)
01:25:04

[when we were selling things in those](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m07s)
01:25:07

[years they were cheaper because like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m09s)
01:25:09

[there was a recession going on so if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m11s)
01:25:11

[you're trying to like actually take some](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m13s)
01:25:13

[action based on this you probably don't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m15s)
01:25:15

[just care about the fact that things](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m18s)
01:25:18

[made in those years are cheaper on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m19s)
01:25:19

[average but how does that impact today](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m21s)
01:25:21

[you know so so this this approach where](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m24s)
01:25:24

[we actually say let's try and remove all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m29s)
01:25:29

[of these externalities so if something](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m31s)
01:25:31

[is sold on the same day to the same](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m34s)
01:25:34

[person of the same kind of vehicle then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m37s)
01:25:37

[actually have as year made impact price](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m40s)
01:25:40

[and so this basically says for example](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m42s)
01:25:42

[if I am deciding what to buy at an](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m44s)
01:25:44

[option then this is kind of saying to me](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m49s)
01:25:49

[okay like getting a more recent vehicle](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m51s)
01:25:51

[on average really does on average give](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m53s)
01:25:53

[you more money which is not what the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h25m57s)
01:25:57

[kind of the naive univariate plot said](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m00s)
01:26:00

[that because it's Tyler](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m03s)
01:26:03

[[Music]](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m11s)
01:26:11

[for like this bulldozer bulldozers made](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m13s)
01:26:13

[in 2010 probably are not close to the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m16s)
01:26:16

[type of bulldozers that were made in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m19s)
01:26:19

[1960 right and if you're taking](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m22s)
01:26:22

[something that would be so very](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m25s)
01:26:25

[different like a 2010 bulldozer and then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m28s)
01:26:28

[trying to just drop it to say oh if it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m31s)
01:26:31

[was made in 1960 that may cause poor](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m35s)
01:26:35

[prediction at a point because it's so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m39s)
01:26:39

[you're outside absolutely rainy](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m41s)
01:26:41

[absolutely so you know I think that's a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m43s)
01:26:43

[good point it's you know it's a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m45s)
01:26:45

[limitation however random forest is if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m47s)
01:26:47

[you're got a kind of data point that's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m51s)
01:26:51

[like over client you know which is kind](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m53s)
01:26:53

[of like in a part of the space that it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m55s)
01:26:55

[not seen before like maybe people didn't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m57s)
01:26:57

[put air conditioning really in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h26m59s)
01:26:59

[bulldozers in 1960 and you're saying how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m01s)
01:27:01

[much would this bulldoze over their](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m03s)
01:27:03

[conditioning have gone for 1960 you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m05s)
01:27:05

[don't really have any information to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m07s)
01:27:07

[know that so you know you it's a it's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m08s)
01:27:08

[it's this is still the best technique I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m15s)
01:27:15

[know of but it's it's not perfect and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m17s)
01:27:17

[you know you kind of hope that the trees](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m21s)
01:27:21

[are still going to find some useful](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m24s)
01:27:24

[truth even if though it hasn't seen that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m28s)
01:27:28

[combination of features before but yeah](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m30s)
01:27:30

[it's something to be aware of so you can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m33s)
01:27:33

[also do the same thing in a PDP](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m37s)
01:27:37

[interaction plot and a PDP interaction](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m41s)
01:27:41

[plot which is really what I'm trying to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m44s)
01:27:44

[get to here is like how to sail elapsed](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m45s)
01:27:45

[and year made together impact price and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m47s)
01:27:47

[so if I do a PDP interaction plot it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m51s)
01:27:51

[shows me sail elapsed versus price it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m54s)
01:27:54

[shows me year made versus price and it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h27m58s)
01:27:58

[shows me the combination versus price](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m01s)
01:28:01

[remember this is always log of price](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m04s)
01:28:04

[that's why these prices look weird right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m05s)
01:28:05

[and so you can see that the combination](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m07s)
01:28:07

[of sale elapsed and year made is as you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m09s)
01:28:09

[would expect later dates so more or less](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m12s)
01:28:12

[time is giving me I'm sorry it's the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m16s)
01:28:16

[other way around isn't it so the higher](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m23s)
01:28:23

[crisis those where there's the least](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m26s)
01:28:26

[elapsed and the most recent year made so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m29s)
01:28:29

[you can see here there's the univariate](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m34s)
01:28:34

[relationship between sale elapsed and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m37s)
01:28:37

[price and here is the univariate](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m39s)
01:28:39

[relationship between year made and price](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m42s)
01:28:42

[and then here is the combination of the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m45s)
01:28:45

[two it's enough to see like clearly that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m49s)
01:28:49

[these two things are driving christs](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m53s)
01:28:53

[together you can also see these are not](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m55s)
01:28:55

[like simple diagonal lines so it's kind](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h28m58s)
01:28:58

[of some interesting interaction going on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m00s)
01:29:00

[and so based on looking at these plots](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m03s)
01:29:03

[it's enough to make me think oh we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m07s)
01:29:07

[should maybe put in some kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m09s)
01:29:09

[interaction term and see what happens](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m11s)
01:29:11

[so let's come back to that in a moment](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m13s)
01:29:13

[but let's just look at a couple more](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m15s)
01:29:15

[remember in this case I did one hot](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m18s)
01:29:18

[encoding way back at the top here I said](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m21s)
01:29:21

[max and cat equals seven so I've got](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m24s)
01:29:24

[like enclosure erupts with AC so if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m27s)
01:29:27

[you've got one hot encoded variables you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m32s)
01:29:32

[can pass an array of them to pit plot](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m34s)
01:29:34

[PDP and it'll treat them as a category](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m39s)
01:29:39

[right and so in this case I'm going to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m42s)
01:29:42

[create a PDP plot of these three](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m45s)
01:29:45

[categories I'm going to call it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m47s)
01:29:47

[enclosure and I can see here that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m49s)
01:29:49

[enclosure erupts with AC on average are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m54s)
01:29:54

[more expensive than enclosure erupts and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h29m59s)
01:29:59

[enclosure arose it actually looks like](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m02s)
01:30:02

[enclosure erupts from closure erupts are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m04s)
01:30:04

[pretty similar](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m06s)
01:30:06

[or else erupts with AC is higher so this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m06s)
01:30:06

[is you know at this point you know I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m11s)
01:30:11

[probably being fine to hop into Google](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m12s)
01:30:12

[and like type erupts and erupts and find](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m14s)
01:30:14

[out what the hell these things are and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m18s)
01:30:18

[here we go](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m20s)
01:30:20

[so it turns out that erupts is enclosed](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m22s)
01:30:22

[rollover protective structure and so it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m26s)
01:30:26

[turns out that if your your bulldozer is](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m31s)
01:30:31

[fully enclosed then optionally you can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m37s)
01:30:37

[also get air conditioning so it turns](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m39s)
01:30:39

[out that actually this thing is telling](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m42s)
01:30:42

[us whether it's got air conditioning if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m43s)
01:30:43

[it's an open structure then obviously](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m44s)
01:30:44

[you don't have air conditioning at all](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m46s)
01:30:46

[so that's what these three levels are](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m47s)
01:30:47

[and so we've now learnt all other things](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m49s)
01:30:49

[being equal the same bulldozer sold at](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m53s)
01:30:53

[the same time built at the same time](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m56s)
01:30:56

[sold to the same person is going to be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h30m58s)
01:30:58

[quite a bit more expensive is if it has](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m00s)
01:31:00

[air conditioning than if it doesn't ok](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m02s)
01:31:02

[so again we're kind of getting this nice](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m05s)
01:31:05

[interpretation ability and you know now](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m07s)
01:31:07

[that I spent some time with this data](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m10s)
01:31:10

[set I'd certainly noticed that this you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m11s)
01:31:11

[know knowing this is the most important](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m14s)
01:31:14

[thing you do notice that there's a lot](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m15s)
01:31:15

[more air conditioned bulldozers nowadays](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m17s)
01:31:17

[and they used to be and so there's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m20s)
01:31:20

[definitely an interaction between kind](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m22s)
01:31:22

[of date and that so based on the earlier](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m23s)
01:31:23

[interaction analysis I've tried](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m27s)
01:31:27

[first of all setting everything before](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m29s)
01:31:29

[1950 to 1950s it seems to be some kind](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m31s)
01:31:31

[of missing value I've been set age to be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m34s)
01:31:34

[equal to sale year - year made and so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m38s)
01:31:38

[then I try running a random forest on](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m44s)
01:31:44

[that and indeed page is now the single](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m46s)
01:31:46

[biggest thing sale elapsed is way back](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m51s)
01:31:51

[down here year made is back down here so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m54s)
01:31:54

[we've kind of used this to find an](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h31m58s)
01:31:58

[interaction but remember of course a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m01s)
01:32:01

[random forest can create or it can](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m05s)
01:32:05

[create an interaction through having](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m07s)
01:32:07

[multiple split points so we shouldn't](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m09s)
01:32:09

[assume that this is actually going to be](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m10s)
01:32:10

[a better result and in practice I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m13s)
01:32:13

[actually found when I looked at my score](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m17s)
01:32:17

[and my rmse adding age was actually a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m21s)
01:32:21

[little worse and we'll see about that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m24s)
01:32:24

[later probably in the next lesson ok](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m26s)
01:32:26

[so one last thing is tree interpreter so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m34s)
01:32:34

[this is also in the category of things](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m40s)
01:32:40

[that most people don't know exists but](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m42s)
01:32:42

[it's super important almost pointless](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m45s)
01:32:45

[for like cattle competitions but super](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m48s)
01:32:48

[important for real life and here's the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m50s)
01:32:50

[idea let's say you're an insurance](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m53s)
01:32:53

[company and somebody rings up and you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m57s)
01:32:57

[give them a quote and they say oh that's](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h32m59s)
01:32:59

[five hundred dollars more than last year](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m02s)
01:33:02

[why okay so in general you've made a](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m05s)
01:33:05

[prediction from some model and somebody](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m08s)
01:33:08

[asks why and so this is where we use](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m11s)
01:33:11

[this method called tree interpreter and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m15s)
01:33:15

[what tree interpreter does is it allows](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m18s)
01:33:18

[us to take a particular row so in this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m21s)
01:33:21

[case we're going to pick row number zero](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m25s)
01:33:25

[right so here here is row zero right uh](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m28s)
01:33:28

[presumably this is like year made I](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m32s)
01:33:32

[don't know what all the codes stand for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m33s)
01:33:33

[but like his is all of the columns in](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m35s)
01:33:35

[row 0 what I can do with a tree](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m38s)
01:33:38

[interpreter is I can go t i dot predict](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m41s)
01:33:41

[pass in my random forest pass in my row](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m45s)
01:33:45

[so this would be like this particular](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m49s)
01:33:49

[customers insurance information or this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m50s)
01:33:50

[in this case this particular option](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m53s)
01:33:53

[right and it'll give me back three](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m55s)
01:33:55

[things the first is the prediction from](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h33m58s)
01:33:58

[the random forest the second is the bias](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m01s)
01:34:01

[the bias is basically the average sale](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m05s)
01:34:05

[price across the whole original data set](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m09s)
01:34:09

[right so like remember you know random](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m12s)
01:34:12

[forest we started with single trees oh](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m15s)
01:34:15

[we haven't got to draw in there anymore](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m23s)
01:34:23

[but remember we started with a single](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m25s)
01:34:25

[tree in our random forest](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m26s)
01:34:26

[and we split it once and then we spit](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m30s)
01:34:30

[that once and then we split that one](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m32s)
01:34:32

[straight we said like oh what's the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m34s)
01:34:34

[average value for the whole data set](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m35s)
01:34:35

[then what's the average value for those](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m38s)
01:34:38

[where the first split was true and then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m41s)
01:34:41

[what's the average value where the next](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m43s)
01:34:43

[that was also true until eventually you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m46s)
01:34:46

[get down to the leaf nodes where you've](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m48s)
01:34:48

[got the average value you predict right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m50s)
01:34:50

[so you can kind of think of it this way](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m51s)
01:34:51

[if this for a single tree if this is our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m54s)
01:34:54

[final leaf node right maybe we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m57s)
01:34:57

[predicting like nine point one right and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h34m59s)
01:34:59

[then maybe the average log sale price](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m01s)
01:35:01

[for the whole the whole lot is like ten](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m04s)
01:35:04

[point two right that's the average](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m08s)
01:35:08

[through all the options and so you could](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m10s)
01:35:10

[kind of like work your way down here so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m13s)
01:35:13

[let's go and create this that's actually](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m16s)
01:35:16

[go and run this so I can see it okay so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m19s)
01:35:19

[let's go back and redraw this single](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m23s)
01:35:23

[tree you'll find like in Jupiter](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m26s)
01:35:26

[notebooks often a lot of the things we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m28s)
01:35:28

[create like videos progress bars and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m32s)
01:35:32

[stuff they don't know how to like save](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m35s)
01:35:35

[themselves to the file so you'll see](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m37s)
01:35:37

[just like a little string here and so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m40s)
01:35:40

[you actually have to rerun it to create](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m42s)
01:35:42

[the string so this was the single tree](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m44s)
01:35:44

[that we created](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m51s)
01:35:51

[so the whole dataset had an average log](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h35m56s)
01:35:56

[sale price of 10.2 the data set for](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m00s)
01:36:00

[those with capital system equals true](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m04s)
01:36:04

[had an average of ten point three the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m06s)
01:36:06

[data set for capital system equals true](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m10s)
01:36:10

[enclosure less than point lesson two was](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m13s)
01:36:13

[nine point nine and then eventually we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m16s)
01:36:16

[get all the way up here and also a model](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m18s)
01:36:18

[ID less than forty five seventy three](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m21s)
01:36:21

[it's ten point two so you could kind of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m23s)
01:36:23

[like say okay why did this particular](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m25s)
01:36:25

[row let's say we had a row that ended up](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m29s)
01:36:29

[over in this leaf node why did we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m32s)
01:36:32

[predict him point two well it's because](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m33s)
01:36:33

[we start with ten point one nine and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m35s)
01:36:35

[then because the capitalist system was](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m39s)
01:36:39

[was was less than point five so it was](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m41s)
01:36:41

[actually false](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m43s)
01:36:43

[we added about point two to that so we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m44s)
01:36:44

[went from ten point one to ten point](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m48s)
01:36:48

[three right so ten point two to ten](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m50s)
01:36:50

[point three so we added a little bit](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m52s)
01:36:52

[because if this one is true and then to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m54s)
01:36:54

[go from ten point three to nine point](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m57s)
01:36:57

[nine so because enclosure is less than](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h36m59s)
01:36:59

[two we subtracted about 0.4 and then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m01s)
01:37:01

[because model ID was less than](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m06s)
01:37:06

[45-hundred we added about point seven](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m08s)
01:37:08

[right so you can see like with a single](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m12s)
01:37:12

[tree you could like break down like why](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m15s)
01:37:15

[is it that we predicted ten point two](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m18s)
01:37:18

[retinas like and each one of these](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m20s)
01:37:20

[decision points we're adding or](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m22s)
01:37:22

[subtracting a little bit from the value](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m24s)
01:37:24

[so what we could then do is we could do](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m26s)
01:37:26

[that for all the treats](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m30s)
01:37:30

[and then we could take the average so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m33s)
01:37:33

[every time we see enclosure did we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m34s)
01:37:34

[increase or decrease the value and how](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m39s)
01:37:39

[much by every time we see model ID did](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m41s)
01:37:41

[we increase what decrease the value and](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m44s)
01:37:44

[how much by and so we could take the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m45s)
01:37:45

[average of all of those and that's what](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m47s)
01:37:47

[ends up in this thing called](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m51s)
01:37:51

[contributions so here is all of our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m52s)
01:37:52

[predictors and here is the value of each](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h37m57s)
01:37:57

[and so this is telling us and I've](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m00s)
01:38:00

[sorted them here that the fact that this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m02s)
01:38:02

[thing was made in 1999 was the thing](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m06s)
01:38:06

[that most negatively impacted our](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m10s)
01:38:10

[prediction and the fact that the age of](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m13s)
01:38:13

[the vehicle was 11 years was more most](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m17s)
01:38:17

[positively impacted](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m22s)
01:38:22

[um I think you actually needs a sort](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m29s)
01:38:29

[after you zip them together they seem to](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m31s)
01:38:31

[be sort of negative point five well my](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m33s)
01:38:33

[bunions are sorted but then they're just](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m35s)
01:38:35

[reassigned to the columns in the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m36s)
01:38:36

[original order which is what's thank you](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m38s)
01:38:38

[thank you that makes perfect sense](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m43s)
01:38:43

[yes we need to do an index sort okay](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m47s)
01:38:47

[thank you we will make sure we fix that](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m52s)
01:38:52

[by next week so we need to sort columns](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m54s)
01:38:54

[by the index from contributions so then](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h38m59s)
01:38:59

[there's this thing called bias and so](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m05s)
01:39:05

[the bias is just the average but before](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m07s)
01:39:07

[we start doing any splits right so if](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m11s)
01:39:11

[you basically start with the average log](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m13s)
01:39:13

[of value and then we went down each tree](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m17s)
01:39:17

[and each time we saw a year made we had](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m19s)
01:39:19

[some impact couple systems some impact](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m21s)
01:39:21

[product size some impact and so forth](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m24s)
01:39:24

[right](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m26s)
01:39:26

[[Music]](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m27s)
01:39:27

[okay so I think what we might do is we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m30s)
01:39:30

[might come back to because we could have](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m32s)
01:39:32

[out of time we might come back to tree](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m34s)
01:39:34

[interpreter next time](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m35s)
01:39:35

[but the basic idea this is the last this](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m38s)
01:39:38

[is the last of our key interpretation](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m40s)
01:39:40

[points and the basic idea is that we](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m42s)
01:39:42

[want some ability to not only tell us](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m45s)
01:39:45

[about the model as a whole and how it](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m50s)
01:39:50

[works on average but to look at how the](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m52s)
01:39:52

[model makes predictions for an](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m53s)
01:39:53

[individual row and that's what we're](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m55s)
01:39:55

[doing here okay great next everybody see](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h39m58s)
01:39:58

[you on this way](https://www.youtube.com/watch?v=0v93qHDqq_g#t=01h40m02s)
01:40:02

