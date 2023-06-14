{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d025fa01",
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "attempted relative import with no known parent package",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtyping\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Set\n\u001b[1;32m----> 2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01memployee\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Employee, Manager\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mexception\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m NoSuchMemberError\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mTeam\u001b[39;00m:\n",
      "\u001b[1;31mImportError\u001b[0m: attempted relative import with no known parent package"
     ]
    }
   ],
   "source": [
    "from typing import Set\n",
    "from .employee import Employee, Manager\n",
    "from .exception import NoSuchMemberError\n",
    "\n",
    "\n",
    "class Team:\n",
    "    \"\"\"\n",
    "    Класс - команда.\n",
    "    У каждой команды есть менеджер, название и участники.\n",
    "\n",
    "    Возможности:\n",
    "    - добавление участников\n",
    "    - удаление участника из команды\n",
    "    - просмотр базовой информации об участниках\n",
    "    - получение списка участников\n",
    "    \"\"\"\n",
    "\n",
    "    name: str\n",
    "    manager: Manager\n",
    "    __members: Set[Employee]\n",
    "\n",
    "    def __init__(self, name: str, manager: Manager):\n",
    "        \"\"\"\n",
    "        Задача:\n",
    "        Реализовать конструктор класса.\n",
    "        Конструктор должен присвоить значения публичным атрибутам\n",
    "        и инициализировать контейнер `__members`\n",
    "        \"\"\"\n",
    "\n",
    "        self.name = name\n",
    "        self.manager = manager\n",
    "        self.__members = set()\n",
    "\n",
    "    def add_member(self, member: Employee) -> None:\n",
    "        \"\"\"\n",
    "        Задача: реализовать метод добавления участника в команду.\n",
    "        Добавить можно только работника.\n",
    "        \"\"\"\n",
    "\n",
    "        if isinstance(member, Employee):\n",
    "            self.__members.add(member)\n",
    "\n",
    "    def remove_member(self, member: Employee) -> None:\n",
    "        \"\"\"\n",
    "        Задача: реализовать метод удаления участника из команды.\n",
    "        Если в команде нет такого участника поднимается исключение `NoSuchMemberError`\n",
    "        \"\"\"\n",
    "\n",
    "        if member not in self.__members:\n",
    "            raise NoSuchMemberError(self.name, member)\n",
    "\n",
    "        self.__members.remove(member)\n",
    "\n",
    "    def get_members(self) -> Set[Employee]:\n",
    "        \"\"\"\n",
    "        Задача: реализовать метод возвращения списка участков команды та,\n",
    "        чтобы из вне нельзя было поменять список участников внутри класса\n",
    "        \"\"\"\n",
    "\n",
    "        return self.__members.copy()\n",
    "\n",
    "    def show(self) -> None:\n",
    "        \"\"\"\n",
    "        DO NOT EDIT!\n",
    "        Данный метод нельзя редактировать!\n",
    "\n",
    "        Метод показывает информацию о команде в формате:\n",
    "        `'team: {team_name} manager: {manager_name} number of members: {members_count)}'`\n",
    "\n",
    "        Задача: доработать класс таким образом, чтобы метод выполнял свою функцию, не меняя содержимое\n",
    "        этого метода\n",
    "        \"\"\"\n",
    "        print(self)\n",
    "\n",
    "    def __str__(self):\n",
    "        \"\"\"\n",
    "        Задача: реализовать строковое представление объекта команды.\n",
    "        \"\"\"\n",
    "\n",
    "        members_count = len(self.__members)\n",
    "        return f\"team: {self.name} manager: {self.manager.name} number of members: {members_count}\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
