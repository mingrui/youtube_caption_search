[so I recognize that by going back to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m00s)
00:00:00

[clustering we're going to talk about](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m04s)
00:00:04

[clustering again in the next lesson or](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m09s)
00:00:09

[two in terms of an application of it but](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m11s)
00:00:11

[specifically what I wanted to do was](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m15s)
00:00:15

[show you k-means clustering intensive](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m18s)
00:00:18

[love it is stay on](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m22s)
00:00:22

[um](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m25s)
00:00:25

[there are some things which is easier to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m28s)
00:00:28

[do intensive flows and play torch](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m30s)
00:00:30

[mainly because tensorflow kind of has a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m32s)
00:00:32

[more complete API at so far so there are](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m34s)
00:00:34

[some things that are just yellow content](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m40s)
00:00:40

[to float if like oh there's already a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m42s)
00:00:42

[method that does that but there isn't](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m43s)
00:00:43

[one in pi torch and so something and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m45s)
00:00:45

[some things are just a bit easier neater](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m47s)
00:00:47

[in gentle flow than implied torch and I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m49s)
00:00:49

[actually found k-means quite easy to do](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m53s)
00:00:53

[but what I'm going to do is I'm going to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m55s)
00:00:55

[try and show you a way to write custom](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m56s)
00:00:56

[tensor flow code in a kind of a really](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h00m59s)
00:00:59

[pie torchy way right and a kind of an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m02s)
00:01:02

[interactivity way and we're going to try](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m05s)
00:01:05

[and avoid all of the you know fancy](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m07s)
00:01:07

[széchenyi graphics kopi business as](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m11s)
00:01:11

[much as possible so to remind you that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m14s)
00:01:14

[where we kind of initially claimed at](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m20s)
00:01:20

[clustering was to say hey what if we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m22s)
00:01:22

[were doing lung cancer detection in CT](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m24s)
00:01:24

[scans and these were like 512 by 512 by](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m30s)
00:01:30

[200 volumetric things which is too big](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m33s)
00:01:33

[to really run a whole CNN over](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m36s)
00:01:36

[conveniently so one of the thoughts to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m39s)
00:01:39

[fix that was to run some kind of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m43s)
00:01:43

[heuristic that found all of the things](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m46s)
00:01:46

[that look like they could vaguely be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m48s)
00:01:48

[modules and then create a new data set](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m50s)
00:01:50

[where you basically zoomed into each of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m53s)
00:01:53

[those maybe nodules and created a small](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m55s)
00:01:55

[little you know 20 by 20 by 20 cube or](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h01m57s)
00:01:57

[something you could then use a 3d CNN on](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m01s)
00:02:01

[there or try planar CNN and I this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m04s)
00:02:04

[general concept I wanted to remind you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m10s)
00:02:10

[about because I feel like it's something](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m12s)
00:02:12

[which maybe I haven't stressed enough](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m13s)
00:02:13

[I've kind of kept from showing any ways](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m17s)
00:02:17

[of doing this think back to the lesson 7](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m18s)
00:02:18

[with a fish I showed you the bounding](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m20s)
00:02:20

[boxes and I showed you the heat maps so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m22s)
00:02:22

[the reason for all of that would](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m24s)
00:02:24

[basically to show you how to zoom into](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m25s)
00:02:25

[things and then create new models based](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m27s)
00:02:27

[on those zoom different things so in the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m29s)
00:02:29

[fisheries case you know you could really](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m34s)
00:02:34

[just use a lower res CNN to find that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m37s)
00:02:37

[maybe fish and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m40s)
00:02:40

[into those in the CT scan case maybe we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m41s)
00:02:41

[can't even do that so maybe we need to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m46s)
00:02:46

[use this kind of mentorship clustering](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m48s)
00:02:48

[approach another thing we necessarily do](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m50s)
00:02:50

[to be interesting to see what the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m53s)
00:02:53

[winners use but certainly particularly](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m54s)
00:02:54

[if you don't have lots of time or you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m57s)
00:02:57

[have a lot of data heuristics become](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h02m58s)
00:02:58

[more and more interesting now the reason](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m01s)
00:03:01

[is you're istic is interesting is you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m04s)
00:03:04

[can do something quickly an approximate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m07s)
00:03:07

[that could have lots and lots and lots](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m11s)
00:03:11

[of false positives and it doesn't really](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m12s)
00:03:12

[matter right because you know those](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m15s)
00:03:15

[false positives means just you know](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m16s)
00:03:16

[extra data that you're feeding to your](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m19s)
00:03:19

[you know your real model so you can](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m21s)
00:03:21

[always tune it it's like okay how much](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m24s)
00:03:24

[time have I got to train my real model](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m26s)
00:03:26

[and then I can decide how many false](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m28s)
00:03:28

[positives](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m30s)
00:03:30

[I can I can handle so as long as you're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m30s)
00:03:30

[kind of pre processing model is better](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m33s)
00:03:33

[than nothing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m35s)
00:03:35

[go you know you can use it to get rid of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m36s)
00:03:36

[some of the stuff that like is clearly](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m40s)
00:03:40

[not a nodule for example for example](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m41s)
00:03:41

[anything that is like in the middle of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m44s)
00:03:44

[the lung wall is not a nodule another](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m47s)
00:03:47

[thing that is you know or whitespace is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m49s)
00:03:49

[not a nodule so forth okay so we talked](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m52s)
00:03:52

[about mean shift clustering and how the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h03m57s)
00:03:57

[big benefit of it is that it allows us](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m00s)
00:04:00

[to build clusters without knowing how](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m06s)
00:04:06

[many clusters there are at a time also](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m09s)
00:04:09

[it without any special extra work that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m13s)
00:04:13

[allows us to find clusters which aren't](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m16s)
00:04:16

[kind of Gaussian or tharok all if you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m19s)
00:04:19

[like in shape but can that's really](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m22s)
00:04:22

[important for something like a CT scan](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m24s)
00:04:24

[where a cluster will often be like a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m26s)
00:04:26

[vessel which is this really skinny long](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m27s)
00:04:27

[thing so k-means on the other hand is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m29s)
00:04:29

[faster I think it's N squared rather](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m36s)
00:04:36

[than n cubed time we have talked to you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m39s)
00:04:39

[on the forum about dramatically speeding](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m43s)
00:04:43

[up means shift clustering using](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m45s)
00:04:45

[approximate nearest neighbors which is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m47s)
00:04:47

[something which we started making some](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m48s)
00:04:48

[progress on today so hopefully we'll](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m50s)
00:04:50

[have results from that maybe by next](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m52s)
00:04:52

[week](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m53s)
00:04:53

[but the basic naive algorithm is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m54s)
00:04:54

[certainly should be a lot classed at the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h04m57s)
00:04:57

[k-means so there's one good reason to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m00s)
00:05:00

[use it so as per usual you know we can](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m02s)
00:05:02

[start with some listing data and we're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m05s)
00:05:05

[going to try and figure out what where](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m10s)
00:05:10

[the cluster centers are so one quick way](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m12s)
00:05:12

[to avoid hassles in tensor flow is to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m16s)
00:05:16

[create an interactive session so an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m21s)
00:05:21

[interactive session basically means that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m24s)
00:05:24

[you can call that run on a computation](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m27s)
00:05:27

[graph which doesn't return something or](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m31s)
00:05:31

[dot eval on our computation graph that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m34s)
00:05:34

[does return something and you don't have](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m36s)
00:05:36

[to worry about creating a graph or a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m39s)
00:05:39

[session or you know calling having a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m42s)
00:05:42

[session with the clause or anything like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m43s)
00:05:43

[that it just it just works so that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m45s)
00:05:45

[basically what happens when you call TF](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m49s)
00:05:49

[interactive session](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m51s)
00:05:51

[okay so by creating an interactive](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m54s)
00:05:54

[session we can then](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h05m58s)
00:05:58

[[Music]](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m01s)
00:06:01

[and if do you things one step at a time](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m03s)
00:06:03

[so in this case the first step in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m07s)
00:06:07

[k-means is to pick some initial](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m09s)
00:06:09

[centroids so you basically start out and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m14s)
00:06:14

[say okay if we're going to create](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m16s)
00:06:16

[however many clusters so in this case n](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m18s)
00:06:18

[plus tis is six okay then start out by](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m21s)
00:06:21

[saying okay well where where might you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m25s)
00:06:25

[know where might those six clusters be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m27s)
00:06:27

[and for a long time with k-means people](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m29s)
00:06:29

[picked them randomly but most](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m32s)
00:06:32

[practitioners realize that that was a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m36s)
00:06:36

[dumb idea soon enough and a lot of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m37s)
00:06:37

[people had various heuristics for](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m40s)
00:06:40

[picking them in 2007 finally a paper was](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m41s)
00:06:41

[published actually suggesting a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m44s)
00:06:44

[heuristic I tend to use a very simple](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m45s)
00:06:45

[heuristic which is what I use here in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m47s)
00:06:47

[find initial centroids so to describe](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m51s)
00:06:51

[this heuristic I will show you the code](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m54s)
00:06:54

[so find additional centroids looks like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h06m59s)
00:06:59

[this basically and I'm going to run](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m03s)
00:07:03

[through it quickly and then I'll run](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m05s)
00:07:05

[through it slowly basically the idea is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m06s)
00:07:06

[we first of all pick a single data point](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m09s)
00:07:09

[index and then we select that single](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m14s)
00:07:14

[data point okay so we have someone](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m17s)
00:07:17

[randomly selected data point and then we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m19s)
00:07:19

[find what is the distance from that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m22s)
00:07:22

[randomly selected data point to every](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m25s)
00:07:25

[other data point](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m28s)
00:07:28

[and then we say okay what is the data](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m30s)
00:07:30

[point that is the farthest away from](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m35s)
00:07:35

[that randomly selected data point the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m37s)
00:07:37

[index of it and the point itself and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m40s)
00:07:40

[then we say okay we're going to append](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m42s)
00:07:42

[that to the initial centroids so say](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m44s)
00:07:44

[they picked at random this plate as my](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m48s)
00:07:48

[random initial point the furthest point](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m52s)
00:07:52

[away from that is probably somewhere](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m54s)
00:07:54

[around here okay so that would be the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m56s)
00:07:56

[first centroid we picked okay we are now](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h07m58s)
00:07:58

[inside a loop and we now go back and we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m03s)
00:08:03

[repeat the process so we now replace our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m06s)
00:08:06

[random point with the actual first](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m08s)
00:08:08

[centroid and we repeat go through the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m12s)
00:08:12

[live once more so if we had our first](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m15s)
00:08:15

[centroid here our second one now might](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m17s)
00:08:17

[be somewhere up here okay so we now have](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m20s)
00:08:20

[two centroids the next time through the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m24s)
00:08:24

[loop therefore this is slightly more](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m27s)
00:08:27

[interesting this all distances we're now](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m29s)
00:08:29

[going to have the distance between every](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m31s)
00:08:31

[one of our initial centroids and every](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m34s)
00:08:34

[other data point that's we've got a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m39s)
00:08:39

[matrix in this case it's going to be two](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m41s)
00:08:41

[by the number of data points so then we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m43s)
00:08:43

[say okay for every data point find the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m47s)
00:08:47

[closest cluster okay so what's the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m51s)
00:08:51

[distance to the closest initial centroid](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m55s)
00:08:55

[okay and then tell me which data point](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h08m58s)
00:08:58

[is the farthest away from its closest](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m02s)
00:09:02

[initial centroid so in other words which](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m06s)
00:09:06

[data point is the furthest away from any](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m08s)
00:09:08

[centroid](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m10s)
00:09:10

[so that's the basic that's the basic](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m12s)
00:09:12

[algorithm so let's look and see how we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m16s)
00:09:16

[actually do that in tensorflow so it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m19s)
00:09:19

[looks a lot like numpy except in places](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m23s)
00:09:23

[you would expect to see NP we see here](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m25s)
00:09:25

[and then we see the API is a little](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m29s)
00:09:29

[different but not too different right so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m32s)
00:09:32

[to get a random number we can just use](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m37s)
00:09:37

[random uniform we can tell it what type](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m41s)
00:09:41

[of random number we want so we want a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m44s)
00:09:44

[random int because we're trying to get a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m45s)
00:09:45

[random index so which the choose a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m47s)
00:09:47

[random data point it's going to be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m49s)
00:09:49

[between 0 and the amount of data points](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m51s)
00:09:51

[we have](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m53s)
00:09:53

[so that gives this is some random index](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h09m55s)
00:09:55

[we can now go ahead and index into our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m00s)
00:10:00

[data now you'll notice that credits](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m04s)
00:10:04

[include V data so what is V data when we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m07s)
00:10:07

[said that when we set up this k-means in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m09s)
00:10:09

[the first place the data was sent in as](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m12s)
00:10:12

[a numpy array and then I call TS](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m15s)
00:10:15

[variable on it now this is the critical](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m17s)
00:10:17

[thing that kind of lets us make](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m20s)
00:10:20

[tensorflow feel more like paper once I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m22s)
00:10:22

[do this data is now basically copied to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m27s)
00:10:27

[the GPU and so when I'm calling](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m30s)
00:10:30

[something using V data I'm calling this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m33s)
00:10:33

[the GPU object okay now there's one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m36s)
00:10:36

[thing problematic are to be aware of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m42s)
00:10:42

[which is that the copying does not](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m44s)
00:10:44

[actually occur when you write this the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m46s)
00:10:46

[copying occurs when you write this okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m49s)
00:10:49

[so anytime you call TS variable if you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h10m55s)
00:10:55

[then try to run something using that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m01s)
00:11:01

[variable you'll get back an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m04s)
00:11:04

[uninitialized variable error unless you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m05s)
00:11:05

[call this in the meantime](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m08s)
00:11:08

[okay so this is kind of like a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m09s)
00:11:09

[performance stuff intensive flow where](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m12s)
00:11:12

[they try to try to say okay well you can](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m15s)
00:11:15

[like set up lots of variables at once](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m17s)
00:11:17

[and then call this initializer and we'll](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m18s)
00:11:18

[do it all at once for you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m21s)
00:11:21

[okay so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m23s)
00:11:23

[earlier on we created this k-means](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m28s)
00:11:28

[object we know that in place in when you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m31s)
00:11:31

[create an object to calls underscore](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m34s)
00:11:34

[underscore underscore underscore at such](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m36s)
00:11:36

[a place and works inside that we copied](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m39s)
00:11:39

[the data to the GPU by using TF variable](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m41s)
00:11:41

[and then inside find initial centroids](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m44s)
00:11:44

[we can now access that in order to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m47s)
00:11:47

[basically do calculations involving data](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m50s)
00:11:50

[on the GPU](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m52s)
00:11:52

[intends to flow pretty much everything](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m57s)
00:11:57

[takes and returns a tensor alright so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h11m59s)
00:11:59

[when you create we call random uniform](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m02s)
00:12:02

[it's giving us a tensor you know an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m04s)
00:12:04

[array of random numbers in this case we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m06s)
00:12:06

[just wanted one of them so we have to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m09s)
00:12:09

[use TF squeeze to take that tensor time](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m10s)
00:12:10

[turn it into a scalar because then we're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m14s)
00:12:14

[just indexing into here to get a single](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m16s)
00:12:16

[item back](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m18s)
00:12:18

[so now that we've got that single open](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m21s)
00:12:21

[back we're then expand it back again](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m23s)
00:12:23

[into a tensor because inside our loop](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m27s)
00:12:27

[remember this is going to be a list of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m30s)
00:12:30

[initial centroids that's just that this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m33s)
00:12:33

[list happens to be of length one at the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m35s)
00:12:35

[moment](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m38s)
00:12:38

[so one of these tricks in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m40s)
00:12:40

[making tensorflow feel more like a torch](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m45s)
00:12:45

[is to use standard Python loops so in a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m48s)
00:12:48

[lot of tensorflow code where it's kind](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m52s)
00:12:52

[of you know more serious performance](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m54s)
00:12:54

[intensive stuff you'll see people use](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m56s)
00:12:56

[like 10 to flow specific loops like T F](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h12m58s)
00:12:58

[dot while or T F dot scan or map or so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m00s)
00:13:00

[close the challenge with using those](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m03s)
00:13:03

[kind of loops is it's basically creating](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m06s)
00:13:06

[a computation graph of that loop you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m07s)
00:13:07

[can't step through which you can't you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m10s)
00:13:10

[know use it in the normal Python it kind](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m12s)
00:13:12

[of ways so we can just use normal loops](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m14s)
00:13:14

[normal plays on words if we're careful](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m18s)
00:13:18

[about how we do it okay so inside our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m19s)
00:13:19

[normal place and loop we can use normal](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m22s)
00:13:22

[Python functions so here's a function I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m25s)
00:13:25

[created which calculates the distance](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m28s)
00:13:28

[between everything in this tensor](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m31s)
00:13:31

[compared to everything in this tensor](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m33s)
00:13:33

[all right so all distances it looks very](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m34s)
00:13:34

[familiar because it looks a lot like the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m41s)
00:13:41

[pay torch code we had right so we for](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m43s)
00:13:43

[the first array for the first chancer we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m46s)
00:13:46

[add an additional access to access 0 and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m49s)
00:13:49

[for the second we add an additional](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m53s)
00:13:53

[access to access one so the reason this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m55s)
00:13:55

[works is because of broadcasting so a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h13m59s)
00:13:59

[when it starts out is a vector now and B](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m05s)
00:14:05

[is a vector now is with a a column or](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m11s)
00:14:11

[add a a row what's the orientation of it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m17s)
00:14:17

[well the answer is it's both in it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m20s)
00:14:20

[neither right it's one-dimensional so it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m22s)
00:14:22

[has no concept of what direction is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m25s)
00:14:25

[looking right so at this so then what we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m27s)
00:14:27

[do is we said expanding an ax is zero so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m30s)
00:14:30

[that's roads right so that basically](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m36s)
00:14:36

[says to a ok you are now](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m37s)
00:14:37

[definitely a row vector right you now](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m40s)
00:14:40

[have one row and however many columns](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m43s)
00:14:43

[same as before and then where else with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m47s)
00:14:47

[B we add an axis at the end right so B](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m49s)
00:14:49

[is now definitely a column vector ax](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m54s)
00:14:54

[that now has one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m57s)
00:14:57

[column and however many rows we had](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h14m59s)
00:14:59

[before okay so with broadcasting what](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m01s)
00:15:01

[happens is that this one gets broadcast](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m06s)
00:15:06

[to this length and this one gets](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m09s)
00:15:09

[broadcast to this length so we end up](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m14s)
00:15:14

[with a matrix containing the difference](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m18s)
00:15:18

[between every one of these items and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m21s)
00:15:21

[every one of these items so that's like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m24s)
00:15:24

[this kind of simple but powerful concept](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m27s)
00:15:27

[of how we can do you know very fast](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m31s)
00:15:31

[gpu-accelerated loops and less code than](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m34s)
00:15:34

[it would have taken to actually write](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m38s)
00:15:38

[the loop and we don't have to worry](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m39s)
00:15:39

[about out of bounds conditions or](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m41s)
00:15:41

[anything like that it's all done for us](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m43s)
00:15:43

[so that's the trick here right and once](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m45s)
00:15:45

[you've got that matrix because intensive](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m48s)
00:15:48

[flow everything is a tensor we can call](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m51s)
00:15:51

[squared difference rather than just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m54s)
00:15:54

[regular difference and it gives us the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m57s)
00:15:57

[squares of those differences and then we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h15m59s)
00:15:59

[can sum over the last axis so the last](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m01s)
00:16:01

[access is the dimensions right so we're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m04s)
00:16:04

[just screwing your Euclidean distance](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m07s)
00:16:07

[here and so that's that's all this code](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m10s)
00:16:10

[does all right so this gives us every](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m14s)
00:16:14

[distance between every Anand of a and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m17s)
00:16:17

[every element of B](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m19s)
00:16:19

[okay so that's how we get to this point](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m21s)
00:16:21

[so then let's say we've gone through a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m27s)
00:16:27

[couple of loops right so at that bar for](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m31s)
00:16:31

[a couple of loops our is going to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m33s)
00:16:33

[contain a few initial centroids so we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m34s)
00:16:34

[now want to basically find out for every](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m39s)
00:16:39

[point how far away is it from its](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m44s)
00:16:44

[nearest initial centroid](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m47s)
00:16:47

[so when we go reduce men](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m49s)
00:16:49

[with access equal zero then we know that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m54s)
00:16:54

[that's going over the axis here because](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h16m57s)
00:16:57

[that's what we put into our or distances](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m00s)
00:17:00

[function so it's going to go through](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m02s)
00:17:02

[like it's reducing across that into that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m06s)
00:17:06

[axis so it's actually reducing across](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m09s)
00:17:09

[our centroids so at the end of this it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m11s)
00:17:11

[says alright this is for every piece of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m14s)
00:17:14

[our data how far it is away from its](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m18s)
00:17:18

[nearest centroid okay and that returns](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m21s)
00:17:21

[the actual distance right because we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m26s)
00:17:26

[said do the actual min so there's a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m28s)
00:17:28

[difference between men and argh](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m31s)
00:17:31

[the argh version so arc max then says](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m34s)
00:17:34

[okay now go through all of the points we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m37s)
00:17:37

[now know how far away they are from](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m41s)
00:17:41

[their closest centroid and tell me the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m43s)
00:17:43

[index of the one which is furthest away](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m46s)
00:17:46

[right so Arg max is a super handy](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m50s)
00:17:50

[function we used it quite a bit in part](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m53s)
00:17:53

[one of the course but it's well worth](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m54s)
00:17:54

[making sure we understand how it works](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m58s)
00:17:58

[I think intensive flow there I think](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h17m59s)
00:17:59

[they're getting rid of these reduced](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m04s)
00:18:04

[underscore prefixes I'm not sure I think](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m05s)
00:18:05

[I read that somewhere so in some version](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m08s)
00:18:08

[you may find this is called mean rather](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m11s)
00:18:11

[than reduced min I certainly hope they](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m13s)
00:18:13

[are for those of you who don't have such](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m16s)
00:18:16

[a computer science background a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m19s)
00:18:19

[reduction basically means taking](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m21s)
00:18:21

[something in a higher dimension and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m23s)
00:18:23

[squishing it down into something that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m24s)
00:18:24

[a lower dimension for example summing a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m26s)
00:18:26

[vector entering into it into a scalar](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m29s)
00:18:29

[this quarter reduction so it was a very](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m31s)
00:18:31

[tensorflow API assuming that everybody's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m33s)
00:18:33

[a computer scientist and that you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m36s)
00:18:36

[wouldn't book for me and you would look](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m37s)
00:18:37

[for reduce underscore mean](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m39s)
00:18:39

[so that's how we got that index and so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m43s)
00:18:43

[generally speaking you know you have to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m48s)
00:18:48

[be a bit careful of data types I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m51s)
00:18:51

[generally don't really notice about data](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m54s)
00:18:54

[type problems until I get the error but](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m56s)
00:18:56

[like if you get an error that kind of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m57s)
00:18:57

[says oh you passed in 64 into something](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h18m59s)
00:18:59

[that expected a 1032 you can always just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m02s)
00:19:02

[cast things like this okay so you need](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m04s)
00:19:04

[to index something within 32 so we just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m07s)
00:19:07

[have to cast it and so this returns the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m09s)
00:19:09

[extra point right append and then this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m12s)
00:19:12

[is very similar to numpy stacking](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m15s)
00:19:15

[together the initial centroids to create](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m18s)
00:19:18

[them a tensor of them okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m20s)
00:19:20

[so the code doesn't look at all weird or](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m24s)
00:19:24

[different but it's important to remember](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m31s)
00:19:31

[that when we run this code nothing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m33s)
00:19:33

[happens](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m35s)
00:19:35

[okay other than that it creates a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m36s)
00:19:36

[computation graph so when we call](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m38s)
00:19:38

[KDOT find initial centroids nothing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m44s)
00:19:44

[happens but because we're in an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m47s)
00:19:47

[interactive session we can now call eval](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m49s)
00:19:49

[and that actually runs it right and it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m53s)
00:19:53

[runs it and it actually takes the data](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m56s)
00:19:56

[that's returned from that and copies it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h19m59s)
00:19:59

[off the CPU and put that's very off the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m01s)
00:20:01

[GPU and puts it back in the CPU as an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m04s)
00:20:04

[umpire array so it's important to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m06s)
00:20:06

[remember that after call of eval we now](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m08s)
00:20:08

[have an actual genuine regular numpy](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m11s)
00:20:11

[array here and this is the thing that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m14s)
00:20:14

[makes us be able to write code that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m16s)
00:20:16

[looks a lot like pi torch code because](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m21s)
00:20:21

[we now know that we can take something](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m23s)
00:20:23

[that's an umpire array and turn it into](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m25s)
00:20:25

[a GPU tensor like that and we can take](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m27s)
00:20:27

[something that's a GPU tensor and turn](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m31s)
00:20:31

[it into an umpire array like that so I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m33s)
00:20:33

[don't know I suspect this might um](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m38s)
00:20:38

[despite makeup tensorflow](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m44s)
00:20:44

[developers shake at how horrible this is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m47s)
00:20:47

[it's not you know really quite the way](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m49s)
00:20:49

[you have to do things I think but it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m51s)
00:20:51

[yeah it's super easy and it seems to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m53s)
00:20:53

[work pretty well um this approach where](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h20m57s)
00:20:57

[we're calling eval you're doing it be a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m01s)
00:21:01

[bit careful if this was like inside a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m03s)
00:21:03

[loop that we were calling the eval and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m06s)
00:21:06

[we were copying back a really really big](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m08s)
00:21:08

[chunk of data to the GPU and the CPU](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m10s)
00:21:10

[again and again and again that would be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m13s)
00:21:13

[a performance nightmare all right so you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m16s)
00:21:16

[just you do need to kind of think about](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m18s)
00:21:18

[what's going on as you do it so we're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m19s)
00:21:19

[looking side the in away from the moment](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m22s)
00:21:22

[and just check anyway the results pretty](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m23s)
00:21:23

[fantastic as you can see this this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m27s)
00:21:27

[little hacky heuristic and does a great](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m30s)
00:21:30

[job and you know it's a hacky heuristic](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m32s)
00:21:32

[I've been using for decades now and it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m37s)
00:21:37

[a kind of thing which often doesn't](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m40s)
00:21:40

[appear in papers in this case of similar](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m43s)
00:21:43

[hacky heuristic did actually appear in a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m45s)
00:21:45

[paper in 2007 and even better one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m46s)
00:21:46

[appeared just last year but it's always](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m48s)
00:21:48

[worth thinking about like how can i pre](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m53s)
00:21:53

[process my data to kind of create get it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m56s)
00:21:56

[close to where I might want it to be and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h21m58s)
00:21:58

[often these kind of approaches are](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m00s)
00:22:00

[useful there's actually I don't know if](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m02s)
00:22:02

[we have time to maybe talk about it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m06s)
00:22:06

[someday but there's a probe to doing TTA](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m07s)
00:22:07

[principal components analysis which has](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m10s)
00:22:10

[a similar flavor basically finding](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m12s)
00:22:12

[random numbers and finding the farthest](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m14s)
00:22:14

[numbers away from them so it's a good](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m16s)
00:22:16

[general technique actually all right so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m19s)
00:22:19

[we've got our initial centroids what are](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m22s)
00:22:22

[we doing next](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m25s)
00:22:25

[well what we do next is we're going to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m26s)
00:22:26

[be doing more computation intensive flow](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m28s)
00:22:28

[with them so we want to copy them back](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m29s)
00:22:29

[to the GPU](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m31s)
00:22:31

[okay and so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m33s)
00:22:33

[copied them to the GPU before we do an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m37s)
00:22:37

[eval or anything later on we're going to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m39s)
00:22:39

[have to make sure we go global variable](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m41s)
00:22:41

[initializes run](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m43s)
00:22:43

[the question you explained what happens](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m46s)
00:22:46

[if you don't create interactive session](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m49s)
00:22:49

[so what the tensorflow authors decided](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m51s)
00:22:51

[to do in their wisdom was to generate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m55s)
00:22:55

[their own whole concept of namespaces](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h22m57s)
00:22:57

[and variables and whatever else so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m02s)
00:23:02

[rather than using pythons](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m05s)
00:23:05

[there's tensor clothes and so a session](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m07s)
00:23:07

[is basically a kind of like a named base](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m10s)
00:23:10

[that holds you know the computation](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m14s)
00:23:14

[graphs and the variables and so forth](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m16s)
00:23:16

[you can and then there's this concept of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m20s)
00:23:20

[a context manager which is basically](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m24s)
00:23:24

[where you have a wizz clause in Python](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m26s)
00:23:26

[and you say like with this session now](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m28s)
00:23:28

[you're going to do stuff in this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m30s)
00:23:30

[namespace and then there's a concept of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m32s)
00:23:32

[a graph you can have multiple](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m35s)
00:23:35

[computation graphs you can say with this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m36s)
00:23:36

[graph you know create these various](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m38s)
00:23:38

[computations where it comes in very](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m39s)
00:23:39

[handy is if you want to say like run](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m43s)
00:23:43

[this graph on this GPU or you know stick](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m46s)
00:23:46

[this variable on that CPU so without an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m50s)
00:23:50

[interactive session you basically have](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h23m58s)
00:23:58

[to create that session you have to say](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m00s)
00:24:00

[which session to use using a wisk laws](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m01s)
00:24:01

[and then like there's many layers of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m03s)
00:24:03

[that so within that you can then create](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m06s)
00:24:06

[name scopes variable scopes and blah](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m08s)
00:24:08

[blah blah so then the annoying thing is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m10s)
00:24:10

[the vast majority of tutorial code out](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m13s)
00:24:13

[there uses all of these concepts right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m15s)
00:24:15

[it's as if like all of python 0 and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m18s)
00:24:18

[variables and modules doesn't exist and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m21s)
00:24:21

[you use tensorflow for everything so I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m25s)
00:24:25

[wanted to show you that you don't have](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m27s)
00:24:27

[to use any of these concepts pretty much](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m28s)
00:24:28

[like thank you for the question ok hey I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m32s)
00:24:32

[haven't fight](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m37s)
00:24:37

[but it's thinking goodness but have you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m38s)
00:24:38

[tried so because your whatever there's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m41s)
00:24:41

[six clusters up there um and if you have](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m45s)
00:24:45

[given if you have initially said I have](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m49s)
00:24:49

[seven clusters or eight clusters but you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m52s)
00:24:52

[refine that see you hit your six sheets](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m55s)
00:24:55

[all the sudden start getting two codes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h24m57s)
00:24:57

[are very close to previous existing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m00s)
00:25:00

[control so it seems like you could come](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m02s)
00:25:02

[how intelligently define a width of a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m05s)
00:25:05

[cluster or look for a jump and things](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m10s)
00:25:10

[dropping down and how far apart they are](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m14s)
00:25:14

[on the cluster](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m15s)
00:25:15

[yeah and programmatically come up with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m16s)
00:25:16

[the weighting decide the number yeah](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m20s)
00:25:20

[yeah I think you could you know maybe](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m22s)
00:25:22

[then you're using k-means I don't know](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m26s)
00:25:26

[like yeah I think it's a fascinating](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m28s)
00:25:28

[question I haven't seen that done there](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m31s)
00:25:31

[are certainly papers about figuring out](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m36s)
00:25:36

[the number of clusters and k-means so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m42s)
00:25:42

[maybe during the week you check one out](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m44s)
00:25:44

[what it's a tends to flow that'll be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m46s)
00:25:46

[that'll be really interesting and i just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m49s)
00:25:49

[wanted to follow up what you said about](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m52s)
00:25:52

[session to kind of emphasize that with a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m54s)
00:25:54

[lot of tutorials you could make the code](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m57s)
00:25:57

[simpler by using an interactive session](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h25m59s)
00:25:59

[in a jupiter notebook instead yeah I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m01s)
00:26:01

[remember when Rachel was going through a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m04s)
00:26:04

[tensor flow crossed a while ago and she](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m05s)
00:26:05

[kept on banging her head against the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m08s)
00:26:08

[desk with sessions and variables cots](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m09s)
00:26:09

[and whatever else and we kind of yeah](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m11s)
00:26:11

[that was part of what led us to think](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m14s)
00:26:14

[okay let's let's simplify all that all](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m15s)
00:26:15

[right so I'm step one is to take our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m18s)
00:26:18

[initial centroids and copy them onto the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m21s)
00:26:21

[GPU so we now have a symbol representing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m22s)
00:26:22

[those so the next step in the k-means](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m25s)
00:26:25

[algorithm is to take every point and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m29s)
00:26:29

[assign them to a cluster which is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m32s)
00:26:32

[basically to say for every point which](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m35s)
00:26:35

[which which of the centroids is the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m37s)
00:26:37

[closest so that's what assigned to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m38s)
00:26:38

[nearest does we'll get to that in a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m46s)
00:26:46

[moment but let's pretend we've done it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m48s)
00:26:48

[this will now be a list](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m49s)
00:26:49

[of rich centroid is the closest or every](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m52s)
00:26:52

[data point so then we need one more](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h26m56s)
00:26:56

[piece of tensor flow concepts which is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m00s)
00:27:00

[we want to update an existing we want to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m05s)
00:27:05

[update an existing variable with some](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m11s)
00:27:11

[new data and so we can actually call](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m14s)
00:27:14

[update centroids to basically do that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m18s)
00:27:18

[updating and I'll show you how that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m21s)
00:27:21

[works as well so basically the idea is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m22s)
00:27:22

[that we're going to loop through doing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m25s)
00:27:25

[this again and again and again but when](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m28s)
00:27:28

[we just do it once you can actually see](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m33s)
00:27:33

[it's nearly perfect already so it's a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m36s)
00:27:36

[pretty powerful pretty powerful idea as](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m40s)
00:27:40

[long as your initial cluster centers are](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m42s)
00:27:42

[good so let's see how this works assign](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m45s)
00:27:45

[the nearest](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m48s)
00:27:48

[it's a single line of code](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m56s)
00:27:56

[now the reason is a single line of code](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h27m58s)
00:27:58

[is we already have the code to find the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m00s)
00:28:00

[distance between every piece of data and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m02s)
00:28:02

[its centroid](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m06s)
00:28:06

[now rather than calling TF reduce min](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m10s)
00:28:10

[which returned the distance to its](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m13s)
00:28:13

[nearest centroid we call TS dot argh men](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m15s)
00:28:15

[to get the index of its nearest centroid](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m18s)
00:28:18

[so generally speaking the the hard bit](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m22s)
00:28:22

[of doing this kind of highly vectorized](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m25s)
00:28:25

[code is figuring out this number which](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m27s)
00:28:27

[is what access are we working with right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m31s)
00:28:31

[and so it's a good idea to actually like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m33s)
00:28:33

[write down on a piece of paper you know](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m35s)
00:28:35

[for each of your 10 sores it's like it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m38s)
00:28:38

[time by batch by row by column or](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m40s)
00:28:40

[whatever let make sure you know what](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m43s)
00:28:43

[every basis represents when I'm creating](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m45s)
00:28:45

[these algorithms I'm constantly printing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m49s)
00:28:49

[out the shape of things and another](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m53s)
00:28:53

[really simple trick that a lot of people](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m57s)
00:28:57

[don't do this is make sure that your](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h28m59s)
00:28:59

[different dimensions actually have](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m01s)
00:29:01

[different sizes so when you're playing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m03s)
00:29:03

[around with setting things don't have a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m06s)
00:29:06

[batch size of ten and an N of ten and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m07s)
00:29:07

[the number of dimensions of ten right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m09s)
00:29:09

[but I find it much easier to think of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m11s)
00:29:11

[real numbers so like have a batch size](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m14s)
00:29:14

[of 8 and an ad of can and a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m16s)
00:29:16

[dimensionality of four right because](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m18s)
00:29:18

[every time you print out the shape](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m20s)
00:29:20

[you're finding out exactly what](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m21s)
00:29:21

[everything is okay so this is going to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m22s)
00:29:22

[return the nearest indices so then we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m25s)
00:29:25

[can go ahead and update the centroids so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m32s)
00:29:32

[here is update centroids and suddenly we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m35s)
00:29:35

[have some crazy function and this is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m38s)
00:29:38

[where tensorflow is super handy it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m41s)
00:29:41

[full of crazy functions and if you know](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m46s)
00:29:46

[the computer science term for the thing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m49s)
00:29:49

[you're trying to do it generally has](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m53s)
00:29:53

[it's generally called that right and so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m55s)
00:29:55

[it's the only other way to find it is to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h29m58s)
00:29:58

[do lots and lots of searching through](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m01s)
00:30:01

[the documentation so in general taking a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m03s)
00:30:03

[set of data and sticking it into](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m09s)
00:30:09

[multiple chunks of data according to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m12s)
00:30:12

[some kind of criteria it's called](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m15s)
00:30:15

[partitioning in computer science so I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m18s)
00:30:18

[got a bit lucky when I first looked for](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m20s)
00:30:20

[this I googled the tensor flow](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m22s)
00:30:22

[petition and bang this thing pops up so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m24s)
00:30:24

[let's take a look at it and this is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m27s)
00:30:27

[where like reading about GPU programming](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m35s)
00:30:35

[in general is very helpful because in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m39s)
00:30:39

[GPU programming there's this kind of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m41s)
00:30:41

[smallish subset of things which](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m43s)
00:30:43

[everything else is built on and one of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m46s)
00:30:46

[them is partitioning](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m48s)
00:30:48

[[Music]](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m49s)
00:30:49

[okay so here we have TF dynamic](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m55s)
00:30:55

[partition partition the data into some](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h30m58s)
00:30:58

[number of partitions using some indices](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m06s)
00:31:06

[and generally speaking it's easier to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m09s)
00:31:09

[just look at some code so here's our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m12s)
00:31:12

[data we're going to create two](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m14s)
00:31:14

[partitions they're calling them clusters](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m16s)
00:31:16

[and it's going to go like this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m19s)
00:31:19

[d-rose partition zeros first first zeros](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m23s)
00:31:23

[so 10 will go to the zeroth partition 20](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m27s)
00:31:27

[will go to the zeroth partition 30 will](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m31s)
00:31:31

[go to the first partition okay this is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m33s)
00:31:33

[exactly what we want right so this is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m36s)
00:31:36

[the nice thing is that there's a lot of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m38s)
00:31:38

[these you can see all this stuff right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m40s)
00:31:40

[there's so many functions available](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m42s)
00:31:42

[often there's the exact function you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m45s)
00:31:45

[need and here it is right so we just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m47s)
00:31:47

[take our list of indices convert it to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m48s)
00:31:48

[os/2 in 32 s Parfitt our data the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m51s)
00:31:51

[indices and the number of clusters and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m55s)
00:31:55

[we're done right this is now a separate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h31m57s)
00:31:57

[array basically a zipper tensor so each](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m04s)
00:32:04

[of our clusters](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m07s)
00:32:07

[so now that we have done that we can](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m10s)
00:32:10

[then figure out what is the mean of each](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m13s)
00:32:13

[of those clusters so the mean of each of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m17s)
00:32:17

[those clusters is our new centroid right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m20s)
00:32:20

[so what we're doing is we're saying okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m22s)
00:32:22

[which points are the closest to this one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m26s)
00:32:26

[and we're kind of going okay these](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m28s)
00:32:28

[points are the closest to this one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m31s)
00:32:31

[okay what's the average of those points](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m32s)
00:32:32

[right that's all that happens from here](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m35s)
00:32:35

[to here](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m37s)
00:32:37

[okay so that's taking the mean of those](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m39s)
00:32:39

[points](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m41s)
00:32:41

[and then we can basically see okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m43s)
00:32:43

[that's our new partition that's our new](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m45s)
00:32:45

[add new clusters so then just join them](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m48s)
00:32:48

[all together concatenate them together](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m54s)
00:32:54

[okay so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h32m57s)
00:32:57

[except for that dynamic partitions well](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m03s)
00:33:03

[I mean in fact including that dynamic](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m06s)
00:33:06

[conditions it was incredibly simple but](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m08s)
00:33:08

[it is incredibly simple because we had a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m09s)
00:33:09

[function that did exactly what we wanted](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m11s)
00:33:11

[so because we assigned a variable up](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m12s)
00:33:12

[here we have to call initializer but run](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m15s)
00:33:15

[and then of course before we can do](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m19s)
00:33:19

[anything with this tensor we have to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m21s)
00:33:21

[call eval to actually call the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m25s)
00:33:25

[computation graph and copy it back to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m27s)
00:33:27

[our CPU okay so that's all those tips](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m30s)
00:33:30

[so then we want to replace the contents](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m37s)
00:33:37

[of current centroids with the contents](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m41s)
00:33:41

[of updated centroids and so to do that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m44s)
00:33:44

[we can't just say equals everything's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m50s)
00:33:50

[different intensive law you have to call](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m53s)
00:33:53

[dot assign right so this is the same as](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m54s)
00:33:54

[basically saying current centroids](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m57s)
00:33:57

[equals updated centroids but it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h33m59s)
00:33:59

[creating a computation graph that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m01s)
00:34:01

[basically does that assignment on the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m03s)
00:34:03

[GPU how can we extrapolate this to other](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m06s)
00:34:06

[non numeric data types such as words](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m12s)
00:34:12

[images](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m14s)
00:34:14

[well they're all numeric data types](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m16s)
00:34:16

[really so an image is absolutely a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m20s)
00:34:20

[numeric data type so it's just a bunch](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m24s)
00:34:24

[of pixels you just have to decide what](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m28s)
00:34:28

[distance measure you want which](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m31s)
00:34:31

[generally just means deciding you're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m34s)
00:34:34

[probably using you city and distance but](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m35s)
00:34:35

[are you doing it in pixel space or](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m37s)
00:34:37

[you're picking one of the activation](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m39s)
00:34:39

[layers in a neural net for words you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m41s)
00:34:41

[would create a word vector for your webs](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m46s)
00:34:46

[there's nothing specifically](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m51s)
00:34:51

[two-dimensional about this it's working](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m53s)
00:34:53

[as many dimensions as we like and and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m56s)
00:34:56

[that's really the whole point and I'm](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h34m59s)
00:34:59

[hoping that maybe during the week some](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m01s)
00:35:01

[people will start to play around with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m02s)
00:35:02

[some higher dimensional data sets to get](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m04s)
00:35:04

[a feel for how this works particularly](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m06s)
00:35:06

[if you can get it working on CT scans](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m09s)
00:35:09

[that would be fascinating using the five](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m10s)
00:35:10

[dimensional clustering we talked about](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m13s)
00:35:13

[okay so to use what it looks like in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m15s)
00:35:15

[total if we weren't using an interactive](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m20s)
00:35:20

[session](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m22s)
00:35:22

[you basically say where's TF session](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m23s)
00:35:23

[let's create the session but as default](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m27s)
00:35:27

[that sets it to the current session and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m30s)
00:35:30

[then within the width block we can now](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m32s)
00:35:32

[run things and then Kay don't run](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m34s)
00:35:34

[there's all the stuff we just saw so if](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m38s)
00:35:38

[we could okay don't run here it is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m40s)
00:35:40

[right so Kay don't run does all of those](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m45s)
00:35:45

[steps so this is how you can create a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m47s)
00:35:47

[complete computation graph in tensor](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m50s)
00:35:50

[flow using a notebook you do each one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m53s)
00:35:53

[one step at a time once you put it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m55s)
00:35:55

[working you put it all together right so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m57s)
00:35:57

[you can see find initial centroids eval](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h35m59s)
00:35:59

[put it back into a variable again](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m03s)
00:36:03

[assigned a nearest at the centroids](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m07s)
00:36:07

[because we created a variable in the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m12s)
00:36:12

[process there we didn't have to rerun](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m15s)
00:36:15

[global variable initializer we could](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m17s)
00:36:17

[have avoided this I guess by not calling](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m21s)
00:36:21

[eval and just treating this as a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m25s)
00:36:25

[variable the whole time but it does](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m27s)
00:36:27

[is fresh lime and then we just look](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m29s)
00:36:29

[through a bunch of times](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m35s)
00:36:35

[calling centroid sort of sign updated](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m36s)
00:36:36

[set droids](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m42s)
00:36:42

[oh I think I see a bug what we should be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m46s)
00:36:46

[doing after that is then calling up site](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m50s)
00:36:50

[centroids each time so there you go](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m55s)
00:36:55

[I'll fix that during the week and then](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h36m58s)
00:36:58

[the nice thing is because I've used a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m01s)
00:37:01

[normal place and full loop here and I'm](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m02s)
00:37:02

[calling eval each time it means I can](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m07s)
00:37:07

[check](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m12s)
00:37:12

[Oh have have any of the cluster](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m12s)
00:37:12

[centroids moved and if they haven't then](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m17s)
00:37:17

[I will stop working right so it makes it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m21s)
00:37:21

[very easy to kind of create dynamic for](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m24s)
00:37:24

[loops which could be quite tricky](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m26s)
00:37:26

[sometimes with tensorflow otherwise okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m28s)
00:37:28

[so that is the the tensorflow](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m34s)
00:37:34

[algorithm from end to end](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m42s)
00:37:42

[Rachel you want to pick out an ano your](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m47s)
00:37:47

[question](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m51s)
00:37:51

[so actually I kind of am helping start a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m53s)
00:37:53

[company the I don't know if you've seen](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h37m58s)
00:37:58

[my talks on ted.com that I kind of show](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m02s)
00:38:02

[this demo of this interactive labeling](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m04s)
00:38:04

[tool a friend of mine said that he](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m08s)
00:38:08

[wanted to start a company to actually](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m12s)
00:38:12

[make that and commercialize it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m13s)
00:38:13

[so I guess my short answer is I'm](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m15s)
00:38:15

[helping somebody do that so I think](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m17s)
00:38:17

[that's pretty cool](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m19s)
00:38:19

[more generally I've mentioned before I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m20s)
00:38:20

[think that best thing to do is always to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m23s)
00:38:23

[scratch an edge so pick whatever you've](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m26s)
00:38:26

[been passionate about or something](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m29s)
00:38:29

[that's just driven you crazy and you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m31s)
00:38:31

[know fix it if you have the benefit of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m33s)
00:38:33

[being able to take enough time to do](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m37s)
00:38:37

[absolutely anything you want I felt like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m39s)
00:38:39

[the three most important areas for](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m42s)
00:38:42

[applying deep learning when I last](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m43s)
00:38:43

[talked which was two or three years ago](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m48s)
00:38:48

[were medicine robotics and satellite](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m50s)
00:38:50

[imagery because at that time computer](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m53s)
00:38:53

[vision was the only area that was](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m57s)
00:38:57

[remotely maturer really for machine](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h38m59s)
00:38:59

[learning deep learning and those three](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m02s)
00:39:02

[areas or were areas that very heavily](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m05s)
00:39:05

[used computer vision or could heavily](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m09s)
00:39:09

[use computer vision and were potentially](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m11s)
00:39:11

[very large markets medicine is probably](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m14s)
00:39:14

[the largest industry in the world I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m17s)
00:39:17

[think it's three trillion dollars in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m18s)
00:39:18

[America alone robotics isn't currently](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m20s)
00:39:20

[that large but at some point it probably](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m24s)
00:39:24

[will become the largest industry in the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m26s)
00:39:26

[world if you know everything we do](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m27s)
00:39:27

[manually is replaced with automated](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m31s)
00:39:31

[approaches and satellite imagery is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m33s)
00:39:33

[basically used by military intelligence](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m36s)
00:39:36

[so you have some of the biggest budgets](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m38s)
00:39:38

[in the world so yeah I guess those three](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m40s)
00:39:40

[areas take it going oh no I got some](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m44s)
00:39:44

[higher weather fish okay well next time](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m49s)
00:39:49

[alright I know it's like a break soon](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m51s)
00:39:51

[before I do I might just introduce what](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h39m56s)
00:39:56

[we're going to be looking at next so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m02s)
00:40:02

[we're going to start on our NLP and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m07s)
00:40:07

[specifically translation deep dive and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m11s)
00:40:11

[we're going to be really following on](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m13s)
00:40:13

[from the end-to-end memory networks from](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m15s)
00:40:15

[last week the one of the things that I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m18s)
00:40:18

[find kind of most interesting and was](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m24s)
00:40:24

[challenging and setting up this course](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m27s)
00:40:27

[is coming up with good problem sets](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m28s)
00:40:28

[which are like hard enough to be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m31s)
00:40:31

[interesting and easy enough to be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m34s)
00:40:34

[possible and often other people already](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m38s)
00:40:38

[done that so I was lucky enough that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m42s)
00:40:42

[somebody else had already shown a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m43s)
00:40:43

[example of using sequence tool sequence](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m45s)
00:40:45

[learning for what they called spelling](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m47s)
00:40:47

[bee and basically we start with this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m51s)
00:40:51

[thing called the CMU pronouncing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m54s)
00:40:54

[dictionary which has things that look](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m55s)
00:40:55

[like this the wiki followed by a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h40m58s)
00:40:58

[phonetic description of how to read the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m03s)
00:41:03

[where key so the way these work this is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m07s)
00:41:07

[actually specifically an American](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m12s)
00:41:12

[pronunciation dictionary the continents](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m14s)
00:41:14

[pretty straightforward the vowel sounds](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m19s)
00:41:19

[have a number at the end showing how](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m22s)
00:41:22

[much stress is an h1 right so 0 1 or 2](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m24s)
00:41:24

[so in this case you can see that the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m27s)
00:41:27

[middle one is where most of the stress](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m29s)
00:41:29

[is so it's risky](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m31s)
00:41:31

[so here is the letter A and it is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m34s)
00:41:34

[pronounced ah okay so the goal that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m38s)
00:41:38

[we're going to be looking out after the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m43s)
00:41:43

[break is to do the other direction which](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m44s)
00:41:44

[is to start with how do you say it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m48s)
00:41:48

[I'm turn it into how do you spell it um](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m51s)
00:41:51

[this is quite a difficult question](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m55s)
00:41:55

[because though English is really weird](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m57s)
00:41:57

[to spell and the number of phonemes and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h41m59s)
00:41:59

[will necessarily match the thumb the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m03s)
00:42:03

[number of letters so this is going to be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m08s)
00:42:08

[where we're going to start and then](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m11s)
00:42:11

[we're going to try and solve this puzzle](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m12s)
00:42:12

[and then we'll use the solutions in this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m13s)
00:42:13

[puzzle to try and learn to translate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m15s)
00:42:15

[French into English using the same basic](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m18s)
00:42:18

[idea so let's have a ten minute break](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m21s)
00:42:21

[and we'll come back at 7:40 so just to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m23s)
00:42:23

[clarify this will make sure everybody](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m29s)
00:42:29

[understands the problem we're solving](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m30s)
00:42:30

[here so the problem we're solving is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m32s)
00:42:32

[we're going to be told here is how to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m35s)
00:42:35

[pronounce something okay and then we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m36s)
00:42:36

[have to say okay here it said a speller](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m39s)
00:42:39

[all right so this is going to be our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m41s)
00:42:41

[input and this is going to be our target](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m42s)
00:42:42

[so this is like a translation problem](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m45s)
00:42:45

[that's writ simpler](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m48s)
00:42:48

[have pre-trained phoneme vectors or pre](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m52s)
00:42:52

[change letter vectors so they'd have to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m57s)
00:42:57

[do this by building a model I'm going to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h42m59s)
00:42:59

[have to create some embeddings of arrow](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m01s)
00:43:01

[so in general the first steps necessary](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m04s)
00:43:04

[to create an NLP model tends to look](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m08s)
00:43:08

[very very similar I feel like I've done](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m13s)
00:43:13

[them in a thousand different ways now](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m16s)
00:43:16

[and at some point I really need to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m18s)
00:43:18

[abstract the cell laughs into us into a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m20s)
00:43:20

[simple set of functions that we use](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m22s)
00:43:22

[again and again and again but let's go](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m23s)
00:43:23

[through it and if you've got any](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m27s)
00:43:27

[questions about any of the code or steps](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m29s)
00:43:29

[or anything let me know](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m32s)
00:43:32

[um so the basic pronounciation](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m34s)
00:43:34

[dictionary is just a text file and I'm](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m40s)
00:43:40

[going to just grab the lines which are](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m43s)
00:43:43

[actual words so they have to start with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m48s)
00:43:48

[a letter now something which I have](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h43m51s)
00:43:51

[actually it's gonna match that okay so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m00s)
00:44:00

[we're going to go through every line of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m03s)
00:44:03

[the text file here's the handy things](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m05s)
00:44:05

[that a lot of people don't realize you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m07s)
00:44:07

[can do in Python when you call open that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m08s)
00:44:08

[returns a generator which lists all of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m11s)
00:44:11

[the lines so I see if you just go for L](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m13s)
00:44:13

[in open blah that's now looping through](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m16s)
00:44:16

[every line in that file okay so I can](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m20s)
00:44:20

[then say filter those which start with a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m23s)
00:44:23

[which start with a lowercase letter okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m27s)
00:44:27

[so sorry boo start with an uppercase](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m31s)
00:44:31

[letter they're all uppercase and then](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m33s)
00:44:33

[strip off any white space and spirit on](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m37s)
00:44:37

[white space so that's the basically the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m42s)
00:44:42

[steps necessary to separate out the word](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m45s)
00:44:45

[from the pronunciation and then the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m49s)
00:44:49

[pronunciation is just white space](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m52s)
00:44:52

[delimited so we can then fit that and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m55s)
00:44:55

[that the steps necessary to get the word](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h44m59s)
00:44:59

[and the pronunciation as a set of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m00s)
00:45:00

[phonemes so as we tend to pretty much](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m03s)
00:45:03

[always do with these language models we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m07s)
00:45:07

[next need to get a list of like water](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m09s)
00:45:09

[all of the vocabulary items so in this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m11s)
00:45:11

[case the vocabulary items are the other](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m13s)
00:45:13

[possible phonemes so we can create a set](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m15s)
00:45:15

[of every possible phoneme and then we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m18s)
00:45:18

[can sort it and what we always like to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m24s)
00:45:24

[do is to get an extra an extra character](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m28s)
00:45:28

[or an extra object in position zero](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m33s)
00:45:33

[because remember we use zero for padding](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m36s)
00:45:36

[right so that's why I stick I'm going to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m38s)
00:45:38

[use underscore is our special padding](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m41s)
00:45:41

[letter here so let's take an underscore](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m44s)
00:45:44

[at the front so here are the first five](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m45s)
00:45:45

[phonemes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m48s)
00:45:48

[this is our special padding one which is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m49s)
00:45:49

[going to be index zero and then there's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m52s)
00:45:52

[an R with three different level stress](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m54s)
00:45:54

[and so forth okay now the next thing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h45m57s)
00:45:57

[that we can to do anytime we've got a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m02s)
00:46:02

[list of vocabulary items is to create a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m04s)
00:46:04

[list in the opposite direction so we go](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m06s)
00:46:06

[from phoneme to index we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m08s)
00:46:08

[just a dictionary where we enumerate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m12s)
00:46:12

[through all of our phonemes and put it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m14s)
00:46:14

[in the opposite order](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m17s)
00:46:17

[so from phoneme to index now we've used](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m18s)
00:46:18

[this approach 2,000 times before but](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m23s)
00:46:23

[it's going to make sure everybody](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m26s)
00:46:26

[understands that when you use enumerate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m27s)
00:46:27

[in Python it doesn't just return each](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m30s)
00:46:30

[phoneme but returns a tuple that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m32s)
00:46:32

[contains the index of the phoneme and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m35s)
00:46:35

[then the phoneme itself so that's the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m37s)
00:46:37

[key and the value so then if we go value](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m39s)
00:46:39

[comma key that's now the phoneme](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m42s)
00:46:42

[followed by the index and so if we turn](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m45s)
00:46:45

[that into a dictionary we now have a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m47s)
00:46:47

[dictionary which you can give it a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m49s)
00:46:49

[phoneme and return it and index here's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m50s)
00:46:50

[all the letters of English again with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m54s)
00:46:54

[our special underscore at the front and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h46m56s)
00:46:56

[we've got one extra thing we'll talk](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m00s)
00:47:00

[about later which is asterisks so that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m01s)
00:47:01

[a list of letters and so again to go](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m04s)
00:47:04

[from letter to letter index we just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m07s)
00:47:07

[create a dictionary which reverses it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m10s)
00:47:10

[again okay so now that we've got our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m12s)
00:47:12

[phoneme to index and letter to index we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m19s)
00:47:19

[can use that to convert this data into](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m22s)
00:47:22

[numeric data right which is like what we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m26s)
00:47:26

[always do with these language models we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m29s)
00:47:29

[end up with just a list of indices we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m31s)
00:47:31

[can pick some maximum length word so I'm](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m35s)
00:47:35

[just going to say 15 and so we're going](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m38s)
00:47:38

[to create a dictionary which maps from](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m41s)
00:47:41

[each word to a list of phonemes we're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m45s)
00:47:45

[going to get the indexes for them yes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m49s)
00:47:49

[Rachel okay so this dictionary](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m51s)
00:47:51

[comprehension is a little bit awkward so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m55s)
00:47:55

[I thought this would be a good](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h47m59s)
00:47:59

[opportunity to talk about dictionary](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m00s)
00:48:00

[comprehensions and list comprehensions](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m02s)
00:48:02

[for a moment so we're going to pause](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m03s)
00:48:03

[this in a moment but first of all let's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m06s)
00:48:06

[look at a couple of examples of list](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m08s)
00:48:08

[comprehensions so the first thing to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m11s)
00:48:11

[note is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m13s)
00:48:13

[when you go something like this the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m14s)
00:48:14

[string X Y Z or the string here - is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m15s)
00:48:15

[perfectly happy to consider that a list](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m20s)
00:48:20

[of letters so the placing considers this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m21s)
00:48:21

[the same as being a list of X comma Y](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m23s)
00:48:23

[comma debt so you can think of this as](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m25s)
00:48:25

[two lists list of X Y Z and almost of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m27s)
00:48:27

[ABC so here is the simplest possible](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m30s)
00:48:30

[list comprehension okay so go through](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m34s)
00:48:34

[every element of a and put that into a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m38s)
00:48:38

[list so if I call that then it returns](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m41s)
00:48:41

[exactly what I started with okay that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m45s)
00:48:45

[not very interesting what if now we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m47s)
00:48:47

[replaced o with another list](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m50s)
00:48:50

[comprehension okay so what that's going](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h48m56s)
00:48:56

[to do is it's now going to return a list](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m00s)
00:49:00

[for each list okay so this is one way of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m03s)
00:49:03

[pulling things out of sub lists is to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m08s)
00:49:08

[basically take the thing that was here](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m11s)
00:49:11

[and replace it with a new list](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m13s)
00:49:13

[comprehension and that's going to give](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m15s)
00:49:15

[you a list of Lists now the reason I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m16s)
00:49:16

[wanted to talk about this is because](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m20s)
00:49:20

[it's quite confusing in Python you can](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m22s)
00:49:22

[also write this which is different so in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m24s)
00:49:24

[this case I'm going for each object in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m28s)
00:49:28

[our a list and then for each object in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m32s)
00:49:32

[that sub list and you see what's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m36s)
00:49:36

[different here I don't have to like in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m39s)
00:49:39

[square brackets right it's just all laid](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m40s)
00:49:40

[out next to each other so I find it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m42s)
00:49:42

[really confusing but the idea is you're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m45s)
00:49:45

[meant to think of this is just being](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m47s)
00:49:47

[like a normal for loop inside a for loop](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m49s)
00:49:49

[right and so what this does is it goes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m51s)
00:49:51

[through X Y Z and then ABC and then in X](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m53s)
00:49:53

[Y Z to go to your each of x and Y and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h49m58s)
00:49:58

[Zed but because there's no embedded set](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m00s)
00:50:00

[of square brackets that actually ends up](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m02s)
00:50:02

[flattening the list okay so we just saw](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m04s)
00:50:04

[um I think](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m12s)
00:50:12

[we're about to see an example of the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m17s)
00:50:17

[square bracket version and pretty soon](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m19s)
00:50:19

[we'll be seeing an example of this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m22s)
00:50:22

[version as well these are both used for](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m23s)
00:50:23

[it's very useful to be able to flatten a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m25s)
00:50:25

[list that's very useful to be able to do](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m27s)
00:50:27

[things with sub lists and then just to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m30s)
00:50:30

[be aware that anytime you have any kind](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m33s)
00:50:33

[of expression like this you can replace](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m36s)
00:50:36

[the thing at the here with any](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m38s)
00:50:38

[expression you like right so we could](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m42s)
00:50:42

[say for example we could say o dot upper](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h50m45s)
00:50:45

[okay so you can basically map different](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m01s)
00:51:01

[computations to each element of a list](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m05s)
00:51:05

[and then the second thing you can do is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m06s)
00:51:06

[put an F here to filter it if o 0 take](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m10s)
00:51:10

[all day](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m19s)
00:51:19

[very wrong there sorry](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m22s)
00:51:22

[oh thank you okay okay so that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m26s)
00:51:26

[basically the idea you can create any](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m36s)
00:51:36

[list comprehension you know you like by](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m39s)
00:51:39

[putting computations here filters here](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m40s)
00:51:40

[and optionally multiple lists of lists](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m43s)
00:51:43

[here the other thing you can do is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m46s)
00:51:46

[replace the square brackets with curly](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m50s)
00:51:50

[brackets in which case you need to put](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m51s)
00:51:51

[something before a colon and something](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m54s)
00:51:54

[after a colon the thing before is your](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m56s)
00:51:56

[key nothing after is your value so here](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h51m58s)
00:51:58

[we're going for oh and then there's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m01s)
00:52:01

[another thing you can do which is if the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m04s)
00:52:04

[thing you're looping through is a bunch](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m05s)
00:52:05

[of lists or tuples or nothing like that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m08s)
00:52:08

[you can pull them out into two pieces](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m10s)
00:52:10

[like so so this is the word and this is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m12s)
00:52:12

[the list of phonemes so we're going to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m16s)
00:52:16

[have the lowercase word will be our keys](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m19s)
00:52:19

[in our dictionary and the values will be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m22s)
00:52:22

[lists](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m27s)
00:52:27

[so we're doing it just like we did down](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m28s)
00:52:28

[here and the list will be let's go](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m30s)
00:52:30

[through each phoneme and go phoneme to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m33s)
00:52:33

[index okay so now we have something that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m38s)
00:52:38

[maps from every word to its list of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m41s)
00:52:41

[phoneme indexes all right so that's that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m43s)
00:52:43

[we can find out what the maximum length](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m52s)
00:52:52

[of editing is in terms of how many](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m56s)
00:52:56

[phonemes that are and we can do that by](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h52m58s)
00:52:58

[again we can just go through every one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m01s)
00:53:01

[of those dictionary items calling](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m03s)
00:53:03

[lengths on each one and then doing a max](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m06s)
00:53:06

[on that okay so there is the maximum](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m08s)
00:53:08

[length so you can see like combining](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m11s)
00:53:11

[list comprehensions with other functions](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m14s)
00:53:14

[is also powerful all right so finally](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m17s)
00:53:17

[we're going to create our nice square](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m26s)
00:53:26

[arrays normally we do this with CAD](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m29s)
00:53:29

[sequences just through a change we're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m33s)
00:53:33

[going to do this manually this time so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m36s)
00:53:36

[the key is that we start out by creating](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m40s)
00:53:40

[two arrays of zeros because all the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m42s)
00:53:42

[padding is going to be 0 right so if we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m47s)
00:53:47

[start off with all zeros and we can just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m48s)
00:53:48

[fill in the non zeros so this is going](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m51s)
00:53:51

[to be our all of our phonemes this is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m53s)
00:53:53

[going to be our actual spelling that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m56s)
00:53:56

[our target labels so then we go through](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h53m58s)
00:53:58

[all of our and we've permitted them](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m00s)
00:54:00

[randomly so randomly ordered things in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m02s)
00:54:02

[the pronunciation dictionaries and we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m05s)
00:54:05

[put in size input all of the items from](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m09s)
00:54:09

[the pronunciation dictionary and into](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m15s)
00:54:15

[labels we go lesser to indexed all right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m17s)
00:54:17

[so we now have one thing called input](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m22s)
00:54:22

[once in court labels that contains nice](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m24s)
00:54:24

[rectangular arrays padded with zeros](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m27s)
00:54:27

[containing exactly what we want](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m31s)
00:54:31

[okay I'm not going to worry about this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m35s)
00:54:35

[line yet because we're not going to use](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m37s)
00:54:37

[it for the starting point](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m38s)
00:54:38

[so anyway you see dick something just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m42s)
00:54:42

[ignore that for now we'll get back to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m44s)
00:54:44

[that later](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m45s)
00:54:45

[trains have split is a very handy](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m48s)
00:54:48

[function from SK learn that takes all of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m50s)
00:54:50

[these lists and splits them all in the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m53s)
00:54:53

[same way with this proportion in the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h54m58s)
00:54:58

[test set and so input becomes input](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m00s)
00:55:00

[train and input test labels becomes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m03s)
00:55:03

[labels train and labels test so that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m06s)
00:55:06

[pretty handy we've often written that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m08s)
00:55:08

[manually but this is a nice quick way to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m11s)
00:55:11

[do it when you've got lots of lists to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m14s)
00:55:14

[do](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m16s)
00:55:16

[um okay so just to have a look at how](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m17s)
00:55:17

[many phonemes we have a no vocabulary](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m22s)
00:55:22

[there are 70 how many letters in our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m23s)
00:55:23

[vocab read is 28 that's us we've got](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m26s)
00:55:26

[that underscore and the star as well](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m28s)
00:55:28

[okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m31s)
00:55:31

[so let's go ahead and create the model](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m32s)
00:55:32

[so here's the basic idea](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m36s)
00:55:36

[[Music]](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m43s)
00:55:43

[the model has three parts the first is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m46s)
00:55:46

[an embedding right so the embedding is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m52s)
00:55:52

[going to take every one of our phonemes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m56s)
00:55:56

[okay max Lenti is the maximum number of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h55m59s)
00:55:59

[phonemes we have in any pronunciation](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m02s)
00:56:02

[and each one of those phonemes is going](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m06s)
00:56:06

[to go into an embedding right and the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m09s)
00:56:09

[look up for that embedding is the vocab](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m13s)
00:56:13

[size for phonemes which I think was 70](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m17s)
00:56:17

[and then the output you know is whatever](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m20s)
00:56:20

[we decide what dimensionality who you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m23s)
00:56:23

[want and in experimentation I found 120](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m25s)
00:56:25

[seems to work pretty well I was](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m28s)
00:56:28

[surprised by how high that number is but](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m31s)
00:56:31

[there you go it is we started out with a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m34s)
00:56:34

[list of phonemes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m39s)
00:56:39

[all right list of 13](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m43s)
00:56:43

[this embedding we now have a list of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m49s)
00:56:49

[embeddings so this is like 70 and this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m53s)
00:56:53

[is like 120 okay so the basic idea is to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h56m58s)
00:56:58

[take this big thing which is all of our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m05s)
00:57:05

[phonemes embedded and we want to turn it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m09s)
00:57:09

[into a single distributed representation](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m11s)
00:57:11

[which contains all of the richness of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m15s)
00:57:15

[what this pronunciation says later on](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m19s)
00:57:19

[we're going to be doing the same thing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m23s)
00:57:23

[with an English sentence right and so we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m24s)
00:57:24

[know that when you have a sequence and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m27s)
00:57:27

[you want to turn it into a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m29s)
00:57:29

[representation one great way of doing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m32s)
00:57:32

[that is with an RNN now why an RN](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m34s)
00:57:34

[because an RNN we know is good at](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m40s)
00:57:40

[dealing with things like state and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m43s)
00:57:43

[memory right so when we're looking at](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m45s)
00:57:45

[translation we really want something](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m48s)
00:57:48

[which can remember like where are we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m51s)
00:57:51

[right so let's say we were let's say we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m54s)
00:57:54

[were doing this simple phonetic](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m57s)
00:57:57

[translation the idea of you know have we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h57m59s)
00:57:59

[just had a C because if we just had a C](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m02s)
00:58:02

[then the H is going to make a totally](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m04s)
00:58:04

[different sound too if we haven't just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m07s)
00:58:07

[had a C right so an iron n we think is a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m08s)
00:58:08

[good way to do this kind of thing and in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m15s)
00:58:15

[general this whole class of models](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m17s)
00:58:17

[remember is called seek to seek sequence](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m19s)
00:58:19

[to sequence models which is where we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m24s)
00:58:24

[start with some arbitrary length](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m26s)
00:58:26

[sequence and we produce some arbitrary](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m29s)
00:58:29

[length sequence and so the general idea](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m31s)
00:58:31

[here is taking that arbitrary length](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m33s)
00:58:33

[sequence and turning it into a six size](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m35s)
00:58:35

[representation using an hour a ten is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m38s)
00:58:38

[probably a good first step and you're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m40s)
00:58:40

[using dropout in your Alice TN is it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m44s)
00:58:44

[best practice to do drop out across time](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m47s)
00:58:47

[you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m50s)
00:58:50

[[Music]](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m50s)
00:58:50

[so okay so looking ahead I'm actually](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h58m52s)
00:58:52

[going to be using quite a few layers of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m00s)
00:59:00

[RNN so to make that easier I've still in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m01s)
00:59:01

[drawing mode so to make that easier](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m06s)
00:59:06

[we've created a get RNN function which](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m10s)
00:59:10

[just and so we can you can put anything](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m14s)
00:59:14

[you like here GRU or LS TM or whatever](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m15s)
00:59:15

[and yes indeed I am using drop out the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m18s)
00:59:18

[kind of drop out that you use in our in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m24s)
00:59:24

[an R and N is slightly different to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m26s)
00:59:26

[normal drop out it turns out that if the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m28s)
00:59:28

[particular thing that you drop out it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m33s)
00:59:33

[best to have some the same things at](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m35s)
00:59:35

[every time step in an RNN there's a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m37s)
00:59:37

[really good paper that explains why this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m41s)
00:59:41

[is the case and shows that this is the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m43s)
00:59:43

[case so this is why there's a special](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m45s)
00:59:45

[drop out parameter inside the air and in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m48s)
00:59:48

[and clear us it does its proper RNN](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m51s)
00:59:51

[style drop out so yeah so we'll you know](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m54s)
00:59:54

[I put in a tiny bit of drop out here and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m57s)
00:59:57

[if it turns out that we over theater we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=00h59m59s)
00:59:59

[can always increase it if we don't we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m05s)
01:00:05

[could always turn it to zero so so what](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m08s)
01:00:08

[we're going to do is yes Rachel I want](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m13s)
01:00:13

[more question about that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m16s)
01:00:16

[can you explain consume less than equals](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m17s)
01:00:17

[GPU so yeah always do that they're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m20s)
01:00:20

[deeply I don't know if you remember but](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m27s)
01:00:27

[when we looked at like doing harridans](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m31s)
01:00:31

[from scratch last year we learnt that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m33s)
01:00:33

[you could like actually combine the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m37s)
01:00:37

[matrices together and led to a single](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m39s)
01:00:39

[matrix computation if you do that it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m41s)
01:00:41

[going to use that more memory but it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m43s)
01:00:43

[allows the GPU to be more highly](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m45s)
01:00:45

[parallel so basically if you look at the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m48s)
01:00:48

[case documentation or Oteri's of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m51s)
01:00:51

[different things you can use but since](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m53s)
01:00:53

[we're using a GPU you probably always](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m55s)
01:00:55

[want to say consume less equals GPU](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h00m57s)
01:00:57

[okay the other thing that we learned](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m01s)
01:01:01

[about last year is bi-directional arrow](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m04s)
01:01:04

[names and maybe the best way to come at](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m07s)
01:01:07

[this is actually to go all the way back](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m10s)
01:01:10

[and remind you how RNs work we haven't](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m13s)
01:01:13

[done much revision but it's been a while](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m19s)
01:01:19

[since we put our an enzyme at the detail](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m20s)
01:01:20

[so just remind you this is kind of our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m23s)
01:01:23

[drawing of a totally basic neural net](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m26s)
01:01:26

[square is input Circle is intermediate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m30s)
01:01:30

[activations hidden and triangles output](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m35s)
01:01:35

[and arrows represent affine](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m38s)
01:01:38

[transformations with nonlinearities we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m41s)
01:01:41

[can then have multiple copies of those](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m47s)
01:01:47

[to create deeper convolutions for](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m49s)
01:01:49

[example and so the other thing we can do](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m52s)
01:01:52

[is actually we can have inputs going in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h01m58s)
01:01:58

[at different places so in this case if](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m01s)
01:02:01

[we were trying to predict the third](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m04s)
01:02:04

[character from first two characters we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m05s)
01:02:05

[can use a totally standard neural](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m08s)
01:02:08

[network and actually have input coming](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m09s)
01:02:09

[in at two different places and then we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m11s)
01:02:11

[realized that we could kind of make this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m18s)
01:02:18

[arbitrarily large but what we should](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m19s)
01:02:19

[probably do then is make everything](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m22s)
01:02:22

[where an input is going to a hidden](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m24s)
01:02:24

[state feeds the same matrix so this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m26s)
01:02:26

[color coding remember represents the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m28s)
01:02:28

[same weight matrix so hidden to hidden](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m31s)
01:02:31

[would be the same weight matrix and hit](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m33s)
01:02:33

[into output and is a separate weight](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m35s)
01:02:35

[matrix so then to remind you we realize](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m37s)
01:02:37

[that we could draw that more simply like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m43s)
01:02:43

[this okay so our it ends when they're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m44s)
01:02:44

[unrolled just look like a normal neural](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m48s)
01:02:48

[network at which some of the weight](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m52s)
01:02:52

[matrices are tied together and if this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m53s)
01:02:53

[is not ringing a bell go back to I think](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m56s)
01:02:56

[it's lessons 5 where we actually build](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h02m59s)
01:02:59

[these weight matrices from scratch and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m02s)
01:03:02

[tie them together manually so that will](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m04s)
01:03:04

[hopefully remind you of what's going on](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m09s)
01:03:09

[now importantly we can then take one of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m11s)
01:03:11

[those our and ends and have the output](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m18s)
01:03:18

[go to the input of another errand and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m21s)
01:03:21

[these are stacks arrogance and stacks](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m24s)
01:03:24

[are and ends basically give us you know](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m26s)
01:03:26

[richer computations in our recurrent](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m28s)
01:03:28

[neural Nets and this is what it looks](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m31s)
01:03:31

[like when we unroll it so you can see](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m36s)
01:03:36

[here that we've got multiple inputs](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m40s)
01:03:40

[coming in going through multiple layers](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m42s)
01:03:42

[and creating multiple outputs but of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m44s)
01:03:44

[course we don't have to create multiple](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m47s)
01:03:47

[outputs](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m48s)
01:03:48

[you could also present networking you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m50s)
01:03:50

[could also get rid of these two](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m56s)
01:03:56

[triangles here and have just one output](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h03m57s)
01:03:57

[and remember in care out the difference](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m00s)
01:04:00

[is whether or not we say return](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m02s)
01:04:02

[sequences equals true or return](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m04s)
01:04:04

[sequences equals false this one your](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m06s)
01:04:06

[thing here is return sequences equals](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m09s)
01:04:09

[true this one here is return sequences](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m11s)
01:04:11

[equals false so what we've got is input](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m16s)
01:04:16

[train has 97 thousand words each one is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m27s)
01:04:27

[of length 16 it's 15 characters long](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m34s)
01:04:34

[plus the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m38s)
01:04:38

[the padding and then no sorry 1616](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m45s)
01:04:45

[proteins long-haul stop plug possibly](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m51s)
01:04:51

[with padding if necessary and then](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m53s)
01:04:53

[labels is 15 because we chose earlier on](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h04m57s)
01:04:57

[that I max length would be a 15 long](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m00s)
01:05:00

[spelling so phonemes don't match two](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m02s)
01:05:02

[letters exactly so after the embedding](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m06s)
01:05:06

[so if we take one of those tens of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m15s)
01:05:15

[thousands of words remember it was](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m18s)
01:05:18

[length](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m19s)
01:05:19

[um](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m22s)
01:05:22

[of length sub 4 phonemes length 16 all](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m25s)
01:05:25

[right and then we're putting it into an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m31s)
01:05:31

[embedding matrix which is 70s by 120 and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m34s)
01:05:34

[the reason it's 70 is that each of these](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m45s)
01:05:45

[phonemes contains a number between](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m47s)
01:05:47

[naught to 69 okay so basically we go](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m51s)
01:05:51

[through and we get each one of these](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h05m59s)
01:05:59

[indexes and we look up to find it so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m00s)
01:06:00

[this is fives here then we find number](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m01s)
01:06:01

[five here okay and so we end up with 16](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m04s)
01:06:04

[by 120 and then part two of the question](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m11s)
01:06:11

[says are we then taking a sequence of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m19s)
01:06:19

[these phonemes represented as 120](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m22s)
01:06:22

[dimensional floating-point vectors and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m24s)
01:06:24

[using an RNN to create a sequence of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m26s)
01:06:26

[word to bec embeddings which we will](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m29s)
01:06:29

[then reverse to actual words so we're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m31s)
01:06:31

[not going to use words avec here right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m34s)
01:06:34

[we're Tyvek is a particular sort of pre](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m35s)
01:06:35

[trained embeddings we're not using pre](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m37s)
01:06:37

[trained embeddings we have to create our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m40s)
01:06:40

[own inventing we're creating phoneme in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m42s)
01:06:42

[betting's so if somebody else would add](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m46s)
01:06:46

[your own wanted to do something else](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m48s)
01:06:48

[with phonemes and we like save the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m50s)
01:06:50

[result of this we could provide phoneme](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m53s)
01:06:53

[Tyvek and you could download them and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m55s)
01:06:55

[use the fast a I pre train phoneme to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h06m57s)
01:06:57

[bec embeddings this is how embeddings](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m01s)
01:07:01

[basically get created right the people](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m03s)
01:07:03

[build models starting with random](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m05s)
01:07:05

[embeddings and then](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m07s)
01:07:07

[save those embeddings and make them](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m10s)
01:07:10

[available for other people to use as](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m11s)
01:07:11

[indian misinterpreting it but I thought](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m15s)
01:07:15

[that question was getting it the second](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m17s)
01:07:17

[set of embeddings when you want to get](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m20s)
01:07:20

[back to your words right so let's wait](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m22s)
01:07:22

[until we get there because we're going](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m27s)
01:07:27

[to create letters not words and then we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m29s)
01:07:29

[just join the letters together so there](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m31s)
01:07:31

[won't be any word to the next year so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m34s)
01:07:34

[we've got as far as creating our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m35s)
01:07:35

[embeddings and then we we've then got an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m39s)
01:07:39

[R and n which is going to take our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m42s)
01:07:42

[embeddings and attempt to turn it into a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m46s)
01:07:46

[single vector that's kind of what an RNN](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m49s)
01:07:49

[does so we've got here return sequences](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h07m53s)
01:07:53

[by default is true so this first r and n](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m00s)
01:08:00

[returns something which is just as long](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m04s)
01:08:04

[as we started with right and so if you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m06s)
01:08:06

[want to stack our and end on top of each](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m09s)
01:08:09

[other every one of them is return](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m10s)
01:08:10

[sequences equals true until the last one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m12s)
01:08:12

[isn't right so that's why we have false](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m14s)
01:08:14

[here right so at the end of this one it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m17s)
01:08:17

[goes gives us a single vector which is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m20s)
01:08:20

[the final state the other important](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m21s)
01:08:21

[piece is bi-directional and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m26s)
01:08:26

[bi-directional you can totally do this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m28s)
01:08:28

[manually yourself you take your input](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m30s)
01:08:30

[and feed it into an R and N and then you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m34s)
01:08:34

[reverse your input and feed it into a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m37s)
01:08:37

[different narrative and then just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m40s)
01:08:40

[concatenate the two together](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m42s)
01:08:42

[so care us has something which does that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m43s)
01:08:43

[for you which is called bi-directional](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m46s)
01:08:46

[and bi-directional actually requires you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m49s)
01:08:49

[to pass it an R and n right so it takes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m51s)
01:08:51

[an RN n and returns two copies of that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m55s)
01:08:55

[are against ax on top of each other](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h08m58s)
01:08:58

[one of which reverses its input and so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m00s)
01:09:00

[why is that interesting well that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m03s)
01:09:03

[interesting because often in language](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m05s)
01:09:05

[what happens later influences what comes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m07s)
01:09:07

[before for example in French the gender](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m11s)
01:09:11

[of your local lawyer your definite](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m15s)
01:09:15

[article depends on the noun](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m18s)
01:09:18

[refers to so you need to go to look](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m21s)
01:09:21

[backwards or forwards in both directions](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m22s)
01:09:22

[to figure out how to match those two](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m26s)
01:09:26

[together or in any language with temps](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m27s)
01:09:27

[you know what verb do you use depends on](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m30s)
01:09:30

[the tense and often also depends on the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m35s)
01:09:35

[details about the subject and the object](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m37s)
01:09:37

[so we want to be able to both look](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m39s)
01:09:39

[forwards and look backwards right so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m41s)
01:09:41

[that's why we want two copies of the RNN](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m44s)
01:09:44

[one which goes from left to right and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m47s)
01:09:47

[one which goes from right to left and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m49s)
01:09:49

[indeed we could assume that when you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m51s)
01:09:51

[spell things I'm not actually sure how](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m53s)
01:09:53

[this work but when you spell things](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m55s)
01:09:55

[depending on what the latest dressers](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m57s)
01:09:57

[might be or the later details of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h09m59s)
01:09:59

[athletics might be might change how you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m02s)
01:10:02

[pronounce things earlier on](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m04s)
01:10:04

[as the bi-directional RNN can cat to our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m08s)
01:10:08

[limbs or does it's Jackson](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m11s)
01:10:11

[it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m16s)
01:10:16

[if you end up with the same you end up](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m19s)
01:10:19

[with the same number of dimensions you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m25s)
01:10:25

[had before but it basically doubles the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m28s)
01:10:28

[number of features that you have so in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m32s)
01:10:32

[this case we have 240 so I just had](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m35s)
01:10:35

[doubled so and I think we had one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m40s)
01:10:40

[question here](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m44s)
01:10:44

[so the currency level is about order](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m46s)
01:10:46

[regarding to level of our men or lsdm](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m50s)
01:10:50

[would be the input of the length of a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m52s)
01:10:52

[pizza box alone underscore drag that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m57s)
01:10:57

[the 16 yeah okay the number 70 here is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h10m59s)
01:10:59

[it like all the possible characters of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m02s)
01:11:02

[yeah all about the phonemes we're going](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m04s)
01:11:04

[from phonemes or you okay okay okay so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m07s)
01:11:07

[let's simplify this down a little bit](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m14s)
01:11:14

[again and basically say we started out](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m17s)
01:11:17

[with a set of embeddings and we've gone](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m22s)
01:11:22

[through two layers well we've gone](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m27s)
01:11:27

[through a bi-directional RNN and then we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m30s)
01:11:30

[feed that to a second Aaron in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m32s)
01:11:32

[right to create a representation of this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m36s)
01:11:36

[ordered list of fillings right and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m40s)
01:11:40

[specifically this represented a vector](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m42s)
01:11:42

[okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m45s)
01:11:45

[so X at this point is a vector okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m46s)
01:11:46

[because return sequences equals false](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m49s)
01:11:49

[that vector once we've trained this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m52s)
01:11:52

[thing the idea is it represents](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m55s)
01:11:55

[everything that important there is to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h11m58s)
01:11:58

[know about this ordered list of phonemes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m01s)
01:12:01

[everything that we could possibly these](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m03s)
01:12:03

[know in order to spell it okay so the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m04s)
01:12:04

[idea is we could now take that vector](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m08s)
01:12:08

[and feed it into a new RNN or even a few](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m10s)
01:12:10

[layers of RNN okay and that are an N](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m16s)
01:12:16

[could basically go through and be with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m20s)
01:12:20

[returned sequences equals true this time](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m23s)
01:12:23

[it could spit out at every time step](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m26s)
01:12:26

[what it thinks the next letter in this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m29s)
01:12:29

[spelling is right and so this is how a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m31s)
01:12:31

[sequence to sequence works is one one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m34s)
01:12:34

[part which is called the n coda takes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m37s)
01:12:37

[our initial sequence](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m42s)
01:12:42

[into a distributed representation into a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m46s)
01:12:46

[into a vector using generally speaking](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m49s)
01:12:49

[some stacked iron ends then the second](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m53s)
01:12:53

[piece called the decoder takes the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m56s)
01:12:56

[output of the encoder and passes that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h12m59s)
01:12:59

[into a separate stack of our it ends](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m04s)
01:13:04

[with return sequences equals true and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m06s)
01:13:06

[those are n ends are taught to then](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m09s)
01:13:09

[generate the labels in this case two](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m12s)
01:13:12

[spellings](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m16s)
01:13:16

[when I later kate's the english](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m16s)
01:13:16

[sentences now in Caruth it's not](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m19s)
01:13:19

[convenient to create an R and n by](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m26s)
01:13:26

[handing it some initial state some](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m31s)
01:13:31

[initial hidden status that's not really](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m34s)
01:13:34

[how care ass likes to do things Tara](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m36s)
01:13:36

[expects to be handed a a list of input](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m38s)
01:13:38

[problem number 1 problem number 2 if you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m44s)
01:13:44

[do hand it to an R and n just at the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m48s)
01:13:48

[start it's quite hard for the RN to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m50s)
01:13:50

[remember the whole time what is this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m53s)
01:13:53

[word I meant to be translating right it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m56s)
01:13:56

[kind of has to keep two things that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m58s)
01:13:58

[head one is like what's the word I meant](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h13m59s)
01:13:59

[to be spelling and the second is like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m02s)
01:14:02

[what's the letter I'm trying to spell](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m04s)
01:14:04

[right now so what we do with care us is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m06s)
01:14:06

[we actually take this whole state and we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m09s)
01:14:09

[copy it so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m15s)
01:14:15

[case we're trying to create a word that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m18s)
01:14:18

[could be up to 15 letters long so in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m22s)
01:14:22

[other words 15 time steps so we take](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m28s)
01:14:28

[this and we actually make 15 copies of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m33s)
01:14:33

[it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m36s)
01:14:36

[okay and those 15 copies of our final](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m44s)
01:14:44

[encoder state becomes the input to our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m48s)
01:14:48

[decoder R and n so it seems kind of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m51s)
01:14:51

[clunky right but it's actually not](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m55s)
01:14:55

[difficult to do in chaos we just go like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m56s)
01:14:56

[this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h14m58s)
01:14:58

[we take the output from our encoder and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m01s)
01:15:01

[we repeat it 15 times all right so we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m06s)
01:15:06

[literally have 15 identical copies of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m11s)
01:15:11

[the same sector and so that's how Clara](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m14s)
01:15:14

[expects to see things and it also turns](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m17s)
01:15:17

[out that it's actually you get better](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m20s)
01:15:20

[results when you pass into the R and n](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m22s)
01:15:22

[the state that it needs again and again](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m24s)
01:15:24

[at every time step so we're basically](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m26s)
01:15:26

[passing in saying something saying we're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m28s)
01:15:28

[trying to spell this word we're trying](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m30s)
01:15:30

[to spell this work we're trying to spell](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m32s)
01:15:32

[this word we're trying to spell this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m33s)
01:15:33

[word and then as the R and n goes along](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m34s)
01:15:34

[it's generating its own internal state](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m37s)
01:15:37

[figuring out like what have we spelt so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m41s)
01:15:41

[far and what are we going to have to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m43s)
01:15:43

[spell next there's a question why can't](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m44s)
01:15:44

[we have return sequences equals true for](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m48s)
01:15:48

[the second bi-directional illa and not](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m51s)
01:15:51

[bi-directional for the second LS TM we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m55s)
01:15:55

[only have one bi-directional calais TM](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h15m58s)
01:15:58

[we don't want return sequence with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m00s)
01:16:00

[equals true here because we're trying to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m03s)
01:16:03

[create a representation of the whole](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m06s)
01:16:06

[word we're trying to spell so there's no](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m09s)
01:16:09

[point having something saying here's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m12s)
01:16:12

[reputation representation of the first](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m15s)
01:16:15

[phoneme of the first two of the first](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m17s)
01:16:17

[three or the first four or the first](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m20s)
01:16:20

[five because we don't really know like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m21s)
01:16:21

[exactly which letter of the output is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m25s)
01:16:25

[going to correspond to which phoneme of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m27s)
01:16:27

[the input and particularly when we get](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m29s)
01:16:29

[to translation it can get much harder](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m30s)
01:16:30

[like some languages totally reverse the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m32s)
01:16:32

[subject and object order or put the verb](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m34s)
01:16:34

[somewhere else so that's why we try to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m36s)
01:16:36

[package up the whole thing into a single](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m38s)
01:16:38

[piece of state which has all of the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m41s)
01:16:41

[information necessary to build our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m44s)
01:16:44

[target sequence so remember these](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m46s)
01:16:46

[sequence to sequence models are also](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m49s)
01:16:49

[used for things like image captioning](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m53s)
01:16:53

[right so with image captioning you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h16m56s)
01:16:56

[wouldn't want to have like something](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m00s)
01:17:00

[that created a representation separately](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m02s)
01:17:02

[for every pixel you know when you're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m05s)
01:17:05

[trying to capture an image you want a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m07s)
01:17:07

[single representation which is like this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m08s)
01:17:08

[is something that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m11s)
01:17:11

[how contains all of the information](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m13s)
01:17:13

[about what this is the picture of or if](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m14s)
01:17:14

[you're doing neural language translation](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m18s)
01:17:18

[here's my English sentence that turns](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m21s)
01:17:21

[into a representation of everything that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m24s)
01:17:24

[it means so that I can generate my](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m25s)
01:17:25

[french sentence](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m28s)
01:17:28

[we're going to be seeing later how we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m30s)
01:17:30

[can use return sequences equals true](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m32s)
01:17:32

[when we look at tension models but for](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m34s)
01:17:34

[now we're just going to keep seeing some](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m37s)
01:17:37

[simple](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m39s)
01:17:39

[the question is then I have an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m43s)
01:17:43

[underlying question regarding why don't](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m44s)
01:17:44

[need discrete text problems the same way](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m46s)
01:17:46

[we do images images have relationships](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m49s)
01:17:49

[between pixels and shapes that are](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m51s)
01:17:51

[complex and rely on positional](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m53s)
01:17:53

[information why doesn't that work with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m55s)
01:17:55

[word or phoneme embeddings well it does](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h17m57s)
01:17:57

[it absolutely does and indeed we can use](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m01s)
01:18:01

[convolutional models but if you remember](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m06s)
01:18:06

[back to lesson 5 we talked about some of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m09s)
01:18:09

[the challenges with that so if you're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m16s)
01:18:16

[trying to create something which can has](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m19s)
01:18:19

[you know some kind of markup block like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m24s)
01:18:24

[this it has to both remember that oh you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m26s)
01:18:26

[know you've just opened up a piece of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m29s)
01:18:29

[markup you're in the middle of it then](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m30s)
01:18:30

[in here you have to remember that you're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m32s)
01:18:32

[actually inside a comment block so that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m34s)
01:18:34

[at the end remember to close it this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m35s)
01:18:35

[kind of long-term dependency and memory](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m38s)
01:18:38

[and stateful representation becomes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m41s)
01:18:41

[increasingly difficult to do with CNN's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m44s)
01:18:44

[as they get longer it's not impossible](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m46s)
01:18:46

[by any means but our an ends are one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m49s)
01:18:49

[good way of of doing this but it is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m52s)
01:18:52

[critical that we start with embedding](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h18m57s)
01:18:57

[because where else an image we are](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m00s)
01:19:00

[already given you know valued numbers](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m03s)
01:19:03

[that really represent the image that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m06s)
01:19:06

[not true with text right so with text](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m09s)
01:19:09

[where you have to use embeddings to turn](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m11s)
01:19:11

[it into these nice numeric](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m13s)
01:19:13

[representations are nervous and on](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m16s)
01:19:16

[generic term she writes or specific](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m22s)
01:19:22

[network uses lsdm yes but there's other](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m25s)
01:19:25

[types of computers GRU](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m28s)
01:19:28

[remember yeah yeah so careful are it in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m30s)
01:19:30

[Solaris support like yeah weird all the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m33s)
01:19:33

[ones we did in the last part of the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m37s)
01:19:37

[course so we looked in simple r NN g iu](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m38s)
01:19:38

[and Emmas TM / so it looked like the LCM](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m41s)
01:19:41

[which is the best preserved task no no](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m44s)
01:19:44

[not at all um the GI is knows TM is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m48s)
01:19:48

[pretty similar](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m52s)
01:19:52

[not worth thinking about too much okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h19m53s)
01:19:53

[all right so at this point](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m01s)
01:20:01

[here when](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m06s)
01:20:06

[now have 15 copies of the 15 copies of X](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m09s)
01:20:09

[right and so we now pass that into](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m18s)
01:20:18

[two more layers of our den so if this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m25s)
01:20:25

[here is our encoder and this here is our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m28s)
01:20:28

[decoder now there's nothing we'd get](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m31s)
01:20:31

[particularly in care us to say this is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m33s)
01:20:33

[an encoder to the decoder the important](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m35s)
01:20:35

[thing is the return sequences equals](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m38s)
01:20:38

[false here and the repeat vector here](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m40s)
01:20:40

[right so like this what does it have to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m43s)
01:20:43

[do well somehow it has to take this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m45s)
01:20:45

[single summary and create some layers of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m48s)
01:20:48

[RN ends until then at the end we say](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m52s)
01:20:52

[okay here's a dense layer okay and it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m56s)
01:20:56

[time distributed so remember that means](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h20m59s)
01:20:59

[that we actually have 15 dense layers](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m02s)
01:21:02

[and so each of these dense layers now](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m06s)
01:21:06

[has a soft max activation which means](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m09s)
01:21:09

[that we basically can then do an Ag Max](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m14s)
01:21:14

[on that to create our final list of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m17s)
01:21:17

[letters so this is kind of our reverse](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m20s)
01:21:20

[embedding if you like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m23s)
01:21:23

[so the model is very little code okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m28s)
01:21:28

[and once we've built it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m33s)
01:21:33

[and again if things like this are](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m35s)
01:21:35

[mysterious to you go back and relook at](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m39s)
01:21:39

[lessons four five and six remind you how](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m42s)
01:21:42

[these embeddings work and how these kind](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m47s)
01:21:47

[of time distributed dense works to give](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m49s)
01:21:49

[us effectively a kind of reversed](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m51s)
01:21:51

[embedding so that's our model starts](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m53s)
01:21:53

[with our phoneme input into that time](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h21m59s)
01:21:59

[tribute dead output we can then compile](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m01s)
01:22:01

[that our targets are just indexes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m05s)
01:22:05

[remember we turn them into indexes so we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m09s)
01:22:09

[use this handy sparse categorical cross](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m12s)
01:22:12

[entropy it's just the same as our normal](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m14s)
01:22:14

[categorical cross entropy but rather](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m17s)
01:22:17

[than one hot encoding we just skip the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m19s)
01:22:19

[whole one code encoding and just leave](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m21s)
01:22:21

[it as an index](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m22s)
01:22:22

[and we can go ahead and sit plussing in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m25s)
01:22:25

[our training data so that was our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m28s)
01:22:28

[rectangular data of the phoneme indexes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m31s)
01:22:31

[our labels and then we can use some](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m36s)
01:22:36

[valid test set data that we set aside as](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m40s)
01:22:40

[well](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m43s)
01:22:43

[so we've hit that for a while I found](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m44s)
01:22:44

[that the first three o'clock the loss](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m48s)
01:22:48

[went down like this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m50s)
01:22:50

[the secondary epochs that went down like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m51s)
01:22:51

[this it seemed to be flattening out so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m53s)
01:22:53

[that's where as far as I stopped it so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m56s)
01:22:56

[we can now see how well that worked](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h22m59s)
01:22:59

[now what I wanted to do was not just say](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m04s)
01:23:04

[what percentage of letters are correct](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m07s)
01:23:07

[because that doesn't really give you the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m10s)
01:23:10

[right sense at all okay what I really](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m12s)
01:23:12

[want to know is what percentage of words](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m14s)
01:23:14

[are correct so that's all this little](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m16s)
01:23:16

[eval chaos function does it takes the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m19s)
01:23:19

[thing that I'm trying to evaluate called](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m24s)
01:23:24

[predict on it it then does the AG max as](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m26s)
01:23:26

[usual to take that softmax and turn it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m31s)
01:23:31

[into a specific number which which](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m34s)
01:23:34

[character is this and then I want to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m36s)
01:23:36

[check whether it's true for all of the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m39s)
01:23:39

[characters that the real character](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m43s)
01:23:43

[equals the predicted character okay so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m46s)
01:23:46

[this is going to return true only if](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m49s)
01:23:49

[every single item in the word is correct](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m52s)
01:23:52

[and so then taking the mean of that it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m55s)
01:23:55

[going to tell us what percentage of the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m58s)
01:23:58

[words to get totally right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h23m59s)
01:23:59

[and unfortunately the answer is not very](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m03s)
01:24:03

[many 26% so let's look at some examples](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m05s)
01:24:05

[so we can go through 20 words at random](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m10s)
01:24:10

[and we can print out all of the phonemes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m14s)
01:24:14

[with dashes between so here's an example](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m18s)
01:24:18

[of some phonemes we can print out the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m20s)
01:24:20

[actual word and we can print out our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m24s)
01:24:24

[prediction so here is a whole bunch of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m27s)
01:24:27

[words that I don't really recognize](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m33s)
01:24:33

[Turtle Bay shuns it should be spelt like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m36s)
01:24:36

[that oh we spelled it like that slightly](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m40s)
01:24:40

[wrong so you can see some of the time](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m43s)
01:24:43

[the mistakes it makes you pretty clear](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m48s)
01:24:48

[so laro could be spelt like that but](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m50s)
01:24:50

[this seems perfectly reasonable](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m55s)
01:24:55

[sometimes on the other hand it's way off](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h24m57s)
01:24:57

[and interestingly what I what you find](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m01s)
01:25:01

[is that most of the time when it's way](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m05s)
01:25:05

[off](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m08s)
01:25:08

[I found a chance to be with the longer](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m08s)
01:25:08

[words and the reason for that it's that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m11s)
01:25:11

[the longer the words so like this one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m17s)
01:25:17

[where it's terrible it's by far the most](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m21s)
01:25:21

[phonemes I think one two three four five](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m24s)
01:25:24

[six seven eight nine ten eleven phonemes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m26s)
01:25:26

[so if we had to somehow create a single](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m30s)
01:25:30

[representation that contained all of the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m34s)
01:25:34

[information of all of those eleven](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m37s)
01:25:37

[phonemes in a single vector and that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m40s)
01:25:40

[hard to do right and then that single](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m44s)
01:25:44

[vector got passed](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m46s)
01:25:46

[I mean copied that passed to the decoder](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m47s)
01:25:47

[and that was everything it had to try to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m50s)
01:25:50

[create this output okay so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h25m54s)
01:25:54

[that's the problem with this basic](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m01s)
01:26:01

[encoder/decoder](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m03s)
01:26:03

[method and indeed here is a graph from](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m04s)
01:26:04

[from the model that means from the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m10s)
01:26:10

[tanker which originally](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m14s)
01:26:14

[introduced attentional models I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m19s)
01:26:19

[this is the knurl translation what it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m23s)
01:26:23

[showed is that as the as the sentence](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m25s)
01:26:25

[lengths got bigger the standard approach](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m29s)
01:26:29

[which we're talking about the standard](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m35s)
01:26:35

[encoder/decoder approach the accuracy](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m36s)
01:26:36

[absolutely died so what these](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m40s)
01:26:40

[researchers did was that they built a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m45s)
01:26:45

[new kind of R and n model coordinate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m47s)
01:26:47

[attentional model and with the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m50s)
01:26:50

[attentional model](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m52s)
01:26:52

[the accuracy actually stayed pretty good](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m55s)
01:26:55

[so goal number one the next couple](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h26m58s)
01:26:58

[weapon system may not have a cold](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m01s)
01:27:01

[anymore](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m03s)
01:27:03

[yeah so basically we're going to finish](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m07s)
01:27:07

[our deep dive into neuro translation and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m11s)
01:27:11

[then we're going to look at time theory](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m14s)
01:27:14

[so that we're not specifically looking](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m16s)
01:27:16

[at time theories it turns out that the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m17s)
01:27:17

[best way that I've found the time series](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m19s)
01:27:19

[is not specific to time to use at all](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m22s)
01:27:22

[that you're certainly reinforcement](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m24s)
01:27:24

[learning was something I was planning to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m30s)
01:27:30

[cover but I just haven't found almost](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m33s)
01:27:33

[any good examples of it actually being](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m38s)
01:27:38

[used in practice to solve important real](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m40s)
01:27:40

[problems and indeed when you look at the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m42s)
01:27:42

[you can see in the paper in the last](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m48s)
01:27:48

[week or two about using evolutionary](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m50s)
01:27:50

[strategies for reinforcement learning](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m51s)
01:27:51

[basically it turns out that using](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m53s)
01:27:53

[basically random search is better than](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m55s)
01:27:55

[reinforcement learning that this paper](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h27m59s)
01:27:59

[by the way like ridiculously overhyped](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m03s)
01:28:03

[these evolutionary strategies is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m05s)
01:28:05

[something that I was working on over 20](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m07s)
01:28:07

[years ago and in those days these are](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m10s)
01:28:10

[genetic algorithms as we called them](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m14s)
01:28:14

[used much more sophisticated methods](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m16s)
01:28:16

[than sick minds brand new evolutionary](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m18s)
01:28:18

[strategies so people are like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m21s)
01:28:21

[rediscovering these randomized Mediterra](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m23s)
01:28:23

[sticks which is great that they're still](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m25s)
01:28:25

[far behind where they were at forty](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m29s)
01:28:29

[years ago but fire ahead of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m30s)
01:28:30

[reinforcement learning approaches so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m34s)
01:28:34

[given I try to teach things which I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m37s)
01:28:37

[think actually going to stand the test](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m39s)
01:28:39

[of time I'm not at all convinced at any](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m41s)
01:28:41

[current technique for reinforcement](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m43s)
01:28:43

[learning to understand the test of time](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m45s)
01:28:45

[so I don't think we're gonna touch that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m46s)
01:28:46

[part three yeah I think before that we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m49s)
01:28:49

[might have a plateau where where we do](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m55s)
01:28:55

[practical machine learning for coders](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h28m59s)
01:28:59

[talk about decision tree ensembles and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m02s)
01:29:02

[training test clips and stuff like that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m05s)
01:29:05

[um yeah and then yeah we'll see where we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m09s)
01:29:09

[are that yet I'm sure Rachel knows I'm](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m12s)
01:29:12

[not going to stop doing this and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m17s)
01:29:17

[Harriet's it's really fun and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m18s)
01:29:18

[interesting and and we're really](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m20s)
01:29:20

[interested in your ideas about how to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m22s)
01:29:22

[how to keep this going like by the end](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m25s)
01:29:25

[of plat to you know you guys have put in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m27s)
01:29:27

[hundreds of hours you know maybe you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m31s)
01:29:31

[know on average maybe 140 hours put](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m34s)
01:29:34

[together your own box written blog posts](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m38s)
01:29:38

[done hackathons you know you're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m41s)
01:29:41

[seriously in this now](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m43s)
01:29:43

[and in fact I could have say this week's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m46s)
01:29:46

[kind of been special for me like this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m49s)
01:29:49

[week's been a week where again and again](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m51s)
01:29:51

[I've spoken to various folks of you guys](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m53s)
01:29:53

[and heard about how like how many of you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h29m56s)
01:29:56

[have like implemented projects at your](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m01s)
01:30:01

[workplace that have worked and are now](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m03s)
01:30:03

[running and making your business money](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m05s)
01:30:05

[or that you've you know achieved the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m06s)
01:30:06

[career thing that you've been aiming for](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m10s)
01:30:10

[or that you've you know won yet another](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m12s)
01:30:12

[GPU at a hackathon like you know or of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m14s)
01:30:14

[course the social impact seeing where](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m17s)
01:30:17

[it's like all these transformative and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m19s)
01:30:19

[inspirational things that you know it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m22s)
01:30:22

[it's gone from yeah we Rachel and I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m24s)
01:30:24

[started this we had no idea if it was](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m27s)
01:30:27

[possible to teach people you know with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m30s)
01:30:30

[no specific required math background](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m33s)
01:30:33

[other than high school math you know](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m38s)
01:30:38

[deep learning to the point that you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m39s)
01:30:39

[could use it to build cool things we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m41s)
01:30:41

[thought we probably could because I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m44s)
01:30:44

[don't have that background and I've been](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m45s)
01:30:45

[able to but you know I've been kind of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m47s)
01:30:47

[playing around with similar things for a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m51s)
01:30:51

[couple of decades so it was a bit of an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m53s)
01:30:53

[experiment and yeah this this week's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m55s)
01:30:55

[been a week that for me it's been fear](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h30m58s)
01:30:58

[that the experiments worked so I don't](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m01s)
01:31:01

[know what party is going to look like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m03s)
01:31:03

[it's I think it'll be a bit different](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m04s)
01:31:04

[because it's like it'll be more of a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m07s)
01:31:07

[meeting of minds along stack group of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m09s)
01:31:09

[people who were kind of at the same](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m12s)
01:31:12

[level and thinking about the same kind](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m14s)
01:31:14

[of thing and so maybe it's more of a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m15s)
01:31:15

[yeah more of a ongoing keep out](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m18s)
01:31:18

[knowledge up-to-date kind of thing it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m24s)
01:31:24

[might be more of us teaching each other](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m25s)
01:31:25

[I'm not sure certainly interested to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m27s)
01:31:27

[hear ideas okay we don't normally have](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m30s)
01:31:30

[three breaks but I think I need one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m37s)
01:31:37

[today and they were covering a lot of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m38s)
01:31:38

[territory so why don't we have a short](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m40s)
01:31:40

[break and well I have a 34 yeah let's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m42s)
01:31:42

[have a short break and we put all the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m49s)
01:31:49

[last 20 minutes let's come back at em](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m50s)
01:31:50

[8:40](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m51s)
01:31:51

[okay thank you so attention models](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h31m57s)
01:31:57

[attention models](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m06s)
01:32:06

[so I actually I really like these](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m12s)
01:32:12

[I think theory and fairly the paper that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m17s)
01:32:17

[introduced these it was quite](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m24s)
01:32:24

[extraordinary paper introduced both GI](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m25s)
01:32:25

[use and attention models at the same](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m28s)
01:32:28

[time I think it might even be before the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m30s)
01:32:30

[guy had his PhD is remember correctly it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m33s)
01:32:33

[was just a wonderful paper very](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m36s)
01:32:36

[successful](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m40s)
01:32:40

[and the basic idea of an attention model](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m43s)
01:32:43

[is it's actually pretty simple you'll](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m46s)
01:32:46

[see here](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m52s)
01:32:52

[see where does this happen](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m55s)
01:32:55

[okay here is is a decoder right okay and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h32m59s)
01:32:59

[here's our embedding](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m07s)
01:33:07

[okay and notice here](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m11s)
01:33:11

[remember that my ghetto and and return](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m16s)
01:33:16

[sequences equals true with the default](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m18s)
01:33:18

[so the decoder now is actually spitting](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m21s)
01:33:21

[out a sequence of states](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m24s)
01:33:24

[now the length of that sequence is equal](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m29s)
01:33:29

[to the number of phonemes okay and we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m32s)
01:33:32

[know that there isn't a mapping one to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m38s)
01:33:38

[one of phonemes de letters all right so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m39s)
01:33:39

[this is kind of interesting to even](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m43s)
01:33:43

[think about how we're going to deal with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m45s)
01:33:45

[this now how we're going to deal with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m46s)
01:33:46

[sixteen states and the states because](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m49s)
01:33:49

[they started with bi-directional state 1](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m54s)
01:33:54

[both represent the combination of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h33m58s)
01:33:58

[everything that's come before the first](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m00s)
01:34:00

[phoneme and everything has come after](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m02s)
01:34:02

[and state 2 is everything that come](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m04s)
01:34:04

[before the second phoneme and everything](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m05s)
01:34:05

[has come after and so forth](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m07s)
01:34:07

[okay so the states in a sense they're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m08s)
01:34:08

[all representing something very similar](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m12s)
01:34:12

[but they've got a different focus you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m14s)
01:34:14

[know each one of these states at each](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m16s)
01:34:16

[one remembers at length of 16 right so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m18s)
01:34:18

[it's one of these 16 states represents](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m20s)
01:34:20

[everything that comes before everything](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m23s)
01:34:23

[that comes after that point but with a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m26s)
01:34:26

[focus on on that phony okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m28s)
01:34:28

[so what we want to do now is create a an](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m32s)
01:34:32

[RNN](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m38s)
01:34:38

[where the number of inputs to the iron n](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m41s)
01:34:41

[needs to be 15 not 16 because remember](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m46s)
01:34:46

[the length of the word we're creating is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m50s)
01:34:50

[15 right so we're going to have at 15](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m52s)
01:34:52

[output time steps](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h34m55s)
01:34:55

[and at each point we wanted to have the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m02s)
01:35:02

[opportunity to look at all of these 16](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m06s)
01:35:06

[output states but we're going to go in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m10s)
01:35:10

[with the assumption that only some of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m14s)
01:35:14

[those 16 are going to be relevant but we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m16s)
01:35:16

[don't know which right so what we want](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m21s)
01:35:21

[to do is basically create a so take a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m25s)
01:35:25

[basically take each of these 16 States](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m29s)
01:35:29

[and to a weighted sum write sum of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m32s)
01:35:32

[weights times encoded fixed](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m35s)
01:35:35

[right where these weights somehow](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m44s)
01:35:44

[represent how important is each one of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m48s)
01:35:48

[those 16 inputs for calculating this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m52s)
01:35:52

[output and how important or each of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m55s)
01:35:55

[those 16 inputs for calculating this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h35m58s)
01:35:58

[output and so forth right if we could](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m00s)
01:36:00

[somehow come up with a set of weights to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m03s)
01:36:03

[every single one of those time steps](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m07s)
01:36:07

[then we can replace the length 16 thing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m08s)
01:36:08

[with a single thing right and if it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m12s)
01:36:12

[turns out that output number 1 only](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m17s)
01:36:17

[really depends on input number 1 and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m21s)
01:36:21

[nothing else then basically that input](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m24s)
01:36:24

[those weights are going to be 1 0 0 0 0](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m26s)
01:36:26

[0 right like it can it can learn to do](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m29s)
01:36:29

[that but if it turns out that if it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m33s)
01:36:33

[turns out that output number 1 actually](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m38s)
01:36:38

[depends on phonemes 1 &amp; 2 equally that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m41s)
01:36:41

[it can learn the weights 0.5 0.5 0 0 0 0](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m45s)
01:36:45

[0 so in other words we want some](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m49s)
01:36:49

[function WI equals some function that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h36m54s)
01:36:54

[returns the right set of weights to tell](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m01s)
01:37:01

[us which bit of the decoded input to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m04s)
01:37:04

[look at so it so happens we actually](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m08s)
01:37:08

[know a good way of learning functions](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m13s)
01:37:13

[what if we made the function a neural](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m16s)
01:37:16

[net and what if we learn to it using SGD](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m19s)
01:37:19

[why not so here's the paper neural](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m26s)
01:37:26

[machine translation by jointly alert](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m36s)
01:37:36

[learning to align and translate and the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m38s)
01:37:38

[great paper it's not the clearest in my](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m43s)
01:37:43

[opinion in terms of understandability](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m48s)
01:37:48

[but let me describe some of the main](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m50s)
01:37:50

[pieces](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m52s)
01:37:52

[okay so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h37m55s)
01:37:55

[here's the starting point oopsy-daisy](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m01s)
01:38:01

[yes I have to do it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m04s)
01:38:04

[[Music]](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m06s)
01:38:06

[okay let's subscribe how to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m09s)
01:38:09

[read this equation when you see a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m11s)
01:38:11

[probability like this you can very often](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m16s)
01:38:16

[think of it as a loss function right the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m19s)
01:38:19

[idea of of SGG basically most time when](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m22s)
01:38:22

[we're using it is to come up with a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m27s)
01:38:27

[model where the probabilities that the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m29s)
01:38:29

[model creates are as high as possible](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m32s)
01:38:32

[for the true data and as well as](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m35s)
01:38:35

[possible for the other data that's like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m37s)
01:38:37

[it's just another way of talking about a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m39s)
01:38:39

[loss function right so very often when](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m41s)
01:38:41

[you read the papers where we would write](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m45s)
01:38:45

[a loss function a people will see a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m46s)
01:38:46

[probability and what this here says](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m48s)
01:38:48

[earlier on they say that y is basically](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m51s)
01:38:51

[our our outputs very common for Y to be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m53s)
01:38:53

[an output and what is it saying is that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m57s)
01:38:57

[the probability of the output at time](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h38m59s)
01:38:59

[step I write so at some particular time](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m01s)
01:39:01

[step depends on to this bar here means](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m04s)
01:39:04

[depends on all of the previous outputs](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m08s)
01:39:08

[right in other words in our spelling](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m11s)
01:39:11

[thing when we're looking at the fourth](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m15s)
01:39:15

[letter that we're spelling it depends on](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m19s)
01:39:19

[the three letters that we spelt so far](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m22s)
01:39:22

[you can't have it depend on the later](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m24s)
01:39:24

[letters that treating right so this is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m27s)
01:39:27

[basically a description of the problem](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m30s)
01:39:30

[is that we're building something which](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m32s)
01:39:32

[is time dependent and where the ice](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m34s)
01:39:34

[thing that we're creating can only be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m37s)
01:39:37

[allowed to depend on the previous I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m40s)
01:39:40

[minus 1 things comma that basically](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m42s)
01:39:42

[means and and it's also allowed to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m47s)
01:39:47

[depend on ok anything in bold is a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m49s)
01:39:49

[vector right a vector of inputs and so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m52s)
01:39:52

[this here is our list of phonemes right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h39m57s)
01:39:57

[and this here is our list of all of the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m00s)
01:40:00

[letters we've spelt so far ok so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m04s)
01:40:04

[so that whole thing right that whole](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m12s)
01:40:12

[probability we're going to calculate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m14s)
01:40:14

[using some some function right and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m17s)
01:40:17

[because this is a neural net paper you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m21s)
01:40:21

[can be pretty sure that's going to turn](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m23s)
01:40:23

[out to be a neural net and what are the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m24s)
01:40:24

[things that were allowed to calculate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m27s)
01:40:27

[with well we're allowed to calculate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m29s)
01:40:29

[with the previous letter that we just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m32s)
01:40:32

[translated](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m35s)
01:40:35

[what's this the R and N hidden state](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m38s)
01:40:38

[that we've built up so far and what's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m42s)
01:40:42

[this a context vector](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m47s)
01:40:47

[the context vector the context vector is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m52s)
01:40:52

[a weighted sum of annotations H so these](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h40m57s)
01:40:57

[are the hidden States to come out of our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m04s)
01:41:04

[encoder and these are some weights okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m07s)
01:41:07

[so I'm trying to give you enough](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m12s)
01:41:12

[information to try and pass this paper](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m13s)
01:41:13

[over the weekend right so that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m15s)
01:41:15

[everything I've described so far the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m18s)
01:41:18

[weights and now the nice thing is that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m22s)
01:41:22

[hopefully you guys have now read enough](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m26s)
01:41:26

[papers that you can look at something](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m28s)
01:41:28

[like this and skip over it and go oh](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m30s)
01:41:30

[that's just softmax over time your](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m33s)
01:41:33

[pattern recognition starts getting good](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m38s)
01:41:38

[right like you start seeing something](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m40s)
01:41:40

[like this you go oh that's a weighted](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m42s)
01:41:42

[sum and you say something like this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m44s)
01:41:44

[together](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m46s)
01:41:46

[oh that's soft mess like people who read](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m46s)
01:41:46

[papers don't actually read every symbol](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m48s)
01:41:48

[that I looks at it and goes softmax](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m52s)
01:41:52

[weighted sum adjusted function okay got](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m54s)
01:41:54

[it right as if it was like pieces of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h41m57s)
01:41:57

[code only this is like really annoying](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m01s)
01:42:01

[clothes you can't look up in a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m03s)
01:42:03

[dictionary and you can't run and you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m04s)
01:42:04

[can't check it you can't debug it but](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m06s)
01:42:06

[apart from that it's just like oh okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m07s)
01:42:07

[so alright so the alphas are things that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m09s)
01:42:09

[came out of a softmax all right what](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m13s)
01:42:13

[goes into the softmax all right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m15s)
01:42:15

[something called e the other annoying](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m18s)
01:42:18

[thing about math notation is often you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m21s)
01:42:21

[introduce something and define it later](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m22s)
01:42:22

[all right so here we are](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m25s)
01:42:25

[later we define e what a equal to e is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m26s)
01:42:26

[equal to some function of what some](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m31s)
01:42:31

[function of the previous hidden state](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m35s)
01:42:35

[and the encoder state okay and what's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m39s)
01:42:39

[that function or that function is again](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m48s)
01:42:48

[a neural network now the important piece](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m55s)
01:42:55

[here is jointly trained jointly trained](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h42m58s)
01:42:58

[means it's not like a again where we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m02s)
01:43:02

[train a bit of disseminator and a bit of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m05s)
01:43:05

[generator it's not like one of these](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m07s)
01:43:07

[kind of manual attentional models where](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m10s)
01:43:10

[we first of all figure out the modules](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m12s)
01:43:12

[are here and then we zoom into them and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m14s)
01:43:14

[find them there jointly trained means we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m16s)
01:43:16

[create a single model in a single](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m19s)
01:43:19

[computation graph if you like where the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m21s)
01:43:21

[gradients are going to flow through](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m22s)
01:43:22

[everything so we have to try and come up](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m24s)
01:43:24

[with a way basically where we're going](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m27s)
01:43:27

[to build a standard regular RNN okay but](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m29s)
01:43:29

[the iron N is going to use as the input](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m34s)
01:43:34

[at each time step this right so we're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m37s)
01:43:37

[going to have to come up with a way of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m44s)
01:43:44

[actually cup of actually making this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m46s)
01:43:46

[mini neuron it's just a single one](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m50s)
01:43:50

[hidden layer standard neuron it it's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m52s)
01:43:52

[going to be inside every time set in our](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h43m56s)
01:43:56

[RN](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m00s)
01:44:00

[so this whole thing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m03s)
01:44:03

[is summarized in another paper this is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m13s)
01:44:13

[actually really cool paper grammar as a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m16s)
01:44:16

[foreign language lots of things you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m19s)
01:44:19

[probably recognize here Geoffrey Hinton](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m23s)
01:44:23

[who's kind of father of deep learning](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m24s)
01:44:24

[earlier who's now I think chief](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m27s)
01:44:27

[scientist or something at some director](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m30s)
01:44:30

[of science at open AI Oreo venules done](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m33s)
01:44:33

[lots of cool stuff this paper is kind of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m38s)
01:44:38

[neat and fun anyway it basically says](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m41s)
01:44:41

[what if you didn't know anything about](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m44s)
01:44:44

[grammar and you attempted to be able to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m47s)
01:44:47

[neural net which assigned grammar to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m49s)
01:44:49

[sentences it turns out you actually end](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m53s)
01:44:53

[up with something more accurate than any](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m57s)
01:44:57

[rule based grammar system that's been](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h44m59s)
01:44:59

[built one of the most things they do is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m01s)
01:45:01

[to summarize all the bits and again this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m06s)
01:45:06

[is where like if you were reading a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m09s)
01:45:09

[paper the first time and didn't know](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m11s)
01:45:11

[what an LS TM was and when oh and lsdm](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m13s)
01:45:13

[is all these things that's not going to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m15s)
01:45:15

[mean anything to you right you have to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m18s)
01:45:18

[recognize that people write stuff in](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m20s)
01:45:20

[papers I mean there's no point writing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m23s)
01:45:23

[Atlas TM equations in papers right but](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m26s)
01:45:26

[it's basically you're going to have to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m28s)
01:45:28

[go and find the lsdm paper or find a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m30s)
01:45:30

[tutorial like learn about lsdm when](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m32s)
01:45:32

[you're finished come back in the same](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m34s)
01:45:34

[way they summarized attention okay so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m36s)
01:45:36

[they say we've used add or adapt to the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m41s)
01:45:41

[attention model from - if you go and you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m42s)
01:45:42

[have a look at - okay that's the paper](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m45s)
01:45:45

[we just looked at all right but the nice](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m47s)
01:45:47

[thing is that because this came a little](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m51s)
01:45:51

[later they've done a pretty good job of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m53s)
01:45:53

[trying to summarize it into a single](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m55s)
01:45:55

[page so during the week if you want to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h45m58s)
01:45:58

[try and get the hang of attention you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m01s)
01:46:01

[might find it good to have a look at](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m02s)
01:46:02

[this paper and look at their summary and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m04s)
01:46:04

[you'll see that basically the idea is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m07s)
01:46:07

[that it's a standard sequence of](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m09s)
01:46:09

[sequence model so a standard sequence](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m14s)
01:46:14

[two tickets model means encoder hidden](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m16s)
01:46:16

[states the final hidden state decoder](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m18s)
01:46:18

[right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m21s)
01:46:21

[plus adding attention okay and so we](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m22s)
01:46:22

[have two separate LS GMS an encoder and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m27s)
01:46:27

[a decoder and now be careful of the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m31s)
01:46:31

[notation encoded states are going to be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m35s)
01:46:35

[called H the decoder states h1 through](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m37s)
01:46:37

[HTA](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m44s)
01:46:44

[the decoder states are D which are also](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m44s)
01:46:44

[going to call H ta plus 1/2 T a plus T B](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m49s)
01:46:49

[so the inputs are 1 through T a and here](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m53s)
01:46:53

[you can see is defining a single layer](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h46m58s)
01:46:58

[neural net okay so we've got our decoder](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m02s)
01:47:02

[States we've got our current encoder](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m09s)
01:47:09

[state put it through a non-linearity put](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m15s)
01:47:15

[it through another affine transformation](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m21s)
01:47:21

[stick it through a soft Max and use that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m23s)
01:47:23

[to create a weighted sum ok so there's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m27s)
01:47:27

[like all of it in one little snapshot ok](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m29s)
01:47:29

[so again like don't expect this to make](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m33s)
01:47:33

[perfect sense the first time you see it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m38s)
01:47:38

[necessarily but hopefully you can kind](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m39s)
01:47:39

[of see that you know these bits there's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m41s)
01:47:41

[all stuff you've seen lots of times](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m44s)
01:47:44

[before so next week we're going to come](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m46s)
01:47:46

[back and work through you know creating](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m48s)
01:47:48

[this code and seeing that seeing how it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m53s)
01:47:53

[works](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m55s)
01:47:55

[did you have some ritual we have two](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m55s)
01:47:55

[questions one is what the way speed the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h47m57s)
01:47:57

[waiting's be heavily impacted by the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m01s)
01:48:01

[padding down to the input set sure](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m03s)
01:48:03

[absolutely and specifically those](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m06s)
01:48:06

[weights will say oh the padding is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m08s)
01:48:08

[always weighted zero it's not going to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m10s)
01:48:10

[take it very long to learn to create](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m13s)
01:48:13

[that pattern and is a shared among all](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m15s)
01:48:15

[IJ pairs or do we train a separate](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m19s)
01:48:19

[alignment for each pair so a is not](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m21s)
01:48:21

[trained a is the output of a suppose a](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m24s)
01:48:24

[is the output of a soft max what trained](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m27s)
01:48:27

[is w1 and w2 and note there capital](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m31s)
01:48:31

[letters are matrices](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m35s)
01:48:35

[right so we just have to learn a single](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m36s)
01:48:36

[w1 and a single w2 but note that they're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m38s)
01:48:38

[being applied to all of the input so](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m43s)
01:48:43

[it's all of the encoded states and the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m50s)
01:48:50

[current state of the decoder all right](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m55s)
01:48:55

[and you know in fact easier is to just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h48m58s)
01:48:58

[abstract out this all the way back to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m02s)
01:49:02

[say it is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m04s)
01:49:04

[function right like this is the best way](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m10s)
01:49:10

[to think that it's some function of what](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m12s)
01:49:12

[some function of the current hidden](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m14s)
01:49:14

[state and all of the decoder states okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m18s)
01:49:18

[so that's that's the inputs to the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m26s)
01:49:26

[function and we just have to learn a set](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m28s)
01:49:28

[of weights that will spit out the inputs](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m31s)
01:49:31

[to ourself Mac you can see you have](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m34s)
01:49:34

[another question okay great so I don't](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m38s)
01:49:38

[feel like I want to study news so let's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m45s)
01:49:45

[take one final AMA before we go home](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m46s)
01:49:46

[[Music]](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m53s)
01:49:53

[advice on imbalance to dataset oh okay](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h49m55s)
01:49:55

[unbalanced datasets yeah](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m00s)
01:50:00

[there's not really that much clever you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m06s)
01:50:06

[can do about it you know basically if](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m08s)
01:50:08

[you've got well a great example would be](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m11s)
01:50:11

[young one of the impact talks talked](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m15s)
01:50:15

[about breast cancer detection from](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m18s)
01:50:18

[mammography scans and you thing called](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m21s)
01:50:21

[the drain challenge had a little Mia](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m24s)
01:50:24

[what was it like less than once](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m27s)
01:50:27

[Teresa them 0.3% of the scans actually](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m30s)
01:50:30

[had cancer so that's very unbalanced I](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m36s)
01:50:36

[think the first thing you try to do is](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m40s)
01:50:40

[such an unbalanced data set is ignore it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m42s)
01:50:42

[and try it try it and see how it goes](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m44s)
01:50:44

[the reason that often it doesn't go well](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m46s)
01:50:46

[is that the initial gradients will tend](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m49s)
01:50:49

[to point to say they never have cancer](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m53s)
01:50:53

[you know because that's going to give](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m56s)
01:50:56

[you a very accurate model so one thing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h50m58s)
01:50:58

[you could try and do is to come up with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m01s)
01:51:01

[some kind of initial model which is like](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m03s)
01:51:03

[you know maybe some kind of heuristic](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m07s)
01:51:07

[which is not terrible](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m08s)
01:51:08

[and gets it to the point where the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m10s)
01:51:10

[gradients are you know don't always](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m11s)
01:51:11

[point to saying they never have cancer](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m14s)
01:51:14

[but the really obvious thing to do is to](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m17s)
01:51:17

[adjust your thing which is creating the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m21s)
01:51:21

[mini-batches so that on every mini batch](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m23s)
01:51:23

[you grab like half of it as being people](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m26s)
01:51:26

[with cancer and half of people being](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m30s)
01:51:30

[without cancer so that way you know you](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m31s)
01:51:31

[still go through lots and lots of epochs](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m38s)
01:51:38

[it's a bit of a challenges that you're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m39s)
01:51:39

[going to the people that do have cancer](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m42s)
01:51:42

[you're going to see lots and lots and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m43s)
01:51:43

[lots of time so you have to be very](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m45s)
01:51:45

[careful of overfitting and then](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m47s)
01:51:47

[basically it is kind of thing](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m52s)
01:51:52

[between those two extremes so I think](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m55s)
01:51:55

[what you really need to do is figure out](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m58s)
01:51:58

[what's the smallest number of people](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h51m59s)
01:51:59

[with cancer that you can get away with](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m03s)
01:52:03

[you know what's the smallest number](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m04s)
01:52:04

[where the gradients don't point to zero](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m06s)
01:52:06

[and then create a model where let's say](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m08s)
01:52:08

[it's 10% so create a model where every](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m11s)
01:52:11

[batch mini-batch you create 10% of it](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m13s)
01:52:13

[with people with cancer and 90% people](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m17s)
01:52:17

[without train that for a while the good](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m18s)
01:52:18

[news is once it's working pretty well](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m22s)
01:52:22

[you can then decrease the size that has](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m25s)
01:52:25

[the has cancer size because you're](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m30s)
01:52:30

[already at a point where your models not](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m32s)
01:52:32

[kind of pointing off to zero so you can](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m34s)
01:52:34

[kind of gradually start to change the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m37s)
01:52:37

[sample to have less and less data get](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m39s)
01:52:39

[the basic technique and so in this](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m42s)
01:52:42

[example we're here you're repeating the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m48s)
01:52:48

[positive results over and over in your](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m52s)
01:52:52

[sphere essentially is waiting more yeah](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m56s)
01:52:56

[could you get the same results by just](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h52m58s)
01:52:58

[throwing away one to the false base and](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h53m01s)
01:53:01

[yeah you could do that and like that's](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h53m04s)
01:53:04

[the really quick way to do it but that](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h53m07s)
01:53:07

[way you're not using like the](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h53m10s)
01:53:10

[information about the false stuff still](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h53m13s)
01:53:13

[has information so yeah okay thanks](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h53m15s)
01:53:15

[everybody have a good week](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h53m18s)
01:53:18

[[Applause]](https://www.youtube.com/watch?v=jy1w0mPCHb0#t=01h53m23s)
01:53:23

