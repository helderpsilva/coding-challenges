def recite(start_verse, end_verse):

    list_days = {
        1:"first" , 2:"second" , 3:"third", 4:"fourth", 5:"fifth", 6:"sixth",
        7:"seventh", 8:"eighth", 9:"ninth", 10:"tenth", 11:"eleventh", 12:"twelfth"
        }

    list_items = [
            "a Partridge in a Pear Tree", "two Turtle Doves", "three French Hens",
            "four Calling Birds", "five Gold Rings", "six Geese-a-Laying",
            "seven Swans-a-Swimming", "eight Maids-a-Milking", "nine Ladies Dancing",
            "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"
            ]
    
    complete_sentence = []

    for i in range(start_verse, end_verse+1):

        sort = sorted(range(i), reverse=True)

        first_sentence = f'On the {list_days[i]} day of Christmas my true love gave to me: '

        second_sentence = ''.join([list_items[i] + (', 'if i != 0 else '.') if i != sort[-1] or len(sort) == 1
                        else 'and '+ list_items[i] + '.'  for i in sort])
        
        complete_sentence.append(first_sentence + second_sentence)

    return complete_sentence