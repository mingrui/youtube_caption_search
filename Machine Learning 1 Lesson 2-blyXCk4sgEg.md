[so from here the next two or three](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m00s)
00:00:00

[lessons we're going to be really diving](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m03s)
00:00:03

[deep into random forests so so far all](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m06s)
00:00:06

[we've learned is there's a thing called](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m08s)
00:00:08

[random forests for some particular](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m11s)
00:00:11

[datasets they seem to work really really](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m13s)
00:00:13

[well without too much trouble](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m16s)
00:00:16

[but we don't really know yet like well](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m18s)
00:00:18

[how do they actually work what do we do](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m21s)
00:00:21

[if they don't work properly what are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m24s)
00:00:24

[their pros and cons what are the can we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m25s)
00:00:25

[tune and so forth so we're gonna look at](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m28s)
00:00:28

[all that and then after that we're going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m29s)
00:00:29

[to look at how do we interpret the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m31s)
00:00:31

[results of random forests to get not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m33s)
00:00:33

[just predictions but to actually deeply](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m35s)
00:00:35

[understand our data in a model driven](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m38s)
00:00:38

[way so that's where we're going to go](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m40s)
00:00:40

[from here](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m42s)
00:00:42

[so let's just review where we're up to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m44s)
00:00:44

[so we learned that there's this library](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m47s)
00:00:47

[called fast AI and the fast AI library](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m51s)
00:00:51

[is basically it's a highly opinionated](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m54s)
00:00:54

[library which is to say we've spent a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h00m58s)
00:00:58

[lot of time researching what are the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m01s)
00:01:01

[best techniques to get like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m03s)
00:01:03

[state-of-the-art results and then we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m05s)
00:01:05

[take those techniques and package them](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m07s)
00:01:07

[into pieces of code so that you can use](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m09s)
00:01:09

[the state-of-the-art results yourself](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m12s)
00:01:12

[and so where possible we wrap or provide](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m14s)
00:01:14

[things on top of existing code and so in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m21s)
00:01:21

[particular for the kind of structured](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m25s)
00:01:25

[data analysis we're doing scikit-learn](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m26s)
00:01:26

[has a lot of really great code so most](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m29s)
00:01:29

[of the stuff that we're showing you from](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m32s)
00:01:32

[fast AI is stuff to help us get stuff](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m33s)
00:01:33

[into scikit-learn and then interpret](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m36s)
00:01:36

[stuff out from scikit-learn the fast AI](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m40s)
00:01:40

[library](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m44s)
00:01:44

[the way it works in our environment here](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m48s)
00:01:48

[is that we've got out our notebooks are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m52s)
00:01:52

[inside fast AI repo / courses and in /](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h01m59s)
00:01:59

[ml 1 + dl 1 and then inside there](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m02s)
00:02:02

[there's a symlink to the parent of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m07s)
00:02:07

[parent fast AI so this is a sim link to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m12s)
00:02:12

[a directory containing a bunch of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m15s)
00:02:15

[modules so if you want to use the fast](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m20s)
00:02:20

[AI library in your own code there's a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m24s)
00:02:24

[number of things you can do one is to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m28s)
00:02:28

[put your notebooks or scripts in the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m30s)
00:02:30

[same directory as ml 1 or 0 1 whether](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m33s)
00:02:33

[it's already this simile and just import](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m35s)
00:02:35

[it just like I do](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m37s)
00:02:37

[you could copy this directory dot dot](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m38s)
00:02:38

[slash dot dot slash birthday I into](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m43s)
00:02:43

[somewhere else and use it or you could](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m46s)
00:02:46

[sim link it just like I have from here](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m49s)
00:02:49

[to wherever you want to use it so notice](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m52s)
00:02:52

[it's mildly confusing there's a github](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m55s)
00:02:55

[repo called fast AI and inside the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h02m57s)
00:02:57

[github repo caught fast AI which looks](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m00s)
00:03:00

[like this there is a folder called fast](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m04s)
00:03:04

[AI okay and so the FASTA a folder in the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m06s)
00:03:06

[FASTA a repo contains the FASTA a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m10s)
00:03:10

[library and it's that library when we go](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m13s)
00:03:13

[from fast AI dot imports to import star](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m17s)
00:03:17

[then that's looking inside the farsi a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m20s)
00:03:20

[folder for a file called inputs imports](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m22s)
00:03:22

[py and importing everything from that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m26s)
00:03:26

[okay yes Danielle](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m31s)
00:03:31

[okay and just like as a clarifying](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m37s)
00:03:37

[question for this Bentley](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m42s)
00:03:42

[it's just that anything](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m43s)
00:03:43

[that's just the Ellen thing that you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m48s)
00:03:48

[talked about yeah so a symlink is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m51s)
00:03:51

[something you can create by typing Ln](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m53s)
00:03:53

[minus s and then the path to the source](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h03m56s)
00:03:56

[which in this case would be dot dot dot](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m00s)
00:04:00

[first AI could be relative or it could](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m01s)
00:04:01

[be absolute and then the name of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m04s)
00:04:04

[destination if you just put the current](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m06s)
00:04:06

[directory at the destination](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m08s)
00:04:08

[it'll use the same name as it comes from](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m09s)
00:04:09

[like a alias on the Mac or a shortcut on](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m12s)
00:04:12

[Windows](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m17s)
00:04:17

[and when you do the important system yep](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m29s)
00:04:29

[got it imports this and then append that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m35s)
00:04:35

[relative link that also creates the same](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m39s)
00:04:39

[link and I don't think I've created the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m41s)
00:04:41

[same link anywhere in the workbooks the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m47s)
00:04:47

[symlink actually lives inside the github](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m49s)
00:04:49

[repo okay I created some symlinks in the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m51s)
00:04:51

[deep learning notebook to some data that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m57s)
00:04:57

[was different at the top of Tim Lee's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h04m59s)
00:04:59

[workbook from the last class there was](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m04s)
00:05:04

[important](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m06s)
00:05:06

[oh yeah don't do that probably I mean](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m10s)
00:05:10

[you you can but I think this is I think](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m12s)
00:05:12

[this is better like this way you can go](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m16s)
00:05:16

[from fast AI imports and regardless of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m18s)
00:05:18

[kind of how you got it there it's it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m22s)
00:05:22

[going to work you know okay okay so then](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m24s)
00:05:24

[we had all of our data for blue books](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m29s)
00:05:29

[for bulldozers competition in data slash](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m31s)
00:05:31

[bulldozers and here it is right so we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m34s)
00:05:34

[were able to read that CSV file the only](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m40s)
00:05:40

[thing we really had to do was to say](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m44s)
00:05:44

[which columns were dates and having done](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m45s)
00:05:45

[that we were able to take a look at a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m49s)
00:05:49

[few earth examples of the rows of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m51s)
00:05:51

[data and so we also noted that it's very](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h05m53s)
00:05:53

[important to deeply understand the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m02s)
00:06:02

[evaluation metric for this project and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m07s)
00:06:07

[so if a cattle they tell you what the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m10s)
00:06:10

[evaluation metric is and in this case it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m13s)
00:06:13

[was the root mean squared log error so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m16s)
00:06:16

[that is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m21s)
00:06:21

[some of the actuals - the predictions](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m25s)
00:06:25

[now but it's the log of the actuals -](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m38s)
00:06:38

[the log the predictions squared right so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m42s)
00:06:42

[if we replace actuals with log actuals](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m50s)
00:06:50

[and replace predictions with log](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m55s)
00:06:55

[predictions then it's just the same as](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m57s)
00:06:57

[root mean squared error so that's what](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h06m59s)
00:06:59

[we did was we replaced sale price with](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m03s)
00:07:03

[log of sale price and so now if if we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m06s)
00:07:06

[optimize for root mean squared error](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m10s)
00:07:10

[we're actually optimizing for the root](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m12s)
00:07:12

[mean squared error of the logs](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m15s)
00:07:15

[okay so then we learnt that we need all](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m17s)
00:07:17

[of our columns to be numbers and so the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m21s)
00:07:21

[first way we did that was to take the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m26s)
00:07:26

[date column and remove it and instead](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m29s)
00:07:29

[replace it with a whole bunch of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m32s)
00:07:32

[different columns such as is that date](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m34s)
00:07:34

[the start of a quarter is at the end of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m43s)
00:07:43

[a year how many days are elapsed since](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m46s)
00:07:46

[generally the first 1970 what's a year](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m49s)
00:07:49

[what's the month or the day of weeks and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m52s)
00:07:52

[so forth okay so they're all numbers](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m53s)
00:07:53

[then we learnt that we can use train](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h07m58s)
00:07:58

[underscore katz to replace all of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m01s)
00:08:01

[strings with categories now when you do](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m03s)
00:08:03

[that it doesn't look like you've done](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m08s)
00:08:08

[anything different they still look like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m11s)
00:08:11

[strings all right but if you actually](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m12s)
00:08:12

[take a deeper look you'll see that the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m16s)
00:08:16

[datatype now is not string but category](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m22s)
00:08:22

[and category is a panda's class where](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m25s)
00:08:25

[you can then go dark cat dot and find a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m32s)
00:08:32

[whole bunch of different attributes such](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m35s)
00:08:35

[as cat categories to find a list of all](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m37s)
00:08:37

[of the possible categories and this says](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m41s)
00:08:41

[hi is going to be 0 low will become 1](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m43s)
00:08:43

[medium will become 2 so we can then get](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m45s)
00:08:45

[codes](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m48s)
00:08:48

[to actually get the numbers so then what](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m49s)
00:08:49

[we need to do to actually use this data](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m53s)
00:08:53

[set to turn it into numbers is take](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m55s)
00:08:55

[every categorical column and replace it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h08m58s)
00:08:58

[with cap codes and so we did that using](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m00s)
00:09:00

[proc DF okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m07s)
00:09:07

[so how do I get the source code for proc](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m11s)
00:09:11

[DF question question mark okay all right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m15s)
00:09:15

[so if I scroll down I go through each](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m28s)
00:09:28

[column and I numerical eyes it okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m30s)
00:09:30

[that's actually the one I want so I'm](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m33s)
00:09:33

[going to now have to look up numerical](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m35s)
00:09:35

[eyes so tab to complete it if it's not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m37s)
00:09:37

[numeric then replace the data frames](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m45s)
00:09:45

[filled with that columns cat codes last](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m48s)
00:09:48

[one because otherwise unknown is minus](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m53s)
00:09:53

[one we went unknown to be zero okay so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m55s)
00:09:55

[that's how we turn the strings into](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h09m58s)
00:09:58

[numbers right they get replaced with a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m03s)
00:10:03

[unique basically arbitrary index it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m06s)
00:10:06

[actually based on the alphabetical order](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m09s)
00:10:09

[of the feature names](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m11s)
00:10:11

[the other thing property f did remember](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m13s)
00:10:13

[was continuous columns that had missing](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m16s)
00:10:16

[values the missing got replaced with the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m20s)
00:10:20

[median and we added an additional column](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m22s)
00:10:22

[called column name underscore na which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m24s)
00:10:24

[is a boolean column told you if that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m27s)
00:10:27

[particular item was missing or not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m30s)
00:10:30

[so once we did that we were able to call](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m34s)
00:10:34

[random forest regressor dot fit and get](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m39s)
00:10:39

[the dots poor and turns out we have an](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m43s)
00:10:43

[r-squared of 0.98 can anybody tell me](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m46s)
00:10:46

[what an r-squared is listen um can we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h10m51s)
00:10:51

[you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m07s)
00:11:07

[so r-squared essentially shows how much](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m12s)
00:11:12

[variance is explained by the modal this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m16s)
00:11:16

[is the yeah this is the relation of this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m20s)
00:11:20

[is ssro which is like trying to trying](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m27s)
00:11:27

[to remember the exact formal but I don't](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m33s)
00:11:33

[roughly a curative way](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m36s)
00:11:36

[yeah intuitively it's how much the model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m37s)
00:11:37

[explains the how much it accounts for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m40s)
00:11:40

[the variance in the data okay good so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m43s)
00:11:43

[let's talk about the formula and so with](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m46s)
00:11:46

[formulas the idea is not to learn the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m50s)
00:11:50

[formula and remember it but to learn](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m52s)
00:11:52

[what the formula does and understand it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m55s)
00:11:55

[right so here's the formula it's 1 minus](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h11m58s)
00:11:58

[something divided by something else so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m04s)
00:12:04

[what's this something else from the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m08s)
00:12:08

[bottom SS taught okay so what this is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m09s)
00:12:09

[saying is we've got some actual data](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m14s)
00:12:14

[so my eyes right we've got some actual](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m20s)
00:12:20

[data 3e two-for-one okay and then we've](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m22s)
00:12:22

[got some average okay so our top bit](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m28s)
00:12:28

[this SS tot is the sum of each of these](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m37s)
00:12:37

[- that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m43s)
00:12:43

[so in other words it's telling us how](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m47s)
00:12:47

[much does this data bury perhaps more](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m50s)
00:12:50

[interestingly is I remember when we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m52s)
00:12:52

[talked about like last week what's the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m55s)
00:12:55

[simplest non stupid model you could come](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h12m58s)
00:12:58

[up with and I think the simplest non](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m01s)
00:13:01

[stupid model we came up with was create](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m03s)
00:13:03

[a column of the mean just copy the mean](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m05s)
00:13:05

[a bunch of times and submit that to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m08s)
00:13:08

[cable if you did that then your root](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m09s)
00:13:09

[mean squared error would be this so this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m13s)
00:13:13

[is the root mean squared error of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m19s)
00:13:19

[most naive non stupid model where the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m22s)
00:13:22

[model is just predict mean on the top we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m26s)
00:13:26

[have SS res which is here which is that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m32s)
00:13:32

[we're now going to add a column of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m37s)
00:13:37

[predictions](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m38s)
00:13:38

[okay and so then what we do is rather](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m48s)
00:13:48

[than taking the why I - why mean we're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m51s)
00:13:51

[going to take why I - Fi right and so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h13m55s)
00:13:55

[now instead of saying what's the root](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m01s)
00:14:01

[mean squared error of our naive model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m04s)
00:14:04

[we're saying what's the root mean](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m06s)
00:14:06

[squared error of the actual model that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m07s)
00:14:07

[we're interested in and then we take the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m09s)
00:14:09

[ratio](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m13s)
00:14:13

[so in other words if we actually were](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m14s)
00:14:14

[exactly as effective as just predicting](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m21s)
00:14:21

[the mean then this would be top and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m24s)
00:14:24

[bottom would be the same that would be 1](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m27s)
00:14:27

[1 minus 1 will be 0 if we were perfect](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m29s)
00:14:29

[so fi minus y I was always zero then](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m34s)
00:14:34

[that's zero divided by something one](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m38s)
00:14:38

[minus that is 1 ok so what is the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m40s)
00:14:40

[possible range of values of R squared](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m46s)
00:14:46

[okay I heard a lot of 0 to 1 does](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m52s)
00:14:52

[anybody want to give me an alternative](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m55s)
00:14:55

[negative 1 to 1](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h14m58s)
00:14:58

[anything less than one there's the right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m05s)
00:15:05

[answer let's find out way through the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m07s)
00:15:07

[boss](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m09s)
00:15:09

[okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m22s)
00:15:22

[so why is it any number less than one](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m24s)
00:15:24

[which you can make a model basically as](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m25s)
00:15:25

[crappy as you want and just I guess like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m27s)
00:15:27

[the arrows as you want you're just](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m29s)
00:15:29

[subtracting from one in the formula](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m31s)
00:15:31

[exactly so interestingly I was talking](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m33s)
00:15:33

[to our computer science professor](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m37s)
00:15:37

[Terrence this morning who was talking to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m40s)
00:15:40

[where a statistics professor told him](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m42s)
00:15:42

[that the possible range of values was](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m44s)
00:15:44

[asked where it was zero to one I said](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m46s)
00:15:46

[that is totally not true if you predict](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m48s)
00:15:48

[infinity for every column sorry for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m51s)
00:15:51

[every row then you're going to have](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m54s)
00:15:54

[infinity for every residue and so you're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m56s)
00:15:56

[going to have one minus infinity okay so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h15m58s)
00:15:58

[the possible range of values is less](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m01s)
00:16:01

[than one that's all we know and this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m03s)
00:16:03

[will happen you will get negative values](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m06s)
00:16:06

[sometimes in your r-squared and when](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m08s)
00:16:08

[that happens it's not a mistake it's not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m10s)
00:16:10

[it's not like a bug it means your moral](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m13s)
00:16:13

[is worse than predicting the main okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m16s)
00:16:16

[which is suggest it's not great so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m19s)
00:16:19

[that's R squared it's not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m23s)
00:16:23

[it's not necessarily what you're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m29s)
00:16:29

[actually trying to optimize right but](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m32s)
00:16:32

[it's it's it's the nice thing about it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m35s)
00:16:35

[is that it's a number that you can use](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m37s)
00:16:37

[kind of for every model and so you can](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m39s)
00:16:39

[kind of start try to get a feel of like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m43s)
00:16:43

[what does point-eight look like what](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m45s)
00:16:45

[does point-9 look like so like something](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m46s)
00:16:46

[I find interesting is to like create](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m48s)
00:16:48

[some different synthetic data sets just](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m51s)
00:16:51

[to two dimensions with kind of different](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m54s)
00:16:54

[amounts of random noise and like see](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m56s)
00:16:56

[what they look like on a scatterplot and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h16m59s)
00:16:59

[see what they are squared are just gonna](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m00s)
00:17:00

[get a feel for like what does it ask for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m02s)
00:17:02

[it you know is it a spur to point line](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m05s)
00:17:05

[close or not about 0.7 closed or not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m06s)
00:17:06

[okay so I think r-squared is a useful](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m11s)
00:17:11

[number to have a familiarity with and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m15s)
00:17:15

[you don't need to remember the formula](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m17s)
00:17:17

[if you remember the meaning which is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m20s)
00:17:20

[what's the ratio between how good your](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m23s)
00:17:23

[model is it means bit error versus how](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m26s)
00:17:26

[good is the naive mean model for it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m28s)
00:17:28

[squared error okay and LK is 0.98 it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m30s)
00:17:30

[saying it's a very good model however it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m34s)
00:17:34

[might be a very good model because it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m38s)
00:17:38

[looks like this all right this would be](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m40s)
00:17:40

[called overfitting so we may well have](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m43s)
00:17:43

[created a model which is very good at](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m46s)
00:17:46

[running through the points that we gave](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m48s)
00:17:48

[it but it's not going to be very good at](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m49s)
00:17:49

[running through points that we didn't](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m51s)
00:17:51

[give it so that's why we always want to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m53s)
00:17:53

[have a validation set creating your](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h17m56s)
00:17:56

[validation set is the most important](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m01s)
00:18:01

[thing that I think you need to do when](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m05s)
00:18:05

[you're doing a machine learning project](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m08s)
00:18:08

[at least in terms of in the actual](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m11s)
00:18:11

[modeling because what you need to do is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m14s)
00:18:14

[come up with a data set where the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m20s)
00:18:20

[scroller of your model on that data set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m23s)
00:18:23

[is going to be representative of how](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m25s)
00:18:25

[well your model is going to do in the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m27s)
00:18:27

[real world like in cattle on the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m30s)
00:18:30

[leaderboard or off Kaggle like when you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m33s)
00:18:33

[actually use it in production](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m35s)
00:18:35

[I very very very often hear people in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m37s)
00:18:37

[industries they I don't trust machine](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m43s)
00:18:43

[loading I tried modeling once it looked](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m46s)
00:18:46

[great we put it in production it didn't](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m48s)
00:18:48

[work now whose fault is that right that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m50s)
00:18:50

[means their validation set was not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m54s)
00:18:54

[representative right so here's a very](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h18m57s)
00:18:57

[simple thing which generally speaking](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m00s)
00:19:00

[cattle is pretty good about doing if](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m02s)
00:19:02

[your data has a time piece in it right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m04s)
00:19:04

[as happens in Blue Book for bulldozers](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m08s)
00:19:08

[in Blue Book for bulldozers we're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m11s)
00:19:11

[talking about the sale price of a piece](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m13s)
00:19:13

[of industrial equipment on a particular](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m16s)
00:19:16

[date so the start up during this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m18s)
00:19:18

[competition wanted to create a model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m21s)
00:19:21

[that wouldn't predict last February's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m23s)
00:19:23

[prices that would predict next month's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m26s)
00:19:26

[prices so what they did was they gave us](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m28s)
00:19:28

[data representing a particular date](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m31s)
00:19:31

[range in the training set and then the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m33s)
00:19:33

[test set represented a future set of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m35s)
00:19:35

[dates that wasn't represented in the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m38s)
00:19:38

[training set right so that's pretty good](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m40s)
00:19:40

[right that means that if we're doing](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m43s)
00:19:43

[well on this model we've built something](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m45s)
00:19:45

[which can actually predict the future or](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m47s)
00:19:47

[at least it could predict the future](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m50s)
00:19:50

[then assuming things haven't changed](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m51s)
00:19:51

[dramatically so that's the test set we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m53s)
00:19:53

[have so we need to create a validation](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m57s)
00:19:57

[set that has the same properties so the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h19m59s)
00:19:59

[test set had 12,000 rows in so let's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m02s)
00:20:02

[create a validation set that has 12,000](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m05s)
00:20:05

[rows right and then let's split the data](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m07s)
00:20:07

[set into the first n minus 12 thousand](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m11s)
00:20:11

[rows for the training set and the last](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m16s)
00:20:16

[12,000 rows for the validation set and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m20s)
00:20:20

[so we've now got something which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m22s)
00:20:22

[hopefully looks like cackles test set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m24s)
00:20:24

[plus enough that when we actually try](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m28s)
00:20:28

[and use this validation set we're going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m31s)
00:20:31

[to get some reasonably accurate scores](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m33s)
00:20:33

[and the reason we want this is because](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m36s)
00:20:36

[on cattle you can only submit so many](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m39s)
00:20:39

[times and if you submit too often you'll](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m41s)
00:20:41

[end up fitting to the leaderboard anyway](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m43s)
00:20:43

[and in real life you actually want to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m45s)
00:20:45

[build a model that's going to work in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m47s)
00:20:47

[why did you have a question can we help](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m49s)
00:20:49

[the green box can you explain the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h20m51s)
00:20:51

[difference between a validation set and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m00s)
00:21:00

[a test set absolutely so what we're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m02s)
00:21:02

[going to learn today is how to set what](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m05s)
00:21:05

[other things alone it's how to set high](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m07s)
00:21:07

[parameters hyper parameters are like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m08s)
00:21:08

[tuning parameters that are going to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m10s)
00:21:10

[change how your model behaves now if you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m12s)
00:21:12

[just have one holdout set so one set of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m15s)
00:21:15

[data that you're not using to train with](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m18s)
00:21:18

[and we use that to decide which set of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m19s)
00:21:19

[hyper parameters to use if we try a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m22s)
00:21:22

[thousand different sets of hyper](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m24s)
00:21:24

[parameters we may end up overfitting to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m25s)
00:21:25

[that holdout set that is to say well](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m29s)
00:21:29

[find something which only accidentally](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m30s)
00:21:30

[worked so what we actually want to do is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m33s)
00:21:33

[we want to have a second holdout set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m35s)
00:21:35

[where we can say okay I'm finished](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m38s)
00:21:38

[okay I've done the best I can and now](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m41s)
00:21:41

[just once right at the end I'm gonna see](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m45s)
00:21:45

[whether it works and so this is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m47s)
00:21:47

[something which almost nobody in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m52s)
00:21:52

[industry does correctly you really](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m54s)
00:21:54

[actually need to remove that holdout set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h21m59s)
00:21:59

[that's called the test set remove it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m01s)
00:22:01

[from the data give it to somebody else](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m03s)
00:22:03

[and tell them do not let me look at this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m05s)
00:22:05

[data until I promise you I'm finished](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m08s)
00:22:08

[like it's so hard otherwise not to look](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m10s)
00:22:10

[at it and for example in the world of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m12s)
00:22:12

[psychology and sociology you might have](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m14s)
00:22:14

[heard about this replication crisis this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m16s)
00:22:16

[is basically because people in these](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m18s)
00:22:18

[fields have accidentally or](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m20s)
00:22:20

[intentionally maybe been peed hacking](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m22s)
00:22:22

[which means they've been basically](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m25s)
00:22:25

[trying lots of different variations](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m27s)
00:22:27

[until they find something that works and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m29s)
00:22:29

[then it turns out and they try to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m31s)
00:22:31

[replicate it in other words it's like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m33s)
00:22:33

[somebody creates a test set somebody](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m34s)
00:22:34

[says okay this study which shows you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m36s)
00:22:36

[know the impact of whether you eat](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m39s)
00:22:39

[marshmallows on your tenacity later in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m40s)
00:22:40

[life I'm going to rerun it and like over](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m42s)
00:22:42

[half the time they're finding the effect](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m46s)
00:22:46

[turns out not to exist so that's why we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m48s)
00:22:48

[want to have a test set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m50s)
00:22:50

[get that next door yeah so for handling](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m52s)
00:22:52

[categorical data you can market those to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m57s)
00:22:57

[numerix two numbers order numbers I've](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h22m59s)
00:22:59

[seen a lot of models where we convert](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m02s)
00:23:02

[categorical data into different columns](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m05s)
00:23:05

[using one for encoding yes](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m08s)
00:23:08

[so which approach to use in which model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m10s)
00:23:10

[yeah we're kind of track for that today](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m12s)
00:23:12

[yeah it's a great question okay so so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m14s)
00:23:14

[I'm splitting my my data into validation](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m19s)
00:23:19

[and training sets and so you can see now](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m24s)
00:23:24

[that my validation set is twelve](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m26s)
00:23:26

[thousand about 66 where else my training](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m29s)
00:23:29

[set is three hundred ninety nine](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m32s)
00:23:32

[thousand sixty-six okay so we're going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m33s)
00:23:33

[to use this set of data to train a model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m37s)
00:23:37

[and this set of data to see how well](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m39s)
00:23:39

[it's working so when we then tried that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m41s)
00:23:41

[last week we found out just a moment we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m44s)
00:23:44

[found out that our model which had point](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m48s)
00:23:48

[nine eight two R squared on the training](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m50s)
00:23:50

[set only had point eight eight seven on](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m52s)
00:23:52

[the validation set which makes us think](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m55s)
00:23:55

[that we're overfitting quite badly but](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h23m57s)
00:23:57

[it turned out it wasn't too badly](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m00s)
00:24:00

[because the root mean squared error on](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m02s)
00:24:02

[the logs of the prices actually would](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m04s)
00:24:04

[have caught us in the top 25 percent of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m06s)
00:24:06

[the competition anyway so even although](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m09s)
00:24:09

[we're overfitting it wasn't the end of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m10s)
00:24:10

[the world could you pass the microphone](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m12s)
00:24:12

[to Marsha please ah in terms of you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m14s)
00:24:14

[dividing the set into training and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m20s)
00:24:20

[validation it seems like you simply take](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m23s)
00:24:23

[the first and train observations of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m26s)
00:24:26

[data status and set them aside why don't](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m29s)
00:24:29

[you like why don't you randomly pick up](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m32s)
00:24:32

[the observations because if I did that I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m35s)
00:24:35

[wouldn't be replicating the test set so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m38s)
00:24:38

[cattle has a test set that when you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m41s)
00:24:41

[actually look at the dates in the test](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m43s)
00:24:43

[set they are a set of dates that are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m45s)
00:24:45

[more recent than any date in the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m48s)
00:24:48

[training set so if we used a validation](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m51s)
00:24:51

[set that was a random sample that is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m53s)
00:24:53

[much easier because we're predicting](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m56s)
00:24:56

[options like what's the value of this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h24m58s)
00:24:58

[piece of industrial equipment on this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m00s)
00:25:00

[day when we add](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m02s)
00:25:02

[we already have some observations from](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m03s)
00:25:03

[that day so in general anytime you're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m05s)
00:25:05

[building a model that has a time element](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m09s)
00:25:09

[you want your test set to be a separate](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m12s)
00:25:12

[time period and therefore you really](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m16s)
00:25:16

[need your validation set to be observer](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m18s)
00:25:18

[time period as well and in this case the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m19s)
00:25:19

[data was already sorted that's why this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m21s)
00:25:21

[works so let's say we have our test the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m23s)
00:25:23

[training set by which we in the data and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m33s)
00:25:33

[then we have the validation set against](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m35s)
00:25:35

[which we are trying to find the r-square](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m37s)
00:25:37

[in in case of r-squared turns out to be](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m39s)
00:25:39

[really bad we would want to cheer to not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m42s)
00:25:42

[parameters and run it again yes so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m45s)
00:25:45

[wouldn't that be eventually overfitting](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m48s)
00:25:48

[on the overall training set yeah so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m50s)
00:25:50

[actually that's that's the issue so that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m53s)
00:25:53

[would eventually have the possibility of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m55s)
00:25:55

[overfitting on the validation set and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m57s)
00:25:57

[then when you try it on the test set or](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h25m59s)
00:25:59

[we submit it to kaggle it turns out not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m01s)
00:26:01

[to be very good and this happens in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m03s)
00:26:03

[careful competitions all the time](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m05s)
00:26:05

[careful actually has a fourth data set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m06s)
00:26:06

[which is called the private leader board](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m09s)
00:26:09

[set and every time you submit to Kaggle](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m11s)
00:26:11

[you actually only get feedback on how](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m14s)
00:26:14

[well it does on something called the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m17s)
00:26:17

[public leader board set and you don't](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m18s)
00:26:18

[know which rows they are and at the end](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m21s)
00:26:21

[of the competition you actually get](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m23s)
00:26:23

[judged on a different data set entirely](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m24s)
00:26:24

[called the private leader board set so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m26s)
00:26:26

[the only way to avoid this is to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m29s)
00:26:29

[actually be a good machine learning](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m32s)
00:26:32

[practitioner and know how to set these](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m34s)
00:26:34

[parameters as effectively as possible](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m37s)
00:26:37

[which we're going to be doing gladly](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m38s)
00:26:38

[today and over the next few weeks](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m41s)
00:26:41

[can you get that actually watching](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m45s)
00:26:45

[is it too early or late to ask what's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m53s)
00:26:53

[the difference between a paper parameter](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m57s)
00:26:57

[and a parameter okay so let's start](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h26m58s)
00:26:58

[tracking things on written in spread era](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m12s)
00:27:12

[so here is root mean square error in a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m14s)
00:27:14

[line of code and you can see here like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m18s)
00:27:18

[this is one of these examples where I'm](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m19s)
00:27:19

[not writing this the way a proper](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m22s)
00:27:22

[software engineer would write this right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m25s)
00:27:25

[so a proper software engineer would be a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m26s)
00:27:26

[number of things differently they would](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m28s)
00:27:28

[have it on a different line they would](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m29s)
00:27:29

[use longer variable names they would](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m32s)
00:27:32

[have documentation blah blah blah right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m40s)
00:27:40

[but](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m44s)
00:27:44

[I really think like for me I really](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m47s)
00:27:47

[think that being able to look at](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m50s)
00:27:50

[something in one go with your eyes and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m57s)
00:27:57

[like over time learn to immediately see](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h27m59s)
00:27:59

[what's going on has a lot of value and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m02s)
00:28:02

[also to like consistently use like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m05s)
00:28:05

[particular letters to have many](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m09s)
00:28:09

[particular things or abbreviations I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m11s)
00:28:11

[think works really well in data science](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m13s)
00:28:13

[if you're doing it like a take-home](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m16s)
00:28:16

[interview test or something you should](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m21s)
00:28:21

[write your code according to pet eight](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m25s)
00:28:25

[standards right so pep eight is the the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m28s)
00:28:28

[style guide for python code and you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m32s)
00:28:32

[should know it and use it because a lot](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m34s)
00:28:34

[of software engineers are super anal](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m36s)
00:28:36

[about this kind of thing but for your](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m38s)
00:28:38

[own work you know I think this is I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m41s)
00:28:41

[think this works well for me you know so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m46s)
00:28:46

[I just wanted to make you aware a that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m48s)
00:28:48

[you shouldn't necessarily use this as a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m50s)
00:28:50

[role model for dealing with software](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m52s)
00:28:52

[engineers but B that I actually think](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m54s)
00:28:54

[this is not this is a reasonable](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m57s)
00:28:57

[approach okay so there's a root mean](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h28m59s)
00:28:59

[squared error and then from time to time](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m01s)
00:29:01

[we're just going to print out the score](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m03s)
00:29:03

[which will give us the RMS C of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m04s)
00:29:04

[predictions on the training versus the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m07s)
00:29:07

[actual there are predictions on the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m09s)
00:29:09

[valid versus the actual RMS see the R](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m10s)
00:29:10

[squared for the training and the R](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m13s)
00:29:13

[squared of the Bell and we'll come back](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m14s)
00:29:14

[to over in a moment so when we ran that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m16s)
00:29:16

[we found that this rmse was in the top](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m19s)
00:29:19

[25% and it's like okay there's a good](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m22s)
00:29:22

[start now this took eight seconds of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m24s)
00:29:24

[wall time so eight actual seconds if you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m31s)
00:29:31

[put percent time it'll tell you how long](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m33s)
00:29:33

[things talk and luckily I've got quite a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m35s)
00:29:35

[few calls quite a few CPUs in this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m38s)
00:29:38

[computer because it actually took over a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m40s)
00:29:40

[minute a compute time so I paralyzed](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m43s)
00:29:43

[that across cause if your dataset was](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m45s)
00:29:45

[bigger or you had less cause you know](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m50s)
00:29:50

[you could well find that this took a few](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m53s)
00:29:53

[minutes to run or even a few hours and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m55s)
00:29:55

[my rule of thumb is that if something](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h29m57s)
00:29:57

[takes more](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m00s)
00:30:00

[10 seconds to run it's too long for me](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m01s)
00:30:01

[to do like interactive analysis with it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m05s)
00:30:05

[right I want to be able to like run](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m09s)
00:30:09

[something wait a moment](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m10s)
00:30:10

[and then continue so what we do is we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m12s)
00:30:12

[try to make sure that things can run in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m17s)
00:30:17

[a reasonable time and then when we're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m19s)
00:30:19

[when we're finished at the end of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m22s)
00:30:22

[day we can then say ok this feature](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m24s)
00:30:24

[engineering these hyper parameters](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m27s)
00:30:27

[whatever these are all working well and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m28s)
00:30:28

[I'll now rerun it you know that's the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m30s)
00:30:30

[big slow precise way so one way to speed](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m33s)
00:30:33

[things up is to pass in the subset](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m37s)
00:30:37

[parameter to proc DF and that will](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m39s)
00:30:39

[randomly sample my data right and so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m42s)
00:30:42

[here I'm got a randomly sample 30,000](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m46s)
00:30:46

[rows now when I do that I still need to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m48s)
00:30:48

[be careful to make sure that my](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m53s)
00:30:53

[validation set doesn't change and that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m55s)
00:30:55

[my training set doesn't overlap with the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h30m58s)
00:30:58

[dates otherwise I'm cheating](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m01s)
00:31:01

[so I call split bells again to again do](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m03s)
00:31:03

[this split by dates and you'll also see](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m06s)
00:31:06

[I'm using rather than putting it into a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m10s)
00:31:10

[validation set I'm putting it into a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m12s)
00:31:12

[variable called underscore this is kind](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m14s)
00:31:14

[of a standard approach in Python is to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m16s)
00:31:16

[use a variable called underscore if you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m18s)
00:31:18

[want to throw something away because I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m20s)
00:31:20

[don't want to change my validation set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m22s)
00:31:22

[like no matter what different models I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m23s)
00:31:23

[build I want to be able to compare them](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m25s)
00:31:25

[all to each other so I want to keep my](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m27s)
00:31:27

[validation set the same all the time](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m29s)
00:31:29

[okay so all I'm doing here is I'm](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m30s)
00:31:30

[resampling my training set into a 20 the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m32s)
00:31:32

[first 20,000 out of a 30,000 subsets so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m36s)
00:31:36

[I now could run that and it runs it 621](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m41s)
00:31:41

[milliseconds so I can like really zip](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m44s)
00:31:44

[through things now try things out okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m47s)
00:31:47

[so with that let's use this subset to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m49s)
00:31:49

[build a model that is so simple that we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m55s)
00:31:55

[can actually take a look at it and so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h31m59s)
00:31:59

[we're going to build a forest is made of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m01s)
00:32:01

[trees and so before we look at the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m04s)
00:32:04

[forest we look at the trees in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m07s)
00:32:07

[scikit-learn they don't call them trees](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m09s)
00:32:09

[they call them estimators](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m12s)
00:32:12

[so we're going to pass in the parameter](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m14s)
00:32:14

[number of estimators equals one the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m15s)
00:32:15

[Creator forest with just one tree and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m18s)
00:32:18

[then we're going to make a small tree](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m21s)
00:32:21

[so we pass in maximum depth equals three](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m23s)
00:32:23

[and a random forest as we're going to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m26s)
00:32:26

[learn randomizes a whole bunch of things](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m28s)
00:32:28

[we want to turn that off so to turn that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m31s)
00:32:31

[off you say bootstrap equals false so if](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m34s)
00:32:34

[I pass you in these parameters that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m36s)
00:32:36

[creates a small deterministic tree okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m38s)
00:32:38

[so if I fit it and say print score my a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m43s)
00:32:43

[squared has gone down from point eight](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m46s)
00:32:46

[five two point four so this is not a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m48s)
00:32:48

[good model it's better than the mean](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m51s)
00:32:51

[model this is better than zero right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m54s)
00:32:54

[it's not a good model but it's a model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m55s)
00:32:55

[that we can draw all right so let's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h32m58s)
00:32:58

[learn about what it's built so a tree](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m02s)
00:33:02

[consists of a sequence of binary](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m07s)
00:33:07

[decisions of binary splits so at first](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m10s)
00:33:10

[of all decided to split on coupla system](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m15s)
00:33:15

[greater than or less than point five](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m18s)
00:33:18

[that's boolean variable so it's actually](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m20s)
00:33:20

[true or false and then within the group](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m22s)
00:33:22

[we're a couple system was true we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m25s)
00:33:25

[decided to split into year made greater](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m27s)
00:33:27

[than or less than 1987 and then we're a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m29s)
00:33:29

[couple system was true and year made was](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m32s)
00:33:32

[less than or equal to 1986](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m34s)
00:33:34

[it used fi product class desk is less](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m36s)
00:33:36

[than or equal to 0.75 and so forth right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m39s)
00:33:39

[so right at the top we have 20,000](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m43s)
00:33:43

[samples 20,000 rows right and the reason](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m47s)
00:33:47

[for that is because that's what we asked](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m50s)
00:33:50

[for here when we split our data in the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m54s)
00:33:54

[sample](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h33m56s)
00:33:56

[I just want to double-check that for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m02s)
00:34:02

[your decision tree that you had there](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m04s)
00:34:04

[that the coloration was whether it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m06s)
00:34:06

[true or false not so like it it gets](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m08s)
00:34:08

[darker it's true for the next one not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m11s)
00:34:11

[the darker is a higher value we'll get](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m14s)
00:34:14

[to that in a moment okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m17s)
00:34:17

[so let's look at these numbers here so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m18s)
00:34:18

[in the whole data set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m21s)
00:34:21

[well our sample that we're using there](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m22s)
00:34:22

[are 20,000 rows](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m25s)
00:34:25

[the meter the average of the log of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m26s)
00:34:26

[Christ is 10.1 and if we built a model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m30s)
00:34:30

[where we just used that average all the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m34s)
00:34:34

[time then the mean squared error would](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m36s)
00:34:36

[be 0.477 okay so this is in other words](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m39s)
00:34:39

[the denominator of an R squared all](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m44s)
00:34:44

[right this is like the most basic model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m49s)
00:34:49

[is a tree with zero splits right which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m50s)
00:34:50

[is just predict the average so the best](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m53s)
00:34:53

[single binary split we can make it turns](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h34m57s)
00:34:57

[out to be splitting by where the coupler](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m02s)
00:35:02

[system is greater than or equal to sorry](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m03s)
00:35:03

[less than or equal to or greater than](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m06s)
00:35:06

[0.5 know whether it's true or false and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m07s)
00:35:07

[turns out if we do that the mean squared](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m09s)
00:35:09

[error of couple system is less than 0.5](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m12s)
00:35:12

[so it's false goes down from 0.477 to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m15s)
00:35:15

[0.1 one right so it's really improved](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m20s)
00:35:20

[the error a lot in the other group it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m23s)
00:35:23

[only improved at a bit so I'm from 0.47](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m26s)
00:35:26

[2.41](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m28s)
00:35:28

[and so we can see that the coupler](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m30s)
00:35:30

[system equals false group has a pretty](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m33s)
00:35:33

[small percentage it's only got twenty](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m35s)
00:35:35

[two hundred of the twenty thousand all](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m38s)
00:35:38

[right where else this other group has a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m41s)
00:35:41

[much larger percentage but it hasn't](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m43s)
00:35:43

[improved it as much so let's say you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m45s)
00:35:45

[wanted to create a tree with just one](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m50s)
00:35:50

[split so you're just trying to find like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m54s)
00:35:54

[what is the very best single binary](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h35m56s)
00:35:56

[decision you can make for your data how](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m01s)
00:36:01

[might you be able to do that how could](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m05s)
00:36:05

[you do it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m06s)
00:36:06

[I'm gonna give it to foot](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m09s)
00:36:09

[specify the max depth of one but I mean](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m13s)
00:36:13

[your writing you don't have a random](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m17s)
00:36:17

[first write how are you going to how are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m18s)
00:36:18

[you going to like write what's an](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m21s)
00:36:21

[algorithm a simple algorithm which you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m23s)
00:36:23

[could use sure so we want to start](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m25s)
00:36:25

[building a random forest from scratch so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m29s)
00:36:29

[the first step is to create a tree the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m32s)
00:36:32

[first step to create a tree is to create](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m34s)
00:36:34

[the first binary decision how are you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m37s)
00:36:37

[gonna do it I'm gonna give it to Chris](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m40s)
00:36:40

[maybe in two steps](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m42s)
00:36:42

[so isn't this simply trying to find the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m48s)
00:36:48

[best predictor based on maybe a linear](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m52s)
00:36:52

[regression you could use a linear](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m54s)
00:36:54

[regression but could you do something](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h36m57s)
00:36:57

[much simpler and more complete we're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m00s)
00:37:00

[trying not to use any statistical](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m03s)
00:37:03

[assumptions here I can't see your name](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m05s)
00:37:05

[sorry](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m08s)
00:37:08

[and of course your friends anything can](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m09s)
00:37:09

[we just do like take just one variable](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m14s)
00:37:14

[if it is true give it like the true](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m16s)
00:37:16

[thing and if it is false so which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m20s)
00:37:20

[variable are we gonna choose so at each](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m24s)
00:37:24

[binary point we have to choose a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m25s)
00:37:25

[variable and something to split on how](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m27s)
00:37:27

[are we going to do that then I pass it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m31s)
00:37:31

[over there how do I pronounce your name](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m33s)
00:37:33

[chicken so the variability tools could](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m36s)
00:37:36

[be like which divides population into](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m42s)
00:37:42

[two groups which kind of heterogeneous](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m44s)
00:37:44

[to each other and homogeneous within](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m47s)
00:37:47

[themselves like having the same quality](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m50s)
00:37:50

[within themselves and they are very](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m52s)
00:37:52

[different](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m55s)
00:37:55

[could you be more specific like in terms](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m55s)
00:37:55

[of the target variable maybe yeah right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h37m59s)
00:37:59

[let's say we have two groups of tested](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m01s)
00:38:01

[so one has a different price altogether](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m03s)
00:38:03

[from the second group yes internally](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m06s)
00:38:06

[they have similar prices okay that's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m09s)
00:38:09

[good](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m11s)
00:38:11

[so like to simplify things a little bit](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m11s)
00:38:11

[when we're saying find a variable that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m14s)
00:38:14

[we could split into such that the two](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m16s)
00:38:16

[groups are as different to each other as](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m19s)
00:38:19

[possible and okay how do you how would](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m21s)
00:38:21

[you pick which variable and which split](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m26s)
00:38:26

[point that's the question](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m28s)
00:38:28

[yeah what's your first cut which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m37s)
00:38:37

[variable and which split point](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m39s)
00:38:39

[we don't like we're making the trade](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m46s)
00:38:46

[from scratch we want to create our own](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m48s)
00:38:48

[tree that makes sense we've got somebody](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m50s)
00:38:50

[amazing](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h38m53s)
00:38:53

[can we test all of the possible split](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m03s)
00:39:03

[and see which one has this ah small and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m05s)
00:39:05

[rmse that sounds good okay so let's dig](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m08s)
00:39:08

[into this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m10s)
00:39:10

[so when you say test all of the possible](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m11s)
00:39:11

[splits what does that mean how do we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m14s)
00:39:14

[enumerate all the possible splits](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m17s)
00:39:17

[oh and think of that but](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m23s)
00:39:23

[if you want for each variable you could](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m26s)
00:39:26

[put one aside and then put a second](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m32s)
00:39:32

[aside and compare the two and if it was](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m36s)
00:39:36

[better good okay so for each variable](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m38s)
00:39:38

[for each possible value of that variable](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m41s)
00:39:41

[see whether it's better now coming back](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m45s)
00:39:45

[to Maslak so I want to dig into the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m48s)
00:39:48

[better when you said see if the RMS see](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m49s)
00:39:49

[is better what does that mean though](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m52s)
00:39:52

[because after a split you've got two](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m54s)
00:39:54

[rmse so you've got two two groups so you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h39m56s)
00:39:56

[just gonna fit what that one variable](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m01s)
00:40:01

[comparing to the other it's not so so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m03s)
00:40:03

[what I mean here is that before we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m06s)
00:40:06

[decided to speed on coupler system we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m08s)
00:40:08

[had a root mean square root of 0.477 and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m10s)
00:40:10

[after we've got two groups one were the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m13s)
00:40:13

[mean square error point one another with](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m16s)
00:40:16

[a mean squared error of 0.4 so you treat](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m18s)
00:40:18

[each individual model separately so for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m22s)
00:40:22

[the first player you're just gonna](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m25s)
00:40:25

[compare between each variable in himself](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m26s)
00:40:26

[and then you move on to the next node](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m28s)
00:40:28

[with the remaining but but even the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m30s)
00:40:30

[first node like so the model with zero](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m32s)
00:40:32

[splits has a single root mean squared](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m37s)
00:40:37

[error the model with one split so the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m39s)
00:40:39

[very first thing we tried we've now got](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m42s)
00:40:42

[two groups with two mean square errors](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m44s)
00:40:44

[you don't give it to Daniel do you pick](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m47s)
00:40:47

[the one that gets them as different as](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m52s)
00:40:52

[they can be well we're truck well okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m54s)
00:40:54

[that would be one idea get the two mean](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m56s)
00:40:56

[squared errors as different as possible](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h40m59s)
00:40:59

[but why might that not work what might](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m01s)
00:41:01

[be a problem with that sample size come](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m04s)
00:41:04

[on because you could just literally](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m08s)
00:41:08

[leave one point out yeah so we could](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m10s)
00:41:10

[have like year made is less than 1950](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m12s)
00:41:12

[and it might have a single sample with a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m15s)
00:41:15

[low price and like that's not a great](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m18s)
00:41:18

[split is it you know because the other](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m21s)
00:41:21

[group is actually not going to be very](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m23s)
00:41:23

[interesting at all can you improve it a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m25s)
00:41:25

[bit can Jason improve it a bit](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m28s)
00:41:28

[could you take a weighted average yeah a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m33s)
00:41:33

[weighted average so we could take point](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m37s)
00:41:37

[four one times 17,000 plus 0.1 times](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m39s)
00:41:39

[2,000 that's good right and that would](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m42s)
00:41:42

[be the same as actually saying I've got](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m45s)
00:41:45

[a model the model is a single binary](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m49s)
00:41:49

[decision and I'm going to say for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m51s)
00:41:51

[everybody with year made less than](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m53s)
00:41:53

[ninety six point five I'm going to fill](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m55s)
00:41:55

[in point ten point two for everybody](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h41m57s)
00:41:57

[else are going to fill in nine point two](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m00s)
00:42:00

[and then I'm going to calculate the root](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m02s)
00:42:02

[mean squared error of this crappy model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m04s)
00:42:04

[and that would give exactly the same](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m07s)
00:42:07

[right as the weighted average that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m09s)
00:42:09

[you're suggesting okay good so we now](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m11s)
00:42:11

[have a single number that represents how](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m14s)
00:42:14

[good a split is which is the weighted](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m18s)
00:42:18

[average of the mean squared errors of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m21s)
00:42:21

[the two groups that creates okay and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m22s)
00:42:22

[thanks to I think it was was it Jake we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m25s)
00:42:25

[have a way to find the best split which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m28s)
00:42:28

[is to try every variable and to try](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m30s)
00:42:30

[every possible value of that variable](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m32s)
00:42:32

[and see which variable and which value](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m34s)
00:42:34

[gives us a split with the best score](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m36s)
00:42:36

[that makes sense](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m40s)
00:42:40

[okay what's your name sir okay and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m42s)
00:42:42

[somebody give Natalie the box when you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m50s)
00:42:50

[see every possible number for every](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h42m59s)
00:42:59

[possible variable link are you saying](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m01s)
00:43:01

[like here we have 0.5 as like our](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m04s)
00:43:04

[criteria to split the tree so are you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m08s)
00:43:08

[are you saying we're trying out a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m12s)
00:43:12

[reasonable number for every possible](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m14s)
00:43:14

[value right so cupola system only has](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m18s)
00:43:18

[two values true and false so there's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m20s)
00:43:20

[only one way of splitting which is trues](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m23s)
00:43:23

[and falses ear made is an integer which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m25s)
00:43:25

[varies between like O'Donnell 1960 and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m29s)
00:43:29

[2010 so we can just say what are all the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m31s)
00:43:31

[possible unique values of year made and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m33s)
00:43:33

[and try them all so we're trying all the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m35s)
00:43:35

[possible spec points can you pass a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m38s)
00:43:38

[better annual pass to me and I so I just](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m40s)
00:43:40

[want to clarify again for the first](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m56s)
00:43:56

[split why did we split on Cutler system](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h43m59s)
00:43:59

[true or false sister because what we did](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m04s)
00:44:04

[was we used Jake's technique we tried](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m06s)
00:44:06

[every variable for every variable we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m09s)
00:44:09

[tried every possible split so each one](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m12s)
00:44:12

[we noted down I think it was Jason's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m15s)
00:44:15

[idea which was the weighted average mean](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m17s)
00:44:17

[squared error of the two groups are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m20s)
00:44:20

[created we found which one had the best](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m22s)
00:44:22

[means grid error and we picked it and it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m24s)
00:44:24

[turned out it was cutlass system true or](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m28s)
00:44:28

[false](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m30s)
00:44:30

[does that make sense I guess my question](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m32s)
00:44:32

[is more like so coupler system is like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m35s)
00:44:35

[one of them like best indicators I guess](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m39s)
00:44:39

[it's the best we tried every variable](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m43s)
00:44:43

[and every possible level everything else](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m46s)
00:44:46

[at try it wasn't as good okay and then](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m51s)
00:44:51

[you do that right so now that we've done](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m53s)
00:44:53

[that we now take this group here](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m56s)
00:44:56

[everybody who's got coupler system](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h44m58s)
00:44:58

[equals true and we do it again for every](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m00s)
00:45:00

[possible variable for every possible](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m03s)
00:45:03

[level for people where coupler system](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m05s)
00:45:05

[equals true what's the best possible](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m07s)
00:45:07

[split and then are there circumstances](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m10s)
00:45:10

[when it's not just like binaries like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m13s)
00:45:13

[you split it into like three groups for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m16s)
00:45:16

[like example you're made so I'm gonna](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m18s)
00:45:18

[make a claim and then I'm gonna see if](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m20s)
00:45:20

[you can justify it I'm gonna claim that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m22s)
00:45:22

[it's never necessary to do more than one](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m24s)
00:45:24

[split at a level because you can just](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m28s)
00:45:28

[cuz you can just split them again](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m31s)
00:45:31

[exactly so you can get exactly the same](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m32s)
00:45:32

[result by submitting twice okay good so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m35s)
00:45:35

[that is the entirety of creating a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m42s)
00:45:42

[decision tree you stop either when you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m45s)
00:45:45

[hit some limit that was requested so we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m49s)
00:45:49

[had a limit where we said max depth](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m52s)
00:45:52

[equals three so that's one one way to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m54s)
00:45:54

[stop would be you ask to stop at some](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m56s)
00:45:56

[point and so we stopped otherwise you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h45m58s)
00:45:58

[stop when you're your leaf nodes these](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m01s)
00:46:01

[things at the end of court leaf nodes](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m05s)
00:46:05

[when your leaf nodes only have one thing](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m06s)
00:46:06

[in them okay that's a decision tree that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m08s)
00:46:08

[is how we grow a decision tree and this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m12s)
00:46:12

[decision tree is not very good because](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m15s)
00:46:15

[it's got a validation r-squared of 0.4](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m16s)
00:46:16

[so we could try to make it better by](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m19s)
00:46:19

[removing next steps equals three right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m22s)
00:46:22

[and creating a deeper tree so it's going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m25s)
00:46:25

[to go all the way down they're going to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m27s)
00:46:27

[keep splitting these things further](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m29s)
00:46:29

[until every leaf node only has one thing](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m30s)
00:46:30

[in it and if we do that the training](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m33s)
00:46:33

[r-squared is of course one](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m37s)
00:46:37

[because we can exactly predict every](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m41s)
00:46:41

[training element because it's in a leaf](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m43s)
00:46:43

[node or on its own but the validation](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m45s)
00:46:45

[r-squared is not one it's actually](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m49s)
00:46:49

[better than our really really shallow](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m52s)
00:46:52

[tree but it's not as good as we'd like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m53s)
00:46:53

[okay so we want to find some other way](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h46m56s)
00:46:56

[of making these trees better and the way](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m01s)
00:47:01

[we're going to do it is to create a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m06s)
00:47:06

[forest so what's the forest to create a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m08s)
00:47:08

[forest we're going to use a statistical](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m13s)
00:47:13

[technique called bagging and you can bag](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m14s)
00:47:14

[any kind of model in fact Michael Jordan](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m19s)
00:47:19

[who is one of the speakers at the recent](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m23s)
00:47:23

[recent data Institute conference here at](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m24s)
00:47:24

[university of san francisco developed a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m26s)
00:47:26

[technique called the bag of little](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m28s)
00:47:28

[bootstraps and which he shows how to use](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m32s)
00:47:32

[bagging for absolutely any kind of model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m35s)
00:47:35

[to make it more robust and also to give](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m38s)
00:47:38

[you confidence intervals the random](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m41s)
00:47:41

[forest is simply a way of bagging trees](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m44s)
00:47:44

[so what is bagging managing is a really](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m48s)
00:47:48

[interesting idea which is what if we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m52s)
00:47:52

[created five different models each of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m55s)
00:47:55

[which was only somewhat predictive but](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h47m59s)
00:47:59

[the models weren't at all correlated](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m02s)
00:48:02

[with each other they gave predictions](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m04s)
00:48:04

[that weren't correlated with each other](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m07s)
00:48:07

[that would mean that the five models](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m08s)
00:48:08

[would have profound different insights](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m10s)
00:48:10

[into the relationships in the data and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m13s)
00:48:13

[so if you took the average of those five](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m16s)
00:48:16

[models right then you're effectively](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m18s)
00:48:18

[bringing in the insights from each of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m21s)
00:48:21

[them and so this idea of averaging](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m23s)
00:48:23

[models is a is is a technique for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m26s)
00:48:26

[ensemble right which is really important](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m30s)
00:48:30

[now let's come up with a more specific](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m34s)
00:48:34

[idea of how to do this ensemble what if](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m37s)
00:48:37

[we created a whole lot of these trees](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m40s)
00:48:40

[big deep massively overfit trees right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m44s)
00:48:44

[but each one let's say we only pick a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m49s)
00:48:49

[random](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m52s)
00:48:52

[one-tenth of the data so we pick one out](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m53s)
00:48:53

[of every 10 rows at random build a deep](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h48m57s)
00:48:57

[tree right which is perfect on that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m00s)
00:49:00

[subset and kind of crappy on the rest](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m04s)
00:49:04

[all right let's say we do that a hundred](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m07s)
00:49:07

[times so different random sample every](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m09s)
00:49:09

[time so all of the trees are going to be](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m12s)
00:49:12

[better than nothing right because they](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m15s)
00:49:15

[do actually have a real random subset of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m16s)
00:49:16

[the data and so they found some insight](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m18s)
00:49:18

[but they're also overfitting terribly](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m20s)
00:49:20

[but they're all using different random](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m22s)
00:49:22

[samples so they all over fit in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m24s)
00:49:24

[different ways on different things so in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m26s)
00:49:26

[other words they all have errors but the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m28s)
00:49:28

[errors are random what is the average of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m31s)
00:49:31

[a bunch of random errors zero so in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m36s)
00:49:36

[other words if we take the average of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m41s)
00:49:41

[these trees each of which have been](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m43s)
00:49:43

[trained on a different random subset the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m45s)
00:49:45

[errors will average out to zero and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m47s)
00:49:47

[what's left is the true relationship and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m49s)
00:49:49

[that's the random forest right so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m52s)
00:49:52

[there's the technique right we've got a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m55s)
00:49:55

[whole bunch of rows of data we grab a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h49m58s)
00:49:58

[few at random all right put them into a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m01s)
00:50:01

[smaller data set and build a tree based](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m05s)
00:50:05

[on that okay and then we put that tree](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m08s)
00:50:08

[aside and do it again with a different](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m13s)
00:50:13

[random subset and do it again with a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m16s)
00:50:16

[different random subset do that a whole](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m18s)
00:50:18

[bunch of times and then for each one we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m20s)
00:50:20

[can then make predictions by running our](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m23s)
00:50:23

[test data through the tree to get to the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m26s)
00:50:26

[leaf mode take the average in that leaf](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m29s)
00:50:29

[node for all the trees and average them](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m32s)
00:50:32

[all together so to do that we simply](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m34s)
00:50:34

[call random forests regressor and by](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m39s)
00:50:39

[default it creates n what scikit-learn](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m42s)
00:50:42

[cords estimators an estimator is a tree](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m45s)
00:50:45

[right so this is going to create ten](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m48s)
00:50:48

[treats](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m51s)
00:50:51

[and so we go ahead and train it I can't](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m53s)
00:50:53

[remember if I remember to split okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h50m59s)
00:50:59

[so create our ten trees and we're just](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m10s)
00:51:10

[doing this on our little random subset](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m12s)
00:51:12

[of 20,000 and so let's take a look at](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m14s)
00:51:14

[one example can you pass the box to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m19s)
00:51:19

[Devin so just to make sure I understand](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m22s)
00:51:22

[this so you're saying like we take ten](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m26s)
00:51:26

[kind of crappy models we average ten](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m28s)
00:51:28

[crappy models and we get a good model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m31s)
00:51:31

[exactly because the crappy models are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m33s)
00:51:33

[based on different random subsets and so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m36s)
00:51:36

[their errors are not correlated with](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m39s)
00:51:39

[each other if the error errors work are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m41s)
00:51:41

[they with other this isn't going to work](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m43s)
00:51:43

[okay so the key insight here is to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m45s)
00:51:45

[construct multiple models which are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m48s)
00:51:48

[better than nothing and where the errors](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m51s)
00:51:51

[are as much as possible not correlated](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m53s)
00:51:53

[with each other so is there like a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m55s)
00:51:55

[certain number of trees that like we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h51m59s)
00:51:59

[need that in order to be this sort of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m00s)
00:52:00

[the things like valid or invalid there's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m03s)
00:52:03

[like has a good validation set our MSC](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m05s)
00:52:05

[or not you know and so that's what we're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m08s)
00:52:08

[going to look at is how to make that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m12s)
00:52:12

[metric higher and so this is the first](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m14s)
00:52:14

[of our hyper parameters then we're going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m17s)
00:52:17

[to learn about how to tune hyper](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m20s)
00:52:20

[parameters and the first one is going to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m21s)
00:52:21

[be the number of trees and we're about](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m22s)
00:52:22

[to us look at that now yes mostly you're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m24s)
00:52:24

[selecting aren't they exclusive yes so I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m30s)
00:52:30

[mentioned you know one approach would be](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m35s)
00:52:35

[pick out like attempt at random but](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m37s)
00:52:37

[actually what scikit-learn does by](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m41s)
00:52:41

[default is for n rows it picks out n](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m42s)
00:52:42

[rows with replacement okay and that's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m46s)
00:52:46

[called bootstrapping and if memory](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m49s)
00:52:49

[serves me correctly that gets you on](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m51s)
00:52:51

[average 63.2% of the rows will be](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m54s)
00:52:54

[represented and you know a bunch of them](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m57s)
00:52:57

[will be represented multiple times yeah](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h52m59s)
00:52:59

[it sure so rather than just picking out](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m03s)
00:53:03

[like a tenth of the rows at random](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m07s)
00:53:07

[instead we're going to pick out of an n](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m09s)
00:53:09

[row data set we're going to pick out n](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m12s)
00:53:12

[rows with replacement which on average](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m14s)
00:53:14

[gets about 63 I think 63.2% of the rows](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m17s)
00:53:17

[will be represented many of those rows](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m20s)
00:53:20

[will appear multiple times I think](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m24s)
00:53:24

[there's a question behind you in essence](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m27s)
00:53:27

[what this model is doing is if I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m33s)
00:53:33

[understand Craig is just picking out](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m35s)
00:53:35

[data points that look very similar to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m37s)
00:53:37

[the one you're looking at yeah that's a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m39s)
00:53:39

[great insight so what a tree is kind of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m42s)
00:53:42

[doing there's no quite complicated way](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m44s)
00:53:44

[of doing about doing that I mean there](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m46s)
00:53:46

[would be other ways of assessing](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m49s)
00:53:49

[similarity there are other ways of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m50s)
00:53:50

[assessing similarity but what's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m52s)
00:53:52

[interesting about this way is it's doing](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m54s)
00:53:54

[it in in tree space right so we're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h53m56s)
00:53:56

[basically saying what are in this case](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m00s)
00:54:00

[like for this little tree what are the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m01s)
00:54:01

[593 samples you know closest to this one](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m03s)
00:54:03

[and what's their average closest in tree](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m06s)
00:54:06

[space so other ways of doing that would](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m08s)
00:54:08

[be like and we'll learn later on in this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m11s)
00:54:11

[course about K nearest neighbors you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m12s)
00:54:12

[could use like Euclidean distance C](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m14s)
00:54:14

[right but here's a thing the whole point](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m17s)
00:54:17

[of machine learning is to identify which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m22s)
00:54:22

[variables actually matter the most and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m25s)
00:54:25

[how do they relate to each other and to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m28s)
00:54:28

[your dependent variable together right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m30s)
00:54:30

[so if you've like imagine a synthetic](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m33s)
00:54:33

[data set where you create five variables](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m35s)
00:54:35

[that add together to create your](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m37s)
00:54:37

[independent to create your dependent](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m39s)
00:54:39

[variable and ninety five variables which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m41s)
00:54:41

[are entirely random and don't impact](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m43s)
00:54:43

[your dependent variable and then if you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m45s)
00:54:45

[do like a K nearest neighbors in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m47s)
00:54:47

[Euclidean space you're going to get](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m49s)
00:54:49

[meaningless nearest neighbors because](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m51s)
00:54:51

[most of your columns are actually](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m53s)
00:54:53

[meaningless or imagine your actual](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m54s)
00:54:54

[relationship is that your dependent](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m57s)
00:54:57

[variable equals x1 times x2 then you'll](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h54m58s)
00:54:58

[actually need to find this interaction](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m03s)
00:55:03

[right so you don't actually care about](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m05s)
00:55:05

[how close it is to x1 and how close to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m07s)
00:55:07

[x2 but how close to the product so the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m09s)
00:55:09

[entire purpose of modeling in machine](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m12s)
00:55:12

[learning is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m14s)
00:55:14

[to find a model which tells you which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m15s)
00:55:15

[variables are important and how do they](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m18s)
00:55:18

[interact together to drive your](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m20s)
00:55:20

[dependent variable and so you'll find in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m21s)
00:55:21

[practice the difference between using](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m24s)
00:55:24

[like tree space or random forest space](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m27s)
00:55:27

[to find your nearest neighbors versus](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m30s)
00:55:30

[like Euclidean space is the difference](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m32s)
00:55:32

[between a model that makes good](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m35s)
00:55:35

[predictions in the model that makes many](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m37s)
00:55:37

[most predictions elicit here](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m39s)
00:55:39

[I did but I feel like we've got only 35](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m43s)
00:55:43

[minutes so yeah great so so in general a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m47s)
00:55:47

[machine learning model which is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h55m58s)
00:55:58

[effective is one which is accurate when](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m00s)
00:56:00

[you look at the training data it's it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m07s)
00:56:07

[accurate at predicting at actually](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m09s)
00:56:09

[finding the relationships in that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m12s)
00:56:12

[training data and then it generalizes](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m14s)
00:56:14

[well to new data and so in bagging that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m16s)
00:56:16

[means that each of your individual](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m21s)
00:56:21

[estimators at your individual trees you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m23s)
00:56:23

[want to be as predictive as possible but](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m27s)
00:56:27

[for the predictions of your individual](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m30s)
00:56:30

[trees to be as uncorrelated as possible](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m32s)
00:56:32

[and so the inventor of random forests](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m34s)
00:56:34

[talks about this at length in his](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m36s)
00:56:36

[original paper that introduced this in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m38s)
00:56:38

[the late 90s this idea of trying to come](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m40s)
00:56:40

[up with predictive but poorly correlated](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m42s)
00:56:42

[trees the the research community in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m45s)
00:56:45

[recent years has generally found that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m50s)
00:56:50

[the more important thing seems to be](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m53s)
00:56:53

[creating uncorrelated trees rather than](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h56m56s)
00:56:56

[more accurate trees so more recent](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m00s)
00:57:00

[advances tend to create trees which are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m02s)
00:57:02

[less predictive on their own but also](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m05s)
00:57:05

[less correlated with each other so for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m08s)
00:57:08

[example in scikit-learn there's another](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m10s)
00:57:10

[class you can use called extra trees](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m13s)
00:57:13

[regress on your extra trees classifier](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m16s)
00:57:16

[with exactly the same API you can try it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m18s)
00:57:18

[tonight just replace my random prose](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m20s)
00:57:20

[regressor with that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m22s)
00:57:22

[that's called an extremely randomized](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m23s)
00:57:23

[trees model and what that does is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m25s)
00:57:25

[the same as what we just discussed but](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m29s)
00:57:29

[rather than trying every speck of every](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m31s)
00:57:31

[variable it randomly tries a few splits](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m33s)
00:57:33

[of a few variables right so it's much](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m36s)
00:57:36

[faster the Train it has more randomness](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m39s)
00:57:39

[okay but then you've got time you can](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m42s)
00:57:42

[build more trees and therefore get](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m45s)
00:57:45

[better generalization so in practice if](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m48s)
00:57:48

[you've got crappy individual models you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m52s)
00:57:52

[just need more trees to get a good end](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m54s)
00:57:54

[up model Melissa could you pass that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m56s)
00:57:56

[over to Devin could you talk a little](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h57m58s)
00:57:58

[bit more about what you mean by like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m05s)
00:58:05

[uncorrelated trees yeah if I build a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m06s)
00:58:06

[thousand trees h1 on just ten data](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m11s)
00:58:11

[points then it's quite likely that the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m15s)
00:58:15

[ten data points for every tree are going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m20s)
00:58:20

[to be totally different and so it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m21s)
00:58:21

[quite likely that those ten trees are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m23s)
00:58:23

[going to trees are going to give totally](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m25s)
00:58:25

[different answers to each other so the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m27s)
00:58:27

[correlation between the predictions of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m30s)
00:58:30

[tree one and three two is going to be](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m33s)
00:58:33

[very small between tree one and three](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m34s)
00:58:34

[three very small and so forth on the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m36s)
00:58:36

[other hand if I create a thousand trees](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m38s)
00:58:38

[where each time I use the entire data](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m40s)
00:58:40

[set with just one element removed all](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m43s)
00:58:43

[those trees are going to be nearly](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m46s)
00:58:46

[identical ie their predictions will be](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m47s)
00:58:47

[highly correlated and so in the latter](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m50s)
00:58:50

[case it's probably not going to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m53s)
00:58:53

[generalize very well where else in the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m54s)
00:58:54

[former case the individual trees we're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m57s)
00:58:57

[not going to be very predictive so I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h58m59s)
00:58:59

[need to find some nice in-between so yes](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m01s)
00:59:01

[Danielle and is there a case where you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m09s)
00:59:09

[want to use one over the other like any](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m12s)
00:59:12

[particular times yeah so again hyper](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m14s)
00:59:14

[parameter tuning so driven in terms of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m17s)
00:59:17

[like random random forests versus](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m19s)
00:59:19

[extremely randomized phase yeah so again](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m20s)
00:59:20

[a hyper parameter walk tree architecture](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m23s)
00:59:23

[do we use so we're going to talk about](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m26s)
00:59:26

[that now can you pass that through do](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m27s)
00:59:27

[you know](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m30s)
00:59:30

[you know I was just trying to understand](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m32s)
00:59:32

[how this random forest actually makes](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m34s)
00:59:34

[sense for continuous variables I mean](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m36s)
00:59:36

[I'm assuming that you build a tree](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m38s)
00:59:38

[structure and the last final notes you'd](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m40s)
00:59:40

[be seeing like maybe the small node](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m42s)
00:59:42

[represents maybe a category a or a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m44s)
00:59:44

[category B but how does it make sense](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m47s)
00:59:47

[for your continuous storage so this is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m48s)
00:59:48

[actually what we have here and so the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m51s)
00:59:51

[value here is the average so this is the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m52s)
00:59:52

[average log of price for this subgroup](https://www.youtube.com/watch?v=blyXCk4sgEg#t=00h59m56s)
00:59:56

[and that's what we do the prediction is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m00s)
01:00:00

[the average of the value of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m03s)
01:00:03

[dependent variable in that leaf node](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m04s)
01:00:04

[means finally if you have just like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m07s)
01:00:07

[dengue nodes you just have 10 values yes](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m10s)
01:00:10

[that's right well if it was only one](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m13s)
01:00:13

[tree right so a couple things to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m16s)
01:00:16

[remember the first is that by default](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m18s)
01:00:18

[we're actually going to train the tree](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m19s)
01:00:19

[all the way down until the leaf nodes](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m21s)
01:00:21

[were size 1 which means for a data set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m23s)
01:00:23

[with n rows we're gonna have n leaf](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m27s)
01:00:27

[nodes and then we're going to have](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m29s)
01:00:29

[multiple trees which we average together](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m31s)
01:00:31

[right so in practice we're gonna have a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m33s)
01:00:33

[you know lots of different possible](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m37s)
01:00:37

[values it's a question behind you so far](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m40s)
01:00:40

[the continuous variable how do we decide](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m45s)
01:00:45

[like which value to split out because](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m47s)
01:00:47

[there could be many values we try every](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m49s)
01:00:49

[possible value of that in the training](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m51s)
01:00:51

[set one did be computationally](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m54s)
01:00:54

[computational expensive and this is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m57s)
01:00:57

[where it's very good to remember that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h00m59s)
01:00:59

[your CPUs performance is measured in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m01s)
01:01:01

[gigahertz which is billions of clock](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m04s)
01:01:04

[cycles per second and it has multiple](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m06s)
01:01:06

[cores and each core has something called](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m09s)
01:01:09

[Simbi single instruction multiple data](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m12s)
01:01:12

[where it can direct up to eight](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m14s)
01:01:14

[computations per core at once and then](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m16s)
01:01:16

[if you do it on the GPU the performance](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m19s)
01:01:19

[is measured in teraflops](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m22s)
01:01:22

[so trillions of floating-point](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m24s)
01:01:24

[operations per second and so this is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m27s)
01:01:27

[where when it comes to designing](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m29s)
01:01:29

[algorithms it's very difficult for us](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m32s)
01:01:32

[mere humans to realize how stupid](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m34s)
01:01:34

[algorithms should be given how fast](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m37s)
01:01:37

[today's computers are so yeah it's quite](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m40s)
01:01:40

[a few operations](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m43s)
01:01:43

[but that trillions per second you hardly](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m45s)
01:01:45

[notice it Russia I have a question so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m48s)
01:01:48

[essentially at each remote we make a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m53s)
01:01:53

[decision like which category T or which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h01m56s)
01:01:56

[variable to use and which pinpoint yes](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m00s)
01:02:00

[so we have MSE a calculated for each](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m05s)
01:02:05

[node so this is kind of our one of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m10s)
01:02:10

[decision criteria but please MSE it is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m13s)
01:02:13

[calculated for which model like which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m16s)
01:02:16

[model underlies the model is the model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m18s)
01:02:18

[is for the initial root mode is what if](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m22s)
01:02:22

[we just predicted the average right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m27s)
01:02:27

[which is here is ten point oh nine eight](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m30s)
01:02:30

[and just the average and then the next](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m32s)
01:02:32

[model is what if we predicted the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m35s)
01:02:35

[average of those people with capitalist](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m37s)
01:02:37

[system equals false and for those people](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m40s)
01:02:40

[with couple of system is true and then](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m43s)
01:02:43

[the next is what if we predicted the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m45s)
01:02:45

[average of couple systems equals true](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m47s)
01:02:47

[yeah made less than 1986 is it always](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m49s)
01:02:49

[average sure we can use median or we can](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m52s)
01:02:52

[even run linear regression there's all](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m54s)
01:02:54

[kinds of things we could do and practice](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m58s)
01:02:58

[the average works really well there are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h02m59s)
01:02:59

[there are types of they're not called](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m03s)
01:03:03

[random forests but there are kinds of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m06s)
01:03:06

[trees where the leaf nodes are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m08s)
01:03:08

[independent linear regressions they're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m09s)
01:03:09

[not terribly widely used but there are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m12s)
01:03:12

[certainly researchers who I have worked](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m14s)
01:03:14

[on them okay thank you and pass it back](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m16s)
01:03:16

[over that afford and then to check](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m19s)
01:03:19

[so this tree has a depth of three yeah](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m25s)
01:03:25

[and then I on one of the next commands](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m27s)
01:03:27

[we get rid of the max depth yeah the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m30s)
01:03:30

[tree without the max depth does that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m33s)
01:03:33

[contain the tree with with the depth of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m36s)
01:03:36

[three yeah so that is that like by](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m38s)
01:03:38

[definition it's yeah well except in this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m40s)
01:03:40

[case we've added randomness but if you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m42s)
01:03:42

[turned bootstrapping off then yeah the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m44s)
01:03:44

[the deeper tree will you know the the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m47s)
01:03:47

[the the less deep tree would be how it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m50s)
01:03:50

[start and then it goes keep spitting](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m53s)
01:03:53

[okay so you have many trees you're gonna](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h03m54s)
01:03:54

[have different leaf nodes across streets](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m02s)
01:04:02

[hopefully so we want um so how do you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m05s)
01:04:05

[average leaf nodes across different](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m07s)
01:04:07

[trees so we just take the first row in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m11s)
01:04:11

[the validation set we run it through the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m14s)
01:04:14

[first tree we find its average nine](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m16s)
01:04:16

[point two eight then do it through the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m19s)
01:04:19

[next tree find its average in the second](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m21s)
01:04:21

[tree nine point nine five and so forth](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m23s)
01:04:23

[and we're about to do that so you'll see](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m26s)
01:04:26

[it okay so let's try it right so after](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m27s)
01:04:27

[you've built a random forest each tree](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m32s)
01:04:32

[is stored in this attribute called](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m35s)
01:04:35

[estimators underscore okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m37s)
01:04:37

[so one of the things that you guys need](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m40s)
01:04:40

[to be very very comfortable with is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m42s)
01:04:42

[using list comprehensions okay so I hope](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m44s)
01:04:44

[you've all been practicing okay so here](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m47s)
01:04:47

[I'm using a list comprehension to go](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m49s)
01:04:49

[through each tree in my model I'm going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m51s)
01:04:51

[to call predict on it with my validation](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m54s)
01:04:54

[set and so that's going to give me a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m56s)
01:04:56

[list of arrays of predictions so H array](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h04m59s)
01:04:59

[will be all of the predictions for that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m05s)
01:05:05

[tree and I have ten trees MP dot stack](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m07s)
01:05:07

[concatenates them together on a new axis](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m12s)
01:05:12

[so after I run this and called shape you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m15s)
01:05:15

[can see I now have the first axis ten](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m22s)
01:05:22

[means I have my ten different sets of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m24s)
01:05:24

[predictions and for each one my](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m27s)
01:05:27

[validation set as a side of twelve](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m29s)
01:05:29

[thousand so here are my twelve thousand](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m30s)
01:05:30

[predictions for each of the ten trees](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m33s)
01:05:33

[alright so let's take the first row of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m35s)
01:05:35

[that and print it out and so here are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m40s)
01:05:40

[what weirdest thing here are ten](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m44s)
01:05:44

[predictions one from each tree okay and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m46s)
01:05:46

[so then if we say take the mean of that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m49s)
01:05:49

[here is the mean of those ten](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m52s)
01:05:52

[predictions and then what was the actual](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m54s)
01:05:54

[the actual was nine point one our](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h05m58s)
01:05:58

[prediction was nine point O seven so you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m01s)
01:06:01

[see how like none of our individual](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m03s)
01:06:03

[trees had very good predictions but the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m05s)
01:06:05

[mean of them was actually pretty good](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m08s)
01:06:08

[and so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m09s)
01:06:09

[when I talk about experimenting like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m11s)
01:06:11

[Jupiter notebook is great for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m13s)
01:06:13

[experimenting this is the kind of stuff](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m15s)
01:06:15

[I mean dig inside these objects and like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m17s)
01:06:17

[look at them and plot them take your own](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m20s)
01:06:20

[averages cross check to make sure that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m22s)
01:06:22

[they work the way you thought they did](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m24s)
01:06:24

[write your own implementation of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m25s)
01:06:25

[r-squared make sure it's the same as a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m27s)
01:06:27

[psychic learn version plot it like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m29s)
01:06:29

[here's an interesting plot I did let's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m31s)
01:06:31

[go through each Taffet entries right and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m34s)
01:06:34

[then take the mean of all of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m37s)
01:06:37

[predictions up to the ithe tree right so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m40s)
01:06:40

[let's start by predicting just based on](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m44s)
01:06:44

[the first tree than the first two trees](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m47s)
01:06:47

[and the first three trees and let's then](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m49s)
01:06:49

[plot the r-squared so here's the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m52s)
01:06:52

[r-squared of just the first tree is the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m55s)
01:06:55

[r-squared of the first two trees three](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h06m57s)
01:06:57

[trees four trees blah blah blah blah up](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m00s)
01:07:00

[to ten trees and so not surprisingly a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m01s)
01:07:01

[script keeps improving right because the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m04s)
01:07:04

[more estimators we have the more bagging](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m07s)
01:07:07

[that we're doing the more it's well it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m11s)
01:07:11

[going to generalize all right and you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m13s)
01:07:13

[should find that that number there bit](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m16s)
01:07:16

[under point eight six should match this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m19s)
01:07:19

[number here okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m22s)
01:07:22

[let's rerun that yeah okay so they're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m25s)
01:07:25

[actually slightly above what it says all](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m28s)
01:07:28

[right so again these are all like the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m30s)
01:07:30

[cross checks you can do the things you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m31s)
01:07:31

[can visualize to deepen your](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m33s)
01:07:33

[understanding okay so as we add more](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m34s)
01:07:34

[trees our r-squared improves it seems to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m37s)
01:07:37

[flatten out after a while so we might](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m39s)
01:07:39

[guess that if we increase the number of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m42s)
01:07:42

[estimators to twenty right it's maybe](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m44s)
01:07:44

[not going to be that much better](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m47s)
01:07:47

[so let's see we've got point eight six](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m52s)
01:07:52

[two first is point eight six oh yeah so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m56s)
01:07:56

[doubling the number of trees didn't help](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h07m59s)
01:07:59

[very much but double it again eight six](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m01s)
01:08:01

[seven double it again eight six nine so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m05s)
01:08:05

[you can see like there's some point at](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m09s)
01:08:09

[which you're going to you know not want](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m12s)
01:08:12

[to add more trees not because it's never](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m14s)
01:08:14

[going to get worse because every tree is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m16s)
01:08:16

[you know giving you more semi-random](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m18s)
01:08:18

[models to bag together](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m23s)
01:08:23

[right but it's going to stop improving](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m24s)
01:08:24

[things much okay and so this is like the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m27s)
01:08:27

[first hyper parameter if you learn to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m29s)
01:08:29

[set is number of estimators and the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m31s)
01:08:31

[method for setting is as many as you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m33s)
01:08:33

[have time to fit and that actually](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m38s)
01:08:38

[seemed to be hopping okay now in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m41s)
01:08:41

[practice we're going to learn to set a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m45s)
01:08:45

[few more hyper parameters adding more](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m46s)
01:08:46

[trees slows it down but with less trees](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m49s)
01:08:49

[you can still get the same insights so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m54s)
01:08:54

[I've build most of my models in practice](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m57s)
01:08:57

[with like 20 to 30 trees and it's only](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h08m59s)
01:08:59

[like then at the end of the project or](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m03s)
01:09:03

[maybe at the end of the day's work I'll](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m05s)
01:09:05

[then try doing like I don't know a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m06s)
01:09:06

[thousand trees and run it overnight was](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m08s)
01:09:08

[there a question yes can we pass that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m11s)
01:09:11

[Prince](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m13s)
01:09:13

[so each tree might have different](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m18s)
01:09:18

[estimators different combination of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m20s)
01:09:20

[estimators HQ is an estimator so this is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m21s)
01:09:21

[a synonym so in scikit-learn when I say](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m24s)
01:09:24

[estimator they name three so I mean each](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m26s)
01:09:26

[tree would have different break points](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m31s)
01:09:31

[on differently on different columns but](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m33s)
01:09:33

[if at the end we want to locate the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m35s)
01:09:35

[important features and we'll get to that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m37s)
01:09:37

[yeah so I'm after we finished with kind](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m40s)
01:09:40

[of setting hyper parameters the next](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m43s)
01:09:43

[stage of the course will be learning](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m45s)
01:09:45

[about what it tells us about the data if](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m48s)
01:09:48

[you need to know it now you know for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m52s)
01:09:52

[your projects feel free to look ahead](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m54s)
01:09:54

[there's a lesson to our F interpretation](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h09m56s)
01:09:56

[them is where we can see it okay so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m00s)
01:10:00

[that's our first type of parameter um I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m05s)
01:10:05

[want to talk next about out-of-bag score](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m08s)
01:10:08

[sometimes your data set will be kind of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m11s)
01:10:11

[small and you won't want to pull out a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m14s)
01:10:14

[validation set because doing so means](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m16s)
01:10:16

[you now don't have enough data to build](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m19s)
01:10:19

[a good model what do you do there's a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m21s)
01:10:21

[cool trick which is pretty much unique](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m24s)
01:10:24

[to random forests and it's this what we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m26s)
01:10:26

[could do is recognize that some of our](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m30s)
01:10:30

[in our first tree some of our columns](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m35s)
01:10:35

[sorry some of our rows didn't get used](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m38s)
01:10:38

[so what we could do would be to pass](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m42s)
01:10:42

[those rows through the first tree and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m46s)
01:10:46

[treat it as a validation set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m49s)
01:10:49

[and then for the second tree we could](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m53s)
01:10:53

[pass through the rows that weren't used](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m55s)
01:10:55

[for the second tree through it to create](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m57s)
01:10:57

[a validation set for that and so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h10m59s)
01:10:59

[effectively we would have a different](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m01s)
01:11:01

[validation set for each tree and so now](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m03s)
01:11:03

[to calculate our prediction we would](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m07s)
01:11:07

[average all of the trees where that row](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m10s)
01:11:10

[is not used for training right so for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m14s)
01:11:14

[tree number one we would have the ones](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m18s)
01:11:18

[I've marked in blue here and then maybe](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m21s)
01:11:21

[for tree number two it turned out it was](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m23s)
01:11:23

[like this one this one this one and this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m26s)
01:11:26

[one and so forth right so as long as](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m29s)
01:11:29

[you've got enough trees every rows going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m31s)
01:11:31

[to appear in the out of bag sample from](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m34s)
01:11:34

[one of them at least so you'll be](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m37s)
01:11:37

[averaging you know hopefully a few trees](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m39s)
01:11:39

[so if you've got a hundred trees it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m43s)
01:11:43

[very likely that all of the rows are](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m46s)
01:11:46

[going to appear many times in these](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m50s)
01:11:50

[other bag samples so what you can do is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m51s)
01:11:51

[you can create an out of bag prediction](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m53s)
01:11:53

[by averaging all of the trees you didn't](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m55s)
01:11:55

[use to train each individual row and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h11m58s)
01:11:58

[then you can calculate your root mean](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m00s)
01:12:00

[square error R squared etc on that if](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m02s)
01:12:02

[you pass low B score equals true to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m06s)
01:12:06

[scikit-learn it will do that for you and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m10s)
01:12:10

[it will create an attribute called oob](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m13s)
01:12:13

[score underscore and so my little print](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m21s)
01:12:21

[score function here if that attribute](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m23s)
01:12:23

[exists it it adds it to the print so if](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m25s)
01:12:25

[you take a look here hoby square equals](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m29s)
01:12:29

[true we've now got one extra number and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m32s)
01:12:32

[it's R squared that is the R squared for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m36s)
01:12:36

[the oeob sample it's a square it is very](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m40s)
01:12:40

[similar the R squared and the validation](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m43s)
01:12:43

[set which is what we hoped for can we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m45s)
01:12:45

[plus it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m48s)
01:12:48

[is it the case that the prediction for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m51s)
01:12:51

[the obese core has to be must be](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m55s)
01:12:55

[mathematically lower than the one for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m57s)
01:12:57

[our entire forest um certainly it's not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h12m59s)
01:12:59

[true that the prediction is lower it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m02s)
01:13:02

[possible for accuracy yeah um it's not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m04s)
01:13:04

[mathematically necessary that it's true](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m09s)
01:13:09

[but it's gonna be true on average](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m11s)
01:13:11

[because your average for each row](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m13s)
01:13:13

[appears in less trees in the oeob](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m15s)
01:13:15

[samples and it does in the full set of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m18s)
01:13:18

[trees so as you see here it's a little](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m20s)
01:13:20

[less good so I'm in general it's a great](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m24s)
01:13:24

[insight Chris in general the OOBE](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m27s)
01:13:27

[r-squared will slightly underestimate](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m29s)
01:13:29

[how generalizable the model is the more](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m33s)
01:13:33

[trees you add the less serious that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m35s)
01:13:35

[underestimation is and for me in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m38s)
01:13:38

[practice I I find it's totally good](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m40s)
01:13:40

[enough you know in practice okay so this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m43s)
01:13:43

[our B score is is is super handy and one](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m51s)
01:13:51

[of the things that super handy for is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m55s)
01:13:55

[you're gonna see there's quite a few](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m57s)
01:13:57

[hyper parameters that were going to set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h13m59s)
01:13:59

[and we would like to find some automated](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m01s)
01:14:01

[way to set them and one way to do that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m04s)
01:14:04

[is to do what's called a grid search a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m08s)
01:14:08

[grid search is where if there's a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m10s)
01:14:10

[scikit-learn function called grid search](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m11s)
01:14:11

[and you pass in the list of all of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m14s)
01:14:14

[parameters all of the hyper parameters](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m17s)
01:14:17

[that you want to tune you pass in for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m18s)
01:14:18

[each one a list of all of the values of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m20s)
01:14:20

[that hyper parameter you want to try and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m23s)
01:14:23

[it runs your model on every possible](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m24s)
01:14:24

[combination of all of those hyper](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m27s)
01:14:27

[parameters and tells you which one is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m29s)
01:14:29

[the best and our B score is a great like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m32s)
01:14:32

[choice for to forgetting it to Tory](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m36s)
01:14:36

[which one is best in terms of our V](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m39s)
01:14:39

[score like that's an example of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m41s)
01:14:41

[something you can do with a which works](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m42s)
01:14:42

[well](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m44s)
01:14:44

[now](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m45s)
01:14:45

[if you think about it I kind of did](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m52s)
01:14:52

[something pretty dumb earlier which is I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m55s)
01:14:55

[took a subset of 30,000 rows of the data](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h14m58s)
01:14:58

[and it built all my models of that which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m01s)
01:15:01

[means every tree in my random forest is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m04s)
01:15:04

[a different subset of that subset of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m08s)
01:15:08

[30,000 why do that why not take a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m11s)
01:15:11

[different I like a totally different](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m16s)
01:15:16

[subset of 30,000 each time so in other](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m18s)
01:15:18

[words let's leave the entire 300](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m22s)
01:15:22

[thousand records as is right and if I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m24s)
01:15:24

[want to make things faster right pick a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m27s)
01:15:27

[different subset of 30,000 each time so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m29s)
01:15:29

[rather than bootstrapping the entire set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m31s)
01:15:31

[of rows that's just randomly sample a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m33s)
01:15:33

[subset of the data and so we can do that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m36s)
01:15:36

[so let's go back and recall property yet](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m40s)
01:15:40

[without the subset parameter to get all](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m44s)
01:15:44

[of our data again and so to remind you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m46s)
01:15:46

[that is okay 400,000 I in the whole data](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m48s)
01:15:48

[frame of which we have three 89,000 in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h15m56s)
01:15:56

[our training set and instead we're going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m01s)
01:16:01

[to go set our F samples 20,000 remember](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m05s)
01:16:05

[that was the site that off the 30,000 we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m09s)
01:16:09

[use 20,000 of them in our training set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m11s)
01:16:11

[if I do this there now when I run a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m12s)
01:16:12

[random forest it's not going to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m16s)
01:16:16

[bootstrap an entire set of 391 thousand](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m18s)
01:16:18

[rows it's going to just grab a subset of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m22s)
01:16:22

[20,000 rows all right and so now if I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m24s)
01:16:24

[run this it will still run just as](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m29s)
01:16:29

[quickly as if I had like originally done](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m32s)
01:16:32

[a random sample of 20,000 but now every](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m35s)
01:16:35

[tree can have access to the whole data](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m38s)
01:16:38

[set right so if I do enough estimators](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m41s)
01:16:41

[enough trees eventually it's going to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m44s)
01:16:44

[see everything right so in this case](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m46s)
01:16:46

[with 10 trees which is the default I get](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m50s)
01:16:50

[an R squared of 0.8 6 which is actually](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m54s)
01:16:54

[about the same as my R squared with the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h16m57s)
01:16:57

[with the 20,000 subsets](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m00s)
01:17:00

[and that's because I haven't used many](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m03s)
01:17:03

[estimators yet right but if I increase](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m04s)
01:17:04

[the number of estimators it's got to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m06s)
01:17:06

[make more of a difference right so if I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m09s)
01:17:09

[increase the number of estimators](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m11s)
01:17:11

[two-forty alright it's going to take a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m16s)
01:17:16

[little bit longer to run but it's going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m19s)
01:17:19

[to be able to see a larger subset of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m22s)
01:17:22

[data set and so as you can see the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m25s)
01:17:25

[r-squared is gone up from point eight](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m27s)
01:17:27

[six two point eight seven six okay so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m28s)
01:17:28

[this is actually a great approach and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m32s)
01:17:32

[for those of you who would doing the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m33s)
01:17:33

[groceries competition that's got](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m35s)
01:17:35

[something like 120 million roads but](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m37s)
01:17:37

[there's no way you would want to create](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m39s)
01:17:39

[a random forest using 128 million roads](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m41s)
01:17:41

[in every tree like it's going to take](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m45s)
01:17:45

[forever so what you could do is use this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m46s)
01:17:46

[set area of samples to do like I don't](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m50s)
01:17:50

[know a hundred thousand or a million](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m52s)
01:17:52

[I'll play around with it so the trick](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m54s)
01:17:54

[here is that with a random forest using](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m56s)
01:17:56

[this technique no data set is too big I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h17m58s)
01:17:58

[don't care if it's got a hundred billion](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m01s)
01:18:01

[rows right you can create a bunch of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m03s)
01:18:03

[trees each one of the different random](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m06s)
01:18:06

[subsets can somebody pass the actual](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m08s)
01:18:08

[accuracy](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m10s)
01:18:10

[so my question was for the albey scores](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m26s)
01:18:26

[and these ones does it take the only](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m29s)
01:18:29

[like for the ones from the sample or](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m33s)
01:18:33

[take from all the that's a great](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m37s)
01:18:37

[question](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m38s)
01:18:38

[so unfortunately scikit-learn does not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m40s)
01:18:40

[support this functionality out of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m45s)
01:18:45

[box so I had to write this and it's kind](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m46s)
01:18:46

[of a horrible hack right because we're](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m50s)
01:18:50

[much rather be passing in like a sample](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m52s)
01:18:52

[size parameter rather than doing this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m55s)
01:18:55

[kind of setting up here so what I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m57s)
01:18:57

[actually do is if you look at the source](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h18m58s)
01:18:58

[code is I'm actually this is a internal](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m03s)
01:19:03

[this is the internal function I looked](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m05s)
01:19:05

[at their source code that they call and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m06s)
01:19:06

[I've replaced it with a with a lambda](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m08s)
01:19:08

[function that has the behavior we want](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m10s)
01:19:10

[unfortunately the current version is not](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m13s)
01:19:13

[changing how our B is calculated so yeah](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m16s)
01:19:16

[so currently low B scores and set our F](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m21s)
01:19:21

[samples are not compatible with each](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m25s)
01:19:25

[other so you need to turn our B equals](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m28s)
01:19:28

[false if you use this approach which I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m30s)
01:19:30

[hope to fix but at this stage it's it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m35s)
01:19:35

[not fixed so if you want to turn it off](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m38s)
01:19:38

[you just call reset our F samples okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m40s)
01:19:40

[and that returns it back to what it was](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m45s)
01:19:45

[okay so in practice when I'm like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m51s)
01:19:51

[doing interactive machine learning using](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h19m59s)
01:19:59

[random forests in order to like explore](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m02s)
01:20:02

[my model explore hyper parameters the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m04s)
01:20:04

[stuff we're going to learn in the future](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m06s)
01:20:06

[lesson where we actually analyze like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m07s)
01:20:07

[feature importance and partial](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m10s)
01:20:10

[dependence and so forth I generally use](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m11s)
01:20:11

[subsets and reasonably small forests](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m14s)
01:20:14

[because all the insights that I'm going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m19s)
01:20:19

[to get are exactly the same as the big](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m21s)
01:20:21

[ones but I can run it in like you know](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m23s)
01:20:23

[three or four seconds rather than hours](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m25s)
01:20:25

[alright so this is one of the biggest](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m28s)
01:20:28

[tips I can give you and very very few](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m31s)
01:20:31

[people in industry or academia actually](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m34s)
01:20:34

[do this most people run all of their](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m37s)
01:20:37

[models on all of the data all of the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m40s)
01:20:40

[time using their best possible](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m42s)
01:20:42

[parameters which is just pointless right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m43s)
01:20:43

[if you're trying to find out like which](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m46s)
01:20:46

[features are important and how are they](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m47s)
01:20:47

[related to each other and so forth](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m49s)
01:20:49

[having that fourth decimal place of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m51s)
01:20:51

[accuracy isn't going to change any of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m53s)
01:20:53

[your insights at all okay so I would say](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m55s)
01:20:55

[like do most of your models on you know](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m57s)
01:20:57

[a large enough sample size that your](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h20m59s)
01:20:59

[accuracy is you know reasonable when I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m02s)
01:21:02

[say reasonable it's like within a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m06s)
01:21:06

[reasonable distance of the best accuracy](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m08s)
01:21:08

[you can get and it's taking you know a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m10s)
01:21:10

[small number of seconds to train so that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m13s)
01:21:13

[you can interactively do your analysis](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m15s)
01:21:15

[so there's a couple more parameters I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m18s)
01:21:18

[wanted to talk about so I'm going to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m21s)
01:21:21

[call reset RF samples to get back to our](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m22s)
01:21:22

[full data set because in this case at](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m24s)
01:21:24

[least on this computer it's actually](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m27s)
01:21:27

[running in less than 10 seconds so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m28s)
01:21:28

[here's our baseline we're going to do a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m32s)
01:21:32

[baseline with 40 estimators okay and so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m36s)
01:21:36

[each of those 40 estimators is going to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m40s)
01:21:40

[Train all the way down to all the leaf](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m42s)
01:21:42

[nodes just have one sample in them](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m44s)
01:21:44

[so that's going to take a few seconds to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m51s)
01:21:51

[run here we go so that gets us a point](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m54s)
01:21:54

[eight nine eight a sweat on the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h21m56s)
01:21:56

[validation set or 0.90 eight on the oeob](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m00s)
01:22:00

[now this case the OB is better why is it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m04s)
01:22:04

[better](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m07s)
01:22:07

[well that's because remember our](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m07s)
01:22:07

[validation set is not a random sample](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m08s)
01:22:08

[our validation set is a different time](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m10s)
01:22:10

[period okay so it's actually much harder](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m13s)
01:22:13

[to predict a different time period than](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m15s)
01:22:15

[this one which is just predicting random](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m19s)
01:22:19

[okay so that's why this is not the way](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m21s)
01:22:21

[around we expected so the next the first](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m23s)
01:22:23

[parameter we can try fiddling with is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m27s)
01:22:27

[min samples leaf and so min samples leaf](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m29s)
01:22:29

[says stop training the tree further when](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m32s)
01:22:32

[your leaf node has three or less samples](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m36s)
01:22:36

[in there are going all the way down](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m42s)
01:22:42

[until there's one we're going to go down](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m44s)
01:22:44

[until there's three so in practice this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m46s)
01:22:46

[means there's going to be like one or](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m50s)
01:22:50

[two less levels of decision being made](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m51s)
01:22:51

[which means we've got like half the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m54s)
01:22:54

[number of actual decision criteria we](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m57s)
01:22:57

[have to do is it's going to train more](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h22m59s)
01:22:59

[quickly it means that when we look at an](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m01s)
01:23:01

[individual tree rather than just taking](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m03s)
01:23:03

[one point we're taking the average of at](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m05s)
01:23:05

[least three points](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m08s)
01:23:08

[that's who would expect the trees to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m08s)
01:23:08

[generalize each one to generalize a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m10s)
01:23:10

[little bit better okay but each tree is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m12s)
01:23:12

[probably going to be slightly less](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m15s)
01:23:15

[powerful on its own so let's try](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m17s)
01:23:17

[training that so possible values of min](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m20s)
01:23:20

[samples leaf I find ones which work well](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m23s)
01:23:23

[are kind of 1 3 5 10 25 you know like I](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m26s)
01:23:26

[find that kind of range seems to work](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m32s)
01:23:32

[well but like sometimes if you've got a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m35s)
01:23:35

[really big data set and you're not using](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m38s)
01:23:38

[the small samples you know you might](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m40s)
01:23:40

[need a mint samples leaf of hundreds or](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m43s)
01:23:43

[thousands so it's you kind of got to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m46s)
01:23:46

[think about like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m48s)
01:23:48

[how bigger your sub-samples going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m50s)
01:23:50

[through and try things out now in this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m51s)
01:23:51

[case going from the default of one to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m53s)
01:23:53

[three has increased our validation set](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m56s)
01:23:56

[our squared from 898 to 902 so it's a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h23m59s)
01:23:59

[slight improvement okay and it's going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m02s)
01:24:02

[to train a little faster as well as](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m04s)
01:24:04

[something else you can try which is and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m07s)
01:24:07

[since this worked I'm going to leave](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m09s)
01:24:09

[that in I'm going to add in max features](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m10s)
01:24:10

[equals point five](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m13s)
01:24:13

[why does max features do well the idea](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m14s)
01:24:14

[is that the less correlated your trees](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m18s)
01:24:18

[are with each other the better now](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m21s)
01:24:21

[imagine you had one column that was so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m24s)
01:24:24

[much better than all of the other](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m30s)
01:24:30

[columns of being predictive that every](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m31s)
01:24:31

[single tree you built regardless of like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m33s)
01:24:33

[which subset of rows always started with](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m35s)
01:24:35

[that column so the trees are all going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m37s)
01:24:37

[to be pretty similar right but you can](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m39s)
01:24:39

[imagine there might be some interaction](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m42s)
01:24:42

[of variables where that interaction is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m45s)
01:24:45

[more important than that individual](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m47s)
01:24:47

[column so if every tree always fits on](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m50s)
01:24:50

[the first thing the same thing the first](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m54s)
01:24:54

[time you're not going to get much](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m56s)
01:24:56

[variation in those trees so what we do](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h24m58s)
01:24:58

[is in addition to just taking a subset](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m01s)
01:25:01

[of rows we then at every single split](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m05s)
01:25:05

[point take a different subset of columns](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m09s)
01:25:09

[so it's slightly different to the row](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m13s)
01:25:13

[sampling for the row sampling H nu tree](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m15s)
01:25:15

[is based on a random set of rows or](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m19s)
01:25:19

[columns sampling every individual binary](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m21s)
01:25:21

[split we choose from a different subset](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m25s)
01:25:25

[of columns so in other words rather than](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m28s)
01:25:28

[looking at every possible level of every](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m32s)
01:25:32

[possible column we look at every](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m35s)
01:25:35

[possible level of a random subset of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m38s)
01:25:38

[columns okay](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m40s)
01:25:40

[and each time each decision point each](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m42s)
01:25:42

[binary split we use a different random](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m46s)
01:25:46

[subset how many well you get to pick 0.5](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m48s)
01:25:48

[means randomly choose half of them](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m53s)
01:25:53

[the default is to use all of them](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h25m56s)
01:25:56

[there's also a couple of special values](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m00s)
01:26:00

[you can use here as you can see in max](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m02s)
01:26:02

[features you can also pass in square](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m07s)
01:26:07

[root to get square root of features or](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m10s)
01:26:10

[log two to get log two in features so in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m12s)
01:26:12

[practice good values I found our range](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m15s)
01:26:15

[from 1.5 log to or square root that's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m19s)
01:26:19

[going to give you a nice bit of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m24s)
01:26:24

[variation right can somebody positive](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m26s)
01:26:26

[Danielle and so just to clarify does](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m28s)
01:26:28

[that just like break it up smaller each](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m33s)
01:26:33

[time it goes through the tree or is it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m36s)
01:26:36

[just taking half of what's left over or](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m38s)
01:26:38

[like hasn't been touched each time](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m40s)
01:26:40

[there's no such thing as what's left](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m41s)
01:26:41

[over after you've split on year made](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m43s)
01:26:43

[less than or greater than 1984 you made](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m46s)
01:26:46

[still there right so later on you might](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m49s)
01:26:49

[then spit on your maid left Center](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m52s)
01:26:52

[greater than 1989 so so it's just each](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m53s)
01:26:53

[time rather than checking every variable](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m57s)
01:26:57

[to see where it's best fit is you just](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h26m59s)
01:26:59

[check half of them and so the next time](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m01s)
01:27:01

[you check a different hops the next time](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m04s)
01:27:04

[you took a different path but I mean](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m05s)
01:27:05

[like terms is as you got like further to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m07s)
01:27:07

[like the leaf you're gonna have less](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m10s)
01:27:10

[options no you're not you'd never remove](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m14s)
01:27:14

[the variables okay you can use them](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m17s)
01:27:17

[again and again and again because you've](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m19s)
01:27:19

[got lots of different spit points](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m20s)
01:27:20

[so imagine for example that the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m23s)
01:27:23

[relationship was just entirely linear](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m25s)
01:27:25

[between year made and price right then](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m27s)
01:27:27

[in practice to actually model that you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m31s)
01:27:31

[know your real relationship is year made](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m33s)
01:27:33

[versus price right but the best we could](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m36s)
01:27:36

[do would be this kind of first of all](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m41s)
01:27:41

[split here right and then just split](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m42s)
01:27:42

[here and here right and like spitting](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m46s)
01:27:46

[spitting split so yeah even if the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m49s)
01:27:49

[binary most random forest libraries](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m53s)
01:27:53

[don't do anything special about that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m56s)
01:27:56

[they just kind of go okay we'll try this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m58s)
01:27:58

[variable oh it turns out there's only](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h27m59s)
01:27:59

[one level left you know so yeah that](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m01s)
01:28:01

[didn't they don't do any kind of clever](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m04s)
01:28:04

[bookkeeping okay okay so if we add next](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m06s)
01:28:06

[features equals 0.5 it goes up from 901](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m13s)
01:28:13

[the 906 so that's better still and so as](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m16s)
01:28:16

[we've been doing this we've also](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m20s)
01:28:20

[hopefully have noticed that our root](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m21s)
01:28:21

[mean squared error log price has been](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m23s)
01:28:23

[dropping on a validation set as well and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m25s)
01:28:25

[so it's now down to 0.2 to 86 so how](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m28s)
01:28:28

[good is that right so like our totally](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m33s)
01:28:33

[untrue and random florists got us in](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m36s)
01:28:36

[about the top 25 percent now remember](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m38s)
01:28:38

[our validation set isn't identical to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m40s)
01:28:40

[the Kaggle test set right and this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m44s)
01:28:44

[competition unfortunately is old enough](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m46s)
01:28:46

[that you can't even put in a kind of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m48s)
01:28:48

[after this after the time entry to find](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m51s)
01:28:51

[out how you would have gone so we can](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m54s)
01:28:54

[only approximate how we could have gone](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m55s)
01:28:55

[but you know generally speaking is going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m57s)
01:28:57

[to be a pretty good approximation so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h28m59s)
01:28:59

[2:286](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m01s)
01:29:01

[here is the competition here's the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m04s)
01:29:04

[public leaderboard](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m06s)
01:29:06

[two two eight six here we go](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m10s)
01:29:10

[14th or 15th place so you know roughly](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m14s)
01:29:14

[speaking](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m18s)
01:29:18

[looks like we would be about in the top](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m19s)
01:29:19

[20 of this competition with basically](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m20s)
01:29:20

[totally brainless random forest with](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m24s)
01:29:24

[some totally brainless minor hyper](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m26s)
01:29:26

[parameter tuning and so this is kind of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m28s)
01:29:28

[why the random forest is such an](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m34s)
01:29:34

[important not just first step but often](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m35s)
01:29:35

[only step from the Xin learning because](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m39s)
01:29:39

[it's kind of hard to screw it up like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m41s)
01:29:41

[even when we didn't tune the hyper](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m43s)
01:29:43

[parameters we still got a good result](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m45s)
01:29:45

[and then a small amount of type of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m46s)
01:29:46

[parameter tuning got us a much better](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m48s)
01:29:48

[result and so any kind of model so and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m50s)
01:29:50

[I'm particularly thinking of like linear](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m54s)
01:29:54

[type models which have a whole bunch of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m56s)
01:29:56

[statistical assumptions and you have to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h29m59s)
01:29:59

[get a whole bunch of things right before](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m00s)
01:30:00

[they start to work at all can really](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m02s)
01:30:02

[throw you off track right because they](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m05s)
01:30:05

[give you like totally wrong answers](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m07s)
01:30:07

[about how accurate the predictions can](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m09s)
01:30:09

[be but also the random forest you know](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m11s)
01:30:11

[generally speaking they tend to work on](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m14s)
01:30:14

[most data sets most of the time with](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m17s)
01:30:17

[most sets of hyper parameters so for](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m19s)
01:30:19

[example we did this thing with it with](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m21s)
01:30:21

[our categorical variables in fact let's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m30s)
01:30:30

[take a look at our tree a single tree](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m32s)
01:30:32

[look at this right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m39s)
01:30:39

[fi product class desc less than 7.5 what](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m41s)
01:30:41

[does that mean so f I product plus desc](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m46s)
01:30:46

[here's some examples of that column all](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h30m58s)
01:30:58

[right so what does it mean to be less](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m02s)
01:31:02

[than or equal to 7](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m03s)
01:31:03

[well we'd have to look at dark cat dark](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m05s)
01:31:05

[categories to find out okay and so it's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m08s)
01:31:08

[0 1 2 3 4 5 6 7 so what it's done is its](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m12s)
01:31:12

[created a split where all of the backhoe](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m18s)
01:31:18

[loaders and these three types of](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m20s)
01:31:20

[hydraulics](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m23s)
01:31:23

[enter in one group and everything else](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m24s)
01:31:24

[is in the other group so like that's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m26s)
01:31:26

[like weird you know like like these](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m29s)
01:31:29

[aren't even in order we could have made](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m32s)
01:31:32

[them in order if we had you know bother](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m35s)
01:31:35

[to say the categories have this order](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m37s)
01:31:37

[but we hadn't right so how come this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m39s)
01:31:39

[even works like because when we turn it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m43s)
01:31:43

[into codes it's actually this is](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m46s)
01:31:46

[actually what the random forest sees and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h31m56s)
01:31:56

[so imagine to think about this imagine](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m00s)
01:32:00

[like the only thing that mattered was](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m04s)
01:32:04

[whether as a hydraulic excavator at zero](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m06s)
01:32:06

[to two metric tons and nothing else](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m08s)
01:32:08

[mattered imagine that right so it has to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m10s)
01:32:10

[pick out this this single level well it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m12s)
01:32:12

[can do that because first of all it](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m16s)
01:32:16

[could say okay let's pick out everything](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m18s)
01:32:18

[less than seven versus greater than](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m20s)
01:32:20

[seven to create you know this is one](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m22s)
01:32:22

[group and this is another group right](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m25s)
01:32:25

[and then within this group they could](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m27s)
01:32:27

[then pick out everything less than six](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m30s)
01:32:30

[versus greater than six we're just going](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m32s)
01:32:32

[to pick out this one item right so with](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m34s)
01:32:34

[two split points we can pull out a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m36s)
01:32:36

[single category so this is why it works](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m39s)
01:32:39

[right is because the tree is like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m42s)
01:32:42

[infinitely flexible even with a](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m45s)
01:32:45

[categorical variable if there's](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m47s)
01:32:47

[particular categories which have](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m49s)
01:32:49

[different levels of price it can like](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m51s)
01:32:51

[gradually zoom in on those groups by](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m54s)
01:32:54

[using multiple splits right now you can](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h32m57s)
01:32:57

[help it by telling it the order of your](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m00s)
01:33:00

[categorical variable but even if you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m02s)
01:33:02

[don't it's okay it's just going to take](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m04s)
01:33:04

[a few more decisions to get there and so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m07s)
01:33:07

[you can see here it's actually using](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m10s)
01:33:10

[this product class desk quite a few](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m12s)
01:33:12

[times right and and as you go deeper](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m14s)
01:33:14

[down the tree you'll see it used more](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m18s)
01:33:18

[and more right where else in a linear](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m21s)
01:33:21

[model or almost any kind of other model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m23s)
01:33:23

[certainly any any non tree model pretty](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m25s)
01:33:25

[much encoding a categorical variable](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m29s)
01:33:29

[like this won't work at all because](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m32s)
01:33:32

[there's no linear relationship to train](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m34s)
01:33:34

[totally arbitrary](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m36s)
01:33:36

[identifiers and anything right so so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m37s)
01:33:37

[these are the kinds of things that make](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m41s)
01:33:41

[Brennan forests very easy to use and and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m43s)
01:33:43

[very resilient and so by using that you](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m45s)
01:33:45

[know we've gotten ourselves a model](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m49s)
01:33:49

[which is clearly you know world class at](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m51s)
01:33:51

[this point already it's like you know](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m56s)
01:33:56

[probably will in the top 20 of this](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h33m58s)
01:33:58

[cackle competition and then in our next](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m00s)
01:34:00

[lesson we're going to learn about how to](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m02s)
01:34:02

[analyze that model to learn more about](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m07s)
01:34:07

[the data to make it even better right so](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m10s)
01:34:10

[this week try and like really experiment](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m13s)
01:34:13

[right have a look inside look try and](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m17s)
01:34:17

[draw the trees try and plot the](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m19s)
01:34:19

[different errors try maybe using](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m22s)
01:34:22

[different data sets to see how they work](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m24s)
01:34:24

[really experiment to try to get a sense](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m26s)
01:34:26

[and maybe try to like replicate things](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m29s)
01:34:29

[like write your own r-squared you know](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m32s)
01:34:32

[write your own versions or some of these](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m35s)
01:34:35

[functions see if ya see how much you can](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m36s)
01:34:36

[really learn about your data set about](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m39s)
01:34:39

[the random person great see you on](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m41s)
01:34:41

[Thursday](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m43s)
01:34:43

[[Music]](https://www.youtube.com/watch?v=blyXCk4sgEg#t=01h34m49s)
01:34:49

