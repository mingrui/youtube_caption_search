[okay so welcome back to deep learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m00s)
00:00:00

[lesson 2 last week we got to the point](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m03s)
00:00:03

[where we had successfully trained a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m10s)
00:00:10

[pretty accurate image classifier and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m12s)
00:00:12

[just to remind you about how we did that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m16s)
00:00:16

[can you guys see okay I think the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m21s)
00:00:21

[actually we can turn the phone once all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m24s)
00:00:24

[right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m25s)
00:00:25

[can you guys all see the screen okay we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m26s)
00:00:26

[can to adjust these ones can we some](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m30s)
00:00:30

[pictures all into darkness but if that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m35s)
00:00:35

[works then is that okay that's better](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m37s)
00:00:37

[isn't it yeah can I dream the other two](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m41s)
00:00:41

[and maybe that one as well](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m46s)
00:00:46

[oh but that one oh that's great sorry I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m47s)
00:00:47

[don't know your renders oh okay great](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m53s)
00:00:53

[that's better isn't it me so just to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h00m55s)
00:00:55

[remind you the way that we built this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m03s)
00:01:03

[image classifier was we used a small](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m05s)
00:01:05

[amount of code basically three lines of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m08s)
00:01:08

[code and these three lines of code](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m11s)
00:01:11

[pointed at a particular path which](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m14s)
00:01:14

[already had some data in it and so the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m17s)
00:01:17

[key thing for this to know how to train](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m19s)
00:01:19

[this model was that this path which was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m21s)
00:01:21

[data dogs cats and had to have a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m25s)
00:01:25

[particular structure which is that it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m27s)
00:01:27

[had a train folder and a valid folder](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m30s)
00:01:30

[and in each of those trained and valid](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m33s)
00:01:33

[folders there was a cats folder in the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m35s)
00:01:35

[dogs folder and if the cats on the docs](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m37s)
00:01:37

[folders was a bunch of images of cats](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m39s)
00:01:39

[and votes but this is like a pretty](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m42s)
00:01:42

[standard it's one of two main structures](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m44s)
00:01:44

[that are used to say here is the data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m48s)
00:01:48

[that I want you to train an image model](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m51s)
00:01:51

[from so I know some of you during the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m52s)
00:01:52

[week went away and tried different data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m55s)
00:01:55

[sets where you had folders with](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h01m58s)
00:01:58

[different sets of images and in credit](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m01s)
00:02:01

[your own image classifiers and generally](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m02s)
00:02:02

[that seems to be working pretty well](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m05s)
00:02:05

[from what I can see on the forums so to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m06s)
00:02:06

[make it clear at this point this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m08s)
00:02:08

[everything you need](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m11s)
00:02:11

[to get started so if you create your own](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m13s)
00:02:13

[folders with different sets of images](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m16s)
00:02:16

[you know a few hundred or a few thousand](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m18s)
00:02:18

[at each folder and run the same three](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m23s)
00:02:23

[lines of code that will give you an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m28s)
00:02:28

[image classifier and you'll be able to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m30s)
00:02:30

[see this third column tells you how](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m32s)
00:02:32

[accurate is so we looked at some kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m35s)
00:02:35

[simple visualizations to see like what](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m42s)
00:02:42

[was it uncertain about what was it wrong](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m46s)
00:02:46

[about and so forth and that's always a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m48s)
00:02:48

[really good idea and then we learned](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m50s)
00:02:50

[about the one key number you have to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m55s)
00:02:55

[pick so this is this number here is the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m57s)
00:02:57

[one key number is 0.01 and this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h02m59s)
00:02:59

[called the learning rate and so I wanted](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m02s)
00:03:02

[to go over this again and we'll learn](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m05s)
00:03:05

[about the theory behind what this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m07s)
00:03:07

[during the rest of the course in quite a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m10s)
00:03:10

[lot of detail and for now I just wanted](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m12s)
00:03:12

[to talk about the practice yes you know](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m14s)
00:03:14

[they cannot see you in the medium](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m23s)
00:03:23

[turnout I just turned it around you tell](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m25s)
00:03:25

[us about the other three numbers being](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m31s)
00:03:31

[bad we did these three here we're going](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m34s)
00:03:34

[to talk about the other other ones](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m38s)
00:03:38

[shortly so the main one we're going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m40s)
00:03:40

[look at for now is is the last column](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m41s)
00:03:41

[which is the accuracy the first column](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m43s)
00:03:43

[as you can see is the epoch number so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m48s)
00:03:48

[this tells us how many times has it been](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m50s)
00:03:50

[through the entire dataset trying to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m52s)
00:03:52

[learn a better classifier and in the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m55s)
00:03:55

[next two columns is what's called the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m57s)
00:03:57

[loss which we'll be learning about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h03m58s)
00:03:58

[either later today or next week the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m00s)
00:04:00

[first point is the loss on the training](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m03s)
00:04:03

[set these are the images that we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m05s)
00:04:05

[looking at in order to try to make a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m07s)
00:04:07

[better classifier and the second is the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m08s)
00:04:08

[loss of the validation set these are the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m10s)
00:04:10

[images that we're not looking at and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m12s)
00:04:12

[we're training but we're just sitting on](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m14s)
00:04:14

[the side to see how accurate we are so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m15s)
00:04:15

[we'll learn about littering loss in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m17s)
00:04:17

[accuracy later](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m19s)
00:04:19

[okay so so we've got the epoch number](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m24s)
00:04:24

[the training loss is the second column](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m30s)
00:04:30

[the validation loss is the third column](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m33s)
00:04:33

[and the accuracy is the fourth column](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m36s)
00:04:36

[you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m40s)
00:04:40

[okay so the basic idea of the loading](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m44s)
00:04:44

[rate so the basic idea of the learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m48s)
00:04:48

[rate is it's the thing that's going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m56s)
00:04:56

[decide how quickly do we zoom do we kind](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h04m58s)
00:04:58

[of hone in on the solution and so I find](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m01s)
00:05:01

[that a good way to think about this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m05s)
00:05:05

[to think about like well what if we were](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m06s)
00:05:06

[trying to fit to a function that looks](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m08s)
00:05:08

[something like this right we're trying](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m13s)
00:05:13

[to say okay where's where abouts is the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m15s)
00:05:15

[minimum point this is basically what we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m17s)
00:05:17

[do when we do deep learning is we try to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m20s)
00:05:20

[find the minimum point of a function now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m23s)
00:05:23

[our function happens to have millions or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m26s)
00:05:26

[hundreds of millions of parameters but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m29s)
00:05:29

[it works the same basic way and so when](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m30s)
00:05:30

[we look at it you know we can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m32s)
00:05:32

[immediately see that the lowest point is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m33s)
00:05:33

[here but how would you do that if you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m36s)
00:05:36

[are a computer algorithm and what we do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m40s)
00:05:40

[is we we start out at some point at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m42s)
00:05:42

[random so you pick say here and we have](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m45s)
00:05:45

[a look and we say okay what's the what's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m47s)
00:05:47

[the loss or the error at this point and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m50s)
00:05:50

[we say what's the gradient in other](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m52s)
00:05:52

[words which way is up and which way is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m53s)
00:05:53

[down and it tells us that down is going](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m55s)
00:05:55

[to be in that direction and it also](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h05m58s)
00:05:58

[tells us how fast is it going down which](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m00s)
00:06:00

[is at this point is going down pretty](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m03s)
00:06:03

[quickly and so then we take a step in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m05s)
00:06:05

[the direction that's down and the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m09s)
00:06:09

[distance we travel is going to be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m11s)
00:06:11

[proportional to the gradient sort of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m13s)
00:06:13

[unfortunately how steep it is the idea](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m15s)
00:06:15

[is if it's deeper then we're probably](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m17s)
00:06:17

[further away that's the general idea](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m20s)
00:06:20

[right and so specifically what we do is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m22s)
00:06:22

[we take the gradient which is how steep](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m25s)
00:06:25

[is it at this point and we multiply it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m26s)
00:06:26

[by some number and that number is called](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m28s)
00:06:28

[the learning rate okay](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m30s)
00:06:30

[so if we pick a number that is very](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m31s)
00:06:31

[small then we're guaranteed that we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m35s)
00:06:35

[going to go a little bit closer and a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m38s)
00:06:38

[little bit closer and a little bit](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m39s)
00:06:39

[closer each time right but it's going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m40s)
00:06:40

[take us a very long time to eventually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m43s)
00:06:43

[get to the bottom if we dig a number](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m45s)
00:06:45

[that's very big we could actually step](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m48s)
00:06:48

[too far could go in the right direction](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m51s)
00:06:51

[but we could step all the way over to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m53s)
00:06:53

[here right as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m54s)
00:06:54

[result of which we end up further away](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m57s)
00:06:57

[than we started and we could oscillate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h06m59s)
00:06:59

[and get worse and worse so if you start](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m01s)
00:07:01

[training a neural net and you find that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m04s)
00:07:04

[your accuracy or your loss is like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m06s)
00:07:06

[spitting off into infinity](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m08s)
00:07:08

[almost certainly your learning rates too](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m10s)
00:07:10

[high so in a sense learning rate too low](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m12s)
00:07:12

[is is a better problem to have because](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m17s)
00:07:17

[you're going to have to wait a long time](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m20s)
00:07:20

[but wouldn't it be nice if there was a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m21s)
00:07:21

[way to figure out like what's the best](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m23s)
00:07:23

[learning rate something where you could](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m25s)
00:07:25

[kind of go quickly go like Bom Bom Bom](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m27s)
00:07:27

[right and so that's why we use this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m30s)
00:07:30

[thing called a learning rate finder and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m34s)
00:07:34

[what the learning rate finder does is it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m36s)
00:07:36

[tries each each time it looks at another](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m39s)
00:07:39

[remember the mini-batch how many batches](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m41s)
00:07:41

[a few images that we look at each time](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m44s)
00:07:44

[so that we're using the parallel](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m46s)
00:07:46

[processing power of the GPU effectively](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m48s)
00:07:48

[we look generally at around 64 128](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m50s)
00:07:50

[images at a time for each mini batch](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m53s)
00:07:53

[which is labeled here as an iteration we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m56s)
00:07:56

[gradually increase the learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h07m59s)
00:07:59

[multiplicatively increase the learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m01s)
00:08:01

[rate we started really really tiny](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m02s)
00:08:02

[learning rates to make sure that we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m04s)
00:08:04

[don't start at something too high and we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m06s)
00:08:06

[gradually increase it and so the idea is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m09s)
00:08:09

[that eventually the learning rate will](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m11s)
00:08:11

[be so big that the loss will start](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m14s)
00:08:14

[getting worse](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m16s)
00:08:16

[and so what we're going to do then is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m17s)
00:08:17

[we're a look at the plot of learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m19s)
00:08:19

[rate against loss right so when the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m22s)
00:08:22

[learning rates tiny it increases slowly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m25s)
00:08:25

[then it's that's where increase a bit](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m28s)
00:08:28

[faster and then eventually it starts not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m29s)
00:08:29

[increasing as quickly and in fact it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m33s)
00:08:33

[starts getting worse right so clearly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m34s)
00:08:34

[here and make sure you're you want to be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m36s)
00:08:36

[familiar with this scientific notation](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m38s)
00:08:38

[okay so ten to the negative one is 0.1](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m42s)
00:08:42

[10 to 50 or is 1 10 to the negative 2 is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m45s)
00:08:45

[0.001 and when we write this in Python](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m48s)
00:08:48

[we'll generally write it like this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m52s)
00:08:52

[rather than writing 10 to the negative 1](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m53s)
00:08:53

[or 10 to the negative 2 we'll just write](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m56s)
00:08:56

[1 a neg 1 or 1 e neg - okay I mean the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h08m59s)
00:08:59

[same thing you're going to see that all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m05s)
00:09:05

[the time and remember that equals 0.1](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m06s)
00:09:06

[Oh point O one okay so don't be confused](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m10s)
00:09:10

[by this text that it prints out here](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m19s)
00:09:19

[this this loss here is the the final](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m21s)
00:09:21

[loss at the very at the end of it's not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m25s)
00:09:25

[of any interest right so ignore this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m27s)
00:09:27

[this is only interesting when we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m29s)
00:09:29

[doing regular trading that's not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m31s)
00:09:31

[interesting for the learning rate finder](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m32s)
00:09:32

[the thing that's interesting for the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m34s)
00:09:34

[learning rate finder is this loan shed](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m35s)
00:09:35

[plot and specifically we're not looking](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m38s)
00:09:38

[for the point where it's the lowest back](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m41s)
00:09:41

[to the point where it's the lowest it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m43s)
00:09:43

[actually not getting better anymore so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m44s)
00:09:44

[that's to higher learning rate so I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m46s)
00:09:46

[generally look to see like where is it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m47s)
00:09:47

[the lowest and then I go back like one](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m49s)
00:09:49

[for magnitude so one enoch two would be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m51s)
00:09:51

[a pretty good choice yeah okay so that's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m56s)
00:09:56

[why you saw when we ran our fit here we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h09m59s)
00:09:59

[picked 0.01 right which is one a neg two](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m05s)
00:10:05

[so important point to make here is like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m09s)
00:10:09

[this this is the one key number that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m12s)
00:10:12

[we've learnt to adjust and if you just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m15s)
00:10:15

[adjust this number at nothing else most](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m21s)
00:10:21

[of the time you're going to be able to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m22s)
00:10:22

[get pretty good results and this is like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m24s)
00:10:24

[a very different message to what you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m26s)
00:10:26

[would hear or see in any textbook or any](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m28s)
00:10:28

[video or any course because up until now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m31s)
00:10:31

[there's been like dozens and dozens of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m35s)
00:10:35

[these they're called hyper parameters](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m38s)
00:10:38

[dozens and dozens of hyper parameters to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m39s)
00:10:39

[set and they've been thought of as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m41s)
00:10:41

[highly sensitive and difficult to set so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m43s)
00:10:43

[inside the first AI library we kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m45s)
00:10:45

[do all that stuff for you as much as we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m48s)
00:10:48

[can and during the course we're going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m51s)
00:10:51

[learn that there are some more we can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m53s)
00:10:53

[quake to get slightly better results but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m55s)
00:10:55

[it's kind of like it's kind of in a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h10m58s)
00:10:58

[funny situation here because for those](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m01s)
00:11:01

[of you that haven't done anything](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m03s)
00:11:03

[learning before is kind of like oh this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m04s)
00:11:04

[is that's all there is to it this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m06s)
00:11:06

[very easy and then when you talk to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m09s)
00:11:09

[people outside this class they'll be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m10s)
00:11:10

[like deep learning so difficult as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m12s)
00:11:12

[someone to say it's a real art form and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m14s)
00:11:14

[so that's why there's this as is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m16s)
00:11:16

[difference right and so that the truth](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m18s)
00:11:18

[is that the learning rate really is the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m19s)
00:11:19

[key thing to set and this ability to use](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m21s)
00:11:21

[this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m24s)
00:11:24

[to figure out how to set it well though](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m24s)
00:11:24

[the paper is now probably 18 months old](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m26s)
00:11:26

[almost nobody knows about this paper it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m29s)
00:11:29

[was from a guy who's not from a famous](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m33s)
00:11:33

[research labs so most people kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m35s)
00:11:35

[ignored it and in fact even this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m36s)
00:11:36

[particular technique was one subpart of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m38s)
00:11:38

[a paper that was about something else](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m40s)
00:11:40

[so again this idea of like this is how](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m42s)
00:11:42

[you can set the learning rate really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m45s)
00:11:45

[nobody outside this classroom just about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m47s)
00:11:47

[knows about it obviously the guy who](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m49s)
00:11:49

[wrote it Leslie Smith knows about it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m51s)
00:11:51

[yeah so it's a good thing to tell your](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m53s)
00:11:53

[colleagues about is like here is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m56s)
00:11:56

[actually a great way to set the learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h11m58s)
00:11:58

[rate and there's even been papers caught](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m00s)
00:12:00

[like one of the famous papers is called](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m03s)
00:12:03

[no more pesky learning rates which](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m04s)
00:12:04

[actually is a less effective technique](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m07s)
00:12:07

[than this one but this idea that like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m09s)
00:12:09

[setting learning rates is is very](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m11s)
00:12:11

[difficult and thirdly is has been true](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m13s)
00:12:13

[for most of the kind of deep learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m15s)
00:12:15

[history so here's the trick right go](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m17s)
00:12:17

[look at this plot find kind of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m20s)
00:12:20

[lowest to go back about a multiple of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m23s)
00:12:23

[ten and try that all right and if that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m24s)
00:12:24

[doesn't quite work you can always try](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m28s)
00:12:28

[you know going back another multiple ten](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m29s)
00:12:29

[but this is always worked for me so far](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m31s)
00:12:31

[once why does this learning rate this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m40s)
00:12:40

[method work versus something else like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m43s)
00:12:43

[momentum base or what's like the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m45s)
00:12:45

[advantages a disadvantage with just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m47s)
00:12:47

[learning rate rate like technique we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m50s)
00:12:50

[just feels that's a great question so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h12m52s)
00:12:52

[we're going to learn during this course](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m00s)
00:13:00

[about a number of ways of improving](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m02s)
00:13:02

[gradient percent like you mentioned](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m03s)
00:13:03

[momentum and atom and so forth this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m05s)
00:13:05

[orthogonal in fact so one of the things](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m08s)
00:13:08

[the faster a library tries to do is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m10s)
00:13:10

[figure out the right gradient descent](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m13s)
00:13:13

[version and in fact behind the scenes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m15s)
00:13:15

[this is actually using something called](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m17s)
00:13:17

[atom and so this technique is telling us](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m18s)
00:13:18

[this is the best learning rate to use](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m21s)
00:13:21

[given what I thought other tweaks you're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m23s)
00:13:23

[using in this case the atom optimizer so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m26s)
00:13:26

[it's not that there's some compromise](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m29s)
00:13:29

[between this and some other approaches](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m31s)
00:13:31

[who sits on top of those approaches and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m32s)
00:13:32

[you still have to set the learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m34s)
00:13:34

[when you use with other approaches so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m36s)
00:13:36

[we're trying to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m38s)
00:13:38

[find the best kind of optimizer to use](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m38s)
00:13:38

[for a problem that you still have to set](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m41s)
00:13:41

[the learning rate and this is how we can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m42s)
00:13:42

[do it and in fact this idea of using](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m44s)
00:13:44

[this technique on top of more advanced](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m46s)
00:13:46

[optimizers like Adam might haven't even](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m49s)
00:13:49

[seen mentioned in a paper before so I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m50s)
00:13:50

[think this is like a I mean it's not a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m52s)
00:13:52

[huge breakthrough it seems obvious but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m54s)
00:13:54

[nobody else seems to tried it so as you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m56s)
00:13:56

[can see it was well](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h13m59s)
00:13:59

[when we use optimizers like Adam ditched](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m05s)
00:14:05

[Harvick adaptive learning rate so and he](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m08s)
00:14:08

[said this learning rate is Italy initial](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m10s)
00:14:10

[learning rate because it changes during](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m12s)
00:14:12

[the people so we're going to be learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m14s)
00:14:14

[about things like Adam the details about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m21s)
00:14:21

[it later in the class but the basic](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m24s)
00:14:24

[answer is no even with even the Adam](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m26s)
00:14:26

[that there actually is a learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m28s)
00:14:28

[it's just being it's being basically](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m29s)
00:14:29

[divided by the the gradient the average](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m35s)
00:14:35

[previous gradient and also the recent](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m39s)
00:14:39

[summer Squared's of gradients so there's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m41s)
00:14:41

[still like a number called the learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m43s)
00:14:43

[rate there there isn't a even these so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m45s)
00:14:45

[called dynamic learning rate methods](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m47s)
00:14:47

[still have unlearning rate okay so the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h14m49s)
00:14:49

[most important thing that you can do to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m00s)
00:15:00

[make your model better and is to give it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m04s)
00:15:04

[more data so the challenge that happens](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m07s)
00:15:07

[is that these models have hundreds of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m10s)
00:15:10

[millions of parameters and if you train](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m13s)
00:15:13

[them for a while they start to do what's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m16s)
00:15:16

[called overfitting and so overfitting](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m19s)
00:15:19

[means that they're going to start to see](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m21s)
00:15:21

[like the specific details of the images](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m23s)
00:15:23

[you're giving them rather than the more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m26s)
00:15:26

[general learning that can transfer](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m27s)
00:15:27

[across to the validation set so the best](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m31s)
00:15:31

[thing we can do to avoid overfitting is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m34s)
00:15:34

[to find more data now obviously one way](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m36s)
00:15:36

[to do that would just be to collect more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m39s)
00:15:39

[data from where you're getting it from](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m41s)
00:15:41

[or label more data but a really easy way](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m42s)
00:15:42

[that we should always do is to use](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m45s)
00:15:45

[something called data augmentation so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m47s)
00:15:47

[they don't open tuition is one of these](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m51s)
00:15:51

[things that's key in many courses it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m53s)
00:15:53

[not even mentioned at all or if it is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m55s)
00:15:55

[it's kind of like an advanced topic](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m57s)
00:15:57

[right at the end but actually it's like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h15m58s)
00:15:58

[the most important thing that you can do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m00s)
00:16:00

[to make a better model okay and so it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m03s)
00:16:03

[built into the faster you library to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m05s)
00:16:05

[make it very easy to do and so we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m07s)
00:16:07

[going to look at the details of the code](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m08s)
00:16:08

[shortly but the basic idea is that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m10s)
00:16:10

[as in our initial code we had a line](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m14s)
00:16:14

[that said image classified data from](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m19s)
00:16:19

[parts and we passed in the path to our](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m22s)
00:16:22

[data and for transforms we passed in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m23s)
00:16:23

[basically the sizing the architecture](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m26s)
00:16:26

[we'll look at this in more detail](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m30s)
00:16:30

[shortly we just add one more parameter](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m31s)
00:16:31

[which is what kind of data augmentation](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m34s)
00:16:34

[do you want to do and so to understand](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m36s)
00:16:36

[data augmentation it's may be easiest to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m41s)
00:16:41

[look at some pictures of data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m43s)
00:16:43

[augmentation so what I've done here](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m44s)
00:16:44

[again we'll look at the code in more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m47s)
00:16:47

[detail later but the basic idea is oh](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m48s)
00:16:48

[I've run I've built a data class like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m50s)
00:16:50

[multiple times I'm going to do it six](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m56s)
00:16:56

[times and each time I'm going to plot](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h16m58s)
00:16:58

[the same catch and you can see that what](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m00s)
00:17:00

[happens is that this cap here is further](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m03s)
00:17:03

[over to the left this one here is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m07s)
00:17:07

[further over to the right and this one](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m09s)
00:17:09

[here is fit horizontally and so forth so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m10s)
00:17:10

[data augmentation different types of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m13s)
00:17:13

[image you're going to want different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m17s)
00:17:17

[types of data augmentation right so for](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m19s)
00:17:19

[example if you were trying to recognize](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m22s)
00:17:22

[letters and digits you wouldn't want to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m25s)
00:17:25

[flip horizontally because like it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m27s)
00:17:27

[actually has a different meaning whereas](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m29s)
00:17:29

[on the other hand if you're looking at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m31s)
00:17:31

[photos of cats and dogs you probably](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m33s)
00:17:33

[don't want to fit vertically because](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m36s)
00:17:36

[cats aren't generally upside down all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m38s)
00:17:38

[right where else if you're looking at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m40s)
00:17:40

[there's a current Cargill competition](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m42s)
00:17:42

[which is recognizing icebergs in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m44s)
00:17:44

[satellite images you probably do want to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m47s)
00:17:47

[fit them upside down because it's really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m50s)
00:17:50

[matter which area around the iceberg or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m52s)
00:17:52

[the satellite was right so one of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m54s)
00:17:54

[examples of the transform sets we have](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h17m58s)
00:17:58

[is transforms sidon so in other words if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m00s)
00:18:00

[you have photos that are like generally](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m03s)
00:18:03

[taken from the side which generally](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m05s)
00:18:05

[means you want to be able to flip them](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m07s)
00:18:07

[horizontally but not vertically this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m08s)
00:18:08

[going to give you all the transforms you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m10s)
00:18:10

[need for that so it'll flip them](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m12s)
00:18:12

[sideways rotate them by small amounts](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m13s)
00:18:13

[but not too much and slightly bury their](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m16s)
00:18:16

[contrast and brightness and slightly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m19s)
00:18:19

[zoom in and out a little bit and move](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m22s)
00:18:22

[them around a little](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m24s)
00:18:24

[so each time it's a slightly different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m25s)
00:18:25

[fight billionaires we're getting a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m26s)
00:18:26

[couple of questions from people about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m30s)
00:18:30

[you explaining in the reason why you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m33s)
00:18:33

[don't think the minimum of the loss](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m36s)
00:18:36

[curve yeah but it's like the higher rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m38s)
00:18:38

[so yeah and also could you people](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m41s)
00:18:41

[understand if this works for every CNN](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m44s)
00:18:44

[for CNN every minute there's a running](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m48s)
00:18:48

[right fine done yeah exactly yeah okay](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m52s)
00:18:52

[great](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m58s)
00:18:58

[um could you put your hand up if there's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h18m58s)
00:18:58

[a spare seat next to you so there was a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m02s)
00:19:02

[question about the learning rate finder](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m11s)
00:19:11

[about why do we use the learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m13s)
00:19:13

[that's less than the lowest point and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m15s)
00:19:15

[the reason why is to understand what's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m18s)
00:19:18

[going on with this learning rate finder](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m20s)
00:19:20

[so let's go back to our picture here](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m24s)
00:19:24

[like how do we figure out what learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m28s)
00:19:28

[rate to use right and so what we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m31s)
00:19:31

[going to do is we're going to take steps](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m33s)
00:19:33

[and each time we're going to double the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m35s)
00:19:35

[learning rate so kind of double the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m39s)
00:19:39

[amount by which we multiply the grander](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m41s)
00:19:41

[gradient so in other words would go tiny](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m43s)
00:19:43

[step slightly bigger slightly bigger](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m45s)
00:19:45

[slightly bigger slightly bigger slightly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m47s)
00:19:47

[bigger slightly bigger okay and so the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m51s)
00:19:51

[question is of the purpose of this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m57s)
00:19:57

[not to find the minimum the purpose of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h19m59s)
00:19:59

[this is to figure out what learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m01s)
00:20:01

[is allowing us to decrease quickly right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m03s)
00:20:03

[so the point at which the loss was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m07s)
00:20:07

[lowest here is actually there right but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m09s)
00:20:09

[that learning rate actually looks like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m13s)
00:20:13

[it's probably too high it's going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m15s)
00:20:15

[just jump like probably backwards and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m16s)
00:20:16

[forwards okay so instead what we do is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m19s)
00:20:19

[we go back to the point where the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m22s)
00:20:22

[learning rates quickly are giving us a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m24s)
00:20:24

[quick increase in the loss so here is so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m26s)
00:20:26

[here is the actual learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m33s)
00:20:33

[increasing every single time we look at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m34s)
00:20:34

[a new mini batch](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m36s)
00:20:36

[so mini-batch reiteration versus](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m38s)
00:20:38

[learning right and then here is learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m40s)
00:20:40

[rate versus loss so here's that point at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m42s)
00:20:42

[the bottom where is now already too high](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m44s)
00:20:44

[okay and so here's the point where we go](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m47s)
00:20:47

[back a little bit and it's increasing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m49s)
00:20:49

[nice and quickly we're going to learn](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m51s)
00:20:51

[about something called stochastic](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m55s)
00:20:55

[gradient descent with restarts shortly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m57s)
00:20:57

[where we're going to see like in a sense](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h20m59s)
00:20:59

[you might want to go back to 1 enoch 3](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m01s)
00:21:01

[where it's actually even steeper still](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m03s)
00:21:03

[and maybe we would actually find this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m05s)
00:21:05

[book actually learn even quicker you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m07s)
00:21:07

[could try it but we're going to see](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m11s)
00:21:11

[later why actually using a higher number](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m13s)
00:21:13

[is going to give us better](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m14s)
00:21:14

[generalization so for now let's put that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m16s)
00:21:16

[aside do you mean higher learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m19s)
00:21:19

[when you say I know I mean higher](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m22s)
00:21:22

[letting retina say higher](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m24s)
00:21:24

[yeah yeah I mean I am learning rate so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m25s)
00:21:25

[as we increase the iterations from the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m31s)
00:21:31

[learning rate finder the learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m33s)
00:21:33

[is going up this is iterations versus](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m35s)
00:21:35

[learning ready okay so as we do that as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m37s)
00:21:37

[the learning rate increases and we plot](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m41s)
00:21:41

[it here the loss Goes Down and here we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m43s)
00:21:43

[get to the point where the learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m46s)
00:21:46

[is too high and at that point the most](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m47s)
00:21:47

[is now getting worse because I asked the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m50s)
00:21:50

[question because you were just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m52s)
00:21:52

[indicating that you know even though the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m54s)
00:21:54

[minimum was at 10 to the minus 1 you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m55s)
00:21:55

[were gonna you suggest that we should](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h21m58s)
00:21:58

[choose 10 to the minus 2 but now you're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m00s)
00:22:00

[saying I mean we should go back the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m03s)
00:22:03

[other way higher so I didn't mean to say](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m04s)
00:22:04

[that I'm sorry if I said something](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m07s)
00:22:07

[backwards I want to go back down to the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m08s)
00:22:08

[lower learning rate so possibly I said a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m11s)
00:22:11

[higher when I meant higher into this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m14s)
00:22:14

[lower OS do you know I'm learning right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m17s)
00:22:17

[okay thanks yep](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m19s)
00:22:19

[last class is said that the local all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m22s)
00:22:22

[the local minima are the same and this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m26s)
00:22:26

[graph also shows the same is that is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m29s)
00:22:29

[this something that was observed or is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m32s)
00:22:32

[the logic theory behind it that's not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m33s)
00:22:33

[what this graph is showing this graph is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m37s)
00:22:37

[simply showing that there's a point](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m40s)
00:22:40

[where if we increase the learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m41s)
00:22:41

[more then it stops getting better than](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m43s)
00:22:43

[actually starts getting worse the idea](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m46s)
00:22:46

[that all local minima are the same is a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m48s)
00:22:48

[totally separate issue and it's actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m53s)
00:22:53

[something else we'll see a picture of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m57s)
00:22:57

[shortly so let's come back to that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h22m58s)
00:22:58

[Jeremy do we have to find the base](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m02s)
00:23:02

[learning rate every time we are going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m05s)
00:23:05

[run a poke third time we're running on a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m08s)
00:23:08

[poke and a pop so how many times should](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m13s)
00:23:13

[I run this like let me write find my](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m15s)
00:23:15

[training that's a great question unit um](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m19s)
00:23:19

[I certainly run it once when I start](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m27s)
00:23:27

[later on in this class we're going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m31s)
00:23:31

[learn about unfreezing layers and after](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m34s)
00:23:34

[I unfreeze layers I sometimes run it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m37s)
00:23:37

[again if I do something to like change](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m40s)
00:23:40

[the thing I'm training or change the way](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m42s)
00:23:42

[I'm training it you may want to run it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m44s)
00:23:44

[again basically or you know if you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m46s)
00:23:46

[particularly if you've changed something](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m50s)
00:23:50

[about how you train like unfreezing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m51s)
00:23:51

[layers which we're gonna soon learn](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m54s)
00:23:54

[about and you're finding the other](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m55s)
00:23:55

[training is unstable or too slow](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h23m57s)
00:23:57

[well again you can run it again there's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m01s)
00:24:01

[never any harm](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m03s)
00:24:03

[in running it it doesn't take very long](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m04s)
00:24:04

[that's great question okay so back to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m07s)
00:24:07

[data augmentation so if we add to a when](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m11s)
00:24:11

[we run this little transforms from model](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m14s)
00:24:14

[function we pass in orientation](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m17s)
00:24:17

[transforms we can pass in the main to a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m20s)
00:24:20

[transform side on or transforms top down](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m23s)
00:24:23

[later on we'll learn about creating your](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m26s)
00:24:26

[own custom transform lists as well but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m28s)
00:24:28

[for now because we're taking pictures](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m31s)
00:24:31

[from the side cats and dogs will say](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m32s)
00:24:32

[transform side on and now each time we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m35s)
00:24:35

[look at an image it's going to be zoomed](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m38s)
00:24:38

[in or out a little bit moved around a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m41s)
00:24:41

[little bit](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m42s)
00:24:42

[rotated a little bit possibly flipped](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m43s)
00:24:43

[okay and so what this does is it's not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m47s)
00:24:47

[exactly creating new data but as far as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m50s)
00:24:50

[the convolutional neural net is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m53s)
00:24:53

[concerned it's a different way of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m55s)
00:24:55

[looking at this thing and it actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m57s)
00:24:57

[therefore allows it to learn how to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h24m59s)
00:24:59

[recognize cats or dogs from somewhat](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m02s)
00:25:02

[different angles right so when we do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m06s)
00:25:06

[data orientation we're basically trying](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m07s)
00:25:07

[to say based on our domain knowledge](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m09s)
00:25:09

[here here are different ways that we can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m12s)
00:25:12

[mess with this image that we know still](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m15s)
00:25:15

[make it the same image you know and that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m18s)
00:25:18

[we could expect that you might actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m20s)
00:25:20

[see that kind of image in the real world](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m22s)
00:25:22

[so what we can do now is when we call](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m25s)
00:25:25

[this from parts function which we'll](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m28s)
00:25:28

[learn more about shortly we can now pass](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m31s)
00:25:31

[in this set of transforms which actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m33s)
00:25:33

[have these augmentations in now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m35s)
00:25:35

[so that's going to we're going to start](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m41s)
00:25:41

[from scratch here we do a fit and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m42s)
00:25:42

[initially the augmentations actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m47s)
00:25:47

[don't do anything and the reason](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m51s)
00:25:51

[initially they don't do anything is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m53s)
00:25:53

[because we've got here something that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m55s)
00:25:55

[says precompute equals true we're going](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m56s)
00:25:56

[to come back to these lots of times but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h25m59s)
00:25:59

[basically what this is doing is do you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m03s)
00:26:03

[remember this picture we saw where we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m06s)
00:26:06

[learn each different layer has these](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m08s)
00:26:08

[activations that basically look for it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m11s)
00:26:11

[or anything from the middle of flowers](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m13s)
00:26:13

[to eyeballs of birds or whatever right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m16s)
00:26:16

[and so literally what happens is that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m21s)
00:26:21

[the the later layers of this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m25s)
00:26:25

[convolutional neural network have these](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m28s)
00:26:28

[things called activations and activation](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m30s)
00:26:30

[literally it's a number an activation is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m32s)
00:26:32

[a number that says this feature like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m34s)
00:26:34

[eyeball of bird is in this location with](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m38s)
00:26:38

[this level of confidence with its](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m42s)
00:26:42

[probability right and so we're going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m44s)
00:26:44

[see a lot of this later but what we can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m46s)
00:26:46

[do is we can say all right well in this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m50s)
00:26:50

[we've got a pre trained network remember](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m52s)
00:26:52

[and a pre trained network is one where](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m55s)
00:26:55

[it's already learned to recognize](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m57s)
00:26:57

[certain things in this case it's learnt](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h26m58s)
00:26:58

[to recognize the one and a half million](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m00s)
00:27:00

[images in the imagenet dataset and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m02s)
00:27:02

[what we could do is we could take the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m05s)
00:27:05

[the second last layer so the one which](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m07s)
00:27:07

[is like got all of the information](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m10s)
00:27:10

[necessary to figure out what kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m12s)
00:27:12

[thing a thing is and we can save those](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m14s)
00:27:14

[activations so basically saving things](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m17s)
00:27:17

[saying you know there's this level of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m19s)
00:27:19

[eyeball nurse here in this level of dogs](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m21s)
00:27:21

[facing us here or in this level of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m24s)
00:27:24

[fluffy ear there and so forth and so we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m25s)
00:27:25

[save for every image these activations](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m29s)
00:27:29

[and that we call them the pre computed](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m32s)
00:27:32

[activations and so the idea is now that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m35s)
00:27:35

[when we want to create a new classifier](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m38s)
00:27:38

[which can basically take advantage of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m41s)
00:27:41

[these pre computed applications we can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m43s)
00:27:43

[just very quickly train when all the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m46s)
00:27:46

[details there shortly we can very](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m48s)
00:27:48

[quickly train a simple linear model](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m50s)
00:27:50

[based on those](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m52s)
00:27:52

[and so that's what happens when we say](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m54s)
00:27:54

[pre-compute equals true and that's why](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m55s)
00:27:55

[you may have noticed this week the first](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h27m58s)
00:27:58

[time that you run a model a new model it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m01s)
00:28:01

[takes a minute or two where else you saw](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m05s)
00:28:05

[when I ran it it took like five or ten](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m08s)
00:28:08

[seconds took you a minute or two and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m10s)
00:28:10

[that's because it had to pre-compute](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m12s)
00:28:12

[these activations and just has to do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m14s)
00:28:14

[that once if you're using like your own](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m16s)
00:28:16

[computer or AWS it just has to do it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m19s)
00:28:19

[once ever if you're using Kressel it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m21s)
00:28:21

[actually has to do it once every single](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m24s)
00:28:24

[time you rerun press all because press](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m28s)
00:28:28

[or uses are just for these pre computed](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m30s)
00:28:30

[activations it uses a special that all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m33s)
00:28:33

[had a scratch space that disappears each](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m35s)
00:28:35

[time you restart your press or instance](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m37s)
00:28:37

[so other than the special case of cresol](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m39s)
00:28:39

[generally speak he does have to run at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m42s)
00:28:42

[once](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m44s)
00:28:44

[ever for a data set okay so the issue](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m44s)
00:28:44

[with that is that since we pre computed](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m50s)
00:28:50

[for each image you know how much does it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m53s)
00:28:53

[have an EI here and how much does it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m56s)
00:28:56

[have a lizard's eyeball there and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h28m57s)
00:28:57

[forth that means that data augmentations](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m00s)
00:29:00

[don't work right in other words even](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m02s)
00:29:02

[though we're trying to show at a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m04s)
00:29:04

[different version of the cat each time](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m05s)
00:29:05

[we've pre computed the activations for a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m07s)
00:29:07

[particular version of that cat so in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m09s)
00:29:09

[order to use data augmentation we just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m13s)
00:29:13

[have to go and learn pre compute equals](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m15s)
00:29:15

[false okay and then we can run a few](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m17s)
00:29:17

[more APIs right and so you can see here](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m20s)
00:29:20

[that as we run more a Potts the accuracy](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m25s)
00:29:25

[isn't particularly getting better that's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m29s)
00:29:29

[the bad news](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m31s)
00:29:31

[the good news is that you can see that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m32s)
00:29:32

[the train loss practices like the way of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m35s)
00:29:35

[measuring the error of this model](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m39s)
00:29:39

[although that's getting better the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m40s)
00:29:40

[errors going down the validation error](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m42s)
00:29:42

[isn't going down and but we're not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m45s)
00:29:45

[overfitting and overfitting would mean](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m48s)
00:29:48

[that the training loss is much lower](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m50s)
00:29:50

[than the validation loss and we're going](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m53s)
00:29:53

[to talk about that a lot during this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m56s)
00:29:56

[course but the general idea here is if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h29m57s)
00:29:57

[you're doing much better job on the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m00s)
00:30:00

[training set then you are on the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m02s)
00:30:02

[validation set that means your models](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m04s)
00:30:04

[not generalize](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m06s)
00:30:06

[so we're not at that point which is good](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m07s)
00:30:07

[but we're not really improving so we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m10s)
00:30:10

[going to have to figure out how to deal](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m14s)
00:30:14

[with that before we do I want to show](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m15s)
00:30:15

[you one other cool trick I've added here](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m19s)
00:30:19

[cycle length equals one and this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m21s)
00:30:21

[another really interesting idea here's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m25s)
00:30:25

[the basic idea](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m29s)
00:30:29

[cycle length equals one enables a recent](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m30s)
00:30:30

[fairly recent discovery and deep](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m33s)
00:30:33

[learning called stochastic gradient](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m35s)
00:30:35

[descent with restarts and the basic idea](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m37s)
00:30:37

[is this as you as you get closer and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m40s)
00:30:40

[closer as you get closer and closer to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m45s)
00:30:45

[the right spot right now getting closer](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m49s)
00:30:49

[and closer I may want to start to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m52s)
00:30:52

[decrease my learning rate right because](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m55s)
00:30:55

[as I get closer I'm kind of like oh I'm](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m57s)
00:30:57

[pretty close down so let's let's slow](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h30m59s)
00:30:59

[down my steps to try to get executive](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m01s)
00:31:01

[the right spot right and so as we do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m04s)
00:31:04

[more iterations](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m08s)
00:31:08

[our learning rate perhaps should](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m12s)
00:31:12

[actually go down right because as we go](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m15s)
00:31:15

[along we're getting closer and closer to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m19s)
00:31:19

[where we want to be and we want to like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m20s)
00:31:20

[get exactly to the right spot okay so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m22s)
00:31:22

[the idea of decreasing the learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m25s)
00:31:25

[as you train is called](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m27s)
00:31:27

[learning rate annealing and it's it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m29s)
00:31:29

[very very common very very popular](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m33s)
00:31:33

[everybody uses it basically all the time](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m36s)
00:31:36

[the most common kind of learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m39s)
00:31:39

[annealing is really horrendously hacky](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m41s)
00:31:41

[it's basically that researchers like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m45s)
00:31:45

[pick a learning rate that seems to work](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m47s)
00:31:47

[for a while and then when it stops](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m49s)
00:31:49

[learning well they drop it down by about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m51s)
00:31:51

[10 times and then they keep learning a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m53s)
00:31:53

[bit more until it doesn't seem to be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m55s)
00:31:55

[improving and they drop it down by](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m56s)
00:31:56

[another ten times that's what most](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h31m58s)
00:31:58

[academic research papers and most people](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m00s)
00:32:00

[in industry do so this would be like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m02s)
00:32:02

[stepwise annealing very manual very](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m04s)
00:32:04

[annoying a better approach is simply to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m07s)
00:32:07

[pick some kind of functional form like a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m11s)
00:32:11

[line it turns out that a really good](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m14s)
00:32:14

[functional form is one half of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m17s)
00:32:17

[cosine curve](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m19s)
00:32:19

[right and the reason why is that for a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m22s)
00:32:22

[while when you're not very close you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m25s)
00:32:25

[kind of have a really high learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m27s)
00:32:27

[and that is you do get close you kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m29s)
00:32:29

[quickly drop down and do a few](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m31s)
00:32:31

[iterations with a really low learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m33s)
00:32:33

[rate and so this is called cosine](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m35s)
00:32:35

[annealing so to those of you who haven't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m37s)
00:32:37

[done trigonometry for a while](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m40s)
00:32:40

[cosine basically looks something like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m41s)
00:32:41

[this right so we've picked one little](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m44s)
00:32:44

[half piece okay so we're going to use](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m47s)
00:32:47

[cosine annealing but here's the thing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m52s)
00:32:52

[when you're in a very high dimensional](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h32m56s)
00:32:56

[space right near we're only able to show](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m00s)
00:33:00

[three dimensions right but in reality](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m02s)
00:33:02

[we've got hundreds of millions of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m05s)
00:33:05

[dimensions we've got lots of different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m06s)
00:33:06

[fairly flat points there no not the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m10s)
00:33:10

[actual local minima but they're fairly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m13s)
00:33:13

[flat points all of which are pretty good](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m14s)
00:33:14

[right but they might differ in a really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m17s)
00:33:17

[interesting way which is that some of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m20s)
00:33:20

[those flat points let me show you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m22s)
00:33:22

[let's imagine we've got a surface that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m32s)
00:33:32

[looks something like this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m35s)
00:33:35

[right now imagine that where you kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m40s)
00:33:40

[random guest started here and our](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m43s)
00:33:43

[initial therefore kind of learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m47s)
00:33:47

[annealing schedule got us down to here](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m49s)
00:33:49

[now indeed that's a pretty nice low](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m51s)
00:33:51

[error right but it probably doesn't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m55s)
00:33:55

[generalize very well which is to say if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h33m57s)
00:33:57

[we use a different data set where things](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m00s)
00:34:00

[are just kind of slightly different in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m02s)
00:34:02

[one of these directions suddenly is a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m04s)
00:34:04

[terrible solution right where else over](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m07s)
00:34:07

[here is basically equally good in terms](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m10s)
00:34:10

[of loss right but it rather suggests](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m13s)
00:34:13

[that if you move if you have slightly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m16s)
00:34:16

[different data sets that are slightly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m18s)
00:34:18

[moved in different directions it's still](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m19s)
00:34:19

[going to be good right so in other words](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m21s)
00:34:21

[we would expect this solution here is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m23s)
00:34:23

[probably going to generalize better than](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m25s)
00:34:25

[this by key one so here's what we do is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m29s)
00:34:29

[we've got like a bunch of different low](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m33s)
00:34:33

[bits right then our standard loading](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m35s)
00:34:35

[rate annealing approach will start of go](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m39s)
00:34:39

[down here or downhill downhill downhill](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m41s)
00:34:41

[downhill to one spot right but what we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m43s)
00:34:43

[could do instead is use a learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m47s)
00:34:47

[schedule that looks like this which is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m49s)
00:34:49

[to say we do a cosign annealing and then](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m54s)
00:34:54

[suddenly jump up again into a cosign](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m56s)
00:34:56

[annealing and then jump up again](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m58s)
00:34:58

[and so each time we jump up it means](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h34m59s)
00:34:59

[that if they're going to spiky bit and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m02s)
00:35:02

[then we subtly increase the learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m04s)
00:35:04

[rate and it jumps now all the way over](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m06s)
00:35:06

[to here and so then we kind of learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m08s)
00:35:08

[right in your learning right near death](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m10s)
00:35:10

[down to here and then we jump up again](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m11s)
00:35:11

[to a high learning rate oh and it stays](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m13s)
00:35:13

[here right so in other words each time](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m16s)
00:35:16

[we jump up the learning rate that means](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m19s)
00:35:19

[that if it's in a nasty spiky part of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m21s)
00:35:21

[the surface it's going to hop out of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m24s)
00:35:24

[spiky part and hopefully if we do that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m26s)
00:35:26

[enough times it'll eventually find a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m28s)
00:35:28

[nice smooth Bowl](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m30s)
00:35:30

[could you get the same effect by running](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m40s)
00:35:40

[multiple iterations through the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m42s)
00:35:42

[different ground of my starting point so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m44s)
00:35:44

[that eventually you explore all possible](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m46s)
00:35:46

[minimize yeah so in fact that that's a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m48s)
00:35:48

[great question and before this approach](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m52s)
00:35:52

[which is called stochastic gradient](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h35m59s)
00:35:59

[descent with restarts was was created](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m01s)
00:36:01

[that's exactly what people used to do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m05s)
00:36:05

[they used to create these things called](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m07s)
00:36:07

[ensembles where they would basically](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m08s)
00:36:08

[relearn a whole new model ten times in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m11s)
00:36:11

[the hope that one of them's like but it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m15s)
00:36:15

[ended up being better and so the cool](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m17s)
00:36:17

[thing about this decosta gradient](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m22s)
00:36:22

[descent with restarts is that the model](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m24s)
00:36:24

[once we're in a reasonably good spot](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m26s)
00:36:26

[each time we jump up the learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m29s)
00:36:29

[it doesn't restart it actually hangs out](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m30s)
00:36:30

[in this nice part part of the space and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m34s)
00:36:34

[then keeps getting better so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m36s)
00:36:36

[interestingly it turns out that this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m37s)
00:36:37

[approach where we do this a bunch of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m39s)
00:36:39

[separate cosine annealing steps we end](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m42s)
00:36:42

[up with a better result as then if we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m45s)
00:36:45

[just randomly try it a few different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m49s)
00:36:49

[starting points so it's a super neat](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m50s)
00:36:50

[trick and it's a fairly recent](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m54s)
00:36:54

[development but and again almost](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h36m58s)
00:36:58

[nobody's heard of it but I found like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m00s)
00:37:00

[it's now like my superpower like using](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m04s)
00:37:04

[this along with the learning rate finder](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m07s)
00:37:07

[like I can get better results than](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m10s)
00:37:10

[nearly anybody like in a casual](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m14s)
00:37:14

[competition you know in the first week](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m16s)
00:37:16

[or two I can like jump in it's been an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m18s)
00:37:18

[arrow to and back I've got a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m20s)
00:37:20

[fantastically good result and so this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m23s)
00:37:23

[why I didn't pick the point where it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m26s)
00:37:26

[got the steepest slope I actually trying](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m29s)
00:37:29

[to pick something kind of aggressively](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m31s)
00:37:31

[high it's still getting down but maybe](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m33s)
00:37:33

[like getting to the point where it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m35s)
00:37:35

[nearly too high not because I want to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m36s)
00:37:36

[make sure because that's because when we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m39s)
00:37:39

[do this stochastic gradient descent with](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m40s)
00:37:40

[restarts this ten to the negative two](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m43s)
00:37:43

[represents the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m46s)
00:37:46

[a highest number that it uses so it goes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m48s)
00:37:48

[up to ten to the negative two and then](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m51s)
00:37:51

[goes down and then up to ten negative](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m54s)
00:37:54

[two and down so if I use to lower](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m56s)
00:37:56

[learning rate it's not going to jump to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h37m58s)
00:37:58

[a different part of the function so I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m01s)
00:38:01

[have a few questions but the first one](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m06s)
00:38:06

[is how many times do you change your](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m08s)
00:38:08

[learning rate you want to work we don't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m10s)
00:38:10

[change the learning rate all three how](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m13s)
00:38:13

[many times - okay so in terms of this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m15s)
00:38:15

[part here where it's going down we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m17s)
00:38:17

[change the learning rate every single](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m19s)
00:38:19

[mini - all right and then the number of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m20s)
00:38:20

[times we reset it is set by the cycle](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m23s)
00:38:23

[length parameter and so 1 means reset it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m27s)
00:38:27

[up to every epoch so if I had to there](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m30s)
00:38:30

[it would reset it up to every to epochs](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m33s)
00:38:33

[and interestingly this this point that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m36s)
00:38:36

[when we do the learning rate and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m38s)
00:38:38

[kneeling that we actually change it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m39s)
00:38:39

[every single batch it turns out to be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m41s)
00:38:41

[really critical to making this work and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m43s)
00:38:43

[it again is very different to what](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m47s)
00:38:47

[nearly everybody in industry in academia](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m48s)
00:38:48

[has done before](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m50s)
00:38:50

[what do you get a chance could you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m52s)
00:38:52

[explain recompute it was true because](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m54s)
00:38:54

[it's still yeah we're going to come back](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h38m58s)
00:38:58

[to that multiple times in this course so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m02s)
00:39:02

[the way this course has been a work is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m04s)
00:39:04

[we're going to like do a really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m06s)
00:39:06

[high-level version of each thing and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m07s)
00:39:07

[then we're going to like come back to it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m09s)
00:39:09

[in two or three lessons and then come](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m11s)
00:39:11

[back to it at the end of the course and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m12s)
00:39:12

[each time we're going to see like more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m14s)
00:39:14

[of the math more of the code and get a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m15s)
00:39:15

[deeper view okay and we can talk about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m18s)
00:39:18

[it also in the forums during the week](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m20s)
00:39:20

[our main goal is to generalize and we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m26s)
00:39:26

[don't want to get those like narrow](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m29s)
00:39:29

[demas yeah that's a it's a very short](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m31s)
00:39:31

[summary this method are we keeping track](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m34s)
00:39:34

[off to minimize and averaging them ah](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m37s)
00:39:37

[that's that's another level of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m40s)
00:39:40

[sophistication and indeed you can see](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m44s)
00:39:44

[there's something here called snapshot](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m45s)
00:39:45

[ensemble so we're not doing it in the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m47s)
00:39:47

[code right now but yes if you wanted to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m50s)
00:39:50

[make us generalize even better you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m53s)
00:39:53

[save the weights here and here and here](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m55s)
00:39:55

[and then take the average](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h39m58s)
00:39:58

[ishes but for now we're just going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m00s)
00:40:00

[pick the last one if you want to skip](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m03s)
00:40:03

[ahead if you want to skip ahead there's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m10s)
00:40:10

[a parameter called cycle safe name which](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m16s)
00:40:16

[you can add as well as cycle them and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m19s)
00:40:19

[that will save a set of weights at the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m21s)
00:40:21

[end of every learning rate cycle and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m23s)
00:40:23

[then you can ensemble them ok so we've](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m26s)
00:40:26

[got a pretty decent model here ninety](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m35s)
00:40:35

[nine point three percent accuracy and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m38s)
00:40:38

[we've gone through of you know a few](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m41s)
00:40:41

[steps that is taken you know a minute or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m42s)
00:40:42

[two to run and so from time to time I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m44s)
00:40:44

[tend to save my weight so if you go](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m47s)
00:40:47

[learn dot save and then pass in a file](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m49s)
00:40:49

[name it's going to go ahead and save](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m51s)
00:40:51

[that for you later on if you go learn](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m53s)
00:40:53

[load you'll be straight back to where](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m55s)
00:40:55

[you came from okay so it's a good idea](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h40m57s)
00:40:57

[to do that from time to time this is a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m00s)
00:41:00

[good time to mention what happens when](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m03s)
00:41:03

[you do this when you go learn dot save](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m06s)
00:41:06

[when you create precomputed activations](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m10s)
00:41:10

[another thing we learn about soon when](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m12s)
00:41:12

[you create resized images these are all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m14s)
00:41:14

[creating various temporary files okay](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m16s)
00:41:16

[and so what happens is if we go to data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m20s)
00:41:20

[and we go to dogs cats this is my data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m28s)
00:41:28

[folder and you'll see there's a folder](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m34s)
00:41:34

[here called TMP or - and so this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m36s)
00:41:36

[automatically created and all of my pre](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m41s)
00:41:41

[computed activations end up in here I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m43s)
00:41:43

[mention this because if if things are if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m46s)
00:41:46

[you're getting weird errors that might](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m50s)
00:41:50

[be because you've got some Oh pre](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m52s)
00:41:52

[computed activations like we're only](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m54s)
00:41:54

[half completed or are in some way](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m56s)
00:41:56

[incompatible with what you're doing so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h41m59s)
00:41:59

[you can always go ahead and just delete](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m01s)
00:42:01

[this TMP this temporary directory and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m03s)
00:42:03

[see if that causes your error to go away](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m05s)
00:42:05

[this is the faster I equivalent of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m08s)
00:42:08

[turning it off and then on again](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m10s)
00:42:10

[you'll also see there's a directory](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m12s)
00:42:12

[called models and that's where all of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m14s)
00:42:14

[these when you say dot save with a model](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m16s)
00:42:16

[that's where that's going to go actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m19s)
00:42:19

[it reminds me when the stochastic](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m22s)
00:42:22

[gradient descent with restarts paper](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m23s)
00:42:23

[came out I saw a tweet that was somebody](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m25s)
00:42:25

[was like Oh to make your deep learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m27s)
00:42:27

[work better turn it off and then on](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m29s)
00:42:29

[again question it so if I want to see I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m30s)
00:42:30

[want to retrain my model fuselage again](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m38s)
00:42:38

[do I just do everything the 10 folder if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m40s)
00:42:40

[you want if you want to train your model](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m43s)
00:42:43

[from scratch there's generally no reason](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m51s)
00:42:51

[to delete the pre computed activations](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m54s)
00:42:54

[because the pre computed activations are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m56s)
00:42:56

[without any training that's what the pre](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h42m59s)
00:42:59

[trained model created with the with the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m02s)
00:43:02

[weights that you downloaded off the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m06s)
00:43:06

[internet the only yeah I mean the only](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m07s)
00:43:07

[reason you want to delete the pre](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m12s)
00:43:12

[computed activations is that there was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m14s)
00:43:14

[some error caused by like half creating](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m15s)
00:43:15

[them and crashing or some something like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m18s)
00:43:18

[that as you change the size of your](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m20s)
00:43:20

[import change different architectures](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m23s)
00:43:23

[and so forth they all create different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m25s)
00:43:25

[sets of activations with different file](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m26s)
00:43:26

[names so you don't generally you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m28s)
00:43:28

[shouldn't have to worry about it if you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m30s)
00:43:30

[want to start training again from](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m32s)
00:43:32

[scratch all you have to do is create a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m33s)
00:43:33

[new learn object so each time you go](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m35s)
00:43:35

[like conch learner dot pre-trained that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m40s)
00:43:40

[creates a new object with with new sets](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m42s)
00:43:42

[of weights fever train from okay so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m45s)
00:43:45

[before our break we'll finish off by](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m50s)
00:43:50

[talking about about fine-tuning and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m52s)
00:43:52

[differential learning rates and so so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h43m56s)
00:43:56

[far everything we've done has not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m00s)
00:44:00

[changed any of these free trained](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m05s)
00:44:05

[filters right so we've used a pre](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m08s)
00:44:08

[trained model that already knows how to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m09s)
00:44:09

[find at the early stages edges](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m12s)
00:44:12

[ingredients and then corners and curves](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m17s)
00:44:17

[and then repeating patterns and bits of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m21s)
00:44:21

[text](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m26s)
00:44:26

[and eventually eyeballs right we have](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m26s)
00:44:26

[not retrained any of those activations](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m30s)
00:44:30

[any of those features well specifically](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m35s)
00:44:35

[any of those weights in the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m38s)
00:44:38

[convolutional kernels all we've done is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m40s)
00:44:40

[we've learnt some new layers that we've](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m43s)
00:44:43

[added on top of these things we've](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m46s)
00:44:46

[learned how to mix and match these](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m48s)
00:44:48

[pre-trained features now obviously it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m50s)
00:44:50

[may turn out that your pictures have you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m54s)
00:44:54

[know different kinds of eyeballs or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h44m58s)
00:44:58

[faces or if you're using different kinds](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m00s)
00:45:00

[of images like satellite images totally](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m03s)
00:45:03

[different kinds of features altogether](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m05s)
00:45:05

[right so if you're like training to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m07s)
00:45:07

[recognize icebergs you'll probably want](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m10s)
00:45:10

[to go all the way back and learn you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m12s)
00:45:12

[know all the way back to kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m15s)
00:45:15

[different combinations of these simple](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m16s)
00:45:16

[gradients and edges in our cases dogs](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m18s)
00:45:18

[vs. cats we're going to have some minor](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m22s)
00:45:22

[differences but we still may find it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m24s)
00:45:24

[helpful to slightly tune some of these](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m26s)
00:45:26

[later layers as well so to tell the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m29s)
00:45:29

[learner that we now want to start](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m34s)
00:45:34

[actually changing the convolutional](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m36s)
00:45:36

[filters themselves we simply say](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m38s)
00:45:38

[unfreeze okay so a frozen layer is a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m41s)
00:45:41

[layer which is not trained is not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m44s)
00:45:44

[updated okay so unfreeze unfreezes all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m46s)
00:45:46

[of the layers now when you think about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m49s)
00:45:49

[it it's pretty obvious that layer one](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m51s)
00:45:51

[right which is like a diagonal edge or a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m56s)
00:45:56

[gradient probably doesn't need to change](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h45m59s)
00:45:59

[by much if at all right from the 1 and a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m02s)
00:46:02

[half million images on image net it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m05s)
00:46:05

[probably already is figured out pretty](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m06s)
00:46:06

[well how to find like edges of gradients](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m08s)
00:46:08

[it probably already knows also like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m10s)
00:46:10

[which kind of corners to look for and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m13s)
00:46:13

[how to find which kinds of curves and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m15s)
00:46:15

[forth so in other words these early](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m17s)
00:46:17

[layers probably need little if any](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m19s)
00:46:19

[learning where else these later ones are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m22s)
00:46:22

[much more likely to need more learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m26s)
00:46:26

[and this is universally true regardless](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m28s)
00:46:28

[of whether you're looking for satellite](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m30s)
00:46:30

[images of rainforests or icebergs or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m32s)
00:46:32

[whether you're looking for cats versus](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m34s)
00:46:34

[dogs right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m36s)
00:46:36

[so what we do is we create an array of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m38s)
00:46:38

[learning rates where we say okay these](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m41s)
00:46:41

[are the learning rates to use for our](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m45s)
00:46:45

[additional layers that we've added on](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m47s)
00:46:47

[top these are the learning rates to use](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m50s)
00:46:50

[in the middle few layers and these are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m53s)
00:46:53

[the learning rates to use for the first](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m56s)
00:46:56

[few layers so these are the ones for the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h46m58s)
00:46:58

[layers that represent like very basic](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m00s)
00:47:00

[geometric features these are the ones](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m02s)
00:47:02

[that are used to for the more complex](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m05s)
00:47:05

[kind of sophisticated convolutional](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m08s)
00:47:08

[features and these are the ones that are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m11s)
00:47:11

[used for the features that we've added](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m13s)
00:47:13

[and went from stretch right so you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m14s)
00:47:14

[create a array of learning rates and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m17s)
00:47:17

[then when we called up fit and pass an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m19s)
00:47:19

[array of learning rates it's now going](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m22s)
00:47:22

[to use those different learning rates](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m24s)
00:47:24

[for different parts of the model this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m25s)
00:47:25

[not something that we've like invented](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m30s)
00:47:30

[but I'd also say it's like it's so not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m34s)
00:47:34

[that common that it doesn't even have a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m37s)
00:47:37

[name as far as I know so we're going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m39s)
00:47:39

[call it differential learning rates if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m42s)
00:47:42

[it actually has a name or indeed if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m46s)
00:47:46

[somebody's actually written a paper](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m48s)
00:47:48

[specifically talking about it I don't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m49s)
00:47:49

[know there's a great researcher called](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m51s)
00:47:51

[Jason your Sinskey who who did write a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m54s)
00:47:54

[paper about the kind of the idea that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m56s)
00:47:56

[you might want different learning rates](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m58s)
00:47:58

[and showing why but I don't think any](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h47m59s)
00:47:59

[other libraries support it and yeah I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m02s)
00:48:02

[don't know of a name for it having said](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m05s)
00:48:05

[that though this ability to like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m07s)
00:48:07

[unfreeze and then use these differential](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m10s)
00:48:10

[learning rates I found it's like the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m12s)
00:48:12

[secret to taking a pretty good model and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m14s)
00:48:14

[putting it into an awesome model so just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m17s)
00:48:17

[to clarify so you have three numbers](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m25s)
00:48:25

[there okay three hyper parameters the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m29s)
00:48:29

[first one is the photo late model so the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m32s)
00:48:32

[mall that are late layers the so with](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m36s)
00:48:36

[the it's your answer is many many right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m41s)
00:48:41

[and they're kind of in groups and we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m44s)
00:48:44

[going to learn about the architecture](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m46s)
00:48:46

[this is called a ResNet for residual](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m47s)
00:48:47

[network](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m49s)
00:48:49

[it kind of has ResNet blocks and so what](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m50s)
00:48:50

[we're doing is we're grouping the blocks](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m53s)
00:48:53

[into three groups and so this one is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m54s)
00:48:54

[actually this first number is for the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h48m58s)
00:48:58

[earliest layers yeah they're ones](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m00s)
00:49:00

[closest to the pixels that represent](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m04s)
00:49:04

[like corners and edges and gradients but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m06s)
00:49:06

[why why do you well I thought those](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m09s)
00:49:09

[layers are frozen at first so yeah right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m12s)
00:49:12

[so we just said unfreeze the streets](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m15s)
00:49:15

[also we so yeah I'm freezing them](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m17s)
00:49:17

[because you have kind of partially](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m19s)
00:49:19

[trained although lately we've trained](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m20s)
00:49:20

[we've trained our added layers yes now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m24s)
00:49:24

[you are we training the Oh step exactly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m26s)
00:49:26

[obviously so it waits and the learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m28s)
00:49:28

[rate is particularly small for the early](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m30s)
00:49:30

[layers that's right because you just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m33s)
00:49:33

[find a want to find food yeah yeah we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m34s)
00:49:34

[probably don't want to change them at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m37s)
00:49:37

[all but you know if it does need to then](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m39s)
00:49:39

[it can thanks no problem so using the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m42s)
00:49:42

[differential in rates a little different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m50s)
00:49:50

[from like grid search there's no](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m51s)
00:49:51

[similarity to grid search so grid search](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m56s)
00:49:56

[is where we're trying to find the best](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h49m58s)
00:49:58

[hyper parameter for something so for](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m00s)
00:50:00

[example you could kind of think of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m03s)
00:50:03

[learning rate finder as a really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m07s)
00:50:07

[sophisticated grid search which is like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m09s)
00:50:09

[trying lots and lots of learning rates](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m11s)
00:50:11

[to find which one is best](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m12s)
00:50:12

[but this has nothing to do with that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m15s)
00:50:15

[this is actually for the entire training](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m16s)
00:50:16

[from now on it's actually going to use a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m18s)
00:50:18

[different learning rate for each layer](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m20s)
00:50:20

[and so I was wondering so you give a pre](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m28s)
00:50:28

[train model then you have to use the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m33s)
00:50:33

[same input dimensions right because I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m35s)
00:50:35

[was thinking okay let's say you have](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m39s)
00:50:39

[this big they use like big machines to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m40s)
00:50:40

[train these things and you want to take](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m43s)
00:50:43

[advantage of it how would you go about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m45s)
00:50:45

[you know you have like images that are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m46s)
00:50:46

[like bigger than the ones that they used](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m48s)
00:50:48

[or we're going to be talking about sizes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m50s)
00:50:50

[later but the short answer is that with](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m52s)
00:50:52

[this library and the modern](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m54s)
00:50:54

[architectures were using we can use any](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m56s)
00:50:56

[size we like so did I mean do we need](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h50m58s)
00:50:58

[can we at least just a specific layer we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m04s)
00:51:04

[can we're not doing it yet but if you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m08s)
00:51:08

[wanted to you can learn dot freeze](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m09s)
00:51:09

[underscore two and pass into layer](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m12s)
00:51:12

[number much to my surprise or at least](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m14s)
00:51:14

[initial my surprise it turns out I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m21s)
00:51:21

[almost never need to do that I almost](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m23s)
00:51:23

[never find it helpful and I think it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m26s)
00:51:26

[because we're using differential](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m28s)
00:51:28

[learning rates the the optimizer can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m29s)
00:51:29

[kind of learn just as much as it needs](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m33s)
00:51:33

[to so yeah it's a little data like very](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m35s)
00:51:35

[little data yeah it still doesn't seem](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m45s)
00:51:45

[to help the one place I have found it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m49s)
00:51:49

[helpful is if I'm using like a really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m51s)
00:51:51

[big memory intensive model and I'm like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m54s)
00:51:54

[running out of GPU crazy having the the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h51m56s)
00:51:56

[less layers you unfreeze the less memory](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m01s)
00:52:01

[it takes and the less time it takes so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m03s)
00:52:03

[there's that kind of practical aspect so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m05s)
00:52:05

[to me she'll say I asked the question](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m07s)
00:52:07

[right can I just like unfreezes specific](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m09s)
00:52:09

[layer no you you can only unfreeze](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m13s)
00:52:13

[layers from layer n onwards you could](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m16s)
00:52:16

[probably delve inside the library in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m21s)
00:52:21

[phase one phase one layer but I don't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m23s)
00:52:23

[know why you would](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m24s)
00:52:24

[okay so I'm really excited to be showing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m28s)
00:52:28

[you guys this stuff because it's like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m30s)
00:52:30

[it's something we've been kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m31s)
00:52:31

[researching all year it's figuring out](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m32s)
00:52:32

[how to train state of the art models and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m34s)
00:52:34

[we've kind of found these like tiny](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m37s)
00:52:37

[number of tricks and so once we do that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m39s)
00:52:39

[we now go learn about fit right and you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m41s)
00:52:41

[can see look at this we get right up to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m45s)
00:52:45

[that 99.5% accuracy which is crazy](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m46s)
00:52:46

[there's one other trick you might see](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m51s)
00:52:51

[here that as well as using stochastic](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m54s)
00:52:54

[gradient descent with restarts a cycle](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m55s)
00:52:55

[length equals one we've done three](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h52m58s)
00:52:58

[cycles so earlier on I lied to you I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m00s)
00:53:00

[said this is this is the number of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m04s)
00:53:04

[epochs it's actually the number of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m05s)
00:53:05

[cyclists right so if you said cycle](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m07s)
00:53:07

[length equals two it would do three](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m09s)
00:53:09

[cycles of each of two epochs or do six](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m11s)
00:53:11

[because so here I've said two three](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m14s)
00:53:14

[cycles yet somehow it's done seven](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m17s)
00:53:17

[epochs and the reason why is I've got](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m19s)
00:53:19

[one last trick to show you which is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m22s)
00:53:22

[cycle mult equals two and to tell you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m23s)
00:53:23

[what that does I'm simply going to draw](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m26s)
00:53:26

[you a picture you the picture if I go](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m27s)
00:53:27

[learn Dutch share top plot learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m30s)
00:53:30

[there it is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m32s)
00:53:32

[now you can see what cycle mode equals](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m34s)
00:53:34

[to is doing okay it's it's doubling the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m36s)
00:53:36

[length of the cycle after each cycle and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m40s)
00:53:40

[so in the paper that introduced this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m42s)
00:53:42

[stochastic gradient descent with](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m44s)
00:53:44

[restarts](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m46s)
00:53:46

[the researcher kind of said hey this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m46s)
00:53:46

[something that seems to sometimes work](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m49s)
00:53:49

[pretty well and I've certainly found](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m51s)
00:53:51

[that often to be the case so basically](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m53s)
00:53:53

[intuitively speaking if your cycle](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h53m57s)
00:53:57

[length is too short right then it's kind](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m00s)
00:54:00

[of starts going down to find a good spot](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m04s)
00:54:04

[and then it pops out and it goes to a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m06s)
00:54:06

[try and photographs button pops out it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m08s)
00:54:08

[never actually gets to find a good spot](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m09s)
00:54:09

[right so earlier on you want it to do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m11s)
00:54:11

[that because it's trying to find the bit](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m14s)
00:54:14

[that's like smoother but then later on](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m16s)
00:54:16

[you want it to fight do more exploring](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m18s)
00:54:18

[and then more exploring right so that's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m20s)
00:54:20

[why this cycle mole equals two thing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m22s)
00:54:22

[often seems to be a pretty good approach](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m26s)
00:54:26

[right so suddenly we're introducing more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m28s)
00:54:28

[and more hyper parameters having told](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m32s)
00:54:32

[you that there aren't that many but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m34s)
00:54:34

[the reason is that like you can really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m36s)
00:54:36

[get away with just taking a good](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m38s)
00:54:38

[learning rate but then adding these](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m40s)
00:54:40

[extra tweaks really helps get that extra](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m42s)
00:54:42

[level up without any effort right and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m47s)
00:54:47

[in practice I find this kind of three](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m50s)
00:54:50

[cycles starting at 1 mode equals 2 works](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m55s)
00:54:55

[very very often to get a pretty decent](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h54m59s)
00:54:59

[model if it does doesn't then often I'll](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m02s)
00:55:02

[just do 3 cycles of length 2 with no](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m07s)
00:55:07

[molt](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m10s)
00:55:10

[okay there's kind of like two things](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m11s)
00:55:11

[that seem to work a lot and there's not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m12s)
00:55:12

[too much fiddling I find necessary and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m14s)
00:55:14

[as I say even even if you just if you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m17s)
00:55:17

[use this line every time I'd be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m19s)
00:55:19

[surprised if you didn't get a reasonable](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m21s)
00:55:21

[result so a question here why does a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m23s)
00:55:23

[smoother services correlate to more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m29s)
00:55:29

[generalize networks so it's kind of this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m32s)
00:55:32

[some this intuitive explanation I try to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m40s)
00:55:40

[just kill the whole thing I try to give](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m44s)
00:55:44

[back here which is that if you've got](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m46s)
00:55:46

[something spiky right and so what this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m51s)
00:55:51

[what this x-axis is showing is like how](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h55m58s)
00:55:58

[how good is this at recognizing dogs](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m02s)
00:56:02

[versus cats as you change this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m05s)
00:56:05

[particular parameter right and so so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m06s)
00:56:06

[something to be generalizable that means](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m10s)
00:56:10

[that we wanted to work when we give it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m12s)
00:56:12

[when we give it a slightly different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m14s)
00:56:14

[data set and so a slightly different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m15s)
00:56:15

[data set may have a slightly different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m17s)
00:56:17

[relationship between this parameter and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m20s)
00:56:20

[how caddy versus dog it is it may](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m22s)
00:56:22

[instead look a little bit like this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m25s)
00:56:25

[right so in other words if we end up at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m30s)
00:56:30

[this point right then it's not going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m33s)
00:56:33

[do a good job on this slightly different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m37s)
00:56:37

[data set for else if we end up on this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m38s)
00:56:38

[point it's still going to do a good job](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m40s)
00:56:40

[on this data set](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m42s)
00:56:42

[okay so that's what psychomotor equals](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m49s)
00:56:49

[doing okay so we've got one last thing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m52s)
00:56:52

[before we going to take a break which is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m54s)
00:56:54

[we're now going to take this model which](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m55s)
00:56:55

[has 99.5 percent accuracy and we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h56m58s)
00:56:58

[going to try and make it better still](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m01s)
00:57:01

[and what we're going to do is we're not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m02s)
00:57:02

[actually going to change the model at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m05s)
00:57:05

[all right but instead we're going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m06s)
00:57:06

[look back at the original virtual](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m08s)
00:57:08

[visualization we did where we looked at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m13s)
00:57:13

[some of our incorrect pictures now what](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m15s)
00:57:15

[I've done is I've printed out the whole](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m22s)
00:57:22

[of these incorrect pictures but the key](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m24s)
00:57:24

[thing to realize is that particularly in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m26s)
00:57:26

[fact when we do the the validation set](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m30s)
00:57:30

[all of our inputs to our model all the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m34s)
00:57:34

[time have to be square right and the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m37s)
00:57:37

[reason for that is it's kind of a minor](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m40s)
00:57:40

[technical detail but basically the GPU](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m43s)
00:57:43

[doesn't go very quickly if you have like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m45s)
00:57:45

[different dimensions for different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m48s)
00:57:48

[images because it needs seems to be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m50s)
00:57:50

[consistent so that every part of the GPU](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m51s)
00:57:51

[can do the same thing and I think this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m53s)
00:57:53

[is probably fixable but it now that's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m55s)
00:57:55

[the state of the technology we have so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m57s)
00:57:57

[our validation set when we actually say](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h57m59s)
00:57:59

[for this particular thing is it's a dog](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m01s)
00:58:01

[what we actually do to make it square as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m03s)
00:58:03

[we just pick out the square in the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m05s)
00:58:05

[middle right so we would take off its](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m08s)
00:58:08

[two edges and so we take the whole](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m10s)
00:58:10

[height and then as much of the middle as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m12s)
00:58:12

[we can and so you can see in this case](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m15s)
00:58:15

[we wouldn't actually see this dog's head](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m16s)
00:58:16

[right so I think the reason this was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m19s)
00:58:19

[actually not correctly classified was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m21s)
00:58:21

[because the validation set only got to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m24s)
00:58:24

[see the body and the body doesn't look](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m26s)
00:58:26

[particularly doglike or cat-like it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m29s)
00:58:29

[not at all punctual what it is so what](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m31s)
00:58:31

[we're going to do when we calculate the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m35s)
00:58:35

[predictions for our validation set is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m38s)
00:58:38

[we're going to use something called test](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m39s)
00:58:39

[time augmentation and what this means is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m40s)
00:58:40

[that every time we decide is this cat or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m43s)
00:58:43

[a dog not in the training but after](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m46s)
00:58:46

[we've trained the model is we're going](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m48s)
00:58:48

[to actually take four random data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m50s)
00:58:50

[augmentations and remember the data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m56s)
00:58:56

[augmentations move around](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h58m58s)
00:58:58

[and zoom in and out and flip okay](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m00s)
00:59:00

[so we're going to take four of them at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m03s)
00:59:03

[random and we're going to take the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m04s)
00:59:04

[original and augmented sent a cropped](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m06s)
00:59:06

[image and we're going to do a prediction](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m09s)
00:59:09

[for all of those and then we're going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m11s)
00:59:11

[take the average of those predictions so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m13s)
00:59:13

[I'm going to say is this a cat is this a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m16s)
00:59:16

[cat is this a cat is this a cat but and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m18s)
00:59:18

[so hopefully in one of those random ones](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m21s)
00:59:21

[we actually make sure that the face is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m24s)
00:59:24

[there zoomed in by a similar amount to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m26s)
00:59:26

[other dogs faces at sea and it's rotated](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m28s)
00:59:28

[by the amount that it expects to see it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m30s)
00:59:30

[and so forth and so do that all we have](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m31s)
00:59:31

[to do is just call tt8](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m36s)
00:59:36

[TTA stands for Test time augmentation](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m38s)
00:59:38

[this term of like what a what do we call](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m41s)
00:59:41

[up when we're making predictions from up](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m43s)
00:59:43

[from a model we've trained sometimes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m45s)
00:59:45

[it's called inference time sometimes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m47s)
00:59:47

[it's called test time everybody since](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m48s)
00:59:48

[have a different name so TTA and so when](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m50s)
00:59:50

[we do that we go learn TTA check the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m53s)
00:59:53

[accuracy and lo and behold](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m55s)
00:59:55

[we're now at ninety nine point six five](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m57s)
00:59:57

[percent which is kind of crazy where's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=00h59m59s)
00:59:59

[our green box but for every park we are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m01s)
01:00:01

[only showing one type of augmentation or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m07s)
01:00:07

[for particular image right so when we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m11s)
01:00:11

[are training back here we're not doing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m13s)
01:00:13

[any TTA right so TTA is not like you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m16s)
01:00:16

[could and sometimes like I've written](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m20s)
01:00:20

[libraries where after a cheap up I run](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m22s)
01:00:22

[TTA to see how well it's going but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m24s)
01:00:24

[that's not what's happening here I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m26s)
01:00:26

[trained the whole thing with training](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m27s)
01:00:27

[time organization which doesn't have a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m31s)
01:00:31

[special name because that's what we mean](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m33s)
01:00:33

[when we say data augmentation we need](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m34s)
01:00:34

[training time augmentation so here every](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m36s)
01:00:36

[time we showed a picture](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m38s)
01:00:38

[we were randomly changing it a little](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m39s)
01:00:39

[bit so each epoch each of these seven](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m41s)
01:00:41

[epochs it was seen slightly different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m43s)
01:00:43

[versions of the picture having done that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m45s)
01:00:45

[we now have a fully trained model we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m47s)
01:00:47

[then said okay let's look at the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m50s)
01:00:50

[validation set so TTA by default uses](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m52s)
01:00:52

[the validation set and said okay what](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m54s)
01:00:54

[are your predictions of which ones are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m56s)
01:00:56

[cats and which ones are dogs and it did](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m57s)
01:00:57

[4 predictions with different random](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h00m59s)
01:00:59

[orientations plus one on the organ under](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m02s)
01:01:02

[Augmented version average them all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m04s)
01:01:04

[together and that's what we got and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m06s)
01:01:06

[that's what we can't clear the accurate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m07s)
01:01:07

[so is there a high probability of having](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m10s)
01:01:10

[sample in TTA that was not shown in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m12s)
01:01:12

[doing trained yeah actually every data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m15s)
01:01:15

[augmented for image is is unique because](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m19s)
01:01:19

[the rotation could be like point zero](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m22s)
01:01:22

[three four degrees and zoom could be 1.0](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m24s)
01:01:24

[one sixty five so every time it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m28s)
01:01:28

[slightly different no problem](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m30s)
01:01:30

[was behind you what's your might not use](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m32s)
01:01:32

[white padding or something like that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m39s)
01:01:39

[just one of your white padding like just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m40s)
01:01:40

[you know put like a white water around](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m44s)
01:01:44

[oh padding's not yes so like there's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m46s)
01:01:46

[lots of different types of a better](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m48s)
01:01:48

[orientation you can do and so one of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m50s)
01:01:50

[things you can do is to add a border](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m52s)
01:01:52

[around it basically adding a border](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m54s)
01:01:54

[around it in my experiments doesn't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m57s)
01:01:57

[doesn't help it doesn't make it any less](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h01m58s)
01:01:58

[cat-like it's not the convolutional](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m00s)
01:02:00

[neural network doesn't seem to find it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m03s)
01:02:03

[very interesting basically something](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m04s)
01:02:04

[that I do do we'll see later is I do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m07s)
01:02:07

[something called reflection padding](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m08s)
01:02:08

[which is where I add some borders that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m10s)
01:02:10

[are the outside just reflected it's a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m12s)
01:02:12

[way to kind of make some bigger images](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m15s)
01:02:15

[works well with satellite imagery in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m16s)
01:02:16

[particular but yeah in general I don't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m18s)
01:02:18

[do I have a lot of padding instead I do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m21s)
01:02:21

[a bit of zooming](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m23s)
01:02:23

[it's kind of follow-up to that last one](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m28s)
01:02:28

[but rather than cropping just at white](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m30s)
01:02:30

[space because when you crop you lose the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m33s)
01:02:33

[dog's face but if you added white space](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m35s)
01:02:35

[you wouldn't yeah so that's that's where](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m37s)
01:02:37

[the kind of the reflection padding or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m40s)
01:02:40

[the zooming or whatever can help so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m43s)
01:02:43

[there are ways in the faster you know](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m44s)
01:02:44

[library when you do custom transforms of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m46s)
01:02:46

[of making that happen I find that it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m48s)
01:02:48

[kind of depends on the image size you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h02m58s)
01:02:58

[know but generally speaking it seems](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m00s)
01:03:00

[that using TTA plus data augmentation](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m03s)
01:03:03

[the best thing to do is to try to use](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m06s)
01:03:06

[this larger image as possible and so if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m08s)
01:03:08

[you kind of crop the thing down and put](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m10s)
01:03:10

[white borders on top and bottom it's now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m11s)
01:03:11

[quite a lot smaller and so to make it as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m13s)
01:03:13

[big as it was before you now have to use](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m16s)
01:03:16

[more GPU and if you're going to use more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m18s)
01:03:18

[that multi figure you could have zoomed](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m20s)
01:03:20

[in and used a bigger image so in my](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m21s)
01:03:21

[playing around that doesn't seem to be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m24s)
01:03:24

[generally as successful there is a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m25s)
01:03:25

[little interest on the topic of how do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m36s)
01:03:36

[the domain tation in older than images](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m38s)
01:03:38

[indeed at least not images um yeah um no](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m41s)
01:03:41

[one seems to know I actually um I asked](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m47s)
01:03:47

[some of my friends in the natural](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m53s)
01:03:53

[language processing community about this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m54s)
01:03:54

[we'll get to natural language processing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m55s)
01:03:55

[in a couple of lessons you know it seems](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m57s)
01:03:57

[like it'd be really helpful there's been](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h03m59s)
01:03:59

[a few example I carry very few number](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m01s)
01:04:01

[examples of people where papers would](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m04s)
01:04:04

[like try replacing synonyms for instance](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m06s)
01:04:06

[but on the whole and understanding of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m08s)
01:04:08

[like appropriate data augmentation for](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m10s)
01:04:10

[non image domains is under-researched in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m12s)
01:04:12

[under under developed the question was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m16s)
01:04:16

[could couldn't we just use a sliding](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m24s)
01:04:24

[window to generate on the images so in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m26s)
01:04:26

[that dog thank you couldn't we generate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m28s)
01:04:28

[three parts of it wouldn't that be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m30s)
01:04:30

[better](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m33s)
01:04:33

[yeah PTI you mean just just in general](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m34s)
01:04:34

[when you're creating your so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m37s)
01:04:37

[training time I would say no that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m40s)
01:04:40

[wouldn't be better because we're not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m42s)
01:04:42

[gonna get as much variation you know we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m43s)
01:04:43

[want to have it like like one degree off](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m45s)
01:04:45

[five you know five degrees off ten](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m48s)
01:04:48

[pixels up like lots of slightly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m49s)
01:04:49

[different versions and so if you just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m51s)
01:04:51

[have three standard ways then you're not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m52s)
01:04:52

[giving it as many different ways of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m56s)
01:04:56

[looking at the data for testing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h04m58s)
01:04:58

[augmentation having fixed cropped](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m00s)
01:05:00

[locations I think probably would be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m03s)
01:05:03

[better and I just haven't gotten around](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m07s)
01:05:07

[to writing that yet I have a version in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m09s)
01:05:09

[an old library I think having fixed](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m12s)
01:05:12

[cropped locations plus random contrast](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m13s)
01:05:13

[brightness rotation changes might be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m19s)
01:05:19

[better](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m21s)
01:05:21

[the reason I've got around to it yet is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m23s)
01:05:23

[because in my testing it didn't seem to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m25s)
01:05:25

[help him practice very much and it made](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m27s)
01:05:27

[the code a lot more complicated so you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m29s)
01:05:29

[know it's kind of it's an interesting](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m31s)
01:05:31

[question](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m32s)
01:05:32

[I just wanted all of this last AI api's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m34s)
01:05:34

[that you are using is it yeah that's a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m39s)
01:05:39

[great question](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m44s)
01:05:44

[so the faster you go libraries open](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m45s)
01:05:45

[source and let's talk about it a bit](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m47s)
01:05:47

[more generally because you know it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m48s)
01:05:48

[like the fact that the fact that we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m52s)
01:05:52

[using this library is kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m55s)
01:05:55

[interesting and unusual and it sits on](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m56s)
01:05:56

[top of something called a torch right so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h05m59s)
01:05:59

[pi torch is a fairly recent development](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m02s)
01:06:02

[and it's kind of I've noticed all the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m08s)
01:06:08

[researchers that I respect pretty much](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m11s)
01:06:11

[are now using high torch I found in part](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m13s)
01:06:13

[two of last year's course that a lot of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m16s)
01:06:16

[the cutting-edge stuff I wanted to teach](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m18s)
01:06:18

[I couldn't do it in chaos and tensorflow](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m20s)
01:06:20

[which is what we used to teach with and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m23s)
01:06:23

[so I had to switch the course to pay](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m26s)
01:06:26

[torch halfway through part two the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m29s)
01:06:29

[problem was that PI torch isn't very](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m31s)
01:06:31

[easy to use you have to write your own](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m35s)
01:06:35

[training loop from scratch I basically](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m37s)
01:06:37

[write everything from scratch or the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m38s)
01:06:38

[stuff you see inside the class they are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m40s)
01:06:40

[library we would have had to written it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m41s)
01:06:41

[you know to learn and so it really makes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m43s)
01:06:43

[it very hard to learn deep learning when](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m47s)
01:06:47

[you have to write hundreds of lines of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m49s)
01:06:49

[code to do anything so so we decided to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m50s)
01:06:50

[create a library on top of Pi torch](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m55s)
01:06:55

[because we you know this our mission is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h06m57s)
01:06:57

[to teach world class big morning so we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m00s)
01:07:00

[wanted to show you like here's how you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m03s)
01:07:03

[can be the best in the world at doing it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m04s)
01:07:04

[and we found that a lot of the world](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m06s)
01:07:06

[class stuff we needed to show really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m09s)
01:07:09

[needed PI torch or at least with PI](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m12s)
01:07:12

[torch it was far easier and but then PI](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m13s)
01:07:13

[thought itself just wasn't suitable as a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m16s)
01:07:16

[first thing to teach with for new for](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m19s)
01:07:19

[new deep learning practitioners so we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m23s)
01:07:23

[built this library on up of PI torch](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m25s)
01:07:25

[initially heavily influenced by chaos](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m28s)
01:07:28

[which is what we taught last year and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m31s)
01:07:31

[but then we realized we could actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m32s)
01:07:32

[make things much much much easier than](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m34s)
01:07:34

[care us so in care us if you look back](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m36s)
01:07:36

[at last year's course notes you'll find](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m38s)
01:07:38

[that all of the code is two to three](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m41s)
01:07:41

[times longer and there's lots more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m43s)
01:07:43

[opportunities for](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m45s)
01:07:45

[stakes because there's just a lot of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m47s)
01:07:47

[things you have to get right so we ended](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m48s)
01:07:48

[up kind of building this this this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m52s)
01:07:52

[library in order to make it easier to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m54s)
01:07:54

[get into deep learning but also easier](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h07m57s)
01:07:57

[to get state-of-the-art results and then](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m00s)
01:08:00

[over the last year as we started](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m03s)
01:08:03

[developing on top of that we started](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m04s)
01:08:04

[discovering that by using this library](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m06s)
01:08:06

[it made us so much more productive that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m09s)
01:08:09

[we actually started kind of developing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m12s)
01:08:12

[you state-of-the-art results and new](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m14s)
01:08:14

[methods ourselves and we started](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m15s)
01:08:15

[realizing that there's a whole bunch of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m17s)
01:08:17

[like papers that have kind of been](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m19s)
01:08:19

[ignored or lost which when you use them](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m21s)
01:08:21

[it could like automate or semi-automated](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m23s)
01:08:23

[stuff like learning read finder that's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m26s)
01:08:26

[not in any other library so so it kind](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m28s)
01:08:28

[of got to the point where now not only](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m31s)
01:08:31

[is kind of fast AI lets us do things](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m33s)
01:08:33

[easier much easier than any other](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m36s)
01:08:36

[approach but at the same time it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m38s)
01:08:38

[actually has a lot more kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m41s)
01:08:41

[sophisticated stuff behind the scenes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m44s)
01:08:44

[than anything else so so it's kind of an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m46s)
01:08:46

[interesting mix so yeah so we've](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m48s)
01:08:48

[released this library like at this stage](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m52s)
01:08:52

[it's like very early version and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m54s)
01:08:54

[through this course by the end of this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m57s)
01:08:57

[course I hope as a group you know we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h08m58s)
01:08:58

[will all a lot of people are already](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m00s)
01:09:00

[helping have developed it into something](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m02s)
01:09:02

[that's you know really pretty stable and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m04s)
01:09:04

[rock-solid and yeah anybody can then can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m08s)
01:09:08

[use it to build your own models under an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m12s)
01:09:12

[open-source license as you can see it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m16s)
01:09:16

[available on github behind the scenes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m18s)
01:09:18

[it's it's creating play torch models and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m23s)
01:09:23

[so apply torch models can then be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m26s)
01:09:26

[exported into various different formats](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m29s)
01:09:29

[having said that like a lot of folks](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m33s)
01:09:33

[like issue if you want to do something](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m35s)
01:09:35

[on a mobile phone for example you're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m36s)
01:09:36

[probably going to need to use tensorflow](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m38s)
01:09:38

[and so later on in this course we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m40s)
01:09:40

[going to show like how some of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m44s)
01:09:44

[things that we're doing in the past AI](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m46s)
01:09:46

[library you can do in chaos and cancel](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m47s)
01:09:47

[flow so you can going to get a sense of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m50s)
01:09:50

[what the different libraries look like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m51s)
01:09:51

[and generally speaking the simple stuff](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m53s)
01:09:53

[is like it'll take you a small number of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m56s)
01:09:56

[days](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h09m59s)
01:09:59

[to learn to do it and care us in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m00s)
01:10:00

[tensorflow versus fast AI and high torch](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m02s)
01:10:02

[and the more complex stuff often this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m04s)
01:10:04

[won't be possible so that like if you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m08s)
01:10:08

[needed to be intensive flow you're just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m09s)
01:10:09

[kind of simplify it off in a little bit](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m12s)
01:10:12

[but you know I think the more important](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m17s)
01:10:17

[thing to realize is every year the kind](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m19s)
01:10:19

[of the libraries that are available and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m24s)
01:10:24

[which ones are the best totally changes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m26s)
01:10:26

[so like the main thing I hope that you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m28s)
01:10:28

[get out of this course is an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m30s)
01:10:30

[understanding of the concepts like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m31s)
01:10:31

[here's how you find a learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m33s)
01:10:33

[here's why differential learning rates](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m34s)
01:10:34

[are important is they do learn where the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m36s)
01:10:36

[kneeling you know here's what stochastic](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m38s)
01:10:38

[gradient a second's restarts does so on](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m40s)
01:10:40

[and so forth because you know by the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m42s)
01:10:42

[time we do this course again next year](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m45s)
01:10:45

[you know the library situations and the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m47s)
01:10:47

[difference the king that's a question of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m52s)
01:10:52

[that I was wondering if you've had an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h10m55s)
01:10:55

[opinion on pyro which is ubers new](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m05s)
01:11:05

[release I haven't looked at it no I'm](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m08s)
01:11:08

[very interested in probabilistic](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m10s)
01:11:10

[programming and it's really cool that's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m11s)
01:11:11

[built on top of paper so one of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m14s)
01:11:14

[things we'll learn about in this course](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m15s)
01:11:15

[is we'll see that PI torch is much more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m17s)
01:11:17

[than just a deep learning library it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m19s)
01:11:19

[actually lets us write arbitrary](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m20s)
01:11:20

[gpu-accelerated algorithms from scratch](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m24s)
01:11:24

[which we're actually going to do and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m28s)
01:11:28

[pyro is a great example of what people](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m29s)
01:11:29

[are now doing with might watch outside](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m31s)
01:11:31

[of the deep level great ok let's take a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m33s)
01:11:33

[eight-minute break and we'll come back](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m38s)
01:11:38

[at 7:55 so ninety nine point six five](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m40s)
01:11:40

[percent accuracy what does that mean so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m52s)
01:11:52

[in classification when we do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m56s)
01:11:56

[classification and machine learning the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h11m59s)
01:11:59

[really simple way to look at the result](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m01s)
01:12:01

[of a classification is what's called the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m04s)
01:12:04

[confusion matrix this is not just deep](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m05s)
01:12:05

[learning but in any kind of classifier](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m07s)
01:12:07

[machine learning where we say okay what](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m09s)
01:12:09

[was the actual truth there were](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m12s)
01:12:12

[thousand cats and a thousand dogs out of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m14s)
01:12:14

[the thousand actual cats how many did we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m17s)
01:12:17

[predict were cats this is obviously in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m20s)
01:12:20

[the validation step this is the images](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m22s)
01:12:22

[that we didn't use to train with it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m25s)
01:12:25

[turns out there were nine hundred](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m27s)
01:12:27

[ninety-eight cats that we actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m28s)
01:12:28

[predicted as cats and two that we got](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m29s)
01:12:29

[wrong](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m32s)
01:12:32

[okay and then for dogs there were nine](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m32s)
01:12:32

[hundred ninety-five that we predicted](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m35s)
01:12:35

[were dogs and then five that we got](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m36s)
01:12:36

[wrong and so often these confusion](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m38s)
01:12:38

[matrices can be helpful particularly if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m41s)
01:12:41

[you've got like four or five classes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m42s)
01:12:42

[you're trying to predict to see like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m44s)
01:12:44

[which group you having the most trouble](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m46s)
01:12:46

[with and you can see it uses color](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m48s)
01:12:48

[coding to tell you you know to highlight](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m49s)
01:12:49

[the large the large bits you've got to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m52s)
01:12:52

[hope that the diagonal is the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m55s)
01:12:55

[highlighted section so now that we've](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h12m57s)
01:12:57

[retrained the model it can be quite](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m01s)
01:13:01

[helpful now that's better to actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m02s)
01:13:02

[look back and see like okay which ones](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m04s)
01:13:04

[in particular were incorrect and we can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m07s)
01:13:07

[see here there were actually only two](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m09s)
01:13:09

[incorrect cats it prints out four by](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m12s)
01:13:12

[default so you can actually see these](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m15s)
01:13:15

[two actually less than 0.5 so they](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m16s)
01:13:16

[weren't they weren't wrong okay so it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m19s)
01:13:19

[actually these two were wrong cats and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m21s)
01:13:21

[this one isn't obviously a cat at all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m23s)
01:13:23

[this one is but it looks like it's got a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m26s)
01:13:26

[lot of weird artifacts and you can't see](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m28s)
01:13:28

[its eyeballs at all so and then here are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m31s)
01:13:31

[the how many dogs where they're all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m34s)
01:13:34

[wrong there were five wrong dogs here](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m36s)
01:13:36

[are four of them that's not obviously a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m38s)
01:13:38

[dog that looks like a mistake that looks](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m40s)
01:13:40

[like a mistake that one I guess doesn't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m44s)
01:13:44

[have enough information that I guess](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m46s)
01:13:46

[it's a mistake so so we've done a pretty](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m47s)
01:13:47

[good job here of creating a good](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m51s)
01:13:51

[classifier I would based on entering a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m53s)
01:13:53

[lot of capital competitions and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m57s)
01:13:57

[comparing results I've done two various](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h13m59s)
01:13:59

[research papers I can tell you it's a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m00s)
01:14:00

[state of the art classifier it's it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m02s)
01:14:02

[right up there with the best in the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m05s)
01:14:05

[world we're going to make it a little](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m06s)
01:14:06

[bit better in a moment but here in the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m08s)
01:14:08

[basic steps right so if you want to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m09s)
01:14:09

[create a world-class image classifier](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m11s)
01:14:11

[the steps that we just went through was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m14s)
01:14:14

[that we started our week's term data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m16s)
01:14:16

[augmentation on by saying oil transforms](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m18s)
01:14:18

[equals and you either say sidon or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m21s)
01:14:21

[top-down depending on what you're doing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m22s)
01:14:22

[start with pre compute equals true find](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m24s)
01:14:24

[a decent learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m27s)
01:14:27

[eight we then train just like it one or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m28s)
01:14:28

[two epochs which that takes a few](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m31s)
01:14:31

[seconds as we got through compute equals](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m33s)
01:14:33

[true then we turn off pre compute which](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m34s)
01:14:34

[allows us to use data augmentation to do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m37s)
01:14:37

[another two or three epochs generally](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m40s)
01:14:40

[with cycle length equals one then I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m43s)
01:14:43

[unfreeze all them as I then set the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m45s)
01:14:45

[earlier layers to be like either](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m48s)
01:14:48

[somewhere between a 3 times 2 10 times](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m50s)
01:14:50

[mobile learning rate in the previous so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m52s)
01:14:52

[in this case I did 10 times right so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h14m54s)
01:14:54

[it's like this was my learning rate that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m01s)
01:15:01

[I found from the learning rate finer](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m03s)
01:15:03

[than I went 10 times smaller and then 10](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m04s)
01:15:04

[times smaller as a rule of thumb like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m06s)
01:15:06

[knowing that you're starting with a pre](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m08s)
01:15:08

[trained imagenet model if you know if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m11s)
01:15:11

[you can see that the things that you're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m13s)
01:15:13

[now trying to classify a pretty similar](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m15s)
01:15:15

[the kinds of things in imagenet ie](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m17s)
01:15:17

[pictures of normal objects in normal](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m18s)
01:15:18

[environments](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m21s)
01:15:21

[you probably want about a 10x difference](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m21s)
01:15:21

[because you want those earlier layers](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m24s)
01:15:24

[like you think that the earlier layers](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m26s)
01:15:26

[are probably very good already but also](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m27s)
01:15:27

[if you're doing something like satellite](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m30s)
01:15:30

[imagery or medical imaging which is not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m31s)
01:15:31

[at all like image net then you probably](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m34s)
01:15:34

[want to be training those earlier layers](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m36s)
01:15:36

[a lot more so you might have like oh](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m37s)
01:15:37

[just a 3/8 difference all right so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m39s)
01:15:39

[that's like one change that I make is to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m42s)
01:15:42

[try to make it out of 10x or 3x yes so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m45s)
01:15:45

[then after unfreezing you can now call](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m52s)
01:15:52

[LR find again but at Nike didn't in this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m56s)
01:15:56

[case but like once you've unfrozen all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h15m59s)
01:15:59

[the layers you've turned on differential](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m01s)
01:16:01

[learning rates you can then call a lot](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m03s)
01:16:03

[of fine again right and so you can then](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m05s)
01:16:05

[check like oh does it still look like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m10s)
01:16:10

[the same point I had last time is about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m12s)
01:16:12

[right something to note is that if you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m13s)
01:16:13

[call LR find having set differential](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m16s)
01:16:16

[learning rates the thing that's actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m20s)
01:16:20

[going to print out is the learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m21s)
01:16:21

[of the last layers right because you've](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m23s)
01:16:23

[got three different learning rates so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m25s)
01:16:25

[it's actually showing you the last layer](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m27s)
01:16:27

[so then yeah then I trained the full](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m28s)
01:16:28

[network with cycle more equals two and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m31s)
01:16:31

[it'll either it starts with the fitting](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m33s)
01:16:33

[or I run out of time right so like let](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m35s)
01:16:35

[me show you all right so let's do this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m38s)
01:16:38

[again](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m40s)
01:16:40

[a totally different data set so this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m41s)
01:16:41

[morning I noticed that some of you on](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m43s)
01:16:43

[the forums were playing around with this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m45s)
01:16:45

[playground Kegel competition very](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m47s)
01:16:47

[similar called dog breed identification](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m49s)
01:16:49

[so the dog breed identification cat will](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m53s)
01:16:53

[challenge is one where you don't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m56s)
01:16:56

[actually have to decide which ones are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h16m59s)
01:16:59

[cats and which ones the dogs they're all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m01s)
01:17:01

[dogs but you have to decide what kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m02s)
01:17:02

[dog it is but there are 120 different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m05s)
01:17:05

[breeds of dogs okay](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m07s)
01:17:07

[so you know obviously this could be like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m10s)
01:17:10

[different types of cells and pathology](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m14s)
01:17:14

[slides it could be different kinds of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m18s)
01:17:18

[cancers in CT scans it could be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m20s)
01:17:20

[different kinds of icebergs and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m23s)
01:17:23

[satellite images whatever right as long](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m25s)
01:17:25

[as you've got some kind of labeled](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m28s)
01:17:28

[images so I want to show you what I did](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m29s)
01:17:29

[this morning so it took me about an hour](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m33s)
01:17:33

[basically to go in to end from something](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m34s)
01:17:34

[I'd never seen before so I downloaded](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m38s)
01:17:38

[the data from kaggle and I'll show you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m42s)
01:17:42

[how to do that shortly but the short](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m43s)
01:17:43

[answer is there's something called cable](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m45s)
01:17:45

[CLI which is a github project you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m47s)
01:17:47

[search for and if you read the docs to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m49s)
01:17:49

[basically run cagey download provide the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m51s)
01:17:51

[competition name and it will grab all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m54s)
01:17:54

[the data for you to your crystal or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m55s)
01:17:55

[Amazon or whatever instance I put in my](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h17m57s)
01:17:57

[data folder and I then went LS and I saw](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m01s)
01:18:01

[that it's a little bit different to our](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m07s)
01:18:07

[previous data set it's not that there's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m12s)
01:18:12

[a train folder which has a separate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m14s)
01:18:14

[folder for each kind of dog but instead](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m17s)
01:18:17

[of tonette there was a CSV file and the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m20s)
01:18:20

[CSV file I read it in with pandas so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m22s)
01:18:22

[pandas is the thing we use in python to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m25s)
01:18:25

[do structured data analysis like csv](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m27s)
01:18:27

[files so he picked pandas we called pd](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m30s)
01:18:30

[that's pretty much universal PDR htsb](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m33s)
01:18:33

[reads in the csv file we can then take a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m36s)
01:18:36

[look at it and you can see that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m38s)
01:18:38

[basically it had like some kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m39s)
01:18:39

[identifier and then the debris right so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m41s)
01:18:41

[this is like a different way this is the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m45s)
01:18:45

[second main way that people kind of give](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m46s)
01:18:46

[you image labels one is to put different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m49s)
01:18:49

[images into different folders](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m51s)
01:18:51

[the second is generally to give you as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m53s)
01:18:53

[some kind of file like a CSV file to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m55s)
01:18:55

[tell you here's the image name and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m57s)
01:18:57

[here's the label okay so what I then did](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h18m59s)
01:18:59

[was I used pandas again to create a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m05s)
01:19:05

[pivot table which basically groups it up](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m08s)
01:19:08

[just to see how many of each breed there](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m10s)
01:19:10

[were and I sorted them and so I saw okay](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m13s)
01:19:13

[they've got like about a hundred some of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m15s)
01:19:15

[the more common breeds and some of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m18s)
01:19:18

[less common breeds they've got like 60](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m21s)
01:19:21

[or so okay altogether there are 120 rows](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m23s)
01:19:23

[and I've been 120 different breeds](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m27s)
01:19:27

[represented okay so I'm going to go](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m28s)
01:19:28

[through the steps right so enable data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m32s)
01:19:32

[augmentation so to enable data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m35s)
01:19:35

[augmentation when we call this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m37s)
01:19:37

[transforms from model you just pass in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m39s)
01:19:39

[and all transformers in this case I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m42s)
01:19:42

[chose side on again these are pictures](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m44s)
01:19:44

[of dots and stuff so this side on photos](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m46s)
01:19:46

[I we're talking about maqsuum as more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m48s)
01:19:48

[detail later but maximum basically says](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m53s)
01:19:53

[when you do the data augmentation we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m55s)
01:19:55

[like zoom into it by up to one point one](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h19m58s)
01:19:58

[times okay so but randomly between one](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m01s)
01:20:01

[the original image size and one point](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m04s)
01:20:04

[one points so it's not always cropping](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m06s)
01:20:06

[out in the middle or an edge but it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m08s)
01:20:08

[could be cropping out a smaller part](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m11s)
01:20:11

[okay so having done that the key step](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m12s)
01:20:12

[now is to graphically going from paths](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m16s)
01:20:16

[so previously we went from paths and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m18s)
01:20:18

[that tells it that the the names of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m21s)
01:20:21

[folders are the names of the labels we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m23s)
01:20:23

[go from CSV and we pass in the CSV file](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m25s)
01:20:25

[that contains the letters so we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m29s)
01:20:29

[passing in the path that contains all of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m32s)
01:20:32

[the data the name of the folder that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m34s)
01:20:34

[contains the training data the CSV that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m37s)
01:20:37

[contains the labels we need to also tell](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m40s)
01:20:40

[it where the test set is if you want to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m43s)
01:20:43

[submit to cattle later talk more about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m45s)
01:20:45

[that next week now this time the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m47s)
01:20:47

[previous data set we had had actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m53s)
01:20:53

[separated a validation set out into a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m55s)
01:20:55

[separate folder right but in this case](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m57s)
01:20:57

[you'll see that there is not a separate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h20m59s)
01:20:59

[folder called validation right so we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m02s)
01:21:02

[want to be able to track how good our](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m05s)
01:21:05

[performance is low](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m07s)
01:21:07

[so we're going to have to separate some](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m09s)
01:21:09

[of the images out to put it into a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m10s)
01:21:10

[validation set okay so I do that at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m12s)
01:21:12

[random and so up here you can see how it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m15s)
01:21:15

[basically opened up the CSV file turned](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m18s)
01:21:18

[it into a list of rows and then taken](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m22s)
01:21:22

[the length of that minus one because](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m25s)
01:21:25

[there's a header at the top right and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m28s)
01:21:28

[that's the number of rows in the CSV](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m30s)
01:21:30

[file which must be the number of images](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m33s)
01:21:33

[that we have and then this is a fast AI](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m35s)
01:21:35

[thing get cross-validation indexes now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m37s)
01:21:37

[we'll talk about cross-validation later](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m40s)
01:21:40

[but basically if you call this and pass](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m42s)
01:21:42

[in a number it's going to return to you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m44s)
01:21:44

[by default a random twenty percent of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m48s)
01:21:48

[the rows who uses your validation set](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m52s)
01:21:52

[and you can pass in parameters to get](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m54s)
01:21:54

[different amounts right so this is now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m57s)
01:21:57

[going to grab twenty percent of the data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h21m58s)
01:21:58

[and say all right this is the this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m00s)
01:22:00

[the indexes the numbers of the files](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m03s)
01:22:03

[which we're going to use as a validation](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m05s)
01:22:05

[set](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m07s)
01:22:07

[okay so now that we've got that in fact](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m08s)
01:22:08

[let's kind of run this so you can see](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m12s)
01:22:12

[what that looks like so well indexes is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m14s)
01:22:14

[just a big bunch of numbers okay and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m19s)
01:22:19

[an is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m23s)
01:22:23

[10,000 right and so we have about twenty](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m26s)
01:22:26

[percent of those is going to be in a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m31s)
01:22:31

[validation set](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m33s)
01:22:33

[so when we call from CSV we can pass in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m34s)
01:22:34

[a parameter which is talent which](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m44s)
01:22:44

[indexes to treat us a validation set and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m46s)
01:22:46

[so that's passed in those indexes one](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m48s)
01:22:48

[thing that's a little bit tricky here is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m52s)
01:22:52

[that the file names actually have I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h22m54s)
01:22:54

[checked they actually have a dot jpg on](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m03s)
01:23:03

[the end and these obviously don't have a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m05s)
01:23:05

[dot jpg so you can pass in when you call](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m07s)
01:23:07

[from CSV you can pass in a suffix it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m11s)
01:23:11

[says that the labels don't actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m13s)
01:23:13

[contain the full file names you need to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m15s)
01:23:15

[add this to them okay so that's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m17s)
01:23:17

[basically all I need to do to set up my](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m22s)
01:23:22

[data and as a lot of Europe noticed](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m24s)
01:23:24

[during the week inside that data object](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m28s)
01:23:28

[you can actually get access to the data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m31s)
01:23:31

[set like what the training data set by](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m33s)
01:23:33

[same train yes and inside train des is a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m35s)
01:23:35

[whole bunch of things including the file](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m38s)
01:23:38

[names](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m41s)
01:23:41

[okay so train desktop file names](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m41s)
01:23:41

[contains all of the file names of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m43s)
01:23:43

[everything in the training set and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m45s)
01:23:45

[here's like one file name](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m47s)
01:23:47

[okay so here's an example of one file](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m48s)
01:23:48

[name so I can now go ahead and open that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m50s)
01:23:50

[file and take a look at it that's the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m54s)
01:23:54

[next thing I did was to try and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m56s)
01:23:56

[understand what my file my dataset looks](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m58s)
01:23:58

[like and it found an adorable puppy so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h23m59s)
01:23:59

[that was very nice](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m02s)
01:24:02

[so feeling good about this I also want](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m03s)
01:24:03

[to know like how big of these files](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m06s)
01:24:06

[right like how big are the images](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m08s)
01:24:08

[because that's a key issue if they're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m09s)
01:24:09

[huge and then I have to think really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m12s)
01:24:12

[carefully about how to deal with huge](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m13s)
01:24:13

[images that's really challenging if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m15s)
01:24:15

[they're tiny well that's also](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m17s)
01:24:17

[challenging most of imagenet models are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m19s)
01:24:19

[trained on either 224 by 224 or 299 by](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m22s)
01:24:22

[299 images so anytime you have images in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m25s)
01:24:25

[that kind of range that's that's really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m28s)
01:24:28

[hopeful you're probably not going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m31s)
01:24:31

[have to do too much different in this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m32s)
01:24:32

[case the first image I looked at was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m34s)
01:24:34

[about the right size so I'm thinking of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m36s)
01:24:36

[pretty hopeful so what I did then is I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m38s)
01:24:38

[created a dictionary comprehension now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m41s)
01:24:41

[if you don't know about list](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m42s)
01:24:42

[comprehensions and dictionary](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m44s)
01:24:44

[comprehensions in Python go study them](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m45s)
01:24:45

[they're the most useful thing super](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m48s)
01:24:48

[handy you can see the basic idea here is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m51s)
01:24:51

[that are going through all of the files](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m54s)
01:24:54

[and then putting a dictionary that map's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m55s)
01:24:55

[the name of the file to the size of that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h24m57s)
01:24:57

[file again this is a handy little Python](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m01s)
01:25:01

[feature which I'll let you think learn](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m05s)
01:25:05

[about during the week if you don't know](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m07s)
01:25:07

[about it which is zip and using a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m08s)
01:25:08

[special star notation is never to take](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m10s)
01:25:10

[this dictionary and turn it into the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m12s)
01:25:12

[rows and the columns and so I can now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m15s)
01:25:15

[turn those into num pay arrays and like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m19s)
01:25:19

[okay here are the first five rows sizes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m22s)
01:25:22

[for each of my images and then](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m26s)
01:25:26

[matplotlib is something you want to be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m28s)
01:25:28

[very familiar with if you do any kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m30s)
01:25:30

[data science or machine learning in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m32s)
01:25:32

[python matplotlib we always refer to as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m33s)
01:25:33

[PLT as if this is a histogram and so I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m36s)
01:25:36

[got a histogram of the how high how many](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m39s)
01:25:39

[rows there are in each image so you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m43s)
01:25:43

[see here I'm kind of getting a sense](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m45s)
01:25:45

[before I start doing any modeling I kind](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m46s)
01:25:46

[of need to know what I'm modeling with](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m49s)
01:25:49

[and I can see some of the images are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m50s)
01:25:50

[going to be like 2500 3000 pixels high](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m52s)
01:25:52

[but most of them seem to be around 500](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m54s)
01:25:54

[so given it so few of them were bigger](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h25m57s)
01:25:57

[than a thousand I use standard numpy](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m00s)
01:26:00

[slicing to just grab those at a smaller](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m03s)
01:26:03

[than a thousand and histogram that just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m05s)
01:26:05

[to zoom in a little bit and I can see](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m08s)
01:26:08

[here all right it looks like yet the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m10s)
01:26:10

[vast majority are around 500 and so this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m12s)
01:26:12

[actually also prints out the histogram](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m15s)
01:26:15

[so I can actually go through and I can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m17s)
01:26:17

[see here for four thousand five hundred](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m19s)
01:26:19

[of them are about 450 okay so I get](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m21s)
01:26:21

[about that seems about anywhere so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m23s)
01:26:23

[generally how many images should we get](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m28s)
01:26:28

[in the validation set is always a 20%](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m32s)
01:26:32

[so the size of the validation set like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m38s)
01:26:38

[using 20% is fine unless you kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m44s)
01:26:44

[feeling like my data is my data sets](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m48s)
01:26:48

[really small I'm not sure that's enough](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m49s)
01:26:49

[you know like if you've got basically](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m53s)
01:26:53

[think of it this way if you train like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m57s)
01:26:57

[the same model multiple times and you're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h26m59s)
01:26:59

[getting very different validation set](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m01s)
01:27:01

[results and your validation sets kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m02s)
01:27:02

[small but smaller than a thousand or so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m04s)
01:27:04

[then it's going to be quite hard to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m08s)
01:27:08

[interpret how well you're doing now this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m10s)
01:27:10

[is particularly true like if you're like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m13s)
01:27:13

[if you care about the third decimal](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m14s)
01:27:14

[place of accuracy and you've got like a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m16s)
01:27:16

[thousand things in your validation set](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m19s)
01:27:19

[then you bring about like a single image](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m21s)
01:27:21

[changing class is changing you know it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m22s)
01:27:22

[what you're looking at so it's it really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m25s)
01:27:25

[depends on my cow accurate you have much](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m28s)
01:27:28

[difference you care about I would say in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m31s)
01:27:31

[general like at the point where you care](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m35s)
01:27:35

[about difference between like out of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m37s)
01:27:37

[0.01 and 0.02 like the second decimal](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m39s)
01:27:39

[place you want that to represent like 10](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m41s)
01:27:41

[or 20 roads you know like changing the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m44s)
01:27:44

[class of that 10 or 20 rows then that's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m48s)
01:27:48

[something you can be pretty confident of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m51s)
01:27:51

[so like most of the time you know give](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m53s)
01:27:53

[them the data sizes we normally have 20](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h27m57s)
01:27:57

[percent seems to work fine but yeah it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m00s)
01:28:00

[it's it's kind of a it depends a lot on](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m04s)
01:28:04

[specifically what you're doing and what](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m07s)
01:28:07

[you care about and it's not it's not a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m09s)
01:28:09

[deep learning specific question either](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m12s)
01:28:12

[you know so those who are interested in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m15s)
01:28:15

[this kind of thing we're going to look](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m17s)
01:28:17

[into it a lot more detail in our machine](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m17s)
01:28:17

[learning course which will also be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m19s)
01:28:19

[available online ok so I did the same](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m23s)
01:28:23

[thing for the columns just to make sure](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m28s)
01:28:28

[that these aren't like super wide and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m29s)
01:28:29

[I've got similar results and checked in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m31s)
01:28:31

[and again found they're kind of like 4](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m33s)
01:28:33

[or 500 seem to be about the average size](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m35s)
01:28:35

[so based on all of that I kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m37s)
01:28:37

[thought ok this looks like a pretty](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m39s)
01:28:39

[normal kind of image data set that I can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m41s)
01:28:41

[probably use pretty normal kinds of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m43s)
01:28:43

[models on I was also particularly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m44s)
01:28:44

[encouraged to see that when I looked at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m46s)
01:28:46

[the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m48s)
01:28:48

[that the dog like takes up most of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m48s)
01:28:48

[frame right so I'm not too worried about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m51s)
01:28:51

[like cropping problems you know if the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m53s)
01:28:53

[if the dog was just like a tiny little](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m56s)
01:28:56

[piece of one little corner that I'd be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h28m57s)
01:28:57

[thinking about doing different you know](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m00s)
01:29:00

[maybe zooming in a lot more or something](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m02s)
01:29:02

[like a medical imaging that happens a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m04s)
01:29:04

[lot like often the tumor or the cell](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m07s)
01:29:07

[whatever is like one tiny piece and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m09s)
01:29:09

[there's much more complex so yeah based](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m11s)
01:29:11

[on all that and this morning I kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m14s)
01:29:14

[thought like okay this looks pretty](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m15s)
01:29:15

[standard so I I went ahead and created a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m18s)
01:29:18

[little function called get data that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m24s)
01:29:24

[basically had my normal two lines of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m26s)
01:29:26

[code in it but I made it so I could](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m28s)
01:29:28

[passed in a size and a batch size the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m31s)
01:29:31

[reason for this is that when I start](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m35s)
01:29:35

[working with new data set I want](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m37s)
01:29:37

[everything to go super fast and so if I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m38s)
01:29:38

[use small images it's going to go super](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m41s)
01:29:41

[fast so I actually started out with size](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m43s)
01:29:43

[equals 64 just to create some super](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m46s)
01:29:46

[small images that just go like a second](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m49s)
01:29:49

[to run through and see how it later on I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m51s)
01:29:51

[started using some big images and some](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m54s)
01:29:54

[and some also some bigger architectures](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m57s)
01:29:57

[at which point I started running out of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h29m59s)
01:29:59

[GPU memory so I started getting these](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m01s)
01:30:01

[errors saying CUDA out of memory error](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m02s)
01:30:02

[when you get a CUDA out of memory error](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m05s)
01:30:05

[the first thing you need to do is to go](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m08s)
01:30:08

[kernel restart once you get a code an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m10s)
01:30:10

[out of memory error on your GPU you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m13s)
01:30:13

[can't really recover from it right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m15s)
01:30:15

[doesn't matter what you do you know you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m17s)
01:30:17

[have to go restart and once I've](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m18s)
01:30:18

[restarted I then just changed my batch](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m22s)
01:30:22

[size to something smaller so when you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m24s)
01:30:24

[call create your data object you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m26s)
01:30:26

[pass in a batch size parameter okay and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m30s)
01:30:30

[like i normally use 64 until i hit](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m34s)
01:30:34

[something that says out of memory and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m37s)
01:30:37

[then i'll just have it and if i still](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m39s)
01:30:39

[get out of memory I was hobbit again](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m40s)
01:30:40

[okay so that's where I created this to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m42s)
01:30:42

[allow me to like start making my size as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m45s)
01:30:45

[bigger as I looked into it more and you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m47s)
01:30:47

[know as I started running out of memory](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m50s)
01:30:50

[to decrease my batch size so at this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m51s)
01:30:51

[point you know I went through this a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m55s)
01:30:55

[couple of iterations but I basically](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m57s)
01:30:57

[found everything was working fine so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h30m59s)
01:30:59

[once it's working fine](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m01s)
01:31:01

[set size 2 to 24 and I created my you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m02s)
01:31:02

[know pre-compute equals true first time](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m07s)
01:31:07

[I did that it took a minute to create](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m10s)
01:31:10

[the precomputed activations and then it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m11s)
01:31:11

[ran through this in about 4 or 5 seconds](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m13s)
01:31:13

[and you can see I was getting](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m15s)
01:31:15

[eighty-three percent accuracy](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m17s)
01:31:17

[now remember accuracy means it's it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m18s)
01:31:18

[exactly right and so it's predicting out](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m21s)
01:31:21

[of a hundred and twenty categories it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m24s)
01:31:24

[predicting exactly right so when you see](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m26s)
01:31:26

[something with two classes is you know](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m27s)
01:31:27

[80% accurate versus something with 120](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m30s)
01:31:30

[classes is 80% accurate they're very](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m33s)
01:31:33

[different levels you know so when I saw](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m36s)
01:31:36

[like eighty-three percent accuracy with](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m39s)
01:31:39

[just a pre computed classify and OData](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m41s)
01:31:41

[augmentation though I'm freezing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m43s)
01:31:43

[anything else](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m45s)
01:31:45

[across 120 classes of the oh this looks](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m46s)
01:31:46

[good right so um then I just kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m49s)
01:31:49

[kept going throughout at all standard](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m54s)
01:31:54

[process right so then I turn precompute](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h31m56s)
01:31:56

[off okay and cycle length equals one and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m01s)
01:32:01

[I started doing a few more cycles few](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m06s)
01:32:06

[more epochs so remember an epoch is one](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m10s)
01:32:10

[pass through the data and a cycle is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m15s)
01:32:15

[however many epochs you said is in a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m19s)
01:32:19

[cycle it's one it's the learning rate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m22s)
01:32:22

[going from the top that you asked for](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m24s)
01:32:24

[all the way down so since here cycle](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m26s)
01:32:26

[length equals one a cycle in an epoch at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m29s)
01:32:29

[the same okay so I did I tried a few](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m31s)
01:32:31

[epochs I did actually do the learning](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m35s)
01:32:35

[rate finder and I found one in a two](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m39s)
01:32:39

[again looked fine it often looks fine](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m41s)
01:32:41

[and I found it kind of kept improving so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m43s)
01:32:43

[I tried five epochs and I found my](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m46s)
01:32:46

[accuracy getting better so then I saved](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m48s)
01:32:48

[that and I tried something which we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m54s)
01:32:54

[haven't looked at before but it's kind](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m56s)
01:32:56

[of cool if you train something on a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h32m58s)
01:32:58

[smaller size you can then actually call](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m01s)
01:33:01

[learned set data and pass in a larger](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m05s)
01:33:05

[size data set and that's gonna take your](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m10s)
01:33:10

[model however it's trained so far and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m12s)
01:33:12

[it's going to let you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m14s)
01:33:14

[in you to train on on larger images and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m16s)
01:33:16

[I tell you something amazing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m20s)
01:33:20

[this actually is another way you can get](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m22s)
01:33:22

[state-of-the-art results and I've never](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m25s)
01:33:25

[seen this written in any paper or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m26s)
01:33:26

[discussed anywhere as far as I know this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m29s)
01:33:29

[is a new insight basically I've got a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m30s)
01:33:30

[pre trained model which in this case](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m34s)
01:33:34

[I've trained a few epochs with the size](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m36s)
01:33:36

[of 224 by 224 and I'm now going to do a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m38s)
01:33:38

[few more air pops with the size of 299](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m41s)
01:33:41

[by 299 now I've gotten very little data](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m43s)
01:33:43

[cut out by deep learning standards only](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m47s)
01:33:47

[about 10,000 images right so with a 224](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m49s)
01:33:49

[by 224 I kind of built this these final](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m52s)
01:33:52

[layers to try to find things that work](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m55s)
01:33:55

[well to 24 but to 24 but I go to 299 by](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h33m57s)
01:33:57

[299 I basically if I over fit before I'm](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m01s)
01:34:01

[definitely not going to over fit now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m05s)
01:34:05

[might have changed the size of my images](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m07s)
01:34:07

[they're kind of like totally different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m08s)
01:34:08

[but like conceptually they're still](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m10s)
01:34:10

[picked the same kinds of pictures are](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m13s)
01:34:13

[the same kinds of things so I found this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m14s)
01:34:14

[trick of like starting training on small](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m16s)
01:34:16

[images for a few a box and then](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m19s)
01:34:19

[switching to bigger images and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m21s)
01:34:21

[continuing training is an amazingly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m22s)
01:34:22

[effective way to avoid overfitting and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m25s)
01:34:25

[it's like it's so easy and so obvious I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m28s)
01:34:28

[don't understand why it's never been](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m32s)
01:34:32

[written about before maybe it's in some](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m34s)
01:34:34

[paper somewhere and I haven't found it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m36s)
01:34:36

[but it's I haven't seen it would it be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m37s)
01:34:37

[possible to do the same thing on using](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m44s)
01:34:44

[let's take a resort our disposal to feed](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m46s)
01:34:46

[a different size yeah I think so like as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m49s)
01:34:49

[long as you use one of these more modern](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m53s)
01:34:53

[architectures what we call fully](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m56s)
01:34:56

[convolutional architectures which means](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h34m57s)
01:34:57

[not vgg and you'll see we don't use vgg](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m00s)
01:35:00

[in this course because it doesn't have](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m02s)
01:35:02

[this property but most of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m04s)
01:35:04

[architectures developed in the last](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m06s)
01:35:06

[couple of years can handle pretty much](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m07s)
01:35:07

[arbitrary sizes yeah be worth trying](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m09s)
01:35:09

[yeah I think it ought to work okay so I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m13s)
01:35:13

[call get data again remember get data is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m18s)
01:35:18

[the just a little function that I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m20s)
01:35:20

[created back up here right get data is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m21s)
01:35:21

[just this little function that's oh I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m22s)
01:35:22

[just passed a different size to it and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m24s)
01:35:24

[so I call freeze just to make sure that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m27s)
01:35:27

[but everything so the last layer is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m31s)
01:35:31

[frozen I mean it actually already was at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m33s)
01:35:33

[its point that really doing a thing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m35s)
01:35:35

[and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m37s)
01:35:37

[you can see now with free compute off](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m42s)
01:35:42

[I've now got that data augmentation](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m44s)
01:35:44

[working so I kind of run a few more a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m46s)
01:35:46

[pox and what I notice here is that the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m48s)
01:35:48

[loss to my training set and the loss of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m51s)
01:35:51

[my validation set my validation set loss](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m54s)
01:35:54

[is a lot lower than my training set this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m56s)
01:35:56

[is still just training the last layer so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h35m58s)
01:35:58

[what this is telling me is I'm under](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m00s)
01:36:00

[fitting right and so from under fitting](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m02s)
01:36:02

[it means this cycle length equals one is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m05s)
01:36:05

[too short it means it's like finding](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m07s)
01:36:07

[something better popped with popping out](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m08s)
01:36:08

[and it's like never getting a chance to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m10s)
01:36:10

[zoom in properly so then I'd set cycle](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m12s)
01:36:12

[mod equals two to give it more time so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m15s)
01:36:15

[like the first time is one epoch the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m18s)
01:36:18

[second one is two epochs](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m21s)
01:36:21

[the third one is for epochs and you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m23s)
01:36:23

[see now the validation train and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m26s)
01:36:26

[training are about the same okay so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m28s)
01:36:28

[that's kind of thinking yeah this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m30s)
01:36:30

[this is about the right track and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m32s)
01:36:32

[then I tried using test time](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m34s)
01:36:34

[augmentation to see if that gets any](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m36s)
01:36:36

[better still didn't actually help a hell](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m38s)
01:36:38

[of a lot just a tiny bit and just kind](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m40s)
01:36:40

[of at this point I think here this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m44s)
01:36:44

[nearly done so I just did it like you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m46s)
01:36:46

[know one more cycle of two to see if it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m48s)
01:36:48

[got any better and it did get a little](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m50s)
01:36:50

[bit better and then I'm like okay that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m53s)
01:36:53

[looks pretty good](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m55s)
01:36:55

[I've got a validation set lost 0.199](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h36m57s)
01:36:57

[and so your Lotus here actually you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m02s)
01:37:02

[haven't tried unfreezing the reason why](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m05s)
01:37:05

[I was going to try to unfreezing and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m08s)
01:37:08

[training more it didn't get any better](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m09s)
01:37:09

[and so the reason for this clearly is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m11s)
01:37:11

[that this data set is so similar the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m13s)
01:37:13

[image net that the training that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m16s)
01:37:16

[convolutional layers actually doesn't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m19s)
01:37:19

[help in the slightest and actually when](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m20s)
01:37:20

[I loaded up into it it turns out that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m23s)
01:37:23

[this competition is actually using a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m25s)
01:37:25

[subset of improve image net so that's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m27s)
01:37:27

[okay so that if we check this out point](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m30s)
01:37:30

[one nine nine against the leaderboard](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m33s)
01:37:33

[this is only a playground competition so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m36s)
01:37:36

[it's not like the best of here but you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m38s)
01:37:38

[know it's still interesting it gets us](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m40s)
01:37:40

[somewhere around ten thrillers okay and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m44s)
01:37:44

[in fact we're competing against I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m48s)
01:37:48

[noticed other](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m52s)
01:37:52

[the first AI student this is a first AI](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m53s)
01:37:53

[student these people up here I know they](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m55s)
01:37:55

[actually posted that they cheated they](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h37m58s)
01:37:58

[actually went you downloaded the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m00s)
01:38:00

[original images and train to that so and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m02s)
01:38:02

[this is why this is a playground](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m07s)
01:38:07

[competition they call it it's not it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m08s)
01:38:08

[not real right you know it's just to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m10s)
01:38:10

[allow us to try things out but you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m12s)
01:38:12

[basically see out of two hundred and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m14s)
01:38:14

[something people where you know we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m18s)
01:38:18

[getting some very good results without](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m20s)
01:38:20

[doing anything remotely interesting or](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m23s)
01:38:23

[clever and we haven't even used the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m25s)
01:38:25

[whole data set you're going to use to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m26s)
01:38:26

[eighty percent of it like to get a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m27s)
01:38:27

[better result I would go back and remove](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m29s)
01:38:29

[that validation set and just rerun the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m31s)
01:38:31

[same steps and then submit that exact](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m33s)
01:38:33

[let's just use it under percent of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m36s)
01:38:36

[data I have three questions the first](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m37s)
01:38:37

[one is like that class in this case is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m48s)
01:38:48

[very it's not balanced](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m50s)
01:38:50

[instead unbalanced like it's not totally](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m53s)
01:38:53

[balanced but it's not bad right it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m56s)
01:38:56

[like between sixty and a hundred like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h38m58s)
01:38:58

[it's it's it's it's not unbalanced](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m02s)
01:39:02

[enough that I would give it a second](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m04s)
01:39:04

[thought](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m05s)
01:39:05

[okay yeah let's get to that later in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m06s)
01:39:06

[this course and don't let me forget](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m14s)
01:39:14

[right the short answer is that there was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m16s)
01:39:16

[a recent list the paper came out about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m18s)
01:39:18

[two or three weeks ago on this and it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m20s)
01:39:20

[said the best way to deal with very](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m21s)
01:39:21

[unbalanced data sets is to basically](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m23s)
01:39:23

[make copies of the rare cases yeah my](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m25s)
01:39:25

[second question is I want to pin down a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m35s)
01:39:35

[difference between creation he read was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m38s)
01:39:38

[and so you have these two options right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m40s)
01:39:40

[so when you beginning I did an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m44s)
01:39:44

[optimization use that pre computed it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m47s)
01:39:47

[was true by not using layers right right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m49s)
01:39:49

[so it's not only they frozen their pre](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m52s)
01:39:52

[computed so the data augmentation](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m54s)
01:39:54

[doesn't do anything at that point](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m55s)
01:39:55

[right before you outcries everything](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h39m59s)
01:39:59

[what as examples you and IV only you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m03s)
01:40:03

[only on freeze](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m06s)
01:40:06

[so we're going to learn more about the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m08s)
01:40:08

[details as we look into the the math and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m10s)
01:40:10

[stuff in coming lessons but basically](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m12s)
01:40:12

[what happened was we started with a pre](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m14s)
01:40:14

[trained network right which was kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m16s)
01:40:16

[finding activations that had these kind](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m20s)
01:40:20

[of rich features and we were adding then](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m23s)
01:40:23

[we add a couple of layers on the end of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m27s)
01:40:27

[it which which start out random and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m29s)
01:40:29

[with fries equals with with everything](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m33s)
01:40:33

[frozen and indeed with pre compute](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m36s)
01:40:36

[equals true all we're learning is told](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m38s)
01:40:38

[is those couple of layers that we've](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m40s)
01:40:40

[added and so with pre compute equals](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m42s)
01:40:42

[true we actually pretty calculate like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m45s)
01:40:45

[how much does this image have something](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m47s)
01:40:47

[that looks like this a ball one looks](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m49s)
01:40:49

[like this face and so forth and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m51s)
01:40:51

[therefore data augmentation doesn't do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m53s)
01:40:53

[anything with pre compute equals true](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m55s)
01:40:55

[because you know we're actually showing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m56s)
01:40:56

[exactly the same activations each time](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h40m59s)
01:40:59

[we can then set pre compute equals false](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m01s)
01:41:01

[which means it's still only training](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m03s)
01:41:03

[those last two layers that we added it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m06s)
01:41:06

[still frozen but data augmentations now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m09s)
01:41:09

[working because it's actually going](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m11s)
01:41:11

[through and recalculating all of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m12s)
01:41:12

[activations from scratch and then](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m14s)
01:41:14

[finally when we unfreeze that's actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m17s)
01:41:17

[saying okay now you can go ahead and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m19s)
01:41:19

[change all of these earlier](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m21s)
01:41:21

[convolutional filters so well you just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m23s)
01:41:23

[so the only reason to have pre compute](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m28s)
01:41:28

[equals true is it's just much faster so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m31s)
01:41:31

[it's like it is it's about you know ten](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m33s)
01:41:33

[or more times faster so particularly if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m35s)
01:41:35

[you're working with like quite a large](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m38s)
01:41:38

[data set you know it can save quite a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m39s)
01:41:39

[bit of time but it's never there's no](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m42s)
01:41:42

[like companies like accuracy reason ever](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m45s)
01:41:45

[to use pre computed calls true it's just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m49s)
01:41:49

[a it's just a shortcut it's also like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m51s)
01:41:51

[quite handy if you're like throwing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m53s)
01:41:53

[together a quick model you know it can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m55s)
01:41:55

[take a few seconds to create](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h41m57s)
01:41:57

[my last question which I think you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m01s)
01:42:01

[answer is I don't like your suggestions](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m03s)
01:42:03

[to build a model you have this aged yeah](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m07s)
01:42:07

[what if would you like we just wanted](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m11s)
01:42:11

[one initial setting without these like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m15s)
01:42:15

[checking after each I mean if you want](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m19s)
01:42:19

[it like if your question is like is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m24s)
01:42:24

[there some shorter version of this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m25s)
01:42:25

[that's like a bit quicker and easier I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m27s)
01:42:27

[could like to lead a few things here](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m29s)
01:42:29

[okay I think this is a kind of a minimal](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m39s)
01:42:39

[version to get you a very good result](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m41s)
01:42:41

[which is like don't worry about pre](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m43s)
01:42:43

[compute equals true because that's just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m45s)
01:42:45

[saving a little bit of time you know so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m47s)
01:42:47

[so I still suggest use LR find at the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m49s)
01:42:49

[start to find a good learning rate by](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m52s)
01:42:52

[default everything is frozen from the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m56s)
01:42:56

[start so then you can just go ahead and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m57s)
01:42:57

[run two or three epochs or cyclic](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h42m59s)
01:42:59

[Nichols one unfreeze and then train the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m01s)
01:43:01

[rest of the network with differential](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m05s)
01:43:05

[learning rates so it's basically three](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m07s)
01:43:07

[steps learning rate finder trained](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m09s)
01:43:09

[frozen network with cycle methods one](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m13s)
01:43:13

[and then trained unfrozen network with](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m15s)
01:43:15

[differential learning rates and cycle](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m18s)
01:43:18

[molecules too so like that's something](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m20s)
01:43:20

[you could turn into I guess five or six](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m22s)
01:43:22

[lines of code at all I think it's a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m26s)
01:43:26

[question provide your own mix book by](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m30s)
01:43:30

[reusing the batch size does the only at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m34s)
01:43:34

[better speed of training yeah pretty](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m36s)
01:43:36

[much so each batch and again we're going](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m39s)
01:43:39

[to see like all this stuff about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m42s)
01:43:42

[precomputing batch sizes we dig into the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m43s)
01:43:43

[details of the algorithms it's going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m45s)
01:43:45

[make a lot more sense intuitively but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m47s)
01:43:47

[basically if you're showing it less](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m49s)
01:43:49

[images each time then it's calculating](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m53s)
01:43:53

[the gradient with less images which](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m56s)
01:43:56

[means it's less accurate which means](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h43m58s)
01:43:58

[like knowing which direction to go and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m00s)
01:44:00

[how far to go in that direction is less](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m02s)
01:44:02

[accurate so as you make the batch size](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m04s)
01:44:04

[smaller](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m06s)
01:44:06

[you're basically making it kind of more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m07s)
01:44:07

[volatile it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m09s)
01:44:09

[kind of like it kind of impacts the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m11s)
01:44:11

[optimal learning rate that you would](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m18s)
01:44:18

[need to use but in practice where only](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m20s)
01:44:20

[you know I generally find only dividing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m22s)
01:44:22

[with the batch size by like 2 or 4 it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m24s)
01:44:24

[doesn't seem to change things very much](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m26s)
01:44:26

[should I reveals the learning rate of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m28s)
01:44:28

[quality me if you if you change the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m30s)
01:44:30

[batch size by much you can rerun the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m33s)
01:44:33

[learning rate finder to see if it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m34s)
01:44:34

[changed if I match but it it I was in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m36s)
01:44:36

[for only generally looking at like a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m38s)
01:44:38

[power of 10 it probably is not going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m40s)
01:44:40

[change the it's not that you can't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m42s)
01:44:42

[because plus back there](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m43s)
01:44:43

[this is sort of a conceptual basic](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m48s)
01:44:48

[questions we're going back to the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m50s)
01:44:50

[previous night where you should put in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m51s)
01:44:51

[the thought behind sorry yeah this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m53s)
01:44:53

[well one for conceptual so a basic](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m55s)
01:44:55

[question we've actually really slide](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m57s)
01:44:57

[where you should what the different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h44m59s)
01:44:59

[layers were doing yes from this slide I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m01s)
01:45:01

[understand right the meaning of sync the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m07s)
01:45:07

[third column relative to the fourth](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m11s)
01:45:11

[column is that what you're interpreting](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m12s)
01:45:12

[what the layer is doing based on what](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m16s)
01:45:16

[the image is actually yeah so we're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m19s)
01:45:19

[going to look at this in more detail so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m23s)
01:45:23

[these these gray ones basically say this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m24s)
01:45:24

[is kind of what the filter looks like so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m26s)
01:45:26

[on the first layer you can see exactly](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m28s)
01:45:28

[what the filter looks like because the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m31s)
01:45:31

[input to it of pixels right so you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m32s)
01:45:32

[absolutely say and remember we looked at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m34s)
01:45:34

[what a convolutional kernel was like was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m36s)
01:45:36

[that three by three thing so this look](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m38s)
01:45:38

[like there's seven by seven kernels you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m41s)
01:45:41

[can say this is actually what it looks](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m43s)
01:45:43

[like but later on it's combined you know](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m44s)
01:45:44

[the the the input to it are themselves](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m47s)
01:45:47

[activations which are combinations of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m50s)
01:45:50

[activations relation to activations so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m52s)
01:45:52

[you can't draw it but there's clever](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m54s)
01:45:54

[technique that I learned focus created](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m56s)
01:45:56

[which allowed them to say this is kind](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h45m58s)
01:45:58

[of what the filters tended to look like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m00s)
01:46:00

[on average alright so this is kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m02s)
01:46:02

[what the photos look like and then here](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m04s)
01:46:04

[is specific examples of patches of image](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m06s)
01:46:06

[which activated that filter highly so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m10s)
01:46:10

[yet the pictures are the ones that I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m14s)
01:46:14

[kind of find more useful because it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m16s)
01:46:16

[tells you this kernel is kind of a mini](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m17s)
01:46:17

[cycle we all find right how do we know](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m21s)
01:46:21

[that's it well we'll come back well we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m35s)
01:46:35

[may come back to that if not in this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m40s)
01:46:40

[part in the next part that probably a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m41s)
01:46:41

[part two actually because this paper](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m45s)
01:46:45

[this paper uses to create these things](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m48s)
01:46:48

[this paper uses something called a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m49s)
01:46:49

[deconvolution which I'm pretty sure we](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m50s)
01:46:50

[won't do in this part but we will do it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m53s)
01:46:53

[in part two so if you're interested](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m54s)
01:46:54

[check out the paper it's it's in the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h46m57s)
01:46:57

[notebook has a link to it xyler in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m00s)
01:47:00

[Fergus it's a very clever technique and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m01s)
01:47:01

[not terribly intuitive](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m06s)
01:47:06

[um right so so you mentioned that it was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m10s)
01:47:10

[good that the dog took up the full](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m18s)
01:47:18

[picture and it would have been a problem](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m20s)
01:47:20

[if it was kind of like off in one of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m22s)
01:47:22

[corners in really tiny well what would](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m24s)
01:47:24

[you what would you technique have been](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m27s)
01:47:27

[to try to make that work something that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m29s)
01:47:29

[we'll learn about in part two but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m34s)
01:47:34

[basically there's a technique that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m36s)
01:47:36

[allows you to to kind of figure out](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m38s)
01:47:38

[roughly which parts of an image and most](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m41s)
01:47:41

[likely to have the interesting things in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m43s)
01:47:43

[them and then you can like crop out](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m45s)
01:47:45

[those bits if you're interested in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m47s)
01:47:47

[learning about it we did cover it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m50s)
01:47:50

[briefly in lesson seven of part one but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m52s)
01:47:52

[I'm going to actually do it properly in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m55s)
01:47:55

[part two of this course because I didn't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h47m58s)
01:47:58

[really cover it thoroughly enough maybe](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m01s)
01:48:01

[we'll find time to have a quick look at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m06s)
01:48:06

[it but we'll see I know your Nets](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m07s)
01:48:07

[written some of the code that we need](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m10s)
01:48:10

[already](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m11s)
01:48:11

[ah](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m13s)
01:48:13

[so once I have something like this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m16s)
01:48:16

[notebook that's basically working I can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m18s)
01:48:18

[immediately make it better by doing two](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m24s)
01:48:24

[things assuming that the size image I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m28s)
01:48:28

[was using is smaller than the average](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m32s)
01:48:32

[size of the image that we've been given](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m34s)
01:48:34

[I can increase the size and as I showed](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m35s)
01:48:35

[before with the dog breeds you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m38s)
01:48:38

[actually increase it during training the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m40s)
01:48:40

[other thing I can do is to create is to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m42s)
01:48:42

[use a better architecture now an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m45s)
01:48:45

[architect we're going to talk a lot in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m48s)
01:48:48

[this course about architectures but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m49s)
01:48:49

[basically there are different ways of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m51s)
01:48:51

[putting together like what size](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h48m58s)
01:48:58

[convolutional filters and how are they](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m00s)
01:49:00

[connected to each other and so forth and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m02s)
01:49:02

[different architectures have different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m05s)
01:49:05

[like numbers of layers and sizes of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m07s)
01:49:07

[kernels and number of filters and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m09s)
01:49:09

[forth and so there are some the one that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m11s)
01:49:11

[we've been using ResNet 34 is a great](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m16s)
01:49:16

[starting point and often a good](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m19s)
01:49:19

[finishing point because it's like it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m21s)
01:49:21

[pretty it doesn't have too many](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m23s)
01:49:23

[parameters often it works pretty well](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m25s)
01:49:25

[with small amounts of data as we've seen](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m27s)
01:49:27

[and so forth but there's actually an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m28s)
01:49:28

[architecture that I really like called](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m32s)
01:49:32

[not res net but res next which was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m34s)
01:49:34

[actually the second-place winner in last](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m37s)
01:49:37

[year's image net competition and like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m39s)
01:49:39

[ResNet you can put a number after the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m44s)
01:49:44

[res next to say like how big it is and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m46s)
01:49:46

[like my next step after resume 34 is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m49s)
01:49:49

[always res next 50 now you'll find res](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m52s)
01:49:52

[next 50 takes like can take like twice](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m55s)
01:49:55

[as long as ResNet 34 that can take like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h49m58s)
01:49:58

[2 to 4 times as much memory as retina 34](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m01s)
01:50:01

[so what I wanted to do was I wanted to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m06s)
01:50:06

[rerun that previous notebook with res](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m08s)
01:50:08

[next and increasing the image size to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m10s)
01:50:10

[turn on a node so here I just said](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m12s)
01:50:12

[architecture equals res next 50 size](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m15s)
01:50:15

[equals 299 and then I found that I had](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m18s)
01:50:18

[to take the batch size all the way back](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m20s)
01:50:20

[to 28 to get it to fit my GPU is 11 gig](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m21s)
01:50:21

[if you're using AWS or cresol I think](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m25s)
01:50:25

[they're like 12 gigs they might be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m27s)
01:50:27

[a bit higher but this is what I found I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m30s)
01:50:30

[had to do so then I this is literally a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m32s)
01:50:32

[copy of the previous notebook so you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m34s)
01:50:34

[actually go file make a copy right and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m36s)
01:50:36

[then rerun it with with these different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m39s)
01:50:39

[parameters and so I deleted some of the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m41s)
01:50:41

[pros and some of the expiratory stuff to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m45s)
01:50:45

[see you know basically I said everything](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m47s)
01:50:47

[else is the same all the same steps as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m49s)
01:50:49

[before there's my in fact you can kind](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m52s)
01:50:52

[of see what this minimum service desk](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m54s)
01:50:54

[looks like I didn't need to worry about](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m55s)
01:50:55

[learning rate finder so I just left it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m57s)
01:50:57

[as is so transforms data equals loan](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h50m59s)
01:50:59

[equals bit pre computed false feet with](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m02s)
01:51:02

[cycle integrals one and freeze](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m06s)
01:51:06

[differential learning rates bits and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m08s)
01:51:08

[more and you can see here I didn't do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m12s)
01:51:12

[the cycle mop thing because I found like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m14s)
01:51:14

[now that I'm using a bigger architecture](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m17s)
01:51:17

[it's got more parameters it was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m19s)
01:51:19

[overfitting pretty quickly so rather](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m21s)
01:51:21

[than like cycle length equals one never](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m23s)
01:51:23

[finding the right spot it actually did](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m25s)
01:51:25

[find the right spot and if I used longer](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m28s)
01:51:28

[cycle legs I found that my validation](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m29s)
01:51:29

[error was higher than my training error](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m34s)
01:51:34

[it was over there so check us out though](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m37s)
01:51:37

[by using these you know three steps](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m40s)
01:51:40

[I got plus TTA 99.75](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m43s)
01:51:43

[so what does that mean that means I have](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m47s)
01:51:47

[one incorrect dog for incorrect cats and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m50s)
01:51:50

[when we look at the pictures of them my](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m54s)
01:51:54

[incorrect dog has a cat now this one is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h51m58s)
01:51:58

[not a either this one is not either so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m02s)
01:52:02

[I've actually got one mistake and then](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m04s)
01:52:04

[my incorrect dog is teeth right so like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m07s)
01:52:07

[we're at a point where we're now able to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m12s)
01:52:12

[train a classifier that's so good that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m15s)
01:52:15

[it has like basically one's dead right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m18s)
01:52:18

[and so when people say like we have](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m23s)
01:52:23

[superhuman image performance now this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m25s)
01:52:25

[kind of what they're talking about right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m27s)
01:52:27

[so did you actually when I looked at the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m29s)
01:52:29

[dog breed one I did this morning I was](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m31s)
01:52:31

[like it was it was getting the dog](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m34s)
01:52:34

[breeds much better than I ever could](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m36s)
01:52:36

[so like hits this this is what we can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m39s)
01:52:39

[get to if you use a really modern](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m42s)
01:52:42

[architect](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m43s)
01:52:43

[like redneck and this suddenly took out](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m44s)
01:52:44

[a tall way and remember don't like 20](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m48s)
01:52:48

[minutes to Train so that's kind of where](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m51s)
01:52:51

[we're up to so if you want to do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h52m55s)
01:52:55

[satellite imagery](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m02s)
01:53:02

[instead right then it's the same thing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m04s)
01:53:04

[and in fact the the planet satellite](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m07s)
01:53:07

[data sets already oh and Chris or if](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m09s)
01:53:09

[you're using Chris or you can jump](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m11s)
01:53:11

[straight there right and I just went](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m12s)
01:53:12

[into this data stash planet and I can do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m17s)
01:53:17

[exactly the same thing right I can image](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m20s)
01:53:20

[classifier from CSV right and you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m25s)
01:53:25

[see these three lines are actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m28s)
01:53:28

[exactly the same as my dog breed lines](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m30s)
01:53:30

[you know how big how many lines are in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m31s)
01:53:31

[the file grab my validation indexes this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m34s)
01:53:34

[get data as you can see it's identical](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m37s)
01:53:37

[except I've changed side on to top down](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m38s)
01:53:38

[the satellite images about top down so I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m42s)
01:53:42

[can fit them vertically and they still](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m44s)
01:53:44

[make sense right and so you can see here](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m47s)
01:53:47

[I'm doing this trick round back to size](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m49s)
01:53:49

[equals 64 and train a little bit first](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m51s)
01:53:51

[learning rate find on right and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m55s)
01:53:55

[interestingly in this case you can see](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m57s)
01:53:57

[it I want really high learning rates I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h53m59s)
01:53:59

[don't know what it is about this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m01s)
01:54:01

[particular data set this is true but](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m03s)
01:54:03

[it's clearly I can use super high](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m05s)
01:54:05

[learning rate so I use a lot here at a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m07s)
01:54:07

[point too and so I've trained for a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m08s)
01:54:08

[while](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m12s)
01:54:12

[differential learning rates right and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m13s)
01:54:13

[remember I said like if the data sets](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m16s)
01:54:16

[very different to image net I probably](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m18s)
01:54:18

[want to train those middle layers a lot](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m20s)
01:54:20

[more so I'm using divided by three](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m23s)
01:54:23

[rather than divided by ten all right the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m25s)
01:54:25

[other than that is the same thing cycle](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m27s)
01:54:27

[Nauticals - all right and then I just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m28s)
01:54:28

[kind of keep an eye on it so you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m33s)
01:54:33

[actually plot the loss if you go and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m34s)
01:54:34

[learned up shared a plot loss you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m35s)
01:54:35

[see here that here's the first cycle is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m37s)
01:54:37

[the second cycle is the third cycle](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m40s)
01:54:40

[right so you can see it gets better pops](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m43s)
01:54:43

[out gets better pops out if better pops](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m45s)
01:54:45

[out and each time it finds something](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m46s)
01:54:46

[better than the last time](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m48s)
01:54:48

[then set the size up to 128 and just](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m50s)
01:54:50

[repeat exactly the last few steps and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m53s)
01:54:53

[then set up to 256](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m55s)
01:54:55

[repeat the last two steps and then do](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h54m58s)
01:54:58

[TTA and if you submit this and this gets](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m02s)
01:55:02

[about 30th place in this competition so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m05s)
01:55:05

[these basic steps work super well this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m10s)
01:55:10

[this thing where I went all the way back](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m12s)
01:55:12

[to a size of 64 I wouldn't do that if I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m14s)
01:55:14

[was doing like dogs and cats or dog](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m19s)
01:55:19

[breeds because like this is so small](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m21s)
01:55:21

[that if if the thing I was working on is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m23s)
01:55:23

[very similar to imagenet I would kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m26s)
01:55:26

[destroy those imagenet weights like 64](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m29s)
01:55:29

[by 64 is so small but in this case the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m32s)
01:55:32

[satellite imagery data it's so different](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m34s)
01:55:34

[to imagenet um you know I really found](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m36s)
01:55:36

[that it worked pretty well](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m38s)
01:55:38

[start right back to these tiny images it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m39s)
01:55:39

[really helped me to avoid overfitting](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m43s)
01:55:43

[and interestingly using this kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m45s)
01:55:45

[approach I actually found that even with](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m48s)
01:55:48

[using only 128 by 128 I was getting like](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m50s)
01:55:50

[much better cackled results than really](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m53s)
01:55:53

[everybody on the leader board](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m55s)
01:55:55

[and when I say 30th place this is a very](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h55m57s)
01:55:57

[recent competition right and so I find](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m00s)
01:56:00

[like in the last year like a lot of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m02s)
01:56:02

[people have got a lot better at computer](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m05s)
01:56:05

[vision and so the people in the top 50](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m07s)
01:56:07

[in this competition were generally](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m09s)
01:56:09

[ensemble in dozens of models lots of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m10s)
01:56:10

[people on a team lots of pre-processing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m13s)
01:56:13

[specific satellite data and so forth so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m15s)
01:56:15

[like to be able to get xxx using this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m18s)
01:56:18

[totally standard technique is pretty](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m21s)
01:56:21

[cool](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m22s)
01:56:22

[alright so now that we've got to this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m24s)
01:56:24

[point right we've got through two](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m28s)
01:56:28

[lessons if you're still here then](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m29s)
01:56:29

[hopefully you're thinking okay this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m32s)
01:56:32

[actually pretty useful I want to do more](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m35s)
01:56:35

[in which case Kressel might not be where](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m37s)
01:56:37

[you want to stay the issues with Kressel](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m41s)
01:56:41

[I mean it's it's it's pretty handy it's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m43s)
01:56:43

[pretty cheap and something we haven't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m45s)
01:56:45

[talked about much is paper space is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m47s)
01:56:47

[another great choice by the way paper](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m50s)
01:56:50

[space are short they're going to be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m52s)
01:56:52

[releasing kress or like instant Drupal](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m53s)
01:56:53

[notebooks unfortunately they're not](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m55s)
01:56:55

[ready quite yet but they do have an](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m57s)
01:56:57

[ability to basically they have the best](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h56m59s)
01:56:59

[price performance relationship right now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m01s)
01:57:01

[and they you can SSH into them and use](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m04s)
01:57:04

[them so they're also a great choice and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m08s)
01:57:08

[probably by the time this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m10s)
01:57:10

[the MOOC will probably have a separate](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m11s)
01:57:11

[lesson showing you how to set up set up](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m13s)
01:57:13

[paper space because there they're likely](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m15s)
01:57:15

[to be a great option but at some point](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m18s)
01:57:18

[you're probably going to want to look at](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m20s)
01:57:20

[AWS a couple of reasons why the first is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m21s)
01:57:21

[as you all know by now amazon have been](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m26s)
01:57:26

[kind enough to donate about $200,000](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m30s)
01:57:30

[worth of compute time to this course so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m33s)
01:57:33

[I want to say thank you very much to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m35s)
01:57:35

[Amazon we've all been given credit so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m37s)
01:57:37

[everybody this year so thanks very much](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m40s)
01:57:40

[hey don't worry we're so sorry you're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m42s)
01:57:42

[sure in the MOOC we didn't get it for](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m46s)
01:57:46

[you but everybody here is like AWS](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m48s)
01:57:48

[credits for everybody so um but you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m50s)
01:57:50

[get even if you're not here in person](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m53s)
01:57:53

[you can get AWS credits from lots of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m55s)
01:57:55

[places github has a student pack Google](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h57m57s)
01:57:57

[for github student pack that's like 150](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m00s)
01:58:00

[bucks worth of credits AWS educate can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m02s)
01:58:02

[get credits these our office students so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m05s)
01:58:05

[there's lots of places you can get](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m08s)
01:58:08

[started on AWS pretty much everybody](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m09s)
01:58:09

[everybody a lot of the people that you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m13s)
01:58:13

[might work with will be using AWS](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m15s)
01:58:15

[because it's like super flexible right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m18s)
01:58:18

[now AWS has the fastest available GPUs](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m21s)
01:58:21

[you can get in the cloud they're p3s](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m25s)
01:58:25

[they're kind of expensive at three bucks](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m28s)
01:58:28

[an hour but if you've got like a model](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m31s)
01:58:31

[where you've done all the steps before](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m32s)
01:58:32

[you're thinking this is looking pretty](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m34s)
01:58:34

[good you know for 6 bucks you could get](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m35s)
01:58:35

[a p3 for 2 hours and run turbo speed](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m38s)
01:58:38

[right um we didn't start with AWS](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m41s)
01:58:41

[because well hey it's like twice as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m45s)
01:58:45

[expensive as Chris Hall for the cheapest](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m48s)
01:58:48

[GPU and being a Texan setup right but I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m49s)
01:58:49

[wanted to kind of go through and show](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m54s)
01:58:54

[you how to get your AWS setup and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m57s)
01:58:57

[we're going to be going slightly over](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h58m59s)
01:58:59

[time to do that but I want to show you a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m01s)
01:59:01

[very quick place I feel prettier if you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m03s)
01:59:03

[have to but I want to show you very](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m05s)
01:59:05

[quickly how you can get your AWS setup](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m07s)
01:59:07

[right from scratch so basically you have](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m10s)
01:59:10

[to go to consult on AWS but amazon.com](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m14s)
01:59:14

[and it'll take you to the console right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m17s)
01:59:17

[and so you can follow along on the video](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m19s)
01:59:19

[with this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m22s)
01:59:22

[quickly from here you have to go to AC -](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m23s)
01:59:23

[this is where you set up your instances](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m27s)
01:59:27

[and so from ec2 you need to do what's](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m29s)
01:59:29

[called launching an instance so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m33s)
01:59:33

[launching an instance means you're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m35s)
01:59:35

[basically creating a computer right now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m36s)
01:59:36

[creating a computer on Amazon so I say](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m38s)
01:59:38

[launch instance and what we've done is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m41s)
01:59:41

[we've created a fast AI it's got an amo](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m44s)
01:59:44

[and ami is like a template for how your](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m47s)
01:59:47

[computer's going to begin so if you've](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m49s)
01:59:49

[got a community a Mis and type in fast](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m51s)
01:59:51

[AI you'll see that there's one there](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m54s)
01:59:54

[called fast AI part 1 version 2 for the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=01h59m56s)
01:59:56

[p2 ok so I'm going to select that and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m00s)
02:00:00

[then we need to say what kind of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m04s)
02:00:04

[computer do you want and so I can say I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m06s)
02:00:06

[want a GPU compute computer and then I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m08s)
02:00:08

[can say I want a p2 x large this is the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m13s)
02:00:13

[cheapest reasonably effective for deep](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m16s)
02:00:16

[learning instance type they have and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m19s)
02:00:19

[then I can say launch and then I can say](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m21s)
02:00:21

[launch and so at this point they asked](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m25s)
02:00:25

[you to choose a key pair right now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m29s)
02:00:29

[if you don't have a key pair you have to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m33s)
02:00:33

[create one right so to create a key pair](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m35s)
02:00:35

[you need to open your terminal if you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m39s)
02:00:39

[don't have a terminal if you've got a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m44s)
02:00:44

[Mac or Linux box you've definitely got](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m47s)
02:00:47

[one if you've got Windows hopefully](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m48s)
02:00:48

[you've got Ubuntu if you don't already](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m50s)
02:00:50

[have Ubuntu setup you can go to the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m53s)
02:00:53

[Windows Store and click on Ubuntu right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h00m56s)
02:00:56

[we'll get it from the Windows Store so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m01s)
02:01:01

[from there you basically go SSH](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m04s)
02:01:04

[- caged in and that will create like a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m08s)
02:01:08

[special password for your computer to be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m12s)
02:01:12

[able to log in to Amazon and then you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m15s)
02:01:15

[just hit enter three times okay and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m16s)
02:01:16

[that's going to create for you your key](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m19s)
02:01:19

[you can use to get into Amazon alright](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m22s)
02:01:22

[so then what I do is I copy that key](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m24s)
02:01:24

[somewhere that I know where it is so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m26s)
02:01:26

[it'll be in the dot SSH folder](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m28s)
02:01:28

[it's called IDRs a dub and so I'm going](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m30s)
02:01:30

[to copy it to my hard drive so if you're](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m33s)
02:01:33

[in a macro and Linux it'll already be in](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m39s)
02:01:39

[an easy to find place it'll be in your](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m41s)
02:01:41

[SSH folder that in documents so from](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m42s)
02:01:42

[there back in AWS you have to tell it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m49s)
02:01:49

[that you've created this key so you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m53s)
02:01:53

[go to key pairs and you say import key](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m55s)
02:01:55

[pair and you just browse to that file](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h01m59s)
02:01:59

[that you just created there it is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m02s)
02:02:02

[I say import okay so if you've ever used](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m06s)
02:02:06

[SSH before you've already got the key](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m11s)
02:02:11

[pair you don't have to do those depths](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m13s)
02:02:13

[if you've used AWS before you've already](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m14s)
02:02:14

[imported it you don't have to do that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m17s)
02:02:17

[step maybe haven't done any of those](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m18s)
02:02:18

[things you have to do both steps so now](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m20s)
02:02:20

[I can go ahead and launch my instance](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m24s)
02:02:24

[community I am eyes search last day I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m30s)
02:02:30

[select launch and so now it asks me](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m35s)
02:02:35

[what's where's your key pair and I can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m41s)
02:02:41

[choose that one that I just grabbed okay](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m43s)
02:02:43

[so this is going to go ahead and create](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m48s)
02:02:48

[a new computer for me to log into and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m51s)
02:02:51

[you can see here it says the following](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m55s)
02:02:55

[have been initiated and so if I click on](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m56s)
02:02:56

[that it'll show me this new computer](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h02m58s)
02:02:58

[that I've created okay so it'll be able](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m02s)
02:03:02

[to log into it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m05s)
02:03:05

[I need to know its IP address so here it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m08s)
02:03:08

[is the IP address there okay so I can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m11s)
02:03:11

[copy that and that's the IP address of](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m14s)
02:03:14

[my computer so to get to this computer I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m17s)
02:03:17

[need to SSH to it so SSH into a computer](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m20s)
02:03:20

[means connecting to that computer so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m23s)
02:03:23

[that it's like you're typing in that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m25s)
02:03:25

[computer so I type SSH and they username](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m26s)
02:03:26

[for this instance is always Ubuntu right](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m29s)
02:03:29

[and then I can paste in that IP address](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m33s)
02:03:33

[and then there's one more thing I have](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m36s)
02:03:36

[to do which is I have to connect up the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m38s)
02:03:38

[jupiter notebook on that instance to the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m41s)
02:03:41

[jupiter notebook on my machine and so to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m44s)
02:03:44

[do that there's just a particular flag](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m46s)
02:03:46

[that i said okay we can talk about it on](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m48s)
02:03:48

[the forums as to exactly what it does](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m50s)
02:03:50

[but you just type - l.a today date](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m52s)
02:03:52

[localhost 8 8 8 8 ok so like once you've](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m55s)
02:03:55

[done it once you can like save that as](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h03m59s)
02:03:59

[an alias and type in the same thing](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m01s)
02:04:01

[every time](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m03s)
02:04:03

[so we can check here we can see it says](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m05s)
02:04:05

[that it's running so we should be able](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m07s)
02:04:07

[to now hit enter first time ever which](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m09s)
02:04:09

[sit reconnect to it it does checks this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m12s)
02:04:12

[is okay I'll say yes and then that goes](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m14s)
02:04:14

[ahead and SSH is in so this ami is all](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m19s)
02:04:19

[set up for you alright so you'll find](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m27s)
02:04:27

[that the very first time you log in it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m29s)
02:04:29

[takes a few extra seconds because it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m31s)
02:04:31

[just kind of is getting everything set](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m32s)
02:04:32

[up but once it's logged in you'll see](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m34s)
02:04:34

[there that there's a directory called](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m36s)
02:04:36

[fast AI and the fast AI directory](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m38s)
02:04:38

[contains our fast AI repo that contains](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m41s)
02:04:41

[all the notebooks or the code etc so I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m45s)
02:04:45

[can just go CD faster all right first](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m48s)
02:04:48

[thing you do when you get in is to make](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m51s)
02:04:51

[sure it's updated so you just go git](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m53s)
02:04:53

[pull right and that updates to make sure](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m55s)
02:04:55

[that your repo is the same as the most](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h04m59s)
02:04:59

[recent video and so as you can see there](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m01s)
02:05:01

[we go](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m05s)
02:05:05

[let's make sure it's got all the most](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m05s)
02:05:05

[recent code the second thing you should](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m06s)
02:05:06

[do is type Condor and update you can](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m08s)
02:05:08

[just do this maybe once a month or so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m11s)
02:05:11

[and that makes sure that the libraries](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m13s)
02:05:13

[there are all the most recent libraries](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m15s)
02:05:15

[I'm not going to run that so it takes a](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m17s)
02:05:17

[couple of minutes okay](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m19s)
02:05:19

[and then the last step is to type](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m20s)
02:05:20

[particular notebook okay](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m22s)
02:05:22

[so this is going to go ahead and launch](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m26s)
02:05:26

[the triplet notebook server on this](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m29s)
02:05:29

[machine again the first time I do it the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m32s)
02:05:32

[first time you do everything on AWS](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m35s)
02:05:35

[it just takes like a minute or two and](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m37s)
02:05:37

[then once you've done it in the future](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m40s)
02:05:40

[we just as fast as running it locally](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m42s)
02:05:42

[basically okay so you can see it's going](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m44s)
02:05:44

[ahead and firing out the notebook and so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m47s)
02:05:47

[what's going to happen is that because](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m49s)
02:05:49

[when we SSH into it we said to both](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m51s)
02:05:51

[connect our notebook port to the remote](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m53s)
02:05:53

[notebook port we're just going to be](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m56s)
02:05:56

[able to use this locally so I see he](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h05m58s)
02:05:58

[says here copy paste this URL so I'm](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m00s)
02:06:00

[going to grab that URL and I'm going to](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m03s)
02:06:03

[paste it into my browser and that's it](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m06s)
02:06:06

[okay so this notebook is now actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m11s)
02:06:11

[not running on my machine it's actually](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m15s)
02:06:15

[running on AWS okay using the AWS GPU](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m17s)
02:06:17

[it's got a lot of memory it's not the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m21s)
02:06:21

[fastest around but it's not terrible](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m23s)
02:06:23

[you can always fire up a p3 if you want](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m25s)
02:06:25

[something that's super fast this is](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m28s)
02:06:28

[costing me ninety cents a minute okay so](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m30s)
02:06:30

[when you're finished please don't forget](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m33s)
02:06:33

[to shut it down right so to shut it down](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m36s)
02:06:36

[you can right-click on it and say](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m38s)
02:06:38

[instance date stop okay we've got five](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m43s)
02:06:43

[hundred bucks of credit assuming that](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m48s)
02:06:48

[you put your code down in the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m51s)
02:06:51

[spreadsheet one thing I forgot to do the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m53s)
02:06:53

[first time I showed you this by the way](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m55s)
02:06:55

[I said make sure you choose a p2 the](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h06m57s)
02:06:57

[second time I went through I didn't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h07m02s)
02:07:02

[choose p2 by mistake so just don't](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h07m03s)
02:07:03

[forget choose gpq compute P - do you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h07m05s)
02:07:05

[have a question](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h07m09s)
02:07:09

[my Bernice it's an hour thank you](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h07m11s)
02:07:11

[90 cents an hour it also costs like I](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h07m15s)
02:07:15

[don't know three or four bucks a month](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h07m20s)
02:07:20

[for the storage as well thanks for](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h07m21s)
02:07:21

[checking that all right see you next](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h07m24s)
02:07:24

[week sorry we're a bit over](https://www.youtube.com/watch?v=JNxcznsrRb8#t=02h07m26s)
02:07:26

