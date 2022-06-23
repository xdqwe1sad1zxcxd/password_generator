from random import choice


chars = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
amount = int(input('Сколько паролей сгенерировать? '))
length = int(input('Введите длину пароля/паролей: '))


def generate_pass(pass_amount: int, pass_length: int) -> str:
    for _ in range(pass_amount):
        yield ''.join(choice(chars) for _ in range(pass_length)) + '\n'


def save_passwords(string: str, write_mode='a'):
    with open('passwords.txt', write_mode, encoding='utf-8') as file:
        file.write(string)


def main():
    answer = input('Хотим стереть прошлые пароли перед заполнением? ').lower().strip()
    if answer in ['yes', 'да']:
        with open('passwords.txt', 'w') as file:
            file.write('')
        for password in (generate_pass(amount, length)):
            save_passwords(password)
        return
    for password in (generate_pass(amount, length)):
        save_passwords(password)


if __name__ == '__main__':
    main()
