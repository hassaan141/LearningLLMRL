# tactiq.io free youtube transcript
# I wish I never did this project..
# https://www.youtube.com/watch/aV4j5pXLP-I

00:00:00.719 The deed is done. I can finally return
00:00:04.640 to this channel cuz I have done what I
00:00:07.279 said I was going to do. Not that. We
00:00:10.800 will get to that. One thing at a time. I
00:00:13.360 trained my own AI model. Yay. How long
00:00:16.560 has it been? I'm making my own AI. I'm
00:00:19.039 making an orb. My own planter. I was
00:00:21.439 hoping to share it by the end of this
00:00:22.720 video, but it takes a long time. So, I
00:00:25.279 feel like those bears coming out of
00:00:26.800 hibernation.
00:00:28.880 What happened? But the deed is done and
00:00:32.238 I ran the benchmarks official AI
00:00:35.680 benchmark and my model outperforms
00:00:39.120 DeepSeek 2.5. Way bigger model than
00:00:42.000 mine. Facebook's flagship model llama 4
00:00:45.760 Maverick destroyed. And most importantly
00:00:50.239 of all, my model outperforms Chad GPTs
00:00:55.840 four.
00:00:58.079 in like November or something. That was
00:01:00.480 This sounds like impressive, but it's
00:01:03.120 way less impressive once we get into it.
00:01:05.119 And we will get into it. It also sounds
00:01:07.280 way less impressive considering the fact
00:01:09.600 that I almost burned down my house twice
00:01:12.479 for this project.
00:01:15.040 It also sounds way LESS IMPRESSIVE. I
00:01:17.360 LOST MY vanity for now. I have not
00:01:21.280 created my own AI. I have merely taken
00:01:24.080 an AI model and trained it. It's like
00:01:27.439 stealing a child on the street instead
00:01:29.920 of birthing one myself. It's way more
00:01:32.640 effective that way. Plus, it would cost
00:01:34.799 millions and millions of dollars in
00:01:36.320 infrastructure which I do not have yet.
00:01:39.200 Am I talking about birthing or but it's
00:01:42.720 important for you to understand just how
00:01:44.320 naive I was going into this because I
00:01:46.640 knew nothing about machine learning
00:01:49.360 training AI and coding that I mentioned
00:01:52.240 my model is a coding model. I can make a
00:01:54.960 coding model. Sure, Felix, great idea.
00:01:58.159 But I also know I wasn't that crazy
00:02:00.240 going into this and I'll explain why.
00:02:02.560 But mainly the fact that I wanted to do
00:02:04.320 this was because I wanted to learn. The
00:02:06.479 reason I'm here with this video and the
00:02:08.639 series of events has just been me
00:02:11.440 approaching this philosophy of just yes
00:02:14.080 this might be difficult but I will learn
00:02:15.840 from it step by step you know that takes
00:02:18.879 you places and that's why I'm so excited
00:02:21.200 to announce today's sponsor which is
00:02:23.360 boot.dev boot.dev is a website that
00:02:25.680 teaches you how to code but for real. I
00:02:28.480 did their Linux course and it's
00:02:30.560 fantastic. When you actually understand
00:02:32.879 how something works, it changes things
00:02:35.280 for real. It's none of this Dualingo
00:02:38.080 bing fake learning, okay? It's fun, it's
00:02:40.959 engaging, and it works. I'm super
00:02:43.200 excited to do their other courses as
00:02:45.120 well. Create your own AI agent in Python
00:02:47.680 course. I'm going to say something that
00:02:49.599 makes me sound like such a boomer, but I
00:02:52.400 am at this point. So, to heck with it.
00:02:54.800 Instead of focusing on gaming too much
00:02:56.560 lately, I just been focusing on leveling
00:02:58.959 up myself. But it's true. It's such an
00:03:02.720 amazing feeling and I want you guys to
00:03:04.879 experience it as well and I think
00:03:06.239 boot.dev is an amazing venture to do so.
00:03:09.040 So check it out in the description and I
00:03:11.040 will remind you later as well. Okay. Now
00:03:14.400 funny enough to train my model AI model
00:03:17.280 it ironically it works very similar to
00:03:19.200 how you would train on yourself on
00:03:20.800 boot.dev. There's an instruction of a
00:03:23.200 problem. You get a framework on how to
00:03:25.360 initiate or what to use and then there's
00:03:27.760 a validated answer at the end of it.
00:03:30.000 Basically, I gathered around 100,000
00:03:31.680 samples like that. And then you feed
00:03:33.440 that to the model, which slightly nudges
00:03:35.519 its parameters. Like it slightly
00:03:37.760 probably nudges your brain. And bada
00:03:39.920 bing, bada boom, you have trained your
00:03:41.519 model. It's kind of like this. You're
00:03:43.599 AI. Look at this.
00:03:48.959 Are you learning?
00:03:53.040 Are you getting this?
00:03:56.239 You will look at these. You will look at
00:03:58.400 100,000 more. Play pay attention.
00:04:07.599 >> This might take a while. The model that
00:04:09.439 I used was Gwen 32B, which is already
00:04:12.000 amazing at coding, but I needed it to be
00:04:14.159 amazing at coding in this format. The
00:04:16.720 whole reason I decided to do this and
00:04:18.320 where I landed, cuz I discovered
00:04:20.160 something. There are many ways to
00:04:22.639 benchmark and test your model. I
00:04:24.639 discovered there's one called Ader
00:04:26.080 Polyglad. If you remember last video, I
00:04:28.800 used the agent ader to code my own web
00:04:30.960 UI. This is a respectable benchmark that
00:04:33.440 tests coding in six different languages.
00:04:36.400 That's six more languages than I know.
00:04:39.680 But what was interesting about this is
00:04:41.360 that state-of-the-art models like CHP
00:04:43.919 perform like garbage on this benchmark.
00:04:46.240 18.2%.
00:04:48.080 Uh what my model that I was planning to
00:04:51.120 train on performs 8%. trash, but it
00:04:55.840 performs 16% if you use a different
00:04:58.720 format called whole format instead of
00:05:00.639 diff format. Basically, there's two
00:05:02.560 different formats, but one of them is
00:05:04.720 important. How do I explain this? It's
00:05:06.800 basically like this. You draw a picture.
00:05:09.039 Okay, imagine you draw a picture and you
00:05:10.960 want to add a cloud, but instead of just
00:05:13.120 adding the [ __ ] cloud, you redraw the
00:05:15.360 entire picture with the cloud. It makes
00:05:17.280 no [ __ ] sense. But basically a lot of
00:05:19.759 these models they struggle to understand
00:05:21.360 the format of just editing in the code
00:05:24.240 instead of just writing the whole thing.
00:05:26.240 It's just stupid. It wastes compute and
00:05:28.240 it wastes time and I never used it as
00:05:30.080 well. So I thought hey if I can just fix
00:05:32.320 the format I will make my model 16%. And
00:05:36.400 I will almost beat Chad GPT. The goal
00:05:39.280 beat chat GPT easy because what I had on
00:05:43.280 my side at my disposal, my arsenal was
00:05:46.960 Chinese AI research. You'd think China
00:05:50.560 would be on the more censorship side of
00:05:52.560 things. At least that's what I thought.
00:05:54.479 How wrong I was. It's completely the
00:05:56.560 opposite. Deepseek China AI basically
00:05:59.680 just released their model for anyone to
00:06:02.000 run and a whole document with their
00:06:04.160 entire training process in great detail.
00:06:07.199 It's amazing. There's so much
00:06:09.199 information from these research
00:06:10.960 documents. It combined with the open
00:06:12.560 source community. There's so much to try
00:06:14.800 and it just makes you really want to try
00:06:16.560 it yourself. At least that's how I saw
00:06:18.560 it. Even though a lot of it was super
00:06:20.400 advanced and I didn't understand
00:06:21.600 anything, eventually I did. I think
00:06:25.520 it's also hilarious reading these
00:06:27.280 documents. Chinese AI researchers are
00:06:29.120 unironically comedians cuz they write
00:06:31.039 the most unhinged [ __ ] They say [ __ ]
00:06:33.039 like, &quot;Oh, we trained our model on 248
00:06:36.639 GPUs.&quot; And you're like, &quot;What? That's
00:06:38.800 like $60 million.&quot; And and you keep
00:06:41.120 reading and they're like, &quot;We emphasize
00:06:42.880 this is an economical APPROACH.&quot; I'M
00:06:44.720 LIKE, &quot;ECONOMICAL? WHAT'S THE
00:06:46.400 NON-ECONOMICAL VERSION?&quot; But I think
00:06:48.880 that kind of puts things in perspective
00:06:50.479 and why a lot of companies in the west,
00:06:52.479 they don't want to share information. So
00:06:54.639 with Chinese AI research on my side and
00:06:56.880 a boot dev course, I was ready to do
00:06:59.759 this thing.
00:07:01.680 Now, what do you need to train AI? Data.
00:07:05.280 Now, how do you get data without
00:07:06.720 sacrificing your soul in the process?
00:07:08.800 Well, there is options, believe it or
00:07:10.639 not. You can mine the stack, which is
00:07:12.400 this 60 TBTE data set that you're
00:07:14.560 allowed to train on. Good thing I kept
00:07:16.160 my hard drives around. You can use
00:07:18.000 publicly available data sets. You can
00:07:20.160 also mine git, which is a little more of
00:07:21.759 a gray zone cuz you have to check for
00:07:23.599 licenses, which I'm sure everyone is
00:07:26.000 doing, right? These big tech companies,
00:07:28.560 they're they're being super ethical and
00:07:30.160 great about it. I'm sure that's why
00:07:31.759 they're not sharing any information. And
00:07:34.400 you can also synthesize your data.
00:07:36.960 Glorious synthetic data. M so tastes so
00:07:40.639 good. I tried every single method there
00:07:42.880 is. It's been a mess. This is scraping
00:07:46.240 git or enriching my data. This is
00:07:48.479 scraping for more data. This is running
00:07:52.800 testing on the data. And this is
00:07:55.520 augmenting the data. And this is my
00:07:58.000 eight LLMs. This is the level we've
00:08:00.560 reached. This project was kind of like I
00:08:03.120 was like in the middle of a freeway and
00:08:05.280 there's a bunch of cars direct that I
00:08:06.960 had to direct constantly because [ __ ]
00:08:09.360 had to move for this to finish.
00:08:11.360 Everything took so much time and my GPUs
00:08:14.000 had to constantly be cooking and I had
00:08:16.639 to do all this makeup cosmetic surgery
00:08:18.879 to the data cuz all these developers
00:08:20.879 writing poor lazy first of all why you
00:08:24.479 even publish some of that lazy
00:08:26.639 instructions. Don't make a commit if
00:08:28.879 you're just going to add a comment. But
00:08:30.960 finally, I had my data, but I still knew
00:08:33.839 I needed more. And I also wanted to try
00:08:36.240 out synthetic generation of data, which
00:08:39.599 is basically you typically take the
00:08:41.760 strongest model that you have and you
00:08:43.519 ask it, hey, look at this. Make more in
00:08:47.760 this format. And my god, it was a
00:08:50.160 beautiful thing. You get the perfect
00:08:52.480 data exactly the way you want it. It's
00:08:55.440 amazing. But the problem is, and maybe
00:08:58.240 you already know this, AI is wrong all
00:09:01.839 the [ __ ] time. Okay? It's basically
00:09:04.080 like this. I tell AI
00:09:12.720 my drawing skills have really I'm sure
00:09:15.680 glad I learned how to draw.
00:09:19.200 I tell AI, &quot;Make a burger by showing him
00:09:22.399 a burger.&quot; And then AI makes what looks
00:09:26.160 like a burger, but I open the lid and he
00:09:29.600 put razor blades in there. So my harness
00:09:33.200 is a burger eater
00:09:37.600 to check that if the real burgers are
00:09:39.440 made instead of fake burgers. I think I
00:09:42.000 explained that pretty well. You lied to
00:09:44.000 me. My synthetic approach, I know that
00:09:47.519 most people don't care. I used oss
00:09:49.360 instruct from magic coder and evol
00:09:51.519 instruct which is an amazing method.
00:09:53.440 It's basically like that cloning dancing
00:09:56.560 guy technique. You get feed a code
00:09:58.399 snippet and then you say hey make it
00:10:00.720 into this format and also make it do
00:10:02.959 another one but make it more advanced. I
00:10:04.959 don't want to get into this technical it
00:10:07.040 doesn't matter. This video will take
00:10:08.000 forever but the problem I had was I was
00:10:10.240 not getting enough of it and I don't
00:10:11.920 trust okay I don't trust like that. Okay
00:10:14.240 so I validated it. I kept thinking the
00:10:16.720 problem was my test hardness, so I
00:10:18.959 needed to fix that. WHAT AN IDIOT. THAT
00:10:22.720 JUST MADE it so I passed more garbage.
00:10:25.519 So when the time came for me to finally
00:10:27.680 train my model after months, months, I
00:10:31.680 was so excited. I ran the benchmark and
00:10:34.800 I had made an AI model that finally
00:10:39.600 that was worse. I had made it worse.
00:10:43.600 I probably should have quit then, but I
00:10:46.560 am way too stubborn for that. I just
00:10:48.320 can't. I I I don't have it in me. I
00:10:50.160 can't do it. This is when you realize AI
00:10:52.880 is kind of like magic, right? But it
00:10:54.720 also isn't. Garbage data in, garbage
00:10:56.880 data out. There was a lot of issues with
00:10:58.880 my data. When I had fixed my harness, I
00:11:00.800 had just let more garbage data pass
00:11:02.720 through. There was also all these other
00:11:04.560 issues like empty white spaces and
00:11:06.399 classic coding issues that I just wasn't
00:11:08.399 aware about. So that's why I had made it
00:11:11.120 worse. But I gave it another attempt.
00:11:13.760 And this time, no more mistakes. No more
00:11:17.120 dillydadling. Lock aim
00:11:20.320 again. The model is worse.
00:11:25.120 It was my harness yet again.
00:11:28.399 I don't know why I got so stuck on this
00:11:30.560 [ __ ] thing. Well, I didn't even need
00:11:32.320 synthetic data. I just wanted it to
00:11:34.079 work. I just wanted to work so bad.
00:11:36.240 Finally, I had fixed the [ __ ] thing
00:11:38.880 and the benchmark came in 16%. Sometimes
00:11:42.959 15, sometimes 14, but 16 was the
00:11:46.640 highest. The model is just not going to
00:11:48.399 solve the same problem every time. It it
00:11:50.240 just doesn't work like that. There is a
00:11:52.160 level of randomness to it to the
00:11:53.920 benchmark performance. But 16 was the
00:11:56.560 ceiling. And that makes sense because
00:11:58.000 that was the ceiling in the official
00:12:00.240 whole format or whatever. And I had
00:12:02.160 fixed it so it's in the diff format. But
00:12:04.079 I had not made a [ __ ] difference. I
00:12:06.639 had not made the model smarter. And and
00:12:08.560 remember I need to beat 18%. To say that
00:12:11.279 I beat Chad GPT otherwise this means
00:12:13.760 nothing. So my plan of attack was to add
00:12:16.800 reasoning to my data. Adding reasoning
00:12:19.120 to your data is basically making it
00:12:21.200 write out some thinking before it solves
00:12:24.000 the problem. Instead of doing 2 plus 2
00:12:26.000 in your head, you go, &quot;Oh, okay. So let
00:12:28.160 me break this down. So I'll have two
00:12:30.079 apples and then if I add two more apples
00:12:32.800 and then I count them all together then
00:12:35.200 I will have four. This is really
00:12:37.519 effective for complicated issues to
00:12:39.760 break down the problem into parts and it
00:12:42.399 really can improve the performance of
00:12:44.000 the AI. But when it's simple questions
00:12:46.639 and it still does it it can be very very
00:12:48.639 irritating as well. You probably seen
00:12:50.880 this actually if you use a stronger AI
00:12:52.880 model a lot of times you ask it
00:12:54.399 questions it goes oh absolutely well
00:12:56.720 let's break this down into parts. First,
00:12:58.720 we're gonna you're like, &quot;That was a
00:13:00.240 simple yes or no question. What do you
00:13:01.600 mean?&quot; But it's a really effective way
00:13:03.360 to make your model solve problems more
00:13:06.079 accurately. And a lot of these smaller
00:13:08.560 open source models that I train on
00:13:10.639 struggle with this because they just
00:13:12.160 haven't been trained on it enough. So,
00:13:13.920 that was my plan of attack to make my
00:13:16.240 model smarter. And I found a study that
00:13:19.120 showed that 10% in performance. I'm
00:13:21.920 like, that's way more than I need, baby.
00:13:24.399 Let's just clone this git repo and get
00:13:26.560 going. The only problem was, of course,
00:13:29.519 that the ungodly level of computation
00:13:31.920 that was needed for this. And that's
00:13:33.680 when things were starting to smell
00:13:36.079 funny. I realized my room had this weird
00:13:39.600 aura to it all of a sudden. Hey, I swear
00:13:41.920 it didn't used to smell like that. So, I
00:13:44.399 decide to reboot my computer and
00:13:47.519 lightning strikes all across it. Smoke
00:13:50.560 starts pouring out. My whole life
00:13:52.480 flashed before my eyes. I turn off the
00:13:54.320 computer, but the damage was done. One
00:13:56.639 of my GPUs had died. Rest in peace. I
00:14:00.880 tested each one one by one and it seemed
00:14:03.760 like everything else was okay. It was
00:14:05.680 just this one problem. And looking at my
00:14:07.680 purchase history, that one GPU came from
00:14:10.480 a different factory. You have to
00:14:12.560 understand what a hack job this setup
00:14:14.639 that I have is. Okay, it's bifurcated.
00:14:18.160 It's undervolted to death. This GPU is
00:14:20.639 run on 450 watt. But I run it on 1751
00:14:23.839 just so my house wouldn't [ __ ] crash
00:14:25.839 every time. And then these are hacked
00:14:28.399 Chinese 4090 GPUs. This whole thing is
00:14:31.519 held together by prayers. Literally in
00:14:34.320 Japan they sell these prayer infused IT
00:14:37.199 badges. Where is it? It's in front of my
00:14:38.959 computer. Official Japanese priests.
00:14:44.000 I probably have now blessed my computer
00:14:46.880 and I was ready to give it another shot
00:14:49.680 only for the smell to appear again.
00:14:52.480 After sniffing my GPUs like a maniac, I
00:14:55.519 concluded my GPUs was not the problem
00:14:57.839 this time. And eventually I found it. I
00:15:00.880 don't think it's supposed to look like
00:15:02.160 that. Again, I was using cable that was
00:15:04.880 graded for 1,500 watt. I was running
00:15:07.360 over 2,000. Change cable. We were good
00:15:10.560 to go. My computer kept crashing still.
00:15:16.480 >> Oh, it's still thought it crashed. It
00:15:20.639 has crashed. Oh, [ __ ] What a pile of
00:15:25.040 You'd think training would be just a
00:15:26.959 straightforward thing, but it's really
00:15:29.199 not. It's taking too long to train. I
00:15:31.760 need more compute. Okay, what am I going
00:15:33.440 to do? It's not my fault. I know what
00:15:35.600 you're thinking, Felix. Are you building
00:15:37.680 another computer? No, I am just
00:15:40.480 extending the one I have. Of course. Of
00:15:44.240 course. I'm an epic minimalist.
00:15:47.600 I had to steal the circuit from my
00:15:50.079 bathroom and I drilled a hole.
00:15:55.040 It's super heavy on your computer and
00:15:57.279 every time it crashes, I have to [ __ ]
00:15:59.920 defibrillate it back. Bring it back from
00:16:02.320 a coma. It's not pleasant. It's and with
00:16:05.759 everything that had happened in the past
00:16:07.839 extremely stressful and I really really
00:16:10.399 really started doubting what the [ __ ]
00:16:13.279 I'm doing here for these 2%. I started
00:16:16.480 calling upon DeepSeek API because it's
00:16:19.040 practically for free and eventually I
00:16:22.079 had 15,000 samples which is way less
00:16:24.959 than I had aimed for but these were the
00:16:28.320 top of the top the creme the cra samples
00:16:31.120 that I have with the most beautifully
00:16:33.360 crafted stepbystep reasoning the world
00:16:36.320 has ever seen. I did my supervised fine
00:16:38.720 tuning three epochs and I ran the
00:16:42.160 benchmark and it scored 17.
00:16:46.959 Are you [ __ ] kidding me? But as I
00:16:49.600 mentioned, the performance is kind of
00:16:51.519 random. So I kept running the benchmark.
00:16:54.000 I had eventually given up, but I had
00:16:56.000 done one more just for the [ __ ] of it.
00:16:58.240 And I noticed, holy [ __ ] this one is
00:17:00.800 having like a god run. It's at 40%. What
00:17:03.519 is happening? It drops to 30. I'm like,
00:17:06.640 &quot;Hold, please hold.&quot; It drops to 25. It
00:17:11.679 drops to 20 and it finally finishes
00:17:15.919 all the exercises in the benchmark. It
00:17:18.400 is done at 19.6%.
00:17:21.599 I have beat chat.
00:17:26.079 It felt so goddamn good. STOP. STOP.
00:17:30.559 DON'T LISTEN to this guy. The benchmark
00:17:33.600 is invalid. I did not check for
00:17:35.840 contamination before the benchmark.
00:17:38.160 Basically, if you grab data all across
00:17:40.160 the internet, there's a high chance that
00:17:41.760 you're going to grab data that might
00:17:43.600 already exist in a benchmark somewhere.
00:17:45.600 So, you have to check for contamination.
00:17:47.600 I didn't check for contamination. I
00:17:49.679 didn't want to check for contamination,
00:17:51.679 but my stupid conscience was like, I
00:17:54.320 should probably do it. I was backing up,
00:17:56.720 going through my data for the
00:17:57.840 gazillionth time, and I realized there
00:18:01.200 was some contamination. It's not a huge
00:18:03.679 deal, but it's like if I just am honest,
00:18:07.039 whatever. To me, it's not good enough.
00:18:08.960 And I want to clear out my data and I'm
00:18:11.039 going to retrain again, benchmark again,
00:18:15.120 and I'm hoping and I think it will still
00:18:17.440 give me the same result cuz it's such
00:18:19.600 small contamination. I'm kind of worried
00:18:22.240 cuz I'm running out of time.
00:18:25.120 Have I done [ __ ] all this entire time?
00:18:27.520 Have I achieved nothing this entire
00:18:29.520 time? and the whole thing was a hoc
00:18:31.600 pogus. That's what I thought. So this
00:18:33.919 time I went all out. I trained on my
00:18:36.640 entire data set. Previously I trained on
00:18:39.200 a small subset of what I thought was my
00:18:41.360 best data because it takes forever to
00:18:43.840 train. It takes forever. It takes days,
00:18:46.400 weeks, and since I reached the score of
00:18:48.640 19.6, I was like, uh, I'M DONE. BUT NOT
00:18:54.160 THEN I made another discovery. I was
00:18:56.960 training on the wrong model. A major
00:18:59.440 update. I'm watching I'm watching my
00:19:01.760 video. This guy I'm giving feedback to
00:19:05.280 my editor and I'm like, &quot;Hold on, hold
00:19:07.760 on. What is that?&quot;
00:19:10.400 That is not the coder version.
00:19:14.160 That's the regular version. Have I been
00:19:17.679 Have I been training on the wrong
00:19:19.039 version this entire time?
00:19:23.520 Oh,
00:19:26.559 so maybe this has all been a blessing in
00:19:28.799 disguise because I feel like with these
00:19:30.480 two in my things in mind, I I should I
00:19:32.960 should beat Chachi. I should, but we
00:19:35.840 will know in a couple days.
00:19:37.200 >> Did I beat Chachi?
00:19:39.840 Well, I train on the coding model and
00:19:42.400 the first score
00:19:44.480 4.4%.
00:19:48.400 I don't know what the [ __ ] happened. I
00:19:49.760 can probably think of five things, but I
00:19:51.440 don't care to figure it all out. It's
00:19:52.799 going to take forever. I just retrained
00:19:54.960 again. And the model score 25%, baby.
00:20:01.360 I am not just beat Chip. I beat Chachi
00:20:04.640 twice. Their August shitty version as
00:20:07.600 well. I was so relieved. I was like,
00:20:09.840 &quot;Thank God.&quot; But I made another
00:20:13.039 discovery. It's not over. A third of the
00:20:16.160 benchmark was not even running. C++ and
00:20:19.360 JavaScript just wasn't being tested
00:20:21.039 properly. So, I fixed the benchmark. I
00:20:23.840 run it again and the final score
00:20:27.600 36%. Baby,
00:20:31.679 this means I also beat Google Schmoogles
00:20:34.960 thing as well. And I think I beat I beat
00:20:37.600 4.1 or something. I don't know. Chat,
00:20:40.080 it's a massacre out here. You're being
00:20:41.919 destroyed. It's embarrassing. Open AI
00:20:44.240 stock just demolished. Just quit
00:20:46.799 already. This is what pops the AI bubble
00:20:49.440 this.
00:20:51.440 But I was like, there are still issues.
00:20:54.559 I'm going to do some post training.
00:20:56.559 1,500 samples. Splinky blinky five
00:21:00.480 epochs. And I ran the benchmark again.
00:21:04.320 Pure decontaminated, let it be known.
00:21:06.720 Purer than the fountain of youth. 39.1%
00:21:10.960 baby.
00:21:13.200 Another destroy. I think this one I beat
00:21:15.280 Google Smoogle. I always stupid
00:21:17.039 benchmark. Yeah, Gemini. Gemini Pro. You
00:21:21.360 guys pay for that? I did not think this
00:21:23.520 would even ever come close. But here's
00:21:26.000 the embarrassing part about all of this.
00:21:28.480 I train on Gwen 2.5, but Gwen 3 is out
00:21:32.799 and it scores 40%.
00:21:35.600 So, unless I beat 40%, this means
00:21:38.240 nothing. And I'm I don't I'm out of
00:21:40.799 time. I don't have [ __ ] time. I need
00:21:43.039 to send this video to my editor. Yes,
00:21:44.799 there was one more thing. A model being
00:21:46.640 good at one benchmark is stupid as [ __ ]
00:21:49.039 Okay, I need to test this model on other
00:21:52.000 benchmarks as well. I want to test it on
00:21:53.600 Sweetbench, all these other coding
00:21:55.200 benchmarks. Unless it improved in that,
00:21:57.200 it really it I don't even know. I am
00:21:59.440 just out of time. Okay, I don't have
00:22:00.880 time to do it, but I will. And if this
00:22:03.120 model ever gets to a point where I feel
00:22:04.720 like it's good enough, I would love to
00:22:06.240 share it. But I think if anything, I
00:22:08.000 might just move on to a different
00:22:09.120 project in in the background because it
00:22:11.120 takes a long time and uh I'm kind of
00:22:13.600 tired. That being said, you've seen me
00:22:15.840 fail a lot in this video. I have become
00:22:18.240 so accustomed to failure, you have no
00:22:21.360 idea. I've almost given up on this
00:22:23.200 project so many times. There are so many
00:22:24.799 times where I'm just like, I don't know
00:22:26.000 what I'm doing. This is the stupidest
00:22:27.679 thing ever. I have graveyards full of
00:22:30.559 just garbage, debunkle, schmunkle,
00:22:33.679 deformed data that I have generated
00:22:36.240 thinking this is the best.
00:22:39.360 I have gone through the whole alphabet
00:22:41.360 of failures. I was just so way in over
00:22:43.919 my head on this project. But I think the
00:22:46.000 number one thing I've learned, how do I
00:22:48.000 explain this? When you install Linux,
00:22:50.000 here's what happens. Linux toural the
00:22:52.320 creator becomes your godfather
00:22:54.159 inevitably. And I was watching one of a
00:22:56.320 random video of him talking and he was
00:22:58.480 talking about how he's doing this
00:23:00.080 project and he was failing. But that's
00:23:02.320 okay because that's how you learn. Uh
00:23:04.720 some people think that failure is a bad
00:23:06.960 thing and I happen to be one of those
00:23:08.880 people who actually enjoy doing
00:23:13.760 things I'm not good at
00:23:16.720 because it's how you learn.
00:23:19.280 >> And I'm watching that lad and I'm like
00:23:21.520 he's speaking to me right now.
00:23:24.159 Oh my god. But I really feel like that's
00:23:26.720 the main thing I've learned from all
00:23:28.000 this because there's so much to learn
00:23:30.159 from failure. Learn from it and
00:23:32.159 iriterate and keep working. I think if
00:23:34.159 you have expectations of how things
00:23:35.760 should go for yourself, you're just
00:23:37.039 going to get disappointed and you're
00:23:38.880 going to want to give up. So expect to
00:23:41.039 fail, embrace failing. That's the
00:23:44.080 message I want to send out to you kids.
00:23:46.480 Last thing, this is a coding model and I
00:23:49.039 think a lot of people are are looking at
00:23:50.880 coding models like are they going to
00:23:52.240 replace and I saw Linus say this as well
00:23:54.400 and he was basically saying coding
00:23:56.159 models if anything it will just bring in
00:23:57.840 more people interested in learning how
00:23:59.360 to code again. He's speaking to me right
00:24:01.520 now like I would never have learned
00:24:03.919 wanting to learn how to code if it
00:24:05.679 wasn't for AI coming into the picture.
00:24:07.520 So on the final note, learn something
00:24:10.880 new. Check out boot.dev. I highly
00:24:13.200 recommend it. It's a great course. Pick
00:24:15.279 out whatever you want. Challenge
00:24:17.039 yourself into something difficult that
00:24:18.880 may be above what you think you're
00:24:20.559 capable of. That's it. Now scram. I'm
00:24:24.480 just kidding, bro.
00:24:27.440 This month we're traveling a lot. And
00:24:29.520 what always happened whenever we travel?
00:24:32.000 The inevitable connecting to public
00:24:34.080 Wi-Fi. Free Wi-Fi is a trap. Get the
00:24:37.679 reference. If you connect to someone
00:24:39.440 else's Wi-Fi, you might as well just
00:24:41.039 give up your credit card and banking
00:24:42.559 information and all your information
00:24:43.919 they ever had. You should always use a
00:24:47.120 VPN. NordVPN. Say it with me. Nord SMGos
00:24:53.279 board connect always. I'm even connected
00:24:56.240 right now. I made a little module for
00:24:59.120 me. Look,
00:25:01.360 cuz whatever I do online, if I want to
00:25:03.440 download, it's my goddamn business. It's
00:25:06.400 my
00:25:08.880 It's about a goddamn right. So, thank
00:25:11.120 you NordVPN for making it possible to
00:25:13.600 free yourself, protect yourself online.
00:25:16.240 If you go to nordvpn.com/pie, you get a
00:25:18.480 huge deal on a 2-year plan, plus a bonus
00:25:21.279 extra 4 months for free. New Year's
00:25:23.520 resolution, take your online privacy
00:25:25.840 seriously. This is the best deal for
00:25:28.000 NordVPN you're going to find. So, take
00:25:29.919 advantage. Thank you, Nord, for
00:25:31.679 sponsoring this video. That's
00:25:32.559 nordvpn.com/piepie.
