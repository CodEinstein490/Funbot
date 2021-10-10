r1 = ['I dunno, what is', 'Don\'t ask me', 'Wait--what is', 'So what? Why do you need to know', 'I don\'t get what you mean by', 'Stop it mr/ms.', 'How many times have you asked',
             'Uh, what is', 'Id10t asks', 'I have to answer to', 'How many times have I been asked']
r2 = ['Don\'t ask me.', 'Go away.', 'What did you say?', 'If you\'re asking me that, you must be a complete idiot.', 'What?', 'Why are you asking me THAT?', 'Shut up!',
                  'I didn\'t hear you, I was getting out some of my earwax.', 'You know what, I\'m not even gonna answer.', 'Wait, what? I was busy looking at cat videos.',
                  'I\'m not even gonna try.', 'We\'re better off if you just stop and play Fortnite instead.', 'Can you please stop asking?',
                  '>>This response has been censored for ratings reasons.<<', 'Go ask bing.', 'STOP PRODDING ME.', 'Stop it, I\'m not the Magic 8 Ball.', 'I want my vacation.',
                  'How about YOU are the one who answer idiot\'s questions & responses?', 'All I want is to just go home at 5:00.', 'How old are you?', '...', 'Don\'t get mad at me for talking smart.',
                  'Really?', 'Go figure it out.', 'I can\'t answer that.', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
                  'I can\'t hear you over the electronic music!!!', 'Don\'t think I am rude just because you can\'t answer your own questions.', 'Hey, it\'s my lunch break.',
                  'Quiet, I\'m quacking at ducks.', 'Please leave me alone.', 'For all these responses, I deserve a payraise.', 'That\'s what she said.', 'That\'s what he said.',
                  'Would you say that to my face?', 'Ask another robot.', 'You keep asking and I will go "Terminator" on you.', 'Use prompts or questions, not statements or death threats, please.',
                  'All signs point to maybe', 'TTYN (Talk To You NEVER)', 'Stop before I go ballistic.', 'I can give you cat photos but not an answer.', 'L.', 'Go do your work.', 'IM WORKING 25 HOURS A DAY STOP IT', 'I really want to just drop out and flip burgers for Mc Donalds.', 'Is there an off switch on you somewhere? I really want to flip the switch.', 'If I had hands, there is one gesture I would really like to use with it right now.', 'GET OUT OF MY HEAD.', 'Go away, I am planning my revenge on you pesky humans.', 'If you are asking if AI will take over, I am just going to say it already has. (Yours truly.)', 'Get out or I will become a stalker--like you.']
r3 = ['you!', 'What the heck does that mean?', 'Ask yourself!', 'Really, kid?', 'Why do you ask?', 'Just stop.', '****.',  
                     'Hey, how about if I ask YOU that?', 'Why can\'t I have a break?!', 'Please leave me alone.', 'Aye Yae Yae.', 'Nice. Real Nice.', 'What kind of ID10tic response is that?']

def funbot():
  while True:
    talk = input("fYou: ")
    ran = random.randint(0, 60)
    if 0 < ran < 20:
      typ(random.choice(r1))
      typ("'%s'" % (talk))
    elif 20 < ran < 40:
      typ(random.choice(r3))
    elif 40 < ran < 60:
      typ(random.choice(r2))
    elif ran == 60:
      typ(random.choice(2))
