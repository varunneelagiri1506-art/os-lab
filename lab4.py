def display(processes, ct):
    n = len(processes)

    total_wt = 0
    total_tat = 0

    print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
    print("------------------------------------------")

    for i in range(n):
        at = processes[i][1]
        bt = processes[i][2]

        tat = ct[i] - at
        wt = tat - bt

        total_tat += tat
        total_wt += wt

        print(
            f"{processes[i][0]}\t"
            f"{at}\t"
            f"{bt}\t"
            f"{ct[i]}\t"
            f"{tat}\t"
            f"{wt}"
        )

    print("------------------------------------------")
    print("Average Waiting Time:", round(total_wt / n, 2))
    print("Average Turnaround Time:", round(total_tat / n, 2))
