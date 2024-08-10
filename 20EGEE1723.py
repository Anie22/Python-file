# A program that convert digit to words and words to digit

reg_no = '20/EG/EE/1723'
name = 'Francis, Edidiong Celestine'

print(f'Welcome to {name}, {reg_no} program')

#This function convert a digit to word
def figureToWord(number):
    units = ['', 'one', 'two', 'three', 'four', 'five',
             'six', 'seven', 'eight', 'nine']
    ten = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen']
    teens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
             'eighty', 'ninety']
    hundred = 'hundred'

    words = []

    if number == 0:
        return ['zero']

    if number < 0:
        words.append('minus')
        number = abs(number)

    while number > 0:
        if number >= 1000:
            words.append(units[number // 1000] )
            words.append('thousand')
            number %= 1000
        elif number >= 100:
            words.append(units[number // 100])
            words.append(hundred)
            number %= 100
            if number > 0:
                words.append('and')
        elif number >= 20:
            words.append(teens[number // 10 - 2])
            number %= 10
        elif number >= 10:
            words.append(ten[number - 10])
            number = 0
        else:
            words.append(units[number])
            number = 0

    return ' '.join(words)

#This function convert a word to digit

def wordToFigure(word):
    wordToFigure = {'one':1, 'two':2, 'three':3, 'four':4,
               'five':5, 'six':6, 'seven':7, 'eight':8,
               'nine':9, 'ten':10, 'eleven':11, 'twelve':12,
               'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16,
               'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20,
               'thirty':30, 'fourty':40, 'fifty':50, 'sixty':60,
               'seventy':70, 'eighty':80, 'ninety':90, 'hundred':100,
               'thousand':1000, 'million':1000000}

    digits = word.split()
    total_num = 0
    half_num = 0

    for digit in digits:
        if digit in wordToFigure:
            value = wordToFigure[digit]
            if value == 100:
                half_num *= value
            elif value >= 1000:
                total_num += half_num * value
                half_num = 0
            elif value > 1000000:
                print('You have exceeded the maximum value of 1 trillion')
            else:
                half_num += value

    return total_num + half_num


print('The program converts figure to word and word to figure')

# Condition to check which option is choosen
number = eval(input('Enter a figure to convert to word: '))
if number > 9999:
    print('Figure is out of range')
else:
    words = figureToWord(number)
    print(f' {number} in words is {words}')
word_inp = input('Enter a word to covert to digit: ').lower()
if word_inp != '':
    ans = wordToFigure(word_inp)
    print(f'{word_inp} in figure is {ans}')
    print('Thank you for using my program')
else:
    print('Have a nice day')



