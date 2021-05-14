# DiscordReactor

![Promo image](images/promo.png "Promo image")

Discord doesn't allow more than one of the same emoji, so finding alternatives to use instead was always a time-consuming task, but not anymore!\
With this small Python program you can convert any sentence to a valid list of Discord emojis, so you can use them to react to messages!\
[Try it here directly in your browser!](https://onlinegdb.com/LI3PE963P)

## Examples
A successful conversion
```
Message to turn into Discord react emojis: Hello World
:regional_indicator_h: :regional_indicator_e: :regional_indicator_l: :clock3: :regional_indicator_o: :black_small_square: :regional_indicator_w: :o2: :regional_indicator_r: :alarm_clock: :regional_indicator_d:
```
![Hello World](images/ex_helloworld.png "Hello World")

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