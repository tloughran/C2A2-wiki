# Levin, Friston and Chis-Ciure on Wandering Thoughts — speaker-attributed transcript

- **Episode:** "Agency & Intelligence Across Scales | Levin, Friston & Chis-Ciure", Wandering Thoughts channel, published 2026-11-18
- **Source:** https://www.youtube.com/watch?v=EY0nrb7AXJs (YouTube auto-transcript, pasted by Tom 2026-11-22)
- **Header corrected 2026-11-23:** the show is "Wandering Thoughts". The auto-transcript renders it "Pondering Thoughts" in the host's opening line, which is left as transcribed, and this file's name still carries the wrong word.
- **Speakers:** Kyriakos (host), Michael Levin, Karl Friston, Robert Chis-Ciure (University of Sussex)
- **Length:** about 1 h 25 min; 18 chapters, headings as given in the scraped transcript
- **Companion analysis:** `claude/levin-friston-chis-ciure-pondering-thoughts-analysis.md`

## How this file was made, and what to distrust

- The words are the auto-transcript's, verbatim, with timestamps stripped and turns joined. A script did the assembly; source and output both count 13,434 words, so nothing was dropped or added.
- **Speaker attribution is inferred** from content (who is addressed, who answers, topic and idiom). The transcript carries no speaker labels, and the video was not watched, so no turn was checked against the audio. Only the page's title, channel and date were read (2026-11-23).
- **Names are confirmed.** The host introduces the third guest only as "Dr. Robert from the University of Sussex"; the video title names him Chis-Ciure, and Tom confirmed that spelling and "Kyriakos" for the host (ASR: "Kiryakas"/"Kyakas") on 2026-11-23.
- **Least certain attributions** (short exchanges where two voices overlap): 1:33 (three-way split of one line), 49:23 (the trailing "Yeah." may be Levin), 58:27 (the "thank you so much" is marked uncertain), 1:25:00 (the first sentence is given to Friston and may be Chis-Ciure), 1:25:20 (the goodbyes).
- **ASR corrections:** a fixed list of 65 substitution patterns repaired names and technical terms (for example Levvin to Levin, Carl to Karl, "markoff"/"mark of blanket" to Markov blanket, "helmholds hodge" to Helmholtz–Hodge, "reormalization" to renormalization, "launch van equation" to Langevin equation, "Mark SS" to Mark Solms, "Newan Simon" to Newell and Simon, "dressing patterns" to ingressing patterns). The full list is the `FIXES` table in the generating script. Everything else is left as transcribed, including disfluencies and uncorrected errors such as "car" for Karl, "xenino organ", "tr principle" and "variance of free energy" (probably "variational free energy").
- Chapter headings fall where the landing page puts them, which is often mid-turn; a turn that continues past a heading is marked "(cont.)".

---
## Chapter 1: Intro

**Kyriakos (host)** [0:00]: Hey guys, welcome to another episode of Pondering Thoughts. Today I'm joined by Professor Michael Levin, Professor Karl Friston, and Dr. Robert from the University of Sussex. So, thank you so much for joining me, guys. It's a pleasure to be able to talk to you and to learn from you. I want to encourage all three of you to take the conversation into any interesting tangents that might come. Um, but I thought it might be a good start to try to understand how all of your guys's work intersects. A kind of big picture question I had in mind is to connect the previous two episodes um, we've done with Professor Levin and Professor Friston.

And so we talked about active inference, Professor Friston on our first episode. And I was wondering how we can understand the goal-directed behavior of cells that we talked about preserving through a framework of active inference and Robert um both Professor Levin and Professor Friston have talked highly of you and so I'd be also interested in your ideas around this question. So, I'll leave it open to you, any any of the three of you. I'm happy to start whoever wants to take the initiative.

**Karl Friston** [1:26]: I think Robert should take the initiative in linking me with Mike.


## Chapter 2: Connecting active inference, biology and Platonic space

**Karl Friston** (cont.) [1:31]: [laughter]

**Robert Chis-Ciure** [1:33]: Am I now? Uh, it's my turn now, Karl.

**Karl Friston** [1:33]: It is your turn now.

**Robert Chis-Ciure** [1:33]: In the in the TMV. So, I've been um a chair for Karl's theoretical neurobiology group for two years.

So I I do have some some insights from from Karl's work and I've been working with Mike for uh about a year and a half now I think and we are uh now actively developing the the story behind the platonic spaces and if I were to to propose a lynch pin knowing very well that Karl has spoken before on the platonic nature of thing I would say that in the context of the free energy principle especially in the somewhat car calls it if I recall deflationary definition of things the ways in which the scales relate to each other and Karl I'm sure will will uh explicate much more about the the specific dynamics that occurs something that exists at a certain scale is fast relative to the scale above and slow relative to the scale below.

And I am curious in the context of uh of Mike's uh of Mike's research, how would Karl in for example xenobots, which if I understood his points correctly in several papers, um the xenobots do not have a genome selected for what they are. They have a frog's genome and the genome is something that's so slow that it never moves. It stops moving as you as you mentioned at some point, Karl. And I [clears throat] I'm curious where would the Xenobots ability or capacity, the forms I suppose that Mike might would call them, emerge from if they are not in the genome.

**Karl Friston** [3:48]: So I will certainly speak to that. Um, but you've introduced the notion of platonic. Uh, so I'm going to pass the bat to Mike just to sort of frame frame [laughter] um, which is great because I'd have to talk about this, but it might be just useful for for the listeners just to understand the deep questions on the table um, from the point of point of view of some platonic forms and the like.

**Michael Levin** [4:13]: Yeah. Um I think that uh before [clears throat] before we make any commitments to platonic space or


## Chapter 3: Xenobots and the origins of novel biological capabilities

**Michael Levin** (cont.) [4:20]: anything else we can just uh uh think about a a a generic question which is that where do novel systems properties come from. So when when whenever we uh make or find anything that has certain uh specific properties we typically have three ways that nowadays that we try to explain those properties. either it was engineered specifically to do certain things or maybe it was evolved slash selected to do those things or maybe it was trained to do those things and some combination one or more of those things are thought to to be the explanation for what you see.

So we've been interested in creating model systems that stress test that assumption and uh one of those systems and we have numerous systems like it one of them is a Xenobot. So, just for anybody who doesn't know, we take wild type cells out of, let's say, a frog embryo. We do the same thing with humans uh in in a in a saltwater medium, which is basically not different from uh the medium that they're normally in. They self assemble into this little creature that is able to move around on its own and do all kinds of interesting things. It has a novel um transcriptome with hundreds of differentially expressed genes.

It has novel behaviors that the normal embryos don't do. has uh it it has it responds to sound it does all sorts of interesting things kinematic self-replication and so on.

So with the question on the table is can we develop a predictive science of where the goal of novel systems the goals and properties and capabilities and just very specifically where do they come from because I don't think it's enough to say that well life is complex and somehow at the same time you were selecting for frogs and humans you also got xenobots and anthrobots that's okay after the fact after somebody produces them and shows you what they do but we have to do better because we make all sorts of novel beings novel structures humans um cyborgs, AIs, whatever.

I would like to understand the space from which their properties are drawn and the conditions in which certain properties appear and not others. So, so that's the question, right? And and and I do not like the standard emergent answer where you just sort of shrug your shoulders and say, "Well, surprise, it was emergent." So, that's that. Um I would like to think that uh upstream of that is some sort of structured space that we can study from which these properties are are pulled. And I'll I'll stop here and then later I can I can talk a little bit about um what we've done with this with this information.

**Karl Friston** [6:43]: Brilliant. Um right. So to just um address Robert's question and just to foreground his uh appeal to scale I think scale invariance is going to be very important here in our discussion.


## Chapter 4: The Free Energy Principle and self-organisation

**Karl Friston** (cont.) [6:58]: Um but to ask the question, what would it mean to understand the the different kinds of self-organization that we can see and how do we explain them in terms of how they emerged? Um, I would read that from the point of view of a physicist trying to think about self-organization as what are the boundary conditions that explain what things are allowable and what things are not.

And if you can identify the right kind of boundary conditions, um, do they plausibly point to self-organization that has the attributes of the kind that Mike was just, uh, just rehearsing? the kind of attributes that you know you would bring a a teleology like selection or training or learning uh to explain post hoc once you've observed these kinds of behaviors um and um from a deflationary to celebrate Robert's uh introduction of that word perspective um I would say yes um and then the quest becomes what are these boundary conditions um and the approach that the free energy principle would take would be to note that you have to be able to specify what it would mean for something to exist over a non-trivial amount of time.

In other words, first of all, you have to define explicitly what it is to be a structure. And if I was talking in the 1950s, this would be a dissipative structure in the in the sense of Prigogine, um what it means to be a structure and how a structure can be separated from the environment in which it is immersed. It could be salt water. It could be a whole host of other um xenobots or cells. Um and then um ask yourself well in so doing am I uh what implicit boundary constraints have I invoked or appealed to?

And the first obvious one is that this self, this thing, this structure has some characteristic states that are defined simply in virtue of the fact that there are lots of states it can't be in. Uh in other words, there are lots of more way there are lots more ways of being dead or dissipated than there are of being alive. Um and that basically um leads to the argument that if something persists in a set of characteristic states that has you know non-trivial dynamics um mathematically has a non-equilibrium steady state. Um what does what what boundary conditions must it conform to? Um and this is not going to please anybody apart from me.

But the um the the boundary condition in question is simply inherits from one thing we know is conserved which is a probability of some thing of anything in this instance uh the structure or where in state space this structure is. Um and that simple conservation noting that the if anything is conserved in the universe its probability mass [sighs] just knowing that means that you can now bring something called the Helmholtz–Hodge decomposition to the table.

So for me the boundary condition the constraints that are implicit in something existing in some characteristic states just as the Helmholtz–Hodge decomposition and that's I think quite insightful because that tells you quite a lot um if you impose this as a boundary condition you can talk about immediately the kinds of behaviors that this structure should exhibit and the non-trivial uh behavior behaviors are due to a decomposition in terms of um a gradient flow and a non-dissipative sometimes called solenoidal flow which tells you immediately that it'll any structure that exists under these boundary conditions must first of all or will look as if it is gathering itself up self-organizing in such a way to resist the dissipation due to random and fluctuations in the universe.

Furthermore, and importantly, because of this non-dissipative solenoidal, sometimes called conservative uh dynamics, it'll look as if it's moving around in state space. Um, and by moving around, I mean quite trivially. It'll look as if it has some oscillations. And if we now put Robert's scale invariance into play um then it will also look as if it has a kind of oscillation a kind of orbit a kind of dynamics that is evident at multiple scales. So I'm talking here about very fast electrochemical oscillations for example or even right down to the quantum level where it measurable um right through um biorhythms right through to life cycles.

So that means just finding the identifying the right kind of constraint immediately tells you that anything that exists in this sense subject to these boundary conditions must confine itself to some characteristic states technically a pullback attractor that has a very particular form which disallows lots of states that it could not be in. And this particular form requires it to have a motility. It requires it to move around and it also requires it to revisit the states it was once in. That's another way of um if you like intuiting why it has to have this circular solenoidal non-dissipative or conservative uh conservative aspect.

So the free principle would say that it is sufficient uh if not terribly enlightening uh to identify um structures of um um that exist um with non with the pullback attractors uh that um are one way of writing down the fact that this system this structure has a non-equilibrium steady state. And there are all sorts of interesting corollaries here. First of all, you're breaking detail balance, which means you've got a time irreversibility, which means that things that exist also cannot be reversed in time. So, they actually go through life cycles.

Um unlike sort of your 20th century physics at equilibrium, if I gave you something at equilibrium, say a cup of coffee, you couldn't tell me um when the cup of coffee once it had cooled down and was at thermal equilibrium, you couldn't tell me whether it was recently made, made 20 years ago or made uh made tomorrow. Whereas if I've got if I stir the coffee and introduce this solenoidal flow, this non-dissipated flow, then you can tell me, oh yes, you've recently stirred this cup of coffee or if it's still, oh, it was stirred a long time ago.

So there's some some really fundamental aspects of the nature of things that conform to um the constraints that just in existing they have to have both this non-dissipative dynamics. And I could witter on about what happens when you when you increase the scale which I hope we will talk about when we move from a single cell or a single structure to structures of structures multicellular organization uh because as the scale increases that has a enormous implication for the um the distinction well for the relative contributions of these dissipative dynamics and these non-dissipative dynamics.

**Robert Chis-Ciure** [14:52]: I I have a an interesting small question on this car. I always wondered whether in this definition of existence that


## Chapter 5: Markov blankets and the scale of the universe

**Robert Chis-Ciure** (cont.) [15:00]: that you propose via boundary conditions. So blankets are if you want to to in blankets if you want to introduce that and um possessing an attracting set. Does the universe exist under this definition?

**Karl Friston** [15:16]: Well, anything that you can name um as a natural kind must have a Markov blanket. So, yes, the universe with

**Robert Chis-Ciure** [15:23]: Does the universe have a Markov blanket as a whole? I mean, uh

**Karl Friston** [15:23]: well, yes, yes, absolutely. Uh but I'm going to elude the trap you're setting for me by by reminding you we are talking about something that is scale invariant. So, it's the universe all the way up and all the way down. There's no edge of the universe. You can't get a higher scale. There's always a higher scale.

So this is a very this is sort of more of a biological physics or a natural physics, a natural science that is um scaled specific uh but also is carefully attending to the scale above and the scale below for the things that are doing the measurement um through their Markov blanket. you know, in in our in our world, of course, it's things of a certain size, but we can look at very small things, not too small. Uh we can't get down to small particles because of quantum physics. Um and not too big uh because we don't have the right kind of telescopes. So, we're we're always sort of telling stories about the universe at a particular scale in relation to the scale above and the scale below.

**Robert Chis-Ciure** [16:33]: I was just a bit cheeky with this.

**Karl Friston** [16:35]: Yes, you were. [laughter]

**Kyriakos (host)** [16:35]: Um before I ask anything else, Professor Levin, do you have anything to add to uh what was said?

**Michael Levin** [16:46]: Um yeah. Yeah, I wanted to um [clears throat] follow up on something that Karl was saying before before this this last thing. So, so here here's so so I'm interested in in what you guys think


## Chapter 6: Biological constraints, evolution and free lunches

**Michael Levin** (cont.) [16:57]: about this because I think I think it relates to this issue of boundary conditions and so on. So uh one of the things that I'm really interested in is an alternative. So so we think about what's allowable and a lot of in biology people talk about constraints right the power the importance of constraints and things like that. So I'm interested in the flip side of this which are enablements or free lunches. In other words, it's not just things you can't do. It's things that it's it's patterns that you've managed to um acquire that cannot be traced back to specific selections, specific training or specific design. But these patterns are um they're useful for navigating some problem space.

They happen to have utility of some sort. And of course, evolution and engineers can can take advantage of them. So uh so I'm interested in quantifying um quantifying these kinds of things. And one way to do that, for example, in our computational model is we ask, okay, if it's doing certain things that I think we never asked it to do, if I did ask it to do those things in conventional ways, so I would write an algorithm or I would do an evolutionary algorithm or something, what would that cost me? You know, what would be the conventional price? And of course, you never know what the what the the absolute lowest is, but we can we can make a, you know, we can make a guess.

And so what would be the price of these things that the system is is doing without without me having spent any of those any of those costs. So let me just talk about how that plays out in in Xenobots because I think it becomes interesting. So so so here's what we have on Xenobots. We have a a transcriptional analysis of what genes they are expressing differently than these cells would under normal conditions. In the case of anthrobots, it's about 9,000 genes. So like half the genome is different. In the case of xenobots, it's a few hundred genes.

And we also have a number of um uh properties such as uh what kind of uh uh what kind of salt conditions, what kind of pH, what kind of things that pressure they can tolerate, things like that. So you have some description of of this. And once you have that description, you can do something interesting which is a kind of reverse ecology. You can ask the following hypothetical question. If these things had evolved under standard conditions, if we if this was a a natural being that we found somewhere, what would the selection forces have had to be to result in that set of gene expressions?

So, so sometimes you can work backwards and you can say, okay, based on this pathway, this is what the pH, the temperature, the oxygen level, the the nutrient level of the war in in effect, what you're what you're trying to reconstruct is the Xenobot home world. you're you're you're looking at the properties now and you're doing what evolution was supposed to do for us, which is to give a tight specificity between the properties that a creature has now and the set of environmental conditions that got got got you there to begin with. So, so I did that. I made um a pipeline that attempts to sort of roll backwards and uh and guess what the selection pressures would have been.

So, it paints a picture of a world. It isn't this world. It's not terribly different, but but it's different. You know, there are significant differences. And now you can ask yourself what is the what is the status of this thing. Um on the one hand it isn't this world. So it's not it's not that but it's also not uh just some crazy random story you could tell because it actually fits very specific properties that are measurable. So what's the so so I was thinking about it first as a kind of counterfactual history and you sort of start fooling around with um you know alternate timelines and weird things like that. But then I thought maybe maybe there's something different going on.

Maybe this is not their past. Maybe this is their future. In other words, as they're being created, of all the different kinds of things they could have done, for some reason, they have some uh I don't know if it's inductive bias or or or some priors or I don't know what it what it is, but there's some reason why they are preparing to live in a particular world whose properties we can now specify at least to some extent. And lots more work to be done about can we can we infer some of them from knowing others. This is still very early days. I'm making no real claims here.

But I think but I think it's interesting to think about what is the specific environment towards which they are uh prepping so to speak. Um why that one why not some other one? Of course as engineers we would like to know can we give them experiences that would prep them for a different world? Maybe one in which they had to I don't know collect uranium from seawater or something you know like useful things that you could sort of push them towards.

But I'm I'm just interested what what what Karl and Robert have to say about this when when you see when you can com sort of infer the kind of pressures uh or the kind of environment that looks fit for a particular being except they've never been in that world. How do we how do we think about these things?

**Karl Friston** [21:29]: Well, while Robert is thinking, um I'll just pick up on on on two um


## Chapter 7: Scale invariance and adaptation to possible futures

**Karl Friston** (cont.) [21:36]: key questions there and key themes. You mentioned free lunch. I'd like to just again for everybody's benefit just to um you know unpack what you know what what sort of commitments a free lunch perspective brings to the table. But um just in relation to this spe really intriguing notion that you know there um this thing has um demonstrates an adaptive fitness for its future. Yeah, I I I think that's a beautiful idea. Um, and it's exactly consistent with the application of the scale invariance that Robert introduced to the um the evolution of or the um contextualization of dynamics at one scale by the scale above.

So the one key thing when you um look at the nature of the scale invariance you can look at this from the point of view of um there being some dynamics that has these boundary conditions that produces some non-dissipative behavior in the context of dissipative effects random fluctuations that has this biotic aspect to it but it's always contextualized by something that is at a higher scale more coarse grained and crucially coarse grained in time. So it changes really really slowly.

So for example it could be the genotype uh contextualizing providing what Hermann Haken would say would be control parameters parameters of the dynamics of the flow at the lower level and of course that flow will evolve during the lifetime of of the say phenotype that is contextualized by the scale above. The the nice thing about that notion is from the point of view of the scale below say the phenotype um the uh there's no um the the past and the future are the same and this in physics would be called um an adiabatic approximation.

So because the the higher scale, the description of this universe or at this scale at the higher scale is changing so slowly because of the um the um this if you like coarse graining or time dilation uh that is implicit in technically the renormalization group. It means that the that there is no difference between the past and the future. Another common sensical way of saying this is that um I'm acting now in this context. But notice the context is the same as the past and in the future at any one point in time that I am acting in this particular context.

And if you now read the higher scale as basically providing the boundary conditions or the constraints on the dynamics at the lower scale, I now think you have a perfectly a mathematically um um licensed argument of exactly the kind that the higher scale is basically providing uh a specification of all plausible or allowable spaces. is for or attracting sets for the lower scale to explore and what it will explore will be different for every you every [clears throat] individual but fact it's contextualized by something that has no sense of time at the lower scale I think I repeat licenses exactly this notion that um you are equipped to say I am a xenobot and I am equipped with a certain uh um epig genomic constraints now my genome does not change during my lifetime.

But it does specify the constraints on all the plausible outcomes at my particular scale. And in that sense, it does exactly specify um the um the the the how well I can adapt to my futures. uh because my futures are prespecified by the allowable uh by the um by the allowable states the attracting set that I could potentially could potentially explore. So I I I think that that notion of counterfactual histories and counterfactual futures is exactly what you'd expect uh or what you could articulate in terms of the adiabatic approximation inherent in this scale invariant scale invariant uh future.

One more final point before I I I pass back to to Robert. um the the you know you you you've we're talking about sort of adaptation um and something that we haven't really mentioned thus far in relation to one particular application of the free energy principle namely active inference um is the fact that um it's that you can always interpret these fast dynamics at any particular scale uh in rel as how the the structure in question stands in relation to the environ enironment it it finds itself.

So basically the free energy principle and its implementation or interpretation in terms of active inference and self-evidencing and modeling and you know measuring uh and aligning itself with the with the environment just is a statement of how good this particular structure speaks to or is aligned or can synchronize with this environment. And of course the environment um is parameterized or contextualized by the scale above you and then you get into dark sort of niche construction the like.

So again you've got exactly this notion that of you know there are a set of possible environments and I am as a structure at any one scale um um um now um able to align myself with all of these i.e. adapt to all of these environments and all the possible environments in the past and in the future from my point of view are contextualized by the by the scale above. So that would be an argument of a purely mathematical sort that rest upon the renormalization group that would be the mathematical expression of this scale invariance. the same kind of physics being um invoked to describe um the dynamics at each and every scale with just a rescaling of time and space and co-spreading and the like.


## Chapter 8: Measuring biological intelligence and search efficiency

**Robert Chis-Ciure** [28:04]: taking a cue from from Karl's u notion of of scale invariance and and the fact that in in the tr principle the form of the law is itself in very basically the larger form of of the equations in a paper in 25 with Mike we tried to quantify a notion via a notion that is scale-free what we called at the time uh search efficiency in problem spaces it was this idea a of trying to formalize how more much more efficient certain biological structures not necessarily uh anchored to a single scale. So it it was meant to be scale free from construction are compared to a baseline. In this sense it was an initial attempt to quantify what a free lunch would be.

Although in in that attempt in that paper we did not specifically consider where the notion or where the source of efficiency was where it was in the phylogenetic selection where it was in some some training that occur via some experimental condition whether it it was in something that was engineered if if the the the biological scale happened to be like that.

So we did not ask okay where does the efficiency count but what we found was and in analyzing planaria regenerative hydro regenerative planaria exposed to barium and amoebas being much much smaller we found and as a baseline we use somewhat a problematic I think now in retrospect notion of a random walk we found two to three orders of magnitude more efficient search compared to a suitably defined random walk for a problem space of a plan of of an amoeba. But for a planaria even under conservative estimations we found 21 or something like that orders of magnitude more efficient even when we are conservative.

And the notion the formal notion the formal measure of search efficiency there was the log t of the of the cost of a blind search divided by the cost of an aential or agent ic of a what we would call probably a biological search.

So in this sense we have this intuition that there is something there that is surprising the endless forms most beautiful of biology and we want to know why that is the case and we need a a way to quantify that and now we are working with Mike on a on a crazy idea of trying to see whether we can find ways in which the patterns the what Michael likes to call them ingressing patterns are themselves in rich of embodiment that we would find and we would we would call them uh we would call them um probably in what we trying what we try to do a xenino organ.

So as an as a sort of um pattern looking for a body whether that could be interpreted from the perspective of the body as an externalized organ. And the the difficulty here would be obviously that a pattern is not something that just subists independently of instantiation of particular instantiation.

However, if it can be shown that the pattern subsists across changes of let's say the target body that it's supposed to be an organ for and other conditions in in the environment I think a notion of free lunch as something that is a novelty that no selection selected for no natural selection was exist for no design and no uh learning induced use task or training exists for I think that's a that's a good way to to approach the issue.

**Michael Levin** [32:23]: Yeah. I mean um so so Karl asked for a for a definition of a of a of a or clarification for free lunch and so the


## Chapter 9: Free lunches, mathematical patterns and agency

**Michael Levin** (cont.) [32:30]: you know the the most uh sort of deflationary minimal um definition that I can give is simply the following. when when you have a set of measured competencies and uh you try to you have a ledger where you write down the effort that it took to produce it and so you total up everything that you can understand be that was input by uh engineering um sorry if um it's it's back whatever this is it's back yeah thank you um so so so you you total up how much effort was put in by direct design by any kind of a selection force and by any kind of experience with the problem space or or learning and whatever you have left over needs to be explained, right?

So, so pretty much my only claim is that the standard way we have of um estimating how much effort it's going to take for something interesting to appear, we uh we don't we we don't have all the ways, right? There's there's something missing uh that we normally don't count. So, so the first thing you can just say is that well, it's just a name for whatever is left over that we don't, you know, we we haven't we don't account for in our normal uh in in our normal accounting. This idea is is old. So, for example, you know, Stu Kauffman talked about order for free and um W.

Grey Walter with his tortoises and so on said that well look at this extremely minimal circuit that does these these like behavior like things. So, so, so we we know that you can get complexity, you can get unpredictability, you can get interesting things from simple systems, but my bigger claim is is something else. Not not only do our standard ways of paying for effort, you know, the things the things that if you were to ask an engineering company to produce for you, these are the things they would charge you for. We're going to have to do this much coding. We're going to have to do this much evolutionary algorithms.

We're going to have to train this thing. you know that you would get build for these things in a very practical way. Um whatever is left over uh what what what I see now through our experiments is that sometimes what you get are patterns that are basically just order for free or they're the kinds of static things you get from from mathematics and so on. But sometimes what you get are things that are actually encoding problem-solving uh strategies or policies. And the way you know that is through experiment. In other words, you take those patterns and you give them a body and you ask a creative questions such as behavior scientists would. What is this thing good for?

If you have the digits of some mathematical constant or something, give them a body and see what is the behavioral policy that's embedded in these things. And so it turns out that uh sometimes what you get are things that are somewhere on the cybernetic spectrum. They are not static patterns. They are in some way an encoded policy for doing interesting things. uh that is at at some level of of sophistication. You know, I'm not saying these are human level kinds of things, but but but they have they have interesting behaviors that are recognizable to any behavior scientist. So, so then the free lunch becomes something slightly different.

It's not just something that was left over in your accounting, it not only was left over in your accounting, but it is also uh something like the kinds of competencies that we see in cognitive systems, at least in in simple ones. And then you have to ask yourself, well, the space of these kinds of things and what's in that space becomes some sort of a um uh uh some sort of a taxonomy of kinds of minds, right? The the the you know what what what are the competencies that you can that you can pull down in some way that's different than those three ways.

And that starts to tell you about the the behavior of novel beings, be they know biobots or AIs or or whatever it is, right? that that's how I see this as a space of as a space of kinds of mind. Some extremely minimal, some barely do anything, some are random walks, but some are really clever and interesting and uh and that's and that's what I see. And I guess I guess the final thing I would just comment on um what Robert was talking about is is the difference between patterns patterns and agents. So I I in my head this is a very scale-free thing kind of like what Karl was talking about in the following way.

If from the perspective of um creatures that live in the core of the earth, so imagine they come up to the surface, they're incredibly dense. They have gamma rays for vision. They, you know, very long live. They don't see us as agents. What they see is a thin sort of gas that surrounds the the planet. They might notice that within this gas there's some kind of little eddies that sort of hold themselves together for for about a hundred years or so. And maybe they maybe one of them will even make a hypothesis that you know they they look kind of agentic. These little eddies they these these patterns I mean literally patterns in an excitable medium.

They they almost look like they're doing something. And the other ones will make fun of them and say that well that's crazy. We are actual beings. You know patterns in a medium can't be agents. They're you know they're just patterns. So I I do think it's there's a scale invariance here. I think it's somewhat whether you're a whether you're data or a machine is in the eye of the beholder. I don't think there's a principal difference. And I think this um thoughts as thinkers uh spectrum I is interesting for these. But I'm curious what um Karl and Robert have to say.

**Karl Friston** [37:37]: Yeah, I love that's the third time I've heard you talk about these dense beings surfacing. That's beautiful. I I think I actually saw you present that with with some lovely graphics as well which uh uh which I would recommend to anybody who


## Chapter 10: Embodiment, active inference and causal structures

**Karl Friston** (cont.) [37:52]: wants to uh have a visual impression of these. But that's a beautiful example of this scale invariance isn't it? You know the the the you know at my scale of the dense being for example um you know that's where I would conceive of as agency but all the constituent fast fluctuations you know the the cells in my brain that or the synapses that come and go minuteby minute they are not agents from my perspective. So we're talking now about, you know, um a scale that allows for um certainly a multicellular kind of organization or at least a deep hierarchal structure to the um internal to the structures that that that we're talking about.

And a couple of points re sort of um um hit a sweet spot from the from the the you know the the mathematical perspective. First of all, the notion that um and I'm not sure that I'm reading this right, but um you can tell me if I'm not.

Um but the notion that the embodiment is basically um uh an installation of some pattern into the structure itself through uh immersing a structure in a particular world or in a particular context. fits exactly with um the uh one of the the the corollaries of active inference and the free energy principle that in many senses can be uh read um as a 21st century reinvention of the good regulator theorem from cybernetics namely that to be in a world uh to which I am open i.e to be a regulator that I can act upon that world just to is to be a good model of that environment.

And what that means mathematically also uh from the point of view of of active inference is that the cause effect structure in this context which is not yet physically realized but can be written down mathematically in terms of a probabilistic cause effect structure or some um you know in terms of say um um um random dynamical attractors um becomes installed and perhaps ingressed into the uh the structure that is actually realized when immersed in this cause effect structure or in this universe or this context that has this cause effect structure.

So I I would see you a really um close alignment with that notion of um ingression if I read it properly of some potentially realizable cause effect structure which is a pattern into an embodied physically realized pattern simply because uh you have now um read the self-organization of this structure uh in terms of the good regulator theorem or in terms of the free energy principle.

So that would be another aspect of storytelling about your this looks like ingression in the same way that I would tell the story this looks as if this um your this little structure has in implicit in its anatomy um the cause effect structure which it's trying to model and trying to predict you know right from things like um the very fact that you and I can see things at a distance means that the sort of co the probabilistic cause effect structure um has to be installed into a certain kind of anatomy and I would imagine that things that see things at a distance have have neurons simply because neurons have long range connections they cover distances literally in the metric space whereas things that can't see things at a distance don't need neurons you can do it all with um you know with local message passing and organels certainly at a single uh so that would be one instance of um if I'm using the word correctly ingressing or installing a pattern which is read as a probabilistic cause effect structure into the physical thing the self that has uh enshrouded by a Markov blanket but but in um what it is enshrouding is basically a good regulator which is just the right structure for this particular world or set of worlds that are contextualized by, you know, by by by the scale by the scale above.

I don't know if that makes sense and whether I'm using ingression in the in the right kind of way, but uh that's how I would use it if forced to do so.

**Michael Levin** [42:35]: I I I think that's that's super interesting. Um and yeah, I mean with the with with only the addition that um I think typically what we get is a whole ecosystem of patterns. I think in most systems that we care about, you end up with lots of different patterns at different at different scales. But I'm I'm really interested in this um in this causal uh causal effect structure thing because that's one of the debates that uh that rage in this around this concept is a lot of people don't think of for example mathematical structures as as causal. So, so people think they're descriptive or they're made up by humans or some kind of uh you know um social construct or something.

And so, so they this this idea of uh how to how to make sense of um specific patterns in that space as being causal as being regulators uh which I think is exactly like I call them controllers but it's like that's exactly what it is. um this this notion that that in fact uh they they are the explanation for why many things happen in biology and and I assume in in physics but c in computer science for sure. So so I think I think that's a really interesting point about the the causality aspect of this. I think I think I need to sort of think about it more and maybe we can even develop some of this in a in a model.

**Karl Friston** [43:53]: C can I just ask and I when you were defining the sort of you know the importance of the free lunchy part the stuff that can't be explained the stuff that you're measuring in terms of the uh the you know how efficiently can this thing do this kind of thing


## Chapter 11: Could everything be a free lunch?

**Karl Friston** (cont.) [44:10]: which incidentally um would be in my world class as finding the path of least action and then you'd score that in terms of the path integral of the um the you know say the variance of free energy would be an obvious thing here to measure the that efficiency to say how well suited uh adaptable is this structure to this environment. And that would be that would be again isomorphic with the you know the whole premise that uh structure learning or the uh the evolution of different structures has to um has to have this kind of efficiency but it only in relation to the counterfactual world in which it's in which it found it finds itself.

But just coming back to this sort of um the free lunchiness um you were talking about before and I think it's a really interesting perspective that you can try and quantify um the um the adaptiveness or the um the the the if you like the cognitive faculties of any given structure by saying how much would it cost me to pay this production company to build one of these things either to you know engineer them using differential evolution or artificial life or to actually sort of sit down and you know and design it.

Um and um the metrics by which I would um judge the cost and the quality you seem to be implying were the kind of metrics that inherit from um biological sciences and you know things like sort of um um competences of a cognitive or a behavioral sort or possibly even a sort of thermodynamic sort. Um my question is um is is do you want to have everything being a free lunch? And most of the free lunch has acquired some semantics from biologists or theoretical you evolutionary theorists and the like. But in reality it's all free lunch.

And pe some people some disciplines have learned to call these things um your your utility or um um your efficiency or your you or or you know wherever you look there'll be somebody who who likes to to say oh there must be some objective function here that is being optimized. Some people say this is the definition of a normative account that you're identifying an optimization and therefore if something sort of if there's a crosscutting optimiz objective function that people keep spotting again and again and again like value or utility then it acquires its semantics and it becomes an explanation.

Whereas from the point of view of the physicist there's no optimization. there is a cause effect structure and things that are uh embedded in that and and it looks as if they're optimizing something and it's easy to uh but um you know that's that wouldn't be if you like the that's not causal the cause effect structure is just what it is it's just a probabilistic specification of the dynamics that you know of the physics of this of this world at this particular scale um so I'm asking you would it be okay if I wanted to reiterate your argument to say that everything is a free lunch.

A proportion of free lunch has now been hijacked and inappropriately ascribed a causal aspect because it can be described as optimizing something.

**Michael Levin** [47:38]: Yeah, that's that's super interesting and it relates to um I got an email from uh from Chris Fields a few days ago saying something similar to the extent that if you take my criteria seriously then then he says many many things in in in he was specifically talking about physics are things that in fact are not explainable the way you know under those three categories. So, um I it makes sense to me. I I've had enough um sort of uh u nasty emails about much much much, you know, much smaller claims. So, so I'm not making this this this, you know, incredibly expansive claim at this point yet.

All I've said was was the following that uh in some cases in a few cases and we've demonstrated just a handful of cases both biological and computational where it looks like the standard uh explanation does not give you the engineering power that you would like. very practically just as I don't know what the ontological status of anything is. I'm just talking about you know if we're going to build build things and and predict things and control things. However, however, I fully agree with you that once the once that door is cracked a little bit and it turns out that there is there exists at least for some things another way to look at what's going on.

Then you start looking at all the conventional things and saying well we assumed this was all going to be uh told by some kind of selection forces that we just didn't know what the what they were but we thought there must be because what else could it possibly be well once once there's a fourth option on the table then you start reooking at everything and that's in fact I I you know I have been doing that at least on the biological side is saying now now I think it's it's it's it's much more prevalent than my you know measly few examples and maybe it is almost everything or maybe it is everything I don't That's it's it's it's interesting that you and Chris both both said that.

**Karl Friston** [49:23]: Well, I'm very pleased to hear I'm in Chris's camp. That's always very reassuring. Yeah.

**Robert Chis-Ciure** [49:30]: Like u so in the way car presented the story of of structured learning ultimately the fact that some some phenotypes in virtue of the good regulator theorems and and and the wisdom of of the organism being a model of the environment embed into them certain factorizations that are profitably modable modable as incurring in the environment. So for example, the fact that we would presumably model our world beyond the Markov blanket as separating the identity of a thing of an object and the position. So you have a factorization there which car would probably say leads to an anatomical recapitulation of this factorization in for example the ventral and dorsal streams.

That's just one example of the way in which you embed a structure that is what you might call Mike and a pattern that ingress and ultimately what we end up observing are the history of the successful ingressions that are embedded in the different ways in which anatomy and physiology in the biological case are are ultimately set up are structured. And another another interesting thing that that uh comes to mind is the fact that if a world has symmetries, which we suspect our world has and we know it has, you would for example see for example a tendency to increase hemispherization across evolutionary time scale.

And we we observe that in in brains over as the brain complexity grew, the hemispherization also increases. in in humans for example being stronger than uh due to the callosal anatomy and and the way the commissures are are uh are set up it's stronger than for example in other species so in a sense as car was saying if we were to to make everything a free lunch then ultimately also everything was at some point an ingressing pattern that just happens to be successful and we we observe it So then what's what else is left for this notion of a free lunch and the notion of an ingressing pattern that seeks an embodiment and I I suspect uh it will be exactly those cases that you that you mentioned Mike where um we see failures of the usual explanation without expecting that failure to be cashed out in in some ultimately arcane pain or uh some some new physics some something extraordinary that is is uh is at play.

It will ultimately be a change of our vantage point as the observers because this is one one thing that we have not explicitly discussed today. the fact we mentioned scale invariance and and scale freess and so on, but we did not emphasize the imperative role of the observer and and the the modeling strategies that are imposed by an observer and ultimately you something exists in to the extent that it is measured by something else as I recall Karl was saying in on the nature of things if I'm not mistaken something for something to exist It must be measurable, right, Karl?

And not necessarily in the mathematical sense of a measure theory, but in the sense of having a probability mass, probability distribution.

**Karl Friston** [53:09]: Absolutely. And the Markov blanket.

**Robert Chis-Ciure** [53:17]: Obviously, obviously, obviously you are quite the idealist, Karl. You'd be surprised how close you are to an idealism. [laughter]

**Karl Friston** [53:24]: Right. I think that's a compliment. I'm not no one's really tell me what the difference is but uh can I just pick up on um just to sort of link that notion


## Chapter 12: Symmetries, observation and biological organisation

**Karl Friston** (cont.) [53:33]: of um ingressing symmetries. Um so symmetries was you know read there in the vernacular literally having having a sort of mirror symmetry in the in the way that we walk around and our brains are uh deposed. Um mathematically a symmetry just means an invariance or an equivariance. Um, and um, what that means is that you'd expect to see um, in the anatomy of anything from, you know, from from a cell to a xenobot to to a worm to to me and you, you'd expect to see um, those kinds of symmetries um, appear as factors in literally in the structure of of your of the biological organism.

And what that would look like is very much a sort of Fodorian modularity, a functional segregation and specialization. So I just mindful, you know, I can't remember whether this conversation or previously how do things know what to do in my body, you know, how does a liver cell know, you know, should be a liver cell. Well, that's just from the point of view of this um good regulator theorem read in terms of installing the right kinds of symmetries.

It's just that this has now become functionally specialized because this is part of this is how it you you ingress the cause effect structure simply because there is a statistical independence between what I the liver is doing and what the brain is doing and what and what the heart is doing.

Um so uh and this kind of factorization also speaks to the efficiency you were talking about before the statistical efficiency coining simplifying your model of the world minimizing its complexity noting that we're always in a complexity arms race. uh but for any given level of accuracy to to maximize the the minimize the surprise or maximize the marginal likelihood or the adaptive fitness you also have to keep things as simple as parsimonious as proh possible um there's one thing which is I decide to say before um I stop wittering um you just in terms of people or Mike particularly um worrying about the the cause effect structure um encompassing all kinds of possibilities.

I think that's absolutely the case. And of course the actual cause effect structure that you cocreate at any given scale will be unique to to to that point in time.

So you know it's a a space of possibilities uh simply because the the universe on the outside is usually constituted by other things like me which means I'm like ecoish construction I am actually building the you know the context that I'm trying to model you know so there is now a circular causality that creeps creeps into the game um the there the the the kind of cause effect structure that um I was referring referring to is something that Robert referred to right at the beginning when when he referred to a Langevin equation all that is and all the physics including quantum physics uh um quantum mechanics mechanics classical mechanics and the basic mechanics of the free energy principle all start with just writing down a cause effect structure in terms of some abstract state of the universe at this scale determines in some lawful way the probability of motion dynamics of that state and that's it.

You know that is causality. You know this is nothing to do with grain of causality or um the the sort of kind of causality you get in in philosophy causes. This is the causality of physics that this state causes this motion uh and probabilistically plus some random fluctuations. So to my mind that that that's an extremely expressive kind of cause effect structure. It is the definition of a probabilistic pattern you know uh and it hasn't committed to any space-time. Well actually that's a bit of a trick because the motion does depend upon time. Uh but ignoring that dependency you it's up for grabs of how you how you read this particular cause effect strategy.

You can read as a physicist you can read it as a biologist. You can read it as a behaviorist. you can read, you know, and so on and so forth, but underneath it's just a pattern.

**Michael Levin** [58:05]: Super interesting, guys. I apologize. Um, I need to uh I need to go to something here. But by all means, if if you're able to continue, I will listen with great interest to the recording. So, I'm not I'm not, you know, suggesting that this is really good, but I've got to I've got to go.

**Kyriakos (host)** [58:22]: No problem. Thank you for joining us.

**Speaker uncertain** [58:27]: President, thank you so much. It was fascinating as as always.

**Michael Levin** [58:27]: Thank you guys. Love to see it.

**Kyriakos (host)** [58:33]: Um, Robert, um, do you have anything to add to the latest thing or before I ask something to both of you?

**Robert Chis-Ciure** [58:41]: No, no, you can can go ahead.

**Kyriakos (host)** [58:41]: Um so just [clears throat] for my own kind of uh understanding but maybe listeners also are a little bit confused and I want to make sure when I use this terminology I


## Chapter 13: Intelligence, agency, sentience and consciousness

**Kyriakos (host)** (cont.) [58:57]: use it with as much accuracy as possible. Um [clears throat] what uh is the difference when we're talking about agency, intelligence, sentience and consciousness. So these four terms specifically um sometimes I I feel people use them and they understand different things when they use them. And so I'd like to understand what we mean let's say when we talk about intelligence let's say biological intelligence.

I was uh looking at your latest paper with uh Professor Levin cognition all the way down 2.0 Oh, and so um [clears throat] if I understand and correct me, tell me just if I'm in the right kind of ball park, we should think about biological intelligence or in terms of some efficient search through problem spaces be it physiological, morphological or behavioral across multiple scales. Am I on the right lines saying that?

**Robert Chis-Ciure** [1:00:01]: Very good. It's It's right on the money. Yes.

**Kyriakos (host)** [1:00:12]: Could you unpack that a little bit more? Um and and kind of contrast what that definition of intelligence entails and what additional or different properties. Um things such as agency, sentience, or consciousness uh an organism would require in order for us to say it has those kind of things.

**Robert Chis-Ciure** [1:00:36]: certainly being also mindful of the of of Karl's time and since I happen to sometimes be a philosopher it's dangerous to ask me to go on definition so so I'll try to to be brief in that specific paper that you mentioned in the cognition all the way down we operated with a Jamesian notion of intelligence in the stance of William James in principles of psychology where he defined intelligence more conceptually rather than formally as the ability to reach the same end or the same goal by different means. same goal variable means and obviously if you were to ask uh someone working in machine learning, someone working in developmental biology, someone working in in mathematics, you would probably get very different senses of intelligence, someone working in psychology for example.

We used in in that paper um the legacy of Newell and Simon for from from computer science and we tried to formalize intelligence as an efficiency metric. So it was not necessarily only the fact that you can reach a goal but also how efficient you are in the reach of that goal assuming a model of the problem space where it is the task and the trajectory which is a sequence of states made by some changes like some operators is well for.

So we have that notion of of intelligence and we in the in the diverse intelligence uh research program we try to project that on the dynamics of certain biological processes and the examples I uh we gave in that paper were uh uh amoeba movement like towards towards nutrient source and um planarian hydrogeneration upon uh barium inductively and we found out according to that model quite impressive efficiency for this notion of biological processing. Now whether that notion of intelligence is an all-encompasses the the definitive notion is a different question.

The point there was only to show that the usual story of intelligence is here is in the head and intelligence is is a symbolic property if you want of only certain kinds of processes that we usually associate with the human minds or minds in general as ingrained. We wanted to challenge that. That was the specific if you want strategic goal of of that notion of intelligence and the way we we formalized it. And that notion of intelligence is very different from sentience which I will let Karl define and also agency because it's more within his uh within his ballpark.

But I will say just one word about consciousness and the fact that consciousness and intelligence according to um widely seen view are to a certain extent dissociable. Some people say they are doubly dissociable and it also depends on how you define consciousness. But the the usual definition of consciousness in uh in the field would be the felt experience. People talk of qualia but that need not be the term we use.

It is if you want the thing that goes away in anesthesia or dream sleep. the thing that the thing that comes back when you are when you are uh awakening from from sleep or anesthesia uh the contents in your experience are themselves felt experiences thoughts I would say are also experiential in nature recollections memories are experiential the the feeling of a deja vu right it shows that something that never occurred in reality feels like a memory so there is a feeling of having a memory There is a feeling of tasting a kind of in this case diet coke.

There is a there is a feeling of um of uh listening to to uh uh what's rep if you are and that is a certain notion of phenomenal consciousness is called other people will define it differently but it's important for the viewers to understand that intelligence need not entail consciousness consciousness need not entail intelligence or at least did not entail a level of intelligence that we usually associate with with what we call intelligence in humans. And the last point on this, the fact that AI exhibits what we perhaps anthropomorphically call intelligence is not a license to attribute experience in the sense of phenomenal consciousness. So, I apologize.

**Karl Friston** [1:05:52]: Brilliant. Well, um, so I'll just I'll just rehearse what has been said, um, from a,


## Chapter 14: Intentional agency and the origins of conscious experience

**Karl Friston** (cont.) [1:06:05]: um, a mathematical perspective. Um, but I'm not going to even bother with intelligence. You just to endorse, um, this notion that intelligence is, um, is something which may or may not uh, well, is does not imply consciousness. Um and um I think um the question about um agency actually puts another interesting dimension into the way that we sort of would describe things or tell stories about things. You know, what's the difference between an autonomous process and an agent? Um and I you don't think there's any um universally accepted um notion.

Um but in my world um I would consider something that had authentic agency to be something that in Robert's words had explicit goals in mind by which I mean it had the ability to select among different futures to reach some intended outcome. So I would say that lots of things can behave and show autonomous behavior like thermostats and viruses and the like.

Um but only a few natural kinds actually act intentionally in the sense that they h they have chosen this path through their personal future towards this outcome that a priority they think they um you know they should give the kind of thing that they are. uh and immediately that that that that speaks to um another key point that Robert brought up right at the beginning which is another aspect of um scaling laws. But here deployed in terms of um what happens when things get bigger and what happens when things get bigger. Say we move from a single cell to a multicellular organization that and we now draw our Markov blanket around the periphery around the epithelia of this structure.

What that means is that the internal states with some suitable coarse graining now become sequestered from the blanket states that are doing the control that those are the things that are influencing the environment and also um the sensory states are registering the consequence of that inference. Um and that basically means that there are some inter internal states that now can be read if you want to you as a physicist you don't have to do this but if you want to tell a story to psychologists or evolutionary theorists or um behavioral um behaviorists then you can tell a story um that now the internal states look as if they are doing uh inferring their own future.

That's because their actual actions are no longer available to them. So they now become hidden causes or vicarious causes of their sensory observations. And as soon as they become random variables or hidden variables, that means that you can now interpret the internal states as making inferences about their own actions or the actions of the thing to which they are internal. Which means that if you were in machine learning or control theory, um you can now describe this thing as moving beyond control as inference to planning as inference.

So now you've got this bright line between autonomous things which may or may not be intelligent um and um authentic agents that have this intentional aspect that have to select their particular future because they are inferring the consequences of their actions.

So I think that's an important uh distinction particularly in relation to Robert's notion of you know could could could we um where would we place artificial intelligence large language models and at the moment we could certainly put them at the level of control as inference and say that they are autonomous and that they do generate material they generate predictions they respond to prompts much like a thermostat does. um but they don't plan because they don't have any um they don't have an internal generative model um of the consequences of their actions in the future. So they they don't have any intentions. Um so they can act but they have no intentions whereas you and I have intentions.

And then the next level would be um action on the inside. And then we get into phenomenology and the um the regulation usually read in terms of the deployment of um precision or attention um which um some people think then give rise to I think what Robert absolutely was I think it's quite important um when he talked about the felt experience the the feeling of something. I think that's that that that that is quite central and sort of slightly a move away from the qualitative experience the qualia you find in philosophy of mind.

I think you know and this is very reminiscent Robert of of Mark Solms's argument you know it's it's a feeling that counts um and the most if you like um the formulation that is most sympathetic to most theories such as global neural workspace theory or global workspace theory uh active inference uh and Mark Solms's constructions um uh and also the neuropsychology and you know the sleep psychology and understanding ing levels of consciousness in the sense of anesthesia and sleep for example. It seems that um once you've got the capacity to contextualize your attention or your precision waiting your um your internal modeling and planning.

Um then that would be the the prerequisite for the feeling. The ability to ignite if you like this particular inferential process or drill down or attend to this as opposed to that. That ability to actively act on the inside. So Thomas Metzinger and his colleagues might call this sort of mental action. um rendering that which was phenomenally a transparent now opaque simply because you can turn the knob on how opaque your window on your own processing is. um in the sense of smart glass.

Uh so once you got some control over your own inferential processing and belief updating um that you can associate with the dynamics on the inside then you may have you that would be if like a prerequisite for feeling. Um, so you know that as far as I understand it would be a summary of what Robert was implying in a way that is sympathetic to the accounts of people like Mark Solms who bring to the table from a sort of you from a very different perspective.

**Kyriakos (host)** [1:13:25]: Uh, Robert, do you have anything to add to that?

**Robert Chis-Ciure** [1:13:29]: only only the perhaps minor point Karl that maybe the audience is amenable to be confused when we talk about the internal states inferring the exterior and they might think of inference as in the psychological sense


## Chapter 15: Statistical inference versus symbolic reasoning

**Robert Chis-Ciure** (cont.) [1:13:46]: which we are doing perhaps symbolic sense of inference. So maybe you would want to say that that's not necessarily

**Karl Friston** [1:13:53]: no you you spotted that so you can you can explain the distinction.

**Robert Chis-Ciure** [1:13:58]: So in in the sense in which Karl means inference here is the statistical physicist sense of of inference or the stat statistician sense of inference not the the way in which we think of an inference as some some mo motion between some symbols like a premise and there is another premise and there is an argument and there's a conclusion and that's the argument and the logic between that is the inference that you make as a sort of of uh stepbystep symbolic procedure that is not the inference in the way in which the internal states are encoding probability distribution over the external states in the sense of the states that they can be read as if not that they infer.

So you you would measure the some some internal states in in some particular system you observe and you you see some homuncular symbolic system inferring the states of what is beyond the the Markov blanket of that of those internal states of that system of interest. That's not the case. It is something that you can read as a modeler, as an observer by seeing the way in which given the statistical independence of the external and the internal states, you can model the evolution of the internal states as recapitulating that of the external states of the environment.

Not that they the internal states themselves, the physical magnitudes are doing anything like a symbolic inference in the way we think of inference in the human case.

**Karl Friston** [1:15:33]: Yeah, excellent. It so um yeah that was nicely put and sort of draws a bright line between um inductive inference you might find in philosophy and the kind of abductive inference that is inherent in probabilistic mechanics you find in physics.

Uh yeah so I apologize whe when people like me and to a certain Robert use the words like surprise belief and the like they mean it in a very technical mathematical sense in the sense of Bayesian belief updating you would find in um in mathematics or belief propagation in various um um statistical tools uh where the belief is just a conditional probability distribution that has sufficient statistics and we're associating those sufficient statistics like a mean and varian with the biophysical state, the internal state of any dissipative structure. Uh at no point is it meant to imply a propositional or inductive or personal kind of belief. You know, this is not declarative.

Of course, if you have something that is self-conscious, then one might start to argue that there is now something [laughter] that becomes declarative. But that's the next level up, I think, from uh from being able to feel.

**Kyriakos (host)** [1:16:50]: That's that's very interesting. Um I'm aware of time but I had one kind of last topic that I I wanted to touch upon and um understand better and it's uh the notion of emergence. So I I'll attempt


## Chapter 16: What is emergence, and can we measure it?

**Kyriakos (host)** (cont.) [1:17:07]: to kind of give kind of my basic understanding of emergence and and you guys can correct me. Um I I understand it as we have many relatively simple components and then those components interact with each other and produce some higher level property or pattern. Now, um please do kind of nudge me to uh the the right direction if I'm off with that. But just to um add kind of a a a further question to that, I I'm curious if once that higher level pattern exists, if it can influence the components that created it and I'm also curious if emergence can be quantified. Robert, I know you're in involved when it comes to this kind of stuff. uh um uh heavily. So yeah.

**Robert Chis-Ciure** [1:18:14]: Um so let me let me just briefly say that emergence is one of those uh somewhat uh canny as in can of worms concept. where people mean very many things by and it has been sometimes used as a as a source of um u easy escape from a of an explanation. You say something is emergence as if something as if that statement the emergence is uh something more than a placeholder for a for an explanation. [clears throat] the more vernacular sense of emergence as something that might be surprisingly uh arriving from the arrangement of some micro components that has a sense of novelty to it. That is how people understand emergence.

But in in our lab for example in the work of of Lionel Barnett in the work of Seth they tried to quantify the notion of emergence in different way. they have different constructs that they propose like dynamical independence uh and and so on. So this idea that something emerges means ultimately that you you see at some coarse grain scale of observation something that is modelable as be being constituted at at a finer grain from some multiple for multiple uh partitions of constituents that are compatible with a single form at a higher level.

So for example, if you think of a traffic jam, which is a standard example of emergence, a traffic jam is something that would emerge from a certain disposition of of individual car irrespective of the identity of of the specific car or a flock of birds and in the way they they organize their flight. Those are the just the very easy examples of emergence. But then some some some people try to propose that consciousness would be something that would emerge out of brain activity or it would emerge out of insert your favorite theoretical construct you want to put forward.

And the last thing I say and then I I give this to Karl is that um to me the notion of emergence if it's not properly quantified if it's not properly made uh hypothesis to be tested um uh construct to be modeled precisely. It is just an empty placeholder. And when I hear when I see the notion emergence road something is emergent out of something else I am immediately skeptical of the understanding that's it's transmitted to me in that statement.

**Kyriakos (host)** [1:21:00]: Mhm. Mhm. Professor Levin also um we briefly touched on it on the first episode we did and um he was describing um that part of what you were saying about immersion being used as a kind of easy escape. M um so yeah that makes sense please.

**Karl Friston** [1:21:18]: Oh well I it's a very reassuring because I've never really used the word emergence. I remember the the last chapter of the particular physics book um Maxwell Maxwell Ramstead was very kind and he wrote he wrote a whole paragraph on it with emergence which I still don't really understand but now you've just given me permission never to use the word again. Um I am I am from the point of view of things like the renormalization group. I should also mention um synergetics as an important uh application of this in terms of um in terms of the slaving principle. There's also a mathematical version called center manifold theory.

So this the way that different scales talk to each other is a really central and ubiquitous theme um in maths and physics. But there's no teleology. There's there's no you don't need to use the word emergence just to have these different levels of description and look for symmetries or invariance in terms of the dynamics or the laws or the um Lagrangians that operate consistently at different scales. Um apart from the work of George Ellis on top down and bottom up causation we just come at this from a sort of physics perspective.

Um and um that's you know apart from that though um I I agree entirely with Robert it you know probably best not to use the word unless you're a philosopher and like arguments

**Kyriakos (host)** [1:22:48]: that makes a lot of sense. Um I was just kind of a closing question. Um I I have a bit I I I have a bit of a a bit of trouble understanding some of the ideas around um uh scales. So how does information uh uh uh trap travel travel


## Chapter 17: How do different scales of organisation interact?

**Kyriakos (host)** (cont.) [1:23:07]: maybe travel is the wrong word but uh move across uh scales

**Karl Friston** [1:23:14]: um mathematically you you apply something called um an RG operator where RG stands for the renormalization group and it's very simple you effectively uh do two things to a particular scale the first is to sort of group things together. Lump them lump things together and then effectively take mixtures of the things you've lumped together to reduce the dimensionality. So you got a grouping and a reduction operator. So it's another way of reading the um the RG operator. Uh it's very very simple.

Um, you know, I'm just trying to think if if if I can persuade Robert to go through the the traffic jam uh example, but if you wanted to think about how you would um summarize to somebody um traffic flow, you you wouldn't you wouldn't list, you know, on a news report, for example, um the position and the velocity of every constituent car. You would take you group together all the cars on the A24 and then you would take the average velocity. Oh, it's 3 miles per hour. And then you report that. So you you've applied uh a reduction and grouping operator in the spirit of the renormalization group.

So you've now described your system in terms of one number that applies to all the individual cars on the A24. And then that number will change over time. And then you got now another set of dynamics and equations of motion and a cause effect structure um that you can then treat at that particular scale which inherits from but also contextualizes the scale below.

**Kyriakos (host)** [1:24:53]: That makes a lot of sense. Do you guys have anything else that you would like to talk about before we end the episode?

**Karl Friston** [1:25:00]: No, I need to speak right now. [snorts]

**Robert Chis-Ciure** [1:25:00]: Now, I'm sure me and Karl could find many things to talk about, but it's it's a bit late, so probably can call it a day here.


## Chapter 18: Closing thoughts

**Kyriakos (host)** [1:25:09]: Cool. Well, thank you both so much for taking the time to have a conversation. I'll send you both link once the episode is out and yeah, I hope you have a pleasant rest of your day, guys. Thank you so much.

**Robert Chis-Ciure** [1:25:20]: Thank you, Kyriakos, for making this possible.

**Kyriakos (host)** [1:25:20]: No problem.

**Robert Chis-Ciure** [1:25:20]: Bye, Karl. Bye, Kyriakos.

**Karl Friston** [1:25:20]: Bye. Love to see you. Bye-bye.
