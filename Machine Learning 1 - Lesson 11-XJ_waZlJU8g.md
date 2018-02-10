[so let's just yeah let's start by](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m00s)
00:00:00

[reviewing kind of what we've learnt](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m02s)
00:00:02

[about optimizing multi-layer functions](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m05s)
00:00:05

[with SGD and so the idea is that we've](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m10s)
00:00:10

[got some data and then we do something](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m13s)
00:00:13

[to that data for example we multiply it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m17s)
00:00:17

[by a weight matrix and then we do](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m20s)
00:00:20

[something to that for example we put it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m24s)
00:00:24

[through a softmax or a sigmoid and then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m28s)
00:00:28

[we do something to that such as do a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m32s)
00:00:32

[cross entropy loss or a root mean](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m35s)
00:00:35

[squared error loss okay and that's gonna](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m38s)
00:00:38

[like give us some scalar so this is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m44s)
00:00:44

[gonna have no hidden layers this has got](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m52s)
00:00:52

[a linear layer a nonlinear activation](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m54s)
00:00:54

[being a soft Max and a loss function](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h00m58s)
00:00:58

[being a root mean squared error or a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m00s)
00:01:00

[cross entropy all right and then we've](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m02s)
00:01:02

[got our input data port linear nonlinear](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m05s)
00:01:05

[bus so for example if this was sigmoid](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m14s)
00:01:14

[or softmax and this was cross entropy](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m22s)
00:01:22

[then that would be logistic regression](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m28s)
00:01:28

[so it's still ya cross entropy yeah](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m34s)
00:01:34

[let's do that next short for now think](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m40s)
00:01:40

[of it like think of RIT means great](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m45s)
00:01:45

[error same thing some loss function okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m46s)
00:01:46

[now we'll look at cross entropy again in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m49s)
00:01:49

[the moment so how do we calculate the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m52s)
00:01:52

[derivative of that with with respect to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h01m59s)
00:01:59

[our weights right so really it would](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m03s)
00:02:03

[probably be better if we said X comma W](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m06s)
00:02:06

[yeah because it's really a function of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m11s)
00:02:11

[the weights as well and so we want the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m13s)
00:02:13

[derivative of this with respect to our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m16s)
00:02:16

[weights sorry I put it in the wrong spot](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m22s)
00:02:22

[Oh G f of X comma W that's why that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m27s)
00:02:27

[didn't make sense all right so to do](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m36s)
00:02:36

[that we just basically we do the chain](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m42s)
00:02:42

[rule so we just say that this is equal](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m45s)
00:02:45

[to H of U and u equals G well G du](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m47s)
00:02:47

[equals G of V and V equals f of X so we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h02m59s)
00:02:59

[can just rewrite it like that right and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h03m09s)
00:03:09

[then we can do the chain rule so we can](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h03m11s)
00:03:11

[say that's equal to H - the derivative](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h03m14s)
00:03:14

[is H - u by G dash V by F dash X hacker](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h03m17s)
00:03:17

[with all that so far okay so in order to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h03m25s)
00:03:25

[take the derivative with respect to the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h03m30s)
00:03:30

[weights therefore we just have to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h03m32s)
00:03:32

[calculate that derivative with respect](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h03m35s)
00:03:35

[to W using that exact formula so if we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h03m38s)
00:03:38

[had in there yeah yeah so so d of all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h03m43s)
00:03:43

[that DW would be yep](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h03m54s)
00:03:54

[so then if if we you know went further](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m00s)
00:04:00

[here and had like another linear layer](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m04s)
00:04:04

[right that's going to be more room now](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m14s)
00:04:14

[that linear layer I cover](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m17s)
00:04:17

[w2 okay so we have another Lydia lair](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m25s)
00:04:25

[there's no difference to now calculate](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m31s)
00:04:31

[the derivative with respect to all of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m34s)
00:04:34

[the parameters we can still use the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m37s)
00:04:37

[exact same chain rule right so so don't](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m39s)
00:04:39

[think of the multi-layer network as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m44s)
00:04:44

[being like things that occur at](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m46s)
00:04:46

[different times it's just a composition](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m48s)
00:04:48

[of functions and so we just use the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m50s)
00:04:50

[chain rule to calculate all the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m53s)
00:04:53

[derivatives at once you know there's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m56s)
00:04:56

[that there just a set of parameters that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h04m58s)
00:04:58

[happen to appear in different parts of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m00s)
00:05:00

[the function but look at that the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m01s)
00:05:01

[calculus is no no different so to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m03s)
00:05:03

[calculate this with respect to w1 and w2](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m07s)
00:05:07

[you know it's it's just you just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m12s)
00:05:12

[increase you know W you can just now](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m14s)
00:05:14

[just call it W and say w1 is all of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m17s)
00:05:17

[those weights so the result ah that's a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m19s)
00:05:19

[great question](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m25s)
00:05:25

[so what you're going to have then is a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m25s)
00:05:25

[list of parameters right so here's w1](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m33s)
00:05:33

[and like it's it's it's probably some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m39s)
00:05:39

[kind of higher rank tensor you know like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m43s)
00:05:43

[if it's a convolutional layer it'll you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m46s)
00:05:46

[don't be like a wreck three tensor or](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m50s)
00:05:50

[whatever but we can flatten it out that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m52s)
00:05:52

[would just make it a list of parameters](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m55s)
00:05:55

[there's w1 here's w2 okay it's just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h05m57s)
00:05:57

[another list of parameters right and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m01s)
00:06:01

[here's our loss which is a single you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m05s)
00:06:05

[know a single number so therefore our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m07s)
00:06:07

[derivative is just a vector of that same](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m12s)
00:06:12

[length right it's how much does changing](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m17s)
00:06:17

[that value of W affect the loss](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m19s)
00:06:19

[how much does changing that value of W](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m21s)
00:06:21

[affect the loss right so you can](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m23s)
00:06:23

[basically think of it as a function like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m26s)
00:06:26

[you know y equals ax 1 plus BX 2 plus C](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m29s)
00:06:29

[right and say like oh what's the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m37s)
00:06:37

[derivative of that with respect to a B](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m39s)
00:06:39

[and C and you would have three numbers](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m41s)
00:06:41

[the derivative with respect to a and B](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m44s)
00:06:44

[and C and that's all this is right if](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m45s)
00:06:45

[the derivative with respect to that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m49s)
00:06:49

[weight that weight and that weight and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m50s)
00:06:50

[that weight that went that way to get](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m51s)
00:06:51

[there inside the chain rule we had to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h06m55s)
00:06:55

[calculate and a lot of detail here but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m01s)
00:07:01

[we had to calculate like jacobians so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m03s)
00:07:03

[like the derivative when you take a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m07s)
00:07:07

[matrix product is you've now got](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m10s)
00:07:10

[something where you've got like a a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m13s)
00:07:13

[weight matrix and you've got an input](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m15s)
00:07:15

[vector these are the activations and the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m20s)
00:07:20

[previous layer right and you've got some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m22s)
00:07:22

[new output activations right and so now](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m29s)
00:07:29

[you've got to say like okay for this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m33s)
00:07:33

[particular sorry for this particular](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m36s)
00:07:36

[weight hablas changing this particular](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m38s)
00:07:38

[weight change this particular output and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m45s)
00:07:45

[how does changing this particular weight](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m49s)
00:07:49

[change this particular output and so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m51s)
00:07:51

[forth so you kind of end up with these](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m54s)
00:07:54

[higher dimensional tensors showing like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m56s)
00:07:56

[for every weight how does it affect](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h07m59s)
00:07:59

[every output all right but then by the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m01s)
00:08:01

[time you get to the last function the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m05s)
00:08:05

[last function is going to have like a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m07s)
00:08:07

[mean or a sum or or something so they're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m08s)
00:08:08

[all going to get added up in the end and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m10s)
00:08:10

[so this kind of thing like I don't know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m14s)
00:08:14

[it drives me a bit crazy to try and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m18s)
00:08:18

[calculate it out by hand or even think](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m20s)
00:08:20

[of it step by step because you tend to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m23s)
00:08:23

[have like you just have to remember for](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m25s)
00:08:25

[every input and Aleya for every output](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m27s)
00:08:27

[in the next layer you know you're going](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m30s)
00:08:30

[to have to account for every weight for](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m32s)
00:08:32

[every output you're going to have to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m34s)
00:08:34

[have a separate grant yet one good way](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m36s)
00:08:36

[to look at this is to learn to use PI](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m41s)
00:08:41

[torches like dot grad attribute and got](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m45s)
00:08:45

[backward method manually and like look](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m49s)
00:08:49

[up the to tour the pi torched](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m51s)
00:08:51

[tutorials and so you can actually start](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m53s)
00:08:53

[setting up some calculations with a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m54s)
00:08:54

[vector import in the vector output and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m56s)
00:08:56

[then type dot backward and then say type](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h08m58s)
00:08:58

[grad and like look at it right and then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m01s)
00:09:01

[do some really small ones with just two](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m04s)
00:09:04

[or three items in the input and output](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m06s)
00:09:06

[vectors and let make the make the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m08s)
00:09:08

[operation like plus two or something and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m10s)
00:09:10

[like see what the shapes are make sure](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m12s)
00:09:12

[it makes sense yeah because it's kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m16s)
00:09:16

[like this vector matrix calculus is not](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m18s)
00:09:18

[like introduces zero new concepts to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m25s)
00:09:25

[anything you learnt in high school like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m28s)
00:09:28

[strictly speaking but getting a feel for](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m30s)
00:09:30

[how these shapes move around I find took](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m33s)
00:09:33

[a lot of practice you know the good news](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m38s)
00:09:38

[is you almost never have to worry about](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m40s)
00:09:40

[it okay so we were talking about then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m42s)
00:09:42

[using this kind of logistic regression](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h09m58s)
00:09:58

[for NLP and before we got to that point](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m01s)
00:10:01

[we were talking about using naive Bayes](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m05s)
00:10:05

[for NLP and the basic idea was that we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m09s)
00:10:09

[could take a document write a review](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m14s)
00:10:14

[like this movie is good and turn it into](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m18s)
00:10:18

[a bag of words representation consisting](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m21s)
00:10:21

[of the number of times each word appears](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m23s)
00:10:23

[right and we call this the vocabulary](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m26s)
00:10:26

[this is the unique list of words okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m29s)
00:10:29

[and we used the SK learn count](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m32s)
00:10:32

[vectorizer to automatically generate](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m36s)
00:10:36

[both the vocabulary which in SK low and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m37s)
00:10:37

[they call they call the features and to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m41s)
00:10:41

[court create the bag of words](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m44s)
00:10:44

[representation z' and the whole group of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m45s)
00:10:45

[them then is called a term document](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m48s)
00:10:48

[matrix okay and we kind of realized that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m50s)
00:10:50

[we could calculate the probability that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m54s)
00:10:54

[a positive review contains the word this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h10m59s)
00:10:59

[by just averaging the number of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m04s)
00:11:04

[time disappears and the positive reviews](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m07s)
00:11:07

[and we could do the same for the and we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m08s)
00:11:08

[could do the same for the negatives all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m13s)
00:11:13

[right and then we could take the ratio](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m15s)
00:11:15

[of them to get something which if it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m16s)
00:11:16

[greater than one was a word that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m19s)
00:11:19

[appeared more often in the positive](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m22s)
00:11:22

[reviews or less than one was a word that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m23s)
00:11:23

[appeared more often than the negative](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m26s)
00:11:26

[reviews okay and then we realized you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m28s)
00:11:28

[know using using Bayes rule that we and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m34s)
00:11:34

[taking the logs that we could basically](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m37s)
00:11:37

[end up with something where we could add](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m39s)
00:11:39

[up the logs of these plus the log of the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m41s)
00:11:41

[ratio of the probabilities that things](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m45s)
00:11:45

[are in class one versus class zero and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m47s)
00:11:47

[end up with something we can compare to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m50s)
00:11:50

[zero if it's be greater than zero then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m53s)
00:11:53

[we can predict a document is positive or](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m55s)
00:11:55

[if it's less than zero we can predict](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h11m59s)
00:11:59

[the document is negative and that was](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m00s)
00:12:00

[our Bayes rule all right so we kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m02s)
00:12:02

[did that from math first principles and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m06s)
00:12:06

[I think we agreed that the the naive in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m09s)
00:12:09

[naive Bayes was a good description](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m12s)
00:12:12

[because it assumes independence when](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m14s)
00:12:14

[it's definitely not true but it's an](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m17s)
00:12:17

[interesting starting point and I think](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m19s)
00:12:19

[it was interesting to observe when we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m21s)
00:12:21

[actually got to the point where like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m23s)
00:12:23

[okay now we've you know calculated the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m24s)
00:12:24

[the ratio of the probabilities and took](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m28s)
00:12:28

[the log and now rather than multiply](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m33s)
00:12:33

[them together of course we have to add](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m35s)
00:12:35

[them up and when when we actually wrote](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m36s)
00:12:36

[that down we realized like oh that is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m38s)
00:12:38

[you know just a standard weight matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m43s)
00:12:43

[product plus a bias right and so then we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m50s)
00:12:50

[kind of realized like oh okay so like if](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m55s)
00:12:55

[this is not very good accuracy eighty](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h12m57s)
00:12:57

[percent accuracy](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m00s)
00:13:00

[why not improve it by saying hey we know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m03s)
00:13:03

[other ways to calculate a cut you know a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m07s)
00:13:07

[bunch of coefficients and a bunch of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m10s)
00:13:10

[biases which is to learn them in a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m12s)
00:13:12

[logistic regression alright so in other](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m16s)
00:13:16

[words this this is the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m18s)
00:13:18

[meanwhile we use for a logistic](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m20s)
00:13:20

[regression and so why don't we just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m22s)
00:13:22

[create a logistic regression and fit it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m26s)
00:13:26

[okay and it's going to be give us the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m29s)
00:13:29

[same thing but rather than coefficients](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m32s)
00:13:32

[and biases which are theoretically](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m35s)
00:13:35

[correct based on you know this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m37s)
00:13:37

[assumption of Independence and based on](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m40s)
00:13:40

[Bayes rule there'll be the coefficients](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m42s)
00:13:42

[and biases that are actually the best in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m44s)
00:13:44

[this data right so that was kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m47s)
00:13:47

[where we got to and so the kind of key](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m50s)
00:13:50

[insight here is like just about](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h13m55s)
00:13:55

[everything I find a machine learning](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m01s)
00:14:01

[ends up being either like a tree or you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m03s)
00:14:03

[know a bunch of matrix products and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m08s)
00:14:08

[monomi era T's right like it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m11s)
00:14:11

[everything seems to end up kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m13s)
00:14:13

[coming down to the same thing including](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m14s)
00:14:14

[as it turns out Bayes rule okay and then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m17s)
00:14:17

[it turns out that nearly all of the time](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m21s)
00:14:21

[then whatever the parameters are in that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m23s)
00:14:23

[function nearly all the time it turns](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m27s)
00:14:27

[out that they're better learnt then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m30s)
00:14:30

[calculated based on the theory right and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m33s)
00:14:33

[indeed that's what happened when we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m36s)
00:14:36

[actually tried learning those](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m37s)
00:14:37

[coefficients we got you know 85% okay so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m39s)
00:14:39

[then we noticed that we could also](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m44s)
00:14:44

[rather than take the whole term document](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m48s)
00:14:48

[matrix we could instead just take them](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m50s)
00:14:50

[the you know ones and zeros for presence](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m52s)
00:14:52

[or absence of a word and you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m55s)
00:14:55

[sometimes it was you know this equally](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h14m58s)
00:14:58

[as good but then we actually tried](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m01s)
00:15:01

[something else which is we tried adding](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m04s)
00:15:04

[regularization and with regularization](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m05s)
00:15:05

[the binarized approach turned out to be](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m08s)
00:15:08

[a little better all right so then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m10s)
00:15:10

[regularization was where we took the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m12s)
00:15:12

[loss function and again let's start with](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m16s)
00:15:16

[our MSE and then we'll talk about](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m21s)
00:15:21

[cross-entropy loss function was our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m22s)
00:15:22

[predictions](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m27s)
00:15:27

[- our actuals](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m29s)
00:15:29

[sum that up take the average plus a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m31s)
00:15:31

[penalty okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m39s)
00:15:39

[and so this specifically is the l2](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m42s)
00:15:42

[penalty if this instead was the absolute](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m44s)
00:15:44

[value of W then that would be the l1](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m49s)
00:15:49

[penalty okay we also noted that we don't](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h15m52s)
00:15:52

[really care about the loss function per](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m01s)
00:16:01

[se we only care about its derivatives](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m03s)
00:16:03

[that's actually the thing that updates](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m05s)
00:16:05

[the weights so we can because this is a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m06s)
00:16:06

[sum we can take the derivative of each](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m09s)
00:16:09

[part separately and so the derivative of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m12s)
00:16:12

[this part was just that right and so we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m14s)
00:16:14

[kind of learnt that even though these](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m20s)
00:16:20

[are mathematically equivalent they have](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m21s)
00:16:21

[different names this version it's called](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m23s)
00:16:23

[weight decay and it's kind of what's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m25s)
00:16:25

[used that term is used in the neural net](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m27s)
00:16:27

[literature okay so cross-entropy](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m30s)
00:16:30

[on the other hand you know it's just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m36s)
00:16:36

[another loss function like root mean](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m38s)
00:16:38

[squared error but it's specifically](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m40s)
00:16:40

[designed for classification alright and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m50s)
00:16:50

[so here's an example of a binary](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m54s)
00:16:54

[cross-entropy](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m57s)
00:16:57

[so let's say this is our you know is it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h16m58s)
00:16:58

[a cat or a dog so as to say is cat one](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m00s)
00:17:00

[or a zero](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m03s)
00:17:03

[so Cat Cat Cat and these are our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m04s)
00:17:04

[predictions this is the output of our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m08s)
00:17:08

[final layer of our neural net or a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m11s)
00:17:11

[logistic regression or whatever all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m13s)
00:17:13

[right then all we do is we say okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m16s)
00:17:16

[let's take the actual times the log of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m20s)
00:17:20

[the prediction and then we add to that 1](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m26s)
00:17:26

[minus actual times the log of 1 minus](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m30s)
00:17:30

[the prediction and then take the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m32s)
00:17:32

[negative of that whole thing right so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m34s)
00:17:34

[I suggested to to you all that you tried](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m40s)
00:17:40

[to kind of write the if statement](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m43s)
00:17:43

[version of this so hopefully you've done](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m44s)
00:17:44

[that by now otherwise I'm about to spoil](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m46s)
00:17:46

[it for you so this was Y times log y](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m48s)
00:17:48

[plus 1 minus y times log 1 minus y right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h17m56s)
00:17:56

[and negative of that okay so here wants](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m05s)
00:18:05

[to tell me how to write this as an if](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m08s)
00:18:08

[statement can she hit me okay if y equal](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m09s)
00:18:09

[to sorry if y equal to 1 mm-hmm then in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m21s)
00:18:21

[return](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m25s)
00:18:25

[I love Y mm-hmm otherwise well um else](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m26s)
00:18:26

[return log 1 minus 1 okay oh that's the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m31s)
00:18:31

[things at brackets and you take C my](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m34s)
00:18:34

[name is good](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m37s)
00:18:37

[so the key inside Chen she's using is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m37s)
00:18:37

[that Y has two possibilities 1 or 0 okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m40s)
00:18:40

[and so very often the math can hide the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m43s)
00:18:43

[key insight which I think happens here](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m48s)
00:18:48

[until you actually think about what the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m50s)
00:18:50

[values it can take right so that's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m51s)
00:18:51

[that's all it's doing it's saying either](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m56s)
00:18:56

[give me that or give me that all right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h18m59s)
00:18:59

[could you pass that to the back please](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m02s)
00:19:02

[Jason all right I'm missing something](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m04s)
00:19:04

[but do you know the two variables in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m08s)
00:19:08

[that statement if you got Y soon it'd be](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m10s)
00:19:10

[like white hat on the wires yeah yeah](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m14s)
00:19:14

[thank you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m16s)
00:19:16

[as usual it's me missing something okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m18s)
00:19:18

[okay and so then the you know the multi](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m26s)
00:19:26

[category version is just the same thing](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m30s)
00:19:30

[but you're saying you know it four](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m33s)
00:19:33

[different more than just y equals one or](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m35s)
00:19:35

[zero but y equals zero one two three](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m37s)
00:19:37

[four five six seven eight nine](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m39s)
00:19:39

[for instance okay and so that you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m40s)
00:19:40

[that loss function has a you can figure](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m45s)
00:19:45

[it out yourself in particularly simple](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m48s)
00:19:48

[derivative and it also you know another](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m50s)
00:19:50

[thing you could play with at home if you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m53s)
00:19:53

[like is like thinking about how the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m55s)
00:19:55

[derivative looks when you add a sigmoid](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m57s)
00:19:57

[or a softmax before it you know it turns](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h19m59s)
00:19:59

[out it all turns out very nicely because](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m01s)
00:20:01

[you've got an X P thing going into a log](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m03s)
00:20:03

[e thing so you end up with you know very](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m06s)
00:20:06

[well behaved derivatives the reason I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m08s)
00:20:08

[guess there's lots of reasons that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m12s)
00:20:12

[people use IR MSE for aggression and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m14s)
00:20:14

[cross-entropy for classification but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m18s)
00:20:18

[most of it comes back to this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m20s)
00:20:20

[statistical idea of a best linear](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m22s)
00:20:22

[unbiased estimator you know and based on](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m25s)
00:20:25

[the likelihood function that kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m27s)
00:20:27

[turns out that these have some nice](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m29s)
00:20:29

[statistical properties it turns out](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m31s)
00:20:31

[however in practice root means great](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m34s)
00:20:34

[error in particular the properties are](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m37s)
00:20:37

[perhaps more theoretical than actual and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m40s)
00:20:40

[actually nowadays using the the absolute](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m42s)
00:20:42

[deviation rather than some as grads](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m47s)
00:20:47

[deviation can often work better so in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m49s)
00:20:49

[practice like everything in machine](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m55s)
00:20:55

[learning I normally try both for](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m56s)
00:20:56

[particular data set I'll try both loss](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h20m58s)
00:20:58

[functions and see which one works better](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m00s)
00:21:00

[and us of course it's a cattle](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m02s)
00:21:02

[competition in which case you're told](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m04s)
00:21:04

[how capital is going to judge it and you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m05s)
00:21:05

[should use the same loss function as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m07s)
00:21:07

[caracals evaluation metric all right so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m10s)
00:21:10

[yeah so this is really the key insight](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m16s)
00:21:16

[is like hey let's let's not use theory](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m18s)
00:21:18

[but instead learn things from the data](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m20s)
00:21:20

[and you know we hope that we're going to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m22s)
00:21:22

[get better results particularly with](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m24s)
00:21:24

[regularization we do and then I think](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m26s)
00:21:26

[the key regularization insight here is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m28s)
00:21:28

[hey let's not like try to reduce the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m30s)
00:21:30

[number of parameters in our model but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m33s)
00:21:33

[instead like use lots of parameters and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m35s)
00:21:35

[then use regularization to figure out](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m36s)
00:21:36

[which](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m39s)
00:21:39

[are actually useful and so then we took](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m40s)
00:21:40

[that a step further by saying hey given](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m42s)
00:21:42

[we can do that with wrecker ization](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m44s)
00:21:44

[let's create lots more features by](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m46s)
00:21:46

[adding by grams and trigrams you know by](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m49s)
00:21:49

[grams like by vast and by vengeance and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m52s)
00:21:52

[trigrams like by vengeance . and by Vera](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m55s)
00:21:55

[miles right and you know just to keep](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h21m58s)
00:21:58

[things a little faster we limited it to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m02s)
00:22:02

[800,000 features but you know even with](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m03s)
00:22:03

[the full 70 million features it works](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m06s)
00:22:06

[just as well and it's not a hell of a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m09s)
00:22:09

[lot slower so we created a term document](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m10s)
00:22:10

[matrix again using the full set of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m13s)
00:22:13

[engrams for the training set the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m17s)
00:22:17

[validation set and so now we can go](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m19s)
00:22:19

[ahead and say okay our labels as the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m23s)
00:22:23

[training set labels as before our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m25s)
00:22:25

[independent variables is the binarized](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m28s)
00:22:28

[term document matrix as before and then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m32s)
00:22:32

[let's fit a logistic regression to that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m37s)
00:22:37

[and do some predictions and we get 90%](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m40s)
00:22:40

[accuracy so this is looking pretty good](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m45s)
00:22:45

[okay so the logistic regression let's go](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m48s)
00:22:48

[back to our naive Bayes right in our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h22m58s)
00:22:58

[naive Bayes we have this term document](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m00s)
00:23:00

[matrix and then for every feature we're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m03s)
00:23:03

[calculating the probability of that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m06s)
00:23:06

[feature occurring if it's class 1 that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m09s)
00:23:09

[probability of that feature occurring if](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m11s)
00:23:11

[it's plus 2 and then the ratio of those](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m13s)
00:23:13

[two all right and in the paper that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m17s)
00:23:17

[we're actually load basing this off they](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m20s)
00:23:20

[call this P this Q and this right maybe](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m22s)
00:23:22

[I should just fill that in P here maybe](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m27s)
00:23:27

[then we'll say probability to make it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m34s)
00:23:34

[more obvious](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m35s)
00:23:35

[okay and so then we kind of said hey](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m41s)
00:23:41

[let's let's not use these ratios as the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m45s)
00:23:45

[coefficients in that in that matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m49s)
00:23:49

[multiply](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m53s)
00:23:53

[but let's instead like try and learn](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m54s)
00:23:54

[some coefficients you know so maybe](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m56s)
00:23:56

[start out with some random numbers you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h23m58s)
00:23:58

[know and then try and use stochastic](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m05s)
00:24:05

[gradient descent to find slightly better](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m07s)
00:24:07

[ones](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m09s)
00:24:09

[so you'll notice you know some important](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m11s)
00:24:11

[features here the R vector is a vector](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m14s)
00:24:14

[of Rank 1 and it's length is equal to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m19s)
00:24:19

[the number of features and of course our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m23s)
00:24:23

[logistic regression coefficient matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m27s)
00:24:27

[is also of length 1](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m29s)
00:24:29

[sorry Rank 1 and length 1/4 the number](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m32s)
00:24:32

[of features right and we know we're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m34s)
00:24:34

[saying like they're kind of two ways of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m36s)
00:24:36

[calculating the same kind of thing right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m38s)
00:24:38

[one based on theory one based on data so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m41s)
00:24:41

[here is like some of the numbers in R](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m46s)
00:24:46

[right remember it's using the log so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m49s)
00:24:49

[these numbers which are less than zero](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m51s)
00:24:51

[represent things which are more likely](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m54s)
00:24:54

[to be negative and these ones are here](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h24m58s)
00:24:58

[are more likely so this one here is more](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m00s)
00:25:00

[likely to be positive and so here's E ^](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m02s)
00:25:02

[that and so these are the ones we can](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m06s)
00:25:06

[compare to one rather than to zero so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m08s)
00:25:08

[I'm going to do something that hopefully](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m13s)
00:25:13

[is going to seem weird and so first of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m16s)
00:25:16

[all I'm going to talk about I got to say](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m21s)
00:25:21

[what we got to do and then I'm gonna try](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m24s)
00:25:24

[and describe why it's weird and then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m27s)
00:25:27

[we'll talk about why it may not be as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m29s)
00:25:29

[weird as we first thought so here's what](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m32s)
00:25:32

[we got to do we're going to take our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m33s)
00:25:33

[term document matrix and we're going to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m35s)
00:25:35

[multiply it by](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m39s)
00:25:39

[so what that means is we're gonna I can](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m43s)
00:25:43

[do it here in Excel right so we're going](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m45s)
00:25:45

[to say let's grab everything in our term](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m48s)
00:25:48

[document matrix and multiply it by the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m51s)
00:25:51

[equivalent value in the vector of our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m55s)
00:25:55

[right so this is like a broadcasted](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h25m57s)
00:25:57

[element-wise multiplication not a matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m00s)
00:26:00

[multiplication okay and that's what that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m03s)
00:26:03

[does](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m12s)
00:26:12

[okay so here is the value of the term](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m14s)
00:26:14

[document matrix times R in other words](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m18s)
00:26:18

[everywhere that a zero appears there a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m21s)
00:26:21

[zero appears here and every time a one](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m24s)
00:26:24

[appears here the equivalent value of R](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m27s)
00:26:27

[appears here so we haven't really we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m30s)
00:26:30

[haven't really changed much all right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m35s)
00:26:35

[we've just we've just kind of changed](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m37s)
00:26:37

[the ones into something else than two](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m40s)
00:26:40

[into the into the odds from that feature](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m42s)
00:26:42

[all right and so what we're now going to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m44s)
00:26:44

[do is we're going to use this as our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m47s)
00:26:47

[independent variables instead in our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m50s)
00:26:50

[logistic regression okay so here we are](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m53s)
00:26:53

[multiply x x NB x naive Bayes version is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h26m56s)
00:26:56

[x times R and now let's do a logistic](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m00s)
00:27:00

[regression fitting using those](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m04s)
00:27:04

[independent variables and let's then do](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m07s)
00:27:07

[that for the validation set okay and get](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m14s)
00:27:14

[the predictions and lo and behold we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m16s)
00:27:16

[have a better number okay so let me](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m20s)
00:27:20

[explain why this hopefully seem](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m28s)
00:27:28

[surprising given that we're just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m31s)
00:27:31

[multiplying oh I picked out the wrong](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m36s)
00:27:36

[ones I should have said ah not going](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m43s)
00:27:43

[okay that's actually uh I got the wrong](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m49s)
00:27:49

[number](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m52s)
00:27:52

[okay so that's our independent variables](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m53s)
00:27:53

[right and then the the logistic](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m57s)
00:27:57

[regression has come up with some set of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h27m59s)
00:27:59

[coefficients let's pretend for a moment](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m01s)
00:28:01

[that these are the coefficients that it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m03s)
00:28:03

[happened to come up with okay we could](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m05s)
00:28:05

[now say well let's not use this set](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m11s)
00:28:11

[let's not use this set of independent](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m15s)
00:28:15

[variables but let's use the original](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m18s)
00:28:18

[binarized feature matrix right and then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m20s)
00:28:20

[divide all of our coefficients by the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m23s)
00:28:23

[values in R and we're going to get](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m27s)
00:28:27

[exactly the same result mathematically](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m30s)
00:28:30

[so you know we've got our X naivebayes](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m34s)
00:28:34

[version of the independent variables and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m42s)
00:28:42

[we've got some some set of weights some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m45s)
00:28:45

[some sort of coefficients I'll call it W](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m50s)
00:28:50

[right W one let's see where it's found](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m52s)
00:28:52

[like this is a good set of coefficients](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h28m58s)
00:28:58

[for making our predictions from right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m00s)
00:29:00

[that X and B is simply equal to x times](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m02s)
00:29:02

[as in element wise x ah right so in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m10s)
00:29:10

[other words this is equal to x times ah](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m16s)
00:29:16

[times the weights and so like we could](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m24s)
00:29:24

[just change the weights to be that right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m27s)
00:29:27

[and get the same number so this ought to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m32s)
00:29:32

[mean that the change that we made to the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m36s)
00:29:36

[dependent variable shouldn't have made](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m41s)
00:29:41

[any difference because we can calculate](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m42s)
00:29:42

[exactly the same thing without making](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m46s)
00:29:46

[that change so there's the question why](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m47s)
00:29:47

[did it make a difference so in order to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m52s)
00:29:52

[answer this question I got to try and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m56s)
00:29:56

[get you all to try and think about this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m57s)
00:29:57

[in order to answer this question you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h29m58s)
00:29:58

[need to think about like okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m00s)
00:30:00

[what are the things that aren't](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m02s)
00:30:02

[mathematically the same why is why is it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m05s)
00:30:05

[not identical what are the reasons like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m07s)
00:30:07

[come up with some hypotheses what are](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m09s)
00:30:09

[some reasons that maybe we've actually](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m11s)
00:30:11

[ended up with a better answer and to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m13s)
00:30:13

[figure that out we need to first of all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m17s)
00:30:17

[start with like well why is it even a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m18s)
00:30:18

[different answer why is that different](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m19s)
00:30:19

[to that is it subtle all right what do](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m21s)
00:30:21

[you think I just wondering if there was](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m33s)
00:30:33

[two different kinds of multiplications](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m35s)
00:30:35

[you said that one is the element wise](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m36s)
00:30:36

[multiplication no they do end up](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m38s)
00:30:38

[mathematically being the same okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m40s)
00:30:40

[pretty much there's a minor in corporate](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m42s)
00:30:42

[not it's not that it's not some order](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m45s)
00:30:45

[operation see let's try](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m47s)
00:30:47

[kimchee you are on a roll today so let's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m49s)
00:30:49

[see how you go I feel like Z features](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m52s)
00:30:52

[aren't less correlated to each other I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m55s)
00:30:55

[mean I've made a claim that these are](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h30m59s)
00:30:59

[mathematically equivalent so so what are](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m02s)
00:31:02

[you saying really you know why are we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m07s)
00:31:07

[getting different answers it's good keep](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m10s)
00:31:10

[on coming up with hypotheses we need](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m17s)
00:31:17

[lots of wrong answers before we start](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m19s)
00:31:19

[finding it's really right ones it's like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m20s)
00:31:20

[that you know warmer hotter colder you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m21s)
00:31:21

[know Ernest you're gonna get as hot Oh](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m24s)
00:31:24

[does it have anything to do with the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m25s)
00:31:25

[regularization ah yes and is it the fact](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m27s)
00:31:27

[that when you let's start there right so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m29s)
00:31:29

[Ernest point here is like okay Jeremy](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m31s)
00:31:31

[you've said they're equivalent but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m34s)
00:31:34

[they're equivalent outcomes right but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m36s)
00:31:36

[you got through and through a process to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m38s)
00:31:38

[get there and that process included](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m40s)
00:31:40

[regularization and they're not](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m42s)
00:31:42

[necessarily equivalent regularization](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m43s)
00:31:43

[like our loss function as a penalty so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m45s)
00:31:45

[yeah help us think through Ernest how](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m49s)
00:31:49

[much that might impact things well this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m51s)
00:31:51

[is I'm just noticing that the numbers](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m53s)
00:31:53

[are bigger in the ones that have been](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m56s)
00:31:56

[weighted by the naive phase mm-hmm our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h31m58s)
00:31:58

[weights and so these are bigger and some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m01s)
00:32:01

[are smaller some are bigger right but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m05s)
00:32:05

[there are some bigger ones like the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m07s)
00:32:07

[variance between the columns is much](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m08s)
00:32:08

[higher the variance is bigger yeah I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m10s)
00:32:10

[think that's a very interesting insight](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m12s)
00:32:12

[okay that's all yeah okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m13s)
00:32:13

[so build on that prince has been on a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m15s)
00:32:15

[roll or month](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m23s)
00:32:23

[so here's not sure is it also consider](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m24s)
00:32:24

[like considering the dependency of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m28s)
00:32:28

[different words instead why this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m30s)
00:32:30

[performing better rather than all but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m32s)
00:32:32

[independent of each other no really I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m36s)
00:32:36

[mean it's it's you know again](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m38s)
00:32:38

[theoretically these are creating](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m39s)
00:32:39

[mathematically equivalent outputs so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m42s)
00:32:42

[they're not they're not doing something](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m46s)
00:32:46

[different except as Ernest mentioned](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m49s)
00:32:49

[they're getting impacted differently by](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m52s)
00:32:52

[regularization so what's so what's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m55s)
00:32:55

[regularization right regularization is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h32m59s)
00:32:59

[we start out with our that was the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m02s)
00:33:02

[weirdest thing I forgot to go to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m07s)
00:33:07

[screenwriting mode and it just turns out](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m08s)
00:33:08

[that you can actually write in Excel and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m11s)
00:33:11

[I had no idea that was true I still use](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m13s)
00:33:13

[screenwriting Rosewood's could kill up](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m17s)
00:33:17

[my spreadsheet I'd never trade so our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m18s)
00:33:18

[loss was equal to like our cross entropy](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m23s)
00:33:23

[loss you know based on the predictions](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m27s)
00:33:27

[of the predictions and the actuals right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m34s)
00:33:34

[plus our penalty so if your if your](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m39s)
00:33:39

[weights a large right then that piece](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m50s)
00:33:50

[gets bigger right and it drowns out that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m55s)
00:33:55

[piece right but that's actually the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h33m59s)
00:33:59

[piece we care about right we actually](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m01s)
00:34:01

[want it to be a good fit so we want to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m03s)
00:34:03

[have as little regularization going on](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m06s)
00:34:06

[as we can get away with we want so we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m08s)
00:34:08

[want to have less weights so here's the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m10s)
00:34:10

[thing right our value yes can you pass](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m15s)
00:34:15

[it over here we should let less weights](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m19s)
00:34:19

[did you mean lesser weights I do yeah](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m24s)
00:34:24

[yeah and I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m27s)
00:34:27

[use the two words are level equivalently](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m28s)
00:34:28

[which is not quite fair I agree but the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m31s)
00:34:31

[idea is that weights that are pretty](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m32s)
00:34:32

[close to zero were kind of not there so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m34s)
00:34:34

[here's the thing our values of ah you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m39s)
00:34:39

[know and I'm not a Bayesian weenie but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m43s)
00:34:43

[I'm still gonna use the word prior right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m45s)
00:34:45

[they're kind of like a prior so like we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m46s)
00:34:46

[think that the the different levels of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m49s)
00:34:49

[importance and positive or negative of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m54s)
00:34:54

[these different features might be](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m57s)
00:34:57

[something like that right we think that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h34m59s)
00:34:59

[like bad you know might be more](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m02s)
00:35:02

[correlated with negative then and good](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m08s)
00:35:08

[right so our kind of implicit assumption](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m12s)
00:35:12

[the before was that we have no priors so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m18s)
00:35:18

[in other words when we'd said squared](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m22s)
00:35:22

[weights we're saying a nonzero weight is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m24s)
00:35:24

[something we don't want to have right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m27s)
00:35:27

[but actually I think what I really want](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m29s)
00:35:29

[to say is that differing from the naive](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m31s)
00:35:31

[Bayes expectation is something I don't](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m36s)
00:35:36

[want to do right like only very from the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m39s)
00:35:39

[naive Bayes prior unless you have good](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m41s)
00:35:41

[reason to believe otherwise](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m45s)
00:35:45

[right and so that's actually what this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m47s)
00:35:47

[ends up doing right we end up saying you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m50s)
00:35:50

[know what we think this value is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m53s)
00:35:53

[probably three right and so if you're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h35m57s)
00:35:57

[going to like make it a lot bigger or a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m01s)
00:36:01

[lot smaller right that's going to create](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m03s)
00:36:03

[the kind of variation in weights that's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m06s)
00:36:06

[going to cause that squared term to go](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m09s)
00:36:09

[up right so so if you can you know just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m11s)
00:36:11

[leave all these values about similar to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m16s)
00:36:16

[where they are now all right and so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m18s)
00:36:18

[that's what the penalty term is now](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m20s)
00:36:20

[doing right the penalty term when our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m22s)
00:36:22

[inputs is already multiplied by our is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m25s)
00:36:25

[saying penalize things where we're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m27s)
00:36:27

[burying it from our naive Bayes prior](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m31s)
00:36:31

[can you pass it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m36s)
00:36:36

[why multiply only with our not constant](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m40s)
00:36:40

[like a square or something later when](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m44s)
00:36:44

[the variance would be much higher](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m46s)
00:36:46

[deciding because our our prior comes](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m47s)
00:36:47

[from an actual theoretical model right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m53s)
00:36:53

[so I said like I don't like to rely on](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m55s)
00:36:55

[the theory but I have if I have some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h36m57s)
00:36:57

[theory then you know maybe we should use](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m00s)
00:37:00

[that as our starting point rather than](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m03s)
00:37:03

[starting off by assuming everything's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m05s)
00:37:05

[equal so our prior said hey we've got](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m07s)
00:37:07

[this model coordinate phase and the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m10s)
00:37:10

[naive Bayes model said if the naive](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m12s)
00:37:12

[Bayes assumptions were correct then R is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m15s)
00:37:15

[the correct coefficient right in this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m19s)
00:37:19

[specific formulation that that's why we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m22s)
00:37:22

[pick that because our our prior is based](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m25s)
00:37:25

[on that that theory okay so this is a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m28s)
00:37:28

[really interesting insight which I never](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m36s)
00:37:36

[really see covered which is this idea is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m40s)
00:37:40

[that we can use these like you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m44s)
00:37:44

[traditional machine learning techniques](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m46s)
00:37:46

[we can imbue them with this kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m49s)
00:37:49

[Bayesian sense by by starting out you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m52s)
00:37:52

[know incorporating our theoretical](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h37m58s)
00:37:58

[expectations into the data that we give](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m00s)
00:38:00

[our model right and when we do so that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m04s)
00:38:04

[then means we don't have to regularize](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m06s)
00:38:06

[as much and that's good right because if](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m09s)
00:38:09

[we regularize a lot let's try it let's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m12s)
00:38:12

[go back to you know here's our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m18s)
00:38:18

[remember the the way they do it in the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m28s)
00:38:28

[eschaton logistic regression is this is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m31s)
00:38:31

[the reciprocal of the amount of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m33s)
00:38:33

[vectorization penalty so will kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m36s)
00:38:36

[add lots of regularization by making a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m41s)
00:38:41

[small so that like really hurts](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m44s)
00:38:44

[that really hurts our accuracy because](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m51s)
00:38:51

[now it's trying really hard to get those](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m53s)
00:38:53

[weights down the loss function is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m57s)
00:38:57

[overwhelmed by the need to reduce the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h38m59s)
00:38:59

[weights and the need to make it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m02s)
00:39:02

[predictive is kind of now seen as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m03s)
00:39:03

[totally unimportant right so so by kind](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m06s)
00:39:06

[of starting out and saying you know what](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m12s)
00:39:12

[don't push the weights down so that you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m14s)
00:39:14

[end up ignoring the the terms but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m17s)
00:39:17

[instead push them down so that you try](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m22s)
00:39:22

[to get rid of you know ignore](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m24s)
00:39:24

[differences from our expectation based](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m26s)
00:39:26

[on the naive Bayes formulation so that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m29s)
00:39:29

[ends up giving us a very nice result](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m38s)
00:39:38

[which actually was originally this this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m43s)
00:39:43

[technique was originally presented I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m46s)
00:39:46

[think about 2012 Chris Manning who's a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m48s)
00:39:48

[terrific NLP researcher up at Stanford](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m51s)
00:39:51

[and CETA Wang who I don't know but I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m52s)
00:39:52

[assume is awesome because his paper is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m56s)
00:39:56

[awesome they basically came up with this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h39m57s)
00:39:57

[with this idea and what they did was](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m00s)
00:40:00

[they compared it to a number of other](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m05s)
00:40:05

[approaches on a number of other data](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m08s)
00:40:08

[sets so one of the things they tried is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m11s)
00:40:11

[this one is the IMDB data set that and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m12s)
00:40:12

[so here's naive Bayes SVM on diagrams](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m15s)
00:40:15

[and as you can see this approach](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m18s)
00:40:18

[outperformed the other linear based](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m21s)
00:40:21

[approaches that they looked at and also](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m24s)
00:40:24

[some restricted Boltzmann machine kind](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m26s)
00:40:26

[of neural net based approaches they](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m31s)
00:40:31

[looked at now nowadays there are better](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m33s)
00:40:33

[ways there are you know there are better](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m36s)
00:40:36

[ways to do this and in fact in the deep](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m37s)
00:40:37

[learning course we showed](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m39s)
00:40:39

[new state-of-the-art result that we just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m40s)
00:40:40

[developed at first a a that gets well](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m41s)
00:40:41

[over ninety four percent but still you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m44s)
00:40:44

[know like particularly for a linear](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m48s)
00:40:48

[technique that's easy fast and intuitive](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m49s)
00:40:49

[this is pretty good and you'll notice](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m52s)
00:40:52

[when they when they did this they only](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m54s)
00:40:54

[used by grams and I assume that's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m56s)
00:40:56

[because they I looked at their code and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h40m58s)
00:40:58

[it was kind of pretty slow and ugly you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m00s)
00:41:00

[know I figured out a way to optimize it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m03s)
00:41:03

[a lot more as you saw and so we were](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m05s)
00:41:05

[able to use here try grams and so we get](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m07s)
00:41:07

[quite a lot better so we've got ninety](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m11s)
00:41:11

[one point eight versus a ninety one](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m13s)
00:41:13

[point two but other than that it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m14s)
00:41:14

[identical also I mean they used a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m16s)
00:41:16

[support vector machine which is almost](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m19s)
00:41:19

[identical to a logistic regression in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m21s)
00:41:21

[this case so there's some minor](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m24s)
00:41:24

[differences right so I think that's a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m28s)
00:41:28

[pretty cool result and you know I will](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m31s)
00:41:31

[mention you know what you get to see](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m34s)
00:41:34

[here in class is the result of like many](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m38s)
00:41:38

[weeks and often many months of research](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m42s)
00:41:42

[that I do and so I don't want you to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m45s)
00:41:45

[think like this stuff is obvious it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m47s)
00:41:47

[not at all like reading this paper](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m50s)
00:41:50

[there's no description in the paper of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m52s)
00:41:52

[like why they use this model how it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m55s)
00:41:55

[different why they thought it works you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h41m59s)
00:41:59

[know it took me a week or two to even](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m01s)
00:42:01

[realize that it's kind of like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m03s)
00:42:03

[mathematically equivalent to a normal](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m05s)
00:42:05

[logistic regression and then a few more](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m07s)
00:42:07

[weeks to realize that the difference is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m10s)
00:42:10

[actually in the regularization you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m11s)
00:42:11

[like this is kind of like machine](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m15s)
00:42:15

[learning as I'm sure you've noticed from](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m18s)
00:42:18

[the Carroll competitions you enter you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m19s)
00:42:19

[know like you come up with a thousand](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m21s)
00:42:21

[good ideas 999 of them no matter how](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m23s)
00:42:23

[confident you are they're going to be](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m27s)
00:42:27

[great they always turn out to be](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m28s)
00:42:28

[you know and then finally after four](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m29s)
00:42:29

[weeks one of them finally works and kind](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m31s)
00:42:31

[of gives you the enthusiasm to spend](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m34s)
00:42:34

[another four weeks of misery and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m37s)
00:42:37

[frustration this is the norm right and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m39s)
00:42:39

[and like for sure that the the best](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m43s)
00:42:43

[practitioners I know in machine learning](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m49s)
00:42:49

[all share one particular trait in common](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m51s)
00:42:51

[which](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m53s)
00:42:53

[they're very very tenacious you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m54s)
00:42:54

[also known as stubborn and bloody-minded](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m56s)
00:42:56

[right which is definitely a reputation I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h42m59s)
00:42:59

[seem to have probably fare along with](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m01s)
00:43:01

[another thing which is that they're all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m06s)
00:43:06

[very good coders you know they're very](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m08s)
00:43:08

[good at turning their ideas into new](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m10s)
00:43:10

[code so yeah so you know this was like a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m12s)
00:43:12

[really interesting experience for me](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m17s)
00:43:17

[working through this a few months ago to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m19s)
00:43:19

[try and like figure out how to at least](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m21s)
00:43:21

[you know how to explain why this at](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m24s)
00:43:24

[there at the time kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m28s)
00:43:28

[state-of-the-art result exists and so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m29s)
00:43:29

[once I figured that out I was actually](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m31s)
00:43:31

[able to build on top of it and make it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m33s)
00:43:33

[quite a bit better and I'll show you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m35s)
00:43:35

[what I did and this is where it was very](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m38s)
00:43:38

[very handy to have hi torch at my](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m41s)
00:43:41

[disposal because I was able to kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m44s)
00:43:44

[create something that was customized](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m47s)
00:43:47

[just the way that I want it to be and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m49s)
00:43:49

[also very fast by using the GPU so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m52s)
00:43:52

[here's the kind of fast AI version of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m56s)
00:43:56

[the NBS vm actually my friend Steven](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h43m58s)
00:43:58

[marady who's a terrific researcher in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m02s)
00:44:02

[NLP has christened this the NBS VM plus](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m06s)
00:44:06

[plus which I thought was lovely so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m10s)
00:44:10

[here's that even though there is no SVM](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m12s)
00:44:12

[it's a logistic regression but as I said](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m14s)
00:44:14

[nearly exactly the same thing so let me](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m16s)
00:44:16

[first of all show you like the code so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m20s)
00:44:20

[this is like we try to like once I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m22s)
00:44:22

[figure out like okay this is like the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m24s)
00:44:24

[best way I can come up with to do a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m25s)
00:44:25

[linear bag of words model I kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m27s)
00:44:27

[embed it into fast AI so you can just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m29s)
00:44:29

[write a couple of lines of code so the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m31s)
00:44:31

[code is basically hey I want to create a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m32s)
00:44:32

[data class for text classification I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m34s)
00:44:34

[want to create it from a bag of words](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m38s)
00:44:38

[all right here is my bag of words here](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m40s)
00:44:40

[are my labels here is the same thing for](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m43s)
00:44:43

[the validation set and use up to 2,000](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m46s)
00:44:46

[unique words per review right which is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m52s)
00:44:52

[plenty so then from that model data](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h44m55s)
00:44:55

[construct a learner which is kind of the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m02s)
00:45:02

[faster I generalization of a moral](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m05s)
00:45:05

[which is based on a dot product of naive](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m07s)
00:45:07

[Bayes and then fit that model and then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m11s)
00:45:11

[do a few epochs and after five epochs I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m16s)
00:45:16

[was already up to ninety two point two](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m19s)
00:45:19

[okay so this is now like you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m21s)
00:45:21

[getting quite well above this this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m24s)
00:45:24

[linear based one so let me show you the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m28s)
00:45:28

[code for for that so the code is like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m32s)
00:45:32

[horrifyingly short that's it right and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m42s)
00:45:42

[it'll also look on the whole extremely](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m46s)
00:45:46

[familiar right there's if there's a few](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m50s)
00:45:50

[tweaks here pretend this thing that says](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m52s)
00:45:52

[embedding pretend it actually says](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m54s)
00:45:54

[linear okay I'm going to show you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m56s)
00:45:56

[embedding in a moment pretend it says](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m57s)
00:45:57

[linear so we've got basically a linear](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h45m59s)
00:45:59

[layer where the number of features](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m00s)
00:46:00

[coming with the number of features as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m02s)
00:46:02

[the rows and remember SK learn features](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m04s)
00:46:04

[means number of words basically and then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m08s)
00:46:08

[for each row we're going to create one](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m11s)
00:46:11

[weight which makes sense right for like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m14s)
00:46:14

[a logistic regression every every sort](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m16s)
00:46:16

[of for each row for each word each word](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m19s)
00:46:19

[has one weight and then we're going to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m21s)
00:46:21

[be multiplying it by the our values so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m26s)
00:46:26

[each word we have one our value per](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m30s)
00:46:30

[class so I actually made this so this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m35s)
00:46:35

[can handle like not just positive versus](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m36s)
00:46:36

[negative but maybe figuring out like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m39s)
00:46:39

[which author created this work they're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m40s)
00:46:40

[cooking five or six authors whatever](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m43s)
00:46:43

[right and basically we kind of use those](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m45s)
00:46:45

[linear layers to to get the the value of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m49s)
00:46:49

[the weight and the value of the R and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m54s)
00:46:54

[then we take the weight times the R and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h46m56s)
00:46:56

[then sum it up and so that's just a dot](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m01s)
00:47:01

[product okay so just just a simple dot](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m04s)
00:47:04

[product just as we would do for any](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m08s)
00:47:08

[logistic regression and then do the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m09s)
00:47:09

[softmax](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m12s)
00:47:12

[so the very minor tweak the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m14s)
00:47:14

[we add to get the the better result is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m20s)
00:47:20

[this the main one really is this year](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m22s)
00:47:22

[this plus something right and the thing](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m25s)
00:47:25

[I'm adding is it's a parameter but I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m28s)
00:47:28

[pretty much always use this this version](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m31s)
00:47:31

[of this value 2.4 so what does this do](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m33s)
00:47:33

[so what this is doing is it's again kind](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m36s)
00:47:36

[of changing the prior right so if you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m40s)
00:47:40

[think about it even once we used this R](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m43s)
00:47:43

[times the term document matrix as their](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m51s)
00:47:51

[independent variables you really want to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m54s)
00:47:54

[start with a question okay the penalty](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h47m57s)
00:47:57

[terms are still pushing W down to 0](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m00s)
00:48:00

[right so what did it mean for W to be 0](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m02s)
00:48:02

[all right so what would it mean if we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m07s)
00:48:07

[had you know coefficient 0 0 0 0 0 all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m09s)
00:48:09

[right so what that would do when we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m16s)
00:48:16

[go.okay this matrix times these](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m18s)
00:48:18

[coefficients we still get 0 right so a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m21s)
00:48:21

[weight of 0 still ends up saying I have](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m25s)
00:48:25

[no opinion on whether this thing is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m28s)
00:48:28

[positive or negative on the other hand](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m29s)
00:48:29

[if they were all one right then it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m33s)
00:48:33

[basically says my opinion is that the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m39s)
00:48:39

[naive Bayes coefficients are exactly](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m42s)
00:48:42

[right okay and so the idea is that I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m45s)
00:48:45

[said 0 is almost certainly not the right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m50s)
00:48:50

[prior right we shouldn't really be](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m56s)
00:48:56

[saying if there's no coefficient it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h48m58s)
00:48:58

[means ignore the naive Bayes coefficient](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m00s)
00:49:00

[one is probably too high right because](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m02s)
00:49:02

[we actually think that naive Bayes is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m06s)
00:49:06

[only kind of part of the answer all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m08s)
00:49:08

[right and so I played around with a few](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m10s)
00:49:10

[different data sets where I basically](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m12s)
00:49:12

[said take the weights and add to them](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m14s)
00:49:14

[some constant right and so 0 would](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m21s)
00:49:21

[become in this case 0.4](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m26s)
00:49:26

[all right so in other words the the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m29s)
00:49:29

[regularization](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m33s)
00:49:33

[penalty is pushing the weights not](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m35s)
00:49:35

[towards zero but towards this value](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m38s)
00:49:38

[right and I found that across a number](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m41s)
00:49:41

[of data sets zero point four works](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m43s)
00:49:43

[pretty well but and it's pretty](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m46s)
00:49:46

[resilient alright so again this is the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m48s)
00:49:48

[basic idea is to kind of like get the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m51s)
00:49:51

[best of both worlds you know where where](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m54s)
00:49:54

[we're learning from the data using a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m56s)
00:49:56

[simple model but we're incorporating you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h49m59s)
00:49:59

[know our prior knowledge as best as we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m04s)
00:50:04

[can and so it turns out when you say](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m07s)
00:50:07

[okay let's let's tell it you know as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m09s)
00:50:09

[white matrix of zeros actually means](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m13s)
00:50:13

[that you should use about you know about](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m16s)
00:50:16

[half of the values that ends up that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m18s)
00:50:18

[ends up working better than the prior](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m23s)
00:50:23

[that the weights should all be 0 yes is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m25s)
00:50:25

[the the weights the W is it that the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m32s)
00:50:32

[point for the amount of regression](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m35s)
00:50:35

[required the amount of so we have this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m38s)
00:50:38

[you know bad things we have the term](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m43s)
00:50:43

[where we reduce the amount of error the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m46s)
00:50:46

[prediction error rmse plus we have the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m48s)
00:50:48

[regularization and is it W to the point](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m51s)
00:50:51

[for denote the amount of visualization](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m53s)
00:50:53

[required so W are the weights right so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m55s)
00:50:55

[this is calculating our activations okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h50m59s)
00:50:59

[so we calculate our activations as being](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m02s)
00:51:02

[equal to the weights times there are](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m05s)
00:51:05

[some right so that's just our normal](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m11s)
00:51:11

[normal linear function right so so the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m18s)
00:51:18

[the thing which is being penalized is my](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m23s)
00:51:23

[weight matrix that's what gets penalized](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m28s)
00:51:28

[so by saying hey you know what don't](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m31s)
00:51:31

[just use W use W plus 0.4 so that's not](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m33s)
00:51:33

[being penalized](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m38s)
00:51:38

[it's not part of the weight matrix okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m39s)
00:51:39

[so effectively the weight matrix gets](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m42s)
00:51:42

[point four for free](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m45s)
00:51:45

[yeah so by doing this even after](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m48s)
00:51:48

[regularization then every I'm sorry](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m54s)
00:51:54

[every feature is getting some form of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h51m58s)
00:51:58

[fate some form of weight or something](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m00s)
00:52:00

[um not necessarily because it could end](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m03s)
00:52:03

[up choosing a coefficient of negative](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m05s)
00:52:05

[0.4 for a feature and so that would say](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m07s)
00:52:07

[you know what](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m11s)
00:52:11

[even though though naive Bayes says it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m13s)
00:52:13

[the AH should be whatever for this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m14s)
00:52:14

[feature I think you should totally](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m16s)
00:52:16

[ignore it yeah great questions okay we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m18s)
00:52:18

[started at 20 past - okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m27s)
00:52:27

[let's take a break for about eight](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m32s)
00:52:32

[minutes or so and start back about 25 -](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m35s)
00:52:35

[okay so a couple of questions at the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m44s)
00:52:44

[break the first was just for a kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m48s)
00:52:48

[reminder or a bit of a summary as to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m54s)
00:52:54

[what's going on here right and so here](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h52m57s)
00:52:57

[we have W plus I'm writing it out yeah](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m02s)
00:53:02

[plus adjusted weight of weight](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m10s)
00:53:10

[adjustment times right so so normally](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m15s)
00:53:15

[what we were doing so normally what we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m21s)
00:53:21

[are doing is saying hey logistic](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m27s)
00:53:27

[regression is basically WX right I'm](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m28s)
00:53:28

[going to ignore the bias okay and then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m33s)
00:53:33

[we were changing it to be W dot times X](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m35s)
00:53:35

[right and then we were kind of saying](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m43s)
00:53:43

[let's do that bit first right although](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m46s)
00:53:46

[in this particular case actually now I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m53s)
00:53:53

[look at it I'm doing it in this code it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m54s)
00:53:54

[doesn't matter obviously in this code](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m57s)
00:53:57

[I'm actually doing](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h53m58s)
00:53:58

[and during this bit first and so so this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h54m04s)
00:54:04

[thing here actually I call it W which is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h54m17s)
00:54:17

[probably pretty bad it's actually W](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h54m20s)
00:54:20

[times X right so so instead of W times X](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h54m22s)
00:54:22

[times R I've got W times X plus a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h54m29s)
00:54:29

[constant times R right so the key idea](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h54m35s)
00:54:35

[here is that regularization can't draw](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h54m41s)
00:54:41

[in yellow that's fair enough](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h54m50s)
00:54:50

[regularization wants the weights to be 0](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h54m52s)
00:54:52

[right because we're trying it's trying](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h54m58s)
00:54:58

[to reduce that okay and so what we're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m01s)
00:55:01

[saying is like ok we want to push the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m07s)
00:55:07

[weights towards 0 because we're saying](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m10s)
00:55:10

[like that's our like default starting](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m12s)
00:55:12

[point expectation is the weights 0 and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m15s)
00:55:15

[so we want to be in a situation where if](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m18s)
00:55:18

[the weights are 0 then we have a model](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m21s)
00:55:21

[that like makes theoretical or intuitive](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m24s)
00:55:24

[sense to us right this model if the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m28s)
00:55:28

[weights are 0 doesn't make intuitive](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m34s)
00:55:34

[sense to us right because it's saying](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m36s)
00:55:36

[hey multiply everything by 0 gets rid of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m38s)
00:55:38

[all of that and gets rid of that as well](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m41s)
00:55:41

[and we were actually saying no we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m43s)
00:55:43

[actually think our R is useful we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m45s)
00:55:45

[actually want to keep that right so so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m47s)
00:55:47

[instead we say you know what let's take](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m53s)
00:55:53

[that piece here and add 0.4 to it all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h55m56s)
00:55:56

[right so now if the regularizer is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m02s)
00:56:02

[pushing the weights towards 0 then it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m05s)
00:56:05

[pushing the value of this sum towards](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m08s)
00:56:08

[0.4](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m11s)
00:56:11

[right and so therefore it's pushing a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m12s)
00:56:12

[whole model to 0.4 times R right so in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m15s)
00:56:15

[other words our kind of default starting](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m20s)
00:56:20

[point if you've regularize to all the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m23s)
00:56:23

[weights out altogether is to say yeah](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m25s)
00:56:25

[you know let's use a bit of our that's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m27s)
00:56:27

[probably a good idea okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m29s)
00:56:29

[[Music]](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m33s)
00:56:33

[so that's the idea right that's the idea](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m35s)
00:56:35

[is basically you know what happens when](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m37s)
00:56:37

[when that's zero but you and you want](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m40s)
00:56:40

[that to like be something sensible](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m43s)
00:56:43

[because otherwise regularizing the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m46s)
00:56:46

[weights to move in that direction](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m50s)
00:56:50

[wouldn't be such a good idea okay second](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m51s)
00:56:51

[question was about engrams so the N in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h56m55s)
00:56:55

[Engram can be uni by try whatever one](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m06s)
00:57:06

[two three whatever grounds so so the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m10s)
00:57:10

[this movie is good right it has four](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m13s)
00:57:13

[unique grams this movie is good it has](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m19s)
00:57:19

[three by grams this movie movie is is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m25s)
00:57:25

[good it has two trigrams this movie is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m30s)
00:57:30

[movie is good okay doc can you pass it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m35s)
00:57:35

[do you mind go back to the double ad](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m45s)
00:57:45

[change that zero point four stuff yeah](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m48s)
00:57:48

[so I was wondering if this adjustment](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m50s)
00:57:50

[will harm the predictability of the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m53s)
00:57:53

[model because think of extreme extreme](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m55s)
00:57:55

[case if it's not zero point four if it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h57m58s)
00:57:58

[four thousand and or black coefficients](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m01s)
00:58:01

[will be like right so so exactly so so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m04s)
00:58:04

[our prior needs to make sense and so our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m08s)
00:58:08

[prior here and you know this is why it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m11s)
00:58:11

[called dot prod NB is there prior is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m13s)
00:58:13

[that this is something where we think](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m16s)
00:58:16

[naive Bayes is a good prior right and so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m18s)
00:58:18

[naive Bayes says that our equals](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m22s)
00:58:22

[p over that's not how you write P P over](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m26s)
00:58:26

[Q I have not had much sleep P over Q is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m31s)
00:58:31

[a good prayer and not only do we think](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m35s)
00:58:35

[it's a good prior that we think our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m37s)
00:58:37

[times X plus B is a good model that's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m42s)
00:58:42

[that's the naive Bayes model so in other](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m48s)
00:58:48

[words we expect that you know a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m49s)
00:58:49

[coefficient of one is a good coefficient](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m53s)
00:58:53

[not not 4,000 yeah so we think](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h58m57s)
00:58:57

[specifically we don't think we think 0](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m00s)
00:59:00

[is probably not a good coefficient all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m02s)
00:59:02

[right but we also think that maybe the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m05s)
00:59:05

[naive Bayes version is a little](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m09s)
00:59:09

[overconfident](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m11s)
00:59:11

[so maybe one's a little high so we're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m12s)
00:59:12

[pretty sure that the right number](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m14s)
00:59:14

[assuming that our moral only Bayes model](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m16s)
00:59:16

[is appropriate is between 0 &amp; 1](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m19s)
00:59:19

[no but what I was thinking is as long as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m23s)
00:59:23

[it's not 0 you are pushing those](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m27s)
00:59:27

[coefficients that are supposed to be 0](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m30s)
00:59:30

[to something not zero and make the like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m32s)
00:59:32

[high coefficients less distinctive from](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m36s)
00:59:36

[0 coefficients well but you see they're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m40s)
00:59:40

[not supposed to be 0 they're supposed to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m42s)
00:59:42

[be are like that's that's what they're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m45s)
00:59:45

[supposed to be they're supposed to be](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m48s)
00:59:48

[are right and so and remember this is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m50s)
00:59:50

[inside our forward function so this is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m55s)
00:59:55

[part of what we're taking the gradient](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m57s)
00:59:57

[of right so it's basically saying okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=00h59m59s)
00:59:59

[we're still gonna you know you can still](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m03s)
01:00:03

[set self W to anything you like but just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m04s)
01:00:04

[the regularizer wants it to be zero and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m10s)
01:00:10

[so all we're saying is okay if if you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m14s)
01:00:14

[want it to be zero then I'll try to make](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m17s)
01:00:17

[0 B you know give a sensible answer](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m19s)
01:00:19

[that's the basic idea and like yeah](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m23s)
01:00:23

[nothing says point fours perfect for](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m26s)
01:00:26

[every data set I've tried a few](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m28s)
01:00:28

[different data sets and found various](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m30s)
01:00:30

[numbers between point three and point](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m32s)
01:00:32

[six that are optimal but I've never](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m33s)
01:00:33

[found one where point four is less good](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m36s)
01:00:36

[than](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m39s)
01:00:39

[zero which is not surprising and I've](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m40s)
01:00:40

[also never found one where one it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m42s)
01:00:42

[better right so the idea is like this is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m44s)
01:00:44

[a reasonable default but it's another](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m46s)
01:00:46

[parameter you can play with which I kind](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m47s)
01:00:47

[of like right it's another thing you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m49s)
01:00:49

[could use grid search or whatever to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m50s)
01:00:50

[figure out from your data set what's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m54s)
01:00:54

[best and you know really the key here](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m56s)
01:00:56

[being every model before this one as far](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h00m58s)
01:00:58

[as I know has implicitly assumed it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m03s)
01:01:03

[should be zero because they just they](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m05s)
01:01:05

[don't have this parameter right and you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m07s)
01:01:07

[know by the way I've actually got a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m09s)
01:01:09

[second parameter here as well which is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m10s)
01:01:10

[the same thing I do to R is actually](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m13s)
01:01:13

[divided by a parameter which I'm not](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m15s)
01:01:15

[going to worry too much about it now but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m19s)
01:01:19

[again it's another parameter you can use](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m20s)
01:01:20

[to kind of adjust what the nature of the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m22s)
01:01:22

[regularization is you know and I mean in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m24s)
01:01:24

[the end I'm a empiricist not a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m28s)
01:01:28

[theoretician you know the I thought this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m31s)
01:01:31

[seemed like a good idea](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m32s)
01:01:32

[nearly all of my things that seem like a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m33s)
01:01:33

[good idea turn out to be stupid](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m35s)
01:01:35

[this particular one Dave good results](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m37s)
01:01:37

[you know on this data set and a few](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m40s)
01:01:40

[other ones as well okay could you pass](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m43s)
01:01:43

[that newest data yep yeah I'm sure a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m45s)
01:01:45

[little bit confused about the W plus W](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m48s)
01:01:48

[is it huh so you mentioned that we do W](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m51s)
01:01:51

[plus W adjusted so that the coefficients](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m56s)
01:01:56

[don't get set to zero that we place some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h01m59s)
01:01:59

[importance on the priors but you also](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m01s)
01:02:01

[said that the the effect of learning can](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m04s)
01:02:04

[be that W get set to a negative value](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m07s)
01:02:07

[which is mentally W plus W right zero so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m09s)
01:02:09

[if if we are we are allowing the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m13s)
01:02:13

[learning process to indeed set the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m16s)
01:02:16

[priors to zero so why is that in any way](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m19s)
01:02:19

[different from just having W because](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m24s)
01:02:24

[yeah great question because of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m26s)
01:02:26

[regularization because we're penalizing](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m27s)
01:02:27

[it by that right so in other words we're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m29s)
01:02:29

[saying you know what if you're if the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m35s)
01:02:35

[best thing to do is to ignore the value](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m37s)
01:02:37

[of R that'll cost you you're going to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m39s)
01:02:39

[have to set W to a negative number right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m42s)
01:02:42

[so only do that if that's fairly a good](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m46s)
01:02:46

[idea unless it's clearly a good idea](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m49s)
01:02:49

[then you should leave](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m51s)
01:02:51

[leave it where it is that that's the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m53s)
01:02:53

[only reason like all of this stuff we've](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m57s)
01:02:57

[done today is basically entirely about](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h02m59s)
01:02:59

[you know maximizing the advantage we get](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m03s)
01:03:03

[from regularization and saying](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m06s)
01:03:06

[regularization pushes us towards some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m07s)
01:03:07

[default assumption and nearly all of the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m11s)
01:03:11

[machine learning literature assumes that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m14s)
01:03:14

[default assumption is everything zero](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m15s)
01:03:15

[and I'm saying like it turns out you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m18s)
01:03:18

[know it makes sense theoretically and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m22s)
01:03:22

[turns out empirically that actually you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m23s)
01:03:23

[should decide what your default](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m25s)
01:03:25

[assumption is and that'll give you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m26s)
01:03:26

[better results so would it be right to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m29s)
01:03:29

[say that in a way you are putting an](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m31s)
01:03:31

[additional hurdle in the along the way](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m35s)
01:03:35

[towards getting all coefficients to zero](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m37s)
01:03:37

[so it will be able to do that if it is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m39s)
01:03:39

[really worth it yeah exactly so I'd say](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m42s)
01:03:42

[like the default herd or without this is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m44s)
01:03:44

[is making a coefficient non zero is the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m46s)
01:03:46

[heck hurdle and now I'm saying no the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m49s)
01:03:49

[coefficient not be equal to 0.40 so this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h03m53s)
01:03:53

[is some of the W squared in to see some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m04s)
01:04:04

[of into some lambda or C penalty](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m09s)
01:04:09

[constant yeah yeah times something yeah](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m11s)
01:04:11

[so the beta K should also depend on the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m14s)
01:04:14

[value of C if it is very less like if C](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m16s)
01:04:16

[is I say to you - hey yeah so if a is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m20s)
01:04:20

[point one then the wage might not go](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m25s)
01:04:25

[towards zero yeah then we might not need](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m28s)
01:04:28

[weight decay so well that the whatever](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m31s)
01:04:31

[this value I mean if the if the value of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m34s)
01:04:34

[this is zero then there is no](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m36s)
01:04:36

[recordation right but if this value is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m37s)
01:04:37

[higher than zero then there is some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m40s)
01:04:40

[penalty right and and presumably we've](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m43s)
01:04:43

[set it to non zero because we're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m46s)
01:04:46

[overfitting so he wants some penalty and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m48s)
01:04:48

[so if there is some penalty then then my](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m50s)
01:04:50

[assertion is that we should penalize](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m55s)
01:04:55

[things that are different to our prior](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m58s)
01:04:58

[not that we should penalize things that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h04m59s)
01:04:59

[are different to zero and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m02s)
01:05:02

[prior is that things should be you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m06s)
01:05:06

[around about equal to our ok let's move](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m09s)
01:05:09

[on thanks for the great questions I want](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m15s)
01:05:15

[to talk about embedding I said pretend](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m18s)
01:05:18

[it's linear and indeed we can pretend](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m26s)
01:05:26

[it's linear let me show you how much we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m28s)
01:05:28

[can pretend it's linear as in n n dot](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m30s)
01:05:30

[linear create a linear layer here is our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m32s)
01:05:32

[data matrix alright here are our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m37s)
01:05:37

[coefficients if we're in the R version](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m41s)
01:05:41

[here are coefficients are right so if we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m43s)
01:05:43

[were to put those into a column vector](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m47s)
01:05:47

[like so right then we could do a matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m55s)
01:05:55

[multiply of that by that right and so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h05m59s)
01:05:59

[we're going to end up with so here's our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h06m06s)
01:06:06

[matrix here's our vector right so we're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h06m13s)
01:06:13

[going to end up with 1 times 1 plus 1](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h06m22s)
01:06:22

[times 1 1 times 1 1 times 3 right 0](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h06m26s)
01:06:26

[times 1 0 times point 3 all right and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h06m39s)
01:06:39

[then the next one 0 times 1 1 times 1 so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h06m44s)
01:06:44

[forth ok so like that the matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h06m46s)
01:06:46

[multiply you know of this independent](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h06m48s)
01:06:48

[variable matrix by this coefficient](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h06m54s)
01:06:54

[matrix is going to give us an answer](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h06m58s)
01:06:58

[ok so that's that is just a matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m00s)
01:07:00

[multiply so the question is like ok well](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m03s)
01:07:03

[why didn't Jeremy right and n minion why](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m06s)
01:07:06

[did Jeremy right and n dot embedding and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m10s)
01:07:10

[the reason is because if you recall we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m13s)
01:07:13

[don't actually store it like this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m16s)
01:07:16

[because this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m18s)
01:07:18

[actually of whit's 800,000 and of height](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m20s)
01:07:20

[25,000 right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m25s)
01:07:25

[so rather than storing it like this we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m27s)
01:07:27

[actually store it as 0 1 2 3 right 1 2 3](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m30s)
01:07:30

[4 0 1 2 5 1 2 4 5 okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m40s)
01:07:40

[that's actually how we store it that is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m53s)
01:07:53

[this bag of words contains which word](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h07m57s)
01:07:57

[indexes that makes sense ok so that's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m01s)
01:08:01

[like this is like a sparse way of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m06s)
01:08:06

[storing it right it's just list out the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m11s)
01:08:11

[indexes in each sentence so given that I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m14s)
01:08:14

[want to now do that matrix multiply that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m20s)
01:08:20

[I just showed you to create that same](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m24s)
01:08:24

[outcome right but I want to do it from](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m27s)
01:08:27

[this representation so if you think](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m31s)
01:08:31

[about it all this is actually doing is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m35s)
01:08:35

[it saying a 1 hot you know this is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m39s)
01:08:39

[basically one hot encoded right it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m43s)
01:08:43

[kind of like a dummy dummy matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m46s)
01:08:46

[version does it have the word this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m48s)
01:08:48

[doesn't have the word movie doesn't have](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m49s)
01:08:49

[the word is and so forth so if we took](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m51s)
01:08:51

[the simple version of like doesn't have](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m55s)
01:08:55

[the word this 100 right and we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h08m56s)
01:08:56

[multiplied that by that right then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m02s)
01:09:02

[that's just going to return the first](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m09s)
01:09:09

[item that makes sense so in general a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m12s)
01:09:12

[one hot encoded vector times a matrix is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m20s)
01:09:20

[identical to looking up that matrix to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m27s)
01:09:27

[find the end](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m31s)
01:09:31

[row in it all right so this is identical](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m32s)
01:09:32

[to saying find the zero first second and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m35s)
01:09:35

[fifth coefficients right so they're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m39s)
01:09:39

[they're the same they're exactly the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m43s)
01:09:43

[same thing and like it doesn't like in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m45s)
01:09:45

[this case I only have one coefficient](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m47s)
01:09:47

[per feature right but actually the way I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m51s)
01:09:51

[did this was to have one coefficient per](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m54s)
01:09:54

[feature for each class right so in this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h09m59s)
01:09:59

[case is both positive and negative so I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m02s)
01:10:02

[actually had kind of like an AA positive](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m05s)
01:10:05

[and a negative so our negative would be](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m07s)
01:10:07

[just the opposite right equals that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m11s)
01:10:11

[divided by that now in the binary case](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m13s)
01:10:13

[obviously it's redundant to have both](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m17s)
01:10:17

[but what if it was like what's the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m20s)
01:10:20

[author of this text is it Jeremy or](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m23s)
01:10:23

[Savannah or Terrence right now we've got](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m27s)
01:10:27

[three categories we want three values of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m30s)
01:10:30

[R right so the nice thing is doing this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m33s)
01:10:33

[sparse version you know you can just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m36s)
01:10:36

[look up you know the 0th and the first](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m39s)
01:10:39

[and the second and the fifth alright and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m43s)
01:10:43

[again it's identical mathematically](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m47s)
01:10:47

[identical to a multiplying by a one](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m50s)
01:10:50

[Haughton coded matrix but when you have](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m53s)
01:10:53

[sparse inputs it's obviously much much](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h10m57s)
01:10:57

[more efficient so this computational](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m00s)
01:11:00

[trick which is mathematically identical](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m06s)
01:11:06

[to not conceptually analogous to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m10s)
01:11:10

[mathematically identical to multiplying](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m12s)
01:11:12

[by a one hot encoded matrix is called an](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m15s)
01:11:15

[embedding right so I'm sure you've all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m17s)
01:11:17

[heard or most of you probably heard](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m20s)
01:11:20

[about embeddings like word embeddings](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m21s)
01:11:21

[word to their core glove or whatever and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m24s)
01:11:24

[people love to make them sound like this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m27s)
01:11:27

[amazing new complex neural net thing](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m31s)
01:11:31

[right they're not embedding means make a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m35s)
01:11:35

[multiplication by a one hot encoded](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m40s)
01:11:40

[matrix faster by replacing it with a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m42s)
01:11:42

[simple array](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m45s)
01:11:45

[cup okay so that's why I said you can](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m46s)
01:11:46

[think of this as if it said self W](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m50s)
01:11:50

[equals n n dot linear and F plus one by](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m54s)
01:11:54

[one right because it actually does the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h11m57s)
01:11:57

[same thing right it actually is a matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m01s)
01:12:01

[with those dimensions this actually is a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m04s)
01:12:04

[matrix with those dimensions right it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m06s)
01:12:06

[a linear layer but it's expecting that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m09s)
01:12:09

[the input we're going to give it is not](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m14s)
01:12:14

[actually one hot encoded matrix but is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m15s)
01:12:15

[actually a list of integers right the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m19s)
01:12:19

[indexes for each word of each item so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m22s)
01:12:22

[you can see that the forward function in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m27s)
01:12:27

[fast AI automatically gets for this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m28s)
01:12:28

[Werner for feature indexes right so they](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m32s)
01:12:32

[come from the sparse matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m36s)
01:12:36

[automatically numpy makes it very easy](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m39s)
01:12:39

[to just grab those those indexes okay so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m41s)
01:12:41

[in other words there we've got here](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m47s)
01:12:47

[we've got a list of H word index of a of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m49s)
01:12:49

[the 800-thousand that are in this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m53s)
01:12:53

[document and so then this here says look](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m55s)
01:12:55

[up each of those in our embedding matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h12m59s)
01:12:59

[which is got 800,000 rows and return](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m02s)
01:13:02

[each thing that you find okay so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m05s)
01:13:05

[mathematically identical to multiplying](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m10s)
01:13:10

[by the one hunting coded matrix so make](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m15s)
01:13:15

[sense so that's all an embedding is and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m19s)
01:13:19

[so what that means is we can now handle](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m21s)
01:13:21

[building any kind of model like a you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m32s)
01:13:32

[know whatever kind of neural network](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m35s)
01:13:35

[where we have potentially very high](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m37s)
01:13:37

[cardinality categorical variables as our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m39s)
01:13:39

[inputs we can then just turn them into a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m42s)
01:13:42

[numeric code between zero and the number](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m48s)
01:13:48

[of levels and then we can learn a you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m50s)
01:13:50

[know a linear layer](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m56s)
01:13:56

[from that as if we had one hot encoded](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h13m59s)
01:13:59

[it without ever actually constructing](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m01s)
01:14:01

[the one hot encoded version and without](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m05s)
01:14:05

[ever actually doing that matrix model](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m07s)
01:14:07

[play okay instead we will just store the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m09s)
01:14:09

[index version and simply do the array](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m12s)
01:14:12

[lookup okay and so the gradients that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m15s)
01:14:15

[are flowing back you know basically in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m18s)
01:14:18

[the one hot encoded version everything](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m21s)
01:14:21

[that was a zero has no gradient so the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m22s)
01:14:22

[gradients flowing back is best go to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m25s)
01:14:25

[update the particular row of the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m26s)
01:14:26

[embedding matrix that we used okay and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m29s)
01:14:29

[so that's fundamentally important for](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m32s)
01:14:32

[NLP just like here like you know I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m36s)
01:14:36

[wanted to create a PI torch model that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m40s)
01:14:40

[would implement this this ridiculously](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m44s)
01:14:44

[simple little equation alright and to do](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m48s)
01:14:48

[what without this trick would have meant](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m52s)
01:14:52

[I was feeding in a twenty five thousand](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m55s)
01:14:55

[by adherence to 800,000 element array](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h14m57s)
01:14:57

[which would have been kind of crazy](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m02s)
01:15:02

[right and so this this trick allowed me](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m04s)
01:15:04

[to write you know you know I've just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m06s)
01:15:06

[replaced the word linear with embedding](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m08s)
01:15:08

[replace the thing that feeds the one-hot](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m10s)
01:15:10

[encodings in with something to dispense](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m13s)
01:15:13

[the indexes in and that was it that then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m14s)
01:15:14

[it kept working and so this now trains](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m17s)
01:15:17

[you know in about a minute per epoch](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m20s)
01:15:20

[okay so what we can now do is we can now](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m28s)
01:15:28

[take this idea and apply it not just to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m34s)
01:15:34

[language but to anything right for](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m37s)
01:15:37

[example predicting the sales of items at](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m41s)
01:15:41

[a grocery yes where's that asset just a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m45s)
01:15:45

[quick question so you're not actually](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m53s)
01:15:53

[looking up anything right we are just](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m54s)
01:15:54

[seeing that now that array with the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m56s)
01:15:56

[indices that is the representation so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h15m58s)
01:15:58

[the represent so we are doing a lookup](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m02s)
01:16:02

[right the representation that's being](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m04s)
01:16:04

[stored it for the book but for the bag](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m06s)
01:16:06

[of words is now not one one 100 one but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m08s)
01:16:08

[oh one two](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m12s)
01:16:12

[five right and so then we actually have](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m13s)
01:16:13

[to do our matrix product right but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m17s)
01:16:17

[rather than doing the matrix product we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m21s)
01:16:21

[look up the zero thing and the first](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m22s)
01:16:22

[thing and the second thing and the fifth](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m26s)
01:16:26

[thing so that means we are still](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m29s)
01:16:29

[retaining the one hard encoded matrix no](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m32s)
01:16:32

[we didn't there's no one hot encoded](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m35s)
01:16:35

[matrix used here this here's the one who](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m37s)
01:16:37

[decoded matrix which is not currently](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m39s)
01:16:39

[highlighted we've currently highlighted](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m41s)
01:16:41

[the list of indexes and the list of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m45s)
01:16:45

[coefficients from the weight matrix so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m48s)
01:16:48

[it says okay okay so what we're going to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m52s)
01:16:52

[do now is we're kind of go to just go to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h16m59s)
01:16:59

[go a step further and saying like let's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m01s)
01:17:01

[not use a linear model at all let's use](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m03s)
01:17:03

[a multi-layer neural network right and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m06s)
01:17:06

[let's have the input to that potentially](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m09s)
01:17:09

[be include some categorical variables](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m11s)
01:17:11

[and those categorical variables we will](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m14s)
01:17:14

[just have as numeric indexes and so the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m17s)
01:17:17

[first layer for those won't be a normal](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m23s)
01:17:23

[linear layer](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m25s)
01:17:25

[there'll be an embedding layer which we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m26s)
01:17:26

[know behaves exactly like a linear layer](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m28s)
01:17:28

[mathematically and so then our hope will](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m31s)
01:17:31

[be that we can now use this to create a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m34s)
01:17:34

[neural network for any kind of data all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m37s)
01:17:37

[right and so there was a competition on](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m40s)
01:17:40

[Kaggle a few years ago called](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m46s)
01:17:46

[rossmann which is a German grocery chain](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m49s)
01:17:49

[where they asked to predict the sales of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m52s)
01:17:52

[items in in their stores right and that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h17m56s)
01:17:56

[included the mixture of categorical and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m01s)
01:18:01

[continuous variables and in this paper](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m02s)
01:18:02

[by Gordon Burke and they described their](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m04s)
01:18:04

[third-place winning entry which was much](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m07s)
01:18:07

[simpler than the first placed winning](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m10s)
01:18:10

[entry but nearly as good but much much](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m13s)
01:18:13

[simpler because they took advantage of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m18s)
01:18:18

[this idea of what they call ng](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m20s)
01:18:20

[embeddings](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m22s)
01:18:22

[in the paper they they thought I think](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m24s)
01:18:24

[that they had invented this actually had](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m27s)
01:18:27

[been written before earlier by yoshua](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m29s)
01:18:29

[bengio and his co-authors in another](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m32s)
01:18:32

[cackle competition which was predicting](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m34s)
01:18:34

[taxi destinations although I will say I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m35s)
01:18:35

[feel like war went a lot further in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m38s)
01:18:38

[describing how this can be used in many](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m43s)
01:18:43

[other ways and so will will talk about](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m46s)
01:18:46

[that as well so the so this one is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m49s)
01:18:49

[actually in the is in the deep learning](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h18m58s)
01:18:58

[one repo okay deal one lesson three okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m00s)
01:19:00

[because we talked about some of the deep](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m05s)
01:19:05

[learning specific aspects in the deep](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m07s)
01:19:07

[learning course where else in this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m08s)
01:19:08

[course we're going to be talking mainly](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m10s)
01:19:10

[about the feature engineering and we're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m12s)
01:19:12

[also going to be talking about you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m14s)
01:19:14

[kind of this this embedding idea so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m16s)
01:19:16

[let's start with the data right so the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m24s)
01:19:24

[data was you know store number one on](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m26s)
01:19:26

[the 31st of July 2015 was open they had](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m30s)
01:19:30

[a promotion going on there was a school](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m36s)
01:19:36

[holiday it was not a state holiday and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m39s)
01:19:39

[they sold five thousand two hundred and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m41s)
01:19:41

[sixty three items so that's the key data](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m43s)
01:19:43

[they provided and so the goal is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m50s)
01:19:50

[obviously to predict sales in a test set](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m52s)
01:19:52

[that has the same information without](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m55s)
01:19:55

[sales they also tell you that for each](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h19m57s)
01:19:57

[store it's of some particular type it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m02s)
01:20:02

[sells some particular assortment of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m06s)
01:20:06

[goods its nearest competitor competitor](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m08s)
01:20:08

[is some distance away the competitor](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m11s)
01:20:11

[opened in September 2008 and there's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m14s)
01:20:14

[some more information about promos I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m18s)
01:20:18

[don't know the details of what that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m20s)
01:20:20

[means like in many Carroll competitions](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m21s)
01:20:21

[they let you download external data sets](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m27s)
01:20:27

[if you wish as long as you share them](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m31s)
01:20:31

[with other competitors so people oh they](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m34s)
01:20:34

[also told you what's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m37s)
01:20:37

[date each store is in so people](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m38s)
01:20:38

[downloaded a list of the names of the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m40s)
01:20:40

[different states of Germany they](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m42s)
01:20:42

[downloaded a file for each state in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m44s)
01:20:44

[Germany for each week some kind of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m46s)
01:20:46

[Google trend data I don't know what](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m50s)
01:20:50

[specific Google trend they got but there](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m51s)
01:20:51

[was that for each date they downloaded a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m54s)
01:20:54

[whole bunch of temperature information](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h20m57s)
01:20:57

[[Music]](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m00s)
01:21:00

[that's it and then here's the test set](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m01s)
01:21:01

[okay so I mean one interesting insight](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m04s)
01:21:04

[here is that the it was probably a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m08s)
01:21:08

[mistake in some ways for Russman to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m10s)
01:21:10

[design this competition as being one](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m13s)
01:21:13

[where you could use external data](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m14s)
01:21:14

[because in reality you don't actually](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m15s)
01:21:15

[get to find out next week's weather or](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m18s)
01:21:18

[next week's Google Trends you know but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m21s)
01:21:21

[you know when you're competing in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m24s)
01:21:24

[category you don't care about that you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m25s)
01:21:25

[just want to win so you use whatever you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m27s)
01:21:27

[can get so let's talk first of all about](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m29s)
01:21:29

[data cleaning you know that there wasn't](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m37s)
01:21:37

[really much feature engineering done in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m39s)
01:21:39

[this third place winning entry like by](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m41s)
01:21:41

[particularly by cattle standards where](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m45s)
01:21:45

[normally every last thing counts this is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m47s)
01:21:47

[a great example of how far you can get](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m52s)
01:21:52

[with with a neural net and it certainly](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m53s)
01:21:53

[reminds me of the claims prediction](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m56s)
01:21:56

[competition we talked about yesterday](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h21m59s)
01:21:59

[where the winner did no feature](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m00s)
01:22:00

[engineering and entirely relied on deep](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m03s)
01:22:03

[learning the laughter in the room I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m05s)
01:22:05

[guess is from people who did a little](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m11s)
01:22:11

[bit more than no feature engineering in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m12s)
01:22:12

[that competition so you know I should](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m15s)
01:22:15

[mention by the way like I find that bit](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m19s)
01:22:19

[where like you work hard at a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m22s)
01:22:22

[competition and then it closes and you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m24s)
01:22:24

[didn't win and the winner comes out and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m27s)
01:22:27

[says this is how I won like that's the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m29s)
01:22:29

[bit where you learn the most right like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m32s)
01:22:32

[sometimes that's happened to me and it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m34s)
01:22:34

[been like oh I thought of that I thought](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m37s)
01:22:37

[I tried that and then I go back and I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m40s)
01:22:40

[realize I like had a bug there I didn't](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m43s)
01:22:43

[test properly and I learn like oh okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m46s)
01:22:46

[like I really need to learn to like test](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m48s)
01:22:48

[this thing in this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m51s)
01:22:51

[away sometimes it's like oh I thought of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m51s)
01:22:51

[that but I assumed it wouldn't work I've](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m55s)
01:22:55

[really got to remember to check](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m57s)
01:22:57

[everything before I make any assumptions](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h22m58s)
01:22:58

[and you know sometimes it's just like oh](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m01s)
01:23:01

[I I did not think of that technique Wow](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m03s)
01:23:03

[now I know it's better than everything I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m07s)
01:23:07

[just tried because like otherwise](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m09s)
01:23:09

[somebody says like hey you know here's a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m11s)
01:23:11

[really good technique you're like okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m13s)
01:23:13

[great](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m15s)
01:23:15

[right but when you spent months trying](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m15s)
01:23:15

[to do something and like somebody else](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m17s)
01:23:17

[did it better by using that technique](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m20s)
01:23:20

[that's pretty convincing right and so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m22s)
01:23:22

[like it's kind of hard like I'm standing](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m25s)
01:23:25

[up in front of you saying here's a bunch](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m27s)
01:23:27

[of techniques that I've I've used and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m29s)
01:23:29

[I've won some capital competitions and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m31s)
01:23:31

[I've got some state of the art results](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m33s)
01:23:33

[but it's like that's kind of second-hand](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m34s)
01:23:34

[information by the time it hits you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m36s)
01:23:36

[right so it's really great to yeah try](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m38s)
01:23:38

[things out and and also like it's been](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m42s)
01:23:42

[kind of nice to see particularly I've](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m45s)
01:23:45

[noticed in the deep learning course](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m47s)
01:23:47

[quite a few of my students have you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m48s)
01:23:48

[I've said like this technique works](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m50s)
01:23:50

[really well and they've tried it and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m52s)
01:23:52

[they've got into the top ten of a Keagle](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m54s)
01:23:54

[competition the next day and they're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m55s)
01:23:55

[like okay that that counts is working](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m57s)
01:23:57

[really well so so yeah caryl](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h23m59s)
01:23:59

[competitions are helpful for lots and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m02s)
01:24:02

[lots of reasons but you know one of the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m05s)
01:24:05

[best ways is what happens after it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m07s)
01:24:07

[finishes and so definitely like for the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m08s)
01:24:08

[ones that you that are now finishing up](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m11s)
01:24:11

[make sure you you know watch the forums](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m13s)
01:24:13

[see what people are sharing in terms of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m15s)
01:24:15

[their solutions and you know if you want](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m17s)
01:24:17

[to learn more about them like don't feel](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m21s)
01:24:21

[free to ask the winners like hey could](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m23s)
01:24:23

[you tell me more about this or that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m25s)
01:24:25

[people are normally pretty pretty good](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m27s)
01:24:27

[about explaining and then ideally try](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m28s)
01:24:28

[and replicate it yourself right and that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m32s)
01:24:32

[can turn into a great blog post you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m35s)
01:24:35

[or a great kernel is to be able to say](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m37s)
01:24:37

[okay such-and-such said that they use](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m39s)
01:24:39

[this technique here's a really short](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m41s)
01:24:41

[explanation of what that technique is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m43s)
01:24:43

[and here's a little bit of code showing](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m45s)
01:24:45

[how it's implemented and you know here's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m47s)
01:24:47

[the results showing you you can get the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m49s)
01:24:49

[same result that can be a really](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m50s)
01:24:50

[interesting write-up as well](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m52s)
01:24:52

[okay so you know it's it's always nice](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h24m57s)
01:24:57

[to kind of have your data reflect like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m01s)
01:25:01

[oh no bee is kind of easy to understand](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m06s)
01:25:06

[as possible so in this case the data](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m09s)
01:25:09

[that came from Kegel used various you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m11s)
01:25:11

[know integers for the holidays we can](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m14s)
01:25:14

[just use a boolean if like was it a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m16s)
01:25:16

[holiday or not so like just clean that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m18s)
01:25:18

[up we've got quite a few different](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m21s)
01:25:21

[tables we need to join them all together](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m24s)
01:25:24

[right I have a standard way of joining](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m26s)
01:25:26

[things together with pandas I just used](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m29s)
01:25:29

[the pandas merge function and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m32s)
01:25:32

[specifically I always do a left joint so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m35s)
01:25:35

[who wants to tell me what a left join is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m39s)
01:25:39

[since it's there go ahead you retain all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m42s)
01:25:42

[the rows in the left table and you take](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m46s)
01:25:46

[so you have a key column you match that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m49s)
01:25:49

[with a key column in the right side](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m51s)
01:25:51

[table and you just merge the rules that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m52s)
01:25:52

[are also present in the right side table](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m55s)
01:25:55

[yeah that's a great explanation good job](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m56s)
01:25:56

[I don't have much to add to that the key](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h25m58s)
01:25:58

[reason that I always do a left join is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m00s)
01:26:00

[that after I do the join I always then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m03s)
01:26:03

[check if there were things in the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m07s)
01:26:07

[right-hand side that a noun no right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m09s)
01:26:09

[because if so it means that I some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m12s)
01:26:12

[things yeah I haven't shown it here but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m15s)
01:26:15

[I also check that the number of rows](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m17s)
01:26:17

[hasn't varied before and after if it has](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m19s)
01:26:19

[that means that the right hand side](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m23s)
01:26:23

[table wasn't unique okay so even when](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m24s)
01:26:24

[I'm sure something's true I always also](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m30s)
01:26:30

[assume that I've screwed it up so I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m33s)
01:26:33

[always check so I could go ahead and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m36s)
01:26:36

[merge the state names into the whether I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m39s)
01:26:39

[can also if you look at the Google](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m42s)
01:26:42

[Trends table it's got this week range](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m51s)
01:26:51

[which I need to turn into a date in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m54s)
01:26:54

[order to join it right and so the nice](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m57s)
01:26:57

[thing about doing this in pandas is that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h26m59s)
01:26:59

[pandas gives us access to you know all](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m01s)
01:27:01

[of Python right and so for example](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m04s)
01:27:04

[inside the the series object](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m08s)
01:27:08

[Str attribute that gives you access to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m10s)
01:27:10

[all the string processing functions not](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m13s)
01:27:13

[just like cat gives you access to the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m16s)
01:27:16

[categorical functions DT gives you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m18s)
01:27:18

[access to the date/time functions so I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m20s)
01:27:20

[can now split everything in that column](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m22s)
01:27:22

[and it's really important to try and use](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m24s)
01:27:24

[these pandas functions because they you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m26s)
01:27:26

[know they're going to be vectorized](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m29s)
01:27:29

[accelerated through you know often](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m30s)
01:27:30

[threesome D at least through you know C](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m33s)
01:27:33

[code so that runs nice and quickly and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m35s)
01:27:35

[then you know as per usual let's add](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m41s)
01:27:41

[date metadata to our dates in the end we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m44s)
01:27:44

[are basically denormalizing all these](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m52s)
01:27:52

[tables we're going to put them all into](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m54s)
01:27:54

[one table so in the Google trend table](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m55s)
01:27:55

[there was also though they were mainly](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h27m59s)
01:27:59

[trends by state but there was also](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m02s)
01:28:02

[trends for the whole of Germany so we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m03s)
01:28:03

[kind of put the Germany on you know the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m06s)
01:28:06

[whole of Germany ones into a separate](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m09s)
01:28:09

[data frame so that we can join that so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m10s)
01:28:10

[we're going to have that Google trend](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m12s)
01:28:12

[for this state and Google trend for the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m14s)
01:28:14

[whole of Germany and so now we can go](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m16s)
01:28:16

[ahead and start joining both for the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m20s)
01:28:20

[training set and for the test set and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m23s)
01:28:23

[then which both check that we don't have](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m25s)
01:28:25

[zeros my merge function i set the suffix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m27s)
01:28:27

[if there are two columns are the same I](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m35s)
01:28:35

[set their suffix on the left to be](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m37s)
01:28:37

[nothing at all so it doesn't screw](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m39s)
01:28:39

[around with the name and the right hand](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m40s)
01:28:40

[side to be underscore Y and in this case](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m42s)
01:28:42

[I didn't want any of that you look at](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m45s)
01:28:45

[ones so I just went through and deleted](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m46s)
01:28:46

[them okay and then we're gonna in a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m51s)
01:28:51

[moment we're going to try to create a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h28m55s)
01:28:55

[competition you know the the the main](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m00s)
01:29:00

[competitor for this store has been open](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m02s)
01:29:02

[since some date right and so you can](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m04s)
01:29:04

[just use pandas to date I'm passing in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m08s)
01:29:08

[the year the month and the day right and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m10s)
01:29:10

[so that's going to give us an error](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m15s)
01:29:15

[unless they all have years and months so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m17s)
01:29:17

[so we're going to fill in the missing](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m19s)
01:29:19

[ones with the 1900 and a1 okay](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m21s)
01:29:21

[and then what we really know it we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m25s)
01:29:25

[didn't want to know is like how long is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m26s)
01:29:26

[this store been open for at the time of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m28s)
01:29:28

[this particular record all right so we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m31s)
01:29:31

[can just do a date subtract okay now if](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m33s)
01:29:33

[you think about it sometimes the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m39s)
01:29:39

[competition you know open later than](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m41s)
01:29:41

[this particular row so sometimes it's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m44s)
01:29:44

[going to be negative and it doesn't](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m47s)
01:29:47

[probably make sense to have negative](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m48s)
01:29:48

[spending like it's going to open in X](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m52s)
01:29:52

[days time now having said that I would](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m54s)
01:29:54

[never put in something like this without](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h29m58s)
01:29:58

[first of all running a model with it in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m02s)
01:30:02

[and without it in right because like our](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m05s)
01:30:05

[assumptions about about the data very](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m08s)
01:30:08

[often turned out not to be true now in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m12s)
01:30:12

[this case I didn't invent any of these](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m14s)
01:30:14

[pre-processing steps I wrote all the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m17s)
01:30:17

[code but it's all based on the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m20s)
01:30:20

[third-place winners github repo right so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m23s)
01:30:23

[knowing what it takes to get third place](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m27s)
01:30:27

[in the cable competition I'm pretty sure](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m29s)
01:30:29

[they would have checked every one of](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m32s)
01:30:32

[these pre-processing steps and made sure](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m33s)
01:30:33

[it actually improved their their](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m35s)
01:30:35

[validation set score okay so what we're](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m37s)
01:30:37

[going to be doing is creating a neural](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m45s)
01:30:45

[network where some of the inputs to it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m50s)
01:30:50

[are continuous and some of them are](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m52s)
01:30:52

[categorical and so what that means in](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m56s)
01:30:56

[the in the neural net that you know we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h30m59s)
01:30:59

[have we're basically going to have you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m02s)
01:31:02

[know this kind of initial weight matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m11s)
01:31:11

[right and we're going to have this this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m13s)
01:31:13

[input feature vector right and so some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m16s)
01:31:16

[of the inputs are just going to be plain](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m20s)
01:31:20

[continuous numbers like you know what's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m22s)
01:31:22

[the maximum temperature here or what's](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m24s)
01:31:24

[the number of kilometers to the nearest](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m26s)
01:31:26

[store and some of them are going to be](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m28s)
01:31:28

[one HUD encoded effectively right but](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m35s)
01:31:35

[we're not actually going to store it as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m41s)
01:31:41

[one hot encoded we're actually going to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m43s)
01:31:43

[store it as the index right and so the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m45s)
01:31:45

[neural net model is going to need to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m49s)
01:31:49

[know which of these columns should you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m51s)
01:31:51

[should you basically create an embedding](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m55s)
01:31:55

[for which ones should you treat you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m57s)
01:31:57

[as if they were kind of one hot encoded](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h31m59s)
01:31:59

[and which ones should you just you feed](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m01s)
01:32:01

[directly into the linear layer right and](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m03s)
01:32:03

[so we're going to tell the model when we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m07s)
01:32:07

[get there which is which but we actually](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m10s)
01:32:10

[need to think ahead of time about like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m12s)
01:32:12

[which ones do we want to treat as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m14s)
01:32:14

[categorical and which ones are](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m16s)
01:32:16

[continuous in particular things that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m18s)
01:32:18

[were going to treat it as categorical we](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m21s)
01:32:21

[don't want to create more categories](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m23s)
01:32:23

[than we need right and so let me show](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m26s)
01:32:26

[you what I mean the the the third-place](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m28s)
01:32:28

[getters in this competition decided that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m33s)
01:32:33

[the number of months that the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m35s)
01:32:35

[competition was open was something that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m36s)
01:32:36

[they were going to use as a categorical](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m37s)
01:32:37

[variable all right and so in order to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m39s)
01:32:39

[avoid having more categories than they](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m42s)
01:32:42

[needed they truncated it at 24 months](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m43s)
01:32:43

[they said anything more than 24 months](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m47s)
01:32:47

[old truncate to 24 so here are the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m49s)
01:32:49

[unique values of competition months open](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m52s)
01:32:52

[and it's all the numbers from naught to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m54s)
01:32:54

[24 right so what that means is that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h32m56s)
01:32:56

[there's going to be you know an](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m01s)
01:33:01

[embedding matrix that's going to have](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m03s)
01:33:03

[basically an embedding vector for things](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m05s)
01:33:05

[that aren't open yet for things that are](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m07s)
01:33:07

[open a month for things that are open](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m10s)
01:33:10

[two months and so forth now they](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m11s)
01:33:11

[absolutely could have done that as a](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m15s)
01:33:15

[continuous variable right they could](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m18s)
01:33:18

[have just had a number here which is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m20s)
01:33:20

[just a single number of how many months](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m22s)
01:33:22

[has it been open and they could have](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m23s)
01:33:23

[treated it as continuous and fed it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m25s)
01:33:25

[straight into the initial weight matrix](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m26s)
01:33:26

[what I found though and obviously what](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m30s)
01:33:30

[these competitors found is where](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m34s)
01:33:34

[possible it's best to treat things as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m37s)
01:33:37

[categorical variables right and the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m40s)
01:33:40

[reason for that is that like when you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m45s)
01:33:45

[feed some](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m48s)
01:33:48

[things through an embedding matrix you](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m48s)
01:33:48

[basically mean it means every level can](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m51s)
01:33:51

[be treated like totally differently](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m53s)
01:33:53

[right and so for example in this case](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m55s)
01:33:55

[whether something's been open for zero](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h33m58s)
01:33:58

[months or one months is right really](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m00s)
01:34:00

[different right and so if you fed that](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m03s)
01:34:03

[in as a continuous variable it would be](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m06s)
01:34:06

[kind of difficult for the neural net to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m08s)
01:34:08

[try and find a functional form that kind](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m10s)
01:34:10

[of has that that big difference as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m13s)
01:34:13

[possible because neural Nets can do](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m14s)
01:34:14

[anything right but you're not making it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m16s)
01:34:16

[easy for it where else if you used an](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m18s)
01:34:18

[embedding treated it as categorical then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m20s)
01:34:20

[it will have a totally different vector](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m22s)
01:34:22

[for zero versus one right so it seems](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m24s)
01:34:24

[like particularly as long as you've got](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m26s)
01:34:26

[enough data that the treating columns as](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m28s)
01:34:28

[categorical variables where possible is](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m33s)
01:34:33

[a better idea](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m35s)
01:34:35

[and so I say when I say we're possible](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m36s)
01:34:36

[that kind of basically means like where](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m38s)
01:34:38

[the cardinalities not too high you know](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m43s)
01:34:43

[so if this was like you know the sales](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m46s)
01:34:46

[ID number that was like uniquely](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m52s)
01:34:52

[different on every row you can't treat](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m54s)
01:34:54

[that as a categorical variable right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m57s)
01:34:57

[because you know it would be a huge](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h34m59s)
01:34:59

[embedding matrix and everything only](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m01s)
01:35:01

[appears once or ditto for like](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m03s)
01:35:03

[kilometers away from the nearest store](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m05s)
01:35:05

[to two decimal places you wouldn't make](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m07s)
01:35:07

[a categorical variable all right so](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m10s)
01:35:10

[that's kind of that's kind of the rule](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m14s)
01:35:14

[of thumb that they both used in this](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m16s)
01:35:16

[competition in fact if we scroll down to](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m18s)
01:35:18

[their choices here is how they did it](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m21s)
01:35:21

[right they're continuous variables with](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m26s)
01:35:26

[things that were genuinely continuous](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m29s)
01:35:29

[like number of kilometers away to the](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m31s)
01:35:31

[competitor the temperature stuff right](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m33s)
01:35:33

[the number you know the specific number](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m36s)
01:35:36

[in the Google trend right where else](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m39s)
01:35:39

[everything else basically they treated](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m43s)
01:35:43

[as categorical okay so that's it for](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m44s)
01:35:44

[today so yeah next time we'll we'll](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m51s)
01:35:51

[finish this off we'll see we'll see how](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m56s)
01:35:56

[to turn this into a neural network](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h35m58s)
01:35:58

[and yeah kind of wrap things up so see](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h36m01s)
01:36:01

[then](https://www.youtube.com/watch?v=XJ_waZlJU8g#t=01h36m05s)
01:36:05

