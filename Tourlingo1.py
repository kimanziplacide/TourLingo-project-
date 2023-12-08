
    # Method to update translations completed for a user
    def update_translations_completed(self, user_id):
        try:
            cursor = self.db_connection.cursor()
            query_update = "UPDATE user_progress SET translations_completed = translations_completed + 1 WHERE id = %s"
            values_update = (user_id,)
            cursor.execute(query_update, values_update)
            self.db_connection.commit()
            cursor.close()
            self.print_visual_border()
            print("Translations completed!")
            self.print_visual_border()
        except Error as e:
            print(f"Error updating translations completed: {e}")

    # Method to get user's progress
    def get_user_progress(self, user_id):
        try:
            cursor = self.db_connection.cursor()
            query_select = "SELECT translations_completed FROM user_progress WHERE id = %s"
            values_select = (user_id,)
            cursor.execute(query_select, values_select)
            progress_row = cursor.fetchone()

            if progress_row is not None:
                current_translations_completed = progress_row[0]
                cursor.close()
                return current_translations_completed
            else:
                self.print_visual_border()
                print("No progress found.")
                self.print_visual_border()
                cursor.close()
                return 0  # Default progress assumed to be 0 if no data found
        except Error as e:
            print(f"Error getting user progress: {e}")
            return None

    # Method to log in a user
    def login(self):
        username_to_authenticate = input("Enter your username for authentication: ")
        password_to_authenticate = input("Enter your password for authentication: ")
        authenticated_user_id = self.authenticate_user(username_to_authenticate, password_to_authenticate)

        if authenticated_user_id is not None:
            self.print_visual_border()
            print("Login successful!")
            self.print_visual_border()
            self.current_user = username_to_authenticate
            self.current_user_id = authenticated_user_id
        else:
            self.print_visual_border()
            print("Authentication failed. Check your credentials.")
            self.print_visual_border()

    # Method to translate text for a logged-in user
    def translate_text(self):
        if not self.current_user:
            pint("You need to log in first.")
            

       

       
           
                
                
                
                
            
              


