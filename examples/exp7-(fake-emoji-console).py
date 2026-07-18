from ShadowB import emoji, fake, console

while True:
    ex1 =  emoji.random_emoji()
    ex2 = emoji.random_emoji()
    if ex1 == ex2:
        console.success(f"Match lol{emoji.crying()}")
        console.info(f"Ur new name is : {fake.username()}, and ur new email is {fake.email()}, ok so are u from {fake.random_country()}?")
        break
    else:
        console.warning("Repeat again")