# Создание основного окна
root = tk.Tk()
root.title("Статистика браков и разводов")

# Создание рамки для ввода параметров
frame_input = tk.Frame(root)
frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="n")

tk.Label(frame_input, text="Количество лет для прогноза:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_years = tk.Entry(frame_input)
entry_years.grid(row=0, column=1, padx=5, pady=5, sticky="w")

tk.Label(frame_input, text="Размер окна для скользящей средней:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_window = tk.Entry(frame_input)
entry_window.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Кнопки для загрузки данных и выполнения расчета
button_load = tk.Button(frame_input, text="Загрузить данные", command=load_data)
button_load.grid(row=2, column=0, padx=5, pady=5, sticky="w")

button_calculate = tk.Button(frame_input, text="Рассчитать прогноз", command=calculate_forecast)
button_calculate.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Создание рамки для таблицы данных
frame_table = tk.Frame(root)
frame_table.grid(row=1, column=0, padx=10, pady=10, sticky="n")

# Создание таблицы данных
columns = ['Год', 'Возраст брака м', 'Возраст брака ж', 'Возраст развода м', 'Возраст развода ж', 'Кол-во браков', 'Кол-во разводов']
tree = ttk.Treeview(frame_table, columns=columns, show='headings', height=15)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=110)
tree.pack(expand=True, fill=tk.BOTH)

# Создание текстового поля для возрастной статистики
text_stats = tk.Text(frame_table, height=6, wrap=tk.WORD)
text_stats.pack(expand=True, fill=tk.BOTH, pady=10)

# Создание рамки для отображения графиков
frame_graph = tk.Frame(root)
frame_graph.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

# Запуск основного цикла Tkinter
root.mainloop()
