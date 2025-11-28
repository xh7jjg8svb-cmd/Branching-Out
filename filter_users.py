import json


def filter_users_by_name(name):
    """Filter users list by name (case-insensitive)."""
    with open("users.json", "r") as file:
        users_list = json.load(file)

    filtered_users = [user for user in users_list if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_email(domain):
    """Filter users list by email domain."""
    with open("users.json", "r") as file:
        users_list = json.load(file)

    filtered_users = [user for user in users_list if user["email"].endswith(domain)]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name/email): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "email":
        email_domain = input("Enter an email domain to filter users (e.g., example.com): ").strip()
        filter_users_by_email(email_domain)
    else:
        print("Filtering by that option is not yet supported.")
