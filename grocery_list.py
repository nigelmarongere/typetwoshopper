import sqlite3

groceries = [
  "Artichoke",
  "Asparagus",
  "Aubergine",
  "Beansprouts",
  "Broad beans",
  "Broccoli",
  "Brussels sprouts",
  "Cabbage",
  "Carrots",
  "Cauliflower",
  "Cavolo Nero",
  "Celeraic",
  "Celery",
  "Courgette",
  "Cucumber",
  "Fennel",
  "Gherkins",
  "Green beans",
  "Lecks",
  "Lettuce",
  "Mange tout",
  "Marrow",
  "Mushrooms",
  "Okra",
  "Onions",
  "Pak choi",
  "Pea shoots",
  "Peppers",
  "Radishes",
  "Rocket",
  "Samphire",
  "Super snap peas",
  "Sauerkraut",
  "Shallots",
  "Spinich",
  "Spring greens",
  "Spring onions",
  "Squash",
  "Swede",
  "Tomatoes",
  "Turnip",
  "Watercress"
]

groceries = sorted(groceries)

connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()

cursor.execute("create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(groceries)):
  cursor.execute("insert into groceries (name) values (?)",[groceries[i]])
  print("added ", groceries[i])

connection.commit()
connection.close()