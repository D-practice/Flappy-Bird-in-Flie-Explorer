import os
import random
import time
import keyboard
import pyautogui as pyautogui
import shutil

files_per_row = 17
total = 153


class Bird:
    def __init__(self):
        self.x = 3 
        self.y = 2  
        self.y_velocity = 0  
        self.flapVelocity = -1.25
        self.gravity = 0.25  
        self.file_name = "C:/Users/HP/Desktop/Flappybird/bird.jpg"
        self.max_fall_velocity = 1.25
        self.previousFileNumber = 152

    def update(self):
        if self.y_velocity < self.max_fall_velocity:
            self.y_velocity += self.gravity
        self.y += self.y_velocity

    def flap(self):
        self.y_velocity = self.flapVelocity

    def update_file_save(self):
        new_file_number = convert_xy_to_single_number(self.x, round(self.y))
        print(self.y)

        if new_file_number == self.previousFileNumber:
            return
        if new_file_number >= 139 or new_file_number <= 3:
            return

        new_filename = f"{new_file_number}.jpg"
        text_file_to_delete = f"C:/Users/HP/Desktop/Flappybird/{new_file_number}.txt"
        text_file_to_create = f"C:/Users/HP/Desktop/Flappybird/{self.previousFileNumber}.txt"

        # Remove the old text file
        if os.path.exists(text_file_to_delete):
            os.remove(text_file_to_delete)

        # Recreate the new text file
        with open(text_file_to_create, 'w') as new_file:
            new_file.write('')

        os.rename(self.file_name, f"C:/Users/HP/Desktop/Flappybird/{new_file_number}.jpg")
        print(f"Renamed '{self.file_name}' to '{new_file_number}.jpg'")
        self.file_name = f"C:/Users/HP/Desktop/Flappybird/{new_file_number}.jpg"
        self.previousFileNumber = new_file_number

    def reset_file_name(self):
        os.rename(self.file_name, "C:/Users/HP/Desktop/Flappybird/bird.jpg")
        with open(f"C:/Users/HP/Desktop/Flappybird/{self.previousFileNumber}.txt", 'w') as new_file:
            new_file.write('')


class Pipe:
    def __init__(self):
        self.x = files_per_row - 1
        self.y = 0
        self.x_velocity = -0.5
        self.file_name = f"C:/Users/HP/Desktop/Flappybird/pipe0.png"
        self.previousFileNumber = 16
        self.all_new_file_number1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    def generate_pipe(self):
        self.y = random.randint(2, 6)
        print(self.y)
        for i in range(9):
            if i == self.y or i == self.y - 1 or i == self.y + 1:
                pass
            else:
                new_file_number = convert_xy_to_single_number(round(self.x), i)
                self.all_new_file_number1[i+9] = new_file_number
                print(self.all_new_file_number1)

    def dupe_and_rename_image(self):
        for i in range(9):
            if self.all_new_file_number1[((-1)*i)-1] == 0:
                pass
            else:
                text_file_to_delete = f"C:/Users/HP/Desktop/Flappybird/{self.all_new_file_number1[((-1)*i)-1]}.txt"
                if os.path.exists(text_file_to_delete):
                    os.remove(text_file_to_delete)
                new_name = f"{self.all_new_file_number1[((-1)*i)-1]}.png"
                duplicate_path = self.file_name + "_duplicate"
                shutil.copy(self.file_name, duplicate_path)
                print(f"Duplicated image to {duplicate_path}")

                # Rename the duplicated file
                new_path = os.path.join(os.path.dirname(self.file_name), new_name)
                os.rename(duplicate_path, new_path)
                print(f"Renamed duplicate to {new_path}")



    def update_file_save(self):
        if self.all_new_file_number1[0] == 0:
            for i in range(9):
                pic_to_delete = f"C:/Users/HP/Desktop/Flappybird/{self.all_new_file_number1[i]}.png"
                text_file_to_create = f"C:/Users/HP/Desktop/Flappybird/{self.all_new_file_number1[i]}.txt"
                if os.path.exists(pic_to_delete):
                    os.remove(pic_to_delete)
                    with open(text_file_to_create, 'w') as new_file:
                        new_file.write('')
            for i in range(9):
                self.all_new_file_number1[i] = self.all_new_file_number1[i+9]
                self.all_new_file_number1[i+9] = 0
        for i in range(18):
            if self.all_new_file_number1[i] == 0:
                pass
            else:
                new_name = f"{self.all_new_file_number1[i]}.png"
                new_path = os.path.join(os.path.dirname(self.file_name), new_name)
                #if new_file_number == self.previousFileNumber:
                    #return

                new_filename = f"{self.all_new_file_number1[i]}.png"
                text_file_to_delete = f"C:/Users/HP/Desktop/Flappybird/{self.all_new_file_number1[i] - 1}.txt"
                text_file_to_create = f"C:/Users/HP/Desktop/Flappybird/{self.all_new_file_number1[i]}.txt"

                # Remove the old text file
                if os.path.exists(text_file_to_delete):
                    os.remove(text_file_to_delete)

                # Recreate the new text file
                with open(text_file_to_create, 'w') as new_file:
                    new_file.write('')

                os.rename(new_path, f"C:/Users/HP/Desktop/Flappybird/{self.all_new_file_number1[i] - 1}.png")
                self.all_new_file_number1[i] -= 1

    def del_all_pipe(self):
        for i in range(153):
            pic_to_delete = f"C:/Users/HP/Desktop/Flappybird/{i}.png"
            if os.path.exists(pic_to_delete):
                os.remove(pic_to_delete)


def convert_xy_to_single_number(x, y):
    return y * files_per_row + x


pipe = Pipe()
bird = Bird()
time.sleep(2)

print("Press the space bar to flap the bird...")
pipe.generate_pipe()
pipe.dupe_and_rename_image()
for i in range(3):
    for i in range(13):
        if keyboard.is_pressed('space'):
            bird.flap()
            print("Flap!")

        bird.update()
        bird.update_file_save()
        pipe.update_file_save()
        time.sleep(0.2)
        pyautogui.press('f5')  # Simulate a refresh (or whatever this is for)
        time.sleep(0.2)
    pipe.generate_pipe()
    pipe.dupe_and_rename_image()

bird.reset_file_name()
pipe.del_all_pipe()


# Define the folder name
folder_name = 'C:/Users/HP/Desktop/Flappybird'

# Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Create 152 .txt files
for i in range(153):
    file_name = f"{i}.txt"
    file_path = os.path.join(folder_name, file_name)

    # Create the file
    with open(file_path, 'w') as file:
        file.write('')  # You can write something inside the file if needed
