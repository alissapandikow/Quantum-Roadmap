import matplotlib.pyplot as plt

def read_data(filename):
    with open(filename, 'r') as file:
        data = file.read().splitlines()
    
    milestones = {}
    for line in data:
        if line:
            key, value = line.split(':')
            milestones[key.strip()] = eval(value.strip())
    
    return milestones

def plot_roadmap(milestones):
    plt.figure(figsize=(10, 8))
    
    for company, milestone in milestones.items():
        years, qubits = zip(*milestone)
        plt.plot(years, qubits, marker='o', label=company)
    
    plt.xlabel('Year')
    plt.ylabel('Qubits')
    plt.title('Quantum Computing Roadmap')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.show()

def main():
    data = read_data('data.txt')
    plot_roadmap(data)

if __name__ == '__main__':
    main()
