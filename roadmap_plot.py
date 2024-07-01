import matplotlib.pyplot as plt
from read_data import read_data

def plot_data(data):
    plt.figure(figsize=(10, 6))

    for company, milestones in data.items():
        years = [year for year, _ in milestones]
        qubits = [qubits for _, qubits in milestones]
        plt.plot(years, qubits, marker='o', label=company)

    plt.yscale('log')
    plt.xlabel('Year')
    plt.ylabel('Number of Qubits')
    plt.title('Qubit Roadmap by Company')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()

def main():
    data = read_data('structured_data.txt')
    plot_data(data)

if __name__ == "__main__":
    main()