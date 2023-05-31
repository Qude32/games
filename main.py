import random
import time


def rock_paper_scissors():
    print('\n📦 Вы играете в "Камень, ножницы, бумага". Игра идет до 3х побед одного из участников.')
    user_point = 0
    comp_point = 0
    while user_point != 3 and comp_point != 3:
        options = ['камень', 'ножницы', 'бумага']
        computer = random.choice(options)
        user_answer = input('\nВведите: камень, ножницы или бумага: ').lower()
        if user_answer == computer:
            print('🤝 Ничья 🤝'
                  f'\nКомпьютер ответил: {computer}'
                  f'\nПромежуточный счет: [Вы: {user_point} | Компьютер: {comp_point}]')
        elif user_answer == 'камень' and computer == 'ножницы':
            print('👍 Вы выиграли! 👍'
                  f'\nКомпьютер ответил: {computer}')
            user_point += 1
            if user_point < 3:
                print(f'Промежуточный счет: [Вы: {user_point} | Компьютер: {comp_point}]')
        elif user_answer == 'ножницы' and computer == 'бумага':
            print('👍 Вы выиграли! 👍'
                  f'\nКомпьютер ответил: {computer}')
            user_point += 1
            if user_point < 3:
                print(f'Промежуточный счет: [Вы: {user_point} | Компьютер: {comp_point}]')
        elif user_answer == 'бумага' and computer == 'камень':
            print('👍 Вы выиграли! 👍'
                  f'\nКомпьютер ответил: {computer}')
            user_point += 1
            if user_point < 3:
                print(f'Промежуточный счет: [Вы: {user_point} | Компьютер: {comp_point}]')
        else:
            print('👎 Вы проиграли 👎'
                  f'\nКомпьютер ответил: {computer}')
            comp_point += 1
            if comp_point < 3:
                print(f'Промежуточный счет: [Вы: {user_point} | Компьютер: {comp_point}]')
    print(f'\nИтоговый счет: [Вы: {user_point} | Компьютер: {comp_point}]')
    if user_point > comp_point:
        print('Вы победили в этом раунде!')
    else:
        print('Вы проиграли в этом раунде...')


def guess_the_number():
    print('\n📝 Вы играете в "Угадай число"')
    computer = random.randint(0, 100)
    user_answer = 0
    counter = 0
    while user_answer != computer:
        user_answer = int(input('\nВведите число: '))
        if user_answer < computer:
            print('Загаданное число больше.')
            counter += 1
        elif user_answer > computer:
            print('Загаданное число меньше.')
            counter += 1
        else:
            print('👍 Вы угадали! 👍')
            counter += 1
    print(f'Всего было {counter} попыток.')


def game_of_dice():
    print('\n🎲 Вы играете в кости! У вас и компьютера по 3 попытки. Победитель - набравший большее кол-во очков.')
    user_total_point = 0
    comp_total_points = 0
    for i in range(1, 4):
        input('\nНажмите Enter, чтобы бросить кубики: ')
        print(f'\n{i}-я попытка')
        user_cube_1 = random.randint(1, 6)
        user_cube_2 = random.randint(1, 6)
        user_total = user_cube_1 + user_cube_2
        user_total_point += user_total
        comp_cube_1 = random.randint(1, 6)
        comp_cube_2 = random.randint(1, 6)
        comp_total = comp_cube_1 + comp_cube_2
        comp_total_points += comp_total
        print('\nВаш результат:'
              f'\nПервый кубик: {user_cube_1}'
              f'\nВторой кубик: {user_cube_2}'
              f'\nСумма двух кубиков: {user_total}')
        print('\nХод компьютера...')
        time.sleep(2)
        print('\nКомпьютер: '
              f'\nПервый кубик: {comp_cube_1}'
              f'\nВторой кубик: {comp_cube_2}'
              f'\nСумма двух кубиков: {comp_total}')
    print('\nИгра окончена!'
          'Подсчет результатов...')
    time.sleep(2)
    if user_total_point > comp_total_points:
        print(f'👍 Вы выиграли! 👍 Итоговый счет [Вы: {user_total_point} | Компьютер: {comp_total_points}]')
    elif user_total_point < comp_total_points:
        print(f'👎 Вы проиграли... 👎 Итоговый счет [Вы: {user_total_point} | Компьютер: {comp_total_points}]')
    else:
        print(f'🤝 Ничья. 🤝 Итоговый счет [Вы: {user_total_point} | Компьютер: {comp_total_points}]')


def main_menu():
    while True:
        print('Доступные игры:\n'
              '1) Камень, ножницы, бумага\n'
              '2) Угадай число\n'
              '3) Игра в кости')
        print('Введите номер игры или введите "over" для выхода: ', end='')
        game = input().lower()
        if game == '1':
            rock_paper_scissors()
        elif game == '2':
            guess_the_number()
        elif game == '3':
            game_of_dice()
        elif game == 'over':
            print('Работа программы завершена.')
            break
        else:
            print('Номер неверный, такой игры нет.')
        print()


main_menu()
