def calculate_forecast():
    try:
        global data
        N = int(entry_years.get())
        window_size = int(entry_window.get())

        def moving_average(data, window_size):
            return data.rolling(window=window_size).mean()

        # Построение графиков с прогнозом
        fig, axs = plt.subplots(2, 1, figsize=(8, 10))  # Увеличиваем размер графика

        # График числа браков с прогнозом
        axs[0].plot(original_data['Year'], original_data['Marriages'], marker='o', label='Браки (факт)', color='b')
        axs[0].plot(forecast_data['Year'], forecast_data['Marriages'], linestyle='--', label='Браки (прогноз)', color='g')
        axs[0].set_xlabel('Год')
        axs[0].set_ylabel('Количество браков')

        # График числа разводов с прогнозом
        axs[1].plot(original_data['Year'], original_data['Divorces'] / 1000, marker='o', label='Разводы (факт)', color='r')
        axs[1].plot(forecast_data['Year'], forecast_data['Divorces'] / 1000, linestyle='--', label='Разводы (прогноз)', color='m')
        axs[1].set_xlabel('Год')
        axs[1].set_ylabel('Количество разводов (в тыс.)')  # Добавляем подпись "в тыс."

        # Установка шага оси x
        axs[0].xaxis.set_major_locator(plt.MultipleLocator(2))
        axs[1].xaxis.set_major_locator(plt.MultipleLocator(2))

        # Добавление заголовков и легенд
        axs[0].set_title('Количество браков по годам')
        axs[0].legend()
        axs[1].set_title('Количество разводов по годам')
        axs[1].legend()

        plt.tight_layout()

        # Отображение графиков в Tkinter
        for widget in frame_graph.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH, padx=2)

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось рассчитать прогноз: {e}")