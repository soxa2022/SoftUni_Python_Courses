from library import Library
from user import User


class Registration:

    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return "We could not find such user to remove!"
        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):

        try:
            update_user = next(filter(lambda x: x.user_id == user_id, library.user_records))

        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if new_username == update_user.username:
            return "Please check again the provided username - it should be different than the username used so far!"

        if update_user.username in library.rented_books:
            library.rented_books[new_username] = library.rented_books.pop(update_user.username)

        update_user.username = new_username

        return f"Username successfully changed to: {new_username} for user id: {user_id}"
