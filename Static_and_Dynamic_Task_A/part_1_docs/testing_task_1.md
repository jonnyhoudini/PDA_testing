### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# if statement uses assignment instead of equality operator and there should be a colon after else

  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# Typo on def to define function and no indentation

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# total is not assigned a value in first line of function
# return is inside the for loop
# you can't concatenate a string to an integer

def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
