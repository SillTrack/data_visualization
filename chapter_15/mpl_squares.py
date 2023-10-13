import matplotlib.pyplot as plt

if __name__ == "__main__":
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    # print(plt.style.available)
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(input_values, squares, linewidth=3)

    # Назначение заголовка и меток осей
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Square of Value", fontsize=14)
    ax.set_ylabel("Value", fontsize=14)

    ax.tick_params(axis="both", labelsize=14)

    plt.show()