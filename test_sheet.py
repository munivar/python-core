import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Define the scope
scopes = [
    # "https://www.googleapis.com/auth/spreadsheets",
    # "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file",
]


# Add your credentials to the account
cred = Credentials.from_service_account_file("gcloud_cred.json", scopes=scopes)

service = build("drive", "v3", credentials=cred)

file_id = "1TuAe3vRxRHNDavd1DNSo9R9cHlFPhWP8"
file_name = "screenshot.png"

# File metadata and file path
media = MediaFileUpload(file_name, resumable=True)

file_metadata = {"name": file_name, "parents": [file_id]}

# Upload the file
uploaded_file = service.files().create(body=file_metadata, media_body=media).execute()
file_id = uploaded_file.get("id")

print("file_id =>", str(file_id))


# Define the scope
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    # "https://www.googleapis.com/auth/drive",
]

# Add your credentials to the account
cred = Credentials.from_service_account_file("gcloud_cred.json", scopes=scopes)

# Authorize the clientsheet
client = gspread.authorize(cred)

# Get the instance of the Spreadsheet
sheet_id = "1V3CGH3ACZbWHY65KOCstC54JJEf3YTMeqYzoYj6EBP8"
main_sheet = client.open_by_key(sheet_id)

# Get all worksheets
worksheet_list = main_sheet.worksheets()
print(worksheet_list)

# Get the first sheet of the Spreadsheet
# sh = main_sheet.sheet1
# print(sh)


# def user_exists(uid):
#     """Check if a user with the given uid exists in the sheet."""
#     data = sh.get_all_records()
#     for row in data:
#         if row["uid"] == uid:
#             return True
#     return False


# def add_user(user_data):
#     """Add a new user to the sheet if they do not already exist."""
#     uid = user_data[0]
#     if user_exists(uid):
#         print(f"User with uid {uid} already exists.")
#     else:
#         # without JSON Serialization
#         sh.append_row(user_data)
#         print(f"Added new user with uid {uid}.")


# # Example user data
# user_data = [
#     515741,
#     "Vishal",
#     "Dabhi",
#     "vishaldabhi@gmail.com",
#     datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
#     datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
# ]

# # Add the user
# add_user(user_data)


# //////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

# Get the sheet of the Spreadsheet
# sh = main_sheet.worksheet("users")
# print(sh)


# def user_exists(uid):
#     """Check if a user with the given uid exists in the sheet."""
#     data = sh.get_all_records()
#     for row in data:
#         if row["uid"] == uid:
#             return True
#     return False


# def add_user(user_data):
#     """Add a new user to the sheet if they do not already exist."""
#     uid = user_data["uid"]
#     if user_exists(uid):
#         print(f"User with uid {uid} already exists.")
#     else:
#         # wit JSON Serialization
#         row = [
#             user_data["uid"],
#             user_data["first_name"],
#             user_data["last_name"],
#             user_data["email"],
#             user_data["created_at"],
#             user_data["updated_at"],
#         ]
#         sh.append_row(row)
#         # without JSON Serialization
#         # sh.append_row(user_data)
#         print(f"Added new user with uid {uid}.")


# user_data = {
#     "uid": 515741,
#     "first_name": "Vishal",
#     "last_name": "Dabhi",
#     "email": "vishaldabhi@gmail.com",
#     "created_at": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
#     "updated_at": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
# }

# # Add the user
# add_user(user_data)


# def update_user(user_data):
#     """Update all fields for the user with the given uid."""
#     uid = user_data["uid"]
#     data = sh.get_all_records()

#     # Find the row number where the uid is located
#     for idx, row in enumerate(data):
#         if row["uid"] == uid:
#             row_number = idx + 2  # Adding 2 to account for header row and 1-based index
#             break
#     else:
#         print(f"User with uid {uid} not found.")
#         return

#     # Update all fields
#     column_names = list(
#         data[0].keys()
#     )  # Get the column names from the first row of data
#     for i, column_name in enumerate(
#         column_names, start=1
#     ):  # start=1 for 1-based indexing
#         sh.update_cell(row_number, i, user_data[column_name])
#     print(f"Updated user with uid {uid}.")


# # Example user data
# user_data = {
#     "uid": 515741,
#     "first_name": "UpdatedFirstName",
#     "last_name": "UpdatedLastName",
#     "email": "updatedemail@gmail.com",
#     "created_at": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
#     "updated_at": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
# }

# # Update the user
# update_user(user_data)


# def delete_user(uid):
#     """Delete the user with the given uid."""
#     data = sh.get_all_records()

#     # Find the row number where the uid is located
#     for idx, row in enumerate(data):
#         if row["uid"] == uid:
#             row_number = idx + 2  # Adding 2 to account for header row and 1-based index
#             break
#     else:
#         print(f"User with uid {uid} not found.")
#         return

#     # Delete the row
#     sh.delete_rows(row_number)
#     print(f"Deleted user with uid {uid}.")


# # Example usage
# uid_to_delete = 515741

# # Delete the user
# delete_user(uid_to_delete)


# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////
