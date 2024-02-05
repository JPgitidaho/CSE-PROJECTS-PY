import csv

YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9


def main():
    try:
        # Prompt the user to enter the name of the file
        filename = input("Name of file that contains NHTSA data: ")
        with open(filename, "rt") as text_file:
            # Prompt the user to enter the percentage reduction
            perc_reduc = float(
                input("Percent reduction of texting while driving [0, 100]: "))

            if perc_reduc < 0 or perc_reduc > 100:
                print(
                    "Error: Invalid percentage value. Please enter a value between 0 and 100.")
                return

            print()
            # Print the purpose of the output
            print(f"With a {perc_reduc}% reduction in using a cell",
                  "phone while driving, approximately the",
                  "following number of injuries and deaths",
                  "would have been prevented in the USA.", sep="\n")
            print()
            # Print the header of the output table
            print("Year, Injuries, Deaths")

            reader = csv.reader(text_file)
            next(reader)

            for row in reader:
                # Extract the year from the row
                year = row[YEAR_COLUMN]

                try:
                    # Calculate the estimated reduction in injuries and deaths
                    injur, fatal = estimate_reduction(
                        row, PHONE_COLUMN, perc_reduc)

                    # Print the year, injuries, and deaths in a formatted string
                    print(year, injur, fatal, sep=", ")
                except ZeroDivisionError:
                    # Handle the case of zero fatal crashes
                    print(
                        f"Zero division error occurred for year {year}. Skipping the calculation.")

    except FileNotFoundError:
        # Handle file not found error
        print(f"[Errno 2] No such file or directory: '{filename}'")
        print("Please choose a different file.")

    except PermissionError:
        # Handle permission denied error
        print(f"[Errno 13] Permission denied: '{filename}'")
        print("Please choose a different file.")

    except csv.Error:
        # Handle invalid CSV file format
        print("Error: Invalid CSV file format.")


def estimate_reduction(row, behavior_key, perc_reduc):
    # Extract behavior and fatal crashes values from the row
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])

    if fatal_crashes == 0:
        # Raise an exception for zero fatal crashes
        raise ZeroDivisionError

    # Calculate the reduction ratio
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    # Extract fatalities and injuries values from the row
    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    # Calculate the reduced fatalities and injuries
    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal


if __name__ == "__main__":
    main()
