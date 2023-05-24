from .summarize import summarize
from .credentials import api_key

def test_summarize_short_text():
    text = "This is a short text for summarization."

    summary = summarize(text, api_key)

    assert isinstance(summary, str)
    assert len(summary.split()) <= 200

def test_summarize_long_text():
    text = " Hi everybody and welcome to Deep Learning for Audio with Python. In this course we're going to learn a lot about deep learning. So what about the learning goals? So first of all, I want you to understand the capabilities and limits of deep learning. So what's possible and what's not possible? Then after that we're going to learn a lot about the fundamental theory behind neural networks. We're going to learn a little bit about the math, for example, that powers this very powerful algorithms. And then we're going to move on to more practice-based stuff. And we're going to learn how to code deep learning networks using industry standards deep learning libraries like TensorFlow. And then obviously we're going to play around with a bunch of different types of neural networks. So like RNMs, CNNs, we're going to learn what all of these action names like really stand for. Cool. The one thing that you should understand about this course is that its focus is on audio and music. Now, can you follow this course even if you're not interested in audio at all? Yes, you can because at the end of the day this is a deep learning course. And so you're going to learn all the theory and implementation about deep learning, but bear in mind that all the examples are good or most of the examples I should say are going to be using audio data or music. Now, what about the technologies that we're going to use? So obviously we're going to use Python. And on top of that we're going to use TensorFlow. So why did they choose both technologies? Right. So Python and TensorFlow are both industry standards for artificial intelligence. So if you're trying to like pick up a job in AI or machine learning, obviously you already know that Python is the way to go. You're going to be required to know or learn Python. And then obviously on top of that, does this super nice deep learning library called TensorFlow, which is used almost everywhere in startups, corporations and even in academia and for doing research. Now, the great thing about TensorFlow is that on top of TensorFlow you have kind of like high-level interface that's called Keras that enables you to create very complex networks using very little code. So that's fantastic and that's very nice. Like just like to get started with deep learning. And finally, another reason why we are going to use TensorFlow is because it is open source. And so if you want to take things around, you actually can. Now, what about the content? So what are we going to actually learn? So you're going to get an intro to artificial intelligence, machine learning and deep learning. So you were going to kind of like learn the differences and the overlaps of these different fields and subfields. But then after that, we're going to move on and jump into the different flavors of new networks that are out there. So we'll start with something that's been like historically the initial network that has been widely adopted. And that's the multilayer perception. Then after that, we're going to get into convolutional neural networks or CNNs. And you may be familiar at least like with this acronym and these networks are super useful for doing processing with images or and also like read audio. And then we're going to jump onto recurrent neural networks or RNNs. And these are fantastic algorithms that you want to use for predicting like time series and for handling time series types of data. And then finally, we're going to look into guns or generative adversarial networks that are super fashionable these days. So what should you expect from this course? What type of style in some stuff like learning? Well, we're going to have three different blocks, I would say. Well, we're going to learn quite a lot about theory. Now, I'm not going to go super deep into math because at the end of the day, this is not a math course, but you're going to learn quite a lot about basic linear algebra and derivatives and these kind of things because we need them to understand how neural networks work and how to trick them in order to have like very effective like algorithms like for solving our problems. Now, we're going to use all of these theory and we're going to implement that. And so basically we're going to have a bunch of different coding tutorials where we're going to use both Python for coding neural networks from scratch. But then on top of that, we're going to have TensorFlow code where we're going to create very complex neural networks. Now, the third part of this is we're going to have a bunch of different applications, kind of real word applications, I would say, where we're going to test all of the knowledge that we've acquired from theory and basic TensorFlow code. So obviously, this is like a very important question. So where do you get code and slides? So I'm going to have a GitHub page like my GitHub page and I'm going to post all of this lessons online. And so you can just like browse them and download what you need. And obviously all of this information is going to be below in the description of each video in the series. Cool. So who's this course for? Now, when I designed this course, I had in mind Python developers who want to pick up deep learning skills. And so this is not a course for beginners, rather like for actual developers. And also this, if you are like a dev who's already playing around with a bunch of this deep learning libraries like TensorFlow, for example, but you want to learn more about how you can, so how like neural networks really work like under the hood. So this is really perfect for you because you're going to get like an understanding like at a deeper level. Now, obviously, this course is also very useful for devs who have an interest in audio and music. Because at the end of the day, you're going to be introduced to AI music and AI audio. And if you are a practitioner who's got some experience in audio digital signal processing or DSP and you want to step up your game even more and get into a UI, again, this is like the right course for you. And finally, I think like another category who would benefit quite a lot from this course are a data analyst who want to learn more about machine learning and who want to learn more about AI as well and how to get things out. As I mentioned, this is not a course for Python beginners, rather you should have some intermediate coding skills because at the end of the day, I'm not going to teach you how to code the focus of this course is on AI, not coding itself. Now, if you know quite a lot about basic linear algebra, that's fantastic, but it's definitely not necessary because I'm going to cover all the month will need to understand neural networks. At the same time, if you know about audio digital signal processing, that's fantastic. But it's not really necessary because again, I'm going to cover all the DSP stuff that we really need. Cool. So this was it for the course overview. So now just brace yourself. Deep learning is coming. Bye."
    summarized_max_len = 100
    temperature = 0.5
    max_tokens = 300

    summary = summarize(text, api_key, summarized_max_len, temperature=temperature, max_tokens=max_tokens)

    assert isinstance(summary, str)
    assert len(summary.split()) <= 100





