
from astra_agent import initialize_kernel

def main():
    kernel = initialize_kernel()
    result = kernel.skills["journal"].save_journal_entry("natalia", "April 26, 2025", "Today I tested the ASTRA Pro agent and it worked beautifully.")
    print(result)

if __name__ == "__main__":
    main()
