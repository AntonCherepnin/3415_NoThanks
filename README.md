# No Thanks

## Привала игры  

### Карты и фишки
* Колода состоит из 33 карт с номиналоми от 3 до 35, а также фишки откупа, у каждого игрока в начале 11 таких фишек.

### Комплектность
* 33 игральных карты с номерами 3–35.
* 55 фишек.

### Раздача
* 3 - 5 игроков.
* 33 карты перемешиваются и 9 из них уходят в «коробку».
* Оставшиеся 24 карты выкладываются рубашкой верх на середину стола. 
* Игрокам раздаётся по 11 фишек, если игроков меньше 5, лишние фишки отбрасываются.
  * Фишки нужны для двух целей.
    * Первая - они являются положительными очками в конце игры.
    * Вторая - вы можете потратить 1 фишку, чтобы отказаться от карты и не потерять указанные на ней очки.
  * Количество фишек одного игрока неизвестно для других.

### Условие победы
* Побеждает игрок, набравший наименьшее количество штрафных очков.

### Правила игры 
* Игроки ходят по очереди.
* Одна карта лежит лицом вверх посередине стола.
* В свой ход каждый игрок
   * Взять карту и положить ее перед собой и получить за это штрафные очки.
   * Отказаться от карты и выложить за это одну свою фишку рядом с ней.
   * Если игрок отказывается взять карту следующий игрок сидящий слева, должен сделать свой выбор: взять карту (вместе с фишкой) или отказаться и положить свою фишку рядос с первой.
   * Если игрок наконец решит взять карту, он кладет её лицом вверх перед собой и забирает все фишки, которые лежали вместе с этой картой.
* Игрок может собирать из карт неразрывные «цепочки», при этом количество штрафных очков за такую «цепоячку» будет равно карте с наименьшим номером с ней. Например, если у игрока карты 20, 21, 22 и 23, эти четыре карты вместе дают ему 20 штрафных очков.
* Когда все 24 карты были использованы и оказались у игроков, выполняется финальный подсчет своих очков.

### Подсчет очков
* Выполняется финальный подсчет очков каждого из игроков.
* Суммируется номера отдельных карт и наименьший номер карты в цепочках. 
* Из этой суммы  вычитает количество фишек, оставшееся у игрока в руке.
* Пример подсчета очков:
  * У Даши есть три отдельных карты и 2 цепочки в конце игры (3 7 8 10 14 15 16 25). За это она получает 59 штрафных очка (3+7+10+14+25=59). Из этой суммы она вычитает 8 очков за 8 фишек, получая конечный результат в 51 очко (59-8=51).

## Пример текстового интерфейса игры
Играет Anton, Alex и Bob
```
Players:
Alex = []
Bob = []
Anton = []
-----
Top: 19 coins: 0
Вы должны Взять карту(take) или Потратить фишку(spend)
Alex: spend
Top: 19 coins: 1
Bob: take
Top: 12 coins: 1
Alex: take
-----
Players:
Bob = []
Alex = [12]
Anton = []
----
Top: 25 coins: 0
Alex: spend
Top: 25 coins: 1
Anton: spend
Top: 25 coins: 2
Bob: spend
Top: 25 coins: 3
Alex: spend
Top: 25 coins: 4
noobik77: spend
Top: 25 coins: 5
Bob: spend
Top: 25 coins: 6
Alex: spend
Top: 25 coins: 7
Anton: spend
Top: 25 coins: 8
Bob: spend
Top: 25 coins: 9
Alex: spend
Top: 25 coins: 10
Anton: spend
Top: 25 coins: 11
Bob: take
-----
Players:
Bob = [25]
Alex = [12]
noobik77 = []
....
Players:
Bob = [25, 29, 7, 3, 4, 5, 35, 30]
Alex = [6, 12, 13, 14, 15, 19, 21]
Anton = [8, 9, 10, 11, 22, 24, 17, 18, 27]
-----
Leaderboard:
1. Alex = 50
2. Anton = 87
3. Bob = 88
----
Alex WIN!
```
## Формат save-файла
```json
{
  "top": {
    "card":15,
    "coins":0},
  "deck": [32, 25, 18, 27, 4],
  "current_player_index": 0,
  "players": [
    {
      "name": "Alex",
      "coins": 10,
      "hand": [33, 22, 14, 28, 7],
      "is_human": true
    },
    {
      "name": "Bob",
      "coins": 8,
      "hand": [13, 15, 19, 21],
      "is_human": false
    },
    {
        "name": "Anton",
        "coins": 15,
        "hand": [8, 9, 10, 11],
        "is_human": true
    }
  ]
}
```
