"""Програма-гра 'Хто хоче стати мільйонером' на Python."""

import random
import json
import os


class MillionaireGame:
    """Клас для гри 'Хто хоче стати мільйонером'"""

    def __init__(self):
        self.questions = [
            {
                "question": "Яка столиця України?",
                "options": ["А) Львів", "Б) Харків", "В) Київ", "Г) Одеса"],
                "correct": 2,  # В) Київ (індекс 2)
                "difficulty": "easy",
            },
            {
                "question": "Скільки днів у високосному році?",
                "options": ["А) 365", "Б) 366", "В) 367", "Г) 364"],
                "correct": 1,  # Б) 366
                "difficulty": "easy",
            },
            {
                "question": "Хто написав роман 'Тіні забутих предків'?",
                "options": [
                    "А) Тарас Шевченко",
                    "Б) Іван Франко",
                    "В) Михайло Коцюбинський",
                    "Г) Леся Українка",
                ],
                "correct": 2,  # В) Михайло Коцюбинський
                "difficulty": "medium",
            },
            {
                "question": "Яка найвища гора в Україні?",
                "options": ["А) Говерла", "Б) Петрос", "В) Піп Іван", "Г) Бребенескул"],
                "correct": 0,  # А) Говерла
                "difficulty": "medium",
            },
            {
                "question": "У якому році Україна проголосила незалежність?",
                "options": ["А) 1990", "Б) 1991", "В) 1992", "Г) 1989"],
                "correct": 1,  # Б) 1991
                "difficulty": "medium",
            },
            {
                "question": "Яка найдовша річка в Україні?",
                "options": [
                    "А) Дністер",
                    "Б) Дніпро",
                    "В) Південний Буг",
                    "Г) Сіверський Донець",
                ],
                "correct": 1,  # Б) Дніпро
                "difficulty": "hard",
            },
            {
                "question": "Скільки областей в Україні?",
                "options": ["А) 24", "Б) 25", "В) 26", "Г) 27"],
                "correct": 0,  # А) 24
                "difficulty": "hard",
            },
            {
                "question": "Який елемент має символ 'Au' в таблиці Менделєєва?",
                "options": ["А) Срібло", "Б) Золото", "В) Алюміній", "Г) Аргентум"],
                "correct": 1,  # Б) Золото
                "difficulty": "hard",
            },
            {
                "question": "Хто з цих письменників отримав Нобелівську премію з літератури?",
                "options": [
                    "А) Іван Франко",
                    "Б) Тарас Шевченко",
                    "В) Світлана Алексієвич",
                    "Г) Ліна Костенко",
                ],
                "correct": 2,  # В) Світлана Алексієвич
                "difficulty": "hard",
            },
            {
                "question": "Яка швидкість світла у вакуумі?",
                "options": [
                    "А) 299,792,458 м/с",
                    "Б) 300,000,000 м/с",
                    "В) 299,792,458 км/с",
                    "Г) 300,000 км/с",
                ],
                "correct": 0,  # А) 299,792,458 м/с
                "difficulty": "expert",
            },
            {
                "question": "Який український козацький гетьман підписав Переяславську угоду?",
                "options": [
                    "А) Іван Мазепа",
                    "Б) Богдан Хмельницький",
                    "В) Петро Сагайдачний",
                    "Г) Іван Виговський",
                ],
                "correct": 1,  # Б) Богдан Хмельницький
                "difficulty": "medium",
            },
            {
                "question": "Яке місто є найбільшим портом України?",
                "options": ["А) Маріуполь", "Б) Херсон", "В) Одеса", "Г) Миколаїв"],
                "correct": 2,  # В) Одеса
                "difficulty": "easy",
            },
            {
                "question": "Хто з українських письменників написав 'Лісову пісню'?",
                "options": [
                    "А) Леся Українка",
                    "Б) Іван Франко",
                    "В) Панас Мирний",
                    "Г) Марко Вовчок",
                ],
                "correct": 0,  # А) Леся Українка
                "difficulty": "medium",
            },
            {
                "question": "Скільки струн має класична гітара?",
                "options": ["А) 5", "Б) 6", "В) 7", "Г) 8"],
                "correct": 1,  # Б) 6
                "difficulty": "easy",
            },
            {
                "question": "Який хімічний елемент має найменшу атомну масу?",
                "options": ["А) Гелій", "Б) Водень", "В) Літій", "Г) Берилій"],
                "correct": 1,  # Б) Водень
                "difficulty": "medium",
            },
            {
                "question": "У якому році відбулася Чорнобильська катастрофа?",
                "options": ["А) 1985", "Б) 1986", "В) 1987", "Г) 1984"],
                "correct": 1,  # Б) 1986
                "difficulty": "medium",
            },
            {
                "question": "Яка планета Сонячної системи найближча до Сонця?",
                "options": ["А) Венера", "Б) Земля", "В) Меркурій", "Г) Марс"],
                "correct": 2,  # В) Меркурій
                "difficulty": "easy",
            },
            {
                "question": "Хто створив теорію відносності?",
                "options": [
                    "А) Ісаак Ньютон",
                    "Б) Альберт Ейнштейн",
                    "В) Галілео Галілей",
                    "Г) Стівен Хокінг",
                ],
                "correct": 1,  # Б) Альберт Ейнштейн
                "difficulty": "easy",
            },
            {
                "question": "Яка найглибша точка Світового океану?",
                "options": [
                    "А) Маріанська западина",
                    "Б) Пуерто-Риканський жолоб",
                    "В) Японський жолоб",
                    "Г) Філіппінський жолоб",
                ],
                "correct": 0,  # А) Маріанська западина
                "difficulty": "hard",
            },
            {
                "question": "Скільки кісток у дорослої людини?",
                "options": ["А) 196", "Б) 206", "В) 216", "Г) 226"],
                "correct": 1,  # Б) 206
                "difficulty": "hard",
            },
            {
                "question": "Який український композитор написав оперу 'Запорожець за Дунаєм'?",
                "options": [
                    "А) Микола Лисенко",
                    "Б) Семен Гулак-Артемовський",
                    "В) Кирило Стеценко",
                    "Г) Левко Ревуцький",
                ],
                "correct": 1,  # Б) Семен Гулак-Артемовський
                "difficulty": "hard",
            },
            {
                "question": "Яка валюта використовується в Японії?",
                "options": ["А) Вона", "Б) Юань", "В) Єна", "Г) Рупія"],
                "correct": 2,  # В) Єна
                "difficulty": "easy",
            },
            {
                "question": "Хто написав роман 'Майстер і Маргарита'?",
                "options": [
                    "А) Лев Толстой",
                    "Б) Михайло Булгаков",
                    "В) Федір Достоєвський",
                    "Г) Антон Чехов",
                ],
                "correct": 1,  # Б) Михайло Булгаков
                "difficulty": "medium",
            },
            {
                "question": "Скільки хвилин в одній добі?",
                "options": ["А) 1440", "Б) 1400", "В) 1480", "Г) 1420"],
                "correct": 0,  # А) 1440
                "difficulty": "medium",
            },
            {
                "question": "Яка найвища гора у світі?",
                "options": ["А) К2", "Б) Канченджанга", "В) Еверест", "Г) Лхоцзе"],
                "correct": 2,  # В) Еверест
                "difficulty": "easy",
            },
            {
                "question": "У якому році закінчилася Друга світова війна?",
                "options": ["А) 1944", "Б) 1945", "В) 1946", "Г) 1943"],
                "correct": 1,  # Б) 1945
                "difficulty": "easy",
            },
            {
                "question": "Який газ складає найбільшу частину атмосфери Землі?",
                "options": ["А) Кисень", "Б) Азот", "В) Вуглекислий газ", "Г) Аргон"],
                "correct": 1,  # Б) Азот
                "difficulty": "medium",
            },
            {
                "question": "Хто винайшов телефон?",
                "options": [
                    "А) Томас Едісон",
                    "Б) Нікола Тесла",
                    "В) Александер Белл",
                    "Г) Гульєльмо Марконі",
                ],
                "correct": 2,  # В) Александер Белл
                "difficulty": "medium",
            },
            {
                "question": "Яка найдовша річка у світі?",
                "options": ["А) Амазонка", "Б) Ніл", "В) Янцзи", "Г) Міссісіпі"],
                "correct": 1,  # Б) Ніл
                "difficulty": "medium",
            },
        ]

        self.prize_levels = [
            100,
            200,
            300,
            500,
            1000,
            2000,
            4000,
            8000,
            16000,
            32000,
            64000,
            125000,
            250000,
            500000,
            1000000,
        ]

        self.current_question = 0
        self.current_prize = 0
        self.lifelines = {"50/50": True, "call_friend": True, "audience": True}

        self.statistics = {
            "games_played": 0,
            "questions_answered": 0,
            "correct_answers": 0,
            "total_winnings": 0,
        }

        self.load_statistics()

    def display_welcome(self):
        """Відображення привітального екрану"""
        print("=" * 60)
        print("🏆 ВІТАЄМО У ГРІ 'ХТО ХОЧЕ СТАТИ МІЛЬЙОНЕРОМ?' 🏆")
        print("=" * 60)
        print("Правила гри:")
        print("• Відповідайте на питання, вибираючи А, Б, В або Г")
        print("• У вас є 3 підказки: 50/50, Дзвінок другу, Допомога залу")
        print("• Ви можете забрати гроші на будь-якому етапі")
        print("• Неправильна відповідь - програш!")
        print("=" * 60)

    def display_question(self, question_data):
        """Відображення питання з варіантами відповідей"""
        print(
            f"\nПитання {self.current_question + 1} за {self.prize_levels[self.current_question]} грн:"
        )
        print("-" * 50)
        print(f"❓ {question_data['question']}")
        print()
        letters = ["А", "Б", "В", "Г"]
        for i, option in enumerate(question_data["options"]):
            print(f"  {letters[i]}) {option.split(')')[1].strip()}")
        print("-" * 50)

    def display_lifelines(self):
        """Відображення доступних підказок"""
        print("\n🆘 Доступні підказки:")
        lifeline_symbols = {
            "50/50": "✂️" if self.lifelines["50/50"] else "❌",
            "call_friend": "📞" if self.lifelines["call_friend"] else "❌",
            "audience": "👥" if self.lifelines["audience"] else "❌",
        }

        print(f"   1) {lifeline_symbols['50/50']} 50/50")
        print(f"   2) {lifeline_symbols['call_friend']} Дзвінок другу")
        print(f"   3) {lifeline_symbols['audience']} Допомога залу")

    def use_fifty_fifty(self, question_data):
        """Підказка 50/50 - залишає тільки 2 варіанти"""
        if not self.lifelines["50/50"]:
            print("❌ Ця підказка вже використана!")
            return question_data

        self.lifelines["50/50"] = False
        correct_answer = question_data["correct"]

        # Створюємо список індексів неправильних відповідей
        wrong_indices = [i for i in range(4) if i != correct_answer]

        # Випадково вибираємо 2 неправильні відповіді для видалення
        to_remove = random.sample(wrong_indices, 2)

        # Створюємо нову версію питання з видаленими варіантами
        new_options = []
        for i, option in enumerate(question_data["options"]):
            if i in to_remove:
                new_options.append("❌ ВИДАЛЕНО")
            else:
                new_options.append(option)

        modified_question = question_data.copy()
        modified_question["options"] = new_options

        print("✂️ Підказка 50/50 використана! Два неправильні варіанти видалено.")
        return modified_question

    def use_call_friend(self, question_data):
        """Підказка - дзвінок другу"""
        if not self.lifelines["call_friend"]:
            print("❌ Ця підказка вже використана!")
            return

        self.lifelines["call_friend"] = False

        # Друг має 70% шансів дати правильну відповідь
        if random.random() < 0.7:
            correct_letter = ["А", "Б", "В", "Г"][question_data["correct"]]
            print(
                f"📞 Ваш друг каже: 'Я думаю, що це відповідь {correct_letter}. Досить впевнений!'"
            )
        else:
            wrong_answers = [i for i in range(4) if i != question_data["correct"]]
            wrong_answer = random.choice(wrong_answers)
            wrong_letter = ["А", "Б", "В", "Г"][wrong_answer]
            print(
                f"📞 Ваш друг каже: 'Складне питання... Можливо {wrong_letter}? Не дуже впевнений.'"
            )

    def use_audience_help(self, question_data):
        """Підказка - допомога залу"""
        if not self.lifelines["audience"]:
            print("❌ Ця підказка вже використана!")
            return

        self.lifelines["audience"] = False

        correct_index = question_data["correct"]

        # Правильна відповідь отримує 50-75% голосів
        correct_percentage = random.randint(50, 75)

        # Розподіляємо решту голосів між трьома неправильними варіантами
        remaining = 100 - correct_percentage

        # Створюємо випадковий розподіл для неправильних відповідей
        wrong_percentages = []
        for i in range(2):  # Перші два неправильних варіанти
            # Кожен отримує від 1% до половини залишку
            max_for_this = min(remaining - (2 - i), remaining // 2)
            if max_for_this < 1:
                max_for_this = 1
            percentage = random.randint(1, max_for_this)
            wrong_percentages.append(percentage)
            remaining -= percentage

        # Останній неправильний варіант отримує все, що залишилося
        wrong_percentages.append(remaining)

        # Перемішуємо неправильні відсотки для випадковості
        random.shuffle(wrong_percentages)

        # Створюємо фінальний список відсотків
        percentages = [0, 0, 0, 0]
        percentages[correct_index] = correct_percentage

        # Розподіляємо неправильні відсотки
        wrong_index = 0
        for i in range(4):
            if i != correct_index:
                percentages[i] = wrong_percentages[wrong_index]
                wrong_index += 1

        print("👥 Результати опитування залу:")
        letters = ["А", "Б", "В", "Г"]
        for i, percentage in enumerate(percentages):
            chart_bar = "█" * (percentage // 5)  # Графічне представлення
            print(f"   {letters[i]}: {percentage:2d}% {chart_bar}")

    def get_user_choice(self):
        """Отримання вибору користувача"""
        while True:
            print("\n💡 Ваші дії:")
            print("   А, Б, В, Г - відповісти на питання")
            print("   П - використати підказку")
            print("   З - забрати гроші")

            choice = input("\nВаш вибір: ").upper().strip()

            if choice in ["А", "Б", "В", "Г", "П", "З"]:
                return choice
            else:
                print("❌ Неправильний вибір! Виберіть А, Б, В, Г, П або З")

    def handle_lifeline_choice(self, question_data):
        """Обробка вибору підказки"""
        self.display_lifelines()

        while True:
            choice = input("\nВиберіть підказку (1-3) або 0 для повернення: ").strip()

            if choice == "0":
                return question_data
            elif choice == "1":
                return self.use_fifty_fifty(question_data)
            elif choice == "2":
                self.use_call_friend(question_data)
                return question_data
            elif choice == "3":
                self.use_audience_help(question_data)
                return question_data
            else:
                print("❌ Неправильний вибір! Виберіть 1, 2, 3 або 0")

    def check_answer(self, user_answer, correct_answer):
        """Перевірка правильності відповіді"""
        answer_map = {"А": 0, "Б": 1, "В": 2, "Г": 3}
        user_index = answer_map.get(user_answer, -1)

        if user_index == correct_answer:
            return True
        return False

    def display_current_winnings(self):
        """Відображення поточних виграних грошей"""
        if self.current_question > 0:
            print(
                f"💰 Поточний виграш: {self.prize_levels[self.current_question - 1]} грн"
            )
        else:
            print("💰 Поточний виграш: 0 грн")

    def take_money(self):
        """Гравець забирає гроші"""
        if self.current_question == 0:
            print("💸 Ви не відповіли на жодне питання! Забирати нічого.")
            return 0

        winnings = self.prize_levels[self.current_question - 1]
        print(f"💰 Ви забираєте {winnings} грн! Дякуємо за гру!")
        return winnings

    def game_over(self, won=False, took_money=False):
        """Завершення гри"""
        if won:
            print("🎉🎉🎉 ВІТАЄМО! ВИ СТАЛИ МІЛЬЙОНЕРОМ! 🎉🎉🎉")
            winnings = 1000000
        elif took_money:
            # Гравець забрав гроші - виграш вже розрахований
            winnings = self.current_prize
        elif self.current_question == 0:
            print("😢 Гра закінчена! Ви не виграли нічого.")
            winnings = 0
        else:
            print(
                f"😢 Гра закінчена! Ви програли, але ваш виграш: {self.current_prize} грн"
            )
            winnings = self.current_prize

        # Оновлюємо статистику
        self.statistics["games_played"] += 1
        self.statistics["total_winnings"] += winnings
        self.save_statistics()

        return winnings

    def play_game(self):
        """Основний ігровий цикл"""
        self.display_welcome()

        # Перемішуємо питання для різноманітності
        random.shuffle(self.questions)

        while self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]

            print(f"\n{'=' * 60}")
            self.display_current_winnings()
            self.display_question(question_data)

            while True:
                user_choice = self.get_user_choice()

                if user_choice == "П":
                    # Використання підказки
                    question_data = self.handle_lifeline_choice(question_data)
                    self.display_question(question_data)
                    continue
                elif user_choice == "З":
                    # Забрати гроші
                    winnings = self.take_money()
                    self.current_prize = winnings
                    self.game_over(took_money=True)
                    return
                else:
                    # Відповідь на питання
                    break

            # Перевіряємо відповідь
            self.statistics["questions_answered"] += 1

            if self.check_answer(user_choice, question_data["correct"]):
                # Правильна відповідь
                self.statistics["correct_answers"] += 1
                self.current_prize = self.prize_levels[self.current_question]

                correct_letter = ["А", "Б", "В", "Г"][question_data["correct"]]
                print(f"✅ Правильно! Відповідь: {correct_letter}")
                print(f"💰 Ви виграли {self.current_prize} грн!")

                self.current_question += 1

                if self.current_question == len(self.questions):
                    # Гравець відповів на всі питання
                    self.game_over(won=True)
                    return

                input("\nНатисніть Enter для наступного питання...")

            else:
                # Неправильна відповідь
                correct_letter = ["А", "Б", "В", "Г"][question_data["correct"]]
                print(f"❌ Неправильно! Правильна відповідь: {correct_letter}")
                self.game_over(won=False)
                return

    def display_statistics(self):
        """Відображення статистики гри"""
        print("\n📊 СТАТИСТИКА ГРИ:")
        print("=" * 40)
        print(f"Зіграно ігор: {self.statistics['games_played']}")
        print(f"Питань відповіли: {self.statistics['questions_answered']}")
        print(f"Правильних відповідей: {self.statistics['correct_answers']}")

        if self.statistics["questions_answered"] > 0:
            accuracy = (
                self.statistics["correct_answers"]
                / self.statistics["questions_answered"]
            ) * 100
            print(f"Точність відповідей: {accuracy:.1f}%")

        print(f"Загальний виграш: {self.statistics['total_winnings']} грн")
        print("=" * 40)

    def save_statistics(self):
        """Збереження статистики в файл"""
        try:
            with open("game_stats.json", "w", encoding="utf-8") as f:
                json.dump(self.statistics, f, ensure_ascii=False, indent=2)
        except (IOError, OSError) as e:
            print(f"Помилка збереження статистики: {e}")

    def load_statistics(self):
        """Завантаження статистики з файлу"""
        try:
            if os.path.exists("game_stats.json"):
                with open("game_stats.json", "r", encoding="utf-8") as f:
                    self.statistics = json.load(f)
        except (IOError, OSError) as e:
            print(f"Помилка збереження статистики: {e}")


def main():
    """Головна функція програми"""
    # Створюємо один екземпляр гри для всієї сесії
    game = MillionaireGame()

    while True:
        print("\n" + "=" * 60)
        print("🏆 ХТО ХОЧЕ СТАТИ МІЛЬЙОНЕРОМ? 🏆")
        print("=" * 60)
        print("1. 🎮 Почати нову гру")
        print("2. 📊 Переглянути статистику")
        print("3. ❌ Вийти")

        choice = input("\nВаш вибір (1-3): ").strip()

        if choice == "1":
            # Створюємо новий екземпляр тільки для нової гри
            new_game = MillionaireGame()
            new_game.play_game()
            # Оновлюємо статистику в основному екземплярі
            game.load_statistics()
        elif choice == "2":
            game.display_statistics()
            input("\nНатисніть Enter для продовження...")
        elif choice == "3":
            print("\n👋 Дякуємо за гру! До зустрічі!")
            break
        else:
            print("❌ Неправильний вибір! Спробуйте ще раз.")


if __name__ == "__main__":
    main()
