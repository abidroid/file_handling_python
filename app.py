# Define the file name
file_name = "employees.txt"

def update_employee_status(name, new_status):
    try:
        # Read the content of the file
        with open(file_name, "r") as file:
            lines = file.readlines()

        # Variable to track if the employee was found
        employee_found = False

        # Open the file again in write mode to update content
        with open(file_name, "w") as file:
            for line in lines:
                # Split the line into name and status
                employee_data = line.strip().split(", ")
                if employee_data[0] == name:
                    employee_found = True
                    # Check the current status
                    current_status = employee_data[1]
                    if current_status == new_status:
                        print(f"{name} is already {new_status}.")
                    else:
                        print(f"Updating {name}'s status to {new_status}.")
                        line = f"{name}, {new_status}\n"  # Update the status
                file.write(line)  # Write the line back to the file

        # If the employee was not found
        if not employee_found:
            print("Employee not found.")

    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

# Input the employee's name and new status
employee_name = input("Enter the employee's name: ").strip()
new_status = input("Enter the new status (Active/Inactive): ").strip()

# Call the function
update_employee_status(employee_name, new_status)
