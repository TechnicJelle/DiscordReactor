# DiscordReactor
[![aur](https://img.shields.io/badge/aur-%231793D1.svg?style=flat&logo=arch-linux&logoColor=white)](https://aur.archlinux.org/packages/discord-reactor-git)

![Promo image](.github/images/promo.png "Promo image")

Discord doesn't allow reactions with more than one of the same emoji, so finding alternatives to use instead was always a time-consuming task, but not anymore!\
With this small Python script you can convert any sentence to a valid list of Discord emojis, so you can use them to react to messages!\
[Try it here directly in your browser!](http://technicjelle.com/DiscordReactor/)

## Examples
A successful conversion
```bash
> python discord-reactor.py
Message to turn into Discord react emojis: Hello World
:regional_indicator_h: :regional_indicator_e: :regional_indicator_l: :clock3: :regional_indicator_o: :black_small_square: :regional_indicator_w: :o2: :regional_indicator_r: :alarm_clock: :regional_indicator_d:
```
![Hello World](.github/images/ex_helloworld.png "Hello World")

Not enough emojis
```diff
Message to turn into Discord react emojis: Yeeeeeeyyyyy
Impossibility at letter Y
Impossibility at letter E
- Impossible message!
```

Invalid input
```diff
Message to turn into Discord react emojis: @!%@&@!%*!#%
- Invalid input!
```

Support for command line arguments:
```bash
> python discord-reactor.py Hello World
:regional_indicator_h: :regional_indicator_e: :regional_indicator_l: :clock3: :regional_indicator_o: :black_small_square: :regional_indicator_w: :o2: :regional_indicator_r: :alarm_clock: :regional_indicator_d:
```

## Installation
You can now install this script from the AUR: https://aur.archlinux.org/packages/discord-reactor-git
```bash
> paru -S discord-reactor-git
Discord Reactor installed successfully.

> discord-reactor Hello
:regional_indicator_h: :regional_indicator_e: :regional_indicator_l: :clock3: :regional_indicator_o:
```

## Contributing
If you find another emoji that could be used as a letter that isn't already in the disctionary, please don't hesitate to PR and add it! :)
