# Language-Translator

A translation app is used to translate words and phrases quickly. Some translation apps will translate the text in a photo. Some apps allow you to speak into your microphone and then will translate your message into your chosen language. Some are simple and translate text based on what you input into the app. The technology behind these applications is Machine Translation, also known as MT. While MT has come a long way since its inception, it’s still not perfect. In many cases, MT makes mistakes that human translators would not. Here are five reasons that translation apps aren’t effective at translating all different types of content.

i.	Context

Machine Translation can’t understand context. If you’re speaking to another person, he or she can understand what words you’re replacing with pronouns, whereas MT is not yet able to do that. Similarly, people can understand what you mean when you say things like “Yes, but no. I mean, yes and no…I don’t know it’s really complicated.” That’s a very complicated series of sentences that are all related to one another. A piece of technology is not likely to realize that these statements are all connected, or that you’re talking about a subject that isn’t in these sentences.

ii.	Accuracy

Translation apps aren’t known for producing high-quality translations. Many translation apps request user feedback to create better translations, but users submit many different ways to translate the same content. Again, the context is missing. To have an accurate, high-quality translation, you need to know why the document is being translated and to whom the materials will be delivered. Translation apps, even with user-submitted translations, cannot determine the context of your document. As a result, using a translation app will prevent from having a high-quality translation of the document.
 
iii.	Confidentiality

Part of finding the right Language Service Provider (LSP) is making sure it can keep your confidential data safe. LSP’s host their servers in secure data centers, and have procedures to ensure protected information is encrypted. Translation apps don’t provide this level of safety. These apps often store data after you submit it. If you’re translating information that is confidential in any manner, you should use a human translator to ensure the information stays protected.

iv.	Editing

If you think you can use a translation app and have your LSP edit and proof the text afterward to save money, you may be surprised. The inaccurate translations provided by translation apps can take more time and can be more expensive to edit than translating the original text. While it may seem beneficial to provide pre-translated text, if it isn’t a quality pre-translation, it will take more time and money to determine what the translation should say. The best way to keep the budget low and keep the translation project on-time is to use human translators, and avoid pre-translating the text.

V.	Inaccuracies

Machine Translation is still being researched and improved, and therefore it still experiences inaccuracies. If you don’t know the language you’re translating to, you may end up with a translation fail rather than a usable message. The consumers won’t receive or discuss the message if it is inaccurately translate. This leads to poor translation. To ensure high-quality, confidential, accurate translations, a dedicated LSP can be helpful. Translation demands a deep understanding of both grammar and culture. Translators need to know the rules of a language as well as the habits of the people who speak it and even for the most experienced professionals, confusion and frustration are familiar feelings. Whether you need to translate literature or medical content, each text comes with difficulties and requires specific language skills. Choosing the right words depending on the context and the purpose of the content is an art that translators master over years of working in this industry. Idioms, phrasal verbs, unique words, and humor are the most difficult to translate. But so are medical terms, industry - specific terminology, and jargon. You need context and research, as well as in-depth knowledge of the language pair, to keep the meaning of the original content and deliver it in an easy to read format in the target language. 

The common challenges in translation include:
 

a.	Translating Idioms:

Idioms are linguistic expressions, specific to each language or culture. While they’re essential elements of the language, they’re also difficult to explain when you’re not aware of the cultural differences between the source and target languages. Think about “it’s raining cats and dogs” or “wrapping your brain around something”. If translators went for a literal translation of these expressions, a foreign audience wouldn’t understand what the text was about. That’s why it’s essential for a translator to recognize idioms and understand the exact meaning before translating the text. It’s difficult because dictionaries often limit definitions to single words or a small number of expressions. “It’s raining cat and dogs,” for instance, means that it’s raining heavily. Linguists need to know the right meaning of the idiom and then look for alternative versions that express the same concept in the target language. Luckily, most languages have idioms to express the concept of heavy rain. So, in this particular case, you can use a similar construction to maintain the tone and voice of the original text in the translated version.

b.	Translating phrasal verbs:

Phrasal verbs are tough challenges in translation, especially when translating from English into languages that don’t use similar constructions. Phrasal verbs are composed of a verb and a preposition, or an adverb, or both. This makes it difficult for translators to recognize it at first glance. Most translators are native speakers of the target language, so English is their second language. The difficulty comes from the fact that the phrasal verb gets an entirely different meaning after you add the preposition or adverb. Think about “to run” vs “to run away” vs “to run into”. It may be easy for you to notice the difference, but for someone who doesn’t speak English every day, it can be a real challenge to get the right meaning of each of these three verbs.

c.	Translating prefixes and suffixes:

Prefixes and suffixes create variety in English. They also turn nouns into adjectives or verbs into nouns, which can quickly become a translator’s nightmare, especially when the target language isn’t that flexible when it comes to creating new words. These groups of letters that English speakers often use to provide deeper meanings to words are hard to translate when the other language doesn’t have so many layers to express the same concept. Most languages use prefixes and suffixes to create new words but
 
each one has different rules when it comes to preserving meanings and empowering words. Slang, f or example, uses many compound words, as well as suffixes to give new meanings to existing words, making it hard for translators to translate the right message in a different language.

d.	Words with no correspondent in target language:

Every language has words that are impossible to translate into some other languages, such as “serendipity” or “procrastination”. When one language has a specific word to describe a situation, finding an alternative expression in another language becomes a challenge in translation. Asian languages, for example, have many words to describe feelings and sensations that are hard to translate into other languages using a single word. “Shinrin -yoku” is the Japanese way of expressing the relaxation you get from bathing in the forest (both figuratively or literally). The Chinese “Yuan bei” means a sense of complete accomplishment.
#  Proposed solution
The Proposed solution is building a Personal Translator Application Using Language Translation API. Language translator translates text from one language to another. A flask application is built by using a Language Translator API. The API supports two endpoints, “detect” and “translate”. As the name suggests, one is for detecting the language, and the other is for translating from one language to another. Language Translator APIs can be seamlessly integrated into your applications, websites, tools, or other solutions to provide multi-language user experiences. It performs language translation and other language-related operations such as text language detection. The user selects the language and gives the input text to be translated and the result is showcased on UI.
 



# SYSTEM ANALYSIS & DESIGN

 Requirement Specification 
3.1 Software Requirements
OS	: Windows/Linux
Rapid API	: Subscription to Text Processing API
Python IDE	: Visual Studio Code or Pycharm or Anaconda

Hardware Requirements

RAM         : 4GB or Higher Processor  : Intel i3 or above Hard Disk  : 256 GB

# Software designing
Anaconda Navigator: Anaconda Navigator is a free and open-source distribution of the Python and R programming languages for data science and machine learning related applications. It can be installed on Windows, Linux, and macOS. Conda is an open-source, cross-platform, package management system. Anaconda comes with great tools like JupyterLab, Jupyter Notebook, QtConsole, Spyder, Glueviz, Orange, Rstudio, Visual Studio Code.

To make a responsive python script the following packages are required.

Requests: Allows you to send HTTP requests using Python.

Flask: Web framework used for building Web applications
API: An application programming interface (API) is a computing interface which defines interactions between multiple software intermediaries.
Steps to install the packages :

1.	Open anaconda prompt.
2.	Type "pip install requests” and click enter.
3.	Type “pip install Flask” and click enter

   ![image](https://github.com/user-attachments/assets/3c372763-b99f-4be8-aeb1-a6432a17f119)

   The user interacts with the web application to fetch the translated results of the given input using language translator API in the form of HTTP REQUEST and the API detects the language and translates the text to selected language and outputs to the web in the form of HTTP RESPONSE.

# Flow Chart

o	Registering for RAPID API Data Preprocessing.
|
o	Subscribing to the desired API.
|
o	Downloading the python code for API calling.
|
o	Test the API endpoint via the code snippet.
|
o	Importing the libraries and Initiating the Flask App.
|
o	Define a function that calls your API to fetch results via web app.
|
o	Configure the Home page and Translator.
|
o	Configure the Results page.
|
o	Run the application.
|
o	Open the browser and navigate to localhost:5000 to check your application.

![image](https://github.com/user-attachments/assets/1f91503d-5d02-48ad-b5ff-b48a5459a80c)

# Use Case Diagram
![image](https://github.com/user-attachments/assets/55c22b94-5527-4aec-b67c-bbd917aaaac7)

# Sequence Diagram

![image](https://github.com/user-attachments/assets/3a4fdeed-73dd-4d5c-af90-fc9857e05ca0)

# Outputs:


![image](https://github.com/user-attachments/assets/4f766213-90d3-40c0-a210-8ae4d9ed2786)

![image](https://github.com/user-attachments/assets/428bf753-22f2-462e-9ab4-5433ee3ba736)
![image](https://github.com/user-attachments/assets/54141a14-1a66-4af5-a36e-aeabc9c5ac20)


In conclusion, the language translation application comes very handy for numerous purposes. It is better to find an appropriate word in the target language for the phrase or verb in its entirety rather than attempting a literal translation. The number of people using the translation apps will increase tremendously especially to learn and translate the message to target language to communicate universally.


